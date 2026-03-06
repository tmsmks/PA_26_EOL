#!/usr/bin/env python3
"""
End of Life - graph_viewer.py
Génère des pages HTML par chapitre avec vis-network.
Mode édition : modification Text, Name, SceneIntroduction, scores.
Mode parcours joueur : parcours interactif, chemin en vert, scores finaux.
"""
import json
import os
import re

from graph_builder import load_chapters, build_scene_graph

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "chapters", "Chapters_v3-4-c_emotional-illustration.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "graphes")


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def _html_escape(s: str) -> str:
    if not s:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    ).replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")


def render_html(chapter: dict, scenes_data: list) -> str:
    """Génère le HTML complet pour un chapitre."""
    chapter_id = chapter["Id"]
    chapter_name = chapter.get("Name", "")

    scenes_json = json.dumps(scenes_data, ensure_ascii=False)
    chapters_json = json.dumps({"Chapters": [chapter]}, ensure_ascii=False)

    sidebar_buttons = ""
    for i, sd in enumerate(scenes_data):
        title = _html_escape(sd.get("title", ""))
        sidebar_buttons += f'<button class="scene-btn" data-idx="{i}">{title}</button>\n'

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>End of Life — Chapitre {chapter_id} : {_html_escape(chapter_name)}</title>
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: system-ui, -apple-system, sans-serif; background: #0f0f14; color: #e4e4e7; display: flex; height: 100vh; overflow: hidden; -webkit-font-smoothing: antialiased; }}
#network {{ -webkit-font-smoothing: antialiased; }}
.sidebar {{ width: 220px; background: #18181b; padding: 14px; border-right: 1px solid #27272a; overflow-y: auto; }}
.sidebar h3 {{ margin: 0 0 10px; font-size: 11px; color: #71717a; text-transform: uppercase; letter-spacing: 0.05em; }}
.search {{ width: 100%; padding: 8px 10px; margin-bottom: 10px; background: #27272a; border: 1px solid #3f3f46; border-radius: 6px; color: #fff; font-size: 12px; }}
.search::placeholder {{ color: #71717a; }}
.scene-btn {{ display: block; width: 100%; background: transparent; color: #d4d4d8; border: none; padding: 9px 12px; margin-bottom: 2px; cursor: pointer; text-align: left; border-radius: 6px; font-size: 13px; }}
.scene-btn:hover {{ background: #27272a; color: #fff; }}
.scene-btn.active {{ background: #3f3f46; color: #38bdf8; font-weight: 500; }}
.main {{ flex: 1; position: relative; min-width: 0; min-height: 0; }}
#network {{ position: absolute; top: 0; left: 0; right: 0; bottom: 40px; width: 100%; background: #0f0f14; min-height: 350px; }}
.hint {{ position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); color: #52525b; font-size: 11px; }}
.editor {{ width: 400px; background: #18181b; padding: 14px; border-left: 1px solid #27272a; overflow-y: auto; }}
.editor h3 {{ margin: 0 0 10px; font-size: 13px; color: #38bdf8; }}
.scene-intro {{ margin-bottom: 14px; }}
.scene-intro label {{ display: block; font-size: 10px; color: #71717a; margin-bottom: 4px; }}
.scene-intro textarea {{ width: 100%; padding: 8px; font-size: 12px; background: #27272a; color: #fff; border: 1px solid #3f3f46; border-radius: 6px; resize: vertical; }}
.block {{ margin-bottom: 14px; padding: 12px; background: #27272a; border-radius: 8px; border: 1px solid #3f3f46; }}
.block .header {{ margin-bottom: 8px; font-weight: 600; color: #38bdf8; font-size: 12px; }}
.block label {{ display: block; font-size: 10px; color: #71717a; margin: 6px 0 3px; }}
.block textarea {{ width: 100%; padding: 8px; font-size: 12px; background: #18181b; color: #fff; border: 1px solid #3f3f46; border-radius: 6px; resize: vertical; }}
.resp {{ margin: 10px 0; padding-left: 10px; border-left: 2px solid #3f3f46; }}
.scores {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-top: 8px; }}
.scores input {{ width: 50px; padding: 4px; font-size: 12px; }}
.export {{ background: #38bdf8; color: #0f0f14; border: none; padding: 12px; cursor: pointer; border-radius: 8px; width: 100%; font-weight: 600; margin-top: 12px; font-size: 13px; }}
.export:hover {{ background: #0ea5e9; }}
.export-secondary {{ background: #3f3f46; margin-top: 8px; }}
.export-secondary:hover {{ background: #52525b; }}
.save-ok {{ margin-top: 10px; padding: 10px; background: #166534; border-radius: 6px; font-size: 12px; color: #22c55e; }}
.save-err {{ margin-top: 10px; padding: 10px; background: #7f1d1d; border-radius: 6px; font-size: 12px; color: #ef4444; }}
.validation {{ margin-top: 10px; padding: 10px; background: #1c1917; border-radius: 6px; font-size: 12px; color: #fbbf24; }}
.validation.ok {{ color: #22c55e; }}
.empty {{ color: #71717a; font-style: italic; padding: 24px; text-align: center; }}
.mode-tabs {{ display: flex; gap: 6px; margin-bottom: 12px; }}
.mode-tabs button {{ padding: 8px 14px; border: 1px solid #3f3f46; background: #27272a; color: #a1a1aa; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 500; }}
.mode-tabs button:hover {{ color: #fff; background: #3f3f46; }}
.mode-tabs button.active {{ background: #38bdf8; color: #0f0f14; border-color: #38bdf8; }}
.panel-edit {{ display: block; }}
.panel-parcours {{ display: none; flex-direction: column; }}
.panel-edit.hidden {{ display: none; }}
.panel-parcours.active {{ display: flex; }}
.parcours-card {{ background: #27272a; border-radius: 10px; padding: 16px; margin-bottom: 12px; border: 1px solid #3f3f46; }}
.parcours-card .parcours-image {{ width: 100%; max-width: 200px; height: auto; border-radius: 8px; margin-bottom: 12px; display: block; object-fit: cover; }}
.parcours-card .actor {{ display: inline-block; background: #38bdf8; color: #0f0f14; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-bottom: 10px; }}
.parcours-card .text {{ font-size: 14px; line-height: 1.5; margin-bottom: 16px; color: #e4e4e7; }}
.parcours-choice {{ display: block; width: 100%; text-align: left; padding: 12px 14px; margin-bottom: 8px; background: #3f3f46; border: 1px solid #52525b; color: #e4e4e7; border-radius: 8px; cursor: pointer; font-size: 13px; transition: all 0.15s; }}
.parcours-choice:hover {{ background: #52525b; border-color: #38bdf8; }}
.parcours-end {{ color: #71717a; font-style: italic; padding: 20px; text-align: center; }}
.parcours-restart {{ background: #71717a; color: #fff; border: none; padding: 10px 14px; cursor: pointer; border-radius: 8px; font-size: 12px; margin-top: 8px; }}
.parcours-restart:hover {{ background: #52525b; }}
.parcours-totals {{ margin-top: 16px; padding: 14px; background: #18181b; border-radius: 8px; border: 1px solid #22c55e; }}
.parcours-totals h4 {{ margin: 0 0 10px; font-size: 12px; color: #22c55e; }}
.parcours-totals .score-line {{ display: flex; justify-content: space-between; padding: 4px 0; font-size: 13px; }}
.parcours-totals .score-line.positive {{ color: #22c55e; }}
.parcours-totals .score-line.negative {{ color: #ef4444; }}
.parcours-totals .score-line.zero {{ color: #71717a; }}
</style>
</head>
<body>
<div class="sidebar">
    <h3>Chapitre {chapter_id} — Scénarios</h3>
    <input type="text" class="search" id="search" placeholder="EG-3 : Recherche par texte">
    {sidebar_buttons}
</div>
<div class="main">
    <div id="network"></div>
    <div class="hint">Molette : zoom — Glisser : déplacer — Survol nœud : infobulle complète</div>
</div>
<div class="editor">
    <div class="mode-tabs">
        <button class="mode-btn active" data-mode="edit">Édition</button>
        <button class="mode-btn" data-mode="parcours">Parcours joueur</button>
    </div>
    <div class="panel-edit" id="panel-edit">
        <h3 id="ed-title">Sélectionnez un scénario</h3>
        <div id="ed-content"><div class="empty">Cliquez sur un scénario à gauche.</div></div>
        <button class="export" id="save-btn">Valider et sauvegarder dans Chapters_v3-4-c_emotional-illustration.json</button>
        <button class="export export-secondary" id="export-btn">Télécharger (JSON)</button>
        <div id="save-status"></div>
        <div id="validation"></div>
    </div>
    <div class="panel-parcours" id="panel-parcours">
        <h3 id="parcours-title">Parcours joueur</h3>
        <div id="parcours-content">
            <div class="parcours-card">
                <div class="parcours-end">Sélectionnez un scénario puis choisissez vos réponses. Votre chemin s'affichera en vert sur le graphe.</div>
            </div>
        </div>
        <button class="parcours-restart" id="parcours-restart" style="display:none">Recommencer</button>
    </div>
</div>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js" crossorigin="anonymous"></script>
<script>
var chapterId = "{chapter_id}";
var chaptersData = {{"Chapters":[]}};
var scenesData = [];
try {{
    chaptersData = {chapters_json};
    scenesData = {scenes_json};
}} catch (e) {{
    console.error("Erreur chargement données:", e);
}}
var container = document.getElementById("network");
var network = null;
var nodesDS = null;
var edgesDS = null;
var currentSceneIdx = 0;
var parcoursPath = {{ nodes: [], edges: [] }};
var parcoursCurrent = null;
var parcoursScores = {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }};

function setMode(mode) {{
    document.querySelectorAll(".mode-btn").forEach(function(b) {{ b.classList.toggle("active", b.dataset.mode === mode); }});
    document.getElementById("panel-edit").classList.toggle("hidden", mode !== "edit");
    document.getElementById("panel-parcours").classList.toggle("active", mode === "parcours");
    if (mode === "parcours" && scenesData.length > 0) {{
        parcoursPath = {{ nodes: [], edges: [] }};
        parcoursCurrent = null;
        parcoursScores = {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }};
        showParcoursScene(currentSceneIdx);
    }} else {{
        parcoursPath = {{ nodes: [], edges: [] }};
        parcoursCurrent = null;
        if (nodesDS && edgesDS) highlightPath();
    }}
}}

function showParcoursScene(idx) {{
    var s = scenesData[idx];
    document.getElementById("parcours-title").textContent = s.title + " — Parcours joueur";
    if (!s.parcours || s.parcours.length === 0) {{
        document.getElementById("parcours-content").innerHTML = '<div class="parcours-card"><div class="parcours-end">Aucune interaction dans ce scénario.</div></div>';
        document.getElementById("parcours-restart").style.display = "none";
        return;
    }}
    parcoursPath = {{ nodes: [], edges: [] }};
    parcoursScores = {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }};
    parcoursCurrent = s.parcours[0];
    renderParcours(s);
    highlightPath();
}}

function esc(s) {{ if (!s) return ""; return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }}
function renderParcours(s) {{
    var ia = parcoursCurrent;
    if (!ia) {{
        var totalsHtml = '<div class="parcours-card"><div class="parcours-end">Fin de cette branche.</div>';
        if (parcoursPath.nodes.length > 0) {{
            totalsHtml += '<div class="parcours-totals"><h4>Score total du parcours</h4>';
            var labels = {{ RespectAndDignity: "Respect et dignité", Empathy: "Empathie", Compassion: "Compassion", EmotionalRegulation: "Régulation émotionnelle", CommunicationClarity: "Clarté communication", ProfessionalBoundaries: "Frontières pro.", InterprofessionalCollaboration: "Collab. interpro." }};
            for (var k in parcoursScores) {{
                var v = parcoursScores[k];
                var cls = v > 0 ? "positive" : (v < 0 ? "negative" : "zero");
                totalsHtml += '<div class="score-line ' + cls + '">' + (labels[k] || k) + ': ' + (v >= 0 ? '+' : '') + v + '</div>';
            }}
            totalsHtml += '</div>';
        }}
        totalsHtml += '</div>';
        document.getElementById("parcours-content").innerHTML = totalsHtml;
        document.getElementById("parcours-restart").style.display = parcoursPath.nodes.length > 0 ? "block" : "none";
        return;
    }}
    var imgHtml = (ia.image) ? '<img class="parcours-image" src="/api/data/images/' + esc(ia.image) + '" alt="" />' : '';
    var html = '<div class="parcours-card">' + imgHtml + '<span class="actor">' + esc(ia.actor) + '</span><div class="text">' + esc(ia.text || "—") + '</div>';
    if (ia.responses && ia.responses.length > 0) {{
        ia.responses.forEach(function(r, i) {{
            var label = (r.text || "").length > 80 ? (r.text || "").substring(0, 80) + "…" : (r.text || "→ I" + r.next_id);
            var scores = {{ RespectAndDignity: r.RespectAndDignity||0, Empathy: r.Empathy||0, Compassion: r.Compassion||0, EmotionalRegulation: r.EmotionalRegulation||0, CommunicationClarity: r.CommunicationClarity||0, ProfessionalBoundaries: r.ProfessionalBoundaries||0, InterprofessionalCollaboration: r.InterprofessionalCollaboration||0 }};
            html += '<button class="parcours-choice" data-next="' + r.next_id + '" data-target="' + esc(r.target_node_id || "") + '" data-edge="' + esc(r.edge_id || "") + '" data-scores="' + esc(JSON.stringify(scores)) + '">' + esc(label) + '</button>';
        }});
    }} else {{
        html += '<div class="parcours-end">Fin de cette branche.</div>';
    }}
    html += '</div>';
    document.getElementById("parcours-content").innerHTML = html;
    document.getElementById("parcours-restart").style.display = parcoursPath.nodes.length > 0 ? "block" : "none";
    document.querySelectorAll(".parcours-choice").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            var scores = JSON.parse(this.dataset.scores || "{{}}");
            for (var k in scores) parcoursScores[k] = (parcoursScores[k] || 0) + (parseInt(scores[k]) || 0);
            var nextId = this.dataset.next;
            var edgeId = this.dataset.edge;
            if (parcoursCurrent && parcoursCurrent.node_id) parcoursPath.nodes.push(parcoursCurrent.node_id);
            if (edgeId) parcoursPath.edges.push(edgeId);
            parcoursCurrent = s.id_to_parcours && nextId !== "-1" && nextId !== "" ? s.id_to_parcours[nextId] : null;
            if (parcoursCurrent) parcoursPath.nodes.push(parcoursCurrent.node_id);
            renderParcours(s);
            highlightPath();
        }});
    }});
}}

function highlightPath() {{
    try {{
        if (!nodesDS || !edgesDS) return;
        var pathNodes = parcoursPath.nodes || [];
        var pathEdges = parcoursPath.edges || [];
        var curNode = parcoursCurrent ? parcoursCurrent.node_id : null;
        nodesDS.getIds().forEach(function(nid) {{
            var inPath = pathNodes.indexOf(nid) >= 0;
            var isCurrent = curNode === nid;
            nodesDS.update({{ id: nid, color: {{ background: inPath ? "#166534" : "#27272a", border: isCurrent ? "#fbbf24" : (inPath ? "#22c55e" : "#38bdf8") }} }});
        }});
        edgesDS.getIds().forEach(function(eid) {{
            var inPath = pathEdges.indexOf(eid) >= 0;
            edgesDS.update({{ id: eid, color: inPath ? "#22c55e" : "#3f3f46" }});
        }});
    }} catch (err) {{ console.warn("highlightPath:", err); }}
}}

function showScene(idx) {{
    currentSceneIdx = idx;
    document.querySelectorAll(".scene-btn").forEach(function(b) {{
        b.classList.toggle("active", parseInt(b.dataset.idx) === idx);
    }});
    var s = scenesData[idx];
    document.getElementById("ed-title").textContent = s.title;
    var introHtml = '<div class="scene-intro"><label>EG-4 : SceneIntroduction</label><textarea class="edit" data-type="intro" rows="3">' + (s.scene_intro || '').replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;") + '</textarea></div>';
    document.getElementById("ed-content").innerHTML = introHtml + s.editor;

    var opts = {{
        nodes: {{ font: {{ size: 18, color: "#fafafa", face: "system-ui, -apple-system, sans-serif" }}, shape: "box", color: {{ background: "#27272a", border: "#38bdf8" }}, margin: 20, borderWidth: 2, widthConstraint: {{ minimum: 160, maximum: 280 }} }},
        edges: {{ arrows: "to", width: 2, color: "#3f3f46", font: {{ color: "#94a3b8", size: 12, face: "system-ui, sans-serif" }} }},
        layout: {{ hierarchical: {{ enabled: true, direction: "UD", sortMethod: "directed", levelSeparation: 380, nodeSpacing: 420, treeSpacing: 380, blockShifting: true, edgeMinimization: true }} }},
        physics: {{ enabled: false }},
        interaction: {{ zoomView: true, dragView: true }}
    }};

    if (nodesDS && edgesDS) {{
        nodesDS.clear();
        edgesDS.clear();
        s.nodes.forEach(function(n) {{ nodesDS.add(n); }});
        s.edges.forEach(function(e) {{ edgesDS.add(e); }});
        setTimeout(function() {{ if (network) network.fit({{ animation: {{ duration: 300 }}, scale: 1.3 }}); }}, 200);
    }} else {{
        nodesDS = new vis.DataSet(s.nodes);
        edgesDS = new vis.DataSet(s.edges);
        network = new vis.Network(container, {{ nodes: nodesDS, edges: edgesDS }}, opts);
        network.once("afterDrawing", function() {{ network.fit({{ animation: {{ duration: 400 }}, scale: 1.3 }}); }});
        setTimeout(function() {{ if (network) {{ network.redraw(); network.fit({{ scale: 1.3 }}); }} }}, 300);
        network.on("click", function(params) {{
            if (params.nodes && params.nodes.length > 0) {{
                var nid = String(params.nodes[0]);
                var m = nid.match(/_I(\\d+)$/);
                if (m) {{
                    var block = document.querySelector('.block[data-interaction-id="' + m[1] + '"]');
                    if (block) block.scrollIntoView({{ behavior: "smooth" }});
                }}
            }}
        }});
    }}

    attachEditors(idx);
    updateValidation();
    if (document.getElementById("panel-parcours").classList.contains("active")) {{
        parcoursPath = {{ nodes: [], edges: [] }};
        parcoursCurrent = null;
        showParcoursScene(idx);
    }} else {{
        highlightPath();
    }}
}}

function escapeHtml(s) {{
    if (!s) return '';
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}}

function attachEditors(idx) {{
    var ch = chaptersData.Chapters[0];
    var sc = ch.Scenes[idx];
    document.querySelectorAll("#ed-content .edit").forEach(function(el) {{
        el.addEventListener("input", function() {{
            var type = this.dataset.type;
            var i = parseInt(this.dataset.i);
            if (type === "intro") {{
                sc.SceneIntroduction = this.value;
            }} else if (type === "name") {{
                sc.Interactions[i].Name = this.value;
            }} else if (type === "text") {{
                sc.Interactions[i].Text = this.value;
                sc.Interactions[i].Name = this.value.substring(0, 50);
            }} else if (type === "response") {{
                var r = parseInt(this.dataset.r);
                sc.Interactions[i].Responses[r].Text = this.value;
                sc.Interactions[i].Responses[r].Name = this.value.substring(0, 80);
            }}
        }});
    }});
    document.querySelectorAll("#ed-content .score").forEach(function(el) {{
        el.addEventListener("change", function() {{
            var i = parseInt(this.dataset.i), r = parseInt(this.dataset.r), skill = this.dataset.skill;
            var v = parseInt(this.value) || 0;
            if (v < -3) v = -3;
            if (v > 3) v = 3;
            sc.Interactions[i].Responses[r][skill] = v;
        }});
    }});
}}

function updateValidation() {{
    var errs = [];
    var ch = chaptersData.Chapters[0];
    ch.Scenes.forEach(function(sc) {{
        var ids = {{}};
        sc.Interactions.forEach(function(ia) {{ ids[ia.Id] = true; }});
        sc.Interactions.forEach(function(ia) {{
            (ia.Responses || []).forEach(function(r) {{
                var nid = r.NextInteractionID;
                if (nid != null && nid !== -1 && !ids[nid]) errs.push("EG-7: NextInteractionID " + nid + " invalide (scène " + sc.Title + ")");
            }});
        }});
    }});
    var div = document.getElementById("validation");
    if (errs.length > 0) {{
        div.className = "validation";
        div.textContent = errs.join(" ; ");
    }} else {{
        div.className = "validation ok";
        div.textContent = "EG-7 : Validation OK — NextInteractionID valides.";
    }}
}}

document.querySelectorAll(".scene-btn").forEach(function(b) {{
    b.addEventListener("click", function() {{ showScene(parseInt(this.dataset.idx)); }});
}});

document.querySelectorAll(".mode-btn").forEach(function(b) {{
    b.addEventListener("click", function() {{ setMode(this.dataset.mode); }});
}});

document.getElementById("parcours-restart").addEventListener("click", function() {{
    if (scenesData.length > 0) showParcoursScene(currentSceneIdx);
}});

document.getElementById("search").addEventListener("input", function() {{
    var q = (this.value || "").toLowerCase();
    document.querySelectorAll(".scene-btn").forEach(function(b) {{
        b.style.display = q && b.textContent.toLowerCase().indexOf(q) < 0 ? "none" : "block";
    }});
    if (scenesData && scenesData.length > 0) {{
        var vis = (this.value || "").toLowerCase();
        if (vis && nodesDS && edgesDS) {{
            var nodeIds = nodesDS.getIds();
            nodeIds.forEach(function(nid) {{
                var node = nodesDS.get(nid);
                var match = (node.label && node.label.toLowerCase().indexOf(vis) >= 0) || (node.title && node.title.toLowerCase().indexOf(vis) >= 0);
                nodesDS.update({{ id: nid, hidden: !match }});
            }});
        }} else if (nodesDS) {{
            nodesDS.getIds().forEach(function(nid) {{ nodesDS.update({{ id: nid, hidden: false }}); }});
        }}
    }}
}});

document.getElementById("save-btn").addEventListener("click", function() {{
    var btn = this;
    var statusEl = document.getElementById("save-status");
    btn.disabled = true;
    statusEl.className = "";
    statusEl.textContent = "Enregistrement…";
    fetch("/api/save", {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify(chaptersData)
    }}).then(function(r) {{ return r.json().then(function(d) {{ return {{ ok: r.ok, data: d }}; }}); }})
    .then(function(result) {{
        btn.disabled = false;
        if (result.ok) {{
            statusEl.className = "save-ok";
            statusEl.textContent = result.data.message || "Sauvegardé.";
        }} else {{
            statusEl.className = "save-err";
            statusEl.textContent = result.data.error || "Erreur. Utilisez python app.py pour activer la sauvegarde directe.";
        }}
    }}).catch(function(err) {{
        btn.disabled = false;
        statusEl.className = "save-err";
        statusEl.textContent = "Erreur réseau. Lancez python app.py puis ouvrez http://localhost:8765";
    }});
}});

document.getElementById("export-btn").addEventListener("click", function() {{
    var blob = new Blob([JSON.stringify(chaptersData, null, 2)], {{ type: "application/json" }});
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "Chapitre_" + chapterId + "_modified.json";
    a.click();
}});

function init() {{
    if (typeof vis === "undefined") {{
        container.innerHTML = "<p style='color:#ef4444;padding:20px'>vis-network non chargé. Vérifiez votre connexion et rechargez.</p>";
        return;
    }}
    if (scenesData && scenesData.length > 0) {{
        try {{ showScene(0); }} catch (err) {{
            console.error("showScene:", err);
            container.innerHTML = "<p style='color:#ef4444;padding:20px'>Erreur: " + String(err.message || err) + "</p>";
        }}
    }} else {{
        document.getElementById("ed-content").innerHTML = "<div class='empty'>Aucune donnée (erreur de chargement?).</div>";
    }}
}}
function runInit() {{
    if (typeof vis !== "undefined") {{ init(); return; }}
    var n = 0;
    var t = setInterval(function() {{
        n++;
        if (typeof vis !== "undefined") {{ clearInterval(t); init(); }}
        else if (n > 60) {{ clearInterval(t); container.innerHTML = "<p style='color:#ef4444;padding:20px'>vis-network timeout.</p>"; }}
    }}, 100);
}}
window.addEventListener("load", function() {{ setTimeout(runInit, 80); }});
</script>
</body>
</html>
'''


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = load_chapters(DATA_PATH)
    links = []

    for ch in data.get("Chapters", []):
        chapter_id = ch["Id"]
        chapter_name = ch.get("Name", "")
        scenes_data = []
        for scene in ch.get("Scenes", []):
            scenes_data.append(build_scene_graph(chapter_id, scene))

        slug = _slug(chapter_name)
        filename = f"chapitre_{chapter_id}_{slug}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        html = render_html(ch, scenes_data)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        links.append((chapter_name, filename))
        print(f"Généré : {filepath}")

    index_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>End of Life — Graphes</title>
<style>body{{font-family:sans-serif;padding:24px;background:#0f0f14;color:#e4e4e7}}
h1{{color:#38bdf8}} a{{color:#38bdf8}} a:hover{{text-decoration:underline}}
ul{{list-style:none;padding:0}}</style></head>
<body><h1>End of Life — Éditeur graphique</h1>
<ul>
"""
    for name, filename in links:
        index_html += f'<li><a href="{filename}">{name}</a></li>\n'
    index_html += "</ul></body></html>"
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"Index : {index_path}")


if __name__ == "__main__":
    main()
