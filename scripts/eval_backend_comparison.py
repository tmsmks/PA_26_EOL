#!/usr/bin/env python3
"""
eval_backend_comparison.py — Compare OpenAI et Ollama sur les mêmes prompts.

Lance 10 générations identiques sur chaque backend et compare :
- Temps de réponse
- Taux de JSON valide
- Conformité à l'orientation
- Qualité textuelle (longueur, cohérence)

Usage :
    # Les deux backends doivent être accessibles :
    export OPENAI_API_KEY="sk-..."
    # + Ollama doit tourner : ollama serve

    python scripts/eval_backend_comparison.py

Résultats écrits dans : output/eval_backend_comparison.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.soft_skills import SOFT_SKILLS, SOFT_SKILL_LABELS
from repositories.chapters import ChapterRepository
from services.enrichment.backends import OpenAIBackend, OllamaBackend, LLMBackendError
from services.enrichment.context import build_context
from services.enrichment.prompt import SYSTEM_MESSAGE, format_user_message
from services.enrichment.filtering import filter_duplicate_texts

BOOK_SLUG = "end_of_life"

# 10 configurations de test (interaction + orientation)
TEST_CONFIGS = [
    {
        "ids": (1, 1, 1),
        "orientation": {"Empathy": 2, "RespectAndDignity": 2, "Compassion": 1},
        "label": "Empathique — Présentation I1",
    },
    {
        "ids": (1, 1, 6),
        "orientation": {"Empathy": -2, "RespectAndDignity": -1},
        "label": "Problématique — Présentation I6",
    },
    {
        "ids": (1, 1, 13),
        "orientation": {"Empathy": 3, "Compassion": 3},
        "label": "Très compassionnel — I13",
    },
    {
        "ids": (1, 2, 1),
        "orientation": {"CommunicationClarity": 2, "ProfessionalBoundaries": 2},
        "label": "Professionnel — Pascal I1",
    },
    {
        "ids": (1, 3, 5),
        "orientation": {"EmotionalRegulation": 2, "Empathy": 1},
        "label": "Régulé — Les soins I5",
    },
    {
        "ids": (1, 3, 18),
        "orientation": {"Compassion": 3, "Empathy": 3, "EmotionalRegulation": -1},
        "label": "Compassionnel débordant — I18",
    },
    {
        "ids": (2, 1, 5),
        "orientation": {"Empathy": 0, "Compassion": 0},
        "label": "Neutre — Lieu de vie I5",
    },
    {
        "ids": (2, 1, 12),
        "orientation": {"InterprofessionalCollaboration": 2, "CommunicationClarity": 2},
        "label": "Collaboratif — Lieu de vie I12",
    },
    {
        "ids": (3, 1, 1),
        "orientation": {"Empathy": 2, "Compassion": 2, "RespectAndDignity": 2},
        "label": "Empathique — Dyspnée I1",
    },
    {
        "ids": (3, 1, 15),
        "orientation": {"ProfessionalBoundaries": 3, "EmotionalRegulation": 2},
        "label": "Cadré — Dyspnée I15",
    },
]


def run_one(
    backend,
    backend_name: str,
    chapters,
    config: dict,
) -> dict[str, Any]:
    """Lance une génération avec un backend donné."""
    ch_id, sc_id, ia_id = config["ids"]
    ori = {k: v for k, v in config["orientation"].items() if k in SOFT_SKILLS}

    ctx = build_context(chapters, ch_id, sc_id, ia_id)
    user_msg = format_user_message(ctx, orientation=ori, guidance=None, n_proposals=1)

    result: dict[str, Any] = {
        "backend": backend_name,
        "label": config["label"],
        "orientation": ori,
        "success": False,
        "json_valid": False,
        "duration_s": 0.0,
        "text": None,
        "scores": None,
        "error": None,
        "compliance_within_1": 0,
        "compliance_total": 0,
    }

    t0 = time.time()
    try:
        raw = backend.complete_json(SYSTEM_MESSAGE, user_msg)
        result["duration_s"] = round(time.time() - t0, 2)
        result["success"] = True
    except LLMBackendError as e:
        result["duration_s"] = round(time.time() - t0, 2)
        result["error"] = str(e)
        return result

    # Vérifier si le JSON est valide
    try:
        parsed = json.loads(raw)
        result["json_valid"] = True
    except json.JSONDecodeError:
        result["json_valid"] = False
        result["error"] = "Invalid JSON"
        return result

    responses = parsed.get("responses", [])
    if not responses:
        result["error"] = "No responses in output"
        return result

    p = responses[0]
    result["text"] = p.get("Text", "")
    generated = p.get("SoftSkillDimensions", {})
    result["scores"] = generated

    # Conformité
    within = 0
    total = 0
    for skill, target in ori.items():
        actual = generated.get(skill, 0)
        try:
            actual = int(actual)
        except (TypeError, ValueError):
            actual = 0
        total += 1
        if abs(actual - target) <= 1:
            within += 1
    result["compliance_within_1"] = within
    result["compliance_total"] = total

    return result


def main():
    print("=== Comparaison OpenAI vs Ollama ===\n")

    repo = ChapterRepository()
    chapters = repo.load_chapters(BOOK_SLUG)

    # Initialiser les backends
    backends: list[tuple[str, Any]] = []

    # OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        backends.append(("openai", OpenAIBackend()))
        print("✓ OpenAI configuré")
    else:
        print("✗ OpenAI non configuré (OPENAI_API_KEY manquant)")

    # Ollama
    try:
        import requests
        r = requests.get("http://localhost:11434/api/tags", timeout=3)
        if r.status_code == 200:
            backends.append(("ollama", OllamaBackend()))
            print("✓ Ollama détecté")
        else:
            print("✗ Ollama non disponible")
    except Exception:
        print("✗ Ollama non disponible (serveur non démarré ?)")

    if not backends:
        print("\nAucun backend disponible. Configurez au moins l'un des deux.")
        sys.exit(1)

    print(f"\nBackends à tester : {[name for name, _ in backends]}")
    print(f"Prompts de test : {len(TEST_CONFIGS)}")
    print("-" * 70)

    all_results: dict[str, list[dict]] = {name: [] for name, _ in backends}

    for cfg_idx, cfg in enumerate(TEST_CONFIGS):
        print(f"\n[{cfg_idx+1}/{len(TEST_CONFIGS)}] {cfg['label']}")
        for backend_name, backend in backends:
            print(f"  → {backend_name}...", end=" ", flush=True)
            result = run_one(backend, backend_name, chapters, cfg)
            all_results[backend_name].append(result)

            if result["error"]:
                print(f"ERREUR: {result['error'][:60]}")
            else:
                compliance = (
                    f"{result['compliance_within_1']}/{result['compliance_total']}"
                    if result["compliance_total"] > 0
                    else "n/a"
                )
                text_preview = (result["text"] or "")[:50]
                print(f"OK ({result['duration_s']:.1f}s) conf={compliance} — {text_preview}...")

    # --- Résumé comparatif ---
    print("\n" + "=" * 70)
    print("RÉSUMÉ COMPARATIF")
    print("=" * 70)
    print(f"{'Critère':<40} ", end="")
    for name, _ in backends:
        print(f"| {name:<20} ", end="")
    print()
    print("-" * (42 + 23 * len(backends)))

    metrics = {}
    for name, _ in backends:
        results = all_results[name]
        n = len(results)
        n_success = sum(1 for r in results if r["success"])
        n_json_valid = sum(1 for r in results if r["json_valid"])
        durations = [r["duration_s"] for r in results if r["success"]]
        avg_duration = sum(durations) / max(1, len(durations))
        total_within = sum(r["compliance_within_1"] for r in results)
        total_targeted = sum(r["compliance_total"] for r in results)
        compliance_pct = round(100 * total_within / max(1, total_targeted), 1)

        metrics[name] = {
            "n": n,
            "success": n_success,
            "json_valid": n_json_valid,
            "avg_duration_s": round(avg_duration, 1),
            "compliance_pct": compliance_pct,
        }

    rows = [
        ("Temps de réponse moyen", lambda m: f"~{m['avg_duration_s']}s"),
        ("JSON valide en sortie", lambda m: f"{m['json_valid']}/{m['n']}"),
        ("Conformité orientation (±1)", lambda m: f"{m['compliance_pct']}%"),
        ("Succès total", lambda m: f"{m['success']}/{m['n']}"),
    ]

    for label, fn in rows:
        print(f"{label:<40} ", end="")
        for name, _ in backends:
            print(f"| {fn(metrics[name]):<20} ", end="")
        print()

    # Sauvegarder
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "eval_backend_comparison.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            {"metrics": metrics, "results": all_results},
            f, ensure_ascii=False, indent=2, default=str,
        )

    print(f"\nRésultats détaillés écrits dans : {output_path}")


if __name__ == "__main__":
    main()
