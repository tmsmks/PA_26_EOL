"""Tests du livre MedStudents Y4 v2 : sources, JSON généré et états narratifs."""
import json
import os
import sys

import pytest

from books import chapters_path, get_book
from domain.models import Chapter
from services.graph_service import chapter_meta, chapter_outline
from services.validation_service import validate_entry_points, validate_next_interaction_ids

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import build_medstudents_y4_v2 as build  # noqa: E402
from medstudents_y4_v2.book import CHAPTERS  # noqa: E402


@pytest.fixture(scope="module")
def chapters() -> list[Chapter]:
    with open(chapters_path("medstudents_y4"), encoding="utf-8") as f:
        raw = json.load(f)
    return [Chapter.from_dict(c) for c in raw["Chapters"]]


def test_book_points_to_v2():
    assert get_book("medstudents_y4")["json"] == "MedStudents_Y4_v2.json"


def test_sources_pass_the_build_validation():
    errors, _ = build.validate(CHAPTERS)
    assert errors == []


def test_generated_json_is_valid(chapters):
    assert validate_next_interaction_ids(chapters) == []
    assert validate_entry_points(chapters) == []


def test_six_chapters_of_five_or_six_played_scenes(chapters):
    assert len(chapters) == 6
    for ch in chapters:
        assert 5 <= chapter_outline(ch)["n_scenes"] <= 6, ch.Name


def test_every_scene_declares_a_soft_skill_focus(chapters):
    for ch in chapters:
        for sc in ch.Scenes:
            assert sc._extra.get("SoftSkillFocus"), sc.Title


def test_every_played_track_contains_very_bad_and_very_good_choices(chapters):
    """La demande : dans chaque chapitre, des choix très bons et très mauvais."""
    for ch in chapters:
        totals = [sum(r.SoftSkillDimensions.values())
                  for sc in ch.Scenes for ia in sc.Interactions
                  if len(ia.Responses) > 1 for r in ia.Responses]
        assert max(totals) >= 9, ch.Name
        assert min(totals) <= -7, ch.Name


def test_error_consequences_are_wired_across_chapters(chapters):
    ch5, ch6 = chapters[4], chapters[5]
    assert {"erreur", "evite", "deces", "survie"} <= set(chapter_meta(ch5)["owned_flags"])
    start = chapter_meta(ch6)["start_choice"]
    assert start and set(start["unless_any"]) == {"erreur", "evite"}
    conditions = {tuple(sc._extra.get("Condition", {}).get("all", [])) for sc in ch6.Scenes}
    assert ("erreur",) in conditions and ("evite",) in conditions


def test_report_is_up_to_date_with_sources():
    """Le rapport soft skills commité correspond aux scores des sources."""
    _, data = build.build_report(CHAPTERS)
    with open(build.OUT_REPORT_JSON, encoding="utf-8") as f:
        assert json.load(f) == json.loads(json.dumps(data))


def test_every_choice_point_offers_at_least_four_answers(chapters):
    """Pas de « trois réponses et puis c'est tout » : 4 réponses minimum.

    Les interactions à 0 ou 1 réponse sont des fins de scène ou des issues
    narratives (« Continuer »), pas des choix.
    """
    for ch in chapters:
        for sc in ch.Scenes:
            for ia in sc.Interactions:
                if len(ia.Responses) >= 2:
                    assert len(ia.Responses) >= 4, (sc.Title, ia.Id)
