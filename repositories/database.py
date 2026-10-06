"""Connexion à la base relationnelle (comptes, sessions, tentatives).

Une seule variable décide du moteur : `DATABASE_URL`.
- absente → SQLite dans `instance/eol.db` (développement, démo locale) ;
- `postgresql://…` → PostgreSQL hébergé (production, accès depuis partout).

Les vues obtiennent une session SQLAlchemy par requête via `db_session()` ;
elle est fermée automatiquement en fin de requête.
"""
from __future__ import annotations

import os

from flask import Flask, current_app, g
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    """Base déclarative commune aux modèles ORM."""


def normalize_url(url: str) -> str:
    """Accepte les URLs `postgres://` (Heroku, Supabase) et force psycopg 3."""
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg://" + url[len("postgresql://"):]
    return url


class Database:
    """Moteur + fabrique de sessions, créés une fois par application."""

    def __init__(self, url: str) -> None:
        self.url = normalize_url(url)
        kwargs: dict = {"future": True}
        if self.url.startswith("sqlite"):
            kwargs["connect_args"] = {"check_same_thread": False}
        else:
            kwargs["pool_pre_ping"] = True
        self.engine: Engine = create_engine(self.url, **kwargs)
        if self.url.startswith("sqlite"):
            event.listen(self.engine, "connect", _sqlite_foreign_keys)
        self.sessionmaker = sessionmaker(bind=self.engine, expire_on_commit=False)

    def create_all(self) -> None:
        # Import local : enregistre les modèles sur Base.metadata.
        from repositories import orm  # noqa: F401

        Base.metadata.create_all(self.engine)


def _sqlite_foreign_keys(dbapi_conn, _record) -> None:
    cur = dbapi_conn.cursor()
    cur.execute("PRAGMA foreign_keys=ON")
    cur.close()


def default_sqlite_url(instance_dir: str) -> str:
    os.makedirs(instance_dir, exist_ok=True)
    return "sqlite:///" + os.path.join(instance_dir, "eol.db")


def init_app(app: Flask) -> Database:
    """Crée la base, les tables manquantes, et le cycle de vie par requête."""
    url = app.config.get("DATABASE_URL") or default_sqlite_url(app.instance_path)
    db = Database(url)
    db.create_all()
    app.extensions["eol_db"] = db

    @app.teardown_appcontext
    def _close_session(_exc) -> None:
        session = g.pop("db_session", None)
        if session is not None:
            session.close()

    return db


def db_session() -> Session:
    """Session SQLAlchemy de la requête courante."""
    if "db_session" not in g:
        g.db_session = current_app.extensions["eol_db"].sessionmaker()
    return g.db_session
