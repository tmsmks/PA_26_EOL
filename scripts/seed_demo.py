"""Jeu de démonstration : participants fictifs et sessions de MedStudents Y4.

Crée un compte formateur et six participants aux trajectoires contrastées
(progression, profil technique, excellence, régression, sessions en cours),
puis joue leurs sessions via l'API, exactement comme le navigateur : mêmes
règles que static/play/engine.js (conditions de scène, points d'entrée,
états narratifs), le serveur rejoue et note chaque scène. Les dates sont
ensuite étalées sur les dernières semaines.

    python -m scripts.seed_demo              # base configurée (DATABASE_URL, sinon instance/eol.db)
    python -m scripts.seed_demo --reset      # supprime puis recrée les comptes de démo
    python -m scripts.seed_demo --feedback   # génère aussi les feedbacks, dans l'ordre chronologique

Le mot de passe (aléatoire, commun à tous les comptes de démo) est écrit dans
instance/demo_credentials.txt. Par sécurité, le script refuse une base autre
que SQLite sans --allow-remote.
"""
from __future__ import annotations

import argparse
import os
import random
import secrets
import sys
from dataclasses import dataclass, field, replace
from datetime import timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app  # noqa: E402
from domain.soft_skills import SOFT_SKILLS  # noqa: E402
from repositories.orm import ROLE_TRAINER, BookSession, User, utcnow  # noqa: E402
from repositories.users import UserRepository  # noqa: E402
from services.auth_service import register  # noqa: E402
from services.graph_service import build_all_scenes, chapter_meta  # noqa: E402
from services.session_service import recount  # noqa: E402

BOOK = "medstudents_y4"
MAX_STEPS = 400


@dataclass
class Plan:
    """Comportement simulé d'un participant pendant une session."""

    skill: float  # probabilité de choisir la réponse la plus alignée avec ses préférences
    days: tuple[int, int | None]  # (début, fin) en jours avant aujourd'hui ; fin None = en cours
    weights: dict[str, float] = field(default_factory=dict)  # préférence par compétence (défaut 1)
    chapters: int | None = None  # nombre de chapitres joués (None = tout le livre)
    replays: int = 0  # scènes rejouées pour s'entraîner (non notées)


@dataclass
class Persona:
    username: str
    name: str
    plans: list[Plan]


PERSONAS = [
    # Progression nette : empathique d'emblée, apprend le cadre et le travail d'équipe.
    Persona("lea.martin", "Léa Martin", [
        Plan(0.35, (34, 31), {"Empathy": 1.6, "ProfessionalBoundaries": -0.6, "InterprofessionalCollaboration": -0.3}),
        Plan(0.60, (19, 17), {"Empathy": 1.3, "ProfessionalBoundaries": 0.4}, replays=3),
        Plan(0.85, (5, 3)),
    ]),
    # Profil technique : clair et cadré, en retrait sur l'émotion.
    Persona("hugo.bernard", "Hugo Bernard", [
        Plan(0.50, (28, 26), {"CommunicationClarity": 1.6, "ProfessionalBoundaries": 1.6, "Empathy": -0.4, "Compassion": -0.4}),
        Plan(0.60, (9, 8), {"CommunicationClarity": 1.4, "ProfessionalBoundaries": 1.4, "Empathy": 0.2, "Compassion": -0.2}),
    ]),
    # Excellence stable.
    Persona("sara.nguyen", "Sara Nguyen", [
        Plan(0.80, (25, 24)),
        Plan(0.92, (6, 5)),
    ]),
    # Régression : bonne première session, deuxième sous tension émotionnelle.
    Persona("yanis.robert", "Yanis Robert", [
        Plan(0.72, (30, 27)),
        Plan(0.40, (11, 10), {"EmotionalRegulation": -0.8, "Compassion": 0.5}),
    ]),
    # Une session terminée, la deuxième en cours (3 chapitres sur 6).
    Persona("ines.fontaine", "Inès Fontaine", [
        Plan(0.50, (21, 18), {"InterprofessionalCollaboration": -0.4}),
        Plan(0.65, (4, None), chapters=3),
    ]),
    # Première session en cours (2 chapitres sur 6).
    Persona("tom.muller", "Tom Müller", [
        Plan(0.45, (2, None), chapters=2),
    ]),
]

TRAINER = ("formateur.demo", "Formateur Démo")


# --- Moteur joueur (miroir de static/play/engine.js) ----------------------

def eval_condition(cond: dict, flags: set[str]) -> bool:
    if not cond:
        return True
    if not all(f in flags for f in cond.get("all", [])):
        return False
    anys = cond.get("any", [])
    if anys and not any(f in flags for f in anys):
        return False
    return not any(f in flags for f in cond.get("none", []))


def next_playable(scenes: list[dict], start: int, flags: set[str]) -> int:
    for i in range(start, len(scenes)):
        if eval_condition(scenes[i]["condition"], flags):
            return i
    return -1


def resolve_entry(scene: dict, flags: set[str]) -> str:
    for ep in scene["entry_points"]:
        if eval_condition(ep["condition"], flags):
            return ep["interaction_id"]
    return scene["default_entry"]


def weighted(response: dict, plan: Plan) -> float:
    return sum(plan.weights.get(k, 1.0) * (response.get(k) or 0) for k in SOFT_SKILLS)


def pick(entry: dict, visited: set[str], plan: Plan, rnd: random.Random) -> dict:
    responses = entry["responses"]
    fresh = [r for r in responses if r["next_id"] in ("-1", "") or r["next_id"] not in visited]
    pool = fresh or responses
    if rnd.random() < plan.skill:
        top = max(weighted(r, plan) for r in pool)
        pool = [r for r in pool if weighted(r, plan) == top]
    return rnd.choice(pool)


def play_scene(scene: dict, flags: set[str], plan: Plan, rnd: random.Random):
    by_id = scene["id_to_parcours"]
    current = by_id.get(resolve_entry(scene, flags)) or (scene["parcours"] or [None])[0]
    if current is None:
        return None
    entry_id = int(current["node_id"].split("_I")[-1])
    flags = set(flags)
    choices: list[int] = []
    visited: set[str] = set()
    while current and current["responses"]:
        if len(choices) >= MAX_STEPS:
            raise RuntimeError(f"Boucle dans la scène {scene['title']}")
        visited.add(current["node_id"].split("_I")[-1])
        r = pick(current, visited, plan, rnd)
        choices.append(r["idx"])
        flags -= set(r["clear_flags"])
        flags |= set(r["set_flags"])
        nid = r["next_id"]
        current = by_id.get(nid) if nid not in ("-1", "") else None
    return entry_id, choices, flags


# --- Simulation d'une session via l'API -----------------------------------

def post(client, url: str, body: dict | None = None) -> dict:
    r = client.post(url, json=body or {})
    if r.status_code != 200:
        raise RuntimeError(f"{url} → {r.status_code} {r.get_json()}")
    return r.get_json()


def play_session(client, book: list[tuple], plan: Plan, rnd: random.Random) -> tuple[int, int, int]:
    """Retourne (id de session, scènes notées, tentatives d'entraînement)."""
    sess = post(client, f"/api/play/{BOOK}/session")["session"]
    flags = set(sess["flags"])
    replays_left = plan.replays
    counted = practice = 0
    chapters = book if plan.chapters is None else book[: plan.chapters]
    for chapter, scenes, meta in chapters:
        owned = set(meta["owned_flags"])
        flags = {f for f in flags if f not in owned}
        start = meta["start_choice"]
        if start and start["options"] and not any(f in flags for f in start["unless_any"]):
            flags |= set(rnd.choice(start["options"])["flags"])

        idx = next_playable(scenes, 0, flags)
        while idx != -1:
            scene = scenes[idx]
            before = set(flags)
            run = play_scene(scene, before, plan, rnd)
            if run is not None:
                entry_id, choices, flags = run
                res = post(client, sess["urls"]["attempts"], {
                    "chapter_id": chapter.Id, "scene_id": scene["scene_id"],
                    "entry_id": entry_id, "choices": choices, "flags": sorted(flags),
                })
                counted += res["counted"]
                if replays_left and rnd.random() < 0.35:
                    # « Refaire ce scénario » : états restaurés, meilleure attention.
                    better = replace(plan, skill=min(1.0, plan.skill + 0.35))
                    entry_id, choices, flags = play_scene(scene, before, better, rnd)
                    res = post(client, sess["urls"]["attempts"], {
                        "chapter_id": chapter.Id, "scene_id": scene["scene_id"],
                        "entry_id": entry_id, "choices": choices, "flags": sorted(flags),
                    })
                    practice += not res["counted"]
                    replays_left -= 1
            idx = next_playable(scenes, idx + 1, flags)
        post(client, sess["urls"]["complete"], {"chapter_id": chapter.Id, "flags": sorted(flags)})
    return sess["id"], counted, practice


def backdate(db, session_id: int, plan: Plan, rnd: random.Random) -> None:
    """Étale les dates : la session commence et se termine il y a quelques jours."""
    bs = db.get(BookSession, session_id)
    now = utcnow()
    start_days, end_days = plan.days
    start = now - timedelta(days=start_days, hours=rnd.randint(1, 8))
    end = now - timedelta(days=end_days, hours=rnd.randint(1, 8)) if end_days is not None else now - timedelta(hours=rnd.randint(1, 20))
    bs.started_at = start
    bs.updated_at = end
    if bs.is_completed:
        bs.completed_at = end
    for i, a in enumerate(bs.attempts):
        a.created_at = start + (end - start) * (i + 1) / (len(bs.attempts) + 1)
    # Passages : du premier au dernier de leurs scénarios.
    for p in bs.passages:
        times = [a.created_at for a in p.attempts] or [start]
        p.started_at = min(times) - timedelta(minutes=2)
        if p.completed_at is not None:
            p.completed_at = max(times) + timedelta(minutes=1)
    db.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--reset", action="store_true", help="supprime les comptes de démo avant de les recréer")
    parser.add_argument("--feedback", action="store_true", help="génère les feedbacks (backend configuré)")
    parser.add_argument("--allow-remote", action="store_true", help="autorise une base non SQLite")
    parser.add_argument("--seed", type=int, default=2026, help="graine aléatoire (parties reproductibles)")
    args = parser.parse_args()

    app = create_app({"CSRF_ENABLED": False})
    database = app.extensions["eol_db"]
    if not database.url.startswith("sqlite") and not args.allow_remote:
        sys.exit("Base non SQLite : relancez avec --allow-remote si c'est bien voulu.")

    usernames = [TRAINER[0]] + [p.username for p in PERSONAS]
    db = database.sessionmaker()
    users = UserRepository(db)
    existing = [u for u in (users.get_by_username(n) for n in usernames) if u is not None]
    if existing and not args.reset:
        sys.exit("Comptes de démo déjà présents : relancez avec --reset pour les recréer.")
    for u in existing:
        db.delete(u)
    db.commit()

    password = secrets.token_urlsafe(9)
    register(users, TRAINER[0], password, TRAINER[1], role=ROLE_TRAINER)
    for p in PERSONAS:
        register(users, p.username, password, p.name)

    repo = app.extensions["eol_chapters"]
    book = [(ch, build_all_scenes(ch), chapter_meta(ch)) for ch in repo.load_chapters(BOOK)]
    rnd = random.Random(args.seed)
    created: list[int] = []

    for persona in PERSONAS:
        client = app.test_client()
        r = client.post("/login", data={"username": persona.username, "password": password})
        if r.status_code != 302:
            sys.exit(f"Connexion impossible pour {persona.username}")
        for plan in persona.plans:
            sid, counted, practice = play_session(client, book, plan, rnd)
            backdate(db, sid, plan, rnd)
            created.append(sid)
            bs = db.get(BookSession, sid)
            db.refresh(bs)
            state = (
                f"bilan {bs.results['global']:.0f}/100" if bs.is_completed
                else f"en cours, {len(bs.completed_chapters)}/{len(book)} chapitres"
            )
            extra = f", {practice} tentative(s) d'entraînement" if practice else ""
            print(f"  {persona.name:15s} session {bs.number} : {counted} scènes notées{extra} — {state}")

        # Création du compte et dernière connexion cohérentes avec les dates ;
        # la règle d'espacement des passages notés est réappliquée sur les dates finales.
        user = users.get_by_username(persona.username)
        recount([p for s in user.sessions for p in s.passages], app.config["PASSAGE_SPACING_DAYS"])
        first = min(s.started_at for s in user.sessions)
        user.created_at = first - timedelta(days=1)
        user.last_login_at = max(s.updated_at for s in user.sessions)
        db.commit()

        if args.feedback:
            for s in sorted(user.sessions, key=lambda s: s.number):
                if s.is_completed:
                    fb = post(client, f"/api/sessions/{s.id}/feedback")["feedback"]
                    print(f"    feedback session {s.number} : {fb['source']}")

    creds = os.path.join(app.instance_path, "demo_credentials.txt")
    with open(creds, "w", encoding="utf-8") as f:
        f.write("Comptes de démonstration (scripts/seed_demo.py) — mot de passe commun :\n")
        f.write(f"  {password}\n\n")
        f.write(f"  {TRAINER[0]:16s} formateur·rice\n")
        for p in PERSONAS:
            f.write(f"  {p.username:16s} participant·e ({p.name})\n")
    os.chmod(creds, 0o600)
    print(f"\n{len(PERSONAS)} participants, {len(created)} sessions. Identifiants : {creds}")


if __name__ == "__main__":
    main()
