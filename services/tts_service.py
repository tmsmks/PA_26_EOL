"""Voix de lecture du parcours joueur : synthèse vocale côté serveur.

Le navigateur envoie le texte d'un écran, déjà préparé pour la voix par
`static/play/speech_text.js` ; le serveur le fait lire par une voix neuronale,
garde le MP3 en cache (même voix et même texte = même fichier) et renvoie son
adresse. Les voix du navigateur restent le repli quand aucun moteur n'est là.

Moteurs (`TTS_ENGINE`) :
- « piper » : voix neuronales locales, gratuites, hors ligne (Piper, modèles
  dans `instance/tts/models`, voir `flask --app app tts-install`). Piper est
  sous GPL-3.0 : il tourne dans un processus séparé, `scripts/tts_piper_worker.py`,
  où les modèles restent chargés ;
- « azure » : voix neuronales de Microsoft Azure, les plus naturelles, dont le
  français de Suisse (`AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION`). Le texte des
  écrans part alors chez Microsoft ;
- « auto » (défaut) : Azure si une clé est configurée, sinon Piper s'il est
  installé avec au moins un modèle, sinon aucun ;
- « off » : pas de voix serveur.
"""
from __future__ import annotations

import atexit
import hashlib
import importlib.util
import json
import os
import queue
import re
import subprocess
import sys
import tempfile
import threading
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Protocol
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
WORKER = ROOT / "scripts" / "tts_piper_worker.py"
# Changer ce numéro invalide le cache (réglages de voix modifiés).
CACHE_VERSION = 1
KEY_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class Voice:
    id: str  # identifiant public, dans les URL et les réglages du joueur
    label: str  # affiché au participant
    engine: str  # piper | azure
    model: str  # nom du modèle Piper, ou nom de la voix Azure
    speaker: int | None = None
    lang: str = "fr-FR"


@dataclass(frozen=True)
class PiperModel:
    name: str
    url: str  # dossier du modèle sur Hugging Face (rhasspy/piper-voices)
    license: str


PIPER_MODELS = [
    PiperModel("fr_FR-siwis-medium", "fr/fr_FR/siwis/medium", "CC BY 4.0 (corpus SIWIS)"),
    PiperModel("fr_FR-upmc-medium", "fr/fr_FR/upmc/medium", "CC BY-SA 4.0 (corpus UPMC)"),
]
PIPER_VOICES = [
    Voice("siwis", "Siwis — voix féminine", "piper", "fr_FR-siwis-medium"),
    Voice("pierre", "Pierre — voix masculine", "piper", "fr_FR-upmc-medium", speaker=1),
    Voice("jessica", "Jessica — voix féminine", "piper", "fr_FR-upmc-medium", speaker=0),
]
AZURE_VOICES = [
    Voice("ariane", "Ariane — voix féminine (Suisse)", "azure", "fr-CH-ArianeNeural", lang="fr-CH"),
    Voice("fabrice", "Fabrice — voix masculine (Suisse)", "azure", "fr-CH-FabriceNeural", lang="fr-CH"),
    Voice("vivienne", "Vivienne — voix féminine (France)", "azure", "fr-FR-VivienneMultilingualNeural"),
    Voice("remy", "Rémy — voix masculine (France)", "azure", "fr-FR-RemyMultilingualNeural"),
]
HF_BASE = "https://huggingface.co/rhasspy/piper-voices/resolve/main/"


class TtsError(Exception):
    def __init__(self, message: str, status: int = 400):
        super().__init__(message)
        self.status = status


class Engine(Protocol):
    name: str

    def synthesize(self, voice: Voice, text: str, out: Path) -> None: ...


# --- Piper (local) ----------------------------------------------------------

def piper_installed() -> bool:
    return all(importlib.util.find_spec(m) is not None for m in ("piper", "soundfile"))


def piper_model_path(models_dir: Path, name: str) -> Path:
    return models_dir / f"{name}.onnx"


class PiperEngine:
    """Parle au processus Piper par lignes JSON ; le relance s'il s'arrête."""

    name = "piper"

    def __init__(self, models_dir: Path, timeout: float = 90.0,
                 length_scale: float = 1.06, sentence_silence: float = 0.32):
        self.models_dir = Path(models_dir)
        self.timeout = timeout
        # Un peu plus lent que le débit par défaut, avec un temps entre les
        # phrases : une lecture posée, plus agréable qu'une lecture pressée.
        self.length_scale = length_scale
        self.sentence_silence = sentence_silence
        self._proc: subprocess.Popen[str] | None = None
        self._replies: queue.Queue[str] = queue.Queue()
        self._lock = threading.Lock()
        atexit.register(self.close)

    def voices(self) -> list[Voice]:
        return [v for v in PIPER_VOICES if piper_model_path(self.models_dir, v.model).exists()]

    def _start(self) -> None:
        self._replies = queue.Queue()
        self._proc = subprocess.Popen(
            [sys.executable, str(WORKER)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        replies, stdout = self._replies, self._proc.stdout

        def pump() -> None:
            for line in stdout:
                replies.put(line)

        threading.Thread(target=pump, daemon=True).start()

    def synthesize(self, voice: Voice, text: str, out: Path) -> None:
        request = {
            "model": str(piper_model_path(self.models_dir, voice.model)),
            "speaker": voice.speaker,
            "text": text,
            "out": str(out),
            "length_scale": self.length_scale,
            "sentence_silence": self.sentence_silence,
        }
        with self._lock:
            if self._proc is None or self._proc.poll() is not None:
                self._start()
            assert self._proc is not None and self._proc.stdin is not None
            try:
                self._proc.stdin.write(json.dumps(request) + "\n")
                self._proc.stdin.flush()
                reply = json.loads(self._replies.get(timeout=self.timeout))
            except (OSError, queue.Empty, ValueError) as e:
                self.close()
                raise TtsError("La voix ne répond pas.", 503) from e
        if not reply.get("ok"):
            raise TtsError("Synthèse impossible : " + str(reply.get("error")), 503)

    def warm(self, voice: Voice) -> None:
        """Lance le processus et charge le modèle avant la première lecture."""
        out = Path(tempfile.gettempdir()) / f"eol-tts-warm-{os.getpid()}.mp3"
        try:
            self.synthesize(voice, "Bonjour.", out)
        except TtsError:
            pass
        finally:
            out.unlink(missing_ok=True)

    def close(self) -> None:
        proc, self._proc = self._proc, None
        if proc is not None and proc.poll() is None:
            proc.kill()


# --- Azure (service en ligne) -------------------------------------------------

class AzureEngine:
    name = "azure"

    def __init__(self, key: str, region: str, timeout: float = 30.0):
        self.key = key
        self.region = region
        self.timeout = timeout

    def voices(self) -> list[Voice]:
        return list(AZURE_VOICES)

    def ssml(self, voice: Voice, text: str) -> str:
        body = escape(text)
        if "Multilingual" in voice.model:
            body = f'<lang xml:lang="{voice.lang}">{body}</lang>'
        return (
            f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{voice.lang}">'
            f'<voice name="{voice.model}">{body}</voice></speak>'
        )

    def synthesize(self, voice: Voice, text: str, out: Path) -> None:
        import requests

        try:
            res = requests.post(
                f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/v1",
                data=self.ssml(voice, text).encode("utf-8"),
                headers={
                    "Ocp-Apim-Subscription-Key": self.key,
                    "Content-Type": "application/ssml+xml",
                    "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
                    "User-Agent": "end-of-life-serious-game",
                },
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            raise TtsError("Le service de voix est injoignable.", 503) from e
        if res.status_code != 200 or not res.content:
            raise TtsError(f"Le service de voix a refusé la demande ({res.status_code}).", 503)
        tmp = out.with_name(out.name + ".part")
        tmp.write_bytes(res.content)
        os.replace(tmp, out)


# --- Service --------------------------------------------------------------------

class TtsService:
    """Cache, limites et choix de la voix ; le moteur fait la synthèse."""

    def __init__(self, engine: Any, cache_dir: Path, *, max_chars: int = 3000,
                 per_minute: int = 40, daily_chars: int = 400_000):
        self.engine = engine
        self.cache_dir = Path(cache_dir)
        self.max_chars = max_chars
        self.per_minute = per_minute
        self.daily_chars = daily_chars
        self._voices: list[Voice] = engine.voices() if engine is not None else []
        self._guard = threading.Lock()
        self._key_locks: dict[str, threading.Lock] = defaultdict(threading.Lock)
        self._recent: dict[Any, deque[float]] = defaultdict(deque)
        self._day = date.today()
        self._chars_today = 0
        self._warmed = False

    @property
    def enabled(self) -> bool:
        return self.engine is not None and bool(self._voices)

    def status(self) -> dict[str, Any]:
        return {
            "enabled": self.enabled,
            "engine": self.engine.name if self.enabled else None,
            "voices": [{"id": v.id, "label": v.label} for v in self._voices],
            "default": self._voices[0].id if self._voices else None,
        }

    def warm(self) -> None:
        """Prépare la voix par défaut en arrière-plan (une fois) : la première
        lecture n'attend pas le chargement du modèle."""
        if self._warmed or not self.enabled or not hasattr(self.engine, "warm"):
            return
        self._warmed = True
        threading.Thread(target=self.engine.warm, args=(self._voices[0],), daemon=True).start()

    def voice(self, voice_id: str) -> Voice:
        for v in self._voices:
            if v.id == voice_id:
                return v
        raise TtsError("Voix inconnue.", 404)

    def key(self, voice: Voice, text: str) -> str:
        raw = f"{CACHE_VERSION}|{voice.engine}|{voice.model}|{voice.speaker}|{text}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def path(self, voice_id: str, key: str) -> Path | None:
        """Fichier en cache, ou None (identifiants vérifiés : pas de chemin arbitraire)."""
        if not KEY_RE.match(key or ""):
            return None
        try:
            self.voice(voice_id)
        except TtsError:
            return None
        p = self.cache_dir / voice_id / key[:2] / f"{key}.mp3"
        return p if p.exists() else None

    def clean(self, text: str) -> str:
        text = re.sub(r"[\x00-\x1f\x7f]+", " ", str(text or ""))
        text = re.sub(r"\s+", " ", text).strip()
        if not re.search(r"\w", text):
            raise TtsError("Rien à lire.")
        if len(text) > self.max_chars:
            raise TtsError(f"Texte trop long ({len(text)} caractères, {self.max_chars} au plus).", 413)
        return text

    def _allow(self, user_key: Any, n_chars: int) -> None:
        now = time.monotonic()
        with self._guard:
            if date.today() != self._day:
                self._day, self._chars_today = date.today(), 0
            if self._chars_today + n_chars > self.daily_chars:
                raise TtsError("La voix a assez lu pour aujourd'hui : les voix du navigateur prennent le relais.", 429)
            recent = self._recent[user_key]
            while recent and now - recent[0] > 60:
                recent.popleft()
            if len(recent) >= self.per_minute:
                raise TtsError("Trop de demandes de lecture : réessayez dans une minute.", 429)
            recent.append(now)
            self._chars_today += n_chars

    def clip(self, voice_id: str, text: str, user_key: Any = None) -> str:
        """Clé du MP3 de ce texte lu par cette voix ; le synthétise s'il manque."""
        if not self.enabled:
            raise TtsError("Aucune voix serveur n'est installée.", 503)
        voice = self.voice(voice_id)
        text = self.clean(text)
        key = self.key(voice, text)
        out = self.cache_dir / voice.id / key[:2] / f"{key}.mp3"
        if out.exists():
            return key
        with self._key_locks[key]:  # deux demandes du même texte : une seule synthèse
            if out.exists():
                return key
            self._allow(user_key, len(text))
            out.parent.mkdir(parents=True, exist_ok=True)
            self.engine.synthesize(voice, text, out)
        self._key_locks.pop(key, None)
        return key


def build_engine(config: dict[str, Any]) -> Any:
    """Moteur choisi d'après la configuration (voir le docstring du module)."""
    choice = (config.get("TTS_ENGINE") or "auto").lower()
    key, region = config.get("AZURE_SPEECH_KEY"), config.get("AZURE_SPEECH_REGION")
    models_dir = Path(config["TTS_MODELS_DIR"])
    if choice == "off":
        return None
    if choice in ("azure", "auto") and key and region:
        return AzureEngine(key, region)
    if choice in ("piper", "auto") and piper_installed():
        engine = PiperEngine(models_dir)
        if engine.voices():
            return engine
    return None


def install_piper_models(models_dir: Path, echo=print) -> list[Path]:
    """Télécharge les modèles Piper français (avec leur fiche et leur licence)."""
    import requests

    models_dir = Path(models_dir)
    models_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for m in PIPER_MODELS:
        for remote, local in (
            (f"{m.name}.onnx", f"{m.name}.onnx"),
            (f"{m.name}.onnx.json", f"{m.name}.onnx.json"),
            ("MODEL_CARD", f"{m.name}.MODEL_CARD.md"),
        ):
            target = models_dir / local
            if target.exists() and target.stat().st_size > 0:
                continue
            echo(f"Téléchargement de {local} ({m.license})…")
            with requests.get(HF_BASE + f"{m.url}/{remote}", stream=True, timeout=60) as res:
                res.raise_for_status()
                tmp = target.with_name(target.name + ".part")
                with open(tmp, "wb") as f:
                    for block in res.iter_content(1 << 20):
                        f.write(block)
                os.replace(tmp, target)
            written.append(target)
    return written
