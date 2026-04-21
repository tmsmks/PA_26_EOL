#!/usr/bin/env python3
"""
Génère MedStudents_Y2_v1.json — un "livre" de scénarios pédagogiques destiné
aux étudiant·e·s en 2e année de médecine.

Même schéma que Chapters_v3-4-c_emotional-illustration.json :
    Chapters > Scenes > Interactions > Responses
avec SoftSkillDimensions (7) + LegacyDimensions (5), scores -3..+3.

Le joueur incarne Alex, étudiant·e en 2e année de médecine en stage
d'immersion. Les chapitres ciblent des compétences communicationnelles
et éthiques fondamentales du cursus pré-clinique.
"""
from __future__ import annotations

import json
import os
from copy import deepcopy
from typing import Any, Dict, List

SOFT_KEYS = [
    "RespectAndDignity",
    "Empathy",
    "Compassion",
    "EmotionalRegulation",
    "CommunicationClarity",
    "ProfessionalBoundaries",
    "InterprofessionalCollaboration",
]
LEGACY_KEYS = ["Authenticity", "Respect", "Compassion", "Hope", "Empathy"]


# ---------------------------------------------------------------------------
# Acteurs réutilisables
# ---------------------------------------------------------------------------
ALEX = {
    "Id": 10,
    "Name": "Alex",
    "Age": 21,
    "Role": "Étudiant·e en 2e année de médecine",
    "History": (
        "Alex est en 2e année de médecine et effectue son premier stage "
        "d'immersion hospitalière. Passionné·e par la relation médecin-patient, "
        "il/elle a suivi les cours de sémiologie, d'éthique et de communication. "
        "Alex est motivé·e mais manque encore d'expérience clinique et craint "
        "de ne pas être à la hauteur face aux patients."
    ),
    "ImageName": "Alex.png",
}

DR_MOREAU = {
    "Id": 11,
    "Name": "Dr Moreau",
    "Age": 42,
    "Role": "Médecin-chef, service de médecine interne",
    "History": (
        "Médecin interniste depuis 15 ans, pédagogue reconnu·e. Dr Moreau "
        "encadre les étudiants en stage avec bienveillance mais exige rigueur "
        "et respect des règles déontologiques. Aime les questions pertinentes "
        "et valorise l'humilité professionnelle."
    ),
    "ImageName": "DrMoreau.png",
}

M_BERNARD = {
    "Id": 12,
    "Name": "Monsieur Bernard",
    "Age": 62,
    "Role": "Patient hospitalisé — hypertension, douleur thoracique investiguée",
    "History": (
        "Ancien chauffeur routier, retraité depuis 3 ans. Hypertension connue "
        "depuis 10 ans, sous bithérapie. Hospitalisé pour exploration d'une "
        "douleur thoracique apparue la veille. Anxieux mais discret, peu "
        "habitué à parler de ses émotions. Vit seul depuis son divorce, a "
        "deux enfants adultes qu'il voit peu."
    ),
    "ImageName": "MBernard.png",
}

MME_COSTA = {
    "Id": 13,
    "Name": "Madame Costa",
    "Age": 54,
    "Role": "Patiente hospitalisée — céphalées investiguées par PL",
    "History": (
        "Enseignante en école primaire, mariée, deux filles. Consulte pour des "
        "céphalées persistantes depuis deux semaines. Une ponction lombaire "
        "est prévue pour éliminer une méningite ou une hémorragie méningée. "
        "Phobie des aiguilles depuis l'enfance, très anxieuse à l'idée du "
        "geste. Cherche à comprendre et à se sentir rassurée."
    ),
    "ImageName": "MmeCosta.png",
}

LEA_COSTA = {
    "Id": 14,
    "Name": "Léa Costa",
    "Age": 28,
    "Role": "Fille de Madame Costa",
    "History": (
        "Infirmière en pédiatrie depuis 4 ans. Proche de sa mère, inquiète "
        "depuis son hospitalisation. Cherche activement des informations "
        "médicales, parfois insistante, tout en connaissant les règles du "
        "secret médical par sa propre pratique."
    ),
    "ImageName": "LeaCosta.png",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def resp(
    rid: int,
    text: str,
    next_id: int,
    soft: Dict[str, int],
    legacy: Dict[str, int],
    name: str | None = None,
) -> Dict[str, Any]:
    """Construit une Response conforme au schéma."""
    full_soft = {k: int(soft.get(k, 0)) for k in SOFT_KEYS}
    full_legacy = {k: int(legacy.get(k, 0)) for k in LEGACY_KEYS}
    return {
        "Id": rid,
        "Name": name or (text[:80] if text else ""),
        "Text": text,
        "SoftSkillDimensions": full_soft,
        "NextInteractionID": next_id,
        "LegacyDimensions": full_legacy,
    }


def interaction(
    iid: int,
    name: str,
    actor: Dict[str, Any],
    text: str,
    expression: str,
    responses: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return {
        "Id": iid,
        "Name": name,
        "Actor": deepcopy(actor),
        "Text": text,
        "AgentFacialExpression": expression,
        "Responses": responses,
    }


# ---------------------------------------------------------------------------
# CHAPITRE 1 — Premier jour de stage
# ---------------------------------------------------------------------------
def build_chapter_1() -> Dict[str, Any]:
    # Scène 1.1 — Accueil dans le service
    s1_interactions: List[Dict[str, Any]] = [
        interaction(
            1,
            "1. Dr Moreau vous accueille",
            DR_MOREAU,
            "« Bienvenue, Alex ! Je vais vous confier votre première "
            "rencontre patient. Monsieur Bernard attend en chambre 204. "
            "Allez vous présenter, prenez le temps qu'il faut. »",
            "DrMoreau_neutral.png",
            [
                resp(
                    1,
                    "« Merci Dr Moreau. Je vais me présenter et m'assurer "
                    "qu'il est à l'aise avant toute chose. »",
                    next_id=2,
                    soft={
                        "RespectAndDignity": 2, "Empathy": 2, "Compassion": 1,
                        "CommunicationClarity": 2, "ProfessionalBoundaries": 2,
                        "InterprofessionalCollaboration": 1,
                    },
                    legacy={"Authenticity": 2, "Respect": 2, "Empathy": 2},
                ),
                resp(
                    2,
                    "« D'accord, j'y vais tout de suite lui poser les "
                    "questions. »",
                    next_id=2,
                    soft={
                        "RespectAndDignity": 0, "Empathy": -1,
                        "CommunicationClarity": 0, "ProfessionalBoundaries": 1,
                        "EmotionalRegulation": -1,
                    },
                    legacy={"Respect": 0, "Empathy": -1},
                ),
                resp(
                    3,
                    "« Je préférerais que vous veniez avec moi, je ne me sens "
                    "pas encore capable d'y aller seul·e. »",
                    next_id=3,
                    soft={
                        "CommunicationClarity": 2, "ProfessionalBoundaries": 2,
                        "InterprofessionalCollaboration": 2,
                        "EmotionalRegulation": 1,
                    },
                    legacy={"Authenticity": 3, "Respect": 1},
                ),
            ],
        ),
        interaction(
            2,
            "2. Vous frappez à la porte de la chambre 204",
            ALEX,
            "Vous êtes devant la chambre 204. Que faites-vous ?",
            "Alex_neutral.png",
            [
                resp(
                    1,
                    "Je frappe deux fois, j'attends une réponse avant d'entrer.",
                    next_id=4,
                    soft={
                        "RespectAndDignity": 3, "CommunicationClarity": 2,
                        "ProfessionalBoundaries": 2,
                    },
                    legacy={"Respect": 3, "Authenticity": 1},
                ),
                resp(
                    2,
                    "J'entre directement pour ne pas perdre de temps.",
                    next_id=5,
                    soft={
                        "RespectAndDignity": -3, "Empathy": -1,
                        "ProfessionalBoundaries": -2,
                    },
                    legacy={"Respect": -3},
                ),
                resp(
                    3,
                    "Je frappe, j'ouvre la porte en même temps et je passe la "
                    "tête en demandant si je peux entrer.",
                    next_id=4,
                    soft={
                        "RespectAndDignity": 0, "CommunicationClarity": 1,
                        "ProfessionalBoundaries": 0,
                    },
                    legacy={"Respect": 0},
                ),
            ],
        ),
        interaction(
            3,
            "3. Dr Moreau vous rassure",
            DR_MOREAU,
            "« C'est honnête de votre part de le dire. Pour une première "
            "rencontre, c'est tout à fait justifié. Je vous accompagne, mais "
            "c'est vous qui mènerez la conversation. »",
            "DrMoreau_smile.png",
            [
                resp(
                    1,
                    "« Merci, je serai plus à l'aise ainsi. »",
                    next_id=2,
                    soft={
                        "Empathy": 1, "CommunicationClarity": 1,
                        "ProfessionalBoundaries": 1,
                        "InterprofessionalCollaboration": 2,
                    },
                    legacy={"Authenticity": 2, "Respect": 1},
                ),
            ],
        ),
        interaction(
            4,
            "4. Monsieur Bernard vous invite à entrer",
            M_BERNARD,
            "« Entrez, entrez… »",
            "MBernard_neutral.png",
            [
                resp(
                    1,
                    "« Bonjour Monsieur Bernard. Je suis Alex, étudiant·e en "
                    "2e année de médecine. Je travaille avec le Dr Moreau. "
                    "Puis-je prendre un moment pour échanger avec vous ? »",
                    next_id=6,
                    soft={
                        "RespectAndDignity": 3, "Empathy": 2,
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 3,
                        "InterprofessionalCollaboration": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 3, "Empathy": 2},
                ),
                resp(
                    2,
                    "« Bonjour, je suis là pour votre anamnèse. »",
                    next_id=6,
                    soft={
                        "CommunicationClarity": 0, "ProfessionalBoundaries": 0,
                        "Empathy": -1, "RespectAndDignity": 0,
                    },
                    legacy={"Authenticity": 0, "Respect": 0},
                ),
                resp(
                    3,
                    "« Salut Monsieur, je suis le nouveau ! »",
                    next_id=5,
                    soft={
                        "RespectAndDignity": -2, "ProfessionalBoundaries": -2,
                        "CommunicationClarity": -1,
                    },
                    legacy={"Authenticity": 0, "Respect": -2},
                ),
            ],
        ),
        interaction(
            5,
            "5. Monsieur Bernard est contrarié",
            M_BERNARD,
            "« Vous auriez pu attendre que je dise 'oui'… et puis, qui "
            "êtes-vous exactement ? »",
            "MBernard_cold-anger.png",
            [
                resp(
                    1,
                    "« Vous avez raison, je vous prie de m'excuser. Je suis "
                    "Alex, étudiant·e en médecine. Je peux repasser plus tard "
                    "si vous préférez. »",
                    next_id=6,
                    soft={
                        "RespectAndDignity": 3, "Empathy": 2,
                        "EmotionalRegulation": 2,
                        "CommunicationClarity": 2,
                        "ProfessionalBoundaries": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 3, "Empathy": 2},
                ),
                resp(
                    2,
                    "« Je suis pressé·e, les médecins ont demandé qu'on fasse "
                    "vite. »",
                    next_id=6,
                    soft={
                        "RespectAndDignity": -2, "Empathy": -2,
                        "EmotionalRegulation": -2,
                        "ProfessionalBoundaries": -1,
                    },
                    legacy={"Respect": -2, "Empathy": -2},
                ),
                resp(
                    3,
                    "« Ce n'est pas grave, ça arrive à tout le monde. »",
                    next_id=6,
                    soft={
                        "Empathy": -1, "EmotionalRegulation": 0,
                        "CommunicationClarity": -1,
                    },
                    legacy={"Authenticity": -1},
                ),
            ],
        ),
        interaction(
            6,
            "6. Monsieur Bernard acquiesce",
            M_BERNARD,
            "« Bon, asseyez-vous. Qu'est-ce que vous voulez savoir ? »",
            "MBernard_neutral.png",
            [
                resp(
                    1,
                    "« Merci. Pour commencer, pouvez-vous me raconter avec vos "
                    "mots ce qui vous amène à l'hôpital ? »",
                    next_id=-1,
                    soft={
                        "RespectAndDignity": 2, "Empathy": 3,
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 2,
                    },
                    legacy={"Authenticity": 2, "Respect": 2, "Empathy": 3},
                ),
                resp(
                    2,
                    "« Depuis quand vous avez mal et où exactement ? »",
                    next_id=-1,
                    soft={
                        "CommunicationClarity": 1, "Empathy": 0,
                        "ProfessionalBoundaries": 1,
                    },
                    legacy={"Respect": 0},
                ),
            ],
        ),
    ]

    # Scène 1.2 — Première anamnèse (raccourcie mais pédagogique)
    s2_interactions: List[Dict[str, Any]] = [
        interaction(
            1,
            "1. Vous démarrez l'anamnèse",
            ALEX,
            "Vous êtes assis·e face à Monsieur Bernard. Comment débutez-vous "
            "l'anamnèse ?",
            "Alex_neutral.png",
            [
                resp(
                    1,
                    "« Prenez votre temps. Racontez-moi ce qui s'est passé, "
                    "de votre point de vue. »",
                    next_id=2,
                    soft={
                        "Empathy": 3, "CommunicationClarity": 3,
                        "RespectAndDignity": 2,
                    },
                    legacy={"Authenticity": 2, "Respect": 2, "Empathy": 3},
                ),
                resp(
                    2,
                    "« Quel est votre motif d'hospitalisation précis ? "
                    "Date d'apparition, intensité sur 10, irradiation ? »",
                    next_id=3,
                    soft={
                        "CommunicationClarity": 1, "Empathy": -1,
                        "ProfessionalBoundaries": 1,
                    },
                    legacy={"Respect": 0, "Empathy": -1},
                ),
            ],
        ),
        interaction(
            2,
            "2. Monsieur Bernard se confie",
            M_BERNARD,
            "« Hier soir, j'ai eu une vraie frousse. Une pression dans la "
            "poitrine, comme si on serrait. J'ai eu peur d'y passer. »",
            "MBernard_sad.png",
            [
                resp(
                    1,
                    "« C'est effrayant ce que vous décrivez. Vous êtes en "
                    "sécurité ici. Est-ce que ça vous va si on reprend ensemble "
                    "les détails, à votre rythme ? »",
                    next_id=4,
                    soft={
                        "Empathy": 3, "Compassion": 3,
                        "EmotionalRegulation": 2,
                        "CommunicationClarity": 3,
                        "RespectAndDignity": 2,
                    },
                    legacy={"Authenticity": 2, "Compassion": 3, "Empathy": 3, "Hope": 2},
                ),
                resp(
                    2,
                    "« Oui, c'est classique comme symptôme. »",
                    next_id=4,
                    soft={
                        "Empathy": -2, "Compassion": -2,
                        "CommunicationClarity": -1,
                    },
                    legacy={"Empathy": -2, "Compassion": -1},
                ),
                resp(
                    3,
                    "« Rassurez-vous, à votre âge on s'en sort toujours. »",
                    next_id=4,
                    soft={
                        "Empathy": -1, "CommunicationClarity": -2,
                        "Compassion": -1,
                    },
                    legacy={"Authenticity": -2, "Hope": -1},
                ),
            ],
        ),
        interaction(
            3,
            "3. Monsieur Bernard se ferme",
            M_BERNARD,
            "Il soupire, croise les bras : « On dirait un interrogatoire… »",
            "MBernard_cold-anger.png",
            [
                resp(
                    1,
                    "« Pardon, je me suis enchaîné·e sur les questions. "
                    "Reprenons calmement — qu'est-ce qui vous a fait le plus "
                    "peur hier soir ? »",
                    next_id=2,
                    soft={
                        "Empathy": 3, "EmotionalRegulation": 3,
                        "RespectAndDignity": 2,
                        "CommunicationClarity": 2,
                    },
                    legacy={"Authenticity": 3, "Empathy": 3, "Respect": 2},
                ),
                resp(
                    2,
                    "« C'est la procédure standard, il faut bien que je "
                    "remplisse le dossier. »",
                    next_id=4,
                    soft={
                        "Empathy": -2, "RespectAndDignity": -2,
                        "CommunicationClarity": -2, "EmotionalRegulation": -1,
                    },
                    legacy={"Respect": -2, "Empathy": -2},
                ),
            ],
        ),
        interaction(
            4,
            "4. Dr Moreau intervient pour débriefer",
            DR_MOREAU,
            "« Bien. On va sortir et parler deux minutes. Qu'est-ce que vous "
            "retenez de cette rencontre ? »",
            "DrMoreau_neutral.png",
            [
                resp(
                    1,
                    "« Qu'une anamnèse, c'est d'abord une relation. Les "
                    "questions fermées peuvent casser le lien. J'aurais dû "
                    "commencer par une question ouverte. »",
                    next_id=-1,
                    soft={
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 2,
                        "InterprofessionalCollaboration": 3,
                        "EmotionalRegulation": 2,
                    },
                    legacy={"Authenticity": 3, "Empathy": 2, "Respect": 2},
                ),
                resp(
                    2,
                    "« Qu'il faut être plus ferme pour obtenir les "
                    "informations nécessaires. »",
                    next_id=-1,
                    soft={
                        "Empathy": -2, "CommunicationClarity": -2,
                        "RespectAndDignity": -1,
                    },
                    legacy={"Respect": -2, "Empathy": -2},
                ),
                resp(
                    3,
                    "« J'ai eu du mal, j'aimerais refaire un entretien demain "
                    "pour progresser. »",
                    next_id=-1,
                    soft={
                        "CommunicationClarity": 2,
                        "ProfessionalBoundaries": 2,
                        "EmotionalRegulation": 2,
                        "InterprofessionalCollaboration": 2,
                    },
                    legacy={"Authenticity": 3, "Hope": 2},
                ),
            ],
        ),
    ]

    scenes = [
        {
            "Id": 1,
            "Title": "1.1 Accueil dans le service",
            "SceneIntroduction": (
                "C'est votre premier jour de stage en médecine interne. Le "
                "Dr Moreau, votre mentor, vient vous accueillir. Votre "
                "première tâche : aller vous présenter à Monsieur Bernard, "
                "62 ans, hospitalisé la veille pour une douleur thoracique."
            ),
            "Min": 8,
            "Interactions": s1_interactions,
        },
        {
            "Id": 2,
            "Title": "1.2 Première anamnèse",
            "SceneIntroduction": (
                "Monsieur Bernard vous a accueilli·e. Il est temps de mener "
                "votre première anamnèse. Rappel pédagogique : on commence "
                "par des questions ouvertes, on valide les émotions, on "
                "précise ensuite avec des questions fermées ciblées."
            ),
            "Min": 8,
            "Interactions": s2_interactions,
        },
    ]

    return {
        "Id": 1,
        "Name": "Premier jour de stage",
        "Intro": (
            "Alex entame son premier stage hospitalier. Objectif pédagogique : "
            "savoir se présenter, respecter l'intimité, entamer une anamnèse "
            "en s'appuyant sur l'écoute active."
        ),
        "Scenes": scenes,
    }


# ---------------------------------------------------------------------------
# CHAPITRE 2 — L'examen qui fait peur
# ---------------------------------------------------------------------------
def build_chapter_2() -> Dict[str, Any]:
    interactions: List[Dict[str, Any]] = [
        interaction(
            1,
            "1. Madame Costa vous interpelle",
            MME_COSTA,
            "« Alex, c'est ça ? On m'a dit que vous alliez m'expliquer la "
            "ponction lombaire… j'ai une trouille bleue des aiguilles. »",
            "MmeCosta_worried.png",
            [
                resp(
                    1,
                    "« Oui, c'est moi. Je comprends que ça fasse peur — "
                    "prenons le temps qu'il faut. Que savez-vous déjà du geste ? »",
                    next_id=2,
                    soft={
                        "Empathy": 3, "Compassion": 3,
                        "EmotionalRegulation": 2,
                        "CommunicationClarity": 2,
                        "RespectAndDignity": 2,
                    },
                    legacy={"Authenticity": 2, "Empathy": 3, "Compassion": 3, "Hope": 1},
                ),
                resp(
                    2,
                    "« Ne vous inquiétez pas, ça ne fait presque pas mal. »",
                    next_id=3,
                    soft={
                        "Empathy": -1, "CommunicationClarity": -2,
                        "ProfessionalBoundaries": -1,
                    },
                    legacy={"Authenticity": -3, "Hope": 1, "Empathy": -1},
                ),
                resp(
                    3,
                    "« Alors, on va vous piquer dans le dos entre deux "
                    "vertèbres pour prélever du liquide céphalo-rachidien. »",
                    next_id=3,
                    soft={
                        "CommunicationClarity": 0, "Empathy": -2,
                        "Compassion": -2,
                    },
                    legacy={"Respect": 0, "Empathy": -2},
                ),
            ],
        ),
        interaction(
            2,
            "2. Madame Costa se livre",
            MME_COSTA,
            "« J'ai déjà fait un malaise lors d'une prise de sang il y a 10 ans… "
            "j'ai peur que ça recommence. »",
            "MmeCosta_sad.png",
            [
                resp(
                    1,
                    "« Merci de me le dire, c'est précieux. On va pouvoir "
                    "prévenir : je vais en parler à l'équipe, on peut vous "
                    "installer allongée, avec quelqu'un à côté. Ça vous "
                    "rassure ? »",
                    next_id=4,
                    soft={
                        "Empathy": 3, "Compassion": 2,
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 2,
                        "InterprofessionalCollaboration": 3,
                    },
                    legacy={"Authenticity": 2, "Empathy": 3, "Hope": 2, "Respect": 2},
                ),
                resp(
                    2,
                    "« Ça n'arrivera sûrement pas aujourd'hui. »",
                    next_id=4,
                    soft={
                        "Empathy": -1, "CommunicationClarity": -2,
                    },
                    legacy={"Authenticity": -2, "Hope": -1},
                ),
                resp(
                    3,
                    "« Il faudra essayer de respirer calmement et tout ira "
                    "bien. »",
                    next_id=4,
                    soft={
                        "Empathy": 0, "Compassion": 0, "CommunicationClarity": 0,
                    },
                    legacy={"Hope": 1},
                ),
            ],
        ),
        interaction(
            3,
            "3. Madame Costa panique",
            MME_COSTA,
            "Sa voix tremble : « Attendez, je ne suis pas sûre de vouloir "
            "faire ça… »",
            "MmeCosta_fear.png",
            [
                resp(
                    1,
                    "« Vous avez tout à fait le droit de ne pas être sûre. On "
                    "peut en reparler ensemble — qu'est-ce qui vous fait le "
                    "plus peur ? »",
                    next_id=2,
                    soft={
                        "RespectAndDignity": 3, "Empathy": 3,
                        "EmotionalRegulation": 2, "Compassion": 2,
                        "CommunicationClarity": 3,
                    },
                    legacy={"Authenticity": 3, "Respect": 3, "Empathy": 3},
                ),
                resp(
                    2,
                    "« Il le faut, le médecin l'a prescrit. »",
                    next_id=4,
                    soft={
                        "RespectAndDignity": -3, "Empathy": -2,
                        "ProfessionalBoundaries": -2,
                        "CommunicationClarity": -2,
                    },
                    legacy={"Authenticity": 0, "Respect": -3},
                ),
                resp(
                    3,
                    "« Je vais chercher le Dr Moreau pour qu'il vous réexplique. »",
                    next_id=5,
                    soft={
                        "ProfessionalBoundaries": 3,
                        "InterprofessionalCollaboration": 3,
                        "EmotionalRegulation": 2,
                    },
                    legacy={"Authenticity": 2, "Respect": 2},
                ),
            ],
        ),
        interaction(
            4,
            "4. Vous expliquez le déroulement",
            ALEX,
            "Comment présentez-vous concrètement le déroulement du geste ?",
            "Alex_neutral.png",
            [
                resp(
                    1,
                    "« Je vous explique étape par étape, et à chaque moment "
                    "vous pouvez me demander de m'arrêter. Ça vous va ? »",
                    next_id=6,
                    soft={
                        "RespectAndDignity": 3, "Empathy": 2,
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 2,
                    },
                    legacy={"Authenticity": 2, "Respect": 3, "Empathy": 2, "Hope": 1},
                ),
                resp(
                    2,
                    "« L'aiguille fait environ 9 centimètres, elle traverse "
                    "plusieurs plans avant le liquide. »",
                    next_id=3,
                    soft={
                        "CommunicationClarity": -1, "Empathy": -2,
                        "EmotionalRegulation": -2,
                    },
                    legacy={"Authenticity": 2, "Hope": -2, "Empathy": -2},
                ),
            ],
        ),
        interaction(
            5,
            "5. Dr Moreau réinterroge le consentement",
            DR_MOREAU,
            "« Madame Costa, Alex m'a alerté·e. On peut tout à fait "
            "reprogrammer l'examen ou trouver une alternative. Votre accord "
            "est indispensable. »",
            "DrMoreau_smile.png",
            [
                resp(
                    1,
                    "Vous observez et complétez : « Madame Costa, je suis "
                    "vraiment désolé·e si j'ai été maladroit·e. »",
                    next_id=6,
                    soft={
                        "EmotionalRegulation": 3, "Empathy": 2,
                        "CommunicationClarity": 2,
                        "InterprofessionalCollaboration": 2,
                        "ProfessionalBoundaries": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 2, "Empathy": 2},
                ),
                resp(
                    2,
                    "Vous quittez la pièce sans rien dire.",
                    next_id=6,
                    soft={
                        "EmotionalRegulation": -2, "ProfessionalBoundaries": -1,
                        "InterprofessionalCollaboration": -1,
                    },
                    legacy={"Authenticity": -1, "Respect": -1},
                ),
            ],
        ),
        interaction(
            6,
            "6. Madame Costa donne son accord",
            MME_COSTA,
            "Elle respire, sourit faiblement : « D'accord, je vous fais "
            "confiance. Merci de m'avoir écoutée. »",
            "MmeCosta_relief.png",
            [
                resp(
                    1,
                    "« C'est moi qui vous remercie de votre confiance. »",
                    next_id=-1,
                    soft={
                        "Empathy": 2, "CommunicationClarity": 2,
                        "RespectAndDignity": 2,
                    },
                    legacy={"Authenticity": 2, "Respect": 2, "Empathy": 2, "Hope": 2},
                ),
            ],
        ),
    ]

    return {
        "Id": 2,
        "Name": "L'examen qui fait peur",
        "Intro": (
            "Madame Costa doit subir une ponction lombaire. Elle est très "
            "anxieuse. Objectif pédagogique : informer avec clarté, accueillir "
            "la peur, respecter le consentement et savoir solliciter l'équipe."
        ),
        "Scenes": [
            {
                "Id": 1,
                "Title": "2.1 Avant la ponction lombaire",
                "SceneIntroduction": (
                    "Vous devez expliquer à Madame Costa, 54 ans, le "
                    "déroulement d'une ponction lombaire prescrite pour "
                    "explorer ses céphalées. Elle est visiblement angoissée."
                ),
                "Min": 8,
                "Interactions": interactions,
            }
        ],
    }


# ---------------------------------------------------------------------------
# CHAPITRE 3 — Secret médical et famille
# ---------------------------------------------------------------------------
def build_chapter_3() -> Dict[str, Any]:
    interactions: List[Dict[str, Any]] = [
        interaction(
            1,
            "1. Léa Costa vous interpelle dans le couloir",
            LEA_COSTA,
            "« Bonjour, je suis la fille de Madame Costa. Pouvez-vous me dire "
            "où en sont les résultats ? Je suis infirmière, vous pouvez me "
            "parler sans problème. »",
            "LeaCosta_worried.png",
            [
                resp(
                    1,
                    "« Bonjour. Je comprends votre inquiétude. Je ne peux pas "
                    "vous communiquer les résultats sans l'accord explicite "
                    "de votre mère, même entre professionnel·le·s. Souhaitez-"
                    "vous qu'on aille lui en parler ensemble ? »",
                    next_id=3,
                    soft={
                        "RespectAndDignity": 3,
                        "ProfessionalBoundaries": 3,
                        "CommunicationClarity": 3, "Empathy": 2,
                        "EmotionalRegulation": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 3, "Empathy": 2},
                ),
                resp(
                    2,
                    "« Bien sûr, entre nous, la PL est prévue cet après-midi "
                    "et la prise de sang montre une CRP à 42. »",
                    next_id=2,
                    soft={
                        "RespectAndDignity": -3,
                        "ProfessionalBoundaries": -3,
                        "CommunicationClarity": -2,
                    },
                    legacy={"Authenticity": -2, "Respect": -3},
                ),
                resp(
                    3,
                    "« Adressez-vous au médecin, ce n'est pas mon problème. »",
                    next_id=4,
                    soft={
                        "Empathy": -2, "Compassion": -2,
                        "CommunicationClarity": -2,
                        "InterprofessionalCollaboration": -2,
                    },
                    legacy={"Respect": -1, "Empathy": -2},
                ),
            ],
        ),
        interaction(
            2,
            "2. Dr Moreau a tout entendu",
            DR_MOREAU,
            "Ton ferme : « Alex, venez avec moi. Il faut qu'on parle de ce "
            "que vous venez de faire. »",
            "DrMoreau_cold-anger.png",
            [
                resp(
                    1,
                    "« Vous avez raison, j'ai partagé des informations "
                    "médicales sans consentement. J'ai manqué au secret "
                    "professionnel. »",
                    next_id=5,
                    soft={
                        "EmotionalRegulation": 3,
                        "CommunicationClarity": 2,
                        "ProfessionalBoundaries": 2,
                        "InterprofessionalCollaboration": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 2},
                ),
                resp(
                    2,
                    "« Elle est infirmière, je pensais que ça ne posait pas "
                    "de problème. »",
                    next_id=5,
                    soft={
                        "ProfessionalBoundaries": -2,
                        "CommunicationClarity": -1,
                        "EmotionalRegulation": -1,
                    },
                    legacy={"Authenticity": 1, "Respect": -2},
                ),
            ],
        ),
        interaction(
            3,
            "3. Léa comprend et accepte",
            LEA_COSTA,
            "« D'accord… c'est vrai, je connais la règle, mais c'est ma mère. "
            "Merci de ne pas avoir cédé. On peut aller la voir ensemble ? »",
            "LeaCosta_calm.png",
            [
                resp(
                    1,
                    "« Oui, avec plaisir. On va d'abord lui demander si elle "
                    "souhaite que les informations vous soient partagées, et "
                    "on adapte. »",
                    next_id=6,
                    soft={
                        "RespectAndDignity": 3,
                        "Empathy": 2,
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 3,
                        "InterprofessionalCollaboration": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 3, "Empathy": 2, "Hope": 2},
                ),
                resp(
                    2,
                    "« Allons-y directement, vous la connaissez bien. »",
                    next_id=6,
                    soft={
                        "ProfessionalBoundaries": -1,
                        "RespectAndDignity": 0,
                        "CommunicationClarity": 0,
                    },
                    legacy={"Respect": -1},
                ),
            ],
        ),
        interaction(
            4,
            "4. Léa se sent abandonnée",
            LEA_COSTA,
            "Les larmes aux yeux : « J'ai juste peur pour ma mère, je ne "
            "demandais pas la lune… »",
            "LeaCosta_sad.png",
            [
                resp(
                    1,
                    "« Je suis désolé·e, j'ai été trop abrupt·e. Je comprends "
                    "votre inquiétude. Je ne peux pas partager les "
                    "résultats sans l'accord de votre mère, mais je peux "
                    "vous accompagner pour lui poser la question. »",
                    next_id=3,
                    soft={
                        "Empathy": 3, "Compassion": 3,
                        "EmotionalRegulation": 2,
                        "CommunicationClarity": 2,
                        "ProfessionalBoundaries": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 2, "Empathy": 3},
                ),
                resp(
                    2,
                    "« Ce n'est pas mon rôle de gérer les familles. »",
                    next_id=5,
                    soft={
                        "Empathy": -3, "Compassion": -3,
                        "ProfessionalBoundaries": -2,
                        "InterprofessionalCollaboration": -2,
                    },
                    legacy={"Respect": -2, "Empathy": -3},
                ),
            ],
        ),
        interaction(
            5,
            "5. Dr Moreau débriefe avec vous",
            DR_MOREAU,
            "« Le secret médical n'est pas une formalité administrative. "
            "C'est la condition de la confiance. Qu'allez-vous retenir ? »",
            "DrMoreau_neutral.png",
            [
                resp(
                    1,
                    "« Que l'accord du patient prime, même avec un proche "
                    "professionnel de santé. Que je peux proposer de "
                    "partager en présence du patient. »",
                    next_id=-1,
                    soft={
                        "ProfessionalBoundaries": 3,
                        "CommunicationClarity": 3,
                        "InterprofessionalCollaboration": 3,
                        "EmotionalRegulation": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 3},
                ),
                resp(
                    2,
                    "« Qu'il faut rediriger tout de suite vers le médecin "
                    "pour éviter les erreurs. »",
                    next_id=-1,
                    soft={
                        "ProfessionalBoundaries": 2,
                        "CommunicationClarity": 1,
                        "Empathy": -1,
                    },
                    legacy={"Respect": 1},
                ),
            ],
        ),
        interaction(
            6,
            "6. Madame Costa donne son accord",
            MME_COSTA,
            "« Oui, bien sûr, je veux que Léa soit informée. Merci de me "
            "l'avoir demandé. »",
            "MmeCosta_smile.png",
            [
                resp(
                    1,
                    "« Merci à vous. Je vais expliquer à toutes les deux où "
                    "on en est des examens. »",
                    next_id=-1,
                    soft={
                        "RespectAndDignity": 3, "Empathy": 2,
                        "CommunicationClarity": 3,
                        "ProfessionalBoundaries": 3,
                        "InterprofessionalCollaboration": 2,
                    },
                    legacy={"Authenticity": 3, "Respect": 3, "Empathy": 2, "Hope": 2},
                ),
            ],
        ),
    ]

    return {
        "Id": 3,
        "Name": "Secret médical et famille",
        "Intro": (
            "Une proche de patiente demande des informations. Objectif "
            "pédagogique : appliquer le secret professionnel, gérer une "
            "famille inquiète, savoir proposer un partage en présence et "
            "avec l'accord du patient."
        ),
        "Scenes": [
            {
                "Id": 1,
                "Title": "3.1 Une demande dans le couloir",
                "SceneIntroduction": (
                    "Dans le couloir du service, Léa Costa, fille de Madame "
                    "Costa et elle-même infirmière, vous aborde pour "
                    "demander des nouvelles médicales de sa mère."
                ),
                "Min": 8,
                "Interactions": interactions,
            }
        ],
    }


# ---------------------------------------------------------------------------
# Entrée principale
# ---------------------------------------------------------------------------
def main() -> None:
    book: Dict[str, Any] = {
        "Chapters": [
            build_chapter_1(),
            build_chapter_2(),
            build_chapter_3(),
        ]
    }
    out_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "chapters",
        "MedStudents_Y2_v1.json",
    )
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
    print(f"Écrit : {out_path}")


if __name__ == "__main__":
    main()
