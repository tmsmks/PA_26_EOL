#!/usr/bin/env python3
"""
eval_scoring_mae.py — Compare le scoring IA aux scores manuels existants.

Prend des réponses dont les scores ont été fixés par les auteurs, les soumet
au LLM pour scoring, puis calcule l'écart moyen absolu (MAE) par dimension.

Usage :
    export OPENAI_API_KEY="sk-..."
    python scripts/eval_scoring_mae.py

Résultats écrits dans : output/eval_scoring_mae.json + résumé console.
"""
from __future__ import annotations

import json
import os
import sys
import time
from typing import Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.models import Chapter
from domain.soft_skills import SOFT_SKILLS, SOFT_SKILL_LABELS
from repositories.chapters import ChapterRepository
from services.enrichment.backends import resolve_backend, LLMBackendError
from services.enrichment.context import build_context
from services.enrichment.prompt import SYSTEM_MESSAGE

BOOK_SLUG = "end_of_life"

# On va évaluer le scoring sur ces réponses (chapter, scene, interaction, response_idx)
# Choisies pour leur diversité : exemplaires, neutres, problématiques
RESPONSES_TO_SCORE = [
    # Chapitre 1 — Présentation
    (1, 1, 1, 0),   # "Je frappe puis j'entre"
    (1, 1, 1, 1),   # "J'entre sans frapper"
    (1, 1, 1, 2),   # "Je frappe doucement"
    (1, 1, 6, 0),   # s'assied auprès d'Agathe
    (1, 1, 6, 1),   # "Je suis vraiment..."
    (1, 1, 13, 0),  # "Je veux rentrer chez moi"
    (1, 1, 13, 2),  # "Et bien moi aussi"
    # Chapitre 1 — Vite fait bien fait
    (1, 2, 1, 0),   # "Que se passe-t-il Pascal"
    (1, 2, 1, 3),   # "Travailler rapidement"
    # Chapitre 1 — Les soins
    (1, 3, 5, 0),   # "Je perçois Agathe comme..."
    (1, 3, 5, 3),   # "Je refuse qu'elle..."
    (1, 3, 18, 0),  # "Il compte beaucoup pour vous"
    (1, 3, 18, 2),  # "Pleurez, allez-y"
    # Chapitre 2
    (2, 1, 5, 0),   # "Je la regarde"
    (2, 1, 5, 1),   # "J'ai encore de beaux jours"
]

SCORING_SYSTEM_MSG = (
    "Tu es un expert en évaluation des compétences relationnelles en soins palliatifs.\n"
    "On te fournit le contexte d'une scène de simulation et UNE réponse spécifique.\n\n"
    "Ta tâche : attribuer un score sur chacune des 7 dimensions soft skills, de -3 à +3,\n"
    "et fournir une justification courte.\n\n"
    "Dimensions : RespectAndDignity, Empathy, Compassion, EmotionalRegulation,\n"
    "CommunicationClarity, ProfessionalBoundaries, InterprofessionalCollaboration.\n\n"
    "Réponds STRICTEMENT en JSON :\n"
    '{ "SoftSkillDimensions": { ... les 7 dimensions ... }, "Rationale": "..." }'
)


def score_one_response(
    backend,
    chapters: list[Chapter],
    ch_id: int,
    sc_id: int,
    ia_id: int,
    r_idx: int,
) -> dict[str, Any]:
    """Envoie une réponse existante au LLM pour scoring et retourne le résultat."""
    # Trouver la réponse
    chapter = next((c for c in chapters if c.Id == ch_id), None)
    if not chapter:
        return {"error": f"Chapter {ch_id} not found"}
    scene = next((s for s in chapter.Scenes if s.Id == sc_id), None)
    if not scene:
        return {"error": f"Scene {sc_id} not found"}
    interaction = next((i for i in scene.Interactions if i.Id == ia_id), None)
    if not interaction:
        return {"error": f"Interaction {ia_id} not found"}
    if r_idx >= len(interaction.Responses):
        return {"error": f"Response index {r_idx} out of range"}

    response = interaction.Responses[r_idx]

    # Scores humains existants
    human_scores = {}
    for skill in SOFT_SKILLS:
        v = (response.SoftSkillDimensions or {}).get(skill)
        if v is None:
            v = response._extra.get(skill, 0)
        try:
            human_scores[skill] = int(v)
        except (TypeError, ValueError):
            human_scores[skill] = 0

    # Construire le contexte
    ctx = build_context(chapters, ch_id, sc_id, ia_id)

    user_msg = (
        f"Voici le contexte de la scène et de l'interaction :\n\n"
        f"{json.dumps(ctx, ensure_ascii=False, indent=2)}\n\n"
        f"Réponse à évaluer (réponse #{r_idx + 1}) :\n"
        f"Texte : {response.Text}\n\n"
        f"Attribue un score -3 à +3 pour chaque dimension et justifie."
    )

    t0 = time.time()
    try:
        raw = backend.complete_json(SCORING_SYSTEM_MSG, user_msg)
        duration = round(time.time() - t0, 2)
        parsed = json.loads(raw)
    except (LLMBackendError, json.JSONDecodeError) as e:
        return {
            "error": str(e),
            "duration_s": round(time.time() - t0, 2),
            "response_text": response.Text,
            "human_scores": human_scores,
        }

    ai_scores = parsed.get("SoftSkillDimensions", {})
    rationale = parsed.get("Rationale", "")

    # Normaliser les scores IA
    ai_scores_clean = {}
    for skill in SOFT_SKILLS:
        v = ai_scores.get(skill, 0)
        try:
            v = max(-3, min(3, int(v)))
        except (TypeError, ValueError):
            v = 0
        ai_scores_clean[skill] = v

    # Calculer les écarts
    diffs = {}
    for skill in SOFT_SKILLS:
        h = human_scores.get(skill, 0)
        a = ai_scores_clean.get(skill, 0)
        diffs[skill] = {
            "human": h,
            "ai": a,
            "abs_error": abs(h - a),
        }

    return {
        "chapter_id": ch_id,
        "scene_id": sc_id,
        "interaction_id": ia_id,
        "response_idx": r_idx,
        "response_text": response.Text[:120],
        "human_scores": human_scores,
        "ai_scores": ai_scores_clean,
        "rationale": rationale,
        "diffs": diffs,
        "duration_s": duration,
        "error": None,
    }


def main():
    backend_name = os.getenv("ENRICH_BACKEND", "openai")
    print(f"=== Évaluation du scoring IA vs scores manuels (backend: {backend_name}) ===\n")

    repo = ChapterRepository()
    chapters = repo.load_chapters(BOOK_SLUG)
    backend = resolve_backend(backend_name)

    all_results: list[dict[str, Any]] = []
    n_tests = len(RESPONSES_TO_SCORE)

    # Accumulateurs pour MAE par dimension
    abs_errors_by_skill: dict[str, list[int]] = {sk: [] for sk in SOFT_SKILLS}
    total_duration = 0.0
    n_success = 0

    for idx, (ch_id, sc_id, ia_id, r_idx) in enumerate(RESPONSES_TO_SCORE):
        print(f"  [{idx+1}/{n_tests}] Ch{ch_id}/S{sc_id}/I{ia_id}/R{r_idx}...", end=" ", flush=True)

        result = score_one_response(backend, chapters, ch_id, sc_id, ia_id, r_idx)
        all_results.append(result)

        if result.get("error"):
            print(f"ERREUR: {result['error'][:80]}")
            continue

        n_success += 1
        total_duration += result["duration_s"]

        # Accumuler les erreurs absolues
        for skill in SOFT_SKILLS:
            ae = result["diffs"][skill]["abs_error"]
            abs_errors_by_skill[skill].append(ae)

        # Afficher un résumé
        mae_this = sum(
            result["diffs"][sk]["abs_error"] for sk in SOFT_SKILLS
        ) / len(SOFT_SKILLS)
        print(f"MAE={mae_this:.2f} ({result['duration_s']:.1f}s) — {result['response_text'][:50]}...")

    # --- Résumé ---
    print("\n" + "=" * 70)
    print("RÉSUMÉ — MAE par dimension")
    print("=" * 70)
    print(f"Backend                  : {backend_name}")
    print(f"Réponses évaluées        : {n_success}/{n_tests}")
    if n_success > 0:
        print(f"Temps de réponse moyen   : {total_duration / n_success:.2f}s")
    print()

    mae_by_skill = {}
    for skill in SOFT_SKILLS:
        errs = abs_errors_by_skill[skill]
        if errs:
            mae = sum(errs) / len(errs)
        else:
            mae = 0.0
        mae_by_skill[skill] = round(mae, 2)
        label_fr = SOFT_SKILL_LABELS.get(skill, skill)
        print(f"  {label_fr:<40} : MAE = {mae:.2f}")

    global_mae = sum(mae_by_skill.values()) / len(SOFT_SKILLS)
    print(f"\n  {'MOYENNE GLOBALE':<40} : MAE = {global_mae:.2f}")

    # Sauvegarder
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"eval_scoring_mae_{backend_name}.json")

    summary = {
        "backend": backend_name,
        "n_success": n_success,
        "n_total": n_tests,
        "avg_duration_s": round(total_duration / max(1, n_success), 2),
        "mae_by_skill": mae_by_skill,
        "global_mae": round(global_mae, 2),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "results": all_results}, f, ensure_ascii=False, indent=2, default=str)

    print(f"\nRésultats détaillés écrits dans : {output_path}")


if __name__ == "__main__":
    main()
