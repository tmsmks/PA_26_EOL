"""Tests des modèles de domaine : round-trip JSON et conservation des extras."""
import json
from pathlib import Path

import pytest

from domain.models import Actor, Chapter, Interaction, Response, Scene


def test_actor_roundtrip_with_extras():
    raw = {"Id": 5, "Name": "Claude", "Age": 60, "UnknownField": "kept"}
    actor = Actor.from_dict(raw)
    assert actor.Id == 5
    assert actor.Name == "Claude"
    assert actor.to_dict() == {
        "Id": 5,
        "Name": "Claude",
        "Age": 60,
        "Role": "",
        "History": "",
        "ImageName": "",
        "UnknownField": "kept",
    }


def test_response_score_falls_back_to_flat_field():
    r = Response.from_dict({
        "Id": 1,
        "Text": "Bonjour",
        "SoftSkillDimensions": {"Empathy": 2},
        "RespectAndDignity": 3,
    })
    assert r.score("Empathy") == 2
    assert r.score("RespectAndDignity") == 3
    assert r.score("Compassion") == 0


def test_chapter_roundtrip_preserves_unknown_scene_extras():
    raw = {
        "Id": 1,
        "Name": "Test",
        "Intro": "",
        "Scenes": [{
            "Id": 1,
            "Title": "S1",
            "SceneIntroduction": "",
            "Min": 0,
            "MaxRespectAndDignity": 5,
            "MaxCompassion": 4,
            "Interactions": [],
        }],
    }
    ch = Chapter.from_dict(raw)
    rt = ch.to_dict()
    assert rt == raw


@pytest.mark.parametrize("filename", [
    "Chapters_v3-4-c_emotional-illustration.json",
    "MedStudents_Y2_v1.json",
])
def test_real_books_full_roundtrip(filename):
    """Round-trip exact sur les vrais fichiers JSON livrés."""
    base = Path(__file__).resolve().parent.parent
    path = base / "data" / "chapters" / filename
    raw = json.loads(path.read_text(encoding="utf-8"))
    for ch_raw in raw["Chapters"]:
        ch = Chapter.from_dict(ch_raw)
        assert ch.to_dict() == ch_raw, f"diff sur Chapter Id={ch.Id} dans {filename}"
