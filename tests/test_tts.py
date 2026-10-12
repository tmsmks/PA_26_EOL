"""Voix de lecture côté serveur : cache, limites, API, moteurs Azure et Piper."""
import json
from pathlib import Path

import pytest

from app import create_app
from services import tts_service
from services.tts_service import (
    AZURE_VOICES,
    AzureEngine,
    PiperEngine,
    TtsError,
    TtsService,
    Voice,
    build_engine,
    piper_installed,
    piper_model_path,
)

MP3 = b"ID3\x03\x00\x00\x00\x00\x00\x00" + b"\xff\xfb" * 200


class FakeEngine:
    name = "fake"

    def __init__(self):
        self.calls = []

    def voices(self):
        return [Voice("claire", "Claire", "fake", "m1"), Voice("paul", "Paul", "fake", "m2")]

    def synthesize(self, voice, text, out):
        self.calls.append((voice.id, text))
        out.write_bytes(MP3)


def test_same_text_is_synthesized_once(tmp_path):
    engine = FakeEngine()
    svc = TtsService(engine, tmp_path)
    k1 = svc.clip("claire", "Bonjour, Madame Pittet.")
    k2 = svc.clip("claire", "  Bonjour,\nMadame Pittet. ")  # espaces normalisés
    assert k1 == k2
    assert engine.calls == [("claire", "Bonjour, Madame Pittet.")]
    assert svc.path("claire", k1).read_bytes() == MP3
    # Autre voix : autre fichier.
    assert svc.clip("paul", "Bonjour, Madame Pittet.") != k1
    assert len(engine.calls) == 2


def test_texts_and_voices_are_checked(tmp_path):
    svc = TtsService(FakeEngine(), tmp_path, max_chars=50)
    with pytest.raises(TtsError) as e:
        svc.clip("inconnue", "Bonjour.")
    assert e.value.status == 404
    with pytest.raises(TtsError) as e:
        svc.clip("claire", " … ! ")
    assert e.value.status == 400
    with pytest.raises(TtsError) as e:
        svc.clip("claire", "x" * 51)
    assert e.value.status == 413


def test_cache_paths_cannot_escape(tmp_path):
    svc = TtsService(FakeEngine(), tmp_path)
    key = svc.clip("claire", "Bonjour.")
    assert svc.path("claire", key) is not None
    assert svc.path("claire", "../../etc/passwd") is None
    assert svc.path("claire", "0" * 64) is None  # pas en cache
    assert svc.path("inconnue", key) is None


def test_rate_and_daily_limits(tmp_path):
    svc = TtsService(FakeEngine(), tmp_path, per_minute=2, daily_chars=1000)
    svc.clip("claire", "Un.", user_key=1)
    svc.clip("claire", "Deux.", user_key=1)
    svc.clip("claire", "Un.", user_key=1)  # en cache : ne compte pas
    with pytest.raises(TtsError) as e:
        svc.clip("claire", "Trois.", user_key=1)
    assert e.value.status == 429
    svc.clip("claire", "Trois.", user_key=2)  # autre participant
    small = TtsService(FakeEngine(), tmp_path / "b", daily_chars=10)
    with pytest.raises(TtsError) as e:
        small.clip("claire", "Bien plus de dix caractères.")
    assert e.value.status == 429


def test_service_without_engine_is_off(tmp_path):
    svc = TtsService(None, tmp_path)
    assert svc.status() == {"enabled": False, "engine": None, "voices": [], "default": None}
    with pytest.raises(TtsError) as e:
        svc.clip("claire", "Bonjour.")
    assert e.value.status == 503


def test_engine_choice(tmp_path):
    base = {"TTS_MODELS_DIR": str(tmp_path / "vide")}
    assert build_engine({**base, "TTS_ENGINE": "off", "AZURE_SPEECH_KEY": "k", "AZURE_SPEECH_REGION": "r"}) is None
    assert isinstance(build_engine({**base, "AZURE_SPEECH_KEY": "k", "AZURE_SPEECH_REGION": "r"}), AzureEngine)
    assert build_engine({**base, "TTS_ENGINE": "piper"}) is None  # aucun modèle installé
    assert build_engine({**base, "TTS_ENGINE": "azure"}) is None  # pas de clé


def test_azure_request(monkeypatch, tmp_path):
    sent = {}

    class Res:
        status_code = 200
        content = MP3

    def fake_post(url, data, headers, timeout):
        sent.update(url=url, ssml=data.decode("utf-8"), headers=headers)
        return Res()

    import requests

    monkeypatch.setattr(requests, "post", fake_post)
    engine = AzureEngine("clé", "switzerlandnorth")
    ariane = AZURE_VOICES[0]
    out = tmp_path / "a.mp3"
    engine.synthesize(ariane, "Daniel & Océane <rient>.", out)
    assert out.read_bytes() == MP3
    assert sent["url"] == "https://switzerlandnorth.tts.speech.microsoft.com/cognitiveservices/v1"
    assert sent["headers"]["Ocp-Apim-Subscription-Key"] == "clé"
    assert 'xml:lang="fr-CH"' in sent["ssml"] and 'name="fr-CH-ArianeNeural"' in sent["ssml"]
    assert "Daniel &amp; Océane &lt;rient&gt;." in sent["ssml"]
    # Voix multilingue : la langue est imposée.
    vivienne = next(v for v in AZURE_VOICES if v.id == "vivienne")
    assert '<lang xml:lang="fr-FR">' in engine.ssml(vivienne, "Bonjour.")


# --- API ------------------------------------------------------------------------

@pytest.fixture()
def app(tmp_path):
    book = {"Chapters": [{"Id": 1, "Name": "Un", "Intro": "", "Scenes": []}]}
    (tmp_path / "chapter.json").write_text(json.dumps(book), encoding="utf-8")
    application = create_app({
        "TESTING": True,
        "SECRET_KEY": "test",
        "DATABASE_URL": "sqlite:///" + str(tmp_path / "test.db"),
        "CHAPTERS_BASE_DIR": str(tmp_path),
        "CSRF_ENABLED": False,
    })
    application.extensions["eol_tts"] = TtsService(FakeEngine(), tmp_path / "cache")
    return application


@pytest.fixture()
def alice(app):
    c = app.test_client()
    c.post("/register", data={
        "username": "alice", "display_name": "Alice",
        "password": "motdepasse1", "password_confirm": "motdepasse1",
    })
    return c


def test_tts_is_off_by_default_in_tests(tmp_path):
    application = create_app({
        "TESTING": True, "SECRET_KEY": "t", "DATABASE_URL": "sqlite:///" + str(tmp_path / "t.db"),
    })
    assert application.extensions["eol_tts"].status()["enabled"] is False


def test_api_requires_login(app):
    c = app.test_client()
    assert c.get("/api/tts/voices").status_code == 401
    assert c.post("/api/tts/speak", json={"voice": "claire", "text": "Bonjour."}).status_code == 401


def test_api_speaks_and_serves_audio(app, alice):
    status = alice.get("/api/tts/voices").get_json()
    assert status["enabled"] is True and status["default"] == "claire"
    res = alice.post("/api/tts/speak", json={"voice": "claire", "text": "Bonjour, petit."})
    assert res.status_code == 200
    url = res.get_json()["url"]
    assert url.startswith("/api/tts/audio/claire/") and url.endswith(".mp3")
    audio = alice.get(url)
    assert audio.status_code == 200
    assert audio.mimetype == "audio/mpeg"
    assert audio.data == MP3
    assert "private" in audio.headers["Cache-Control"]
    # Safari lit l'audio par morceaux (requêtes partielles).
    part = alice.get(url, headers={"Range": "bytes=0-9"})
    assert part.status_code == 206 and part.data == MP3[:10]
    # Même texte : même adresse, pas de nouvelle synthèse.
    again = alice.post("/api/tts/speak", json={"voice": "claire", "text": "Bonjour, petit."})
    assert again.get_json()["url"] == url
    assert len(app.extensions["eol_tts"].engine.calls) == 1


def test_api_errors(alice):
    assert alice.post("/api/tts/speak", json={"voice": "nope", "text": "Bonjour."}).status_code == 404
    assert alice.post("/api/tts/speak", json={"voice": "claire", "text": ""}).status_code == 400
    assert alice.post("/api/tts/speak", json={"voice": "claire", "text": "a" * 5000}).status_code == 413
    assert alice.get("/api/tts/audio/claire/" + "0" * 64 + ".mp3").status_code == 404
    assert alice.get("/api/tts/audio/claire/pas-une-cle.mp3").status_code == 404


# --- Piper (réel, si installé avec ses modèles) -----------------------------------

MODELS = Path(tts_service.ROOT) / "instance" / "tts" / "models"


@pytest.mark.skipif(
    not piper_installed() or not piper_model_path(MODELS, "fr_FR-siwis-medium").exists(),
    reason="Piper ou le modèle siwis n'est pas installé (flask --app app tts-install)",
)
def test_piper_reads_french(tmp_path):
    engine = PiperEngine(MODELS)
    try:
        siwis = next(v for v in engine.voices() if v.id == "siwis")
        out = tmp_path / "bonjour.mp3"
        engine.synthesize(siwis, "Bonjour. Je suis la voix du parcours.", out)
        data = out.read_bytes()
        assert len(data) > 2000
        assert data[:3] == b"ID3" or data[0] == 0xFF  # en-tête MP3
    finally:
        engine.close()
