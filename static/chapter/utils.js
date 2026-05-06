// Helpers communs (HTML escape, confirm dialog, ID helpers).

export function esc(s) {
    if (!s) return "";
    return String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}

export const escapeHtml = esc;

export function confirmDialog(message) {
    return new Promise((resolve) => {
        const ov = document.createElement("div");
        ov.className = "confirm-overlay";
        ov.innerHTML =
            '<div class="confirm-box"><p>' +
            esc(message) +
            '</p><div class="confirm-actions">' +
            '<button class="confirm-yes">Supprimer</button>' +
            '<button class="confirm-no">Annuler</button>' +
            "</div></div>";
        document.body.appendChild(ov);
        ov.querySelector(".confirm-yes").addEventListener("click", () => {
            document.body.removeChild(ov);
            resolve(true);
        });
        ov.querySelector(".confirm-no").addEventListener("click", () => {
            document.body.removeChild(ov);
            resolve(false);
        });
    });
}

export function getNextInteractionId(scene) {
    let maxId = 0;
    for (const ia of scene.Interactions || []) {
        if (ia.Id > maxId) maxId = ia.Id;
    }
    return maxId + 1;
}

export function getNextResponseId(interaction) {
    let maxId = 0;
    for (const r of interaction.Responses || []) {
        if (r.Id > maxId) maxId = r.Id;
    }
    return maxId + 1;
}

export function getInteractionIdFromNodeId(nodeId, nodesDS) {
    if (!nodeId || !nodesDS) return "";
    const node = nodesDS.get(nodeId);
    if (node && node.interaction_id != null) return String(node.interaction_id);
    const raw = String(nodeId);
    const pos = raw.lastIndexOf("_I");
    if (pos >= 0) return raw.substring(pos + 2);
    return "";
}
