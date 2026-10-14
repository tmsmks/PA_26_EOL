"""API des sessions de jeu — appelée par le parcours joueur (static/play)."""
from __future__ import annotations

from typing import Any

from flask import Blueprint, current_app, jsonify, request, url_for

from books import get_book
from repositories.database import db_session
from repositories.orm import BookSession, ChapterPassage
from repositories.passages import PassageRepository
from repositories.sessions import SessionRepository
from services.history_service import chapter_progress, cohort_first_sds, completed_with_results
from services.scoring_service import InvalidPathError, chapter_review, scene_review, weighted_profile
from services.session_service import PlaySessionService, SessionError, passage_attempt_dicts
from views.guards import current_user, login_required
from views.scoring_context import book_thresholds

session_api_bp = Blueprint("session_api", __name__, url_prefix="/api")


def play_service() -> PlaySessionService:
    return PlaySessionService(
        db_session(),
        current_app.extensions["eol_chapters"],
        current_app.config["PASSAGE_SPACING_DAYS"],
    )



def session_payload(bs: BookSession) -> dict[str, Any]:
    return {
        "id": bs.id,
        "number": bs.number,
        "book_slug": bs.book_slug,
        "status": bs.status,
        "flags": list(bs.flags or []),
        "completed_chapters": list(bs.completed_chapters or []),
        "urls": {
            "attempts": url_for("session_api.record_attempt", session_id=bs.id),
            "complete": url_for("session_api.complete_chapter", session_id=bs.id),
            "passages": url_for("session_api.start_passage", session_id=bs.id),
            "report": url_for("account.session_report", session_id=bs.id),
        },
    }


def passage_payload(p: ChapterPassage) -> dict[str, Any]:
    results = p.results or {}
    timing = results.get("timing") or {}
    return {
        "id": p.id,
        "chapter_id": p.chapter_id,
        "status": p.status,
        "counted": p.counted,
        "flags": list(p.flags_in or []),
        "global": results.get("global"),
        "n_choices": results.get("n_choices"),
        "n_critical": results.get("n_critical"),
        "too_fast": bool(timing.get("too_fast")),
        "timing": timing or None,
    }


def _load(session_id: int, allow_trainer: bool = False) -> BookSession:
    bs = SessionRepository(db_session()).get(session_id)
    user = current_user()
    if bs is None:
        raise SessionError("Session introuvable.", 404)
    if bs.user_id != user.id and not (allow_trainer and user.is_trainer):
        raise SessionError("Cette session ne vous appartient pas.", 403)
    return bs


def _int(payload: dict, key: str) -> int:
    try:
        return int(payload[key])
    except (KeyError, TypeError, ValueError):
        raise SessionError(f"Champ « {key} » manquant ou invalide.") from None


@session_api_bp.errorhandler(SessionError)
def _session_error(e: SessionError):
    return jsonify({"error": str(e)}), e.status


@session_api_bp.errorhandler(InvalidPathError)
def _path_error(e: InvalidPathError):
    return jsonify({"error": str(e)}), 400


@session_api_bp.route("/play/<book_slug>/session", methods=["POST"])
@login_required
def start_session(book_slug: str):
    """Reprend la session en cours du livre, ou en démarre une nouvelle."""
    try:
        get_book(book_slug)
    except ValueError:
        raise SessionError("Livre inconnu.", 404) from None
    bs = play_service().get_or_start(current_user(), book_slug)
    return jsonify({"session": session_payload(bs)})


@session_api_bp.route("/sessions/<int:session_id>/passages", methods=["POST"])
@login_required
def start_passage(session_id: int):
    """Ouvre (ou reprend) le passage d'un chapitre ; renvoie les états de départ."""
    payload = request.get_json(silent=True) or {}
    passage = play_service().start_passage(_load(session_id), _int(payload, "chapter_id"))
    return jsonify({"passage": passage_payload(passage)})


@session_api_bp.route("/sessions/<int:session_id>/attempts", methods=["POST"])
@login_required
def record_attempt(session_id: int):
    payload = request.get_json(silent=True) or {}
    choices = payload.get("choices")
    if not isinstance(choices, list) or not all(isinstance(c, int) for c in choices):
        raise SessionError("« choices » doit être une liste d'indices.")
    passage_id = payload.get("passage_id")
    if passage_id is not None and not isinstance(passage_id, int):
        raise SessionError("« passage_id » invalide.")
    bs = _load(session_id)
    attempt = play_service().record_attempt(
        bs,
        chapter_id=_int(payload, "chapter_id"),
        scene_id=_int(payload, "scene_id"),
        entry_id=_int(payload, "entry_id"),
        choices=choices,
        flags=payload.get("flags"),
        passage_id=passage_id,
        times=payload.get("times"),
    )
    return jsonify({
        "counted": attempt.counted,
        "attempt_no": attempt.attempt_no,
        # Retour de fin de scène : ce qui était attendu, et pourquoi.
        "review": scene_review(attempt.trace or []),
    })


@session_api_bp.route("/sessions/<int:session_id>/complete-chapter", methods=["POST"])
@login_required
def complete_chapter(session_id: int):
    payload = request.get_json(silent=True) or {}
    bs = _load(session_id)
    chapter_id = _int(payload, "chapter_id")
    book_done, passage = play_service().complete_chapter(bs, chapter_id, payload.get("flags"))
    repo = PassageRepository(db_session())
    passages = repo.list_for_user(bs.user_id, bs.book_slug, chapter_id, completed_only=True)
    cohort = cohort_first_sds(repo.list_all(book_slug=bs.book_slug), bs.book_slug)
    return jsonify({
        "book_completed": book_done,
        "session": session_payload(bs),
        "passage": passage_payload(passage),
        "progress": chapter_progress(
            passages,
            cohort.get(chapter_id),
            thresholds=book_thresholds(
                bs.book_slug, current_app.extensions["eol_chapters"].load_chapters(bs.book_slug)
            ).get(chapter_id),
        ),
        # Feedback d'abord (proposition v3, § 2.7) : ce qu'il faut retenir du
        # chapitre, puis la tendance par compétence ; la note se lit à la demande.
        "review": chapter_review(passage_attempt_dicts(passage)),
        "trend": {
            "strengths": (passage.results or {}).get("strengths") or [],
            "weaknesses": (passage.results or {}).get("weaknesses") or [],
        },
    })


@session_api_bp.route("/sessions/<int:session_id>/feedback", methods=["POST"])
@login_required
def session_feedback(session_id: int):
    """Retourne le feedback général, en le générant au premier appel."""
    payload = request.get_json(silent=True) or {}
    user = current_user()
    bs = _load(session_id, allow_trainer=True)
    if not bs.is_completed or not bs.results:
        raise SessionError("Le feedback est disponible à la fin du livre.", 409)

    regenerate = bool(payload.get("regenerate"))
    if bs.feedback and regenerate:
        # Un participant ne peut relancer que si l'IA avait échoué.
        if bs.feedback.get("source") == "ai" and not user.is_trainer:
            raise SessionError("Le feedback a déjà été généré.", 403)
    if bs.feedback and not regenerate:
        return jsonify({"feedback": bs.feedback})

    repo = SessionRepository(db_session())
    history = [
        s for s in completed_with_results(repo.list_for_user(bs.user_id, bs.book_slug))
        if s.number <= bs.number
    ]
    previous = [
        {
            "number": s.number,
            "completed_on": s.completed_at.strftime("%d.%m.%Y") if s.completed_at else "?",
            "results": s.results,
            "feedback": s.feedback,
        }
        for s in reversed(history)
        if s.number < bs.number
    ]
    feedback = current_app.extensions["eol_feedback"].generate(
        get_book(bs.book_slug),
        bs.number,
        bs.results,
        previous,
        weighted_profile([s.results for s in history]),
    )
    bs.feedback = feedback
    repo.save(bs)
    return jsonify({"feedback": feedback})
