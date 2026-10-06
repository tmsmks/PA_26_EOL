"""Export des données brutes (espace formateur) : Excel, CSV et JSON."""
import csv
import io
import json
import re
import zipfile
from datetime import datetime

import pytest
from openpyxl import load_workbook

from app import create_app
from repositories.orm import ROLE_TRAINER
from repositories.users import UserRepository
from services.auth_service import hash_password

TABLES = ["participants", "niveaux", "passages", "sessions", "chapitres", "scenes", "choix"]


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
    book = {"Chapters": [
        {"Id": 1, "Name": "Un", "Intro": "", "Scenes": [_scene()]},
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


def _register(client, username, display_name=None):
    client.post("/register", data={
        "username": username, "display_name": display_name or username.title(),
        "password": "motdepasse1", "password_confirm": "motdepasse1",
    })


def _attempt(client, sess, chapter_id, choices):
    r = client.post(sess["urls"]["attempts"], json={
        "chapter_id": chapter_id, "scene_id": 1, "entry_id": 1,
        "choices": choices, "flags": [f"vu_{chapter_id}"],
    })
    assert r.status_code == 200, r.get_json()


@pytest.fixture()
def played(app):
    """Alice : une session terminée (meilleurs choix), puis une session en cours
    (un chapitre rejoué tout de suite : passage d'entraînement, une scène jouée
    deux fois, chapitre pas terminé). Bob n'a pas joué."""
    alice = app.test_client()
    _register(alice, "alice")
    s1 = alice.post("/api/play/end_of_life/session").get_json()["session"]
    for chapter_id in (1, 2):
        _attempt(alice, s1, chapter_id, [0, 0])
        alice.post(s1["urls"]["complete"], json={"chapter_id": chapter_id})
    s2 = alice.post("/api/play/end_of_life/session").get_json()["session"]
    _attempt(alice, s2, 1, [1])
    _attempt(alice, s2, 1, [0, 1])  # rejouée : ne compte pas

    _register(app.test_client(), "bob")
    with app.app_context():
        from repositories.database import db_session
        UserRepository(db_session()).create("trainer", "Formatrice", hash_password("motdepasse1"), ROLE_TRAINER)
    trainer = app.test_client()
    trainer.post("/login", data={"username": "trainer", "password": "motdepasse1"})
    return {"alice": alice, "trainer": trainer, "s1": s1, "s2": s2}


def _json(client, query=""):
    r = client.get("/trainer/export?format=json" + query)
    assert r.status_code == 200, r.data[:200]
    return json.loads(r.data)


def test_export_is_reserved_to_trainers(app, played):
    assert played["alice"].get("/trainer/export").status_code == 403
    r = app.test_client().get("/trainer/export")
    assert r.status_code == 302 and "/login" in r.headers["Location"]


def test_xlsx_has_one_sheet_per_table(played):
    r = played["trainer"].get("/trainer/export?format=xlsx")
    assert r.status_code == 200
    assert r.mimetype == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert re.search(r'attachment; filename=eol_donnees_tous_livres_\d{4}-\d{2}-\d{2}\.xlsx',
                     r.headers["Content-Disposition"])
    assert r.headers["Cache-Control"] == "no-store"

    wb = load_workbook(io.BytesIO(r.data))
    assert wb.sheetnames == TABLES + ["lisez-moi"]
    rows = {name: list(wb[name].iter_rows(values_only=True)) for name in TABLES}
    sessions = [dict(zip(rows["sessions"][0], v)) for v in rows["sessions"][1:]]
    assert [len(rows[n]) - 1 for n in TABLES] == [3, 2, 3, 2, 3, 4, 7]

    done, live = sessions
    assert (done["statut"], done["resultats"]) == ("terminee", "definitifs")
    assert done["note_globale"] == 100
    # 2 choix seulement mettent l'empathie en jeu : pas assez pour la noter.
    assert done["empathie"] is None
    assert done["etats_narratifs"] == "vu_2" and isinstance(done["debut"], datetime)
    assert (live["statut"], live["resultats"]) == ("en_cours", "provisoires")
    assert live["scenes_notees"] == 1 and live["note_globale"] == 0

    passages = [dict(zip(rows["passages"][0], v)) for v in rows["passages"][1:]]
    assert [(p["chapitre_id"], p["passage_no"], p["compte"], p["statut"]) for p in passages] == [
        (1, 1, True, "termine"), (1, 2, False, "en_cours"), (2, 1, True, "termine"),
    ]
    levels = [dict(zip(rows["niveaux"][0], v)) for v in rows["niveaux"][1:]]
    assert [(lv["chapitre_id"], lv["niveau"], lv["passages_notes"]) for lv in levels] == [(1, 100, 1), (2, 100, 1)]

    choices = [dict(zip(rows["choix"][0], v)) for v in rows["choix"][1:]]
    first = choices[0]
    assert (first["etape"], first["personnage"], first["replique"]) == (1, "Mme A", "Bonjour")
    assert (first["reponse_no"], first["empathie"], first["total"], first["ecart"]) == (1, 2, 2, 0)
    assert (first["pire_total"], first["qualite"]) == (-1, 100)
    missed = next(c for c in choices if c["session_no"] == 2)
    assert (missed["reponse_no"], missed["total"], missed["meilleure_reponse_no"], missed["ecart"]) == (2, -1, 1, 3)
    assert missed["qualite"] == 0
    # Chapitre rejoué tout de suite : passage d'entraînement, rien n'est noté.
    assert [c["notee"] for c in choices if c["session_no"] == 2] == [False, False, False]


def test_csv_and_json_carry_the_same_rows(played):
    data = _json(played["trainer"])
    assert list(data["tables"]) == TABLES
    assert data["meta"]["livre"] == "Tous les livres" and data["meta"]["pseudonymise"] is False
    assert set(data["dictionnaire"]["choix"]["colonnes"]) >= {"reponse_no", "ecart", "empathie"}
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$",
                    data["tables"]["sessions"][0]["debut"])

    r = played["trainer"].get("/trainer/export?format=csv")
    assert r.mimetype == "application/zip"
    zf = zipfile.ZipFile(io.BytesIO(r.data))
    assert set(zf.namelist()) == {f"{n}.csv" for n in TABLES} | {"dictionnaire.csv", "LISEZMOI.txt"}
    for name in TABLES:
        raw = zf.read(f"{name}.csv")
        assert raw.startswith(b"\xef\xbb\xbf")  # BOM : accents lisibles dans Excel
        rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
        assert len(rows) == len(data["tables"][name])
        assert list(rows[0]) == list(data["tables"][name][0]) if rows else True


def test_filters_and_pseudonymization(played):
    page = played["trainer"].get("/trainer/").get_data(as_text=True)
    assert 'action="/trainer/export"' in page
    alice_id = int(re.search(r"/trainer/participants/(\d+)\">Alice", page).group(1))
    assert f'name="user" value="{alice_id}"' in played["trainer"].get(
        f"/trainer/participants/{alice_id}").get_data(as_text=True)

    data = _json(played["trainer"], f"&book=end_of_life&user={alice_id}&pseudo=1")
    text = json.dumps(data["tables"]).lower()
    assert "alice" not in text
    code = f"P{alice_id:03d}"
    assert [p["participant"] for p in data["tables"]["participants"]] == [code]
    assert {s["participant"] for s in data["tables"]["sessions"]} == {code}
    assert data["meta"]["participant"] == code and data["meta"]["livre"] == "End of Life"

    t = played["trainer"]
    assert t.get("/trainer/export?format=pdf").status_code == 400
    assert t.get("/trainer/export?book=inconnu").status_code == 404
    assert t.get("/trainer/export?user=abc").status_code == 400
    assert t.get("/trainer/export?user=999").status_code == 404


def test_formula_like_names_stay_text(app, played):
    _register(app.test_client(), "eve", "=1+1")
    r = played["trainer"].get("/trainer/export?format=csv")
    participants = zipfile.ZipFile(io.BytesIO(r.data)).read("participants.csv").decode("utf-8-sig")
    assert "'=1+1" in participants

    wb = load_workbook(io.BytesIO(played["trainer"].get("/trainer/export?format=xlsx").data))
    cell = next(c for row in wb["participants"].iter_rows() for c in row if c.value == "=1+1")
    assert cell.data_type == "s"
