"""Constantes des soft skills (dimensions des réponses)."""
from __future__ import annotations

from typing import Final

SOFT_SKILLS: Final[tuple[str, ...]] = (
    "RespectAndDignity",
    "Empathy",
    "Compassion",
    "EmotionalRegulation",
    "CommunicationClarity",
    "ProfessionalBoundaries",
    "InterprofessionalCollaboration",
)

SOFT_SKILL_LABELS: Final[dict[str, str]] = {
    "RespectAndDignity": "Respect et dignité",
    "Empathy": "Empathie",
    "Compassion": "Compassion",
    "EmotionalRegulation": "Régulation émotionnelle",
    "CommunicationClarity": "Clarté de communication",
    "ProfessionalBoundaries": "Frontières professionnelles",
    "InterprofessionalCollaboration": "Collaboration interprofessionnelle",
}

LEGACY_SKILLS: Final[tuple[str, ...]] = (
    "Authenticity",
    "Respect",
    "Compassion",
    "Hope",
    "Empathy",
)
