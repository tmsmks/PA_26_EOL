"""Clé de cotation du livre, appliquée par-dessus les scores écrits dans les chapitres.

Les scores des sources (`R(..., "rd3 cc2")` dans ch1…ch5) sont la clé de
l'auteur. La clé en vigueur est `data/keys/MedStudents_Y2_v2_cle.json` : chaque
réponse d'un point de choix y a ses cotes, son drapeau « critique » et sa
justification d'une phrase, avec, pour la traçabilité, la cote de l'auteur et
celle du premier tour (méthode : docs/MedStudents_Y2_v2_cle.md).

Une réponse est repérée par `c{chapitre}-s{scène}-i{interaction}-r{rang}`, le
rang commençant à 1 dans l'ordre du livre (comme `services.expert_key_service`).
Le début du texte est vérifié : si une réponse a été ajoutée, retirée ou
réécrite depuis la cotation, le build s'arrête au lieu d'appliquer une cote à
la mauvaise réponse.
"""
from __future__ import annotations

import json
import os
from typing import Any

from .dsl import C

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KEY_PATH = os.path.join(ROOT, "data", "keys", "MedStudents_Y2_v2_cle.json")


class KeyMismatch(ValueError):
    """La clé ne correspond plus aux réponses du livre."""


def load_key(path: str = KEY_PATH) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def apply_key(chapters: list[C], key: dict[str, Any] | None = None) -> list[C]:
    """Remplace les scores des réponses des points de choix par ceux de la clé."""
    items = (key or load_key())["reponses"]
    seen: set[str] = set()
    problems: list[str] = []
    for ch in chapters:
        for sc in ch.scenes:
            for node in sc.nodes:
                if len(node.responses) < 2:
                    continue
                for no, r in enumerate(node.responses, start=1):
                    ref = f"c{ch.id}-s{sc.id}-i{node.id}-r{no}"
                    item = items.get(ref)
                    if item is None:
                        problems.append(f"{ref} : réponse absente de la clé")
                        continue
                    if not r.text.startswith(item["texte"]):
                        problems.append(f"{ref} : le texte a changé depuis la cotation")
                        continue
                    seen.add(ref)
                    r.scores = item["cotes"]
                    r.critical = bool(item["critique"])
                    r.rationale = item["justification"]
    problems += [f"{ref} : n'existe plus dans le livre" for ref in sorted(set(items) - seen)
                 if not any(p.startswith(ref) for p in problems)]
    if problems:
        raise KeyMismatch("Clé de cotation à mettre à jour :\n  " + "\n  ".join(problems))
    return chapters
