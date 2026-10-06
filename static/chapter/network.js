// Module Network — vis-network setup, rebuild, highlight, panels.

import { SCORE_SKILLS, state } from "./store.js";
import {
    applyCurrentScenePositions,
    saveCurrentScenePositions,
    scheduleCacheSave,
} from "./persistence.js";
import { getInteractionIdFromNodeId } from "./utils.js";

export function updatePanelToggleButtons() {
    const leftBtn = document.getElementById("toggle-left-panel");
    const rightBtn = document.getElementById("toggle-right-panel");
    if (leftBtn) leftBtn.textContent = state.leftPanelHidden ? "› Afficher la liste" : "‹ Masquer la liste";
    if (rightBtn) rightBtn.textContent = state.rightPanelHidden ? "Afficher l'éditeur ‹" : "Masquer l'éditeur ›";
}

export function applyPanelVisibility() {
    const sidebar = document.querySelector(".sidebar");
    const editor = document.querySelector(".editor");
    if (sidebar) sidebar.classList.toggle("hidden-panel", state.leftPanelHidden);
    if (editor) editor.classList.toggle("hidden-panel", state.rightPanelHidden);
    updatePanelToggleButtons();
}

export function highlightPath() {
    try {
        if (!state.nodesDS || !state.edgesDS) return;
        const pathNodes = state.parcoursPath.nodes || [];
        const pathEdges = state.parcoursPath.edges || [];
        const curNode = state.parcoursCurrent ? state.parcoursCurrent.node_id : null;
        for (const nid of state.nodesDS.getIds()) {
            const node = state.nodesDS.get(nid) || {};
            const isRoot = !!node.is_root;
            const inPath = pathNodes.indexOf(nid) >= 0;
            const isCurrent = curNode === nid;
            let bg, border;
            if (inPath) {
                bg = "#e3f6e6";
                border = isCurrent ? "#ab4400" : "#007e2a";
            } else if (node.is_entry) {
                // Point d'entrée alternatif (états narratifs), pas un orphelin.
                bg = "#fcf0f5";
                border = "#9a0050";
            } else if (isRoot) {
                bg = "#ffeae8";
                border = "#b50000";
            } else {
                bg = "#ffffff";
                border = "#0040bb";
            }
            state.nodesDS.update({ id: nid, color: { background: bg, border: border } });
        }
        for (const eid of state.edgesDS.getIds()) {
            const inPath = pathEdges.indexOf(eid) >= 0;
            state.edgesDS.update({ id: eid, color: inPath ? "#007e2a" : "#989fa8" });
        }
    } catch (err) {
        console.warn("highlightPath:", err);
    }
}

function getNodeId(chapterId, sceneId, interactionId) {
    return "C" + chapterId + "_S" + sceneId + "_I" + interactionId;
}

function getEdgeId(nodeId, responseIdx, targetNodeId) {
    return nodeId + "_R" + responseIdx + "_>" + targetNodeId;
}

function responseScore(response, skill) {
    const dims = response.SoftSkillDimensions || {};
    const raw = dims[skill] != null ? dims[skill] : response[skill];
    const value = parseInt(raw, 10);
    return isNaN(value) ? 0 : value;
}

function buildParcoursPayload(chapterId, scene, idToIa) {
    const interactions = scene.Interactions || [];
    let starts = interactions.map((ia) => ia.Id);

    for (const ia of interactions) {
        for (const r of ia.Responses || []) {
            const nextId = r.NextInteractionID;
            if (nextId != null && nextId !== -1) {
                starts = starts.filter((id) => id !== nextId);
            }
        }
    }
    if (starts.length === 0 && interactions.length > 0) {
        starts = [interactions[0].Id];
    }

    const parcours = [];
    const visited = {};

    function addEntry(interactionId) {
        if (visited[interactionId]) return;
        visited[interactionId] = true;
        const ia = idToIa[interactionId];
        if (!ia) return;

        const nodeId = getNodeId(chapterId, scene.Id, ia.Id);
        const responses = [];
        (ia.Responses || []).forEach((r, rIdx) => {
            const nextId = r.NextInteractionID;
            const payload = {
                text: r.Text || "",
                next_id: nextId != null ? String(nextId) : "-1",
            };
            for (const skill of SCORE_SKILLS) {
                payload[skill] = responseScore(r, skill);
            }
            if (nextId != null && nextId !== -1) {
                const targetNodeId = getNodeId(chapterId, scene.Id, nextId);
                payload.target_node_id = targetNodeId;
                payload.edge_id = getEdgeId(nodeId, rIdx, targetNodeId);
            } else {
                payload.target_node_id = "";
                payload.edge_id = "";
            }
            responses.push(payload);
        });

        parcours.push({
            node_id: nodeId,
            actor: (ia.Actor || {}).Name || "",
            text: ia.Text || "",
            image: ia.AgentFacialExpression || "",
            responses,
        });

        for (const r of ia.Responses || []) {
            const nextId = r.NextInteractionID;
            if (nextId != null && nextId !== -1 && !visited[nextId]) {
                addEntry(nextId);
            }
        }
    }

    starts.sort((a, b) => a - b).forEach(addEntry);
    for (const ia of interactions) {
        if (!visited[ia.Id]) addEntry(ia.Id);
    }

    const idToParcours = {};
    for (const entry of parcours) {
        idToParcours[String(getInteractionIdFromNodeId(entry.node_id, null))] = entry;
    }
    return { parcours, idToParcours };
}

export function rebuildSceneGraph(idx) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    const sc = chapter.Scenes[idx];
    const chId = chapter.Id;
    const interactions = sc.Interactions || [];
    const idToIa = {};
    for (const ia of interactions) idToIa[ia.Id] = ia;

    const newNodes = [];
    const newEdges = [];
    for (const ia of interactions) {
        const actorName = (ia.Actor || {}).Name || "?";
        const text = ia.Text || "";
        const name = ia.Name || text.substring(0, 50);
        const nodeId = getNodeId(chId, sc.Id, ia.Id);
        let baseLabel = name || text || "—";
        if (baseLabel.length > 38) baseLabel = baseLabel.substring(0, 37) + "…";
        const label = ia.Id + " — " + baseLabel;
        const title = "[" + actorName + "] " + (text || name);
        newNodes.push({ id: nodeId, label, title, interaction_id: String(ia.Id) });

        const respList = ia.Responses || [];
        const respCount = respList.length;
        respList.forEach((r, rIdx) => {
            const nextId = r.NextInteractionID;
            if (nextId == null || nextId === -1) return;
            if (!idToIa[nextId]) return;
            const targetNodeId = getNodeId(chId, sc.Id, nextId);
            const edgeId = getEdgeId(nodeId, rIdx, targetNodeId);
            const rText = (r.Text || "").trim();
            let edgeTitle = "Réponse " + (rIdx + 1);
            if (rText) edgeTitle += " — " + rText;

            const direction = rIdx % 2 === 0 ? "curvedCW" : "curvedCCW";
            let roundness;
            if (respCount <= 1) {
                roundness = 0.2;
            } else {
                roundness = 0.2 + Math.floor(rIdx / 2) * 0.15;
                if (roundness > 0.85) roundness = 0.85;
            }
            const isBackOrLateral = parseInt(nextId, 10) <= parseInt(ia.Id, 10);
            if (isBackOrLateral) {
                roundness = Math.max(roundness, 0.55 + rIdx * 0.1);
                if (roundness > 0.95) roundness = 0.95;
            }
            newEdges.push({
                id: edgeId,
                from: nodeId,
                to: targetNodeId,
                label: "R" + (rIdx + 1),
                title: edgeTitle,
                smooth: { enabled: true, type: direction, roundness },
            });
        });
    }

    const targets = {};
    for (const e of newEdges) targets[e.to] = true;
    const firstNodeId = interactions.length > 0
        ? getNodeId(chId, sc.Id, interactions[0].Id)
        : null;
    const entryIds = {};
    for (const ep of sc.EntryPoints || []) {
        entryIds[getNodeId(chId, sc.Id, ep.InteractionId)] = true;
    }
    for (const n of newNodes) {
        if (entryIds[n.id]) {
            n.is_entry = true;
            n.color = { background: "#fcf0f5", border: "#9a0050" };
        } else if (!targets[n.id] && n.id !== firstNodeId) {
            n.is_root = true;
            n.color = { background: "#ffeae8", border: "#b50000" };
        } else {
            n.color = { background: "#ffffff", border: "#0040bb" };
        }
    }

    state.scenesData[idx].nodes = newNodes;
    state.scenesData[idx].edges = newEdges;
    state.scenesData[idx].scene_intro = sc.SceneIntroduction || "";
    const parcoursPayload = buildParcoursPayload(chId, sc, idToIa);
    state.scenesData[idx].parcours = parcoursPayload.parcours;
    state.scenesData[idx].id_to_parcours = parcoursPayload.idToParcours;

    if (state.nodesDS && state.edgesDS) {
        state.nodesDS.clear();
        state.edgesDS.clear();
        for (const n of newNodes) state.nodesDS.add(n);
        for (const e of newEdges) state.edgesDS.add(e);
    }
    highlightPath();
    // editor s'occupe de mettre à jour la validation au changement de scène
    import("./editor.js").then((m) => m.updateValidation());
}

export function focusResponseByEdgeId(edgeId) {
    try {
        if (!edgeId) return;
        const edge = state.edgesDS ? state.edgesDS.get(edgeId) : null;
        if (!edge) return;
        const iaId = getInteractionIdFromNodeId(edge.from, state.nodesDS);
        const m = String(edgeId).match(/_R(\d+)_>/);
        const rIdx = m ? parseInt(m[1], 10) : -1;
        if (!iaId || rIdx < 0) return;
        // editor handles the visible block focus + textarea highlight
        import("./editor.js").then((mod) => mod.focusResponseInEditor(iaId, rIdx));
    } catch (e) {
        console.warn("focusResponseByEdgeId:", e);
    }
}

export function showScene(idx) {
    if (idx < 0 || idx >= state.scenesData.length) return;
    if (state.network && state.nodesDS && idx !== state.currentSceneIdx) {
        saveCurrentScenePositions();
    }
    state.currentSceneIdx = idx;
    scheduleCacheSave();

    document.querySelectorAll(".scene-btn").forEach((b) => {
        b.classList.toggle("active", parseInt(b.dataset.idx) === idx);
    });

    const s = state.scenesData[idx];
    document.getElementById("ed-title").textContent = s.title;

    rebuildSceneGraph(idx);
    import("./editor.js").then((m) => {
        m.rebuildEditorHtml(idx);
        m.showOnlySelectedBlock(null);
    });

    const opts = {
        nodes: {
            font: {
                size: 38,
                color: "#192230",
                face: "system-ui, -apple-system, sans-serif",
                bold: true,
            },
            shape: "box",
            color: { background: "#ffffff", border: "#0040bb" },
            margin: 32,
            borderWidth: 2,
            widthConstraint: { minimum: 260, maximum: 360 },
        },
        edges: {
            arrows: "to",
            width: 2,
            hoverWidth: 3,
            selectionWidth: 5,
            smooth: { enabled: true, type: "dynamic", roundness: 0.35 },
            color: "#989fa8",
            font: {
                color: "#47505e",
                size: 14,
                align: "top",
                face: "system-ui, sans-serif",
                strokeWidth: 0,
            },
        },
        layout: {
            hierarchical: {
                enabled: true,
                direction: "UD",
                sortMethod: "directed",
                levelSeparation: 420,
                nodeSpacing: 560,
                treeSpacing: 520,
                blockShifting: true,
                edgeMinimization: true,
                parentCentralization: true,
            },
        },
        physics: { enabled: false },
        interaction: { zoomView: true, dragView: true, zoomSpeed: 0.35 },
    };

    if (!state.network) {
        state.nodesDS = new vis.DataSet(state.scenesData[idx].nodes);
        state.edgesDS = new vis.DataSet(state.scenesData[idx].edges);
        state.network = new vis.Network(
            state.container,
            { nodes: state.nodesDS, edges: state.edgesDS },
            opts
        );
        state.network.once("afterDrawing", () => {
            state.network.fit({ animation: { duration: 400 }, scale: 1.6 });
        });
        setTimeout(() => {
            if (state.network) {
                state.network.redraw();
                state.network.fit({ scale: 1.6 });
            }
        }, 300);
        setTimeout(() => applyCurrentScenePositions(idx), 360);
        state.network.on("click", (params) => {
            if (params.nodes && params.nodes.length > 0) {
                const nid = String(params.nodes[0]);
                const iaId = getInteractionIdFromNodeId(nid, state.nodesDS);
                if (iaId) {
                    import("./editor.js").then((m) => m.focusInteractionInEditor(iaId));
                }
            } else if (params.edges && params.edges.length > 0) {
                focusResponseByEdgeId(String(params.edges[0]));
            }
        });
        state.network.on("dragEnd", (params) => {
            if (params && params.nodes && params.nodes.length > 0) {
                saveCurrentScenePositions();
            }
        });
    } else {
        setTimeout(() => {
            if (state.network) {
                state.network.fit({ animation: { duration: 300 }, scale: 1.3 });
                applyCurrentScenePositions(idx);
            }
        }, 220);
    }

    import("./editor.js").then((m) => m.updateValidation());
    if (document.getElementById("panel-parcours").classList.contains("active")) {
        state.parcoursPath = { nodes: [], edges: [] };
        state.parcoursCurrent = null;
        import("./parcours.js").then((m) => m.showParcoursScene(idx));
    } else {
        highlightPath();
    }
}
