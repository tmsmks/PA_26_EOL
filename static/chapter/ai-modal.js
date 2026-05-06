// Module AI Modal — proposer une nouvelle réponse via LLM (4.2).

import { config, SCORE_SKILLS, SKILL_LABELS_FR, state } from "./store.js";
import {
    rebuildEditorHtml,
    showOnlySelectedBlock,
} from "./editor.js";
import { rebuildSceneGraph } from "./network.js";
import { scheduleCacheSave } from "./persistence.js";
import { escapeHtml, getNextResponseId } from "./utils.js";

function buildOrientationStepper(skill) {
    return (
        '<div class="ai-ori-item">' +
        "<label>" + (SKILL_LABELS_FR[skill] || skill) + "</label>" +
        '<div class="score-stepper">' +
        '<button type="button" class="score-btn ai-ori-minus" data-skill="' + skill + '">-</button>' +
        '<input type="hidden" class="ai-ori" data-skill="' + skill + '" value="0">' +
        '<span class="score-value ai-ori-value" data-skill="' + skill + '">0</span>' +
        '<button type="button" class="score-btn ai-ori-plus" data-skill="' + skill + '">+</button>' +
        "</div></div>"
    );
}

function renderAiProposalCard(p) {
    const cat = (p.Category || "").toLowerCase();
    const catClass =
        cat === "exemplaire"
            ? "exemplaire"
            : cat === "problématique" || cat === "problematique"
            ? "problematique"
            : "neutre";
    const catLabel = p.Category || "neutre";
    const dims = p.SoftSkillDimensions || {};
    let html = '<div class="ai-proposal">';
    html += '<span class="ai-cat ' + catClass + '">' + escapeHtml(catLabel) + "</span>";
    html += '<div class="ai-text">' + escapeHtml(p.Text || "") + "</div>";
    if (p.Rationale) {
        html += '<div class="ai-rationale">' + escapeHtml(p.Rationale) + "</div>";
    }
    html += '<div class="ai-scores">';
    for (const sk of SCORE_SKILLS) {
        let v = parseInt(dims[sk], 10);
        if (isNaN(v)) v = 0;
        const vcls = v > 0 ? "pos" : v < 0 ? "neg" : "zero";
        const sign = v > 0 ? "+" : "";
        html +=
            '<div class="sc"><span>' +
            (SKILL_LABELS_FR[sk] || sk) +
            '</span><span class="v ' + vcls + '">' + sign + v + "</span></div>";
    }
    html += "</div>";
    html += '<button type="button" class="ai-accept">Accepter et ajouter comme nouvelle réponse</button>';
    html += "</div>";
    return html;
}

export function openAiProposalModal(sceneIdx, iIdx) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[sceneIdx]) return;
    const sc = chapter.Scenes[sceneIdx];
    const ia = sc.Interactions[iIdx];
    if (!ia) return;

    const actorName = (ia.Actor || {}).Name || "?";
    let orientationHtml = "";
    for (const sk of SCORE_SKILLS) orientationHtml += buildOrientationStepper(sk);

    let nextOptionsHtml =
        '<option value="-1">-1 — Fin de branche (aucune suite)</option>';
    for (const otherIa of sc.Interactions || []) {
        if (otherIa.Id === ia.Id) continue;
        const preview = (otherIa.Text || otherIa.Name || "").substring(0, 80);
        const otherActor = (otherIa.Actor || {}).Name || "?";
        nextOptionsHtml +=
            '<option value="' + otherIa.Id + '">#' + otherIa.Id +
            " [" + escapeHtml(otherActor) + "] " + escapeHtml(preview) +
            (otherIa.Text && otherIa.Text.length > 80 ? "…" : "") + "</option>";
    }

    const ov = document.createElement("div");
    ov.className = "ai-overlay";
    ov.innerHTML =
        '<div class="ai-modal">' +
            "<h3>✨ Proposer une réponse avec IA</h3>" +
            '<p class="ai-sub">Le LLM analyse le contexte et propose une nouvelle réplique de l\'acteur, orientée selon vos choix. Aucune insertion n\'est faite tant que vous n\'avez pas cliqué sur « Accepter ».</p>' +
            '<div class="ai-context">' +
                "<div><strong>Scène</strong> : " + escapeHtml(sc.Title || "") + "</div>" +
                "<div><strong>Interaction</strong> #" + ia.Id + " (" + escapeHtml(actorName) + ") : " +
                escapeHtml((ia.Text || "").substring(0, 140)) +
                (ia.Text && ia.Text.length > 140 ? "…" : "") + "</div>" +
            "</div>" +
            '<div class="ai-section-title">Prochain bloc (NextInteractionID)</div>' +
            '<select class="ai-next">' + nextOptionsHtml + "</select>" +
            '<div class="ai-next-hint">La réponse générée sera rédigée pour mener naturellement à ce bloc, et sera liée à lui une fois acceptée.</div>' +
            '<div class="ai-section-title">Orientation soft skills (-3 à +3)</div>' +
            '<div class="ai-orientation">' + orientationHtml + "</div>" +
            '<div class="ai-section-title">Consigne libre (optionnel)</div>' +
            '<textarea class="ai-guidance" placeholder="Ex : « Ton plus direct, pas de paternalisme »"></textarea>' +
            '<div class="ai-actions">' +
                '<button type="button" class="ai-btn ai-btn-secondary ai-cancel">Fermer</button>' +
                '<button type="button" class="ai-btn ai-btn-primary ai-generate">Générer avec IA</button>' +
            "</div>" +
            '<div class="ai-status" style="display:none"></div>' +
            '<div class="ai-proposals"></div>' +
        "</div>";
    document.body.appendChild(ov);

    function closeModal() {
        if (ov.parentNode) ov.parentNode.removeChild(ov);
    }

    ov.querySelector(".ai-cancel").addEventListener("click", closeModal);
    ov.addEventListener("click", (e) => {
        if (e.target === ov) closeModal();
    });

    ov.querySelectorAll(".ai-ori-minus, .ai-ori-plus").forEach((btn) => {
        btn.addEventListener("click", function () {
            const skill = this.dataset.skill;
            const hidden = ov.querySelector('.ai-ori[data-skill="' + skill + '"]');
            const valueEl = ov.querySelector('.ai-ori-value[data-skill="' + skill + '"]');
            if (!hidden || !valueEl) return;
            let v = parseInt(hidden.value) || 0;
            v += this.classList.contains("ai-ori-plus") ? 1 : -1;
            if (v < -3) v = -3;
            if (v > 3) v = 3;
            hidden.value = String(v);
            valueEl.textContent = (v > 0 ? "+" : "") + String(v);
        });
    });

    ov.querySelector(".ai-generate").addEventListener("click", function () {
        const genBtn = this;
        const statusEl = ov.querySelector(".ai-status");
        const proposalsEl = ov.querySelector(".ai-proposals");
        proposalsEl.innerHTML = "";

        const orientation = {};
        ov.querySelectorAll(".ai-ori").forEach((inp) => {
            const v = parseInt(inp.value, 10);
            if (!isNaN(v) && v !== 0) orientation[inp.dataset.skill] = v;
        });
        const guidance = (ov.querySelector(".ai-guidance").value || "").trim();
        const nextSelect = ov.querySelector(".ai-next");
        let nextId = nextSelect ? parseInt(nextSelect.value, 10) : -1;
        if (isNaN(nextId)) nextId = -1;

        const payload = {
            book_slug: config.bookSlug,
            chapter_id: parseInt(config.chapterId, 10),
            scene_id: sc.Id,
            interaction_id: ia.Id,
            orientation,
            guidance,
            n: 1,
            next_interaction_id: nextId,
        };

        genBtn.disabled = true;
        statusEl.style.display = "block";
        statusEl.className = "ai-status loading";
        statusEl.textContent =
            "Appel du LLM en cours… (cela peut prendre quelques secondes)";

        fetch(config.apiEnrichUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        })
            .then((r) => r.json().then((d) => ({ ok: r.ok, data: d })))
            .then((result) => {
                genBtn.disabled = false;
                if (!result.ok) {
                    statusEl.className = "ai-status err";
                    statusEl.textContent =
                        (result.data && result.data.error) || "Erreur lors de l'appel IA.";
                    return;
                }
                const proposals = (result.data && result.data.proposals) || [];
                if (proposals.length === 0) {
                    statusEl.className = "ai-status err";
                    statusEl.textContent =
                        "Aucune proposition (tout a été filtré comme doublon ?).";
                    return;
                }
                statusEl.style.display = "none";
                proposals.forEach((p) => {
                    const card = document.createElement("div");
                    card.innerHTML = renderAiProposalCard(p);
                    const node = card.firstChild;
                    proposalsEl.appendChild(node);
                    node.querySelector(".ai-accept").addEventListener("click", () => {
                        acceptAiProposal(sceneIdx, iIdx, p, nextId);
                        closeModal();
                    });
                });
            })
            .catch(() => {
                genBtn.disabled = false;
                statusEl.className = "ai-status err";
                statusEl.textContent =
                    "Erreur réseau. Vérifiez que `python app.py` est lancé.";
            });
    });
}

function acceptAiProposal(sceneIdx, iIdx, proposal, nextInteractionId) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[sceneIdx]) return;
    const sc = chapter.Scenes[sceneIdx];
    const ia = sc.Interactions[iIdx];
    if (!ia) return;
    if (!ia.Responses) ia.Responses = [];

    const newRespId = getNextResponseId(ia);
    const dims = proposal.SoftSkillDimensions || {};
    const nextId =
        nextInteractionId == null || isNaN(parseInt(nextInteractionId, 10))
            ? -1
            : parseInt(nextInteractionId, 10);
    const newResp = {
        Id: newRespId,
        Name: (proposal.Text || "").substring(0, 80),
        Text: proposal.Text || "",
        NextInteractionID: nextId,
        Category: proposal.Category || "neutre",
        Rationale: proposal.Rationale || "",
        GeneratedByAI: true,
        SoftSkillDimensions: {},
        LegacyDimensions: proposal.LegacyDimensions || {},
    };
    for (const sk of SCORE_SKILLS) {
        let v = parseInt(dims[sk], 10);
        if (isNaN(v)) v = 0;
        if (v < -3) v = -3;
        if (v > 3) v = 3;
        newResp[sk] = v;
        newResp.SoftSkillDimensions[sk] = v;
    }
    ia.Responses.push(newResp);
    scheduleCacheSave();
    rebuildEditorHtml(sceneIdx);
    rebuildSceneGraph(sceneIdx);
    showOnlySelectedBlock(String(ia.Id));
    const block = document.querySelector('.block[data-interaction-id="' + ia.Id + '"]');
    if (block) block.scrollIntoView({ behavior: "smooth", block: "start" });
}
