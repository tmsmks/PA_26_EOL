#!/usr/bin/env python3
"""
End of Life - graph_builder.py
Charge Chapters_v3-4-c_emotional-illustration.json, construit les nœuds et arêtes pour la visualisation.
EG-7 : NextInteractionID -1 = fin de branche (valide).
"""
import json
import os
from collections import defaultdict

LABEL_MAX = 38
# Dimensions principales (v3) : au niveau des réponses
SKILLS = [
    "RespectAndDignity",
    "Empathy",
    "Compassion",
    "EmotionalRegulation",
    "CommunicationClarity",
    "ProfessionalBoundaries",
    "InterprofessionalCollaboration",
]


def _get_score(r: dict, skill: str) -> int:
    """Lit un score depuis la réponse (dimensions v3 : SoftSkillDimensions ou champs plats)."""
    soft = r.get("SoftSkillDimensions") or {}
    return soft.get(skill, r.get(skill, 0))


def load_chapters(json_path: str) -> dict:
    """Charge le fichier JSON des chapitres."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _truncate(s: str, max_len: int) -> str:
    if not s:
        return ""
    s = str(s).strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _escape_html(s: str) -> str:
    if not s:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _apply_edge_curves(edges: list) -> list:
    """
    Répartit les courbures des arêtes pour éviter la superposition.
    Pour chaque nœud source avec N arêtes sortantes, répartit roundness de -max à +max.
    """
    by_source: dict[str, list] = defaultdict(list)
    for e in edges:
        by_source[e["from"]].append(e)

    for source, out_edges in by_source.items():
        n = len(out_edges)
        max_roundness = min(1.0, 0.35 + 0.06 * n)  # plus de flèches = courbure plus forte
        for i, e in enumerate(out_edges):
            if n == 1:
                roundness = 0
            else:
                roundness = -max_roundness + (2 * max_roundness * i) / (n - 1)
            e["smooth"] = {"type": "curvedCW", "roundness": roundness}

    return edges


def build_scene_graph(chapter_id: int, scene: dict) -> dict:
    """
    Construit les nœuds, arêtes et structures pour une scène.
    Retourne : nodes, edges, editor (HTML), parcours, id_to_parcours.
    """
    nodes = []
    edges = []
    interactions = scene.get("Interactions", [])
    id_to_interaction = {ia["Id"]: ia for ia in interactions}
    scene_intro = scene.get("SceneIntroduction", "")

    for ia in interactions:
        actor_name = (ia.get("Actor") or {}).get("Name", "?")
        text = ia.get("Text", "")
        name = ia.get("Name", text[:50])
        node_id = f"C{chapter_id}_S{scene['Id']}_I{ia['Id']}"
        label = _truncate(name or text or "—", LABEL_MAX)
        title = f"[{actor_name}] {text}" if text else f"[{actor_name}] {name}"

        nodes.append({"id": node_id, "label": label, "title": title})

        for r_idx, r in enumerate(ia.get("Responses", [])):
            next_id = r.get("NextInteractionID")
            if next_id is None:
                continue
            if next_id == -1:
                continue
            target = id_to_interaction.get(next_id)
            if not target:
                continue
            target_node_id = f"C{chapter_id}_S{scene['Id']}_I{next_id}"
            edge_id = f"{node_id}_R{r_idx}_>{target_node_id}"
            edges.append({
                "id": edge_id,
                "from": node_id,
                "to": target_node_id,
            })

    # Distribution des courbures : évite la superposition des flèches multiples
    edges = _apply_edge_curves(edges)

    editor_html = _build_editor_html(scene)

    parcours, id_to_parcours = _build_parcours(
        chapter_id, scene, nodes, edges
    )

    return {
        "title": scene.get("Title", ""),
        "scene_id": scene.get("Id"),
        "scene_intro": scene_intro,
        "nodes": nodes,
        "edges": edges,
        "editor": editor_html,
        "parcours": parcours,
        "id_to_parcours": id_to_parcours,
    }


def _build_editor_html(scene: dict) -> str:
    """Génère le HTML du panneau d'édition (EG-4)."""
    parts = []
    for i, ia in enumerate(scene.get("Interactions", [])):
        actor = (ia.get("Actor") or {}).get("Name", "")
        text = ia.get("Text", "")
        name = ia.get("Name", text[:50])
        block = f'<div class="block" data-interaction-id="{ia["Id"]}">'
        block += f'<div class="header">Interaction {ia["Id"]} — {_escape_html(actor)}</div>'
        block += '<label>EG-4 : Name</label>'
        block += f'<textarea class="edit" data-type="name" data-i="{i}" rows="1">{_escape_html(name or "")}</textarea>'
        block += '<label>EG-4 : Text</label>'
        block += f'<textarea class="edit" data-type="text" data-i="{i}" rows="3">{_escape_html(text or "")}</textarea>'
        for r_idx, r in enumerate(ia.get("Responses", [])):
            rtext = r.get("Text", "")
            block += f'<div class="resp"><label>Réponse {r_idx + 1} — Text</label>'
            block += f'<textarea class="edit" data-type="response" data-i="{i}" data-r="{r_idx}" rows="2">{_escape_html(rtext)}</textarea>'
            block += '<div class="scores">'
            for sk in SKILLS:
                val = _get_score(r, sk)
                block += (
                    f'<div class="score-item">'
                    f'<label>{sk}</label>'
                    f'<input type="number" class="score" data-i="{i}" data-r="{r_idx}" '
                    f'data-skill="{sk}" value="{val}" min="-3" max="3"></div>'
                )
            block += "</div></div>"
        block += "</div>"
        parts.append(block)
    return "".join(parts)


def _build_parcours(
    chapter_id: int, scene: dict, nodes: list, edges: list
) -> tuple:
    """
    Construit la structure parcours joueur : liste ordonnée et map id -> entry.
    Entry : { node_id, actor, text, responses: [{ next_id, target_node_id, edge_id, RespectAndDignity, ... }] }
    """
    interactions = scene.get("Interactions", [])
    id_to_ia = {ia["Id"]: ia for ia in interactions}
    edge_by_id = {e["id"]: e for e in edges}

    starts = set(ia["Id"] for ia in interactions)
    for ia in interactions:
        for r in ia.get("Responses", []):
            nid = r.get("NextInteractionID")
            if nid is not None and nid != -1:
                starts.discard(nid)

    if not starts:
        starts = {interactions[0]["Id"]} if interactions else set()

    parcours = []
    id_to_parcours = {}
    visited = set()

    def add_entry(ia_id: int):
        if ia_id in visited:
            return
        visited.add(ia_id)
        ia = id_to_ia.get(ia_id)
        if not ia:
            return
        actor = (ia.get("Actor") or {}).get("Name", "")
        text = ia.get("Text", "")
        node_id = f"C{chapter_id}_S{scene['Id']}_I{ia['Id']}"
        responses = []
        for r_idx, r in enumerate(ia.get("Responses", [])):
            next_id = r.get("NextInteractionID")
            target_node_id = ""
            edge_id = ""
            if next_id is not None and next_id != -1:
                target_node_id = f"C{chapter_id}_S{scene['Id']}_I{next_id}"
                edge_id = f"{node_id}_R{r_idx}_>{target_node_id}"
            responses.append({
                "text": r.get("Text", ""),
                "next_id": str(next_id) if next_id is not None else "-1",
                "target_node_id": target_node_id,
                "edge_id": edge_id,
                "RespectAndDignity": _get_score(r, "RespectAndDignity"),
                "Empathy": _get_score(r, "Empathy"),
                "Compassion": _get_score(r, "Compassion"),
                "EmotionalRegulation": _get_score(r, "EmotionalRegulation"),
                "CommunicationClarity": _get_score(r, "CommunicationClarity"),
                "ProfessionalBoundaries": _get_score(r, "ProfessionalBoundaries"),
                "InterprofessionalCollaboration": _get_score(r, "InterprofessionalCollaboration"),
            })
        entry = {
            "node_id": node_id,
            "actor": actor,
            "text": text,
            "image": ia.get("AgentFacialExpression") or "",
            "responses": responses,
        }
        parcours.append(entry)
        id_to_parcours[str(ia_id)] = entry
        for r in ia.get("Responses", []):
            nid = r.get("NextInteractionID")
            if nid is not None and nid != -1 and nid not in visited:
                add_entry(nid)

    for start_id in sorted(starts):
        add_entry(start_id)

    for ia in interactions:
        if ia["Id"] not in visited:
            add_entry(ia["Id"])

    id_to_parcours_final = {}
    for entry in parcours:
        ia_id = entry["node_id"].split("_I")[-1]
        id_to_parcours_final[ia_id] = entry

    for ia in interactions:
        sid = str(ia["Id"])
        if sid not in id_to_parcours_final:
            actor = (ia.get("Actor") or {}).get("Name", "")
            node_id = f"C{chapter_id}_S{scene['Id']}_I{ia['Id']}"
            responses = []
            for r_idx, r in enumerate(ia.get("Responses", [])):
                next_id = r.get("NextInteractionID")
                target_node_id = f"C{chapter_id}_S{scene['Id']}_I{next_id}" if next_id not in (None, -1) else ""
                edge_id = f"{node_id}_R{r_idx}_>{target_node_id}" if next_id not in (None, -1) else ""
                responses.append({
                    "text": r.get("Text", ""),
                    "next_id": str(next_id) if next_id is not None else "-1",
                    "target_node_id": target_node_id,
                    "edge_id": edge_id,
                    "RespectAndDignity": _get_score(r, "RespectAndDignity"),
                    "Empathy": _get_score(r, "Empathy"),
                    "Compassion": _get_score(r, "Compassion"),
                    "EmotionalRegulation": _get_score(r, "EmotionalRegulation"),
                    "CommunicationClarity": _get_score(r, "CommunicationClarity"),
                    "ProfessionalBoundaries": _get_score(r, "ProfessionalBoundaries"),
                    "InterprofessionalCollaboration": _get_score(r, "InterprofessionalCollaboration"),
                })
            entry = {
                "node_id": node_id,
                "actor": actor,
                "text": ia.get("Text", ""),
                "image": ia.get("AgentFacialExpression") or "",
                "responses": responses,
            }
            id_to_parcours_final[sid] = entry

    return parcours, id_to_parcours_final


def build_all_chapters(json_path: str) -> list:
    """Construit les graphes pour tous les chapitres."""
    data = load_chapters(json_path)
    result = []
    for ch in data.get("Chapters", []):
        chapter_id = ch["Id"]
        for scene in ch.get("Scenes", []):
            scene_data = build_scene_graph(chapter_id, scene)
            scene_data["chapter_name"] = ch.get("Name", "")
            scene_data["chapter_id"] = chapter_id
            result.append((ch, scene_data))
    return result


def validate_next_interaction_ids(json_path: str) -> list:
    """EG-7 : Vérifie que tous les NextInteractionID pointent vers des Id valides ou -1."""
    data = load_chapters(json_path)
    errors = []
    for ch in data.get("Chapters", []):
        for scene in ch.get("Scenes", []):
            ids = {ia["Id"]: True for ia in scene.get("Interactions", [])}
            for ia in scene.get("Interactions", []):
                for r in ia.get("Responses", []):
                    nid = r.get("NextInteractionID")
                    if nid is not None and nid != -1 and nid not in ids:
                        errors.append(
                            f"EG-7: NextInteractionID {nid} invalide (scène {scene.get('Title', '?')})"
                        )
    return errors


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, "data", "chapters", "Chapters_v3-4-c_emotional-illustration.json")
    errors = validate_next_interaction_ids(path)
    if errors:
        for e in errors:
            print(e)
    else:
        print("EG-7 : Validation OK — NextInteractionID valides.")
    built = build_all_chapters(path)
    print(f"Chapitres/scènes traités : {len(built)}")
