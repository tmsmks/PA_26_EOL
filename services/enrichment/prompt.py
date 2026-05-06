"""Construction du prompt LLM pour l'enrichissement."""
from __future__ import annotations

import json
from typing import Any

from domain.soft_skills import SOFT_SKILL_LABELS, SOFT_SKILLS

SYSTEM_MESSAGE = (
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
    '{ "responses": [ { "Text": ..., "Category": ..., "Rationale": ..., '
    '"SoftSkillDimensions": { ... 7 dimensions ... }, '
    '"LegacyDimensions": { ... } } ] }'
)


def format_user_message(
    context: dict[str, Any],
    orientation: dict[str, int] | None,
    guidance: str | None,
    n_proposals: int,
) -> str:
    """Construit le message utilisateur du prompt."""
    lines: list[str] = [
        f"Nombre de propositions demandées : EXACTEMENT {max(1, int(n_proposals))}.",
    ]

    next_interaction = context.get("next_interaction")
    if next_interaction is not None:
        if next_interaction.get("EndOfBranch") or next_interaction.get("Id") == -1:
            lines += [
                "",
                "SUITE NARRATIVE : la réponse générée est une FIN DE BRANCHE "
                "(aucune interaction ne suit). Elle doit pouvoir clôturer "
                "l'échange de manière cohérente.",
            ]
        else:
            next_actor = (next_interaction.get("Actor") or {}).get("Name", "?")
            next_text = next_interaction.get("Text") or ""
            lines += [
                "",
                "SUITE NARRATIVE (contrainte forte) : la réponse générée doit "
                "mener NATURELLEMENT à l'interaction suivante ci-dessous, "
                "c'est-à-dire provoquer / justifier / enchaîner de façon "
                "crédible la prise de parole qui suit.",
                f"  - Interaction suivante #{next_interaction.get('Id')} "
                f"[{next_actor}] : {next_text}",
                "La réponse proposée NE DOIT PAS répéter ni spoiler ce texte, "
                "mais l'amener logiquement.",
            ]

    if orientation:
        targeted = {
            k: int(v)
            for k, v in orientation.items()
            if k in SOFT_SKILLS and isinstance(v, (int, float))
        }
        if targeted:
            lines += [
                "",
                "ORIENTATION CIBLÉE (priorité forte) — la réponse proposée doit "
                "ILLUSTRER le profil suivant sur l'échelle -3..+3 :",
            ]
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
        lines += ["", "CONSIGNE AUTEUR (à respecter) :", guidance.strip()]

    return (
        "\n".join(lines)
        + "\n\nContexte JSON suivant :\n\n"
        + json.dumps(context, ensure_ascii=False, indent=2)
    )
