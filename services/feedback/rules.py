"""Feedback de repli, sans IA : toujours disponible et factuel.

Sert quand le backend LLM est absent ou en erreur, et complète les champs
qu'une réponse IA aurait laissés vides ou invalides.
"""
from __future__ import annotations

from typing import Any, Mapping

from domain.soft_skills import SOFT_SKILL_LABELS
from services.scoring_service import score_deltas

SKILL_TIPS: dict[str, str] = {
    "RespectAndDignity": (
        "Demandez l'accord de la personne avant d'agir et laissez-lui la décision "
        "sur ce qui la concerne, y compris quand la famille pousse dans un autre sens."
    ),
    "Empathy": (
        "Reformulez l'émotion entendue (« Vous semblez inquiet… ») avant d'apporter "
        "une information ou une solution."
    ),
    "Compassion": (
        "Restez présent·e dans les silences et proposez une aide concrète plutôt "
        "que de rassurer trop vite."
    ),
    "EmotionalRegulation": (
        "Quand la tension monte, marquez un temps d'arrêt et différez la réponse "
        "plutôt que de réagir à chaud ; parlez-en ensuite en débriefing."
    ),
    "CommunicationClarity": (
        "Utilisez des mots simples, vérifiez la compréhension (« Qu'avez-vous "
        "retenu ? ») et annoncez clairement les prochaines étapes."
    ),
    "ProfessionalBoundaries": (
        "Restez dans votre rôle : ne promettez pas ce qui ne dépend pas de vous et "
        "orientez vers la bonne personne."
    ),
    "InterprofessionalCollaboration": (
        "Transmettez les informations clés à l'équipe de façon structurée (SBAR) et "
        "sollicitez l'avis des autres professionnel·le·s."
    ),
}


def _fmt(value: float | None) -> str:
    return "—" if value is None else str(round(value))


def _label(skill: str) -> str:
    return SOFT_SKILL_LABELS.get(skill, skill)


def _join(labels: list[str]) -> str:
    if len(labels) <= 1:
        return "".join(labels)
    return ", ".join(labels[:-1]) + " et " + labels[-1]


def progression_text(
    results: Mapping[str, Any], previous: Mapping[str, Any] | None
) -> str | None:
    """Comparaison factuelle avec la session précédente."""
    if not previous:
        return None
    prev_results = previous.get("results") or {}
    g, pg = results.get("global"), prev_results.get("global")
    parts: list[str] = []
    if g is not None and pg is not None:
        diff = round(g - pg)
        sign = "+" if diff > 0 else ""
        parts.append(
            f"Par rapport à votre session {previous.get('number')} ({_fmt(pg)}/100), "
            f"votre note passe à {_fmt(g)}/100 ({sign}{diff} points)."
        )
    deltas = {
        k: v
        for k, v in score_deltas(results.get("scores") or {}, prev_results.get("scores") or {}).items()
        if v is not None
    }
    if deltas:
        best = max(deltas, key=lambda k: deltas[k])
        worst = min(deltas, key=lambda k: deltas[k])
        if deltas[best] >= 3:
            parts.append(f"Plus forte progression : {_label(best)} (+{round(deltas[best])}).")
        if deltas[worst] <= -3:
            parts.append(f"Recul le plus net : {_label(worst)} ({round(deltas[worst])}).")
    prev_weak = (previous.get("feedback") or {}).get("weaknesses") or []
    followed = [
        _label(w["skill"])
        for w in prev_weak
        if isinstance(w, dict) and (deltas.get(w.get("skill")) or 0) >= 3
    ]
    if followed:
        parts.append(f"Les axes travaillés depuis la dernière fois portent leurs fruits : {_join(followed)}.")
    return " ".join(parts) or None


def rules_feedback(
    book_title: str,
    number: int,
    results: Mapping[str, Any],
    previous: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    scores = results.get("scores") or {}
    chapters = {c["id"]: c for c in results.get("chapters") or []}
    strengths = results.get("strengths") or []
    weaknesses = results.get("weaknesses") or []

    summary = (
        f"Session {number} de « {book_title} » terminée avec une note globale de "
        f"{_fmt(results.get('global'))}/100."
    )
    if strengths:
        summary += f" Vos points d'appui : {_join([_label(k) for k in strengths])}."
    if weaknesses:
        summary += f" À travailler en priorité : {_join([_label(k) for k in weaknesses])}."

    rework = []
    for cid in results.get("chapters_to_rework") or []:
        ch = chapters.get(cid)
        if not ch:
            continue
        focus = [k for k in weaknesses if ch["scores"].get(k) is not None][:2]
        detail = ", ".join(f"{_label(k)} {_fmt(ch['scores'][k])}/100" for k in focus)
        rework.append({
            "chapter_id": cid,
            "reason": f"Chapitre le plus en retrait sur vos axes de progrès ({detail})."
            if detail
            else f"Note du chapitre : {_fmt(ch.get('global'))}/100.",
        })

    def extreme_chapter(skill: str, best: bool) -> dict[str, Any] | None:
        rated = [c for c in chapters.values() if c["scores"].get(skill) is not None]
        if not rated:
            return None
        pick = max if best else min
        return pick(rated, key=lambda c: c["scores"][skill])

    def strength_text(k: str) -> str:
        ch = extreme_chapter(k, best=True)
        where = f" Votre meilleur chapitre sur ce point : le chapitre {ch['id']} « {ch['name']} »." if ch else ""
        return "L'une de vos dimensions les plus solides sur ce livre." + where

    def weakness_text(k: str) -> str:
        ch = extreme_chapter(k, best=False)
        where = (
            f" C'est au chapitre {ch['id']} « {ch['name']} » qu'elle ressort le plus "
            f"({_fmt(ch['scores'][k])}/100)."
            if ch
            else ""
        )
        return "En retrait par rapport à vos autres compétences." + where

    return {
        "summary": summary,
        "strengths": [{"skill": k, "text": strength_text(k)} for k in strengths],
        "weaknesses": [{"skill": k, "text": weakness_text(k)} for k in weaknesses],
        "improvements": [SKILL_TIPS[k] for k in weaknesses if k in SKILL_TIPS],
        "chapters_to_rework": rework,
        "progression": progression_text(results, previous),
        "source": "rules",
    }
