#!/usr/bin/env python3
"""
Module d'enrichissement (4.2)
-----------------------------

Objectif : préparer le contexte d'une interaction pour générer de nouvelles
réponses plausibles via un LLM, sans rien modifier automatiquement dans le JSON.

Ce module fournit :
- une fonction d'extraction de contexte : `get_interaction_context`
- un petit utilitaire CLI pour inspecter ce contexte
- des squelettes pour l'appel LLM et le filtrage des doublons
"""
from __future__ import annotations

import argparse
import json
import os
from typing import Any, Dict, List, Tuple

import openai
import requests

from graph_builder import load_chapters


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_PATH = os.path.join(
    BASE_DIR,
    "data",
    "chapters",
    "Chapters_v3-4-c_emotional-illustration.json",
)


def _find_interaction(
    data: Dict[str, Any],
    chapter_id: int,
    scene_id: int,
    interaction_id: int,
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    """
    Retourne (chapter, scene, interaction) pour les Id donnés.
    Lève ValueError si non trouvé.
    """
    for ch in data.get("Chapters", []):
        if ch.get("Id") != chapter_id:
            continue
        for sc in ch.get("Scenes", []):
            if sc.get("Id") != scene_id:
                continue
            for ia in sc.get("Interactions", []):
                if ia.get("Id") == interaction_id:
                    return ch, sc, ia
            raise ValueError(f"Interaction Id={interaction_id} introuvable dans scène {scene_id}.")
        raise ValueError(f"Scène Id={scene_id} introuvable dans chapitre {chapter_id}.")
    raise ValueError(f"Chapitre Id={chapter_id} introuvable.")


def get_interaction_context(
    json_path: str,
    chapter_id: int,
    scene_id: int,
    interaction_id: int,
) -> Dict[str, Any]:
    """
    Construit le "contexte enrichissement" tel que défini en 4.2 :

    - SceneIntroduction
    - Title (de la scène)
    - Interaction (Texte + Name)
    - Profil acteur (Actor)
    - Réponses existantes (texte + scores si présents)
    """
    data = load_chapters(json_path)
    chapter, scene, interaction = _find_interaction(
        data, chapter_id, scene_id, interaction_id
    )

    scene_intro = scene.get("SceneIntroduction") or ""
    scene_title = scene.get("Title") or ""

    actor = (interaction.get("Actor") or {}).copy()
    ia_text = interaction.get("Text") or ""
    ia_name = interaction.get("Name") or ""

    existing_responses: List[Dict[str, Any]] = []
    for r in interaction.get("Responses", []):
        existing_responses.append(
            {
                "Id": r.get("Id"),
                "Name": r.get("Name"),
                "Text": r.get("Text"),
                # Soft skills (v3 / v3-4)
                "SoftSkillDimensions": r.get("SoftSkillDimensions", {}),
                # Legacy dimensions (Authenticity, Respect, Compassion, Hope, Empathy)
                "LegacyDimensions": r.get("LegacyDimensions", {}),
                "NextInteractionID": r.get("NextInteractionID"),
            }
        )

    return {
        "chapter": {
            "Id": chapter.get("Id"),
            "Name": chapter.get("Name"),
        },
        "scene": {
            "Id": scene.get("Id"),
            "Title": scene_title,
            "SceneIntroduction": scene_intro,
            "Min": scene.get("Min"),
        },
        "interaction": {
            "Id": interaction.get("Id"),
            "Name": ia_name,
            "Text": ia_text,
            "Actor": actor,
        },
        "existing_responses": existing_responses,
    }


def filter_duplicate_texts(
    candidates: List[Dict[str, Any]],
    existing_responses: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Supprime les réponses candidates dont le texte duplique (quasi) une réponse existante.
    Règle 4.2 : « pas de duplication des réponses existantes ».
    """
    seen = {
        (r.get("Text") or "").strip().lower()
        for r in existing_responses
        if (r.get("Text") or "").strip()
    }

    filtered: List[Dict[str, Any]] = []
    for c in candidates:
        txt = (c.get("Text") or "").strip()
        if not txt:
            continue
        if txt.lower() in seen:
            continue
        filtered.append(c)
    return filtered


def call_llm_for_enrichment(context: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Appelle un LLM réel pour proposer de nouvelles réponses.

    Backend sélectionné par ENRICH_BACKEND :
    - \"openai\" (par défaut) : API OpenAI officielle
    - \"ollama\"           : serveur local Ollama (compat. /v1/chat/completions)

    OpenAI :
    - Lit la clé dans OPENAI_API_KEY.
    - Utilise par défaut le modèle ENRICH_OPENAI_MODEL ou 'gpt-4.1-mini'.
    Ollama :
    - Utilise ENRICH_OLLAMA_MODEL (par défaut 'llama3.1:8b').
    - Suppose un serveur local sur http://localhost:11434.
    - Retourne une liste de réponses déjà filtrées pour éviter les doublons.
    """
    backend = os.getenv("ENRICH_BACKEND", "openai").lower()
    system_msg = (
        "Tu es un assistant pédagogique spécialisé en communication en fin de vie.\n"
        "On te fournit le contexte complet d'une scène de simulation (EMS), "
        "une interaction précise et la liste des réponses déjà existantes.\n\n"
        "Ta tâche : proposer de 1 à 3 nouvelles réponses plausibles que l'ACTEUR pourrait dire.\n"
        "Contraintes :\n"
        "- respecter la déontologie infirmière et les bonnes pratiques relationnelles ;\n"
        "- ne JAMAIS dupliquer les réponses déjà existantes (même sens, même tournure) ;\n"
        "- proposer pour chaque réponse :\n"
        "  - le texte exact de la réplique (en français) ;\n"
        "  - une catégorie parmi : 'exemplaire', 'neutre', 'problématique' ;\n"
        "  - des scores soft skills au format SoftSkillDimensions (RespectAndDignity, Empathy, etc.) ;\n"
        "  - des scores LegacyDimensions (Authenticity, Respect, Compassion, Hope, Empathy), chacun de -3 à +3.\n\n"
        "Réponds STRICTEMENT en JSON de la forme :\n"
        "{ \"responses\": [ { \"Text\": ..., \"Category\": ..., "
        "\"SoftSkillDimensions\": { ... }, \"LegacyDimensions\": { ... } } ] }"
    )

    user_msg = "Contexte JSON suivant :\n\n" + json.dumps(
        context, ensure_ascii=False, indent=2
    )

    if backend == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ENRICH_BACKEND=openai mais OPENAI_API_KEY est manquant. "
                "Définissez la variable d'environnement avec votre clé OpenAI."
            )
        model = os.getenv("ENRICH_OPENAI_MODEL", "gpt-4.1-mini")
        client = openai.OpenAI(api_key=api_key)
        try:
            completion = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
            )
        except openai.RateLimitError as exc:
            raise RuntimeError(
                "Erreur de quota OpenAI (RateLimitError). "
                "Vérifiez votre plan / crédits ou utilisez ENRICH_BACKEND=ollama."
            ) from exc
        content = completion.choices[0].message.content or "{}"

    elif backend == "ollama":
        model = os.getenv("ENRICH_OLLAMA_MODEL", "llama3.1:8b")
        url = os.getenv("ENRICH_OLLAMA_URL", "http://localhost:11434/v1/chat/completions")
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            "response_format": {"type": "json_object"},
        }
        try:
            resp = requests.post(url, json=payload, timeout=60)
        except requests.RequestException as exc:
            raise RuntimeError(
                f"Impossible de joindre Ollama sur {url}. "
                "Assurez-vous que 'ollama serve' est démarré."
            ) from exc
        if resp.status_code != 200:
            raise RuntimeError(
                f"Erreur Ollama {resp.status_code}: {resp.text[:400]}"
            )
        data = resp.json()
        content = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "{}")
        )
    else:
        raise RuntimeError(
            f"ENRICH_BACKEND='{backend}' inconnu. Utilisez 'openai' ou 'ollama'."
        )

    try:
        parsed = json.loads(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Réponse LLM non valide (JSON) : {exc}") from exc

    raw_candidates = parsed.get("responses") or []
    if not isinstance(raw_candidates, list):
        raise RuntimeError("Format LLM inattendu : 'responses' doit être une liste.")

    return filter_duplicate_texts(raw_candidates, context.get("existing_responses", []))


def propose_new_responses_stub(context: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Stub : à remplacer par un appel LLM réel.

    Retour attendu par le module d'enrichissement (4.2) pour CHAQUE nouvelle réponse :
    - Text (str)
    - Category (\"exemplaire\" | \"neutre\" | \"problématique\")
    - SoftSkillDimensions : dictionnaire de scores
    - LegacyDimensions : dictionnaire de scores
    """
    # Exemple minimal purement illustratif. Ne doit PAS être utilisé en production.
    dummy = [
        {
            "Text": "« Je vous entends, voulez-vous m'en dire un peu plus ? »",
            "Category": "exemplaire",
            "SoftSkillDimensions": {
                "RespectAndDignity": 2,
                "Empathy": 2,
                "Compassion": 2,
                "EmotionalRegulation": 1,
                "CommunicationClarity": 1,
                "ProfessionalBoundaries": 1,
                "InterprofessionalCollaboration": 0,
            },
            "LegacyDimensions": {
                "Authenticity": 2,
                "Respect": 2,
                "Compassion": 2,
                "Hope": 1,
                "Empathy": 2,
            },
        }
    ]

    return filter_duplicate_texts(dummy, context.get("existing_responses", []))


def _cli() -> None:
    parser = argparse.ArgumentParser(
        description="Inspecter le contexte d'une interaction pour le module d'enrichissement (4.2)."
    )
    parser.add_argument("--json", default=CHAPTERS_PATH, help="Chemin du fichier Chapters JSON.")
    parser.add_argument("--chapter", type=int, required=True, help="Id du chapitre.")
    parser.add_argument("--scene", type=int, required=True, help="Id de la scène.")
    parser.add_argument("--interaction", type=int, required=True, help="Id de l'interaction.")
    parser.add_argument(
        "--with-stub",
        action="store_true",
        help="Ajoute une proposition de nouvelles réponses (stub, sans LLM réel).",
    )
    parser.add_argument(
        "--with-llm",
        action="store_true",
        help="Appelle le LLM OpenAI réel pour proposer de nouvelles réponses.",
    )
    args = parser.parse_args()

    ctx = get_interaction_context(
        json_path=args.json,
        chapter_id=args.chapter,
        scene_id=args.scene,
        interaction_id=args.interaction,
    )

    out: Dict[str, Any] = {"context": ctx}
    if args.with_stub:
        out["proposed_responses_stub"] = propose_new_responses_stub(ctx)
    if args.with_llm:
        out["proposed_responses_llm"] = call_llm_for_enrichment(ctx)

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    _cli()

