"""Modèles ORM : comptes, sessions de livre, passages de chapitre, tentatives.

Une *session* est un parcours de l'histoire d'un livre par un participant ;
elle peut s'étaler sur plusieurs jours et porte les états narratifs. Un
*passage* est une partie complète d'un chapitre dans une session : c'est
l'unité de note (scoring v2). Chaque scène jouée produit une tentative ;
dans un passage, seule la première tentative d'une scène est notée.
Les scores et le texte des choix sont figés au moment du jeu : modifier un
livre ensuite ne réécrit pas l'historique.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from repositories.database import Base

ROLE_PARTICIPANT = "participant"
ROLE_TRAINER = "trainer"
ROLES = (ROLE_PARTICIPANT, ROLE_TRAINER)

STATUS_IN_PROGRESS = "in_progress"
STATUS_COMPLETED = "completed"


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    display_name: Mapped[str] = mapped_column(String(80))
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default=ROLE_PARTICIPANT)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    sessions: Mapped[list["BookSession"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    @property
    def is_trainer(self) -> bool:
        return self.role == ROLE_TRAINER


class BookSession(Base):
    __tablename__ = "book_sessions"
    __table_args__ = (UniqueConstraint("user_id", "book_slug", "number"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    book_slug: Mapped[str] = mapped_column(String(80), index=True)
    # Rang de la session pour ce participant et ce livre (1, 2, 3…).
    number: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20), default=STATUS_IN_PROGRESS)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    # États narratifs courants (suivent le joueur d'un chapitre à l'autre).
    flags: Mapped[list[str]] = mapped_column(JSON, default=list)
    completed_chapters: Mapped[list[int]] = mapped_column(JSON, default=list)
    # Instantané des résultats calculé à la fin du livre (scoring_service).
    results: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    # Feedback général (IA ou règles de repli) — voir services/feedback.
    feedback: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    user: Mapped[User] = relationship(back_populates="sessions")
    attempts: Mapped[list["SceneAttempt"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
        order_by="SceneAttempt.id",
    )
    passages: Mapped[list["ChapterPassage"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
        order_by="ChapterPassage.id",
    )

    @property
    def is_completed(self) -> bool:
        return self.status == STATUS_COMPLETED


# Tentatives jouées pendant un passage (table d'association : la table
# scene_attempts existante n'est pas modifiée, voir README « évolution du schéma »).
passage_attempts = Table(
    "passage_attempts",
    Base.metadata,
    Column("passage_id", ForeignKey("chapter_passages.id", ondelete="CASCADE"), primary_key=True),
    Column("attempt_id", ForeignKey("scene_attempts.id", ondelete="CASCADE"), primary_key=True),
)


class ChapterPassage(Base):
    """Une partie complète d'un chapitre : l'unité de note du scoring v2."""

    __tablename__ = "chapter_passages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    session_id: Mapped[int] = mapped_column(
        ForeignKey("book_sessions.id", ondelete="CASCADE"), index=True
    )
    book_slug: Mapped[str] = mapped_column(String(80), index=True)
    chapter_id: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20), default=STATUS_IN_PROGRESS)
    # Compte dans le niveau du chapitre : 1er passage, ou passage assez espacé
    # du précédent passage compté (sinon : entraînement).
    counted: Mapped[bool] = mapped_column(Boolean, default=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    # États narratifs au début du passage : rejouer le chapitre seul repart d'ici.
    flags_in: Mapped[list[str]] = mapped_column(JSON, default=list)
    # Instantané calculé à la fin du passage (scoring_service.passage_results).
    results: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    session: Mapped[BookSession] = relationship(back_populates="passages")
    user: Mapped[User] = relationship()
    attempts: Mapped[list["SceneAttempt"]] = relationship(
        secondary=passage_attempts, order_by="SceneAttempt.id"
    )

    @property
    def is_completed(self) -> bool:
        return self.status == STATUS_COMPLETED


class SceneAttempt(Base):
    __tablename__ = "scene_attempts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(
        ForeignKey("book_sessions.id", ondelete="CASCADE"), index=True
    )
    chapter_id: Mapped[int] = mapped_column(Integer)
    scene_id: Mapped[int] = mapped_column(Integer)
    scene_title: Mapped[str] = mapped_column(String(255), default="")
    attempt_no: Mapped[int] = mapped_column(Integer, default=1)
    counted: Mapped[bool] = mapped_column(Boolean, default=True)
    entry_id: Mapped[int] = mapped_column(Integer)
    # Par compétence : score obtenu, pire et meilleur score atteignables.
    raw: Mapped[dict[str, int]] = mapped_column(JSON, default=dict)
    lo: Mapped[dict[str, int]] = mapped_column(JSON, default=dict)
    hi: Mapped[dict[str, int]] = mapped_column(JSON, default=dict)
    # Choix effectués, avec la meilleure alternative à chaque étape.
    trace: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    session: Mapped[BookSession] = relationship(back_populates="attempts")


class ExpertRating(Base):
    """Cote d'un expert pour une réponse du livre (validation de la clé de cotation).

    `ref` identifie la réponse : « c{chapitre}-s{scène}-i{interaction}-r{rang} »,
    le rang commençant à 1 dans l'ordre du livre.
    """

    __tablename__ = "expert_ratings"
    __table_args__ = (UniqueConstraint("book_slug", "ref", "expert", "round"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_slug: Mapped[str] = mapped_column(String(80), index=True)
    ref: Mapped[str] = mapped_column(String(40))
    expert: Mapped[str] = mapped_column(String(80))
    round: Mapped[int] = mapped_column(Integer, default=1)
    # Points par compétence (−3 à +3) ; une compétence laissée vide vaut 0.
    scores: Mapped[dict[str, int]] = mapped_column(JSON, default=dict)
    critical: Mapped[bool] = mapped_column(Boolean, default=False)
    rationale: Mapped[str] = mapped_column(Text, default="")
    comment: Mapped[str] = mapped_column(Text, default="")
    uploaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)



class AngoffRating(Base):
    """Choix d'un·e juge pour un point de choix (seuils de niveau, Angoff modifié).

    Le ou la juge indique la réponse que choisirait le plus probablement un·e
    étudiant·e « tout juste compétent·e » de l'année visée. `point` :
    « c{chapitre}-s{scène}-i{interaction} ».
    """

    __tablename__ = "angoff_ratings"
    __table_args__ = (UniqueConstraint("book_slug", "point", "judge"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_slug: Mapped[str] = mapped_column(String(80), index=True)
    point: Mapped[str] = mapped_column(String(40))
    chapter_id: Mapped[int] = mapped_column(Integer)
    judge: Mapped[str] = mapped_column(String(80))
    response_no: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(Text, default="")
    uploaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
