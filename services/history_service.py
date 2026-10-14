"""Historique d'un participant : niveaux par chapitre, profil du livre, sessions."""
from __future__ import annotations

import statistics
from datetime import datetime
from typing import Any

from books import BOOKS
from domain.models import Chapter
from repositories.orm import BookSession, ChapterPassage
from services.scoring_service import COHORT_MIN, book_profile, chapter_level, critical_choices, quoted
from services.session_service import as_utc, passage_attempt_dicts


def completed_with_results(sessions: list[BookSession]) -> list[BookSession]:
    """Sessions terminées et notées, de la plus ancienne à la plus récente."""
    return sorted(
        (s for s in sessions if s.is_completed and s.results),
        key=lambda s: s.number,
    )


def _counted(passages: list[ChapterPassage]) -> list[ChapterPassage]:
    return [
        p
        for p in sorted(passages, key=lambda p: (as_utc(p.started_at), p.id))
        if p.is_completed and p.counted and p.results
    ]


def _passage_record(p: ChapterPassage) -> dict[str, Any]:
    """Résultats d'un passage, avec sa date et son nombre de réponses critiques
    (recalculé depuis les traces pour les passages notés avant le 13.10.2026)."""
    record = dict(p.results or {})
    record["completed_at"] = p.completed_at
    if "n_critical" not in record:
        record["n_critical"] = len(critical_choices(passage_attempt_dicts(p)))
    return record


def chapter_progress(
    passages: list[ChapterPassage],
    cohort_sd: float | None = None,
    now: datetime | None = None,
    thresholds: Any = None,
) -> dict[str, Any] | None:
    """Niveau d'un chapitre : ses passages terminés et comptés, dans l'ordre."""
    return chapter_level(
        [_passage_record(p) for p in _counted(passages)], now=now, cohort_sd=cohort_sd, thresholds=thresholds
    )


def open_critical(passages: list[ChapterPassage]) -> list[dict[str, Any]]:
    """Réponses critiques du dernier passage compté d'un chapitre (à débriefer)."""
    counted = _counted(passages)
    if not counted:
        return []
    return [
        {
            "scene_title": st.get("scene_title", ""),
            "prompt": st.get("prompt", ""),
            "text": quoted(st["choice"].get("text", "")),
            "rationale": st["choice"].get("rationale", ""),
        }
        for st in critical_choices(passage_attempt_dicts(counted[-1]))
    ]


def cohort_first_sds(passages: list[ChapterPassage], book_slug: str) -> dict[int, float | None]:
    """Écart-type, par chapitre, des 1ᵉʳˢ passages comptés de la cohorte.

    Sert au seuil du « progrès net » (un tiers d'écart-type). None tant que
    moins de `COHORT_MIN` personnes ont un premier passage noté.
    """
    firsts: dict[tuple[int, int], float] = {}
    for p in sorted(passages, key=lambda p: (as_utc(p.started_at), p.id)):
        if p.book_slug != book_slug or not (p.is_completed and p.counted and p.results):
            continue
        g = p.results.get("global")
        if g is not None:
            firsts.setdefault((p.chapter_id, p.user_id), g)
    by_chapter: dict[int, list[float]] = {}
    for (cid, _), g in firsts.items():
        by_chapter.setdefault(cid, []).append(g)
    return {
        cid: round(statistics.stdev(v), 1) if len(v) >= COHORT_MIN else None
        for cid, v in by_chapter.items()
    }


def cohorts_for(passages: list[ChapterPassage], slugs: Any) -> dict[str, dict[int, float | None]]:
    """Écarts-types de cohorte, livre par livre (voir `cohort_first_sds`)."""
    return {slug: cohort_first_sds(passages, slug) for slug in slugs}


def book_progress(
    chapters: list[Chapter],
    passages: list[ChapterPassage],
    cohort: dict[int, float | None] | None = None,
    now: datetime | None = None,
    thresholds: dict[int, Any] | None = None,
) -> dict[str, Any]:
    """Niveau de chaque chapitre et profil du livre, sans session obligatoire.

    `thresholds` : seuils de bande fixés par des juges, par chapitre (Angoff).
    """
    cohort = cohort or {}
    thresholds = thresholds or {}
    by_chapter: dict[int, list[ChapterPassage]] = {}
    for p in passages:
        if p.is_completed:
            by_chapter.setdefault(p.chapter_id, []).append(p)
    rows = []
    levels: dict[int, dict[str, Any] | None] = {}
    for ch in chapters:
        done = by_chapter.get(ch.Id, [])
        level = chapter_progress(done, cohort.get(ch.Id), now, thresholds.get(ch.Id))
        levels[ch.Id] = level
        rows.append({
            "id": ch.Id,
            "name": ch.Name,
            "level": level,
            "n_practice": sum(1 for p in done if not p.counted),
            "n_too_fast": sum(1 for p in done if ((p.results or {}).get("timing") or {}).get("too_fast")),
            "critical": open_critical(done) if level and level.get("critical_capped") else [],
            "last_at": max((p.completed_at for p in done), key=as_utc, default=None),
        })
    return {"chapters": rows, "profile": book_profile(levels, len(chapters))}


def book_history(
    book: dict[str, Any],
    sessions: list[BookSession],
    chapters: list[Chapter],
    passages: list[ChapterPassage],
    cohort: dict[int, float | None] | None = None,
    thresholds: dict[int, Any] | None = None,
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
        "progress": book_progress(chapters, passages, cohort, thresholds=thresholds),
        "in_progress": next((i for i in items if i["status"] != "completed"), None),
    }


def user_history(
    sessions: list[BookSession],
    passages: list[ChapterPassage],
    chapters_by_book: dict[str, list[Chapter]],
    cohorts: dict[str, dict[int, float | None]] | None = None,
    thresholds: dict[str, dict[int, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Un bloc par livre joué, dans l'ordre de `BOOKS`."""
    cohorts = cohorts or {}
    thresholds = thresholds or {}
    blocks = []
    for book in BOOKS:
        mine = [s for s in sessions if s.book_slug == book["slug"]]
        if mine:
            blocks.append(book_history(
                dict(book),
                mine,
                chapters_by_book.get(book["slug"], []),
                [p for p in passages if p.book_slug == book["slug"]],
                cohorts.get(book["slug"]),
                thresholds.get(book["slug"]),
            ))
    return blocks
