// Persistance : localStorage (positions de nœuds, mode courant) et /api/save.

import { config, state } from "./store.js";

export function scheduleCacheSave() {
    if (state.cacheSaveTimer) clearTimeout(state.cacheSaveTimer);
    state.cacheSaveTimer = setTimeout(saveCacheToLocalStorage, 120);
}

export function saveCacheToLocalStorage() {
    try {
        const payload = {
            version: 1,
            chapterId: config.chapterId,
            currentSceneIdx: state.currentSceneIdx,
            currentMode: state.currentMode,
            leftPanelHidden: state.leftPanelHidden,
            rightPanelHidden: state.rightPanelHidden,
            chaptersData: state.chaptersData,
            sceneNodePositions: state.sceneNodePositions,
        };
        localStorage.setItem(state.cacheKey, JSON.stringify(payload));
    } catch (err) {
        console.warn("saveCacheToLocalStorage:", err);
    }
}

export function restoreCacheFromLocalStorage() {
    try {
        const raw = localStorage.getItem(state.cacheKey);
        if (!raw) return;
        const parsed = JSON.parse(raw);
        if (!parsed || parsed.chapterId !== config.chapterId) return;
        if (
            parsed.chaptersData &&
            parsed.chaptersData.Chapters &&
            parsed.chaptersData.Chapters.length > 0
        ) {
            state.chaptersData = parsed.chaptersData;
        }
        if (
            parsed.sceneNodePositions &&
            typeof parsed.sceneNodePositions === "object"
        ) {
            state.sceneNodePositions = parsed.sceneNodePositions;
        }
        if (typeof parsed.currentSceneIdx === "number") {
            state.currentSceneIdx = parsed.currentSceneIdx;
        }
        if (parsed.currentMode === "edit" || parsed.currentMode === "parcours") {
            state.currentMode = parsed.currentMode;
        }
        state.leftPanelHidden = !!parsed.leftPanelHidden;
        state.rightPanelHidden = !!parsed.rightPanelHidden;
    } catch (err) {
        console.warn("restoreCacheFromLocalStorage:", err);
    }
}

export function getScenePositionKey(idx) {
    const s = state.scenesData[idx];
    if (!s) return String(idx || 0);
    return s.scene_id != null ? String(s.scene_id) : String(idx || 0);
}

export function saveCurrentScenePositions() {
    try {
        if (!state.network || !state.nodesDS) return;
        const ids = state.nodesDS.getIds();
        if (!ids || ids.length === 0) return;
        const key = getScenePositionKey(state.currentSceneIdx);
        state.sceneNodePositions[key] = state.network.getPositions(ids);
        scheduleCacheSave();
    } catch (err) {
        console.warn("saveCurrentScenePositions:", err);
    }
}

export function applyCurrentScenePositions(idx) {
    try {
        if (!state.network || !state.nodesDS) return;
        const key = getScenePositionKey(idx);
        const pos = state.sceneNodePositions[key];
        if (!pos) return;
        for (const nodeId of Object.keys(pos)) {
            const p = pos[nodeId];
            if (p && typeof p.x === "number" && typeof p.y === "number") {
                state.network.moveNode(nodeId, p.x, p.y);
            }
        }
    } catch (err) {
        console.warn("applyCurrentScenePositions:", err);
    }
}

export function postSave() {
    return fetch(config.apiSaveUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            book_slug: config.bookSlug,
            Chapters: state.chaptersData.Chapters,
        }),
    }).then((r) => r.json().then((d) => ({ ok: r.ok, data: d })));
}

export function downloadJsonExport() {
    const blob = new Blob([JSON.stringify(state.chaptersData, null, 2)], {
        type: "application/json",
    });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "Chapitre_" + config.chapterId + "_modified.json";
    a.click();
}
