// Module Editor — édition des interactions/réponses + CRUD + validation EG-7.

import { SCORE_SKILLS, state } from "./store.js";
import { scheduleCacheSave } from "./persistence.js";
import { rebuildSceneGraph } from "./network.js";
import {
    confirmDialog,
    escapeHtml,
    getNextInteractionId,
    getNextResponseId,
} from "./utils.js";

export function showOnlySelectedBlock(interactionId) {
    const blocks = Array.from(document.querySelectorAll("#ed-content .block"));
    if (!blocks.length) return;
    const target = interactionId ? String(interactionId) : "";
    let selected = null;
    for (const block of blocks) {
        const isMatch = !!target && block.dataset.interactionId === target;
        block.style.display = isMatch ? "block" : "none";
        block.classList.toggle("active", isMatch);
        if (isMatch) selected = block;
    }
    if (!selected) {
        selected = blocks[0];
        selected.style.display = "block";
        selected.classList.add("active");
    }
}

export function focusInteractionInEditor(interactionId) {
    showOnlySelectedBlock(interactionId);
    const block = document.querySelector(
        '.block[data-interaction-id="' + interactionId + '"]'
    );
    if (block) block.scrollIntoView({ behavior: "smooth", block: "start" });
}

export function focusResponseInEditor(interactionId, rIdx) {
    showOnlySelectedBlock(interactionId);
    const block = document.querySelector(
        '.block[data-interaction-id="' + interactionId + '"]'
    );
    if (!block) return;
    const textarea = block.querySelector(
        'textarea.edit[data-type="response"][data-r="' + rIdx + '"]'
    );
    if (!textarea) return;
    textarea.scrollIntoView({ behavior: "smooth", block: "center" });
    textarea.focus();
    block.classList.add("highlight-edge");
    setTimeout(() => block.classList.remove("highlight-edge"), 1500);
}

export function rebuildEditorHtml(idx) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    const sc = chapter.Scenes[idx];

    const introValue = sc.SceneIntroduction || "";
    const introHtml =
        '<div class="scene-intro"><label>EG-4 : SceneIntroduction</label>' +
        '<textarea class="edit" data-type="intro" rows="3">' +
        escapeHtml(introValue) +
        "</textarea></div>";

    let blocksHtml = "";
    (sc.Interactions || []).forEach((ia, i) => {
        const actor = (ia.Actor || {}).Name || "";
        const text = ia.Text || "";
        const name = ia.Name || text.substring(0, 50);
        let b = '<div class="block" data-interaction-id="' + ia.Id + '" data-i="' + i + '">';
        b += '<div class="header"><span>Interaction ' + ia.Id + ' — ' + escapeHtml(actor) + "</span>";
        b += '<button type="button" class="crud-btn crud-delete-interaction" data-i="' + i + '" title="Supprimer cette interaction">✕</button></div>';
        b += "<label>EG-4 : Name</label>";
        b += '<textarea class="edit" data-type="name" data-i="' + i + '" rows="1">' + escapeHtml(name) + "</textarea>";
        b += "<label>EG-4 : Text</label>";
        b += '<textarea class="edit" data-type="text" data-i="' + i + '" rows="3">' + escapeHtml(text) + "</textarea>";
        b += '<div class="responses-container" data-i="' + i + '">';
        (ia.Responses || []).forEach((r, rIdx) => {
            const rtext = r.Text || "";
            const nextId = r.NextInteractionID;
            b += '<div class="resp" data-i="' + i + '" data-r="' + rIdx + '">';
            b += '<div class="resp-header"><label>Réponse ' + (rIdx + 1) + " — Text</label>";
            b += '<button type="button" class="crud-btn crud-delete-response" data-i="' + i + '" data-r="' + rIdx + '" title="Supprimer cette réponse">✕</button></div>';
            b += '<textarea class="edit" data-type="response" data-i="' + i + '" data-r="' + rIdx + '" rows="2">' + escapeHtml(rtext) + "</textarea>";
            b += '<div class="scores">';
            for (const sk of SCORE_SKILLS) {
                const dims = r.SoftSkillDimensions || {};
                const val = dims[sk] != null ? dims[sk] : r[sk] != null ? r[sk] : 0;
                b += '<div class="score-item"><label>' + sk + "</label>";
                b += '<div class="score-stepper">';
                b += '<button type="button" class="score-btn score-minus" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '">-</button>';
                b += '<input type="hidden" class="score" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '" value="' + val + '">';
                b += '<span class="score-value" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '">' + val + "</span>";
                b += '<button type="button" class="score-btn score-plus" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '">+</button>';
                b += "</div></div>";
            }
            b += '<div class="score-item next-id-item"><label>Next Id</label>';
            b += '<input type="number" class="next-id" data-i="' + i + '" data-r="' + rIdx + '" value="' + (nextId != null ? nextId : "") + '"></div>';
            b += "</div></div>";
        });
        b += "</div>";
        b += '<button type="button" class="crud-btn crud-add-response" data-i="' + i + '">+ Ajouter une réponse</button>';
        b += '<button type="button" class="crud-btn crud-ai-response" data-i="' + i + '" data-ia-id="' + ia.Id + '">✨ Proposer une réponse avec IA</button>';
        b += '<button type="button" class="crud-btn crud-add-followup" data-ia-id="' + ia.Id + '" title="Crée une nouvelle interaction enchaînée à celle-ci, via une nouvelle réponse">↳ + Interaction enchaînée</button>';
        b += "</div>";
        blocksHtml += b;
    });
    blocksHtml +=
        '<div class="add-interaction-container">' +
        '<button type="button" class="crud-btn crud-add-interaction">+ Ajouter une interaction</button></div>';

    document.getElementById("ed-content").innerHTML = introHtml + blocksHtml;
    attachEditors(idx);
    attachCrudHandlers(idx);
}

function attachEditors(idx) {
    const ch = state.chaptersData.Chapters[0];
    const sc = ch.Scenes[idx];

    document.querySelectorAll("#ed-content .edit").forEach((el) => {
        el.addEventListener("input", function () {
            const type = this.dataset.type;
            const i = parseInt(this.dataset.i);
            if (type === "intro") {
                sc.SceneIntroduction = this.value;
            } else if (type === "name") {
                sc.Interactions[i].Name = this.value;
            } else if (type === "text") {
                sc.Interactions[i].Text = this.value;
                sc.Interactions[i].Name = this.value.substring(0, 50);
            } else if (type === "response") {
                const r = parseInt(this.dataset.r);
                sc.Interactions[i].Responses[r].Text = this.value;
                sc.Interactions[i].Responses[r].Name = this.value.substring(0, 80);
            }
            scheduleCacheSave();
        });
    });

    document.querySelectorAll("#ed-content .score-btn").forEach((btn) => {
        btn.addEventListener("click", function () {
            const i = parseInt(this.dataset.i);
            const r = parseInt(this.dataset.r);
            const skill = this.dataset.skill;
            const hidden = document.querySelector(
                '.score[data-i="' + i + '"][data-r="' + r + '"][data-skill="' + skill + '"]'
            );
            const valueEl = document.querySelector(
                '.score-value[data-i="' + i + '"][data-r="' + r + '"][data-skill="' + skill + '"]'
            );
            if (!hidden || !valueEl) return;
            let v = parseInt(hidden.value) || 0;
            v += this.classList.contains("score-plus") ? 1 : -1;
            if (v < -3) v = -3;
            if (v > 3) v = 3;
            hidden.value = String(v);
            valueEl.textContent = String(v);
            const resp = sc.Interactions[i].Responses[r];
            resp[skill] = v;
            if (resp.SoftSkillDimensions) resp.SoftSkillDimensions[skill] = v;
            scheduleCacheSave();
        });
    });

    document.querySelectorAll("#ed-content .next-id").forEach((el) => {
        el.addEventListener("change", function () {
            const i = parseInt(this.dataset.i);
            const r = parseInt(this.dataset.r);
            const raw = (this.value || "").trim();
            if (raw === "") {
                delete sc.Interactions[i].Responses[r].NextInteractionID;
                scheduleCacheSave();
                return;
            }
            const v = parseInt(raw, 10);
            if (isNaN(v)) {
                this.value = "";
                delete sc.Interactions[i].Responses[r].NextInteractionID;
                scheduleCacheSave();
                return;
            }
            sc.Interactions[i].Responses[r].NextInteractionID = v;
            scheduleCacheSave();
        });
    });
}

function attachCrudHandlers(idx) {
    document.querySelectorAll("#ed-content .crud-add-interaction").forEach((btn) => {
        btn.addEventListener("click", () => addInteraction(idx));
    });
    document.querySelectorAll("#ed-content .crud-add-followup").forEach((btn) => {
        btn.addEventListener("click", function () {
            const sourceId = parseInt(this.dataset.iaId, 10);
            addInteraction(idx, isNaN(sourceId) ? null : sourceId);
        });
    });
    document.querySelectorAll("#ed-content .crud-add-response").forEach((btn) => {
        btn.addEventListener("click", function () {
            addResponse(idx, parseInt(this.dataset.i));
        });
    });
    document.querySelectorAll("#ed-content .crud-delete-interaction").forEach((btn) => {
        btn.addEventListener("click", function () {
            deleteInteraction(idx, parseInt(this.dataset.i));
        });
    });
    document.querySelectorAll("#ed-content .crud-delete-response").forEach((btn) => {
        btn.addEventListener("click", function () {
            deleteResponse(idx, parseInt(this.dataset.i), parseInt(this.dataset.r));
        });
    });
    document.querySelectorAll("#ed-content .crud-ai-response").forEach((btn) => {
        btn.addEventListener("click", function () {
            import("./ai-modal.js").then((m) =>
                m.openAiProposalModal(idx, parseInt(this.dataset.i))
            );
        });
    });
}

function getActiveInteractionId() {
    const activeBlock = document.querySelector("#ed-content .block.active");
    if (!activeBlock) return null;
    const raw = activeBlock.dataset.interactionId;
    if (!raw) return null;
    const parsed = parseInt(raw, 10);
    return isNaN(parsed) ? null : parsed;
}

function linkInteractionFromSource(sourceIa, targetId) {
    if (!sourceIa) return;
    if (!sourceIa.Responses) sourceIa.Responses = [];
    const newRespId = getNextResponseId(sourceIa);
    const newResp = {
        Id: newRespId,
        Name: "",
        Text: "",
        NextInteractionID: targetId,
        SoftSkillDimensions: {},
    };
    for (const sk of SCORE_SKILLS) {
        newResp[sk] = 0;
        newResp.SoftSkillDimensions[sk] = 0;
    }
    sourceIa.Responses.push(newResp);
}

export function addInteraction(idx, sourceInteractionId) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    const sc = chapter.Scenes[idx];
    const newId = getNextInteractionId(sc);

    const srcId =
        sourceInteractionId != null ? sourceInteractionId : getActiveInteractionId();
    const sourceIa =
        srcId != null ? sc.Interactions.find((i) => i.Id === srcId) : null;

    const firstActor =
        sc.Interactions && sc.Interactions.length > 0 && sc.Interactions[0].Actor
            ? JSON.parse(JSON.stringify(sc.Interactions[0].Actor))
            : { Id: 0, Name: "Nouveau" };
    const newIa = {
        Id: newId,
        Name: "Nouvelle interaction " + newId,
        Actor: firstActor,
        Text: "",
        AgentFacialExpression: "",
        Responses: [],
    };
    sc.Interactions.push(newIa);

    if (sourceIa) linkInteractionFromSource(sourceIa, newId);

    scheduleCacheSave();
    rebuildEditorHtml(idx);
    rebuildSceneGraph(idx);
    showOnlySelectedBlock(String(newId));
    const block = document.querySelector('.block[data-interaction-id="' + newId + '"]');
    if (block) block.scrollIntoView({ behavior: "smooth", block: "start" });
}

export function deleteInteraction(idx, iIdx) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    const sc = chapter.Scenes[idx];
    const ia = sc.Interactions[iIdx];
    if (!ia) return;
    const deletedId = ia.Id;
    confirmDialog(
        "Supprimer l'interaction " + deletedId + " et toutes ses réponses ?"
    ).then((ok) => {
        if (!ok) return;
        sc.Interactions.splice(iIdx, 1);
        for (const otherIa of sc.Interactions) {
            for (const r of otherIa.Responses || []) {
                if (r.NextInteractionID === deletedId) r.NextInteractionID = -1;
            }
        }
        scheduleCacheSave();
        rebuildEditorHtml(idx);
        rebuildSceneGraph(idx);
        showOnlySelectedBlock(null);
    });
}

export function addResponse(idx, iIdx) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    const sc = chapter.Scenes[idx];
    const ia = sc.Interactions[iIdx];
    if (!ia) return;
    if (!ia.Responses) ia.Responses = [];
    const newRespId = getNextResponseId(ia);
    const newResp = {
        Id: newRespId,
        Name: "",
        Text: "",
        NextInteractionID: -1,
        SoftSkillDimensions: {},
    };
    for (const sk of SCORE_SKILLS) {
        newResp[sk] = 0;
        newResp.SoftSkillDimensions[sk] = 0;
    }
    ia.Responses.push(newResp);
    scheduleCacheSave();
    rebuildEditorHtml(idx);
    rebuildSceneGraph(idx);
    showOnlySelectedBlock(String(ia.Id));
}

export function deleteResponse(idx, iIdx, rIdx) {
    const chapter = state.chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    const sc = chapter.Scenes[idx];
    const ia = sc.Interactions[iIdx];
    if (!ia || !ia.Responses || !ia.Responses[rIdx]) return;
    confirmDialog(
        "Supprimer la réponse " + (rIdx + 1) + " de l'interaction " + ia.Id + " ?"
    ).then((ok) => {
        if (!ok) return;
        ia.Responses.splice(rIdx, 1);
        scheduleCacheSave();
        rebuildEditorHtml(idx);
        rebuildSceneGraph(idx);
        showOnlySelectedBlock(String(ia.Id));
    });
}

export function updateValidation() {
    const errs = [];
    const ch = state.chaptersData.Chapters[0];
    for (const sc of ch.Scenes) {
        const ids = {};
        for (const ia of sc.Interactions) ids[ia.Id] = true;
        for (const ia of sc.Interactions) {
            for (const r of ia.Responses || []) {
                const nid = r.NextInteractionID;
                if (nid != null && nid !== -1 && !ids[nid]) {
                    errs.push("EG-7: NextInteractionID " + nid + " invalide (scène " + sc.Title + ")");
                }
            }
        }
    }
    const div = document.getElementById("validation");
    if (errs.length > 0) {
        div.className = "validation";
        div.textContent = errs.join(" ; ");
    } else {
        div.className = "validation ok";
        div.textContent = "EG-7 : Validation OK — NextInteractionID valides.";
    }
}
