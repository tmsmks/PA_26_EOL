"""Views — Blueprints Flask (couche contrôleur)."""
from views.account import account_bp
from views.api import api_bp
from views.auth import auth_bp
from views.expert_key import expert_key_bp
from views.pages import pages_bp
from views.session_api import session_api_bp
from views.tts import tts_bp

__all__ = ["account_bp", "api_bp", "auth_bp", "expert_key_bp", "pages_bp", "session_api_bp", "tts_bp"]
