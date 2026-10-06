"""Cycle de vie d'une session et de ses passages de chapitre.

Règles (scoring v2) :
- un participant a au plus une session en cours par livre ; la session porte
  les états narratifs de l'histoire d'un chapitre à l'autre ;
- jouer un chapitre en entier = un **passage**, l'unité de note. Un passage
  compte dans le niveau du chapitre si c'est le premier, ou s'il commence au
  moins `spacing_days` jours après la fin du dernier passage compté de ce
  chapitre ; sinon c'est de l'entraînement (rejouer de suite gonfle le score
  par simple mémorisation) ;
- dans un passage, seule la 1ʳᵉ tentative d'une scène est notée ;
- rejouer un chapitre seul (sans les précédents dans la session) repart des
  états narratifs du début de son dernier passage ;
- la session est terminée quand tous les chapitres le sont ; son bilan est
  alors figé dans `BookSession.results`.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from sqlalchemy.orm import Session

from books import get_book
from domain.models import Chapter, Scene
from repositories.chapters import ChapterRepository
from repositories.orm import (
    STATUS_COMPLETED,
    STATUS_IN_PROGRESS,
    BookSession,
    ChapterPassage,
    SceneAttempt,
    User,
    utcnow,
)
from repositories.passages import PassageRepository
from repositories.sessions import SessionRepository
from services.scoring_service import passage_results, replay_scene, session_results

MAX_FLAGS = 200
MAX_FLAG_LEN = 80
PASSAGE_SPACING_DAYS = 7


class SessionError(ValueError):
    """Requête incohérente avec l'état de la session (→ HTTP 4xx)."""

    def __init__(self, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.status = status


def clean_flags(flags: Any) -> list[str]:
    if not isinstance(flags, list):
        return []
    out = sorted({str(f)[:MAX_FLAG_LEN] for f in flags if str(f).strip()})
    return out[:MAX_FLAGS]


def attempt_dict(a: SceneAttempt) -> dict[str, Any]:
    return {
        "chapter_id": a.chapter_id,
        "scene_id": a.scene_id,
        "scene_title": a.scene_title,
        "raw": a.raw,
        "lo": a.lo,
        "hi": a.hi,
        "trace": a.trace,
    }


def as_utc(value: datetime | None) -> datetime | None:
    """SQLite ne conserve pas le fuseau : une date sans fuseau est de l'UTC."""
    if value is None or value.tzinfo is not None:
        return value
    return value.replace(tzinfo=timezone.utc)


def scored_attempts(attempts: list[SceneAttempt]) -> list[SceneAttempt]:
    """Première tentative de chaque scène, dans l'ordre d'enregistrement."""
    seen: set[tuple[int, int]] = set()
    out = []
    for a in sorted(attempts, key=lambda a: a.id):
        key = (a.chapter_id, a.scene_id)
        if key not in seen:
            seen.add(key)
            out.append(a)
    return out


def countable(last_counted_end: datetime | None, start: datetime, spacing_days: int) -> bool:
    """Un passage compte s'il est le premier ou assez espacé du précédent compté."""
    if last_counted_end is None:
        return True
    return as_utc(start) - as_utc(last_counted_end) >= timedelta(days=spacing_days)


def next_counted_date(last_counted_end: datetime | None, spacing_days: int) -> datetime | None:
    if last_counted_end is None:
        return None
    return as_utc(last_counted_end) + timedelta(days=spacing_days)


def recount(passages: list[ChapterPassage], spacing_days: int) -> None:
    """Réapplique la règle d'espacement, chapitre par chapitre, dans l'ordre.

    Sert après une reprise de données (passages antidatés, historique v1).
    Met aussi à jour `counted` des tentatives : notée = passage compté et
    1ʳᵉ tentative de la scène dans le passage.
    """
    groups: dict[tuple[int, str, int], list[ChapterPassage]] = {}
    for p in passages:
        groups.setdefault((p.user_id, p.book_slug, p.chapter_id), []).append(p)
    for group in groups.values():
        last_end: datetime | None = None
        for p in sorted(group, key=lambda p: (as_utc(p.started_at), p.id)):
            p.counted = countable(last_end, p.started_at, spacing_days)
            if p.counted and p.is_completed:
                last_end = p.completed_at
            first = {a.id for a in scored_attempts(p.attempts)}
            for a in p.attempts:
                a.counted = p.counted and a.id in first


def passage_attempt_dicts(passage: ChapterPassage) -> list[dict[str, Any]]:
    return [attempt_dict(a) for a in scored_attempts(passage.attempts)]


class PlaySessionService:
    def __init__(
        self, db: Session, chapters: ChapterRepository, spacing_days: int = PASSAGE_SPACING_DAYS
    ) -> None:
        self._db = db
        self._sessions = SessionRepository(db)
        self._passages = PassageRepository(db)
        self._chapters = chapters
        self.spacing_days = spacing_days

    # --- Démarrage ----------------------------------------------------------

    def get_or_start(self, user: User, book_slug: str) -> BookSession:
        book = get_book(book_slug)
        current = self._sessions.in_progress(user.id, book["slug"])
        return current or self._sessions.create(user.id, book["slug"])

    def restart(self, user: User, book_slug: str) -> BookSession:
        """Abandonne la session en cours (supprimée, avec ses passages) et en démarre une neuve."""
        book = get_book(book_slug)
        current = self._sessions.in_progress(user.id, book["slug"])
        if current is not None:
            self._sessions.delete(current)
        return self._sessions.create(user.id, book["slug"])

    # --- Passages -----------------------------------------------------------

    def _last_counted_end(self, user_id: int, book_slug: str, chapter_id: int) -> datetime | None:
        done = self._passages.list_for_user(user_id, book_slug, chapter_id, completed_only=True)
        ends = [p.completed_at for p in done if p.counted and p.completed_at]
        return max(ends, key=as_utc) if ends else None

    def outlook(self, user_id: int, book_slug: str, chapter_id: int) -> dict[str, Any]:
        """Un passage commencé maintenant compterait-il ? (affiché avant de jouer)"""
        done = self._passages.list_for_user(user_id, book_slug, chapter_id, completed_only=True)
        last_end = self._last_counted_end(user_id, book_slug, chapter_id)
        counted = countable(last_end, utcnow(), self.spacing_days)
        return {
            "counted": counted,
            "n_counted": sum(1 for p in done if p.counted),
            "last_counted_at": last_end,
            "next_counted_at": None if counted else next_counted_date(last_end, self.spacing_days),
        }

    def start_passage(self, book_session: BookSession, chapter_id: int) -> ChapterPassage:
        """Reprend le passage en cours de ce chapitre dans la session, ou en ouvre un."""
        self._ensure_open(book_session)
        chapters = self._chapters.load_chapters(book_session.book_slug)
        ids = [ch.Id for ch in chapters]
        if chapter_id not in ids:
            raise SessionError(f"Chapitre {chapter_id} introuvable.", 404)
        current = self._passages.in_progress(book_session.id, chapter_id)
        if current is not None:
            return current

        # L'histoire continue si un chapitre précédent a été joué dans cette
        # session ; sinon (chapitre rejoué seul), on repart des états du début
        # de son dernier passage.
        before = set(ids[: ids.index(chapter_id)])
        flags = list(book_session.flags or [])
        if not before & set(book_session.completed_chapters or []):
            done = self._passages.list_for_user(
                book_session.user_id, book_session.book_slug, chapter_id, completed_only=True
            )
            if done:
                flags = list(done[-1].flags_in or [])

        now = utcnow()
        last_end = self._last_counted_end(book_session.user_id, book_session.book_slug, chapter_id)
        return self._passages.create(
            book_session,
            chapter_id,
            status=STATUS_IN_PROGRESS,
            counted=countable(last_end, now, self.spacing_days),
            started_at=now,
            flags_in=clean_flags(flags),
        )

    def _passage_for(
        self, book_session: BookSession, chapter_id: int, passage_id: int | None
    ) -> ChapterPassage:
        if passage_id is None:
            return self.start_passage(book_session, chapter_id)
        passage = self._passages.get(passage_id)
        if (
            passage is None
            or passage.session_id != book_session.id
            or passage.chapter_id != chapter_id
        ):
            raise SessionError("Passage introuvable pour ce chapitre.", 404)
        if passage.is_completed:
            raise SessionError("Ce passage est terminé : rechargez la page pour en commencer un autre.", 409)
        return passage

    # --- Jeu ----------------------------------------------------------------

    def _chapter(self, book_slug: str, chapter_id: int) -> Chapter:
        chapter = self._chapters.find_chapter(book_slug, chapter_id)
        if chapter is None:
            raise SessionError(f"Chapitre {chapter_id} introuvable.", 404)
        return chapter

    @staticmethod
    def _scene(chapter: Chapter, scene_id: int) -> Scene:
        scene = next((s for s in chapter.Scenes if s.Id == scene_id), None)
        if scene is None:
            raise SessionError(f"Scène {scene_id} introuvable dans le chapitre {chapter.Id}.", 404)
        return scene

    @staticmethod
    def _ensure_open(book_session: BookSession) -> None:
        if book_session.is_completed:
            raise SessionError("Cette session est terminée. Rechargez la page pour en commencer une nouvelle.", 409)

    def record_attempt(
        self,
        book_session: BookSession,
        chapter_id: int,
        scene_id: int,
        entry_id: int,
        choices: list[int],
        flags: Any = None,
        passage_id: int | None = None,
    ) -> SceneAttempt:
        """Rejoue et enregistre une scène terminée (InvalidPathError si incohérente)."""
        self._ensure_open(book_session)
        chapter = self._chapter(book_session.book_slug, chapter_id)
        scene = self._scene(chapter, scene_id)
        run = replay_scene(scene, entry_id, choices)
        passage = self._passage_for(book_session, chapter_id, passage_id)

        previous = sum(1 for a in passage.attempts if a.scene_id == scene_id)
        if flags is not None:
            book_session.flags = clean_flags(flags)
        attempt = self._sessions.add_attempt(
            book_session,
            chapter_id=chapter_id,
            scene_id=scene_id,
            scene_title=scene.Title[:255],
            attempt_no=previous + 1,
            counted=passage.counted and previous == 0,
            entry_id=entry_id,
            raw=run.raw,
            lo=run.lo,
            hi=run.hi,
            trace=run.trace,
        )
        self._passages.link_attempt(passage, attempt)
        return attempt

    def complete_chapter(
        self, book_session: BookSession, chapter_id: int, flags: Any = None
    ) -> tuple[bool, ChapterPassage]:
        """Clôt le passage du chapitre et marque le chapitre terminé.

        Retourne (livre terminé ?, passage clos).
        """
        self._ensure_open(book_session)
        chapters = self._chapters.load_chapters(book_session.book_slug)
        if chapter_id not in {ch.Id for ch in chapters}:
            raise SessionError(f"Chapitre {chapter_id} introuvable.", 404)

        passage = self.start_passage(book_session, chapter_id)
        passage.status = STATUS_COMPLETED
        passage.completed_at = utcnow()
        passage.results = passage_results(passage_attempt_dicts(passage))

        done = set(book_session.completed_chapters or []) | {chapter_id}
        book_session.completed_chapters = sorted(done)
        if flags is not None:
            book_session.flags = clean_flags(flags)

        book_done = {ch.Id for ch in chapters} <= done
        if book_done:
            book_session.results = self.compute_results(book_session, chapters)
            book_session.status = STATUS_COMPLETED
            book_session.completed_at = utcnow()
        self._sessions.save(book_session)
        return book_done, passage

    def compute_results(
        self, book_session: BookSession, chapters: list[Chapter] | None = None
    ) -> dict[str, Any]:
        if chapters is None:
            chapters = self._chapters.load_chapters(book_session.book_slug)
        return results_from_passages(book_session, chapters)


def results_from_passages(book_session: BookSession, chapters: list[Chapter]) -> dict[str, Any]:
    """Bilan d'une session : pour chaque chapitre, son dernier passage dans la session
    (terminé de préférence, sinon celui en cours : résultats provisoires)."""
    latest: dict[int, ChapterPassage] = {}
    for p in book_session.passages:
        if p.is_completed or p.chapter_id not in latest or not latest[p.chapter_id].is_completed:
            latest[p.chapter_id] = p
    attempts = [d for p in latest.values() for d in passage_attempt_dicts(p)]
    return session_results(chapters, attempts)
