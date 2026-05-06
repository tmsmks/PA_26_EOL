"""APIs HTTP — Blueprint /api/*."""
from __future__ import annotations

import os

from flask import Blueprint, current_app, jsonify, request, send_from_directory

from domain.models import Chapter
from repositories.chapters import ChapterRepository
from services.enrichment import EnrichmentService, EnrichRequest
from services.enrichment.backends import LLMBackendError
from services.enrichment.context import InteractionNotFoundError

api_bp = Blueprint("api", __name__, url_prefix="/api")

_repo = ChapterRepository()
_enrichment = EnrichmentService(repository=_repo)


@api_bp.route("/data/images/<path:filename>")
def serve_images(filename: str):
    """Sert les images des personnages depuis data/images/."""
    images_dir = current_app.config["IMAGES_DIR"]
    return send_from_directory(images_dir, filename)


@api_bp.route("/save", methods=["POST"])
def api_save():
    """Sauvegarde un chapitre dans le JSON du livre ciblé (écriture atomique)."""
    payload = request.get_json(silent=True)
    if not payload or "Chapters" not in payload:
        return jsonify({"error": "Données invalides"}), 400

    incoming = payload.get("Chapters") or []
    if not incoming:
        return jsonify({"error": "Aucun chapitre à sauvegarder"}), 400

    try:
        chapter = Chapter.from_dict(incoming[0])
        filename = _repo.upsert_chapter(payload.get("book_slug"), chapter)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except OSError as e:
        return jsonify({"error": f"Erreur d'écriture : {e}"}), 500

    return jsonify({"message": f"Sauvegardé dans {filename}."})


@api_bp.route("/enrich", methods=["POST"])
def api_enrich():
    """Propose de nouvelles réponses via LLM pour une interaction donnée."""
    payload = request.get_json(silent=True) or {}

    try:
        req = EnrichRequest.from_payload(payload)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    try:
        proposals = _enrichment.propose_responses(req)
    except InteractionNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except LLMBackendError as e:
        return jsonify({"error": str(e)}), 502
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"proposals": proposals})
