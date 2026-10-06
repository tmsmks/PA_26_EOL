"""Tests du feedback général : validation IA, repli, prise en compte de l'historique."""
import json

from services.enrichment.backends import LLMBackendError
from services.feedback import FeedbackService
from services.feedback.prompt import format_user_message

BOOK = {"title": "Livre test", "audience": "Étudiant·e·s"}

RESULTS = {
    "scores": {"Empathy": 80.0, "Compassion": 30.0, "RespectAndDignity": 55.0},
    "global": 55.0,
    "chapters": [
        {"id": 1, "name": "Un", "scores": {"Empathy": 90.0, "Compassion": 40.0}, "global": 65.0},
        {"id": 2, "name": "Deux", "scores": {"Empathy": 70.0, "Compassion": 20.0}, "global": 45.0},
    ],
    "strengths": ["Empathy"],
    "weaknesses": ["Compassion", "RespectAndDignity"],
    "chapters_to_rework": [2],
    "moments": {"missed": [], "good": []},
    "n_scenes": 4,
}

PREVIOUS = {
    "number": 1,
    "completed_on": "01.09.2026",
    "results": {"scores": {"Empathy": 60.0, "Compassion": 35.0}, "global": 47.0},
    "feedback": {"weaknesses": [{"skill": "Empathy", "text": "…"}], "improvements": ["Reformulez."]},
}


class FakeBackend:
    name = "fake"

    def __init__(self, reply=None, error=None):
        self.reply, self.error, self.calls = reply, error, []

    def complete_json(self, system_msg, user_msg):
        self.calls.append(user_msg)
        if self.error:
            raise self.error
        return json.dumps(self.reply)


AI_REPLY = {
    "summary": "Bonne session.",
    "strengths": [{"skill": "Empathy", "text": "Vous reformulez."}, {"skill": "Inventée", "text": "x"}],
    "weaknesses": [{"skill": "Compassion", "text": "Restez présent."}],
    "improvements": ["Reformulez l'émotion.", 42],
    "chapters_to_rework": [{"chapter_id": 2, "reason": "Compassion faible."}, {"chapter_id": 99, "reason": "?"}],
    "progression": "Vous progressez.",
}


def test_ai_feedback_is_sanitized():
    fb = FeedbackService(FakeBackend(AI_REPLY)).generate(BOOK, 1, RESULTS, [])
    assert fb["source"] == "ai"
    assert [s["skill"] for s in fb["strengths"]] == ["Empathy"]
    assert fb["improvements"] == ["Reformulez l'émotion."]
    assert [c["chapter_id"] for c in fb["chapters_to_rework"]] == [2]
    # Première session : pas de paragraphe de progression, même si le LLM en invente un.
    assert fb["progression"] is None


def test_llm_failure_falls_back_to_rules():
    fb = FeedbackService(FakeBackend(error=LLMBackendError("quota"))).generate(BOOK, 1, RESULTS, [])
    assert fb["source"] == "rules"
    assert "quota" in fb["error"]
    assert [w["skill"] for w in fb["weaknesses"]] == ["Compassion", "RespectAndDignity"]
    assert fb["chapters_to_rework"][0]["chapter_id"] == 2
    assert fb["improvements"]


def test_invalid_json_falls_back_to_rules():
    backend = FakeBackend()
    backend.complete_json = lambda s, u: "pas du json"
    fb = FeedbackService(backend).generate(BOOK, 1, RESULTS, [])
    assert fb["source"] == "rules"


def test_previous_sessions_reach_prompt_and_progression():
    backend = FakeBackend(AI_REPLY)
    fb = FeedbackService(backend).generate(BOOK, 2, RESULTS, [PREVIOUS], {"global": 52.0, "n_sessions": 2})
    prompt = backend.calls[0]
    assert "SESSIONS PRÉCÉDENTES" in prompt
    assert "Session 1" in prompt and "Reformulez." in prompt
    assert "Empathy +20" in prompt
    assert fb["progression"] == "Vous progressez."


def test_rules_progression_mentions_previous_session():
    fb = FeedbackService(FakeBackend(error=RuntimeError("down"))).generate(BOOK, 2, RESULTS, [PREVIOUS])
    assert "session 1" in fb["progression"]
    assert "+8" in fb["progression"]


def test_prompt_contains_no_personal_data_fields():
    msg = format_user_message(BOOK, 1, RESULTS, [], None)
    assert "première session" in msg
    assert "username" not in msg and "display_name" not in msg
