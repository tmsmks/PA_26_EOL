"""Espace formateur : validation de la clé de cotation par un panel d'experts."""
from __future__ import annotations

import io

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)

from books import BOOKS, get_book
from domain.expert_rubric import RUBRIC, RUBRIC_STATUS
from domain.soft_skills import SOFT_SKILL_LABELS, SOFT_SKILLS
from exporters.expert_key import grid_workbook, synthesis_meta, synthesis_tables
from exporters.tables import to_xlsx
from repositories.database import db_session
from repositories.expert_ratings import ExpertRatingRepository
from services.expert_key_service import analyse, key_items, parse_grid
from views.guards import trainer_required

expert_key_bp = Blueprint("expert_key", __name__, url_prefix="/trainer/cle")

XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
SAMPLES = (0, 10, 15, 20)
MAX_UPLOAD_FILES = 30


def _book(slug: str) -> dict:
    try:
        return get_book(slug)
    except ValueError:
        abort(404)


def _chapters(book: dict):
    try:
        return current_app.extensions["eol_chapters"].load_chapters(book)
    except (OSError, ValueError):
        abort(404)


def _rating_dicts(ratings) -> list[dict]:
    return [
        {
            "ref": r.ref,
            "expert": r.expert,
            "scores": r.scores,
            "critical": r.critical,
            "rationale": r.rationale,
            "comment": r.comment,
        }
        for r in ratings
    ]


def _int_arg(name: str, default: int, allowed: tuple[int, ...] | None = None) -> int:
    value = request.args.get(name, type=int)
    if value is None:
        return default
    if allowed is not None and value not in allowed:
        abort(400)
    return value


@expert_key_bp.route("/")
@trainer_required
def index():
    book = _book(request.args.get("book") or BOOKS[0]["slug"])
    chapters = _chapters(book)
    items = key_items(chapters)
    repo = ExpertRatingRepository(db_session())
    summary = repo.summary(book["slug"])
    rounds = sorted({s["round"] for s in summary})
    round_ = _int_arg("round", rounds[-1] if rounds else 1)
    result = analyse(items, _rating_dicts(repo.for_book(book["slug"], round_))) if rounds else None
    return render_template(
        "expert_key.html.jinja",
        books=BOOKS,
        book=book,
        chapters=[
            {
                "id": ch.Id,
                "name": ch.Name,
                "n_items": sum(1 for it in items if it.chapter_id == ch.Id),
                "n_points": len({(it.scene_id, it.interaction_id) for it in items if it.chapter_id == ch.Id}),
            }
            for ch in chapters
        ],
        n_items=len(items),
        samples=SAMPLES,
        summary=summary,
        rounds=rounds,
        round=round_,
        result=result,
        rubric=RUBRIC,
        rubric_status=RUBRIC_STATUS,
        skills=SOFT_SKILLS,
        labels=SOFT_SKILL_LABELS,
    )


@expert_key_bp.route("/<book_slug>/grille")
@trainer_required
def grid(book_slug: str):
    """Grille Excel à envoyer aux experts (sans les points de l'auteur)."""
    book = _book(book_slug)
    chapters = _chapters(book)
    chapter = request.args.get("chapter", type=int)
    if chapter is not None and chapter not in {ch.Id for ch in chapters}:
        abort(404)
    sample = _int_arg("sample", 0, SAMPLES)
    round_ = _int_arg("round", 1, (1, 2, 3))
    items = key_items(chapters, [chapter] if chapter else None, sample or None)
    scope = (f"Chapitre {chapter}" if chapter else "Tous les chapitres") + (
        f" · échantillon de {sample} points de choix par chapitre" if sample else ""
    )
    name = f"grille_experts_{book['slug']}_{'ch' + str(chapter) if chapter else 'tout'}"
    name += f"_ech{sample}" if sample else ""
    response = send_file(
        io.BytesIO(grid_workbook(book["title"], items, round_, scope)),
        mimetype=XLSX,
        as_attachment=True,
        download_name=f"{name}_tour{round_}.xlsx",
    )
    response.headers["Cache-Control"] = "no-store"
    return response


@expert_key_bp.route("/<book_slug>/import", methods=["POST"])
@trainer_required
def upload(book_slug: str):
    """Importe une ou plusieurs grilles remplies (réimporter remplace les cotes de l'expert)."""
    book = _book(book_slug)
    known = {it.ref for it in key_items(_chapters(book))}
    files = [f for f in request.files.getlist("grids") if f and f.filename][:MAX_UPLOAD_FILES]
    if not files:
        flash("Choisissez au moins une grille remplie (.xlsx).", "error")
    repo = ExpertRatingRepository(db_session())
    for f in files:
        parsed = parse_grid(f.read(), f.filename, known)
        for err in parsed.errors[:5]:
            flash(err, "error")
        if len(parsed.errors) > 5:
            flash(f"{f.filename} : {len(parsed.errors) - 5} autre(s) erreur(s).", "error")
        if parsed.errors or not parsed.expert:
            flash(f"{f.filename} : grille non importée, corrigez-la puis réimportez-la.", "error")
            continue
        n = repo.replace(book["slug"], parsed.expert, parsed.round, parsed.ratings)
        note = f" ({parsed.unknown_refs} ligne(s) d'une autre version du livre ignorée(s))" if parsed.unknown_refs else ""
        flash(f"{parsed.expert}, tour {parsed.round} : {n} réponse(s) cotée(s) importée(s){note}.", "ok")
    return redirect(url_for("expert_key.index", book=book["slug"]))


@expert_key_bp.route("/<book_slug>/supprimer", methods=["POST"])
@trainer_required
def remove(book_slug: str):
    book = _book(book_slug)
    expert = request.form.get("expert", "")
    round_ = request.form.get("round", type=int)
    if not expert or round_ is None:
        abort(400)
    ExpertRatingRepository(db_session()).delete(book["slug"], expert, round_)
    flash(f"Cotes de {expert} (tour {round_}) supprimées.", "ok")
    return redirect(url_for("expert_key.index", book=book["slug"]))


@expert_key_bp.route("/<book_slug>/synthese")
@trainer_required
def synthesis(book_slug: str):
    """Synthèse Excel d'un tour : accord par compétence, réponses à revoir."""
    book = _book(book_slug)
    round_ = _int_arg("round", 1)
    items = key_items(_chapters(book))
    result = analyse(items, _rating_dicts(ExpertRatingRepository(db_session()).for_book(book["slug"], round_)))
    if not result["n_rated"]:
        abort(404)
    data = to_xlsx(synthesis_tables(result, round_), synthesis_meta(book["title"], result, round_))
    response = send_file(
        io.BytesIO(data),
        mimetype=XLSX,
        as_attachment=True,
        download_name=f"synthese_experts_{book['slug']}_tour{round_}.xlsx",
    )
    response.headers["Cache-Control"] = "no-store"
    return response
