"""Tests du repository (load + écriture atomique)."""
import json
import os
import shutil
import tempfile

import pytest

from domain.models import Chapter, Scene
from repositories.chapters import ChapterRepository


@pytest.fixture()
def tmp_book_dir(tmp_path):
    """Crée un répertoire temporaire avec un JSON copié depuis le livre réel."""
    src = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data", "chapters", "MedStudents_Y2_v1.json",
    )
    dst = tmp_path / "MedStudents_Y2_v1.json"
    shutil.copy2(src, dst)
    return str(tmp_path)


def test_load_chapters_returns_typed_chapters(tmp_book_dir):
    repo = ChapterRepository(base_dir=tmp_book_dir)
    chapters = repo.load_chapters("medstudents_y2")
    assert all(isinstance(c, Chapter) for c in chapters)
    assert len(chapters) > 0


def test_upsert_chapter_writes_atomically(tmp_book_dir):
    repo = ChapterRepository(base_dir=tmp_book_dir)
    chapters = repo.load_chapters("medstudents_y2")
    target = chapters[0]
    target.Name = "Renommé en test"
    repo.upsert_chapter("medstudents_y2", target)

    reloaded = repo.load_chapters("medstudents_y2")
    assert reloaded[0].Name == "Renommé en test"


def test_upsert_chapter_appends_when_missing(tmp_book_dir):
    repo = ChapterRepository(base_dir=tmp_book_dir)
    new_chapter = Chapter(Id=999, Name="Nouveau chapitre de test", Scenes=[])
    repo.upsert_chapter("medstudents_y2", new_chapter)

    reloaded = repo.load_chapters("medstudents_y2")
    assert any(c.Id == 999 for c in reloaded)


def test_upsert_no_partial_write_on_failure(tmp_book_dir, monkeypatch):
    """Si l'écriture échoue, le fichier original ne doit pas être tronqué."""
    repo = ChapterRepository(base_dir=tmp_book_dir)
    json_path = os.path.join(tmp_book_dir, "MedStudents_Y2_v1.json")
    original = open(json_path, "r", encoding="utf-8").read()

    def boom(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr(os, "replace", boom)

    chapters = repo.load_chapters("medstudents_y2")
    chapters[0].Name = "Should not be persisted"
    with pytest.raises(OSError):
        repo.upsert_chapter("medstudents_y2", chapters[0])

    assert open(json_path, "r", encoding="utf-8").read() == original
