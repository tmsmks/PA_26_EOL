"""Tests EG-7 — validation des NextInteractionID."""
from domain.models import Chapter, Interaction, Response, Scene
from services.validation_service import validate_next_interaction_ids


def _build_chapter(responses_next_ids: list[int]) -> Chapter:
    """Helper : 1 chapitre, 1 scène, 2 interactions, N réponses dans la 1ère."""
    interactions = [
        Interaction(
            Id=1,
            Responses=[Response(Id=i + 1, NextInteractionID=nid) for i, nid in enumerate(responses_next_ids)],
        ),
        Interaction(Id=2),
    ]
    return Chapter(
        Id=1, Name="C", Scenes=[Scene(Id=1, Title="S", Interactions=interactions)]
    )


def test_no_errors_when_all_ids_valid():
    ch = _build_chapter([2, -1])
    assert validate_next_interaction_ids([ch]) == []


def test_no_errors_when_next_id_is_minus_one():
    ch = _build_chapter([-1])
    assert validate_next_interaction_ids([ch]) == []


def test_no_errors_when_next_id_is_none():
    ch = _build_chapter([None])  # type: ignore[list-item]
    assert validate_next_interaction_ids([ch]) == []


def test_error_when_next_id_unknown():
    ch = _build_chapter([2, 99])
    errors = validate_next_interaction_ids([ch])
    assert len(errors) == 1
    err = errors[0]
    assert err.invalid_next_id == 99
    assert err.chapter_id == 1
    assert err.scene_id == 1
    assert err.interaction_id == 1
    assert err.response_idx == 1
    assert "EG-7" in str(err)
