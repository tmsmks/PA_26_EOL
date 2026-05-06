"""Views — Blueprints Flask (couche contrôleur)."""
from views.api import api_bp
from views.pages import pages_bp

__all__ = ["api_bp", "pages_bp"]
