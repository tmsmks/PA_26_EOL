"""Reprise des données du scoring v1 vers le v2 — au démarrage, idempotente.

1. Les sessions jouées avant le v2 n'ont pas de passages : on en crée un par
   chapitre joué (terminé ou en cours), avec ses tentatives, et on applique
   la règle d'espacement dans l'ordre chronologique.
2. Les traces v1 ne gardent pas les bornes des réponses proposées : on les
   reprend du livre actuel (un pas dont l'interaction a changé reste non noté).
3. Les bilans de session v1 sont recalculés avec la qualité des choix ;
   l'ancien bilan reste en entier dans `results["v1"]`.
"""
from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models import Chapter, Scene
from repositories.chapters import ChapterRepository
from repositories.orm import (
    STATUS_COMPLETED,
    STATUS_IN_PROGRESS,
    BookSession,
    ChapterPassage,
    SceneAttempt,
)
from services.scoring_service import enrich_trace, passage_results, session_results
from services.session_service import passage_attempt_dicts, recount


def _chapters(repo: ChapterRepository, cache: dict[str, list[Chapter]], slug: str) -> list[Chapter]:
    if slug not in cache:
        try:
            cache[slug] = repo.load_chapters(slug)
        except (OSError, ValueError):  # livre retiré ou renommé depuis
            cache[slug] = []
    return cache[slug]


def _enrich(attempts: list[SceneAttempt], scenes: dict[tuple[int, int], Scene]) -> None:
    for a in attempts:
        scene = scenes.get((a.chapter_id, a.scene_id))
        if scene is not None and any("bounds" not in st for st in a.trace or []):
            a.trace = enrich_trace(scene, a.trace)


def upgrade_scoring(db: Session, repo: ChapterRepository, spacing_days: int) -> dict[str, int]:
    """Met la base au format du scoring v2. Retourne ce qui a été repris."""
    cache: dict[str, list[Chapter]] = {}
    stats = {"passages": 0, "sessions": 0}

    legacy = db.scalars(
        select(BookSession).where(BookSession.attempts.any(), ~BookSession.passages.any())
    ).all()
    touched: set[tuple[int, str]] = set()
    for bs in legacy:
        chapters = _chapters(repo, cache, bs.book_slug)
        _enrich(bs.attempts, {(ch.Id, s.Id): s for ch in chapters for s in ch.Scenes})
        by_chapter: dict[int, list[SceneAttempt]] = {}
        for a in sorted(bs.attempts, key=lambda a: a.id):
            by_chapter.setdefault(a.chapter_id, []).append(a)
        for chapter_id, attempts in by_chapter.items():
            done = chapter_id in (bs.completed_chapters or [])
            passage = ChapterPassage(
                user_id=bs.user_id,
                session_id=bs.id,
                book_slug=bs.book_slug,
                chapter_id=chapter_id,
                status=STATUS_COMPLETED if done else STATUS_IN_PROGRESS,
                counted=True,
                started_at=min(a.created_at for a in attempts),
                completed_at=max(a.created_at for a in attempts) if done else None,
                flags_in=[],
            )
            passage.attempts = attempts
            if done:
                passage.results = passage_results(passage_attempt_dicts(passage))
            db.add(passage)
            stats["passages"] += 1
        touched.add((bs.user_id, bs.book_slug))
    db.flush()

    for user_id, slug in touched:
        recount(
            list(db.scalars(select(ChapterPassage).where(
                ChapterPassage.user_id == user_id, ChapterPassage.book_slug == slug
            ))),
            spacing_days,
        )

    for bs in db.scalars(select(BookSession).where(BookSession.status == STATUS_COMPLETED)):
        if not bs.results or bs.results.get("version") == 2:
            continue
        old = bs.results
        chapters = _chapters(repo, cache, bs.book_slug)
        latest: dict[int, ChapterPassage] = {}
        for p in bs.passages:
            if p.is_completed:
                latest[p.chapter_id] = p
        attempts = [d for p in latest.values() for d in passage_attempt_dicts(p)]
        results = session_results(chapters, attempts)
        results["v1"] = old
        bs.results = results
        stats["sessions"] += 1

    db.commit()
    return stats
