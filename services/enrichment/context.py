"""Construction du contexte LLM à partir d'un chapitre/scène/interaction."""
from __future__ import annotations

from typing import Any

from domain.models import Chapter


class InteractionNotFoundError(LookupError):
    """Levée quand un (chapter_id, scene_id, interaction_id) est introuvable."""


def build_context(
    chapters: list[Chapter],
    chapter_id: int,
    scene_id: int,
    interaction_id: int,
    next_interaction_id: int | None = None,
) -> dict[str, Any]:
    """Construit le contexte d'enrichissement (cf. spec 4.2).

    Inclut SceneIntroduction, profil acteur, réponses existantes et,
    optionnellement, l'interaction suivante (`next_interaction_id`).
    """
    chapter = next((ch for ch in chapters if ch.Id == chapter_id), None)
    if chapter is None:
        raise InteractionNotFoundError(f"Chapitre Id={chapter_id} introuvable.")
    scene = next((s for s in chapter.Scenes if s.Id == scene_id), None)
    if scene is None:
        raise InteractionNotFoundError(
            f"Scène Id={scene_id} introuvable dans chapitre {chapter_id}."
        )
    interaction = next(
        (ia for ia in scene.Interactions if ia.Id == interaction_id), None
    )
    if interaction is None:
        raise InteractionNotFoundError(
            f"Interaction Id={interaction_id} introuvable dans scène {scene_id}."
        )

    existing_responses = [
        {
            "Id": r.Id,
            "Name": r.Name,
            "Text": r.Text,
            "SoftSkillDimensions": dict(r.SoftSkillDimensions),
            "LegacyDimensions": dict(r.LegacyDimensions),
            "NextInteractionID": r.NextInteractionID,
        }
        for r in interaction.Responses
    ]

    next_block: dict[str, Any] | None = None
    if next_interaction_id is not None:
        nxt_id = int(next_interaction_id)
        if nxt_id == -1:
            next_block = {"Id": -1, "EndOfBranch": True}
        else:
            nxt = next((ia for ia in scene.Interactions if ia.Id == nxt_id), None)
            if nxt is not None:
                next_block = {
                    "Id": nxt.Id,
                    "Name": nxt.Name,
                    "Text": nxt.Text,
                    "Actor": nxt.Actor.to_dict(),
                }

    result: dict[str, Any] = {
        "chapter": {"Id": chapter.Id, "Name": chapter.Name},
        "scene": {
            "Id": scene.Id,
            "Title": scene.Title,
            "SceneIntroduction": scene.SceneIntroduction,
            "Min": scene.Min,
        },
        "interaction": {
            "Id": interaction.Id,
            "Name": interaction.Name,
            "Text": interaction.Text,
            "Actor": interaction.Actor.to_dict(),
        },
        "existing_responses": existing_responses,
    }
    if next_block is not None:
        result["next_interaction"] = next_block
    return result
