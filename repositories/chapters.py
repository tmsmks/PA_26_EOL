"""Repository des chapitres — persistance JSON avec écriture atomique.

Pattern Repository : encapsule TOUT accès aux fichiers JSON. Le reste du code
(services, vues) ignore qu'il s'agit de fichiers ; il pourrait être remplacé
par une base de données sans changer une ligne ailleurs.
"""
from __future__ import annotations

import json
import os
import tempfile

from books import Book, chapters_path, get_book
from domain.models import Chapter


class ChapterRepository:
    """Accès lecture/écriture aux livres (JSON)."""

    def __init__(self, base_dir: str | None = None) -> None:
        # `base_dir` permet de pointer vers un autre répertoire en test.
        # Si None, on utilise les chemins définis dans `books.py`.
        self._base_dir = base_dir

    def _path_for(self, book_or_slug: Book | str | None) -> str:
        path = chapters_path(book_or_slug)
        if self._base_dir is None:
            return path
        return os.path.join(self._base_dir, os.path.basename(path))

    def load_raw(self, book_or_slug: Book | str | None) -> dict:
        """Charge le JSON brut d'un livre."""
        path = self._path_for(book_or_slug)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_chapters(self, book_or_slug: Book | str | None) -> list[Chapter]:
        """Charge tous les chapitres typés d'un livre."""
        raw = self.load_raw(book_or_slug)
        return [Chapter.from_dict(ch) for ch in raw.get("Chapters", [])]

    def find_chapter(
        self, book_or_slug: Book | str | None, chapter_id: int
    ) -> Chapter | None:
        """Retourne le chapitre d'Id donné ou None."""
        for ch in self.load_chapters(book_or_slug):
            if ch.Id == chapter_id:
                return ch
        return None

    def upsert_chapter(
        self, book_slug: str | None, chapter: Chapter | dict
    ) -> str:
        """Insère ou met à jour un chapitre, écriture atomique.

        Returns: le nom du fichier JSON modifié.
        """
        book = get_book(book_slug)
        path = self._path_for(book)

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                full = json.load(f)
        else:
            full = {"Chapters": []}

        ch_dict = chapter.to_dict() if isinstance(chapter, Chapter) else dict(chapter)
        ch_id = ch_dict.get("Id")

        chapters_list = full.setdefault("Chapters", [])
        for i, existing in enumerate(chapters_list):
            if existing.get("Id") == ch_id:
                chapters_list[i] = ch_dict
                break
        else:
            chapters_list.append(ch_dict)

        self._atomic_write_json(path, full)
        return os.path.basename(path)

    @staticmethod
    def _atomic_write_json(path: str, data: dict) -> None:
        """Écriture atomique : write-then-rename via os.replace (POSIX atomic)."""
        directory = os.path.dirname(path) or "."
        os.makedirs(directory, exist_ok=True)
        fd, tmp = tempfile.mkstemp(
            prefix=os.path.basename(path) + ".",
            suffix=".tmp",
            dir=directory,
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, path)
        except Exception:
            try:
                os.unlink(tmp)
            except OSError:
                pass
            raise
