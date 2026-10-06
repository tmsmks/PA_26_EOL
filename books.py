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
        "json": "chapter.json",
    },
    {
        "slug": "medstudents_y2",
        "title": "MedStudents Y2",
        "subtitle": "Le corps donné — 2ᵉ année de Bachelor",
        "description": (
            "Un livre conçu pour les étudiant·e·s en 2ᵉ année de médecine "
            "(UNIL BMed2, UNIGE 2ᵉ Bachelor, UZH 2. Studienjahr). Une année "
            "d'Alex, de la salle de dissection au cabinet de médecine de "
            "famille de Montchéry : « Madame 14 », la donneuse de la table "
            "14 ; Jeannine Pittet, 81 ans, ancienne sage-femme, qui a donné "
            "son corps à la faculté sans le dire à son fils ; la table 14 et "
            "ses fêlures. Des branches parallèles, des histoires annexes, et "
            "des choix qui ont une mémoire d'un chapitre à l'autre."
        ),
        "audience": "Étudiant·e·s en 2ᵉ année de médecine (UNIL, UNIGE, UZH)",
        "json": "MedStudents_Y2_v2.json",
    },
    {
        "slug": "medstudents_y4",
        "title": "MedStudents Y4",
        "subtitle": "Six semaines au 3ᵉ étage — 1ʳᵉ année de Master",
        "description": (
            "Un livre conçu pour les étudiant·e·s en 1ʳᵉ année de Master de "
            "médecine (UNIL M1 / UNIGE M1). Six semaines de stage d'Alex en "
            "médecine interne, avec toujours la même équipe — médecin-chef, "
            "assistant, infirmières, ASSC, co-stagiaire. Première annonce "
            "grave, pacte de silence familial, incertitude diagnostique, fin "
            "de vie d'un patient suivi depuis le premier jour, puis une nuit "
            "de garde où une allergie non transmise peut tuer — et tout ce qui "
            "s'ensuit : famille, avocate, revue d'incident. Les choix ont une "
            "mémoire d'un chapitre à l'autre."
        ),
        "audience": "Étudiant·e·s en 1ʳᵉ année de Master de médecine (UNIL M1 / UNIGE M1)",
        "json": "MedStudents_Y4_v2.json",
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
