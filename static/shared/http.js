// Appels JSON vers le serveur, avec le jeton CSRF exposé par la page
// (<meta name="csrf-token">). Toute requête qui modifie l'état doit l'envoyer.

export function csrfToken() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    return meta ? meta.content : "";
}

export function jsonHeaders() {
    return { "Content-Type": "application/json", "X-CSRF-Token": csrfToken() };
}

/** POST JSON ; rejette avec le message d'erreur du serveur si !ok. */
export async function postJSON(url, body) {
    const r = await fetch(url, {
        method: "POST",
        headers: jsonHeaders(),
        body: JSON.stringify(body || {}),
    });
    if (r.status === 401) {
        const next = window.location.pathname + window.location.search;
        window.location.href = "/login?next=" + encodeURIComponent(next);
        throw new Error("Connexion requise.");
    }
    let data = {};
    try {
        data = await r.json();
    } catch (e) {
        /* réponse vide ou non JSON */
    }
    if (!r.ok) throw new Error(data.error || "Erreur " + r.status);
    return data;
}
