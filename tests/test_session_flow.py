"""Parcours complet via le client Flask : comptes, sessions, bilan, droits."""
import json
import re

import pytest

from app import create_app
from repositories.orm import ROLE_TRAINER
from repositories.users import UserRepository
from services.auth_service import hash_password

FEEDBACK = {
    "summary": "Synthèse IA.",
    "strengths": [{"skill": "Empathy", "text": "Bien."}],
    "weaknesses": [{"skill": "RespectAndDignity", "text": "À revoir."}],
    "improvements": ["Demandez l'accord."],
    "chapters_to_rework": [{"chapter_id": 2, "reason": "Plus faible."}],
    "progression": "Mieux qu'avant.",
}


class FakeBackend:
    name = "fake"

    def __init__(self):
        self.prompts = []

    def complete_json(self, system_msg, user_msg):
        self.prompts.append(user_msg)
        return json.dumps(FEEDBACK)


def _scene():
    """1 → (EM+2 → 2 | EM-1 → fin) ; 2 → (RD+1 → fin | RD-2 → fin)."""
    def resp(next_id, **scores):
        return {"Id": 1, "Text": f"vers {next_id}", "NextInteractionID": next_id, "SoftSkillDimensions": scores}

    return {
        "Id": 1,
        "Title": "Scène",
        "Interactions": [
            {"Id": 1, "Text": "Bonjour", "Actor": {"Name": "Mme A"}, "Responses": [
                resp(2, Empathy=2), resp(-1, Empathy=-1)]},
            {"Id": 2, "Text": "Et alors ?", "Actor": {"Name": "Mme A"}, "Responses": [
                resp(-1, RespectAndDignity=1), resp(-1, RespectAndDignity=-2)]},
        ],
    }


@pytest.fixture()
def app(tmp_path):
    # Le livre « end_of_life » lit chapter.json : on le remplace par un mini-livre.
    book = {"Chapters": [
        {"Id": 1, "Name": "Un", "Intro": "", "Scenes": [_scene()]},
        {"Id": 2, "Name": "Deux", "Intro": "", "Scenes": [_scene()]},
    ]}
    (tmp_path / "chapter.json").write_text(json.dumps(book), encoding="utf-8")
    backend = FakeBackend()
    app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test",
        "DATABASE_URL": "sqlite:///" + str(tmp_path / "test.db"),
        "CHAPTERS_BASE_DIR": str(tmp_path),
        "CSRF_ENABLED": False,
        "FEEDBACK_BACKEND": backend,
    })
    app.fake_backend = backend
    return app


def _register(client, username="alice"):
    return client.post("/register", data={
        "username": username, "display_name": username.title(),
        "password": "motdepasse1", "password_confirm": "motdepasse1",
    })


def _play_book(client, choices_ch1=(0, 0), choices_ch2=(0, 0)):
    sess = client.post("/api/play/end_of_life/session").get_json()["session"]
    for chapter_id, choices in ((1, choices_ch1), (2, choices_ch2)):
        r = client.post(sess["urls"]["attempts"], json={
            "chapter_id": chapter_id, "scene_id": 1, "entry_id": 1,
            "choices": list(choices), "flags": ["vu_" + str(chapter_id)],
        })
        assert r.status_code == 200, r.get_json()
        done = client.post(sess["urls"]["complete"], json={"chapter_id": chapter_id}).get_json()
    return sess, done


def test_play_requires_login(app):
    r = app.test_client().get("/play/end_of_life/")
    assert r.status_code == 302 and "/login" in r.headers["Location"]
    assert app.test_client().post("/api/play/end_of_life/session").status_code == 401


def test_register_login_logout(app):
    c = app.test_client()
    assert _register(c).status_code == 302
    assert c.get("/me").status_code == 200
    c.post("/logout")
    assert c.get("/me").status_code == 302
    bad = c.post("/login", data={"username": "alice", "password": "faux-faux-faux"})
    assert bad.status_code == 401
    ok = c.post("/login", data={"username": "ALICE", "password": "motdepasse1", "next": "/me"})
    assert ok.status_code == 302 and ok.headers["Location"].endswith("/me")


def test_register_rejects_duplicates_and_open_redirects(app):
    c = app.test_client()
    _register(c)
    c.post("/logout")
    assert _register(c).status_code == 400
    r = c.post("/login", data={"username": "alice", "password": "motdepasse1", "next": "https://evil.example"})
    assert r.headers["Location"].endswith("/")


def test_full_book_session_report_and_feedback(app):
    c = app.test_client()
    _register(c)
    sess, done = _play_book(c)
    assert done["book_completed"] is True
    assert done["session"]["status"] == "completed"

    page = c.get(sess["urls"]["report"])
    assert page.status_code == 200
    assert "Bilan · Session 1" in page.get_data(as_text=True)

    fb = c.post(f"/api/sessions/{sess['id']}/feedback", json={}).get_json()["feedback"]
    assert fb["source"] == "ai" and fb["summary"] == "Synthèse IA."
    assert fb["progression"] is None  # première session
    # Le feedback est mis en cache : pas de 2ᵉ appel au LLM.
    c.post(f"/api/sessions/{sess['id']}/feedback", json={})
    assert len(app.fake_backend.prompts) == 1
    # Un participant ne peut pas régénérer un feedback IA réussi.
    r = c.post(f"/api/sessions/{sess['id']}/feedback", json={"regenerate": True})
    assert r.status_code == 403


def test_second_session_builds_on_the_first(app):
    c = app.test_client()
    _register(c)
    s1, _ = _play_book(c, choices_ch1=(1,), choices_ch2=(1,))
    c.post(f"/api/sessions/{s1['id']}/feedback", json={})
    s2, _ = _play_book(c)
    assert s2["number"] == 2 and s2["id"] != s1["id"]

    fb = c.post(f"/api/sessions/{s2['id']}/feedback", json={}).get_json()["feedback"]
    assert fb["progression"] == "Mieux qu'avant."
    prompt = app.fake_backend.prompts[-1]
    assert "SESSIONS PRÉCÉDENTES" in prompt and "Session 1" in prompt

    history = c.get("/me").get_data(as_text=True)
    # La 2ᵉ session rejoue les chapitres tout de suite : entraînement, non noté.
    assert "Session 2" in history and "+ 2 d'entraînement" in history


def test_only_first_attempt_counts(app):
    c = app.test_client()
    _register(c)
    sess = c.post("/api/play/end_of_life/session").get_json()["session"]
    url = sess["urls"]["attempts"]
    first = c.post(url, json={"chapter_id": 1, "scene_id": 1, "entry_id": 1, "choices": [1]}).get_json()
    again = c.post(url, json={"chapter_id": 1, "scene_id": 1, "entry_id": 1, "choices": [0, 0]}).get_json()
    assert first == {"counted": True, "attempt_no": 1}
    assert again == {"counted": False, "attempt_no": 2}


def test_server_rejects_impossible_paths(app):
    c = app.test_client()
    _register(c)
    sess = c.post("/api/play/end_of_life/session").get_json()["session"]
    r = c.post(sess["urls"]["attempts"], json={"chapter_id": 1, "scene_id": 1, "entry_id": 1, "choices": [0]})
    assert r.status_code == 400
    r = c.post(sess["urls"]["attempts"], json={"chapter_id": 9, "scene_id": 1, "entry_id": 1, "choices": [1]})
    assert r.status_code == 404


def test_sessions_are_private_but_visible_to_trainers(app):
    alice = app.test_client()
    _register(alice)
    sess, _ = _play_book(alice)

    bob = app.test_client()
    _register(bob, "bob")
    assert bob.get(sess["urls"]["report"]).status_code == 403
    assert bob.post(sess["urls"]["attempts"], json={}).status_code in (400, 403)
    assert bob.get("/trainer/").status_code == 403
    assert bob.get("/books/end_of_life/").status_code == 403
    assert bob.post("/api/save", json={}).status_code == 403

    with app.app_context():
        from repositories.database import db_session
        users = UserRepository(db_session())
        users.create("trainer", "Formatrice", hash_password("motdepasse1"), ROLE_TRAINER)
    t = app.test_client()
    t.post("/login", data={"username": "trainer", "password": "motdepasse1"})
    assert t.get(sess["urls"]["report"]).status_code == 200
    dash = t.get("/trainer/").get_data(as_text=True)
    assert "Alice" in dash and "Bob" in dash
    alice_id = int(re.search(r"/trainer/participants/(\d+)\">Alice", dash).group(1))
    assert t.post(f"/trainer/participants/{alice_id}/password", data={"password": "nouveau-mdp"}).status_code == 302
    alice.post("/logout")
    assert alice.post("/login", data={"username": "alice", "password": "nouveau-mdp"}).status_code == 302


def test_restart_discards_in_progress_session(app):
    c = app.test_client()
    _register(c)
    first = c.post("/api/play/end_of_life/session").get_json()["session"]
    attempt = {"chapter_id": 1, "scene_id": 1, "entry_id": 1, "choices": [1]}
    c.post(first["urls"]["attempts"], json=attempt)
    c.post(first["urls"]["complete"], json={"chapter_id": 1})
    c.post("/play/end_of_life/restart")
    second = c.post("/api/play/end_of_life/session").get_json()["session"]
    assert second["number"] == 1 and second["completed_chapters"] == []
    # Les tentatives de la session abandonnée ont disparu : la scène recompte.
    assert c.post(second["urls"]["attempts"], json=attempt).get_json()["counted"] is True


def test_csrf_blocks_forged_posts(tmp_path):
    app = create_app({
        "TESTING": True, "SECRET_KEY": "t",
        "DATABASE_URL": "sqlite:///" + str(tmp_path / "csrf.db"),
    })
    c = app.test_client()
    assert c.post("/register", data={"username": "eve"}).status_code == 400
    page = c.get("/register").get_data(as_text=True)
    token = re.search(r'name="csrf_token" value="([^"]+)"', page).group(1)
    r = c.post("/register", data={
        "csrf_token": token, "username": "eve", "password": "motdepasse1", "password_confirm": "motdepasse1",
    })
    assert r.status_code == 302
