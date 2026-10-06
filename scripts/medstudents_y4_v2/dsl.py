"""Mini-langage d'écriture des scènes du livre MedStudents Y4 v2.

Une scène s'écrit comme une liste d'interactions `I(...)`, chacune avec ses
réponses `R(...)`. Les scores s'écrivent en abrégé, seules les dimensions non
nulles sont notées :

    R("« Je peux relire le dossier avec vous ? »", 2, "cc2 pb2 ic1 er1")

Codes : rd Respect et dignité · em Empathie · co Compassion · er Régulation
émotionnelle · cc Clarté de communication · pb Frontières professionnelles ·
ic Collaboration interprofessionnelle. Valeurs de -3 à +3.

Les états narratifs s'écrivent `sets=` / `clears=` sur une réponse, `when=` sur
une scène, `Entry(...)` pour un point d'entrée conditionnel et `Debrief(...)`
pour un bilan propre à une issue. `to_dict()` produit le JSON du schéma
Chapters > Scenes > Interactions > Responses.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from domain.soft_skills import LEGACY_SKILLS, SOFT_SKILLS

from .cast import actor_dict, expression_image

END = -1

SKILL_CODES: dict[str, str] = {
    "rd": "RespectAndDignity",
    "em": "Empathy",
    "co": "Compassion",
    "er": "EmotionalRegulation",
    "cc": "CommunicationClarity",
    "pb": "ProfessionalBoundaries",
    "ic": "InterprofessionalCollaboration",
}
CODE_OF_SKILL: dict[str, str] = {v: k for k, v in SKILL_CODES.items()}

_TOKEN = re.compile(r"([a-z]{2})([+-]?\d)")


def parse_scores(spec: str) -> dict[str, int]:
    """« cc2 er-1 » -> dict complet des 7 dimensions."""
    out = {k: 0 for k in SOFT_SKILLS}
    for tok in spec.split():
        m = _TOKEN.fullmatch(tok)
        if not m or m.group(1) not in SKILL_CODES:
            raise ValueError(f"Score illisible : {tok!r} dans {spec!r}")
        value = int(m.group(2))
        if not -3 <= value <= 3:
            raise ValueError(f"Score hors bornes : {tok!r}")
        out[SKILL_CODES[m.group(1)]] = value
    return out


def legacy_from(soft: dict[str, int]) -> dict[str, int]:
    """Dimensions historiques (non utilisées par le parcours) dérivées des 7."""
    def clamp(v: float) -> int:
        return max(-3, min(3, round(v)))

    derived = {
        "Authenticity": clamp((soft["CommunicationClarity"] + soft["ProfessionalBoundaries"]
                               + soft["EmotionalRegulation"]) / 2),
        "Respect": soft["RespectAndDignity"],
        "Compassion": soft["Compassion"],
        "Hope": 0,
        "Empathy": soft["Empathy"],
    }
    return {k: derived[k] for k in LEGACY_SKILLS}


def when(all: tuple[str, ...] | list[str] = (), any: tuple[str, ...] | list[str] = (),
         none: tuple[str, ...] | list[str] = ()) -> dict[str, list[str]]:
    """Condition sur les états : tous (all), au moins un (any), aucun (none)."""
    cond = {"all": list(all), "any": list(any), "none": list(none)}
    return {k: v for k, v in cond.items() if v}


@dataclass
class R:
    """Réponse proposée au joueur."""

    text: str
    next: int
    scores: str = ""
    sets: tuple[str, ...] | list[str] = ()
    clears: tuple[str, ...] | list[str] = ()

    def soft(self) -> dict[str, int]:
        return parse_scores(self.scores)

    def total(self) -> int:
        return sum(self.soft().values())

    def to_dict(self, rid: int) -> dict[str, Any]:
        soft = self.soft()
        d: dict[str, Any] = {
            "Id": rid,
            "Name": self.text[:80],
            "Text": self.text,
            "SoftSkillDimensions": soft,
            "NextInteractionID": self.next,
            "LegacyDimensions": legacy_from(soft),
        }
        if self.sets:
            d["SetFlags"] = list(self.sets)
        if self.clears:
            d["ClearFlags"] = list(self.clears)
        return d


@dataclass
class I:
    """Interaction : un personnage (clé de `cast.CAST`) parle, le joueur répond.

    `actor="narr"` pour une narration sans portrait. Une interaction sans
    réponse termine la scène (bouton « Continuer »).
    """

    id: int
    actor: str
    expr: str
    text: str
    responses: list[R] = field(default_factory=list)
    name: str | None = None

    def auto_name(self) -> str:
        if self.name:
            return f"{self.id}. {self.name}"
        words = re.sub(r"[«»\"]", "", self.text).split()
        short = " ".join(words[:6])
        return f"{self.id}. {short}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "Id": self.id,
            "Name": self.auto_name(),
            "Actor": actor_dict(self.actor),
            "Text": self.text,
            "AgentFacialExpression": expression_image(self.actor, self.expr),
            "Responses": [r.to_dict(i + 1) for i, r in enumerate(self.responses)],
        }


@dataclass
class Entry:
    """Point d'entrée conditionnel d'une scène (le premier qui correspond gagne)."""

    interaction: int
    cond: dict[str, list[str]]
    intro: str = ""

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {"Condition": self.cond, "InteractionId": self.interaction}
        if self.intro:
            d["Intro"] = self.intro
        return d


@dataclass
class Debrief:
    """Bilan de fin de scène propre à une issue (remplace l'appréciation générique)."""

    cond: dict[str, list[str]]
    lead: str
    tone: str = "hard"

    def to_dict(self) -> dict[str, Any]:
        return {"Condition": self.cond, "Tone": self.tone, "Lead": self.lead}


@dataclass
class S:
    """Scène. `slot` regroupe des scènes alternatives (même rang dans le chapitre)."""

    id: int
    title: str
    intro: str
    nodes: list[I]
    focus: tuple[str, ...] = ()
    slot: str | None = None
    cond: dict[str, list[str]] | None = None
    entries: list[Entry] = field(default_factory=list)
    debriefs: list[Debrief] = field(default_factory=list)

    def minutes(self) -> int:
        # Un parcours traverse un peu plus de la moitié des interactions.
        return max(5, round(len(self.nodes) * 0.6))

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "Id": self.id,
            "Title": self.title,
            "SceneIntroduction": self.intro,
            "Min": self.minutes(),
            "Interactions": [n.to_dict() for n in self.nodes],
            "Slot": self.slot or self.title.split(" ", 1)[0],
            "SoftSkillFocus": [SKILL_CODES[c] for c in self.focus],
        }
        if self.cond:
            d["Condition"] = self.cond
        if self.entries:
            d["EntryPoints"] = [e.to_dict() for e in self.entries]
        if self.debriefs:
            d["Debriefs"] = [x.to_dict() for x in self.debriefs]
        return d


@dataclass
class StartChoice:
    """Écran proposé au début d'un chapitre si aucun des états attendus n'est connu."""

    unless_any: list[str]
    question: str
    options: list[tuple[str, list[str]]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "UnlessAny": self.unless_any,
            "Question": self.question,
            "Options": [{"Label": label, "Flags": flags} for label, flags in self.options],
        }


@dataclass
class C:
    """Chapitre. L'intro joueur est suivie des objectifs et ancrages (enseignant·e)."""

    id: int
    name: str
    situation: str
    objectives: str
    anchoring: str
    scenes: list[S]
    focus: tuple[str, ...] = ()
    start_choice: StartChoice | None = None

    def to_dict(self) -> dict[str, Any]:
        intro = (
            f"{self.situation} Objectif pédagogique : {self.objectives} "
            f"Ancrage M1 : {self.anchoring}"
        )
        d: dict[str, Any] = {
            "Id": self.id,
            "Name": self.name,
            "Intro": intro,
            "Scenes": [s.to_dict() for s in self.scenes],
            "SoftSkillFocus": [SKILL_CODES[c] for c in self.focus],
        }
        if self.start_choice:
            d["StartChoice"] = self.start_choice.to_dict()
        return d
