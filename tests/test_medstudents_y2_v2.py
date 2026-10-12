"""Tests du livre MedStudents Y2 v2 « Le corps donné » : sources, JSON généré, états narratifs."""
import copy
import json
import os
import sys

import pytest

from books import chapters_path, get_book
from domain.models import Chapter
from domain.soft_skills import SOFT_SKILLS
from services.graph_service import chapter_meta, scene_slot
from services.scoring_service import MIN_SKILL_EVIDENCE
from services.validation_service import validate_entry_points, validate_next_interaction_ids

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import build_medstudents_y2_v2 as build  # noqa: E402
from medstudents_y2_v2.book import CHAPTERS  # noqa: E402
from medstudents_y2_v2.dsl import parse_scores  # noqa: E402
from medstudents_y2_v2.key import KeyMismatch, apply_key, load_key  # noqa: E402


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


def test_book_has_five_chapters_of_five_or_six_scenarios(chapters):
    """La demande (10.10.2026) : cinq chapitres d'environ cinq ou six scénarios.
    Un emplacement à branches parallèles compte pour un scénario (une seule est
    jouée) ; une histoire annexe s'ajoute quand elle est débloquée."""
    assert len(chapters) == 5
    for ch in chapters:
        mandatory = {scene_slot(sc) for sc in ch.Scenes if not sc._extra.get("Annex")}
        everything = {scene_slot(sc) for sc in ch.Scenes}
        assert 5 <= len(mandatory) <= 6, ch.Name
        assert len(everything) <= 6, ch.Name


def test_book_has_about_five_hundred_interactions(chapters):
    n = sum(len(sc.Interactions) for ch in chapters for sc in ch.Scenes)
    assert 480 <= n <= 530, n


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


# --- Clé de notation -------------------------------------------------------

@pytest.fixture(scope="module")
def audit() -> dict:
    """Joueur·euse·s simulé·e·s rejoué·e·s par le vrai calcul serveur."""
    return build.scoring_audit(CHAPTERS)


def test_simulated_players_span_the_whole_scale(audit):
    """Toujours la meilleure réponse = 100, toujours la pire = 0, au hasard ≈ 50 :
    le rejeu serveur et la clé de notation sont cohérents, chapitre par chapitre."""
    sim = audit["simulated"]
    for cid in [str(c.id) for c in CHAPTERS] + ["book"]:
        assert sim["best"][cid] == 100, cid
        assert sim["worst"][cid] == 0, cid
        assert 35 <= sim["random"][cid] <= 60, cid


def test_answer_length_does_not_give_the_best_answer_away(audit):
    """Le livre v1 donnait 89,5/100 en choisissant toujours la réponse la plus longue."""
    for cid in [str(c.id) for c in CHAPTERS] + ["book"]:
        assert audit["simulated"]["longest"][cid] <= build.BLIND_MAX, cid
        assert audit["simulated"]["shortest"][cid] <= build.BLIND_MAX, cid
    for cid, blind in audit["blind_static"].items():
        assert max(blind.values()) <= build.BLIND_MAX, (cid, blind)
    ranks = audit["best_length_ranks"]
    assert ranks["1"] / sum(ranks.values()) < 0.4, ranks


def test_every_skill_is_scored_on_every_path(audit):
    """Chaque compétence est en jeu dans assez de choix pour être notée, même sur le
    parcours le plus court de chaque chapitre (et dans toutes les parties simulées)."""
    assert audit["random_unscored_skills"] == 0
    for cid, evidence in audit["min_evidence"].items():
        for skill, n in evidence.items():
            assert n >= MIN_SKILL_EVIDENCE, (cid, skill, n)


def test_skills_are_evenly_represented_in_the_answers():
    """Chaque compétence pèse entre 10 et 20 % des points positifs du livre."""
    pos = {k: 0 for k in SOFT_SKILLS}
    for ch in CHAPTERS:
        for sc in ch.scenes:
            for n in sc.nodes:
                for r in n.responses:
                    for k, v in r.soft().items():
                        pos[k] += max(v, 0)
    total = sum(pos.values())
    for k, v in pos.items():
        assert 0.10 <= v / total <= 0.20, (k, round(100 * v / total, 1))


def _first_choice_point(chapter):
    return next(n for sc in chapter.scenes for n in sc.nodes if len(n.responses) > 1)


def test_validation_rejects_a_tied_best_answer():
    ch = copy.deepcopy(CHAPTERS[0])
    node = _first_choice_point(ch)
    totals = [r.total() for r in node.responses]
    best = totals.index(max(totals))
    twin = next(i for i in range(len(totals)) if i != best)
    node.responses[twin].scores = node.responses[best].scores
    errors = build._validate_scoring([ch])
    assert any("ex aequo" in e for e in errors), errors


def test_validation_rejects_a_length_cue():
    """Si la meilleure réponse est toujours la plus longue, le build échoue."""
    ch = copy.deepcopy(CHAPTERS[0])
    for sc in ch.scenes:
        for n in sc.nodes:
            if len(n.responses) > 1:
                totals = [r.total() for r in n.responses]
                best = n.responses[totals.index(max(totals))]
                best.text += " " + "x" * 400
    errors = build._validate_scoring([ch])
    assert any("la longueur trahit" in e for e in errors), errors


# --- Clé de cotation (data/keys) ---------------------------------------------

def test_key_scores_every_answer_of_every_choice_point(chapters):
    """La clé couvre toutes les réponses des points de choix, et le JSON la porte :
    cotes, justification, drapeau critique."""
    key = load_key()["reponses"]
    n_answers = 0
    for ch in chapters:
        for sc in ch.Scenes:
            for ia in sc.Interactions:
                if len(ia.Responses) < 2:
                    continue
                for no, r in enumerate(ia.Responses, start=1):
                    item = key[f"c{ch.Id}-s{sc.Id}-i{ia.Id}-r{no}"]
                    n_answers += 1
                    assert r.Text.startswith(item["texte"])
                    assert r.SoftSkillDimensions == parse_scores(item["cotes"])
                    assert r._extra.get("Rationale") == item["justification"]
                    assert bool(r._extra.get("Critical")) == item["critique"]
    assert n_answers == len(key)


def test_key_refuses_an_answer_rewritten_since_the_rating():
    """Une réponse réécrite après la cotation arrête le build au lieu de recevoir
    la cote d'une autre."""
    ch = copy.deepcopy(CHAPTERS[0])
    _first_choice_point(ch).responses[0].text = "Une tout autre réponse."
    with pytest.raises(KeyMismatch, match="le texte a changé"):
        apply_key([ch])
