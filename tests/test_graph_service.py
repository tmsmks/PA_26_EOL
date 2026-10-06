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


# --- États narratifs ----------------------------------------------------------

def _branching_scene() -> Scene:
    """1 -> 2 (pose « a »), entrée alternative 3 si « a », scène conditionnelle."""
    return Scene.from_dict({
        "Id": 2,
        "Title": "5.4 Test",
        "Slot": "5.4",
        "Condition": {"all": ["erreur"], "any": [], "none": []},
        "EntryPoints": [{"Condition": {"all": ["a"]}, "InteractionId": 3, "Intro": "Variante"}],
        "Debriefs": [{"Condition": {"all": ["deces"]}, "Tone": "hard", "Lead": "Issue grave"}],
        "SoftSkillFocus": ["ProfessionalBoundaries"],
        "Interactions": [
            {"Id": 1, "Responses": [
                {"Id": 1, "NextInteractionID": 2, "SetFlags": ["a"], "ClearFlags": ["b"]},
            ]},
            {"Id": 2, "Responses": [{"Id": 1, "NextInteractionID": -1}]},
            {"Id": 3, "Responses": [{"Id": 1, "NextInteractionID": -1}]},
        ],
    })


def test_response_payload_carries_flags():
    sd = build_scene_graph(5, _branching_scene())
    first = sd["id_to_parcours"]["1"]["responses"][0]
    assert first["set_flags"] == ["a"]
    assert first["clear_flags"] == ["b"]
    assert sd["id_to_parcours"]["2"]["responses"][0]["set_flags"] == []


def test_scene_payload_carries_condition_entries_and_debriefs():
    sd = build_scene_graph(5, _branching_scene())
    assert sd["condition"] == {"all": ["erreur"]}
    assert sd["entry_points"] == [
        {"condition": {"all": ["a"]}, "interaction_id": "3", "intro": "Variante"}
    ]
    assert sd["default_entry"] == "1"
    assert sd["slot"] == "5.4"
    assert sd["focus"] == ["ProfessionalBoundaries"]
    assert sd["debriefs"] == [{"condition": {"all": ["deces"]}, "tone": "hard", "lead": "Issue grave"}]


def test_entry_point_is_not_marked_as_orphan_root():
    sd = build_scene_graph(5, _branching_scene())
    node3 = next(n for n in sd["nodes"] if n["interaction_id"] == "3")
    assert node3.get("is_entry") is True
    assert "is_root" not in node3


def test_scene_without_narrative_fields_has_neutral_defaults():
    sd = build_scene_graph(1, _scene())
    assert sd["condition"] == {}
    assert sd["entry_points"] == []
    assert sd["slot"] == "#1"
    assert sd["debriefs"] == []


def test_chapter_outline_counts_alternative_scenes_once():
    from services.graph_service import chapter_outline

    def scene(sid: int, slot: str, minutes: int) -> Scene:
        return Scene.from_dict({"Id": sid, "Slot": slot, "Min": minutes, "Interactions": []})

    ch = Chapter(Id=5, Scenes=[scene(1, "5.1", 8), scene(2, "5.2", 6), scene(3, "5.2", 9)])
    assert chapter_outline(ch) == {"n_scenes": 2, "minutes": 17}


def test_chapter_meta_lists_owned_flags_and_start_choice():
    from services.graph_service import chapter_meta

    ch = Chapter.from_dict({
        "Id": 6,
        "StartChoice": {
            "UnlessAny": ["erreur", "evite"],
            "Question": "Quelle nuit ?",
            "Options": [{"Label": "Évitée", "Flags": ["evite"]}],
        },
        "Scenes": [_branching_scene().to_dict()],
    })
    meta = chapter_meta(ch)
    assert meta["owned_flags"] == ["a", "b"]
    assert meta["start_choice"] == {
        "unless_any": ["erreur", "evite"],
        "question": "Quelle nuit ?",
        "options": [{"label": "Évitée", "flags": ["evite"]}],
    }
