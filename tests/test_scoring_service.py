"""Tests du scoring : rejeu, qualité des choix, niveaux, profil, pondération."""
import pytest

from domain.models import Actor, Chapter, Interaction, Response, Scene
from services.scoring_service import (
    MIN_SKILL_EVIDENCE,
    InvalidPathError,
    book_profile,
    chapter_level,
    choice_quality,
    enrich_trace,
    normalized_change,
    option_stats,
    passage_results,
    quoted,
    rank_skills,
    replay_scene,
    scene_review,
    session_results,
    session_weight,
    skill_bounds,
    weighted_profile,
)


def _r(next_id, **scores):
    return Response(Text=f"r→{next_id}", NextInteractionID=next_id, SoftSkillDimensions=scores)


def _scene() -> Scene:
    """1 --(EM+2)--> 2 --(RD+1)--> fin
                        --(RD-2)--> fin
       1 --(EM-1)--> fin"""
    return Scene(
        Id=1,
        Title="Test",
        Interactions=[
            Interaction(Id=1, Text="Bonjour", Actor=Actor(Name="Mme A"), Responses=[
                _r(2, Empathy=2), _r(-1, Empathy=-1),
            ]),
            Interaction(Id=2, Text="Et alors ?", Responses=[
                _r(-1, RespectAndDignity=1), _r(-1, RespectAndDignity=-2),
            ]),
        ],
    )


def test_replay_best_path_scores_and_trace():
    run = replay_scene(_scene(), 1, [0, 0])
    assert run.raw["Empathy"] == 2 and run.raw["RespectAndDignity"] == 1
    assert len(run.trace) == 2
    assert run.trace[0]["actor"] == "Mme A"
    assert run.trace[1]["choice"]["total"] == 1 and run.trace[1]["best"]["index"] == 0


def test_replay_records_best_alternative_when_choice_is_worse():
    run = replay_scene(_scene(), 1, [0, 1])
    step = run.trace[1]
    assert step["choice"]["total"] == -2
    assert step["best"]["total"] == 1


def test_bounds_per_skill():
    lo, hi = skill_bounds(_scene(), 1)
    assert (lo["Empathy"], hi["Empathy"]) == (-1, 2)
    assert (lo["RespectAndDignity"], hi["RespectAndDignity"]) == (-2, 1)
    assert (lo["Compassion"], hi["Compassion"]) == (0, 0)


@pytest.mark.parametrize("choices", [[5], [0], [1, 0], [0, 0, 0]])
def test_replay_rejects_impossible_paths(choices):
    with pytest.raises(InvalidPathError):
        replay_scene(_scene(), 1, choices)


def test_replay_rejects_unknown_entry():
    with pytest.raises(InvalidPathError):
        replay_scene(_scene(), 2, [0])


def test_bounds_survive_cycles():
    scene = Scene(Id=1, Interactions=[
        Interaction(Id=1, Responses=[_r(2, Empathy=1)]),
        Interaction(Id=2, Responses=[_r(1, Empathy=1), _r(-1, Empathy=3)]),
    ])
    lo, hi = skill_bounds(scene, 1)
    # Meilleur : 1 → 2 → fin (+1 +3) ; pire : 1 → 2 → retour vers 1, coupé (+1 +1).
    assert hi["Empathy"] == 4
    assert lo["Empathy"] == 2


def test_trace_keeps_bounds_of_offered_responses():
    step = replay_scene(_scene(), 1, [1]).trace[0]
    assert step["bounds"]["Empathy"] == [-1, 2]
    assert step["bounds"]["Compassion"] == [0, 0]
    assert step["total_bounds"] == [-1, 2]
    assert step["chance"] == 1.5  # (3 + 0) / 2


def _plan_example():
    """Exemple du plan (§ 3.2) : quatre réponses à +9, +3, −2 et −8."""
    return [
        _r(-1, RespectAndDignity=3, Empathy=3, Compassion=3),
        _r(-1, Empathy=3),
        _r(-1, Empathy=-2),
        _r(-1, RespectAndDignity=-2, Empathy=-3, Compassion=-3),
    ]


def test_choice_quality_matches_the_plan_example():
    responses = _plan_example()
    step = {"choice": {"scores": {"Empathy": 3}, "total": 3}, **option_stats(responses)}
    q = choice_quality([step])
    assert step["chance"] == 8.5
    assert q["global"] == 64.7  # (3 + 8) / 17
    assert q["chance_corrected"] == 29.4  # (11 − 8,5) / (17 − 8,5)
    # Empathie : 3 − (−3) sur un écart de 6.
    assert q["raw_scores"]["Empathy"] == 100.0
    assert q["n_choices"] == 1 and q["steps"] == [[11, 17]]


def test_best_choice_everywhere_reaches_100():
    run = replay_scene(_scene(), 1, [0, 0])
    assert choice_quality(run.trace)["global"] == 100.0
    worst = replay_scene(_scene(), 1, [1])
    assert choice_quality(worst.trace)["global"] == 0.0


def test_a_skill_needs_enough_choices_to_be_scored():
    q = choice_quality(replay_scene(_scene(), 1, [0, 0]).trace)
    assert q["evidence"]["Empathy"] == 1 < MIN_SKILL_EVIDENCE
    assert q["scores"]["Empathy"] is None and q["raw_scores"]["Empathy"] == 100.0
    many = choice_quality(replay_scene(_scene(), 1, [0, 0]).trace * MIN_SKILL_EVIDENCE)
    assert many["scores"]["Empathy"] == 100.0


def test_v1_traces_are_enriched_from_the_book_or_skipped():
    trace = replay_scene(_scene(), 1, [0, 1]).trace
    v1 = [{k: v for k, v in st.items() if k not in ("bounds", "total_bounds", "chance")} for st in trace]
    assert choice_quality(v1)["n_choices"] == 0
    assert choice_quality(enrich_trace(_scene(), v1)) == choice_quality(trace)
    changed = [{**v1[0], "n_options": 9}]  # l'interaction a changé depuis : pas de bornes
    assert "bounds" not in enrich_trace(_scene(), changed)[0]


def test_normalized_change_marx_cummings():
    assert normalized_change(40, 70) == 50.0  # 30 gagnés sur 60 possibles
    assert normalized_change(80, 60) == -25.0  # 20 perdus sur 80
    assert normalized_change(50, 50) == 0.0
    assert normalized_change(100, 100) is None
    assert normalized_change(None, 70) is None


def _passage(globals_):
    return {"global": globals_, "raw_scores": {"Empathy": globals_}, "evidence": {"Empathy": 10},
            "n_choices": 20, "steps": [[g, 10] for g in ([3, 8, 5, 10, 0] * 4)]}


def test_chapter_level_weights_recent_passages_and_tracks_progress():
    level = chapter_level([_passage(40), _passage(60), _passage(75)])
    # (40·1 + 60·1,25 + 75·1,5) / 3,75 = 60,67, comme la note pondérée v1
    assert level["level"] == 60.7
    assert level["weights"] == [1.0, 1.25, 1.5]
    assert level["progression"] == normalized_change(40, 60.7)
    assert level["n_passages"] == 3 and level["first"] == 40 and level["last"] == 75
    assert level["scores"]["Empathy"] == 60.7
    assert chapter_level([]) is None
    assert chapter_level([_passage(50)])["progression"] is None


def test_margin_narrows_with_more_passages():
    one = chapter_level([_passage(50)])["margin"]
    three = chapter_level([_passage(50)] * 3)["margin"]
    assert one > three > 0


def test_book_profile_averages_chapters_equally_and_reports_coverage():
    a = chapter_level([_passage(80)])
    b = chapter_level([_passage(40), _passage(60)])
    profile = book_profile({1: a, 2: b, 3: None}, n_chapters=3)
    assert profile["global"] == round((80 + b["level"]) / 2, 1)
    assert profile["n_evaluated"] == 2 and profile["complete"] is False
    assert profile["n_passages"] == 3
    assert profile["progression"] == b["progression"]
    # Profil : pondéré par les choix qui mettent la compétence en jeu (10 et 10).
    assert profile["scores"]["Empathy"] == round((80 + b["raw_scores"]["Empathy"]) / 2, 1)
    assert book_profile({1: None}, 1)["global"] is None


def test_passage_results_keeps_steps_for_the_margin():
    run = replay_scene(_scene(), 1, [0, 1])
    res = passage_results([{"chapter_id": 1, "scene_id": 1, "scene_title": "T", "trace": run.trace}])
    assert res["n_scenes"] == 1 and res["n_choices"] == 2
    assert res["steps"] == [[3, 3], [0, 3]]
    assert res["global"] == 50.0


def test_rank_skills_is_relative_to_the_participant_mean():
    scores = {"Empathy": 80, "Compassion": 20, "RespectAndDignity": 50, "EmotionalRegulation": None}
    strengths, weaknesses = rank_skills(scores)
    assert strengths == ["Empathy"]
    # 50 = la moyenne : ni force ni faiblesse.
    assert weaknesses == ["Compassion"]


def test_rank_skills_high_scores_are_not_called_weak():
    scores = {"Empathy": 100, "RespectAndDignity": 100, "CommunicationClarity": 98,
              "Compassion": 86, "ProfessionalBoundaries": 86,
              "InterprofessionalCollaboration": 65, "EmotionalRegulation": 52}
    strengths, weaknesses = rank_skills(scores)
    assert strengths == ["RespectAndDignity", "Empathy", "CommunicationClarity"]
    assert weaknesses == ["EmotionalRegulation", "InterprofessionalCollaboration"]


def test_rank_skills_flat_profile_still_names_one_of_each():
    strengths, weaknesses = rank_skills({"Empathy": 50, "Compassion": 50})
    assert strengths == ["Empathy"] and weaknesses == ["Compassion"]


def test_session_weights():
    assert [session_weight(n) for n in (1, 2, 3, 4)] == [1.0, 1.25, 1.5, 1.75]


def test_weighted_profile_matches_spec_example():
    sessions = [{"scores": {"Empathy": v}} for v in (40, 60, 75)]
    profile = weighted_profile(sessions)
    # (40·1 + 60·1,25 + 75·1,5) / (1 + 1,25 + 1,5) = 60,67
    assert profile["scores"]["Empathy"] == 60.7
    assert profile["global"] == 60.7
    assert profile["weights"] == [1.0, 1.25, 1.5]
    assert weighted_profile([]) is None


def test_session_results_ranks_chapters_to_rework():
    ch1 = Chapter(Id=1, Name="Un", Scenes=[_scene()])
    ch2 = Chapter(Id=2, Name="Deux", Scenes=[_scene()])
    good = replay_scene(_scene(), 1, [0, 0])
    bad = replay_scene(_scene(), 1, [1])
    attempts = [
        {"chapter_id": 1, "scene_id": 1, "scene_title": "Test", "raw": good.raw, "lo": good.lo, "hi": good.hi, "trace": good.trace},
        {"chapter_id": 2, "scene_id": 1, "scene_title": "Test", "raw": bad.raw, "lo": bad.lo, "hi": bad.hi, "trace": bad.trace},
    ]
    res = session_results([ch1, ch2], attempts)
    assert res["n_scenes"] == 2
    assert res["chapters"][0]["global"] > res["chapters"][1]["global"]
    assert res["chapters_to_rework"][0] == 2
    assert res["moments"]["missed"][0]["chapter_id"] == 2


# --- Justification et réponses critiques (feedback d'abord) ----------------

def _keyed_scene() -> Scene:
    """Comme _scene, avec la clé : justification partout, la pire réponse du
    2ᵉ choix est critique."""
    def r(next_id, why, critical=False, **scores):
        extra = {"Rationale": why, **({"Critical": True} if critical else {})}
        return Response(Text=f"r→{next_id} {why}", NextInteractionID=next_id,
                        SoftSkillDimensions=scores, _extra=extra)

    return Scene(
        Id=1,
        Title="Clé",
        Interactions=[
            Interaction(Id=1, Text="Bonjour", Actor=Actor(Name="Mme A"), Responses=[
                r(2, "Accueille l'émotion.", Empathy=2), r(-1, "Coupe court.", Empathy=-1),
            ]),
            Interaction(Id=2, Text="Et alors ?", Responses=[
                r(-1, "Respecte le secret.", RespectAndDignity=1),
                r(-1, "Viole le secret médical.", critical=True, RespectAndDignity=-3),
                r(-1, "Reste vague.", RespectAndDignity=-1),
            ]),
        ],
    )


def test_trace_keeps_rationale_of_chosen_and_best_response():
    step = replay_scene(_keyed_scene(), 1, [0, 1]).trace[1]
    assert step["choice"]["rationale"] == "Viole le secret médical."
    assert step["choice"]["critical"] is True
    assert step["best"]["rationale"] == "Respecte le secret."
    # Livre sans clé : justification vide, rien d'inventé.
    plain = replay_scene(_scene(), 1, [0, 0]).trace[0]
    assert plain["choice"]["rationale"] == "" and plain["best"]["rationale"] == ""


def test_scene_review_puts_critical_answers_first_then_largest_gaps():
    trace = replay_scene(_keyed_scene(), 1, [0, 1]).trace
    review = scene_review(trace)
    assert len(review) == 1  # le 1ᵉʳ choix était le meilleur : rien à reprendre
    item = review[0]
    assert item["choice"]["critical"] and not item["is_best"]
    assert item["choice"]["rationale"] == "Viole le secret médical."
    assert item["best"]["rationale"] == "Respecte le secret."

    missed = scene_review(replay_scene(_keyed_scene(), 1, [0, 2]).trace)
    assert [i["choice"]["rationale"] for i in missed] == ["Reste vague."]
    assert not missed[0]["choice"]["critical"]

    # Tous les choix étaient les meilleurs : le plus décisif, avec son pourquoi.
    best = scene_review(replay_scene(_keyed_scene(), 1, [0, 0]).trace)
    assert len(best) == 1 and best[0]["is_best"]
    assert best[0]["choice"]["rationale"] == "Respecte le secret."  # écart 4 > 3

    # Au plus `limit` choix, mais toutes les réponses critiques.
    crit = trace[1]
    many = [crit, crit, crit, crit] + [replay_scene(_keyed_scene(), 1, [1]).trace[0]]
    assert len(scene_review(many, limit=3)) == 4


def test_scene_review_ignores_books_without_key():
    assert scene_review(replay_scene(_scene(), 1, [1]).trace) == []


def test_session_lists_critical_answers_apart_from_missed_moments():
    attempts = [
        {"chapter_id": 1, "scene_title": "Clé", "trace": replay_scene(_keyed_scene(), 1, [0, 1]).trace},
        {"chapter_id": 2, "scene_title": "Clé", "trace": replay_scene(_keyed_scene(), 1, [1]).trace},
    ]
    res = session_results([Chapter(Id=1, Name="Un"), Chapter(Id=2, Name="Deux")], attempts)
    assert [(c["chapter_id"], c["choice"]["rationale"]) for c in res["critical"]] == [
        (1, "Viole le secret médical.")]
    assert res["critical"][0]["gap"] == 4
    # La réponse critique (écart 4) n'est pas répétée parmi les occasions manquées.
    assert all(not m["choice"]["critical"] for m in res["moments"]["missed"])
    assert [m["choice"]["rationale"] for m in res["moments"]["missed"]] == ["Coupe court."]


def test_quoted_does_not_wrap_a_gesture_that_carries_its_own_speech():
    assert quoted("Bonjour.") == "« Bonjour. »"
    assert quoted("« Bonjour. »") == "« Bonjour. »"
    assert quoted("« Bonjour, je…") == "« Bonjour, je… »"  # tronquée
    gesture = "Poser la main sur son téléphone. « Range-le. »"
    assert quoted(gesture) == gesture
    assert quoted("Poser la main. « Range-le, et…") == "Poser la main. « Range-le, et… »"
