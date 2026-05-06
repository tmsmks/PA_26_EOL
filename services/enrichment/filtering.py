"""Filtrage des doublons côté propositions LLM (règle 4.2)."""
from __future__ import annotations

from typing import Any


def filter_duplicate_texts(
    candidates: list[dict[str, Any]],
    existing_responses: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Supprime les candidats dont le texte duplique (à la casse près) un existant."""
    seen = {
        (r.get("Text") or "").strip().lower()
        for r in existing_responses
        if (r.get("Text") or "").strip()
    }
    out: list[dict[str, Any]] = []
    for c in candidates:
        txt = (c.get("Text") or "").strip()
        if not txt:
            continue
        if txt.lower() in seen:
            continue
        out.append(c)
    return out
