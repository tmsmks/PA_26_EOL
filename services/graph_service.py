"""Construction du graphe d'une scène pour la visualisation et le parcours.

Pure logique métier : prend un Chapter typé, retourne un dict prêt à être
sérialisé en JSON pour le frontend (vis-network + parcours joueur).
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from domain.models import Chapter, Interaction, Response, Scene
from domain.soft_skills import SOFT_SKILLS

LABEL_MAX = 38


def _truncate(s: str, max_len: int) -> str:
    if not s:
        return ""
    s = str(s).strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _apply_edge_curves(edges: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Distribue les courbures pour éviter la superposition des arêtes.

    1) Sépare les arêtes parallèles (même from/to).
    2) Évente les autres arêtes sortantes par nœud source.
    """
    by_pair: dict[tuple[str, str], list] = defaultdict(list)
    for e in edges:
        by_pair[(e["from"], e["to"])].append(e)

    locked_ids: set[str] = set()
    for pair_edges in by_pair.values():
        n = len(pair_edges)
        if n <= 1:
            continue
        for i, e in enumerate(pair_edges):
            step = i // 2 + 1
            sign = -1 if i % 2 else 1
            roundness = min(1.0, 0.22 + (step - 1) * 0.11)
            curve_type = "curvedCW" if sign > 0 else "curvedCCW"
            e["smooth"] = {"type": curve_type, "roundness": roundness}
            locked_ids.add(e["id"])

    by_source: dict[str, list] = defaultdict(list)
    for e in edges:
        by_source[e["from"]].append(e)

    for out_edges in by_source.values():
        free_edges = [e for e in out_edges if e["id"] not in locked_ids]
        n = len(free_edges)
        if n == 0:
            continue
        max_roundness = min(0.65, 0.16 + 0.05 * n)
        for i, e in enumerate(free_edges):
            if n == 1:
                roundness = 0.0
            else:
                roundness = -max_roundness + (2 * max_roundness * i) / (n - 1)
            curve_type = "curvedCW" if roundness >= 0 else "curvedCCW"
            e["smooth"] = {"type": curve_type, "roundness": abs(roundness)}

    return edges


def _node_id(chapter_id: int, scene_id: int, interaction_id: int) -> str:
    return f"C{chapter_id}_S{scene_id}_I{interaction_id}"


def _edge_id(node_id: str, response_idx: int, target_node_id: str) -> str:
    return f"{node_id}_R{response_idx}_>{target_node_id}"


def _build_nodes_and_edges(
    chapter_id: int, scene: Scene
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    interactions = scene.Interactions
    id_to_interaction = {ia.Id: ia for ia in interactions}

    for ia in interactions:
        actor_name = ia.Actor.Name or "?"
        text = ia.Text
        name = ia.Name or text[:50]
        node_id = _node_id(chapter_id, scene.Id, ia.Id)
        base_label = _truncate(name or text or "—", LABEL_MAX)
        nodes.append({
            "id": node_id,
            "label": f"{ia.Id} — {base_label}",
            "title": f"[{actor_name}] {text}" if text else f"[{actor_name}] {name}",
            "interaction_id": str(ia.Id),
        })

        for r_idx, r in enumerate(ia.Responses):
            next_id = r.NextInteractionID
            if next_id is None or next_id == -1:
                continue
            if next_id not in id_to_interaction:
                continue
            target_node_id = _node_id(chapter_id, scene.Id, next_id)
            edge_id = _edge_id(node_id, r_idx, target_node_id)
            edge_title = f"Réponse {r_idx + 1}"
            r_text = (r.Text or "").strip()
            if r_text:
                edge_title += f" — {r_text}"
            edges.append({
                "id": edge_id,
                "from": node_id,
                "to": target_node_id,
                "label": f"R{r_idx + 1}",
                "title": edge_title,
            })

    targets = {e["to"] for e in edges}
    first_node_id = (
        _node_id(chapter_id, scene.Id, interactions[0].Id) if interactions else None
    )
    for n in nodes:
        if n["id"] not in targets and n["id"] != first_node_id:
            n["is_root"] = True

    return nodes, _apply_edge_curves(edges)


def _response_payload(r: Response) -> dict[str, Any]:
    """Sérialise une Response pour le mode parcours joueur (scores aplatis)."""
    return {
        "text": r.Text,
        "next_id": str(r.NextInteractionID) if r.NextInteractionID is not None else "-1",
        "RespectAndDignity": r.score("RespectAndDignity"),
        "Empathy": r.score("Empathy"),
        "Compassion": r.score("Compassion"),
        "EmotionalRegulation": r.score("EmotionalRegulation"),
        "CommunicationClarity": r.score("CommunicationClarity"),
        "ProfessionalBoundaries": r.score("ProfessionalBoundaries"),
        "InterprofessionalCollaboration": r.score("InterprofessionalCollaboration"),
    }


def _build_parcours(
    chapter_id: int, scene: Scene
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    """Construit la liste ordonnée et la map id->entry du parcours joueur."""
    interactions = scene.Interactions
    id_to_ia = {ia.Id: ia for ia in interactions}

    starts: set[int] = {ia.Id for ia in interactions}
    for ia in interactions:
        for r in ia.Responses:
            nid = r.NextInteractionID
            if nid is not None and nid != -1:
                starts.discard(nid)
    if not starts and interactions:
        starts = {interactions[0].Id}

    parcours: list[dict[str, Any]] = []
    visited: set[int] = set()

    def add_entry(ia_id: int) -> None:
        if ia_id in visited:
            return
        visited.add(ia_id)
        ia = id_to_ia.get(ia_id)
        if not ia:
            return
        node_id = _node_id(chapter_id, scene.Id, ia.Id)
        responses = []
        for r_idx, r in enumerate(ia.Responses):
            payload = _response_payload(r)
            next_id = r.NextInteractionID
            if next_id is not None and next_id != -1:
                target_node_id = _node_id(chapter_id, scene.Id, next_id)
                payload["target_node_id"] = target_node_id
                payload["edge_id"] = _edge_id(node_id, r_idx, target_node_id)
            else:
                payload["target_node_id"] = ""
                payload["edge_id"] = ""
            responses.append(payload)
        parcours.append({
            "node_id": node_id,
            "actor": ia.Actor.Name,
            "text": ia.Text,
            "image": ia.AgentFacialExpression,
            "responses": responses,
        })
        for r in ia.Responses:
            nid = r.NextInteractionID
            if nid is not None and nid != -1 and nid not in visited:
                add_entry(nid)

    for start_id in sorted(starts):
        add_entry(start_id)
    for ia in interactions:
        if ia.Id not in visited:
            add_entry(ia.Id)

    id_to_parcours = {
        entry["node_id"].split("_I")[-1]: entry for entry in parcours
    }
    return parcours, id_to_parcours


def build_scene_graph(chapter_id: int, scene: Scene) -> dict[str, Any]:
    """Construit le payload complet d'une scène pour le frontend.

    Retourne :
      - title, scene_id, scene_intro
      - nodes, edges (vis-network)
      - parcours, id_to_parcours (mode parcours joueur)
    """
    nodes, edges = _build_nodes_and_edges(chapter_id, scene)
    parcours, id_to_parcours = _build_parcours(chapter_id, scene)
    return {
        "title": scene.Title,
        "scene_id": scene.Id,
        "scene_intro": scene.SceneIntroduction,
        "nodes": nodes,
        "edges": edges,
        "parcours": parcours,
        "id_to_parcours": id_to_parcours,
    }


def build_all_scenes(chapter: Chapter) -> list[dict[str, Any]]:
    """Construit le payload de toutes les scènes d'un chapitre."""
    return [build_scene_graph(chapter.Id, scene) for scene in chapter.Scenes]


__all__ = ["SOFT_SKILLS", "build_scene_graph", "build_all_scenes"]
