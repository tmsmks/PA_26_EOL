// Entry point — initialisation et wiring des event listeners.

import { state } from "./store.js";
import {
    applyPanelVisibility,
    showScene,
} from "./network.js";
import { setMode, showParcoursScene } from "./parcours.js";
import {
    downloadJsonExport,
    postSave,
    restoreCacheFromLocalStorage,
    saveCacheToLocalStorage,
    saveCurrentScenePositions,
    scheduleCacheSave,
} from "./persistence.js";

function init() {
    if (typeof vis === "undefined") {
        state.container.innerHTML =
            "<p style='color:#ef4444;padding:20px'>vis-network non chargé. Vérifiez votre connexion et rechargez.</p>";
        return;
    }
    restoreCacheFromLocalStorage();
    applyPanelVisibility();

    if (state.scenesData && state.scenesData.length > 0) {
        if (state.currentSceneIdx < 0 || state.currentSceneIdx >= state.scenesData.length) {
            state.currentSceneIdx = 0;
        }
        try {
            showScene(state.currentSceneIdx);
            setMode(state.currentMode);
        } catch (err) {
            console.error("showScene:", err);
            state.container.innerHTML =
                "<p style='color:#ef4444;padding:20px'>Erreur: " +
                String(err.message || err) + "</p>";
        }
    } else {
        document.getElementById("ed-content").innerHTML =
            "<div class='empty'>Aucune donnée (erreur de chargement?).</div>";
    }
}

function runInit() {
    if (typeof vis !== "undefined") {
        init();
        return;
    }
    let n = 0;
    const t = setInterval(() => {
        n++;
        if (typeof vis !== "undefined") {
            clearInterval(t);
            init();
        } else if (n > 60) {
            clearInterval(t);
            state.container.innerHTML =
                "<p style='color:#ef4444;padding:20px'>vis-network timeout.</p>";
        }
    }, 100);
}

function wireEventListeners() {
    document.querySelectorAll(".scene-btn").forEach((b) => {
        b.addEventListener("click", function () {
            showScene(parseInt(this.dataset.idx));
        });
    });

    document.getElementById("chapter-select").addEventListener("change", function () {
        const target = (this.value || "").trim();
        if (target) {
            saveCurrentScenePositions();
            saveCacheToLocalStorage();
            window.location.href = target;
        }
    });

    document.querySelectorAll(".mode-btn").forEach((b) => {
        b.addEventListener("click", function () {
            setMode(this.dataset.mode);
        });
    });

    document.getElementById("toggle-left-panel").addEventListener("click", () => {
        state.leftPanelHidden = !state.leftPanelHidden;
        applyPanelVisibility();
        scheduleCacheSave();
    });

    document.getElementById("toggle-right-panel").addEventListener("click", () => {
        state.rightPanelHidden = !state.rightPanelHidden;
        applyPanelVisibility();
        scheduleCacheSave();
    });

    document.getElementById("parcours-restart").addEventListener("click", () => {
        if (state.scenesData.length > 0) showParcoursScene(state.currentSceneIdx);
    });

    document.getElementById("search").addEventListener("input", function () {
        const q = (this.value || "").toLowerCase();
        document.querySelectorAll(".scene-btn").forEach((b) => {
            b.style.display =
                q && b.textContent.toLowerCase().indexOf(q) < 0 ? "none" : "block";
        });
        if (state.scenesData && state.scenesData.length > 0) {
            const visQuery = (this.value || "").toLowerCase();
            if (visQuery && state.nodesDS && state.edgesDS) {
                for (const nid of state.nodesDS.getIds()) {
                    const node = state.nodesDS.get(nid);
                    const match =
                        (node.label && node.label.toLowerCase().indexOf(visQuery) >= 0) ||
                        (node.title && node.title.toLowerCase().indexOf(visQuery) >= 0);
                    state.nodesDS.update({ id: nid, hidden: !match });
                }
            } else if (state.nodesDS) {
                for (const nid of state.nodesDS.getIds()) {
                    state.nodesDS.update({ id: nid, hidden: false });
                }
            }
        }
    });

    window.addEventListener("beforeunload", () => {
        saveCurrentScenePositions();
        saveCacheToLocalStorage();
    });

    document.getElementById("save-btn").addEventListener("click", function () {
        const btn = this;
        const statusEl = document.getElementById("save-status");
        btn.disabled = true;
        statusEl.className = "";
        statusEl.textContent = "Enregistrement…";
        postSave()
            .then((result) => {
                btn.disabled = false;
                if (result.ok) {
                    statusEl.className = "save-ok";
                    statusEl.textContent = result.data.message || "Sauvegardé.";
                } else {
                    statusEl.className = "save-err";
                    statusEl.textContent =
                        result.data.error ||
                        "Erreur. Utilisez python app.py pour activer la sauvegarde directe.";
                }
            })
            .catch(() => {
                btn.disabled = false;
                statusEl.className = "save-err";
                statusEl.textContent =
                    "Erreur réseau. Lancez python app.py puis ouvrez http://localhost:8765";
            });
    });

    document.getElementById("export-btn").addEventListener("click", downloadJsonExport);
}

window.addEventListener("load", () => {
    state.container = document.getElementById("network");
    wireEventListeners();
    setTimeout(runInit, 80);
});
