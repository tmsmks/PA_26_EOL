#!/usr/bin/env python3
"""
End of Life - app.py
Serveur Flask (port 8765) : sert output/graphes/ et API POST /api/save.
"""
import json
import os

from flask import Flask, send_from_directory, request, jsonify

from enrichment import (
    SOFT_SKILLS,
    call_llm_for_enrichment,
    get_interaction_context,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPHES_DIR = os.path.join(BASE_DIR, "output", "graphes")
DATA_DIR = os.path.join(BASE_DIR, "data")
CHAPTERS_DIR = os.path.join(DATA_DIR, "chapters")
IMAGES_DIR = os.path.join(DATA_DIR, "images")

# Mapping book_slug -> fichier JSON (aligné sur graph_viewer.BOOKS).
BOOKS_BY_SLUG = {
    "end_of_life": "Chapters_v3-4-c_emotional-illustration.json",
    "medstudents_y2": "MedStudents_Y2_v1.json",
}
DEFAULT_BOOK_SLUG = "end_of_life"


def _resolve_data_path(book_slug: str | None) -> str:
    """Résout le chemin JSON à partir d'un book_slug (avec fallback legacy)."""
    slug = (book_slug or DEFAULT_BOOK_SLUG).strip()
    filename = BOOKS_BY_SLUG.get(slug)
    if filename is None:
        raise ValueError(
            f"book_slug inconnu : '{slug}'. Valeurs possibles : "
            f"{', '.join(BOOKS_BY_SLUG)}."
        )
    return os.path.join(CHAPTERS_DIR, filename)


app = Flask(__name__, static_folder=GRAPHES_DIR, static_url_path="")


@app.route("/")
def index():
    """Sert la page de garde (landing avec les deux livres)."""
    return send_from_directory(GRAPHES_DIR, "index.html")


@app.route("/api/data/images/<path:filename>")
def serve_images(filename):
    """Sert les images des personnages depuis data/images/ pour le parcours joueur."""
    return send_from_directory(IMAGES_DIR, filename)


@app.route("/<path:path>")
def serve_graphes(path):
    """Sert les fichiers HTML et autres ressources depuis output/graphes."""
    return send_from_directory(GRAPHES_DIR, path)


@app.route("/api/save", methods=["POST"])
def api_save():
    """Sauvegarde les données modifiées dans le JSON du livre ciblé."""
    try:
        data = request.get_json()
        if not data or "Chapters" not in data:
            return jsonify({"error": "Données invalides"}), 400

        incoming = data.get("Chapters", [])
        if not incoming:
            return jsonify({"error": "Aucun chapitre à sauvegarder"}), 400

        try:
            full_path = _resolve_data_path(data.get("book_slug"))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                full_data = json.load(f)
        else:
            full_data = {"Chapters": []}

        ch_id = incoming[0].get("Id")
        found = False
        for i, ch in enumerate(full_data.get("Chapters", [])):
            if ch.get("Id") == ch_id:
                full_data["Chapters"][i] = incoming[0]
                found = True
                break
        if not found:
            full_data.setdefault("Chapters", []).append(incoming[0])

        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(full_data, f, ensure_ascii=False, indent=2)

        return jsonify({
            "message": f"Sauvegardé dans {os.path.basename(full_path)}."
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/enrich", methods=["POST"])
def api_enrich():
    """
    Propose de nouvelles réponses via LLM pour une interaction donnée.

    Corps attendu (JSON) :
        {
            "chapter_id": int,
            "scene_id": int,
            "interaction_id": int,
            "orientation": { "RespectAndDignity": 2, "Empathy": 3, ... },   # optionnel
            "guidance": "ton plus direct",                                   # optionnel
            "n": 1                                                           # optionnel (1..3)
        }

    Réponse :
        { "proposals": [ { Text, Category, Rationale, SoftSkillDimensions, LegacyDimensions }, ... ] }
    """
    try:
        payload = request.get_json(silent=True) or {}
        chapter_id = payload.get("chapter_id")
        scene_id = payload.get("scene_id")
        interaction_id = payload.get("interaction_id")
        if chapter_id is None or scene_id is None or interaction_id is None:
            return jsonify({"error": "chapter_id, scene_id et interaction_id requis."}), 400

        raw_orientation = payload.get("orientation") or {}
        orientation = {}
        for skill in SOFT_SKILLS:
            if skill in raw_orientation and raw_orientation[skill] is not None:
                try:
                    v = int(raw_orientation[skill])
                except (TypeError, ValueError):
                    continue
                orientation[skill] = max(-3, min(3, v))

        guidance = payload.get("guidance") or None
        try:
            n_proposals = int(payload.get("n", 1))
        except (TypeError, ValueError):
            n_proposals = 1
        n_proposals = max(1, min(3, n_proposals))

        next_interaction_id = payload.get("next_interaction_id")
        if next_interaction_id is not None:
            try:
                next_interaction_id = int(next_interaction_id)
            except (TypeError, ValueError):
                next_interaction_id = None

        try:
            json_path = _resolve_data_path(payload.get("book_slug"))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        context = get_interaction_context(
            json_path=json_path,
            chapter_id=int(chapter_id),
            scene_id=int(scene_id),
            interaction_id=int(interaction_id),
            next_interaction_id=next_interaction_id,
        )

        proposals = call_llm_for_enrichment(
            context,
            orientation=orientation or None,
            guidance=guidance,
            n_proposals=n_proposals,
        )
        return jsonify({"proposals": proposals})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    os.makedirs(GRAPHES_DIR, exist_ok=True)
    print("End of Life — Serveur sur http://localhost:8765")
    app.run(host="0.0.0.0", port=8765, debug=False)
