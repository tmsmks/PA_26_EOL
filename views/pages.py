"""Pages HTML — rendu dynamique via Jinja (pas de build statique)."""
from __future__ import annotations

from flask import Blueprint, abort, render_template

from books import BOOKS, get_book
from repositories.chapters import ChapterRepository
from services.graph_service import build_all_scenes

pages_bp = Blueprint("pages", __name__)
_repo = ChapterRepository()


def _summary(book: dict) -> dict:
    chapters = _repo.load_chapters(book)
    n_scenes = sum(len(ch.Scenes) for ch in chapters)
    n_interactions = sum(
        len(s.Interactions) for ch in chapters for s in ch.Scenes
    )
    first = chapters[0] if chapters else None
    return {
        "book": book,
        "n_chapters": len(chapters),
        "n_scenes": n_scenes,
        "n_interactions": n_interactions,
        "first_chapter_id": first.Id if first else None,
    }


@pages_bp.route("/")
def landing():
    """Page de garde : carte par livre."""
    summaries = [_summary(b) for b in BOOKS]
    return render_template("landing.html.jinja", summaries=summaries)


@pages_bp.route("/books/<book_slug>/")
def book_index(book_slug: str):
    """Index d'un livre : liste des chapitres."""
    try:
        book = get_book(book_slug)
    except ValueError:
        abort(404)
    chapters = _repo.load_chapters(book)
    return render_template(
        "book_index.html.jinja",
        book=book,
        chapters=chapters,
    )


@pages_bp.route("/books/<book_slug>/chapters/<int:chapter_id>")
def chapter_page(book_slug: str, chapter_id: int):
    """Page d'un chapitre : éditeur + graphe + parcours."""
    try:
        book = get_book(book_slug)
    except ValueError:
        abort(404)
    chapters = _repo.load_chapters(book)
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
