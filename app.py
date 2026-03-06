#!/usr/bin/env python3
"""
End of Life - app.py
Serveur Flask (port 8765) : sert output/graphes/ et API POST /api/save.
"""
import json
import os

from flask import Flask, send_from_directory, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPHES_DIR = os.path.join(BASE_DIR, "output", "graphes")
DATA_DIR = os.path.join(BASE_DIR, "data")
CHAPTERS_DIR = os.path.join(DATA_DIR, "chapters")
IMAGES_DIR = os.path.join(DATA_DIR, "images")
DATA_PATH = os.path.join(CHAPTERS_DIR, "Chapters_v3-4-c_emotional-illustration.json")

app = Flask(__name__, static_folder=GRAPHES_DIR, static_url_path="")


@app.route("/")
def index():
    """Redirige vers l'index des graphes."""
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
    """Sauvegarde les données modifiées dans Chapters_v3-4-c_emotional-illustration.json."""
    try:
        data = request.get_json()
        if not data or "Chapters" not in data:
            return jsonify({"error": "Données invalides"}), 400

        incoming = data.get("Chapters", [])
        if not incoming:
            return jsonify({"error": "Aucun chapitre à sauvegarder"}), 400

        full_path = DATA_PATH
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

        return jsonify({"message": "Sauvegardé."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    os.makedirs(GRAPHES_DIR, exist_ok=True)
    print("End of Life — Serveur sur http://localhost:8765")
    app.run(host="0.0.0.0", port=8765, debug=False)
