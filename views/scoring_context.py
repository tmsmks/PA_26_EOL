"""Contexte de notation partagé par les pages : seuils de bande fixés par des juges."""
from __future__ import annotations

from typing import Any

from domain.models import Chapter
from repositories.angoff_ratings import AngoffRatingRepository
from repositories.database import db_session
from services.angoff_service import angoff_points, chapter_thresholds, cut_scores


def book_thresholds(book_slug: str, chapters: list[Chapter]) -> dict[int, Any]:
    """Seuils appliqués de chaque chapitre (Angoff, au moins 3 juges), sinon vide."""
    ratings = AngoffRatingRepository(db_session()).for_book(book_slug)
    if not ratings or not chapters:
        return {}
    picks = [{"judge": r.judge, "point": r.point, "response_no": r.response_no} for r in ratings]
    return chapter_thresholds(cut_scores(angoff_points(chapters), picks))


def thresholds_for(chapters_by_book: dict[str, list[Chapter]]) -> dict[str, dict[int, Any]]:
    return {slug: book_thresholds(slug, chs) for slug, chs in chapters_by_book.items()}
