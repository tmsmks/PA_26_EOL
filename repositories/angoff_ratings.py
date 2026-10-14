"""Repository des choix des juges pour les seuils de niveau (Angoff modifié)."""
from __future__ import annotations

from typing import Any

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from repositories.orm import AngoffRating


class AngoffRatingRepository:
    def __init__(self, session: Session) -> None:
        self._s = session

    def for_book(self, book_slug: str) -> list[AngoffRating]:
        q = select(AngoffRating).where(AngoffRating.book_slug == book_slug)
        return list(self._s.scalars(q.order_by(AngoffRating.judge, AngoffRating.id)))

    def summary(self, book_slug: str) -> list[dict[str, Any]]:
        """Une ligne par juge : nombre de points de choix jugés, dernière importation."""
        rows = self._s.execute(
            select(AngoffRating.judge, func.count(AngoffRating.id), func.max(AngoffRating.uploaded_at))
            .where(AngoffRating.book_slug == book_slug)
            .group_by(AngoffRating.judge)
            .order_by(AngoffRating.judge)
        )
        return [{"judge": j, "n": n, "uploaded_at": at} for j, n, at in rows]

    def replace(self, book_slug: str, judge: str, picks: list[dict[str, Any]]) -> int:
        """Remplace tous les choix de ce ou cette juge (réimporter = corriger)."""
        self._delete(book_slug, judge)
        for p in picks:
            self._s.add(AngoffRating(book_slug=book_slug, judge=judge, **p))
        self._s.commit()
        return len(picks)

    def delete(self, book_slug: str, judge: str) -> None:
        self._delete(book_slug, judge)
        self._s.commit()

    def _delete(self, book_slug: str, judge: str) -> None:
        self._s.execute(
            delete(AngoffRating).where(AngoffRating.book_slug == book_slug, AngoffRating.judge == judge)
        )
