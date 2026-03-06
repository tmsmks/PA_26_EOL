#!/usr/bin/env python3
"""
End of Life - graph_to_md.py
Génère output/graphes_end_of_life.md au format Mermaid.
"""
import os

from graph_builder import load_chapters, build_scene_graph

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "chapters", "Chapters_v3-4-c_emotional-illustration.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "graphes_end_of_life.md")

LABEL_MAX = 20


def _truncate(s: str, max_len: int) -> str:
    if not s:
        return ""
    s = str(s).strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


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


def scene_to_mermaid(chapter_id: int, chapter_name: str, scene: dict) -> str:
    """Produit le diagramme Mermaid pour une scène."""
    nodes, edges = [], []
    interactions = scene.get("Interactions", [])
    id_to_ia = {ia["Id"]: ia for ia in interactions}

    for ia in interactions:
        actor = (ia.get("Actor") or {}).get("Name", "")
        text = ia.get("Text", "") or ia.get("Name", "")
        label = _truncate(text, 45)
        label = _mermaid_escape(f"({actor}) {label}")
        nodes.append(f'    I{ia["Id"]}["{label}"]')

    for ia in interactions:
        for r in ia.get("Responses", []):
            next_id = r.get("NextInteractionID")
            if next_id is None or next_id == -1:
                continue
            if next_id not in id_to_ia:
                continue
            rlabel = _truncate(r.get("Name") or r.get("Text", ""), LABEL_MAX)
            rlabel = _mermaid_escape(rlabel)
            edges.append(f'    I{ia["Id"]} -->|"{rlabel}"| I{next_id}')

    lines = [
        "```mermaid",
        "flowchart TD",
        *nodes,
        "",
        *edges,
        "```",
        "",
        f"*{len(interactions)} nœuds, {len(edges)} arêtes*",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def main():
    data = load_chapters(DATA_PATH)
    parts = ["# Graphes End of Life", "", "Structure des scénarios — Généré à partir de Chapters_v3-4-c_emotional-illustration.json", "", "---", ""]

    for ch in data.get("Chapters", []):
        chapter_id = ch["Id"]
        chapter_name = ch.get("Name", "")
        parts.append(f"## Chapitre {chapter_id} : {chapter_name}")
        parts.append("")

        for scene in ch.get("Scenes", []):
            parts.append(f"### Scénario : {scene.get('Title', '')}")
            parts.append("")
            mermaid = scene_to_mermaid(chapter_id, chapter_name, scene)
            parts.append(mermaid)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"Généré : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
