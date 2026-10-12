"""Repository des cotes d'experts (validation de la clé de cotation)."""
from __future__ import annotations

from typing import Any

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from repositories.orm import ExpertRating


class ExpertRatingRepository:
    def __init__(self, session: Session) -> None:
        self._s = session

    def for_book(self, book_slug: str, round_: int | None = None) -> list[ExpertRating]:
        q = select(ExpertRating).where(ExpertRating.book_slug == book_slug)
        if round_ is not None:
            q = q.where(ExpertRating.round == round_)
        return list(self._s.scalars(q.order_by(ExpertRating.expert, ExpertRating.id)))

    def summary(self, book_slug: str) -> list[dict[str, Any]]:
        """Une ligne par (tour, expert) : nombre de réponses cotées, dernière importation."""
        rows = self._s.execute(
            select(
                ExpertRating.round,
                ExpertRating.expert,
                func.count(ExpertRating.id),
                func.max(ExpertRating.uploaded_at),
            )
            .where(ExpertRating.book_slug == book_slug)
            .group_by(ExpertRating.round, ExpertRating.expert)
            .order_by(ExpertRating.round, ExpertRating.expert)
        )
        return [
            {"round": r, "expert": e, "n": n, "uploaded_at": at} for r, e, n, at in rows
        ]

    def replace(
        self, book_slug: str, expert: str, round_: int, ratings: list[dict[str, Any]]
    ) -> int:
        """Remplace toutes les cotes de cet expert pour ce tour (réimporter = corriger)."""
        self._delete(book_slug, expert, round_)
        for r in ratings:
            self._s.add(ExpertRating(book_slug=book_slug, expert=expert, round=round_, **r))
        self._s.commit()
        return len(ratings)

    def delete(self, book_slug: str, expert: str, round_: int) -> None:
        self._delete(book_slug, expert, round_)
        self._s.commit()

    def _delete(self, book_slug: str, expert: str, round_: int) -> None:
        self._s.execute(
            delete(ExpertRating).where(
                ExpertRating.book_slug == book_slug,
                ExpertRating.expert == expert,
                ExpertRating.round == round_,
            )
        )
