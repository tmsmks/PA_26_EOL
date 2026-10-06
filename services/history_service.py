"""Historique d'un participant : niveaux par chapitre, profil du livre, sessions."""
from __future__ import annotations

from typing import Any

from books import BOOKS
from domain.models import Chapter
from repositories.orm import BookSession, ChapterPassage
from services.scoring_service import book_profile, chapter_level
from services.session_service import as_utc


def completed_with_results(sessions: list[BookSession]) -> list[BookSession]:
    """Sessions terminées et notées, de la plus ancienne à la plus récente."""
    return sorted(
        (s for s in sessions if s.is_completed and s.results),
        key=lambda s: s.number,
    )


def chapter_progress(passages: list[ChapterPassage]) -> dict[str, Any] | None:
    """Niveau d'un chapitre : ses passages terminés et comptés, dans l'ordre."""
    counted = [
        p.results
        for p in sorted(passages, key=lambda p: (as_utc(p.started_at), p.id))
        if p.is_completed and p.counted and p.results
    ]
    return chapter_level(counted)


def book_progress(chapters: list[Chapter], passages: list[ChapterPassage]) -> dict[str, Any]:
    """Niveau de chaque chapitre et profil du livre, sans session obligatoire."""
    by_chapter: dict[int, list[ChapterPassage]] = {}
    for p in passages:
        if p.is_completed:
            by_chapter.setdefault(p.chapter_id, []).append(p)
    rows = []
    levels: dict[int, dict[str, Any] | None] = {}
    for ch in chapters:
        done = by_chapter.get(ch.Id, [])
        level = chapter_progress(done)
        levels[ch.Id] = level
        rows.append({
            "id": ch.Id,
            "name": ch.Name,
            "level": level,
            "n_practice": sum(1 for p in done if not p.counted),
            "last_at": max((p.completed_at for p in done), key=as_utc, default=None),
        })
    return {"chapters": rows, "profile": book_profile(levels, len(chapters))}


def book_history(
    book: dict[str, Any],
    sessions: list[BookSession],
    chapters: list[Chapter],
    passages: list[ChapterPassage],
) -> dict[str, Any]:
    items = []
    for s in sorted(sessions, key=lambda s: s.number, reverse=True):
        items.append({
            "id": s.id,
            "number": s.number,
            "status": s.status,
            "started_at": s.started_at,
            "completed_at": s.completed_at,
            "updated_at": s.updated_at,
            "global": (s.results or {}).get("global"),
            "n_done": len(s.completed_chapters or []),
            "n_chapters": len(chapters),
        })
    return {
        "book": book,
        "sessions": items,
        "progress": book_progress(chapters, passages),
        "in_progress": next((i for i in items if i["status"] != "completed"), None),
    }


def user_history(
    sessions: list[BookSession],
    passages: list[ChapterPassage],
    chapters_by_book: dict[str, list[Chapter]],
) -> list[dict[str, Any]]:
    """Un bloc par livre joué, dans l'ordre de `BOOKS`."""
    blocks = []
    for book in BOOKS:
        mine = [s for s in sessions if s.book_slug == book["slug"]]
        if mine:
            blocks.append(book_history(
                dict(book),
                mine,
                chapters_by_book.get(book["slug"], []),
                [p for p in passages if p.book_slug == book["slug"]],
            ))
    return blocks
