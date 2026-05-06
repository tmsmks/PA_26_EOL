"""EnrichmentService — façade publique du module d'enrichissement."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any

from domain.soft_skills import SOFT_SKILLS
from repositories.chapters import ChapterRepository
from services.enrichment.backends import LLMBackend, LLMBackendError, resolve_backend
from services.enrichment.context import (
    InteractionNotFoundError,
    build_context,
)
from services.enrichment.filtering import filter_duplicate_texts
from services.enrichment.prompt import SYSTEM_MESSAGE, format_user_message


@dataclass
class EnrichRequest:
    """Requête d'enrichissement validée et normalisée."""

    book_slug: str | None
    chapter_id: int
    scene_id: int
    interaction_id: int
    next_interaction_id: int | None = None
    orientation: dict[str, int] = field(default_factory=dict)
    guidance: str | None = None
    n_proposals: int = 1

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "EnrichRequest":
        """Construit la requête depuis un JSON HTTP, en validant et clampant."""
        for key in ("chapter_id", "scene_id", "interaction_id"):
            if payload.get(key) is None:
                raise ValueError(
                    "chapter_id, scene_id et interaction_id sont requis."
                )

        raw_orientation = payload.get("orientation") or {}
        orientation: dict[str, int] = {}
        for skill in SOFT_SKILLS:
            v = raw_orientation.get(skill)
            if v is None:
                continue
            try:
                orientation[skill] = max(-3, min(3, int(v)))
            except (TypeError, ValueError):
                continue

        try:
            n = int(payload.get("n", 1))
        except (TypeError, ValueError):
            n = 1
        n = max(1, min(3, n))

        next_id_raw = payload.get("next_interaction_id")
        next_id: int | None
        if next_id_raw is None:
            next_id = None
        else:
            try:
                next_id = int(next_id_raw)
            except (TypeError, ValueError):
                next_id = None

        return cls(
            book_slug=payload.get("book_slug"),
            chapter_id=int(payload["chapter_id"]),
            scene_id=int(payload["scene_id"]),
            interaction_id=int(payload["interaction_id"]),
            next_interaction_id=next_id,
            orientation=orientation,
            guidance=(payload.get("guidance") or None),
            n_proposals=n,
        )


Proposal = dict[str, Any]


class EnrichmentService:
    """Façade : prend une EnrichRequest, retourne des Proposals filtrés."""

    def __init__(
        self,
        repository: ChapterRepository | None = None,
        backend: LLMBackend | None = None,
    ) -> None:
        self._repo = repository or ChapterRepository()
        if backend is None:
            backend_name = os.getenv("ENRICH_BACKEND", "openai")
            backend = resolve_backend(backend_name)
        self._backend = backend

    def propose_responses(self, request: EnrichRequest) -> list[Proposal]:
        chapters = self._repo.load_chapters(request.book_slug)
        try:
            context = build_context(
                chapters,
                chapter_id=request.chapter_id,
                scene_id=request.scene_id,
                interaction_id=request.interaction_id,
                next_interaction_id=request.next_interaction_id,
            )
        except InteractionNotFoundError:
            raise

        user_msg = format_user_message(
            context,
            orientation=request.orientation or None,
            guidance=request.guidance,
            n_proposals=request.n_proposals,
        )
        raw = self._backend.complete_json(SYSTEM_MESSAGE, user_msg)

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise LLMBackendError(f"Réponse LLM non valide (JSON) : {exc}") from exc

        candidates = parsed.get("responses") or []
        if not isinstance(candidates, list):
            raise LLMBackendError(
                "Format LLM inattendu : 'responses' doit être une liste."
            )
        return filter_duplicate_texts(candidates, context.get("existing_responses", []))
