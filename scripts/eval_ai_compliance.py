#!/usr/bin/env python3
"""
eval_ai_compliance.py — Évalue la conformité du LLM aux orientations soft skills.

Lance N générations avec des profils variés et mesure :
- le taux de conformité ±1 par dimension
- le taux de conformité exacte
- le nombre de doublons filtrés
- le temps de réponse moyen

Usage :
    export OPENAI_API_KEY="sk-..."
    python scripts/eval_ai_compliance.py

    # Ou avec Ollama :
    export ENRICH_BACKEND=ollama
    python scripts/eval_ai_compliance.py

Résultats écrits dans : output/eval_ai_compliance.json + résumé console.
"""
from __future__ import annotations

import json
import os
import sys
import time
from typing import Any

# Ajouter la racine du projet au path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.soft_skills import SOFT_SKILLS, SOFT_SKILL_LABELS
from repositories.chapters import ChapterRepository
from services.enrichment import EnrichmentService, EnrichRequest
from services.enrichment.backends import LLMBackendError

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BOOK_SLUG = "end_of_life"
# Paires (chapter_id, scene_id, interaction_id) à tester
TEST_INTERACTIONS = [
    (1, 1, 1),   # Présentation — "Je suis devant la porte"
    (1, 1, 6),   # Présentation — Agathe détourne le regard
    (1, 1, 13),  # Présentation — "Je veux rentrer chez moi"
    (1, 2, 1),   # Vite fait bien fait — Pascal
    (1, 3, 1),   # Les soins — "Je suis devant la porte"
    (1, 3, 18),  # Les soins — larmes
    (2, 1, 5),   # Lieu de vie — "Mon mari me manque"
    (2, 1, 12),  # Lieu de vie — "Oui et ça me fait peur"
    (3, 1, 1),   # Angoisse dyspnée — regard inquiet
    (3, 1, 15),  # Angoisse — "J'aimerais que vous me fassiez la piqûre"
]

# Profils d'orientation variés à tester
ORIENTATION_PROFILES = [
    {"label": "Très empathique", "Empathy": 3, "Compassion": 2, "RespectAndDignity": 2},
    {"label": "Problématique", "Empathy": -2, "RespectAndDignity": -2, "CommunicationClarity": -1},
    {"label": "Neutre", "Empathy": 0, "Compassion": 0, "RespectAndDignity": 0},
    # Empathique mais franchissant les frontières (cas pédagogique limite)
    {"label": "Empathique mais intrusif", "Empathy": 3, "ProfessionalBoundaries": -2},
    # Communication claire mais froide
    {"label": "Clair mais froid", "CommunicationClarity": 3, "Empathy": -1, "Compassion": -1},
]


def run_single_test(
    service: EnrichmentService,
    chapter_id: int,
    scene_id: int,
    interaction_id: int,
    orientation: dict[str, int],
    label: str,
) -> dict[str, Any]:
    """Lance une génération et mesure la conformité."""
    # Construire l'orientation sans le label
    ori = {k: v for k, v in orientation.items() if k in SOFT_SKILLS}

    req = EnrichRequest(
        book_slug=BOOK_SLUG,
        chapter_id=chapter_id,
        scene_id=scene_id,
        interaction_id=interaction_id,
        orientation=ori,
        n_proposals=1,
    )

    result: dict[str, Any] = {
        "chapter_id": chapter_id,
        "scene_id": scene_id,
        "interaction_id": interaction_id,
        "orientation_label": label,
        "orientation": ori,
        "success": False,
        "error": None,
        "duration_s": 0.0,
        "proposal": None,
        "compliance": {},
        "exact_matches": 0,
        "within_tolerance": 0,
        "total_targeted": 0,
        "was_duplicate": False,
    }

    t0 = time.time()
    try:
        proposals = service.propose_responses(req)
        result["duration_s"] = round(time.time() - t0, 2)

        if not proposals:
            result["was_duplicate"] = True
            result["success"] = True
            return result

        p = proposals[0]
        result["proposal"] = p
        result["success"] = True

        # Évaluer la conformité
        generated_scores = p.get("SoftSkillDimensions", {})
        exact = 0
        within = 0
        total = 0

        compliance = {}
        for skill in SOFT_SKILLS:
            if skill not in ori:
                continue
            total += 1
            target = ori[skill]
            actual = generated_scores.get(skill, 0)
            try:
                actual = int(actual)
            except (TypeError, ValueError):
                actual = 0
            diff = abs(actual - target)
            is_exact = diff == 0
            is_within = diff <= 1
            if is_exact:
                exact += 1
            if is_within:
                within += 1
            compliance[skill] = {
                "target": target,
                "actual": actual,
                "diff": diff,
                "exact": is_exact,
                "within_1": is_within,
            }

        result["compliance"] = compliance
        result["exact_matches"] = exact
        result["within_tolerance"] = within
        result["total_targeted"] = total

    except LLMBackendError as e:
        result["duration_s"] = round(time.time() - t0, 2)
        result["error"] = str(e)
    except Exception as e:
        result["duration_s"] = round(time.time() - t0, 2)
        result["error"] = f"{type(e).__name__}: {e}"

    return result


def main():
    backend_name = os.getenv("ENRICH_BACKEND", "openai")
    print(f"=== Évaluation de la conformité IA (backend: {backend_name}) ===\n")

    repo = ChapterRepository()
    service = EnrichmentService(repository=repo)

    all_results: list[dict[str, Any]] = []
    total_gen = 0
    total_success = 0
    total_duplicates = 0
    total_exact = 0
    total_within = 0
    total_targeted_dims = 0
    total_duration = 0.0
    errors = []

    # Combiner interactions × profils
    tests = []
    for ch_id, sc_id, ia_id in TEST_INTERACTIONS:
        for profile in ORIENTATION_PROFILES:
            tests.append((ch_id, sc_id, ia_id, profile))

    n_tests = len(tests)
    print(f"Nombre de générations prévues : {n_tests}")
    print(f"Interactions testées : {len(TEST_INTERACTIONS)}")
    print(f"Profils d'orientation : {len(ORIENTATION_PROFILES)}")
    print("-" * 70)

    for idx, (ch_id, sc_id, ia_id, profile) in enumerate(tests):
        label = profile.get("label", "?")
        print(f"  [{idx+1}/{n_tests}] Ch{ch_id}/S{sc_id}/I{ia_id} — {label}...", end=" ", flush=True)

        result = run_single_test(service, ch_id, sc_id, ia_id, profile, label)
        all_results.append(result)
        total_gen += 1

        if result["error"]:
            print(f"ERREUR: {result['error'][:80]}")
            errors.append(result["error"])
            continue

        total_success += 1
        total_duration += result["duration_s"]

        if result["was_duplicate"]:
            total_duplicates += 1
            print(f"doublon filtré ({result['duration_s']:.1f}s)")
            continue

        total_exact += result["exact_matches"]
        total_within += result["within_tolerance"]
        total_targeted_dims += result["total_targeted"]

        within_pct = (
            f"{result['within_tolerance']}/{result['total_targeted']}"
            if result["total_targeted"] > 0
            else "n/a"
        )
        print(f"OK — conformité ±1: {within_pct} ({result['duration_s']:.1f}s)")

    # --- Résumé ---
    print("\n" + "=" * 70)
    print("RÉSUMÉ")
    print("=" * 70)
    print(f"Backend                         : {backend_name}")
    print(f"Générations totales             : {total_gen}")
    print(f"Succès                          : {total_success}")
    print(f"Erreurs                         : {len(errors)}")
    print(f"Doublons filtrés                : {total_duplicates}")
    if total_success > 0:
        print(f"Temps de réponse moyen          : {total_duration / total_success:.2f}s")
    if total_targeted_dims > 0:
        exact_pct = round(100 * total_exact / total_targeted_dims, 1)
        within_pct = round(100 * total_within / total_targeted_dims, 1)
        print(f"Dimensions exactement conformes : {total_exact}/{total_targeted_dims} ({exact_pct}%)")
        print(f"Dimensions dans tolérance ±1    : {total_within}/{total_targeted_dims} ({within_pct}%)")

    # Conformité par dimension
    if total_targeted_dims > 0:
        print(f"\nConformité ±1 par dimension :")
        for skill in SOFT_SKILLS:
            skill_total = sum(
                1 for r in all_results
                if skill in r.get("compliance", {})
            )
            skill_within = sum(
                1 for r in all_results
                if r.get("compliance", {}).get(skill, {}).get("within_1", False)
            )
            if skill_total > 0:
                pct = round(100 * skill_within / skill_total, 1)
                label_fr = SOFT_SKILL_LABELS.get(skill, skill)
                print(f"  {label_fr:<40} : {skill_within}/{skill_total} ({pct}%)")

    # Sauvegarder les résultats détaillés
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"eval_ai_compliance_{backend_name}.json")

    summary = {
        "backend": backend_name,
        "total_generations": total_gen,
        "total_success": total_success,
        "total_errors": len(errors),
        "total_duplicates": total_duplicates,
        "avg_duration_s": round(total_duration / max(1, total_success), 2),
        "exact_matches_pct": round(100 * total_exact / max(1, total_targeted_dims), 1),
        "within_tolerance_pct": round(100 * total_within / max(1, total_targeted_dims), 1),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "results": all_results}, f, ensure_ascii=False, indent=2, default=str)

    print(f"\nRésultats détaillés écrits dans : {output_path}")


if __name__ == "__main__":
    main()
