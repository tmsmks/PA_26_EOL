"""Validation EG-7 : NextInteractionID doivent pointer vers des Id valides ou -1."""
from __future__ import annotations

from dataclasses import dataclass

from domain.models import Chapter


@dataclass(frozen=True)
class ValidationError:
    chapter_id: int
    scene_id: int
    scene_title: str
    interaction_id: int
    response_idx: int
    invalid_next_id: int

    def __str__(self) -> str:
        return (
            f"EG-7: NextInteractionID {self.invalid_next_id} invalide "
            f"(scène '{self.scene_title}', interaction {self.interaction_id}, "
            f"réponse {self.response_idx + 1})"
        )


def validate_next_interaction_ids(chapters: list[Chapter]) -> list[ValidationError]:
    """Retourne la liste des références NextInteractionID invalides.

    Une référence est valide si elle pointe vers un Id existant dans la même
    scène, ou vaut -1 (fin de branche).
    """
    errors: list[ValidationError] = []
    for ch in chapters:
        for scene in ch.Scenes:
            valid_ids = {ia.Id for ia in scene.Interactions}
            for ia in scene.Interactions:
                for r_idx, r in enumerate(ia.Responses):
                    nid = r.NextInteractionID
                    if nid is None or nid == -1:
                        continue
                    if nid not in valid_ids:
                        errors.append(ValidationError(
                            chapter_id=ch.Id,
                            scene_id=scene.Id,
                            scene_title=scene.Title,
                            interaction_id=ia.Id,
                            response_idx=r_idx,
                            invalid_next_id=nid,
                        ))
    return errors
