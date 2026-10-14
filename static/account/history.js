// Historique : profil de compétences du livre et courbe de chaque chapitre rejoué.

import { skillRose, trendLine } from "./charts.js";

const H = window.PA_HISTORY || { books: [] };

H.books.forEach((book) => {
    const profile = document.querySelector('[data-chart="profile"][data-book="' + book.slug + '"]');
    if (profile && book.profile && book.profile.global !== null) {
        skillRose(profile, {
            skills: H.skills,
            labels: H.labels,
            current: book.profile.scores,
            currentLabel: "Profil du livre",
            strengths: book.profile.strengths,
            weaknesses: book.profile.weaknesses,
        });
    }

    (book.chapters || []).forEach((ch) => {
        const el = document.querySelector(
            '[data-chart="chapter"][data-book="' + book.slug + '"][data-chapter="' + ch.id + '"]'
        );
        if (el) trendLine(el, ch.points, { prefix: "P", unit: "Passage", label: "Qualité des choix" });
    });
});
