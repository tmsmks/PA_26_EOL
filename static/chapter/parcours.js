// Module Parcours — mode parcours joueur (chemin vert sur le graphe + scores).

import { config, resetParcours, SKILL_LABELS_FR, state } from "./store.js";
import { highlightPath } from "./network.js";
import { scheduleCacheSave } from "./persistence.js";
import { esc } from "./utils.js";

export function setMode(mode) {
    state.currentMode = mode;
    document.querySelectorAll(".mode-btn").forEach((b) => {
        b.classList.toggle("active", b.dataset.mode === mode);
    });
    document.getElementById("panel-edit").classList.toggle("hidden", mode !== "edit");
    document.getElementById("panel-parcours").classList.toggle("active", mode === "parcours");
    if (mode === "parcours" && state.scenesData.length > 0) {
        resetParcours();
        showParcoursScene(state.currentSceneIdx);
    } else {
        state.parcoursPath = { nodes: [], edges: [] };
        state.parcoursCurrent = null;
        if (state.nodesDS && state.edgesDS) highlightPath();
    }
    scheduleCacheSave();
}

export function showParcoursScene(idx) {
    const s = state.scenesData[idx];
    document.getElementById("parcours-title").textContent =
        s.title + " — Parcours joueur";
    if (!s.parcours || s.parcours.length === 0) {
        document.getElementById("parcours-content").innerHTML =
            '<div class="parcours-card"><div class="parcours-end">Aucune interaction dans ce scénario.</div></div>';
        document.getElementById("parcours-restart").style.display = "none";
        return;
    }
    resetParcours();
    state.parcoursCurrent = s.parcours[0];
    renderParcours(s);
    highlightPath();
}

function renderTotals(title) {
    let html = '<div class="parcours-totals"><h4>' + title + "</h4>";
    for (const k of Object.keys(state.parcoursScores)) {
        const v = state.parcoursScores[k] || 0;
        const cls = v > 0 ? "positive" : v < 0 ? "negative" : "zero";
        html +=
            '<div class="score-line ' + cls + '">' +
            (SKILL_LABELS_FR[k] || k) +
            ": " + (v >= 0 ? "+" : "") + v + "</div>";
    }
    return html + "</div>";
}

function renderParcours(s) {
    const ia = state.parcoursCurrent;
    if (!ia) {
        let html = '<div class="parcours-card"><div class="parcours-end">Fin de cette branche.</div>';
        if (state.parcoursPath.nodes.length > 0) {
            html += renderTotals("Score total du parcours");
        }
        html += "</div>";
        document.getElementById("parcours-content").innerHTML = html;
        document.getElementById("parcours-restart").style.display =
            state.parcoursPath.nodes.length > 0 ? "block" : "none";
        return;
    }

    const imgHtml = ia.image
        ? '<img class="parcours-image" src="' + esc(config.imagesBaseUrl + ia.image) + '" alt="" />'
        : "";
    let html =
        '<div class="parcours-card">' + imgHtml +
        '<span class="actor">' + esc(ia.actor) + "</span>" +
        '<div class="text">' + esc(ia.text || "—") + "</div>";

    if (ia.responses && ia.responses.length > 0) {
        ia.responses.forEach((r) => {
            const label = r.text || "→ I" + r.next_id;
            const scores = {
                RespectAndDignity: r.RespectAndDignity || 0,
                Empathy: r.Empathy || 0,
                Compassion: r.Compassion || 0,
                EmotionalRegulation: r.EmotionalRegulation || 0,
                CommunicationClarity: r.CommunicationClarity || 0,
                ProfessionalBoundaries: r.ProfessionalBoundaries || 0,
                InterprofessionalCollaboration: r.InterprofessionalCollaboration || 0,
            };
            html +=
                '<button class="parcours-choice" data-next="' + r.next_id + '"' +
                ' data-target="' + esc(r.target_node_id || "") + '"' +
                ' data-edge="' + esc(r.edge_id || "") + '"' +
                ' data-scores="' + esc(JSON.stringify(scores)) + '">' +
                esc(label) + "</button>";
        });
    } else {
        html += '<div class="parcours-end">Fin de cette branche.</div>';
    }
    html += "</div>";
    html += renderTotals("Score courant du parcours");

    document.getElementById("parcours-content").innerHTML = html;
    document.getElementById("parcours-restart").style.display =
        state.parcoursPath.nodes.length > 0 ? "block" : "none";

    document.querySelectorAll(".parcours-choice").forEach((btn) => {
        btn.addEventListener("click", function () {
            const scores = JSON.parse(this.dataset.scores || "{}");
            for (const k of Object.keys(scores)) {
                state.parcoursScores[k] =
                    (state.parcoursScores[k] || 0) + (parseInt(scores[k]) || 0);
            }
            const nextId = this.dataset.next;
            const edgeId = this.dataset.edge;
            if (state.parcoursCurrent && state.parcoursCurrent.node_id) {
                state.parcoursPath.nodes.push(state.parcoursCurrent.node_id);
            }
            if (edgeId) state.parcoursPath.edges.push(edgeId);
            state.parcoursCurrent =
                s.id_to_parcours && nextId !== "-1" && nextId !== ""
                    ? s.id_to_parcours[nextId]
                    : null;
            if (state.parcoursCurrent) {
                state.parcoursPath.nodes.push(state.parcoursCurrent.node_id);
            }
            renderParcours(s);
            highlightPath();
        });
    });
}
