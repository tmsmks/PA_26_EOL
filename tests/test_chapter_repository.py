"""Tests du repository (load + écriture atomique + archivage horodaté)."""
import json
import os
import re
import shutil
import tempfile

import pytest

from books import get_book
from domain.models import Chapter, Scene
from repositories.chapters import HISTORY_DIRNAME, ChapterRepository

# Fichier JSON du livre utilisé comme données de test (celui que books.py désigne).
Y2_JSON = get_book("medstudents_y2")["json"]
Y2_STEM = os.path.splitext(Y2_JSON)[0]


@pytest.fixture()
def tmp_book_dir(tmp_path):
    """Crée un répertoire temporaire avec un JSON copié depuis le livre réel."""
    src = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data", "chapters", Y2_JSON,
    )
    dst = tmp_path / Y2_JSON
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
    json_path = os.path.join(tmp_book_dir, Y2_JSON)
    original = open(json_path, "r", encoding="utf-8").read()

    def boom(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr(os, "replace", boom)

    chapters = repo.load_chapters("medstudents_y2")
    chapters[0].Name = "Should not be persisted"
    with pytest.raises(OSError):
        repo.upsert_chapter("medstudents_y2", chapters[0])

    assert open(json_path, "r", encoding="utf-8").read() == original


def test_upsert_archives_previous_version(tmp_book_dir):
    """Avant d'écraser le JSON principal, l'ancienne version est copiée
    dans `history/` avec un nom horodaté, et le contenu est identique."""
    repo = ChapterRepository(base_dir=tmp_book_dir)
    json_path = os.path.join(tmp_book_dir, Y2_JSON)
    original_content = open(json_path, "r", encoding="utf-8").read()

    chapters = repo.load_chapters("medstudents_y2")
    chapters[0].Name = "Renommé pour archivage"
    result = repo.upsert_chapter("medstudents_y2", chapters[0])

    assert isinstance(result, dict)
    assert result["filename"] == Y2_JSON
    assert result["archive"] is not None

    history_dir = os.path.join(tmp_book_dir, HISTORY_DIRNAME)
    assert os.path.isdir(history_dir)
    archive_path = os.path.join(history_dir, result["archive"])
    assert os.path.isfile(archive_path)
    assert open(archive_path, "r", encoding="utf-8").read() == original_content

    pattern = rf"^{Y2_STEM}_\d{{2}}-\d{{2}}-\d{{2}}\.json$"
    assert re.match(pattern, result["archive"]), result["archive"]


def test_upsert_first_time_no_archive(tmp_path):
    """Si le fichier principal n'existe pas encore, aucune archive n'est créée."""
    src = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data", "chapters", Y2_JSON,
    )
    shutil.copy2(src, tmp_path / Y2_JSON)
    fresh_dir = tmp_path / "fresh"
    fresh_dir.mkdir()
    repo = ChapterRepository(base_dir=str(fresh_dir))

    new_chapter = Chapter(Id=1, Name="Premier", Scenes=[])
    result = repo.upsert_chapter("medstudents_y2", new_chapter)

    assert result["archive"] is None
    assert not (fresh_dir / HISTORY_DIRNAME).exists()
