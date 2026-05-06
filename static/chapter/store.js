// Store singleton — toutes les variables d'état de l'éditeur de chapitre.
// Initialisé depuis window.PA_INIT (injecté par le template Jinja).

const init = window.PA_INIT || {};

export const config = {
    chapterId: String(init.chapterId || ""),
    bookSlug: String(init.bookSlug || ""),
    apiSaveUrl: init.apiSaveUrl || "/api/save",
    apiEnrichUrl: init.apiEnrichUrl || "/api/enrich",
    imagesBaseUrl: init.imagesBaseUrl || "/api/data/images/",
};

export const SCORE_SKILLS = [
    "RespectAndDignity",
    "Empathy",
    "Compassion",
    "EmotionalRegulation",
    "CommunicationClarity",
    "ProfessionalBoundaries",
    "InterprofessionalCollaboration",
];

export const SKILL_LABELS_FR = {
    RespectAndDignity: "Respect et dignité",
    Empathy: "Empathie",
    Compassion: "Compassion",
    EmotionalRegulation: "Régulation émotionnelle",
    CommunicationClarity: "Clarté communication",
    ProfessionalBoundaries: "Frontières pro.",
    InterprofessionalCollaboration: "Collab. interpro.",
};

function emptyScores() {
    const obj = {};
    for (const sk of SCORE_SKILLS) obj[sk] = 0;
    return obj;
}

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
