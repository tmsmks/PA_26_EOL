"""Scoring v2 : passages de chapitre, règle d'espacement, chapitre rejoué seul,
niveaux affichés et reprise des données v1."""
import json
import re
from datetime import timedelta

import pytest

from app import create_app
from repositories.orm import (
    ROLE_TRAINER,
    STATUS_COMPLETED,
    BookSession,
    ChapterPassage,
    SceneAttempt,
    utcnow,
)
from repositories.users import UserRepository
from services.auth_service import hash_password
from services.scoring_upgrade import upgrade_scoring


def _scene(critical=False):
    """1 → (EM+2 → 2 | EM-1 → fin) ; 2 → (RD+1 → fin | RD-2 → fin).

    `critical` : la réponse RD+1 est marquée critique dans la clé (pour tester le
    plafond, elle reste la meilleure en points)."""
    def resp(next_id, text=None, **scores):
        return {"Id": 1, "Text": text or f"vers {next_id}", "NextInteractionID": next_id, "SoftSkillDimensions": scores}

    best = resp(-1, "Promettre le secret", RespectAndDignity=1)
    if critical:
        best.update(Critical=True, Rationale="Promettre le secret empêche de chercher de l'aide.")
    return {
        "Id": 1,
        "Title": "Scène",
        "Interactions": [
            {"Id": 1, "Text": "Bonjour", "Actor": {"Name": "Mme A"}, "Responses": [
                resp(2, Empathy=2), resp(-1, Empathy=-1)]},
            {"Id": 2, "Text": "Et alors ?", "Actor": {"Name": "Mme A"}, "Responses": [
                best, resp(-1, RespectAndDignity=-2)]},
        ],
    }


def _make_app(tmp_path, critical=False):
    book = {"Chapters": [
        {"Id": 1, "Name": "Un", "Intro": "", "Scenes": [_scene(critical)]},
        {"Id": 2, "Name": "Deux", "Intro": "", "Scenes": [_scene()]},
    ]}
    (tmp_path / "chapter.json").write_text(json.dumps(book), encoding="utf-8")
    return create_app({
        "TESTING": True,
        "SECRET_KEY": "test",
        "DATABASE_URL": "sqlite:///" + str(tmp_path / "test.db"),
        "CHAPTERS_BASE_DIR": str(tmp_path),
        "CSRF_ENABLED": False,
    })


@pytest.fixture()
def app(tmp_path):
    return _make_app(tmp_path)


@pytest.fixture()
def alice(app):
    c = app.test_client()
    c.post("/register", data={
        "username": "alice", "display_name": "Alice",
        "password": "motdepasse1", "password_confirm": "motdepasse1",
    })
    return c


def _session(client):
    return client.post("/api/play/end_of_life/session").get_json()["session"]


def _play_chapter(client, sess, chapter_id, choices, flags=None, times=None):
    """Joue un chapitre comme le navigateur : ouvre le passage, joue, clôt."""
    passage = client.post(sess["urls"]["passages"], json={"chapter_id": chapter_id}).get_json()["passage"]
    r = client.post(sess["urls"]["attempts"], json={
        "chapter_id": chapter_id, "scene_id": 1, "entry_id": 1, "choices": list(choices),
        "flags": flags if flags is not None else passage["flags"] + [f"vu_{chapter_id}"],
        "passage_id": passage["id"],
        "times": times if times is not None else [6000] * len(choices),
    })
    assert r.status_code == 200, r.get_json()
    done = client.post(sess["urls"]["complete"], json={"chapter_id": chapter_id}).get_json()
    return passage, done


def _age_passages(app, days):
    """Antidate tous les passages terminés (simule le temps qui passe)."""
    with app.app_context():
        from repositories.database import db_session
        db = db_session()
        for p in db.query(ChapterPassage).all():
            p.started_at = p.started_at - timedelta(days=days)
            if p.completed_at:
                p.completed_at = p.completed_at - timedelta(days=days)
        db.commit()


def test_a_completed_chapter_is_scored_without_finishing_the_book(alice):
    sess = _session(alice)
    passage, done = _play_chapter(alice, sess, 1, [0, 1])
    assert passage["counted"] is True
    assert done["book_completed"] is False
    assert done["passage"]["global"] == 50.0  # (3 + 0) / (3 + 3)
    assert done["progress"]["level"] == 50.0 and done["progress"]["n_passages"] == 1
    assert done["progress"]["progression"] is None


def test_replaying_at_once_is_practice_then_counts_after_the_delay(app, alice):
    s1 = _session(alice)
    _play_chapter(alice, s1, 1, [1])
    _play_chapter(alice, s1, 2, [1])  # livre terminé : la session suivante est neuve

    s2 = _session(alice)
    assert s2["number"] == 2
    page = alice.get("/play/end_of_life/chapters/1").get_data(as_text=True)
    assert "Passage d'entraînement" in page
    practice, done = _play_chapter(alice, s2, 1, [0, 0])
    assert practice["counted"] is False
    assert done["passage"]["global"] == 100.0
    assert done["progress"]["n_passages"] == 1 and done["progress"]["level"] == 0.0

    _age_passages(app, 8)
    assert "Ce passage comptera" in alice.get("/play/end_of_life/chapters/1").get_data(as_text=True)
    counted, done = _play_chapter(alice, s2, 1, [0, 0])
    assert counted["counted"] is True
    progress = done["progress"]
    assert progress["n_passages"] == 2
    # Poids selon l'âge : le passage d'il y a 8 jours pèse 2^(−8/90), l'actuel 1.
    assert progress["level"] == round(100 / (1 + 2 ** (-8 / 90)), 1)
    assert progress["gain"] == 100.0
    assert progress["progression"] == progress["level"]  # parti de 0 : tout ce qui restait


def test_a_scene_replayed_in_a_passage_is_not_scored_twice(alice):
    sess = _session(alice)
    passage = alice.post(sess["urls"]["passages"], json={"chapter_id": 1}).get_json()["passage"]
    body = {"chapter_id": 1, "scene_id": 1, "entry_id": 1, "passage_id": passage["id"]}
    first = alice.post(sess["urls"]["attempts"], json={**body, "choices": [1]}).get_json()
    again = alice.post(sess["urls"]["attempts"], json={**body, "choices": [0, 0]}).get_json()
    assert (first["counted"], first["attempt_no"]) == (True, 1)
    assert (again["counted"], again["attempt_no"]) == (False, 2)
    done = alice.post(sess["urls"]["complete"], json={"chapter_id": 1}).get_json()
    assert done["passage"]["global"] == 0.0  # la 1ʳᵉ tentative fait foi
    # Reprendre le chapitre ouvre le même passage tant qu'il n'est pas clos.
    reopened = alice.post(sess["urls"]["passages"], json={"chapter_id": 2}).get_json()["passage"]
    assert alice.post(sess["urls"]["passages"], json={"chapter_id": 2}).get_json()["passage"]["id"] == reopened["id"]


def test_a_chapter_played_alone_restarts_from_its_previous_story_state(alice):
    s1 = _session(alice)
    _play_chapter(alice, s1, 1, [0, 0], flags=["vu_1", "secret_garde"])
    p2, _ = _play_chapter(alice, s1, 2, [0, 0])
    assert p2["flags"] == ["secret_garde", "vu_1"]  # l'histoire continue dans la session

    s2 = _session(alice)
    alone = alice.post(s2["urls"]["passages"], json={"chapter_id": 2}).get_json()["passage"]
    assert alone["flags"] == ["secret_garde", "vu_1"]  # repris du dernier passage du chapitre 2


def test_restart_deletes_the_session_passages(app, alice):
    sess = _session(alice)
    _play_chapter(alice, sess, 1, [0, 0])
    alice.post("/play/end_of_life/restart")
    with app.app_context():
        from repositories.database import db_session
        assert db_session().query(ChapterPassage).count() == 0


def test_levels_are_shown_to_the_player_and_the_trainer(app, alice):
    sess = _session(alice)
    _play_chapter(alice, sess, 1, [0, 1])
    history = alice.get("/me").get_data(as_text=True)
    assert "Note du livre" in history and "1<small> /2</small>" in history
    assert "/play/end_of_life/chapters/2" in history  # « Jouer → » le chapitre pas encore noté
    assert "niveau 50/100" in alice.get("/play/end_of_life/").get_data(as_text=True)

    with app.app_context():
        from repositories.database import db_session
        UserRepository(db_session()).create("trainer", "Formatrice", hash_password("motdepasse1"), ROLE_TRAINER)
    t = app.test_client()
    t.post("/login", data={"username": "trainer", "password": "motdepasse1"})
    dash = t.get("/trainer/?book=end_of_life").get_data(as_text=True)
    assert "Niveaux par chapitre" in dash
    row = re.search(r'Alice</a></td>(.*?)</tr>', dash, re.S).group(1)
    assert "50 <span class=\"muted\">(1)</span>" in row
    assert t.get("/trainer/?book=inconnu").status_code == 404


def test_upgrade_turns_v1_sessions_into_passages(app, alice):
    """Une session jouée avant le v2 : tentatives sans passage, traces sans bornes."""
    sess = _session(alice)
    _play_chapter(alice, sess, 1, [0, 1])
    _play_chapter(alice, sess, 2, [0, 0])
    with app.app_context():
        from repositories.database import db_session
        db = db_session()
        bs = db.get(BookSession, sess["id"])
        for p in list(bs.passages):
            db.delete(p)
        for a in db.query(SceneAttempt).all():
            a.trace = [{k: v for k, v in st.items() if k not in ("bounds", "total_bounds", "chance")}
                       for st in a.trace]
        bs.results = {"version": 1, "global": 61.0, "scores": {"Empathy": 70.0}}
        assert bs.status == STATUS_COMPLETED
        db.commit()

        stats = upgrade_scoring(db, app.extensions["eol_chapters"], 7)
        assert stats == {"passages": 2, "sessions": 1}
        db.expire_all()
        bs = db.get(BookSession, sess["id"])
        assert [(p.chapter_id, p.counted, p.results["global"]) for p in bs.passages] == [(1, True, 50.0), (2, True, 100.0)]
        assert bs.results["version"] == 2 and bs.results["global"] == 75.0
        assert bs.results["v1"]["global"] == 61.0
        assert all("bounds" in st for a in bs.attempts for st in a.trace)
        # Idempotente : rien à refaire au démarrage suivant.
        assert upgrade_scoring(db, app.extensions["eol_chapters"], 7) == {"passages": 0, "sessions": 0}


def test_passage_ids_are_checked(alice):
    s1 = _session(alice)
    p1 = alice.post(s1["urls"]["passages"], json={"chapter_id": 1}).get_json()["passage"]
    body = {"chapter_id": 2, "scene_id": 1, "entry_id": 1, "choices": [1], "passage_id": p1["id"]}
    assert alice.post(s1["urls"]["attempts"], json=body).status_code == 404
    assert alice.post(s1["urls"]["passages"], json={"chapter_id": 9}).status_code == 404
    assert alice.post(s1["urls"]["attempts"], json={**body, "passage_id": "x"}).status_code == 400


def test_response_times_are_kept_and_a_too_fast_passage_does_not_count(app, alice, monkeypatch):
    import services.scoring_service as scoring
    monkeypatch.setattr(scoring, "FAST_MIN_TIMED", 2)  # la scène de test n'a que 2 choix
    sess = _session(alice)
    passage, done = _play_chapter(alice, sess, 1, [0, 0], times=[300, 400])
    assert passage["counted"] is True
    assert done["passage"]["too_fast"] is True and done["passage"]["counted"] is False
    assert done["progress"] is None  # aucun passage compté
    with app.app_context():
        from repositories.database import db_session
        trace = db_session().query(SceneAttempt).first().trace
        assert [st["time_ms"] for st in trace] == [300, 400]

    # Le passage trop rapide ne bloque pas le délai : le suivant compte tout de suite.
    passage, done = _play_chapter(alice, sess, 1, [0, 0], times=[5000, 7000])
    assert passage["counted"] is True and done["passage"]["too_fast"] is False
    assert done["progress"]["n_passages"] == 1
    assert "dont 1 trop rapide" in alice.get("/me").get_data(as_text=True)


def test_malformed_response_times_are_ignored(alice):
    sess = _session(alice)
    _, done = _play_chapter(alice, sess, 1, [0, 0], times=["vite", None, 3])
    assert done["passage"]["counted"] is True and done["passage"]["timing"]["n_timed"] == 0


def test_a_critical_answer_caps_the_band_and_asks_for_a_debriefing(tmp_path):
    app = _make_app(tmp_path, critical=True)
    alice = app.test_client()
    alice.post("/register", data={
        "username": "alice", "display_name": "Alice",
        "password": "motdepasse1", "password_confirm": "motdepasse1",
    })
    sess = _session(alice)
    _, done = _play_chapter(alice, sess, 1, [0, 0])  # meilleure réponse en points, mais critique
    # Fin de chapitre, feedback d'abord : ce qu'il faut retenir (la réponse critique en tête).
    assert done["review"][0]["choice"]["critical"] is True
    assert done["review"][0]["scene_title"] == "Scène"
    assert set(done["trend"]) == {"strengths", "weaknesses"}
    progress = done["progress"]
    assert done["passage"]["n_critical"] == 1 and progress["level"] == 100.0
    assert progress["critical_capped"] and progress["band"]["label"] == "À consolider"
    history = alice.get("/me").get_data(as_text=True)
    assert "Réponses critiques à revoir" in history and "Promettre le secret" in history

    with app.app_context():
        from repositories.database import db_session
        UserRepository(db_session()).create("trainer", "Formatrice", hash_password("motdepasse1"), ROLE_TRAINER)
    t = app.test_client()
    t.post("/login", data={"username": "trainer", "password": "motdepasse1"})
    dash = t.get("/trainer/?book=end_of_life").get_data(as_text=True)
    assert "À débriefer" in dash and "Promettre le secret" in dash

    # Un passage compté suivant, sans réponse critique, lève le plafond.
    _age_passages(app, 8)
    _, done = _play_chapter(alice, sess, 1, [0, 1])
    assert done["progress"]["critical_capped"] is False
    assert "À débriefer" not in t.get("/trainer/?book=end_of_life").get_data(as_text=True)



def test_the_scoring_is_explained_before_playing(alice):
    page = alice.get("/notation").get_data(as_text=True)
    assert "Comment est-ce noté ?" in page and "7 jours" in page and "À consolider" in page
    assert "/notation" in alice.get("/play/end_of_life/chapters/1").get_data(as_text=True)


def test_the_trainer_sees_the_group_progress(app, alice):
    sess = _session(alice)
    _play_chapter(alice, sess, 1, [1])
    with app.app_context():
        from repositories.database import db_session
        UserRepository(db_session()).create("trainer", "Formatrice", hash_password("motdepasse1"), ROLE_TRAINER)
    t = app.test_client()
    t.post("/login", data={"username": "trainer", "password": "motdepasse1"})
    dash = t.get("/trainer/?book=end_of_life").get_data(as_text=True)
    assert "Progrès du groupe" in dash and "deux personnes ont rejoué" in dash
