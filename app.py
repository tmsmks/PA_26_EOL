#!/usr/bin/env python3
"""End of Life — entry point Flask (factory pattern).

Architecture :
- views/ : blueprints (pages HTML, APIs JSON)
- services/ : logique métier (graph, validation, enrichment)
- repositories/ : persistance
- domain/ : modèles purs

Démarrage : `python app.py` → http://localhost:8765
"""
from __future__ import annotations

import os

from flask import Flask

from views import api_bp, pages_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app() -> Flask:
    """Application factory."""
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
        static_url_path="/static",
    )
    app.config["IMAGES_DIR"] = os.path.join(BASE_DIR, "data", "images")
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)
    return app


app = create_app()


if __name__ == "__main__":
    print("End of Life — Serveur sur http://localhost:8765")
    app.run(host="0.0.0.0", port=8765, debug=False)
