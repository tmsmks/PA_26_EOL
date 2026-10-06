#!/usr/bin/env python3
"""End of Life — entry point Flask (factory pattern).

Architecture :
- views/ : blueprints (pages HTML, APIs JSON, comptes, sessions)
- services/ : logique métier (graph, validation, enrichment, scoring, feedback)
- repositories/ : persistance (JSON des livres, base SQL des comptes/sessions)
- domain/ : modèles purs

Démarrage : `python app.py` → http://localhost:8765
Créer un compte formateur : `flask --app app create-user <identifiant> --role trainer`
"""
from __future__ import annotations

import os
import secrets
from datetime import datetime, timedelta, timezone
from typing import Any
from zoneinfo import ZoneInfo

import click
from flask import Flask

from repositories import database
from repositories.chapters import ChapterRepository
from repositories.orm import ROLES, ROLE_PARTICIPANT
from repositories.users import UserRepository
from services.auth_service import AuthError, hash_password, register, validate_password
from services.feedback import FeedbackService
from services.scoring_service import quoted
from services.scoring_upgrade import upgrade_scoring
from views import account_bp, api_bp, auth_bp, pages_bp, session_api_bp
from views import guards

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def _load_or_create_secret(instance_dir: str) -> str:
    """Clé de signature des cookies, persistée pour survivre aux redémarrages.

    En production, préférer la variable d'environnement SECRET_KEY.
    """
    os.makedirs(instance_dir, exist_ok=True)
    path = os.path.join(instance_dir, "secret_key")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    key = secrets.token_hex(32)
    with open(path, "w", encoding="utf-8") as f:
        f.write(key)
    os.chmod(path, 0o600)
    return key


def _local_time(value: datetime | None) -> datetime | None:
    if value is None:
        return None
    if value.tzinfo is None:  # SQLite ne conserve pas le fuseau : c'est de l'UTC
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(ZoneInfo(os.getenv("APP_TIMEZONE", "Europe/Zurich")))


def create_app(config: dict[str, Any] | None = None) -> Flask:
    """Application factory."""
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
        static_url_path="/static",
        instance_path=os.path.join(BASE_DIR, "instance"),
    )
    app.config.update(
        IMAGES_DIR=os.path.join(BASE_DIR, "data", "images"),
        DATABASE_URL=os.getenv("DATABASE_URL"),
        SECRET_KEY=os.getenv("SECRET_KEY"),
        REGISTRATION_CODE=os.getenv("REGISTRATION_CODE") or None,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.getenv("SESSION_COOKIE_SECURE") == "1",
        PERMANENT_SESSION_LIFETIME=timedelta(days=30),
        CSRF_ENABLED=True,
        CHAPTERS_BASE_DIR=None,
        FEEDBACK_BACKEND=None,
        # Scoring v2 : délai minimal entre deux passages notés d'un même chapitre.
        PASSAGE_SPACING_DAYS=int(os.getenv("PASSAGE_SPACING_DAYS", "7")),
    )
    if config:
        app.config.update(config)
    if not app.config["SECRET_KEY"]:
        app.config["SECRET_KEY"] = _load_or_create_secret(app.instance_path)

    database.init_app(app)
    app.extensions["eol_chapters"] = ChapterRepository(base_dir=app.config["CHAPTERS_BASE_DIR"])
    app.extensions["eol_feedback"] = FeedbackService(backend=app.config["FEEDBACK_BACKEND"])
    guards.init_app(app)

    # Reprise idempotente des parties jouées avant le scoring v2.
    db = app.extensions["eol_db"].sessionmaker()
    try:
        stats = upgrade_scoring(db, app.extensions["eol_chapters"], app.config["PASSAGE_SPACING_DAYS"])
    finally:
        db.close()
    if any(stats.values()):
        app.logger.warning("Scoring v2 : %(passages)d passage(s) et %(sessions)d bilan(s) repris.", stats)

    @app.template_filter("date_fr")
    def _date_fr(value: datetime | None, with_time: bool = False) -> str:
        local = _local_time(value)
        if local is None:
            return "—"
        return local.strftime("%d.%m.%Y à %H:%M" if with_time else "%d.%m.%Y")

    @app.template_filter("note")
    def _note(value: float | None, digits: int = 0) -> str:
        if value is None:
            return "—"
        return str(round(value)) if not digits else f"{value:.{digits}f}".replace(".", ",")

    app.add_template_filter(quoted, "quoted")

    @app.template_filter("weight")
    def _weight(value: float | None) -> str:
        return "—" if value is None else "×" + f"{value:.2f}".rstrip("0").rstrip(".").replace(".", ",")

    for bp in (pages_bp, api_bp, auth_bp, account_bp, session_api_bp):
        app.register_blueprint(bp)

    @app.cli.command("create-user")
    @click.argument("username")
    @click.option("--role", type=click.Choice(ROLES), default=ROLE_PARTICIPANT, show_default=True)
    @click.option("--name", "display_name", default="", help="Nom affiché.")
    @click.password_option(help="Mot de passe (demandé si absent).")
    def create_user(username: str, role: str, display_name: str, password: str) -> None:
        """Crée un compte, ou met à jour le rôle et le mot de passe s'il existe."""
        users = UserRepository(app.extensions["eol_db"].sessionmaker())
        existing = users.get_by_username(username)
        try:
            if existing is None:
                user = register(users, username, password, display_name, role=role)
                click.echo(f"Compte créé : {user.username} ({user.role}).")
            else:
                validate_password(password)
                users.set_password(existing, hash_password(password))
                users.set_role(existing, role)
                click.echo(f"Compte mis à jour : {existing.username} ({role}).")
        except AuthError as e:
            raise click.ClickException(str(e)) from e

    return app


app = create_app()


if __name__ == "__main__":
    print("End of Life — Serveur sur http://localhost:8765")
    app.run(host="0.0.0.0", port=8765, debug=False)
