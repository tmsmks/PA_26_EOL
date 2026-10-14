"""Pages de suivi : historique participant, bilan de session, espace formateur."""
from __future__ import annotations

import io
from typing import Any

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
from domain.models import Chapter
from domain.soft_skills import SOFT_SKILL_LABELS, SOFT_SKILLS
from exporters.tables import to_csv_zip, to_json, to_xlsx
from repositories.database import db_session
from repositories.orm import BookSession, User
from repositories.passages import PassageRepository
from repositories.sessions import SessionRepository
from repositories.users import UserRepository
from services.auth_service import AuthError, hash_password, validate_password
from services.export_service import build_export, participant_code
from services.history_service import book_progress, cohorts_for, completed_with_results, user_history
from services.scoring_service import group_change
from views.scoring_context import book_thresholds, thresholds_for
from services.scoring_service import MIN_SKILL_EVIDENCE
from views.guards import current_user, login_required, trainer_required
from views.session_api import play_service

account_bp = Blueprint("account", __name__)


def _book_chapters(slugs: set[str]) -> dict[str, list[Chapter]]:
    """Chapitres des livres joués (les autres ne sont pas chargés)."""
    repo = current_app.extensions["eol_chapters"]
    chapters = {}
    for slug in slugs:
        try:
            chapters[slug] = repo.load_chapters(slug)
        except (OSError, ValueError):  # livre retiré ou renommé depuis
            chapters[slug] = []
    return chapters


def _history_page(user: User, trainer_view: bool):
    sessions = SessionRepository(db_session()).list_for_user(user.id)
    passages = PassageRepository(db_session()).list_for_user(user.id)
    chapters = _book_chapters({s.book_slug for s in sessions})
    cohorts = cohorts_for(PassageRepository(db_session()).list_all(), chapters)
    blocks = user_history(sessions, passages, chapters, cohorts, thresholds_for(chapters))
    return render_template(
        "account_history.html.jinja",
        subject=user,
        trainer_view=trainer_view,
        blocks=blocks,
        skills=SOFT_SKILLS,
        labels=SOFT_SKILL_LABELS,
        min_evidence=MIN_SKILL_EVIDENCE,
        spacing_days=current_app.config["PASSAGE_SPACING_DAYS"],
        charts=[
            {
                "slug": b["book"]["slug"],
                "profile": b["progress"]["profile"],
                "chapters": [
                    {"id": c["id"], "name": c["name"], "points": c["level"]["points"]}
                    for c in b["progress"]["chapters"]
                    if c["level"] and c["level"]["n_passages"] > 1
                ],
            }
            for b in blocks
        ],
    )


@account_bp.route("/me")
@login_required
def my_history():
    return _history_page(current_user(), trainer_view=False)


def _report_data(bs: BookSession) -> dict[str, Any]:
    repo = SessionRepository(db_session())
    history = [
        s for s in completed_with_results(repo.list_for_user(bs.user_id, bs.book_slug))
        if s.number <= bs.number
    ]
    previous = next((s for s in reversed(history) if s.number < bs.number), None)
    if bs.is_completed and bs.results:
        results = bs.results
    else:
        # Session en cours : résultats provisoires, sans feedback.
        results = play_service().compute_results(bs)
    repo = PassageRepository(db_session())
    book_chapters = _book_chapters({bs.book_slug})[bs.book_slug]
    progress = book_progress(
        book_chapters,
        repo.list_for_user(bs.user_id, bs.book_slug),
        cohorts_for(repo.list_all(book_slug=bs.book_slug), [bs.book_slug])[bs.book_slug],
        thresholds=book_thresholds(bs.book_slug, book_chapters),
    )
    user = current_user()
    feedback = bs.feedback
    return {
        "session": {
            "id": bs.id,
            "number": bs.number,
            "status": bs.status,
            "book_slug": bs.book_slug,
        },
        "results": results,
        "previous": {
            "number": previous.number,
            "scores": previous.results.get("scores"),
            "global": previous.results.get("global"),
        } if previous else None,
        "book": progress["profile"],
        "points": [{"number": s.number, "global": s.results.get("global")} for s in history],
        "feedback": feedback,
        "feedbackUrl": url_for("session_api.session_feedback", session_id=bs.id),
        "canRegenerate": bool(user.is_trainer or (feedback and feedback.get("source") != "ai")),
        "playBookUrl": url_for("pages.play_book", book_slug=bs.book_slug),
        "skills": list(SOFT_SKILLS),
        "labels": SOFT_SKILL_LABELS,
    }


@account_bp.route("/sessions/<int:session_id>")
@login_required
def session_report(session_id: int):
    bs = SessionRepository(db_session()).get(session_id)
    user = current_user()
    if bs is None:
        abort(404)
    if bs.user_id != user.id and not user.is_trainer:
        abort(403)
    try:
        book = get_book(bs.book_slug)
    except ValueError:
        abort(404)
    data = _report_data(bs)
    return render_template(
        "session_report.html.jinja",
        book=book,
        bs=bs,
        owner=bs.user,
        is_own=bs.user_id == user.id,
        results=data["results"],
        report=data,
    )


# --- Espace formateur -------------------------------------------------------

@account_bp.route("/trainer/")
@trainer_required
def trainer_dashboard():
    users = UserRepository(db_session()).list_all()
    by_user: dict[int, list[BookSession]] = {}
    for s in SessionRepository(db_session()).list_all():
        by_user.setdefault(s.user_id, []).append(s)
    passages_by_user: dict[int, list] = {}
    all_passages = PassageRepository(db_session()).list_all()
    for p in all_passages:
        passages_by_user.setdefault(p.user_id, []).append(p)
    chapters = _book_chapters({b["slug"] for b in BOOKS})
    cohorts = cohorts_for(all_passages, chapters)
    thresholds = thresholds_for(chapters)
    titles = {b["slug"]: b["title"] for b in BOOKS}

    # Livre détaillé chapitre par chapitre : celui demandé, sinon le premier joué.
    played = [b["slug"] for b in BOOKS if any(p.book_slug == b["slug"] for ps in passages_by_user.values() for p in ps)]
    detail_slug = request.args.get("book") or (played[0] if played else BOOKS[0]["slug"])
    try:
        detail_book = get_book(detail_slug)
    except ValueError:
        abort(404)

    rows = []
    # À débriefer (erreurs critiques non résolues) et passages trop rapides :
    # le débriefing humain est ce qui rend les patients virtuels efficaces.
    debriefs: list[dict] = []
    fast: list[dict] = []
    for u in users:
        sessions = by_user.get(u.id, [])
        passages = passages_by_user.get(u.id, [])
        progress = {
            b["slug"]: book_progress(
                chapters[b["slug"]], [p for p in passages if p.book_slug == b["slug"]], cohorts.get(b["slug"]),
                thresholds=thresholds.get(b["slug"]),
            )
            for b in BOOKS
        }
        for slug, pr in progress.items():
            for c in pr["chapters"]:
                if c["critical"]:
                    debriefs.append({
                        "user": u, "book": titles[slug], "chapter": f"{c['id']}. {c['name']}",
                        "answers": c["critical"], "at": c["level"]["last_at"],
                    })
        for p in passages:
            timing = (p.results or {}).get("timing") or {}
            if timing.get("too_fast"):
                fast.append({
                    "user": u, "book": titles.get(p.book_slug, p.book_slug), "chapter_id": p.chapter_id,
                    "at": p.completed_at, "n_fast": timing.get("n_fast"), "n_timed": timing.get("n_timed"),
                })
        activity = max(
            [s.updated_at for s in sessions] + [p.completed_at for p in passages if p.completed_at],
            default=u.last_login_at,
        )
        rows.append({
            "user": u,
            "n_completed": sum(1 for s in sessions if s.is_completed),
            "n_in_progress": sum(1 for s in sessions if not s.is_completed),
            "n_passages": sum(1 for p in passages if p.is_completed and p.counted),
            "last_activity": activity,
            "profiles": {slug: pr["profile"] for slug, pr in progress.items()},
            "detail": progress[detail_book["slug"]]["chapters"],
        })
    # Progrès du groupe, chapitre par chapitre : 1ᵉʳ et dernier passage compté.
    group = []
    for ch in chapters[detail_book["slug"]]:
        pairs = [
            (c["level"]["first"], c["level"]["last"])
            for r in rows
            for c in r["detail"]
            if c["id"] == ch.Id and c["level"] and c["level"]["n_passages"] >= 2
        ]
        group.append({"id": ch.Id, "name": ch.Name, "change": group_change(pairs)})
    return render_template(
        "trainer_dashboard.html.jinja",
        rows=rows,
        group=group,
        debriefs=debriefs,
        fast=sorted(fast, key=lambda f: f["at"] or 0, reverse=True)[:20],
        books=BOOKS,
        detail_book=detail_book,
        detail_chapters=chapters[detail_book["slug"]],
    )


def _participant(user_id: int) -> User:
    user = UserRepository(db_session()).get(user_id)
    if user is None:
        abort(404)
    return user


@account_bp.route("/trainer/participants/<int:user_id>")
@trainer_required
def trainer_participant(user_id: int):
    return _history_page(_participant(user_id), trainer_view=True)


@account_bp.route("/trainer/participants/<int:user_id>/password", methods=["POST"])
@trainer_required
def trainer_reset_password(user_id: int):
    """Mot de passe temporaire défini par le/la formateur·rice (pas d'e-mail)."""
    user = _participant(user_id)
    password = request.form.get("password", "")
    try:
        validate_password(password)
    except AuthError as e:
        flash(str(e), "error")
    else:
        UserRepository(db_session()).set_password(user, hash_password(password))
        flash(f"Nouveau mot de passe enregistré pour {user.display_name}.", "ok")
    return redirect(url_for("account.trainer_participant", user_id=user.id))


# --- Export des données brutes ----------------------------------------------

EXPORT_FORMATS = {
    "xlsx": (to_xlsx, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "xlsx"),
    "csv": (to_csv_zip, "application/zip", "zip"),
    "json": (to_json, "application/json", "json"),
}


@account_bp.route("/trainer/export")
@trainer_required
def trainer_export():
    """Données de jeu brutes (Excel, CSV ou JSON), par livre et par participant."""
    fmt = request.args.get("format", "xlsx")
    if fmt not in EXPORT_FORMATS:
        abort(400)
    book_slug = request.args.get("book") or None
    if book_slug is not None:
        try:
            get_book(book_slug)
        except ValueError:
            abort(404)
    participant = None
    if request.args.get("user"):
        user_id = request.args.get("user", type=int)
        if user_id is None:
            abort(400)
        participant = _participant(user_id)
    pseudonymize = request.args.get("pseudo") == "1"

    users = [participant] if participant else UserRepository(db_session()).list_all()
    user_id = participant.id if participant else None
    sessions = SessionRepository(db_session()).list_for_export(user_id=user_id, book_slug=book_slug)
    export_chapters = _book_chapters({s.book_slug for s in sessions})
    tables, meta = build_export(
        users,
        sessions,
        PassageRepository(db_session()).list_all(user_id=user_id, book_slug=book_slug),
        export_chapters,
        thresholds=thresholds_for(export_chapters),
        book_slug=book_slug,
        participant=participant,
        pseudonymize=pseudonymize,
        spacing_days=current_app.config["PASSAGE_SPACING_DAYS"],
    )

    write, mimetype, ext = EXPORT_FORMATS[fmt]
    parts = ["eol_donnees", book_slug or "tous_livres"]
    if participant:
        parts.append(participant_code(participant, pseudonymize))
    if pseudonymize:
        parts.append("pseudo")
    parts.append(meta["exporte_le"].strftime("%Y-%m-%d"))
    response = send_file(
        io.BytesIO(write(tables, meta)),
        mimetype=mimetype,
        as_attachment=True,
        download_name="_".join(parts) + "." + ext,
    )
    response.headers["Cache-Control"] = "no-store"  # données personnelles
    return response
