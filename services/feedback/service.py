"""FeedbackService — feedback général de fin de livre (IA + repli par règles)."""
from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from typing import Any, Mapping

from domain.soft_skills import SOFT_SKILLS
from services.enrichment.backends import LLMBackend, resolve_backend
from services.feedback.prompt import SYSTEM_MESSAGE, format_user_message
from services.feedback.rules import rules_feedback

log = logging.getLogger(__name__)

TEXT_MAX = 1200


def _text(value: Any) -> str:
    return " ".join(str(value).split())[:TEXT_MAX] if isinstance(value, str) else ""


def _skill_items(value: Any) -> list[dict[str, str]]:
    items = []
    for it in value if isinstance(value, list) else []:
        if isinstance(it, dict) and it.get("skill") in SOFT_SKILLS and _text(it.get("text")):
            items.append({"skill": it["skill"], "text": _text(it["text"])})
    return items[:3]


def sanitize(
    parsed: Any,
    fallback: Mapping[str, Any],
    chapter_ids: set[int],
    has_previous: bool,
) -> dict[str, Any]:
    """Valide la réponse du LLM ; chaque champ invalide reprend le repli."""
    if not isinstance(parsed, dict):
        raise ValueError("La réponse du LLM n'est pas un objet JSON.")

    rework = []
    for it in parsed.get("chapters_to_rework") if isinstance(parsed.get("chapters_to_rework"), list) else []:
        try:
            cid = int(it.get("chapter_id"))
        except (AttributeError, TypeError, ValueError):
            continue
        if cid in chapter_ids and _text(it.get("reason")):
            rework.append({"chapter_id": cid, "reason": _text(it["reason"])})

    improvements = [
        _text(s) for s in parsed.get("improvements") or [] if isinstance(s, str) and _text(s)
    ][:5]

    progression = _text(parsed.get("progression")) if has_previous else ""
    return {
        "summary": _text(parsed.get("summary")) or fallback["summary"],
        "strengths": _skill_items(parsed.get("strengths")) or fallback["strengths"],
        "weaknesses": _skill_items(parsed.get("weaknesses")) or fallback["weaknesses"],
        "improvements": improvements or fallback["improvements"],
        "chapters_to_rework": rework[:3] or fallback["chapters_to_rework"],
        "progression": (progression or fallback["progression"]) if has_previous else None,
    }


class FeedbackService:
    """Génère le feedback d'une session terminée.

    Backend : `FEEDBACK_BACKEND`, à défaut `ENRICH_BACKEND` (openai | ollama).
    En cas d'échec du LLM, le feedback par règles est renvoyé (source="rules")
    avec l'erreur, pour que le bilan reste toujours consultable.
    """

    def __init__(self, backend: LLMBackend | None = None) -> None:
        self._backend = backend

    def _get_backend(self) -> LLMBackend:
        if self._backend is None:
            name = os.getenv("FEEDBACK_BACKEND") or os.getenv("ENRICH_BACKEND", "openai")
            self._backend = resolve_backend(name)
        return self._backend

    def generate(
        self,
        book: Mapping[str, Any],
        number: int,
        results: Mapping[str, Any],
        previous: list[Mapping[str, Any]],
        weighted: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """`previous` : sessions terminées antérieures, la plus récente d'abord,
        sous forme {number, completed_on, results, feedback}."""
        fallback = rules_feedback(book.get("title", ""), number, results, previous[0] if previous else None)
        chapter_ids = {c["id"] for c in results.get("chapters") or []}
        try:
            backend = self._get_backend()
            raw = backend.complete_json(
                SYSTEM_MESSAGE,
                format_user_message(book, number, results, previous, weighted),
            )
            feedback = sanitize(json.loads(raw), fallback, chapter_ids, bool(previous))
            feedback["source"] = "ai"
            feedback["backend"] = getattr(backend, "name", "")
        except Exception as exc:  # le bilan ne doit jamais échouer à cause du LLM
            log.warning("Feedback IA indisponible, repli sur les règles : %s", exc)
            feedback = dict(fallback)
            feedback["error"] = str(exc)[:300]
        feedback["generated_at"] = datetime.now(timezone.utc).isoformat()
        return feedback
