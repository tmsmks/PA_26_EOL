"""Prompt du feedback général de fin de livre.

Aucune donnée personnelle n'est envoyée au LLM (ni nom, ni identifiant) :
seulement les scores, les chapitres et les extraits de scénario joués.
"""
from __future__ import annotations

from typing import Any, Mapping

from domain.soft_skills import SOFT_SKILL_LABELS, SOFT_SKILLS
from services.scoring_service import quoted

MAX_PREVIOUS = 3
# Réponses critiques transmises au LLM, au plus (les premières jouées).
MAX_CRITICAL = 8

SYSTEM_MESSAGE = (
    "Tu es formateur·rice en communication clinique et en soins palliatifs. "
    "Tu rédiges le feedback de fin de parcours d'un·e participant·e à un serious "
    "game de formation en santé : il/elle a joué un livre entier (plusieurs "
    "chapitres de dialogues avec patient·e·s, proches et collègues).\n\n"
    "Le jeu évalue 7 compétences, notées sur 100 : 0 = pire parcours possible, "
    "100 = meilleur parcours possible pour cette compétence dans les scènes jouées. "
    "Codes : " + ", ".join(f"{k} ({SOFT_SKILL_LABELS[k]})" for k in SOFT_SKILLS) + ".\n\n"
    "Règles :\n"
    "- Vouvoie le/la participant·e. Ton bienveillant, direct et concret, sans flatterie.\n"
    "- N'invente AUCUN chiffre : ne cite que les scores fournis, arrondis à l'entier.\n"
    "- Appuie tes remarques sur les moments clés fournis (choix effectué vs réponse "
    "plus ajustée) : évoque brièvement la situation, sans recopier de longs passages, "
    "et appuie-toi sur la justification de la clé quand elle est fournie.\n"
    "- Si des RÉPONSES CRITIQUES sont fournies, nomme-les clairement et explique pourquoi, "
    "sans dramatiser ni juger la personne.\n"
    "- Points forts / points faibles : utilise les codes exacts, en priorité ceux "
    "des listes FORCES et FAIBLESSES.\n"
    "- Chapitres à retravailler : choisis uniquement parmi les chapitres fournis (id "
    "exact), en priorité les CHAPITRES SUGGÉRÉS, et explique le lien avec les faiblesses.\n"
    "- Si des SESSIONS PRÉCÉDENTES sont fournies : compare explicitement (écarts "
    "fournis), dis si les conseils donnés la dernière fois ont porté leurs fruits, "
    "et rebondis dessus pour la suite. Sinon, \"progression\" vaut null.\n\n"
    "Réponds STRICTEMENT en JSON :\n"
    "{\n"
    '  "summary": "3 à 5 phrases de synthèse",\n'
    '  "strengths": [{"skill": "<code>", "text": "1 à 2 phrases"}],   // 2 à 3\n'
    '  "weaknesses": [{"skill": "<code>", "text": "1 à 2 phrases"}],  // 2 à 3\n'
    '  "improvements": ["conseil actionnable commençant par un verbe"], // 3 à 4\n'
    '  "chapters_to_rework": [{"chapter_id": <int>, "reason": "1 phrase"}], // 1 à 2\n'
    '  "progression": "3 à 4 phrases" | null\n'
    "}"
)


def _fmt(value: float | None) -> str:
    return "n/a" if value is None else str(round(value))


def _scores_line(scores: Mapping[str, float | None]) -> str:
    return " ; ".join(f"{k} {_fmt(scores.get(k))}" for k in SOFT_SKILLS)


def _why(part: Mapping[str, Any]) -> str:
    return f" [justification de la clé : {part['rationale']}]" if part.get("rationale") else ""


def _moment_line(m: Mapping[str, Any]) -> str:
    who = m.get("actor") or "Narration"
    return (
        f"- [Ch. {m['chapter_id']} · « {m.get('scene_title', '')} »] {who} : {quoted(m['prompt'])} "
        f"→ choix : {quoted(m['choice']['text'])} (total {m['choice']['total']:+d}){_why(m['choice'])}"
        + (
            f" ; réponse plus ajustée : {quoted(m['best']['text'])} (total {m['best']['total']:+d})"
            f"{_why(m['best'])}"
            if m.get("gap", 0) > 0
            else ""
        )
    )


def format_user_message(
    book: Mapping[str, Any],
    number: int,
    results: Mapping[str, Any],
    previous: list[Mapping[str, Any]],
    weighted: Mapping[str, Any] | None,
) -> str:
    """`previous` : sessions terminées antérieures, la plus récente d'abord."""
    scores = results.get("scores") or {}
    lines = [
        f"LIVRE : {book.get('title')} — public : {book.get('audience')}",
        f"SESSION : n° {number}"
        + (" (première session)" if not previous else f" ({len(previous)} session(s) précédente(s) fournie(s))"),
        f"NOTE GLOBALE DE LA SESSION : {_fmt(results.get('global'))}/100",
        "",
        "SCORES PAR COMPÉTENCE :",
        *[f"- {k} — {SOFT_SKILL_LABELS[k]} : {_fmt(scores.get(k))}" for k in SOFT_SKILLS],
        "",
        f"FORCES : {', '.join(results.get('strengths') or []) or 'aucune'}",
        f"FAIBLESSES : {', '.join(results.get('weaknesses') or []) or 'aucune'}",
        "",
        "SCORES PAR CHAPITRE :",
    ]
    for ch in results.get("chapters") or []:
        lines.append(
            f"- Chapitre {ch['id']} « {ch['name']} » : global {_fmt(ch.get('global'))} "
            f"({_scores_line(ch.get('scores') or {})})"
        )
    lines += [
        "",
        "CHAPITRES SUGGÉRÉS À RETRAVAILLER : "
        + (", ".join(str(c) for c in results.get("chapters_to_rework") or []) or "aucun"),
    ]

    if results.get("critical"):
        lines += ["", "RÉPONSES CRITIQUES CHOISIES :", *map(_moment_line, results["critical"][:MAX_CRITICAL])]
    moments = results.get("moments") or {}
    if moments.get("missed"):
        lines += ["", "MOMENTS CLÉS — OCCASIONS MANQUÉES :", *map(_moment_line, moments["missed"])]
    if moments.get("good"):
        lines += ["", "MOMENTS CLÉS — RÉUSSITES :", *map(_moment_line, moments["good"])]

    if previous:
        lines += ["", "SESSIONS PRÉCÉDENTES (la plus récente d'abord) :"]
        for p in previous[:MAX_PREVIOUS]:
            res = p.get("results") or {}
            fb = p.get("feedback") or {}
            lines.append(
                f"- Session {p['number']} (terminée le {p.get('completed_on', '?')}) : "
                f"note {_fmt(res.get('global'))}/100 ; {_scores_line(res.get('scores') or {})}"
            )
            weak = [w.get("skill") for w in fb.get("weaknesses") or [] if isinstance(w, dict)]
            if weak:
                lines.append(f"  faiblesses relevées alors : {', '.join(weak)}")
            if fb.get("improvements"):
                lines.append(f"  conseils donnés alors : {' | '.join(fb['improvements'][:4])}")
            rework = [str(c.get("chapter_id")) for c in fb.get("chapters_to_rework") or [] if isinstance(c, dict)]
            if rework:
                lines.append(f"  chapitres à retravailler alors : {', '.join(rework)}")
        last = (previous[0].get("results") or {}).get("scores") or {}
        deltas = [
            f"{k} {scores[k] - last[k]:+.0f}"
            for k in SOFT_SKILLS
            if scores.get(k) is not None and last.get(k) is not None
        ]
        lines += ["", "ÉCARTS PAR RAPPORT À LA SESSION PRÉCÉDENTE : " + " ; ".join(deltas)]
        if weighted:
            lines.append(
                f"NOTE PONDÉRÉE ({weighted['n_sessions']} sessions, la plus récente pèse le plus) : "
                f"{_fmt(weighted.get('global'))}/100"
            )
    return "\n".join(lines)
