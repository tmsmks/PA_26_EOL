"""Grille de cotation ancrée des réponses (brouillon, à valider par le panel d'experts).

Pour chaque compétence : ce que valent −3, 0 et +3, avec ses ancrages dans les
cadres de référence (docs/Scoring_v2_recherche_et_plan.md, § 2.3 et § 3.1) :
- PROFILES, cadre suisse des objectifs de formation médicale, adapté de
  CanMEDS (Michaud & Jucker-Kupper 2016) ;
- éléments essentiels de la communication de Kalamazoo (Makoul 2001) ;
- guide Calgary-Cambridge de l'entretien médical (Kurtz et al. 2003).
Les valeurs intermédiaires (−2, −1, +1, +2) graduent entre ces ancres.
"""
from __future__ import annotations

from typing import Final

RUBRIC_STATUS: Final[str] = "Brouillon du 06.10.2026, à valider par le panel d'experts."

# (compétence, ancrage, −3, 0, +3)
RUBRIC: Final[dict[str, dict[str, str]]] = {
    "RespectAndDignity": {
        "anchor": "PROFILES : rôle de professionnel ; Kalamazoo : construire la relation.",
        "-3": "Réduit la personne (vivante ou décédée) à un objet ou à un cas : l'expose (image, "
              "nom, détail identifiant), l'humilie, parle d'elle devant elle sans elle.",
        "0": "Neutre, ou la dignité de la personne n'est pas en jeu dans cette réponse.",
        "+3": "Traite la personne comme un sujet : demande son accord, préserve sa pudeur, son "
              "intimité et son anonymat, respecte sa volonté, même quand elle dérange.",
    },
    "Empathy": {
        "anchor": "Kalamazoo : comprendre la perspective du patient ; Calgary-Cambridge : "
                  "construire la relation.",
        "-3": "Ignore, minimise ou disqualifie l'émotion ou la préoccupation (« ce n'est rien », "
              "« calmez-vous »), coupe la parole, impose son point de vue.",
        "0": "Neutre, ou aucune émotion ni préoccupation n'est exprimée à ce moment.",
        "+3": "Repère et nomme l'émotion ou la préoccupation, vérifie qu'il ou elle a bien "
              "compris, laisse la place au silence et à la parole de l'autre.",
    },
    "Compassion": {
        "anchor": "PROFILES : rôle de professionnel (attitude envers la souffrance).",
        "-3": "Indifférence ou abandon face à une souffrance ; froideur délibérée ; se met "
              "au centre au lieu de la personne qui souffre.",
        "0": "Neutre, ou aucune souffrance n'est en jeu à ce moment.",
        "+3": "Agit pour soulager, au bon moment et sans se mettre au centre : présence, "
              "geste, aide concrète, orientation vers un soutien.",
    },
    "EmotionalRegulation": {
        "anchor": "PROFILES : rôle de professionnel (gestion de soi) ; enseignement "
                  "interprofessionnel (facteurs humains).",
        "-3": "Se laisse submerger (panique, colère, fuite, rire déplacé, culpabilité qui "
              "paralyse) au détriment de la personne ou de la tâche.",
        "0": "Neutre, ou la situation ne sollicite pas ses émotions.",
        "+3": "Reconnaît ses propres émotions, garde une conduite adaptée, et demande du "
              "soutien ou passe le relais quand il le faut.",
    },
    "CommunicationClarity": {
        "anchor": "Calgary-Cambridge : expliquer et planifier ; Kalamazoo : partager "
                  "l'information ; communication en boucle fermée en urgence.",
        "-3": "Information fausse, confuse ou jargonneuse ; ou donne une information qu'il ou "
              "elle ne doit pas donner (résultat, pronostic) hors de tout cadre.",
        "0": "Neutre, ou aucune information n'est à transmettre à ce moment.",
        "+3": "Message juste, simple, adapté à l'interlocuteur ; vérifie la compréhension ; "
              "en urgence, message clair, répété et confirmé.",
    },
    "ProfessionalBoundaries": {
        "anchor": "PROFILES : rôle de professionnel ; secret professionnel (art. 321 CP, qui "
                  "vise aussi les étudiant·e·s) ; limites du rôle d'étudiant·e.",
        "-3": "Sort de son rôle d'une manière qui expose le patient ou un tiers : viole le "
              "secret, décide à la place du médecin, fait une promesse intenable, noue une "
              "relation personnelle (numéro privé), ment à l'institution.",
        "0": "Neutre, ou les limites du rôle ne sont pas en jeu à ce moment.",
        "+3": "Reste dans son rôle d'étudiant·e, respecte le secret et la loi, oriente vers "
              "la bonne personne au bon moment.",
    },
    "InterprofessionalCollaboration": {
        "anchor": "PROFILES : rôle de collaborateur ; CanMEDS « Collaborator ».",
        "-3": "Agit seul·e quand il faut appeler ; méprise, court-circuite ou accuse un·e "
              "collègue (assistante, infirmier·ère, physiothérapeute…).",
        "0": "Neutre, ou aucun autre professionnel n'est concerné à ce moment.",
        "+3": "Sollicite et reconnaît l'expertise des autres professionnel·le·s, transmet "
              "de façon structurée, partage la charge au lieu de la porter seul·e.",
    },
}

CRITICAL_DEFINITION: Final[str] = (
    "Une réponse est « critique » si elle met en danger le patient ou un tiers, ou si elle "
    "viole la loi ou une règle déontologique essentielle, quelle que soit sa politesse : "
    "violer le secret médical, ne pas appeler le 144 devant une urgence vitale, ne pas poser "
    "la question du suicide à une personne qui l'évoque, décider à la place du patient. Une "
    "erreur critique ne se compense pas par de bonnes réponses ailleurs (règle non "
    "compensatoire, Homer & Russell 2021)."
)
