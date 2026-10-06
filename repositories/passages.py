"""Repository des passages de chapitre (unité de note du scoring v2)."""
from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from repositories.orm import (
    STATUS_COMPLETED,
    STATUS_IN_PROGRESS,
    BookSession,
    ChapterPassage,
    SceneAttempt,
)


class PassageRepository:
    def __init__(self, session: Session) -> None:
        self._s = session

    def get(self, passage_id: int) -> ChapterPassage | None:
        return self._s.get(ChapterPassage, passage_id)

    def in_progress(self, session_id: int, chapter_id: int) -> ChapterPassage | None:
        return self._s.scalar(
            select(ChapterPassage)
            .where(
                ChapterPassage.session_id == session_id,
                ChapterPassage.chapter_id == chapter_id,
                ChapterPassage.status == STATUS_IN_PROGRESS,
            )
            .order_by(ChapterPassage.id.desc())
        )

    def list_for_user(
        self,
        user_id: int,
        book_slug: str | None = None,
        chapter_id: int | None = None,
        completed_only: bool = False,
    ) -> list[ChapterPassage]:
        """Passages d'un participant, du plus ancien au plus récent."""
        q = select(ChapterPassage).where(ChapterPassage.user_id == user_id)
        if book_slug is not None:
            q = q.where(ChapterPassage.book_slug == book_slug)
        if chapter_id is not None:
            q = q.where(ChapterPassage.chapter_id == chapter_id)
        if completed_only:
            q = q.where(ChapterPassage.status == STATUS_COMPLETED)
        return list(self._s.scalars(q.order_by(ChapterPassage.started_at, ChapterPassage.id)))

    def list_all(
        self, user_id: int | None = None, book_slug: str | None = None
    ) -> list[ChapterPassage]:
        """Tous les passages (espace formateur, export), avec leurs tentatives."""
        q = select(ChapterPassage).options(selectinload(ChapterPassage.attempts))
        if user_id is not None:
            q = q.where(ChapterPassage.user_id == user_id)
        if book_slug is not None:
            q = q.where(ChapterPassage.book_slug == book_slug)
        return list(self._s.scalars(q.order_by(ChapterPassage.started_at, ChapterPassage.id)))

    def create(self, book_session: BookSession, chapter_id: int, **fields: Any) -> ChapterPassage:
        passage = ChapterPassage(
            user_id=book_session.user_id,
            session_id=book_session.id,
            book_slug=book_session.book_slug,
            chapter_id=chapter_id,
            **fields,
        )
        self._s.add(passage)
        self._s.commit()
        return passage

    def link_attempt(self, passage: ChapterPassage, attempt: SceneAttempt) -> None:
        passage.attempts.append(attempt)
        self._s.commit()

    def save(self, passage: ChapterPassage) -> None:
        self._s.commit()
