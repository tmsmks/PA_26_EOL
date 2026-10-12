"""API de la voix de lecture — appelée par le parcours joueur (static/play/audio.js)."""
from __future__ import annotations

from flask import Blueprint, current_app, jsonify, request, send_file, url_for

from services.tts_service import TtsError, TtsService
from views.guards import current_user, login_required

tts_bp = Blueprint("tts", __name__, url_prefix="/api/tts")


def tts() -> TtsService:
    return current_app.extensions["eol_tts"]


@tts_bp.get("/voices")
@login_required
def voices():
    """Voix serveur disponibles (vide : le jeu garde les voix du navigateur).
    La page de jeu les demande à son ouverture : on en profite pour préparer la
    voix par défaut."""
    tts().warm()
    return jsonify(tts().status())


@tts_bp.post("/speak")
@login_required
def speak():
    """Fait lire un texte d'écran ; renvoie l'adresse du MP3 (en cache ou créé)."""
    data = request.get_json(silent=True) or {}
    voice_id = str(data.get("voice") or "")
    try:
        key = tts().clip(voice_id, str(data.get("text") or ""), user_key=current_user().id)
    except TtsError as e:
        return jsonify({"error": str(e)}), e.status
    return jsonify({"url": url_for("tts.audio", voice_id=voice_id, key=key)})


@tts_bp.get("/audio/<voice_id>/<key>.mp3")
@login_required
def audio(voice_id: str, key: str):
    path = tts().path(voice_id, key)
    if path is None:
        return jsonify({"error": "Audio introuvable."}), 404
    # Les requêtes partielles (Range) sont nécessaires à Safari pour l'audio.
    res = send_file(path, mimetype="audio/mpeg", conditional=True, max_age=31536000)
    res.cache_control.public = False
    res.cache_control.private = True
    res.cache_control.immutable = True
    return res
