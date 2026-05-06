"""Modèles métier (dataclasses) — round-trip safe avec le JSON source.

Chaque dataclass expose `from_dict(d)` et `to_dict()`. Tout champ JSON inconnu
est conservé dans `_extra` pour garantir un aller-retour fidèle (les scènes
embarquent par exemple des `Min/MaxXXX` que le code métier n'utilise pas).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar, TypedDict


class Book(TypedDict):
    """Description d'un livre (déclaré dans `books.py`)."""

    slug: str
    title: str
    subtitle: str
    description: str
    audience: str
    json: str


SoftSkillScores = dict[str, int]


def _split_known(d: dict[str, Any], known: tuple[str, ...]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Sépare un dict entre clés connues et clés inconnues."""
    known_set = set(known)
    knowns = {k: d[k] for k in d if k in known_set}
    extras = {k: d[k] for k in d if k not in known_set}
    return knowns, extras


@dataclass
class Actor:
    Id: int = 0
    Name: str = ""
    Age: int | str = ""
    Role: str = ""
    History: str = ""
    ImageName: str = ""
    _extra: dict[str, Any] = field(default_factory=dict, repr=False)

    KNOWN: ClassVar[tuple[str, ...]] = ("Id", "Name", "Age", "Role", "History", "ImageName")

    @classmethod
    def from_dict(cls, d: dict[str, Any] | None) -> "Actor":
        if not d:
            return cls()
        knowns, extras = _split_known(d, cls.KNOWN)
        return cls(
            Id=knowns.get("Id", 0),
            Name=knowns.get("Name", ""),
            Age=knowns.get("Age", ""),
            Role=knowns.get("Role", ""),
            History=knowns.get("History", ""),
            ImageName=knowns.get("ImageName", ""),
            _extra=extras,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Age": self.Age,
            "Role": self.Role,
            "History": self.History,
            "ImageName": self.ImageName,
            **self._extra,
        }


@dataclass
class Response:
    Id: int = 0
    Name: str = ""
    Text: str = ""
    NextInteractionID: int | None = None
    SoftSkillDimensions: SoftSkillScores = field(default_factory=dict)
    LegacyDimensions: dict[str, int] = field(default_factory=dict)
    _extra: dict[str, Any] = field(default_factory=dict, repr=False)

    KNOWN: ClassVar[tuple[str, ...]] = (
        "Id", "Name", "Text", "NextInteractionID",
        "SoftSkillDimensions", "LegacyDimensions",
    )

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Response":
        knowns, extras = _split_known(d, cls.KNOWN)
        return cls(
            Id=knowns.get("Id", 0),
            Name=knowns.get("Name", ""),
            Text=knowns.get("Text", ""),
            NextInteractionID=knowns.get("NextInteractionID"),
            SoftSkillDimensions=dict(knowns.get("SoftSkillDimensions") or {}),
            LegacyDimensions=dict(knowns.get("LegacyDimensions") or {}),
            _extra=extras,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Text": self.Text,
            "NextInteractionID": self.NextInteractionID,
            "SoftSkillDimensions": dict(self.SoftSkillDimensions),
            "LegacyDimensions": dict(self.LegacyDimensions),
            **self._extra,
        }

    def score(self, skill: str) -> int:
        """Lit un score depuis SoftSkillDimensions ou un champ plat (compat v3)."""
        return self.SoftSkillDimensions.get(skill, self._extra.get(skill, 0))


@dataclass
class Interaction:
    Id: int = 0
    Name: str = ""
    Text: str = ""
    Actor: Actor = field(default_factory=Actor)
    Responses: list[Response] = field(default_factory=list)
    AgentFacialExpression: str = ""
    _extra: dict[str, Any] = field(default_factory=dict, repr=False)

    KNOWN: ClassVar[tuple[str, ...]] = (
        "Id", "Name", "Text", "Actor", "Responses", "AgentFacialExpression",
    )

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Interaction":
        knowns, extras = _split_known(d, cls.KNOWN)
        return cls(
            Id=knowns.get("Id", 0),
            Name=knowns.get("Name", ""),
            Text=knowns.get("Text", ""),
            Actor=Actor.from_dict(knowns.get("Actor")),
            Responses=[Response.from_dict(r) for r in knowns.get("Responses") or []],
            AgentFacialExpression=knowns.get("AgentFacialExpression", ""),
            _extra=extras,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Text": self.Text,
            "Actor": self.Actor.to_dict(),
            "Responses": [r.to_dict() for r in self.Responses],
            "AgentFacialExpression": self.AgentFacialExpression,
            **self._extra,
        }


@dataclass
class Scene:
    Id: int = 0
    Title: str = ""
    SceneIntroduction: str = ""
    Min: int = 0
    Interactions: list[Interaction] = field(default_factory=list)
    _extra: dict[str, Any] = field(default_factory=dict, repr=False)

    KNOWN: ClassVar[tuple[str, ...]] = (
        "Id", "Title", "SceneIntroduction", "Min", "Interactions",
    )

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Scene":
        knowns, extras = _split_known(d, cls.KNOWN)
        return cls(
            Id=knowns.get("Id", 0),
            Title=knowns.get("Title", ""),
            SceneIntroduction=knowns.get("SceneIntroduction", ""),
            Min=knowns.get("Min", 0),
            Interactions=[Interaction.from_dict(i) for i in knowns.get("Interactions") or []],
            _extra=extras,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "Id": self.Id,
            "Title": self.Title,
            "SceneIntroduction": self.SceneIntroduction,
            "Min": self.Min,
            "Interactions": [i.to_dict() for i in self.Interactions],
            **self._extra,
        }


@dataclass
class Chapter:
    Id: int = 0
    Name: str = ""
    Intro: str = ""
    Scenes: list[Scene] = field(default_factory=list)
    _extra: dict[str, Any] = field(default_factory=dict, repr=False)

    KNOWN: ClassVar[tuple[str, ...]] = ("Id", "Name", "Intro", "Scenes")

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Chapter":
        knowns, extras = _split_known(d, cls.KNOWN)
        return cls(
            Id=knowns.get("Id", 0),
            Name=knowns.get("Name", ""),
            Intro=knowns.get("Intro", ""),
            Scenes=[Scene.from_dict(s) for s in knowns.get("Scenes") or []],
            _extra=extras,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Intro": self.Intro,
            "Scenes": [s.to_dict() for s in self.Scenes],
            **self._extra,
        }
