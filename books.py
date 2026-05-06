#!/usr/bin/env python3
"""
End of Life - books.py
Source de vérité unique des livres (scénarios pédagogiques).

Tout module qui a besoin de connaître la liste des livres, leur slug, leur
fichier JSON ou leur chemin absolu doit importer depuis ce module et
NULLE PART AILLEURS. Ajouter un livre = éditer ce fichier uniquement.
"""
from __future__ import annotations

import os
from typing import TypedDict


class Book(TypedDict):
    slug: str
    title: str
    subtitle: str
    description: str
    audience: str
    json: str


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(BASE_DIR, "data", "chapters")


BOOKS: list[Book] = [
    {
        "slug": "end_of_life",
        "title": "End of Life",
        "subtitle": "Communication en fin de vie — EMS",
        "description": (
            "Le livre historique du projet. Le joueur incarne Claude, "
            "infirmier·ère en EMS, confronté·e à des situations de fin de "
            "vie : rencontre, deuil, représentations collectives, "
            "accompagnement des proches. Destiné aux professionnel·le·s "
            "soignant·e·s en formation continue."
        ),
        "audience": "Soignant·e·s en formation continue",
        "json": "Chapters_v3-4-c_emotional-illustration.json",
    },
    {
        "slug": "medstudents_y2",
        "title": "MedStudents Y2",
        "subtitle": "Scénarios pédagogiques — 2ᵉ année de médecine",
        "description": (
            "Un livre conçu pour les étudiant·e·s en 2ᵉ année de médecine. "
            "Le joueur incarne Alex, en stage d'immersion hospitalière, et "
            "travaille les compétences communicationnelles et éthiques "
            "fondamentales du cursus pré-clinique (anamnèse, consentement, "
            "secret médical)."
        ),
        "audience": "Étudiant·e·s en 2ᵉ année de médecine",
        "json": "MedStudents_Y2_v1.json",
    },
]

DEFAULT_BOOK_SLUG: str = BOOKS[0]["slug"]

BOOKS_BY_SLUG: dict[str, Book] = {b["slug"]: b for b in BOOKS}


def get_book(slug: str | None) -> Book:
    """Retourne le livre correspondant au slug (ou le livre par défaut si None).

    Lève ValueError si le slug est inconnu.
    """
    effective = (slug or DEFAULT_BOOK_SLUG).strip()
    book = BOOKS_BY_SLUG.get(effective)
    if book is None:
        raise ValueError(
            f"book_slug inconnu : '{effective}'. Valeurs possibles : "
            f"{', '.join(BOOKS_BY_SLUG)}."
        )
    return book


def default_book() -> Book:
    """Livre par défaut (premier de la liste)."""
    return BOOKS_BY_SLUG[DEFAULT_BOOK_SLUG]


def chapters_path(book_or_slug: Book | str | None) -> str:
    """Chemin absolu vers le fichier JSON d'un livre.

    Accepte un slug, un dict Book, ou None (= livre par défaut).
    """
    if isinstance(book_or_slug, dict):
        book: Book = book_or_slug  # type: ignore[assignment]
    else:
        book = get_book(book_or_slug)
    return os.path.join(CHAPTERS_DIR, book["json"])
