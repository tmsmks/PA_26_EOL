"""Tests de la validation/normalisation des EnrichRequest."""
import pytest

from services.enrichment import EnrichRequest


def test_required_ids_must_be_present():
    with pytest.raises(ValueError):
        EnrichRequest.from_payload({"chapter_id": 1, "scene_id": 1})


def test_orientation_clamped_to_minus_three_to_three():
    req = EnrichRequest.from_payload({
        "chapter_id": 1, "scene_id": 1, "interaction_id": 1,
        "orientation": {"Empathy": 99, "RespectAndDignity": -99},
    })
    assert req.orientation == {"Empathy": 3, "RespectAndDignity": -3}


def test_orientation_unknown_skill_is_ignored():
    req = EnrichRequest.from_payload({
        "chapter_id": 1, "scene_id": 1, "interaction_id": 1,
        "orientation": {"BadKey": 2, "Empathy": 1},
    })
    assert req.orientation == {"Empathy": 1}


def test_n_proposals_clamped_to_one_three():
    req = EnrichRequest.from_payload({
        "chapter_id": 1, "scene_id": 1, "interaction_id": 1, "n": 99,
    })
    assert req.n_proposals == 3
    req2 = EnrichRequest.from_payload({
        "chapter_id": 1, "scene_id": 1, "interaction_id": 1, "n": 0,
    })
    assert req2.n_proposals == 1


def test_next_interaction_id_invalid_becomes_none():
    req = EnrichRequest.from_payload({
        "chapter_id": 1, "scene_id": 1, "interaction_id": 1,
        "next_interaction_id": "not-an-int",
    })
    assert req.next_interaction_id is None
