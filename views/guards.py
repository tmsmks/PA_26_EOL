"""Authentification et protections transverses des vues.

- `current_user()` : utilisateur connecté (cookie de session signé) ;
- `login_required` / `trainer_required` : décorateurs de vues ;
- CSRF : jeton par session, exigé sur toute requête qui modifie l'état
  (champ `csrf_token` des formulaires ou en-tête `X-CSRF-Token` des fetch).
"""
from __future__ import annotations

import hmac
import secrets
from functools import wraps
from typing import Callable
from urllib.parse import urlsplit

from flask import Flask, abort, current_app, g, jsonify, redirect, request, session, url_for

from repositories.database import db_session
from repositories.orm import User
from repositories.users import UserRepository

UNSAFE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}


def current_user() -> User | None:
    if "current_user" not in g:
        uid = session.get("user_id")
        g.current_user = UserRepository(db_session()).get(uid) if uid else None
    return g.current_user


def login_user(user: User) -> None:
    session.clear()
    session.permanent = True
    session["user_id"] = user.id
    g.current_user = user


def logout_user() -> None:
    session.clear()
    g.current_user = None


def _wants_json() -> bool:
    return request.path.startswith("/api/")


def safe_next(target: str | None) -> str | None:
    """N'accepte qu'un chemin local (évite les redirections ouvertes)."""
    if not target:
        return None
    parts = urlsplit(target)
    if parts.scheme or parts.netloc or not target.startswith("/") or target.startswith("//"):
        return None
    return target


def login_required(view: Callable) -> Callable:
    @wraps(view)
    def wrapper(*args, **kwargs):
        if current_user() is None:
            if _wants_json():
                return jsonify({"error": "Connexion requise."}), 401
            return redirect(url_for("auth.login", next=request.full_path.rstrip("?")))
        return view(*args, **kwargs)

    return wrapper


def trainer_required(view: Callable) -> Callable:
    @wraps(view)
    @login_required
    def wrapper(*args, **kwargs):
        if not current_user().is_trainer:
            if _wants_json():
                return jsonify({"error": "Réservé aux formateur·rice·s."}), 403
            abort(403)
        return view(*args, **kwargs)

    return wrapper


def csrf_token() -> str:
    token = session.get("csrf_token")
    if not token:
        token = secrets.token_urlsafe(32)
        session["csrf_token"] = token
    return token


def _check_csrf():
    if request.method not in UNSAFE_METHODS or not current_app.config.get("CSRF_ENABLED", True):
        return None
    sent = request.headers.get("X-CSRF-Token") or request.form.get("csrf_token") or ""
    expected = session.get("csrf_token") or ""
    if expected and hmac.compare_digest(sent.encode(), expected.encode()):
        return None
    message = "Jeton de sécurité expiré : rechargez la page et réessayez."
    if _wants_json():
        return jsonify({"error": message}), 400
    return message, 400


def init_app(app: Flask) -> None:
    app.before_request(_check_csrf)

    @app.context_processor
    def _inject():
        return {"current_user": current_user(), "csrf_token": csrf_token}
