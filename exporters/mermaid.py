"""Export Markdown au format Mermaid d'un livre.

Usage :
    python -m exporters.mermaid                 # livre par défaut
    python -m exporters.mermaid --book medstudents_y2
"""
from __future__ import annotations

import argparse
import os

from books import BOOKS_BY_SLUG, DEFAULT_BOOK_SLUG, get_book
from domain.models import Chapter, Scene
from repositories.chapters import ChapterRepository

LABEL_MAX = 20

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def _truncate(s: str, max_len: int) -> str:
    if not s:
        return ""
    s = str(s).strip()
    return s if len(s) <= max_len else s[: max_len - 1] + "…"


def _mermaid_escape(s: str) -> str:
    """Échappe les caractères spéciaux Mermaid."""
    if not s:
        return ""
    return (
        str(s)
        .replace('"', "#quot;")
        .replace("[", "(")
        .replace("]", ")")
        .replace("{", "(")
        .replace("}", ")")
    )


def scene_to_mermaid(scene: Scene) -> str:
    nodes: list[str] = []
    edges: list[str] = []
    id_to_ia = {ia.Id: ia for ia in scene.Interactions}

    for ia in scene.Interactions:
        actor = ia.Actor.Name or ""
        text = ia.Text or ia.Name or ""
        label = _mermaid_escape(f"({actor}) {_truncate(text, 45)}")
        nodes.append(f'    I{ia.Id}["{label}"]')

    for ia in scene.Interactions:
        for r in ia.Responses:
            nid = r.NextInteractionID
            if nid is None or nid == -1 or nid not in id_to_ia:
                continue
            rlabel = _mermaid_escape(_truncate(r.Name or r.Text, LABEL_MAX))
            edges.append(f'    I{ia.Id} -->|"{rlabel}"| I{nid}')

    return "\n".join([
        "```mermaid",
        "flowchart TD",
        *nodes,
        "",
        *edges,
        "```",
        "",
        f"*{len(scene.Interactions)} nœuds, {len(edges)} arêtes*",
        "",
        "---",
        "",
    ])


def export_book(book_slug: str) -> str:
    """Génère output/graphes_<slug>.md, retourne le chemin."""
    book = get_book(book_slug)
    chapters: list[Chapter] = ChapterRepository().load_chapters(book)

    parts = [
        f"# Graphes — {book['title']}",
        "",
        f"Structure des scénarios — Généré à partir de {book['json']}",
        "",
        "---",
        "",
    ]
    for ch in chapters:
        parts.append(f"## Chapitre {ch.Id} : {ch.Name}")
        parts.append("")
        for scene in ch.Scenes:
            parts.append(f"### Scénario : {scene.Title}")
            parts.append("")
            parts.append(scene_to_mermaid(scene))

    output_path = os.path.join(OUTPUT_DIR, f"graphes_{book['slug']}.md")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Mermaid d'un livre.")
    parser.add_argument(
        "--book",
        default=DEFAULT_BOOK_SLUG,
        choices=sorted(BOOKS_BY_SLUG.keys()),
        help="Slug du livre à exporter.",
    )
    args = parser.parse_args()
    out = export_book(args.book)
    print(f"Généré : {out}")


if __name__ == "__main__":
    main()
