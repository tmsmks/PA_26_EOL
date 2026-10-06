// Source unique des 7 dimensions de soft skills, partagée par l'éditeur et le
// parcours joueur. Doit rester alignée avec domain/soft_skills.py côté serveur.

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

export function emptyScores() {
    const obj = {};
    for (const sk of SCORE_SKILLS) obj[sk] = 0;
    return obj;
}
