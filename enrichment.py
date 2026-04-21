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

SOFT_SKILLS = [
    "RespectAndDignity",
    "Empathy",
    "Compassion",
    "EmotionalRegulation",
    "CommunicationClarity",
    "ProfessionalBoundaries",
    "InterprofessionalCollaboration",
]

SOFT_SKILL_LABELS = {
    "RespectAndDignity": "Respect et dignité",
    "Empathy": "Empathie",
    "Compassion": "Compassion",
    "EmotionalRegulation": "Régulation émotionnelle",
    "CommunicationClarity": "Clarté de communication",
    "ProfessionalBoundaries": "Frontières professionnelles",
    "InterprofessionalCollaboration": "Collaboration interprofessionnelle",
}


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
    next_interaction_id: int | None = None,
) -> Dict[str, Any]:
    """
    Construit le "contexte enrichissement" tel que défini en 4.2 :

    - SceneIntroduction
    - Title (de la scène)
    - Interaction (Texte + Name)
    - Profil acteur (Actor)
    - Réponses existantes (texte + scores si présents)

    Si next_interaction_id est fourni (et différent de -1), ajoute un bloc
    `next_interaction` décrivant l'interaction suivante vers laquelle la
    réponse générée doit naturellement mener.
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

    next_interaction_block: Dict[str, Any] | None = None
    if next_interaction_id is not None and int(next_interaction_id) != -1:
        for ia in scene.get("Interactions", []):
            if ia.get("Id") == int(next_interaction_id):
                next_interaction_block = {
                    "Id": ia.get("Id"),
                    "Name": ia.get("Name"),
                    "Text": ia.get("Text"),
                    "Actor": (ia.get("Actor") or {}).copy(),
                }
                break

    result: Dict[str, Any] = {
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
    if next_interaction_block is not None:
        result["next_interaction"] = next_interaction_block
    elif next_interaction_id is not None and int(next_interaction_id) == -1:
        result["next_interaction"] = {"Id": -1, "EndOfBranch": True}
    return result


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


def _format_orientation_instructions(
    orientation: Dict[str, int] | None,
    guidance: str | None,
    n_proposals: int,
    next_interaction: Dict[str, Any] | None = None,
) -> str:
    """
    Formate l'orientation soft skills + consigne libre + bloc suivant
    en instructions pour le LLM.

    orientation      : {skill: target_score (-3..+3)} — partiel autorisé.
    guidance         : texte libre (ex : "ton plus direct, moins paternaliste").
    next_interaction : bloc vers lequel la réponse doit mener (ou {Id:-1} pour fin).
    """
    lines: List[str] = []
    lines.append(
        f"Nombre de propositions demandées : EXACTEMENT {max(1, int(n_proposals))}."
    )

    if next_interaction is not None:
        if next_interaction.get("EndOfBranch") or next_interaction.get("Id") == -1:
            lines.append("")
            lines.append(
                "SUITE NARRATIVE : la réponse générée est une FIN DE BRANCHE "
                "(aucune interaction ne suit). Elle doit pouvoir clôturer "
                "l'échange de manière cohérente."
            )
        else:
            next_actor = (next_interaction.get("Actor") or {}).get("Name", "?")
            next_text = next_interaction.get("Text") or ""
            lines.append("")
            lines.append(
                "SUITE NARRATIVE (contrainte forte) : la réponse générée doit "
                "mener NATURELLEMENT à l'interaction suivante ci-dessous, "
                "c'est-à-dire provoquer / justifier / enchaîner de façon "
                "crédible la prise de parole qui suit."
            )
            lines.append(
                f"  - Interaction suivante #{next_interaction.get('Id')} "
                f"[{next_actor}] : {next_text}"
            )
            lines.append(
                "La réponse proposée NE DOIT PAS répéter ni spoiler ce texte, "
                "mais l'amener logiquement."
            )

    if orientation:
        targeted = {
            k: int(v)
            for k, v in orientation.items()
            if k in SOFT_SKILLS and isinstance(v, (int, float))
        }
        if targeted:
            lines.append("")
            lines.append(
                "ORIENTATION CIBLÉE (priorité forte) — la réponse proposée doit "
                "ILLUSTRER le profil suivant sur l'échelle -3..+3 :"
            )
            for skill in SOFT_SKILLS:
                if skill in targeted:
                    v = max(-3, min(3, targeted[skill]))
                    sign = "+" if v > 0 else ""
                    label = SOFT_SKILL_LABELS.get(skill, skill)
                    lines.append(f"  - {skill} ({label}) : cible = {sign}{v}")
            lines.append(
                "Les scores SoftSkillDimensions renvoyés DOIVENT correspondre "
                "à ce profil (tolérance ±1 par dimension). Le texte de la "
                "réplique doit concrètement traduire ces orientations."
            )

    if guidance and guidance.strip():
        lines.append("")
        lines.append("CONSIGNE AUTEUR (à respecter) :")
        lines.append(guidance.strip())

    return "\n".join(lines)


def call_llm_for_enrichment(
    context: Dict[str, Any],
    orientation: Dict[str, int] | None = None,
    guidance: str | None = None,
    n_proposals: int = 1,
    next_interaction: Dict[str, Any] | None = None,
) -> List[Dict[str, Any]]:
    """
    Appelle un LLM réel pour proposer de nouvelles réponses.

    Backend sélectionné par ENRICH_BACKEND :
    - \"openai\" (par défaut) : API OpenAI officielle
    - \"ollama\"           : serveur local Ollama (compat. /v1/chat/completions)

    Paramètres :
    - orientation : dict partiel {skill: score -3..+3} pour guider le profil
      soft skills de la réponse générée.
    - guidance    : texte libre d'instructions auteur.
    - n_proposals : nombre de propositions demandées (1 à 3).
    """
    backend = os.getenv("ENRICH_BACKEND", "openai").lower()
    system_msg = (
        "Tu es un assistant pédagogique spécialisé en communication en fin de vie.\n"
        "On te fournit le contexte complet d'une scène de simulation (EMS), "
        "une interaction précise et la liste des réponses déjà existantes.\n\n"
        "Ta tâche : proposer de nouvelles réponses plausibles que l'ACTEUR pourrait dire.\n"
        "Contraintes :\n"
        "- respecter la déontologie infirmière et les bonnes pratiques relationnelles ;\n"
        "- ne JAMAIS dupliquer les réponses déjà existantes (même sens, même tournure) ;\n"
        "- proposer pour chaque réponse :\n"
        "  - le texte exact de la réplique (en français, entre guillemets français « » si citation directe) ;\n"
        "  - une catégorie parmi : 'exemplaire', 'neutre', 'problématique' ;\n"
        "  - des scores SoftSkillDimensions OBLIGATOIRES couvrant les 7 dimensions :\n"
        "    RespectAndDignity, Empathy, Compassion, EmotionalRegulation, "
        "CommunicationClarity, ProfessionalBoundaries, InterprofessionalCollaboration ;\n"
        "    chaque score est un entier de -3 à +3 ;\n"
        "  - des scores LegacyDimensions (Authenticity, Respect, Compassion, Hope, Empathy), chacun de -3 à +3 ;\n"
        "  - un champ Rationale (1–2 phrases) justifiant brièvement le choix et les scores.\n\n"
        "Réponds STRICTEMENT en JSON de la forme :\n"
        "{ \"responses\": [ { \"Text\": ..., \"Category\": ..., \"Rationale\": ..., "
        "\"SoftSkillDimensions\": { ... 7 dimensions ... }, "
        "\"LegacyDimensions\": { ... } } ] }"
    )

    if next_interaction is None:
        next_interaction = context.get("next_interaction")
    orientation_block = _format_orientation_instructions(
        orientation, guidance, n_proposals, next_interaction=next_interaction
    )

    user_msg = (
        orientation_block
        + "\n\nContexte JSON suivant :\n\n"
        + json.dumps(context, ensure_ascii=False, indent=2)
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
        try:
            timeout_s = float(os.getenv("ENRICH_OLLAMA_TIMEOUT", "300"))
        except ValueError:
            timeout_s = 300.0
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            "response_format": {"type": "json_object"},
        }
        try:
            resp = requests.post(url, json=payload, timeout=timeout_s)
        except requests.Timeout as exc:
            raise RuntimeError(
                f"Ollama a dépassé le timeout de {int(timeout_s)}s sur {url}. "
                "Le premier appel peut être long (chargement du modèle). "
                "Essayez de précharger le modèle avec `ollama run <modèle> ''` "
                "ou augmentez ENRICH_OLLAMA_TIMEOUT."
            ) from exc
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
    parser.add_argument(
        "--n",
        type=int,
        default=1,
        help="Nombre de propositions à demander au LLM (1 à 3).",
    )
    parser.add_argument(
        "--guidance",
        type=str,
        default=None,
        help="Consigne libre auteur (ex: 'ton plus direct').",
    )
    parser.add_argument(
        "--next-id",
        type=int,
        default=None,
        help="Id de l'interaction suivante vers laquelle la réponse doit mener (-1 = fin).",
    )
    for skill in SOFT_SKILLS:
        parser.add_argument(
            f"--{skill}",
            type=int,
            default=None,
            help=f"Score cible -3..+3 pour la dimension {skill}.",
        )
    args = parser.parse_args()

    orientation = {
        skill: getattr(args, skill)
        for skill in SOFT_SKILLS
        if getattr(args, skill) is not None
    }

    ctx = get_interaction_context(
        json_path=args.json,
        chapter_id=args.chapter,
        scene_id=args.scene,
        interaction_id=args.interaction,
        next_interaction_id=args.next_id,
    )

    out: Dict[str, Any] = {"context": ctx}
    if args.with_stub:
        out["proposed_responses_stub"] = propose_new_responses_stub(ctx)
    if args.with_llm:
        out["proposed_responses_llm"] = call_llm_for_enrichment(
            ctx,
            orientation=orientation or None,
            guidance=args.guidance,
            n_proposals=args.n,
        )

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    _cli()

