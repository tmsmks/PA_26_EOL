"""Lecture audio du parcours joueur : commandes dans la page de jeu, modules
servis, et règles de préparation du texte (tests JavaScript lancés avec Node)."""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app import create_app

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture()
def client(tmp_path):
    scene = {
        "Id": 1,
        "Title": "Scène",
        "Interactions": [
            {"Id": 1, "Text": "Bonjour", "Actor": {"Name": "Mme A"}, "Responses": [
                {"Id": 1, "Text": "fin", "NextInteractionID": -1, "SoftSkillDimensions": {"Empathy": 1}},
            ]},
        ],
    }
    book = {"Chapters": [{"Id": 1, "Name": "Un", "Intro": "Le début.", "Scenes": [scene]}]}
    (tmp_path / "chapter.json").write_text(json.dumps(book), encoding="utf-8")
    app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test",
        "DATABASE_URL": "sqlite:///" + str(tmp_path / "test.db"),
        "CHAPTERS_BASE_DIR": str(tmp_path),
        "CSRF_ENABLED": False,
    })
    c = app.test_client()
    c.post("/register", data={
        "username": "alice", "display_name": "Alice",
        "password": "motdepasse1", "password_confirm": "motdepasse1",
    })
    return c


def test_play_page_offers_audio_reading(client):
    html = client.get("/play/end_of_life/chapters/1").get_data(as_text=True)
    for marker in (
        'id="audio-toggle"',
        'aria-pressed="false"',
        'id="audio-pause"',
        'id="audio-replay"',
        'id="audio-voice"',
        'id="audio-rate"',
        'id="audio-choices"',
        'name="audio-agreement"',
        'id="keyhint-audio"',
        'id="audio-engine-note"',
        '"/api/tts/voices"',
        '"/api/tts/speak"',
    ):
        assert marker in html, marker
    # Masquées tant que audio.js n'a pas vérifié que le navigateur sait lire.
    assert 'class="audio-ctl" id="audio-ctl" data-state="off" hidden' in html


def test_audio_modules_are_served_as_javascript(client):
    for name in ("main.js", "audio.js", "speech_text.js"):
        res = client.get(f"/static/play/{name}")
        assert res.status_code == 200, name
        assert "javascript" in res.content_type, (name, res.content_type)
    assert 'from "./audio.js"' in client.get("/static/play/main.js").get_data(as_text=True)


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js n'est pas installé")
def test_speech_text_rules():
    """Écriture inclusive, abréviations, heures, capitales, découpage, choix de la
    voix, et tous les textes des livres lisibles sans symbole."""
    res = subprocess.run(
        ["node", "--test", str(ROOT / "tests" / "js" / "speech_text.test.mjs")],
        capture_output=True, text=True, timeout=120, cwd=ROOT,
    )
    assert res.returncode == 0, res.stdout + res.stderr
