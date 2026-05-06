"""Domain layer — modèles métier purs (zéro dépendance externe)."""
from domain.models import (
    Actor,
    Book,
    Chapter,
    Interaction,
    Response,
    Scene,
    SoftSkillScores,
)
from domain.soft_skills import (
    LEGACY_SKILLS,
    SOFT_SKILL_LABELS,
    SOFT_SKILLS,
)

__all__ = [
    "Actor",
    "Book",
    "Chapter",
    "Interaction",
    "Response",
    "Scene",
    "SoftSkillScores",
    "LEGACY_SKILLS",
    "SOFT_SKILL_LABELS",
    "SOFT_SKILLS",
]
