// Store singleton — toutes les variables d'état de l'éditeur de chapitre.
// Initialisé depuis window.PA_INIT (injecté par le template Jinja).

import { emptyScores } from "../shared/skills.js";

const init = window.PA_INIT || {};

export const config = {
    chapterId: String(init.chapterId || ""),
    bookSlug: String(init.bookSlug || ""),
    bookJson: String(init.bookJson || ""),
    // Fichier source du livre, figé au chargement (bookJson, lui, affiche le
    // nom de l'archive après une sauvegarde). Sert à valider le cache local.
    bookSource: String(init.bookJson || ""),
    apiSaveUrl: init.apiSaveUrl || "/api/save",
    apiEnrichUrl: init.apiEnrichUrl || "/api/enrich",
    imagesBaseUrl: init.imagesBaseUrl || "/api/data/images/",
};

// Les 7 dimensions vivent dans shared/skills.js (partagé avec le parcours
// joueur) ; on les ré-exporte pour ne rien casser des imports existants.
export { SCORE_SKILLS, SKILL_LABELS_FR } from "../shared/skills.js";

export const state = {
    chaptersData: init.chaptersData || { Chapters: [] },
    scenesData: init.scenesData || [],

    currentSceneIdx: 0,
    currentMode: "edit",
    leftPanelHidden: false,
    rightPanelHidden: false,

    network: null,
    nodesDS: null,
    edgesDS: null,
    container: null,
    sceneNodePositions: {},

    parcoursPath: { nodes: [], edges: [] },
    parcoursCurrent: null,
    parcoursScores: emptyScores(),

    cacheSaveTimer: null,
    cacheKey:
        "eol_graph_cache_v4_book_" +
        String(init.bookSlug || "default") +
        "_chapter_" +
        String(init.chapterId || ""),
};

export function resetParcours() {
    state.parcoursPath = { nodes: [], edges: [] };
    state.parcoursCurrent = null;
    state.parcoursScores = emptyScores();
}
