"""Tests du livre MedStudents Y2 v2 « Le corps donné » : sources, JSON généré, états narratifs."""
import json
import os
import sys

import pytest

from books import chapters_path, get_book
from domain.models import Chapter
from services.graph_service import chapter_meta, scene_slot
from services.validation_service import validate_entry_points, validate_next_interaction_ids

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import build_medstudents_y2_v2 as build  # noqa: E402
from medstudents_y2_v2.book import CHAPTERS  # noqa: E402


@pytest.fixture(scope="module")
def chapters() -> list[Chapter]:
    with open(chapters_path("medstudents_y2"), encoding="utf-8") as f:
        raw = json.load(f)
    return [Chapter.from_dict(c) for c in raw["Chapters"]]


def test_book_points_to_v2():
    assert get_book("medstudents_y2")["json"] == "MedStudents_Y2_v2.json"


def test_sources_pass_the_build_validation():
    errors, _ = build.validate(CHAPTERS)
    assert errors == []


def test_generated_json_matches_sources():
    """Le JSON commité est celui que produisent les sources (pas d'édition à la main)."""
    with open(build.OUT_JSON, encoding="utf-8") as f:
        assert json.load(f) == {"Chapters": [c.to_dict() for c in CHAPTERS]}


def test_generated_json_is_valid(chapters):
    assert validate_next_interaction_ids(chapters) == []
    assert validate_entry_points(chapters) == []


def test_every_chapter_plays_at_least_four_scenes(chapters):
    """La demande : au moins quatre scénarios joués par chapitre (annexes non comptées)."""
    for ch in chapters:
        mandatory = {scene_slot(sc) for sc in ch.Scenes if not sc._extra.get("Annex")}
        assert len(mandatory) >= 4, ch.Name


def test_every_scene_declares_a_soft_skill_focus(chapters):
    for ch in chapters:
        for sc in ch.Scenes:
            assert sc._extra.get("SoftSkillFocus"), sc.Title


def test_every_chapter_has_very_good_and_very_bad_choices(chapters):
    for ch in chapters:
        totals = [sum(r.SoftSkillDimensions.values())
                  for sc in ch.Scenes for ia in sc.Interactions
                  if len(ia.Responses) > 1 for r in ia.Responses]
        assert max(totals) >= 9, ch.Name
        assert min(totals) <= -7, ch.Name


def test_every_choice_point_offers_four_to_six_answers(chapters):
    """Les interactions à 0 ou 1 réponse sont des fins de scène ou des « Continuer »."""
    for ch in chapters:
        for sc in ch.Scenes:
            for ia in sc.Interactions:
                if len(ia.Responses) >= 2:
                    assert 4 <= len(ia.Responses) <= 6, (sc.Title, ia.Id)


def test_parallel_branches_and_side_stories_are_wired(chapters):
    ch1 = chapters[0]
    by_slot: dict[str, list] = {}
    for sc in ch1.Scenes:
        by_slot.setdefault(scene_slot(sc), []).append(sc)
    # Branche parallèle 1.5 : deux scènes, l'une si la photo a circulé, l'autre sinon.
    conditions = [sc._extra.get("Condition") for sc in by_slot["1.5"]]
    assert {"all": ["photo_virale"]} in conditions
    assert {"none": ["photo_virale"]} in conditions
    # Histoire annexe 1.6 : débloquée par le soutien à Noah en 1.1.
    (annex,) = by_slot["1.6"]
    assert annex._extra.get("Annex") is True
    assert annex._extra.get("Condition") == {"all": ["noah_soutenu"]}
    assert {"photo_virale", "photo_supprimee", "noah_soutenu"} <= set(
        chapter_meta(ch1)["owned_flags"])


def test_report_is_up_to_date_with_sources():
    """Le rapport soft skills commité correspond aux scores des sources."""
    _, data = build.build_report(CHAPTERS)
    with open(build.OUT_REPORT_JSON, encoding="utf-8") as f:
        assert json.load(f) == json.loads(json.dumps(data))
