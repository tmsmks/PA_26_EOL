"""Pages HTML — rendu dynamique via Jinja (pas de build statique)."""
from __future__ import annotations

from flask import Blueprint, abort, current_app, redirect, render_template, url_for

from books import BOOKS, get_book
from repositories.chapters import ChapterRepository
from repositories.database import db_session
from repositories.passages import PassageRepository
from repositories.sessions import SessionRepository
from services.graph_service import build_all_scenes, chapter_meta, chapter_outline
from services.history_service import book_progress
from views.guards import current_user, login_required, trainer_required
from views.session_api import play_service, session_payload

pages_bp = Blueprint("pages", __name__)


def _repo() -> ChapterRepository:
    return current_app.extensions["eol_chapters"]


# Les intros de chapitre mêlent la mise en situation (pour le joueur) et les
# objectifs pédagogiques et ancrages curriculaires (pour l'enseignant·e).
# Le parcours joueur n'affiche que la première partie.
_TEACHER_MARKERS = ("Objectif pédagogique", "Ancrage M1", "Ancrage :")


def _split_intro(intro: str) -> tuple[str, str]:
    """Sépare la mise en situation du contenu destiné à l'enseignant·e."""
    text = (intro or "").strip()
    cut = len(text)
    for marker in _TEACHER_MARKERS:
        pos = text.find(marker)
        if pos != -1:
            cut = min(cut, pos)
    return text[:cut].strip(), text[cut:].strip()


def _duration_label(minutes: int) -> str:
    """Durée lisible, arrondie à 10 min au-delà d'une heure (« 2 h 30 »)."""
    if minutes < 60:
        return f"{minutes} min"
    hours, rest = divmod(round(minutes / 10) * 10, 60)
    return f"{hours} h {rest:02d}" if rest else f"{hours} h"


def _summary(book: dict) -> dict:
    chapters = _repo().load_chapters(book)
    outlines = [chapter_outline(ch) for ch in chapters]
    first = chapters[0] if chapters else None
    return {
        "book": book,
        "n_chapters": len(chapters),
        "n_scenes": sum(o["n_scenes"] for o in outlines),
        "duration": _duration_label(sum(o["minutes"] for o in outlines)),
        "first_chapter_id": first.Id if first else None,
    }


@pages_bp.route("/")
def landing():
    """Page de garde : carte par livre."""
    summaries = [_summary(b) for b in BOOKS]
    return render_template("landing.html.jinja", summaries=summaries)


@pages_bp.route("/books/<book_slug>/")
@trainer_required
def book_index(book_slug: str):
    """Index d'un livre : liste des chapitres."""
    try:
        book = get_book(book_slug)
    except ValueError:
        abort(404)
    chapters = _repo().load_chapters(book)
    return render_template(
        "book_index.html.jinja",
        book=book,
        chapters=chapters,
    )


@pages_bp.route("/play/<book_slug>/")
@login_required
def play_book(book_slug: str):
    """Sommaire joueur d'un livre : les chapitres, sans l'éditeur."""
    try:
        book = get_book(book_slug)
    except ValueError:
        abort(404)
    chapters = _repo().load_chapters(book)
    chapters_info = [
        {
            "id": ch.Id,
            "name": ch.Name,
            "intro": _split_intro(ch.Intro)[0],
            **chapter_outline(ch),
        }
        for ch in chapters
    ]
    user = current_user()
    sessions = SessionRepository(db_session()).list_for_user(user.id, book["slug"])
    current = next((s for s in reversed(sessions) if not s.is_completed), None)
    last_completed = next((s for s in reversed(sessions) if s.is_completed), None)
    progress = book_progress(chapters, PassageRepository(db_session()).list_for_user(user.id, book["slug"]))
    return render_template(
        "play_book.html.jinja",
        book=book,
        chapters=chapters_info,
        levels={c["id"]: c["level"] for c in progress["chapters"]},
        profile=progress["profile"],
        current=current,
        done=set(current.completed_chapters or []) if current else set(),
        last_completed=last_completed,
        next_number=(sessions[-1].number + 1) if sessions else 1,
    )


@pages_bp.route("/play/<book_slug>/restart", methods=["POST"])
@login_required
def play_restart(book_slug: str):
    """Abandonne la session en cours et repart de zéro (nouvelle session)."""
    try:
        get_book(book_slug)
    except ValueError:
        abort(404)
    play_service().restart(current_user(), book_slug)
    return redirect(url_for("pages.play_book", book_slug=book_slug))


@pages_bp.route("/play/<book_slug>/chapters/<int:chapter_id>")
@login_required
def play_chapter(book_slug: str, chapter_id: int):
    """Parcours joueur d'un chapitre : plein écran, sans graphe ni édition."""
    try:
        book = get_book(book_slug)
    except ValueError:
        abort(404)
    chapters = _repo().load_chapters(book)
    chapter = next((ch for ch in chapters if ch.Id == chapter_id), None)
    if chapter is None:
        abort(404)

    ids = [ch.Id for ch in chapters]
    pos = ids.index(chapter.Id)
    next_chapter_id = ids[pos + 1] if pos + 1 < len(ids) else None

    player_intro, teacher_intro = _split_intro(chapter.Intro)
    user = current_user()
    sessions = SessionRepository(db_session()).list_for_user(user.id, book["slug"])
    current = next((s for s in reversed(sessions) if not s.is_completed), None)
    return render_template(
        "play.html.jinja",
        session_info=session_payload(current) if current else None,
        outlook=play_service().outlook(user.id, book["slug"], chapter.Id),
        next_number=(sessions[-1].number + 1) if sessions else 1,
        chapter_count=len(chapters),
        book=book,
        chapter=chapter,
        player_intro=player_intro,
        teacher_intro=teacher_intro,
        scenes_data=build_all_scenes(chapter),
        chapter_meta=chapter_meta(chapter),
        next_chapter_id=next_chapter_id,
    )


@pages_bp.route("/books/<book_slug>/chapters/<int:chapter_id>")
@trainer_required
def chapter_page(book_slug: str, chapter_id: int):
    """Page d'un chapitre : éditeur + graphe + parcours."""
    try:
        book = get_book(book_slug)
    except ValueError:
        abort(404)
    chapters = _repo().load_chapters(book)
    chapter = next((ch for ch in chapters if ch.Id == chapter_id), None)
    if chapter is None:
        abort(404)

    chapter_links = [
        {"id": ch.Id, "name": ch.Name} for ch in chapters
    ]
    scenes_data = build_all_scenes(chapter)
    chapters_payload = {"Chapters": [chapter.to_dict()]}

    return render_template(
        "chapter.html.jinja",
        book=book,
        chapter=chapter,
        chapter_links=chapter_links,
        current_chapter_id=chapter.Id,
        scenes_data=scenes_data,
        chapters_payload=chapters_payload,
    )
