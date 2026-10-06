"""Repository des sessions de livre et des tentatives de scène."""
from __future__ import annotations

from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from repositories.orm import (
    STATUS_COMPLETED,
    STATUS_IN_PROGRESS,
    BookSession,
    SceneAttempt,
    utcnow,
)


class SessionRepository:
    def __init__(self, session: Session) -> None:
        self._s = session

    def get(self, session_id: int) -> BookSession | None:
        return self._s.get(BookSession, session_id)

    def in_progress(self, user_id: int, book_slug: str) -> BookSession | None:
        return self._s.scalar(
            select(BookSession)
            .where(
                BookSession.user_id == user_id,
                BookSession.book_slug == book_slug,
                BookSession.status == STATUS_IN_PROGRESS,
            )
            .order_by(BookSession.number.desc())
        )

    def list_for_user(
        self,
        user_id: int,
        book_slug: str | None = None,
        completed_only: bool = False,
    ) -> list[BookSession]:
        """Sessions d'un participant, de la plus ancienne à la plus récente."""
        q = select(BookSession).where(BookSession.user_id == user_id)
        if book_slug is not None:
            q = q.where(BookSession.book_slug == book_slug)
        if completed_only:
            q = q.where(BookSession.status == STATUS_COMPLETED)
        return list(self._s.scalars(q.order_by(BookSession.book_slug, BookSession.number)))

    def list_all(self) -> list[BookSession]:
        """Toutes les sessions (tableau de bord formateur)."""
        return list(self._s.scalars(select(BookSession).order_by(BookSession.id)))

    def list_for_export(
        self, user_id: int | None = None, book_slug: str | None = None
    ) -> list[BookSession]:
        """Sessions avec leur compte et toutes leurs tentatives (export des données)."""
        q = select(BookSession).options(
            selectinload(BookSession.user), selectinload(BookSession.attempts)
        )
        if user_id is not None:
            q = q.where(BookSession.user_id == user_id)
        if book_slug is not None:
            q = q.where(BookSession.book_slug == book_slug)
        return list(self._s.scalars(q.order_by(BookSession.id)))

    def create(self, user_id: int, book_slug: str) -> BookSession:
        last = self._s.scalar(
            select(func.max(BookSession.number)).where(
                BookSession.user_id == user_id, BookSession.book_slug == book_slug
            )
        )
        book_session = BookSession(
            user_id=user_id,
            book_slug=book_slug,
            number=(last or 0) + 1,
            flags=[],
            completed_chapters=[],
        )
        self._s.add(book_session)
        self._s.commit()
        return book_session

    def delete(self, book_session: BookSession) -> None:
        self._s.delete(book_session)
        self._s.commit()

    def add_attempt(self, book_session: BookSession, **fields: Any) -> SceneAttempt:
        attempt = SceneAttempt(session_id=book_session.id, **fields)
        self._s.add(attempt)
        book_session.updated_at = utcnow()
        self._s.commit()
        return attempt

    def save(self, book_session: BookSession) -> None:
        """Valide les modifications faites sur la session (flags, statut…)."""
        book_session.updated_at = utcnow()
        self._s.commit()
