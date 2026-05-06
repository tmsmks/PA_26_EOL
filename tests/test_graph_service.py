"""Tests du service de construction du graphe."""
from domain.models import Actor, Chapter, Interaction, Response, Scene
from services.graph_service import build_scene_graph


def _scene() -> Scene:
    """Petite scène : 1 -> 2 -> -1, 1 -> 3, 3 -> -1."""
    return Scene(
        Id=1,
        Title="Test",
        Interactions=[
            Interaction(
                Id=1,
                Name="Intro",
                Text="Bonjour",
                Actor=Actor(Name="Claude"),
                Responses=[
                    Response(Id=1, Text="r1", NextInteractionID=2),
                    Response(Id=2, Text="r2", NextInteractionID=3),
                ],
            ),
            Interaction(Id=2, Responses=[Response(Id=1, NextInteractionID=-1)]),
            Interaction(Id=3, Responses=[Response(Id=1, NextInteractionID=-1)]),
        ],
    )


def test_build_scene_graph_node_count_and_root_marking():
    sd = build_scene_graph(chapter_id=1, scene=_scene())
    assert len(sd["nodes"]) == 3
    # Aucun nœud n'est root (la 1ère interaction est le démarrage)
    roots = [n for n in sd["nodes"] if n.get("is_root")]
    assert roots == []


def test_build_scene_graph_edges_and_curves():
    sd = build_scene_graph(chapter_id=1, scene=_scene())
    edges = sd["edges"]
    assert len(edges) == 2
    for e in edges:
        assert "smooth" in e and "type" in e["smooth"]


def test_build_scene_graph_response_with_invalid_next_id_is_skipped():
    scene = Scene(Id=1, Title="t", Interactions=[
        Interaction(Id=1, Responses=[Response(Id=1, NextInteractionID=99)])
    ])
    sd = build_scene_graph(1, scene)
    assert sd["edges"] == []


def test_parcours_lists_all_interactions_once():
    sd = build_scene_graph(1, _scene())
    ids = sorted(int(entry["node_id"].split("_I")[-1]) for entry in sd["parcours"])
    assert ids == [1, 2, 3]


def test_parcours_response_payload_includes_target_and_edge_for_valid_next():
    sd = build_scene_graph(1, _scene())
    first = sd["parcours"][0]
    assert first["responses"][0]["next_id"] == "2"
    assert first["responses"][0]["target_node_id"] == "C1_S1_I2"
    assert "_R0_>" in first["responses"][0]["edge_id"]
