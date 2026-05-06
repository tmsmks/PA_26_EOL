"""Tests du filtrage des doublons LLM."""
from services.enrichment.filtering import filter_duplicate_texts


def test_removes_exact_duplicate():
    existing = [{"Text": "Bonjour, comment allez-vous ?"}]
    candidates = [
        {"Text": "Bonjour, comment allez-vous ?"},
        {"Text": "Je vous écoute."},
    ]
    out = filter_duplicate_texts(candidates, existing)
    assert out == [{"Text": "Je vous écoute."}]


def test_case_insensitive_duplicate():
    existing = [{"Text": "JE VOUS ÉCOUTE."}]
    candidates = [{"Text": "je vous écoute."}]
    assert filter_duplicate_texts(candidates, existing) == []


def test_strips_whitespace():
    existing = [{"Text": "  Bonjour  "}]
    candidates = [{"Text": "Bonjour"}]
    assert filter_duplicate_texts(candidates, existing) == []


def test_skips_empty_text_candidates():
    candidates = [{"Text": ""}, {"Text": "   "}, {"Text": "OK"}]
    assert filter_duplicate_texts(candidates, []) == [{"Text": "OK"}]
