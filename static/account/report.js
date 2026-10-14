// Bilan d'une session : graphiques + feedback général (généré au 1er affichage).

import { postJSON } from "../shared/http.js";
import { esc, heatmap, skillRose, trendLine } from "./charts.js";

const R = window.PA_REPORT || {};
const results = R.results || {};
const labels = R.labels || {};
const $ = (id) => document.getElementById(id);

skillRose($("skills-chart"), {
    skills: R.skills,
    labels: labels,
    current: results.scores || {},
    compare: R.previous ? R.previous.scores : null,
    currentLabel: "Session " + R.session.number,
    compareLabel: R.previous ? "Session " + R.previous.number : "",
    strengths: results.strengths,
    weaknesses: results.weaknesses,
});

heatmap($("heatmap"), {
    chapters: results.chapters || [],
    skills: R.skills,
    labels: labels,
    rework: results.chapters_to_rework || [],
});

if ($("trend")) trendLine($("trend"), R.points || [], { highlight: R.session.number });

/* --- Feedback --- */

function chapterName(id) {
    const ch = (results.chapters || []).find((c) => c.id === id);
    return ch ? ch.name : "";
}

function skillList(items) {
    if (!items || !items.length) return '<p class="acc-hint">—</p>';
    const score = (k) =>
        results.scores && results.scores[k] != null ? " · " + Math.round(results.scores[k]) + "/100" : "";
    return (
        "<ul>" +
        items
            .map(
                (it) =>
                    "<li><strong>" + esc(labels[it.skill] || it.skill) + score(it.skill) + "</strong>" +
                    esc(it.text) + "</li>"
            )
            .join("") +
        "</ul>"
    );
}

function renderFeedback(fb) {
    const box = $("feedback-body");
    const rework = (fb.chapters_to_rework || [])
        .map(
            (c) =>
                '<a href="' + esc(R.playBookUrl + "chapters/" + c.chapter_id) + '">' +
                '<span class="fb-ch">Chapitre ' + esc(c.chapter_id) + " · " + esc(chapterName(c.chapter_id)) + "</span>" +
                '<span class="fb-why">' + esc(c.reason) + "</span>" +
                '<span class="fb-go">Rejouer ce chapitre →</span></a>'
        )
        .join("");
    const date = fb.generated_at ? new Date(fb.generated_at).toLocaleDateString("fr-CH") : "";
    const source =
        fb.source === "ai"
            ? "Rédigé par l'IA à partir de vos scores" + (R.previous ? " et de vos sessions précédentes" : "")
            : "Feedback automatique (IA indisponible)";

    box.innerHTML =
        '<p class="fb-summary">' + esc(fb.summary) + "</p>" +
        (fb.progression
            ? '<p class="fb-progress"><strong>Votre progression.</strong> ' + esc(fb.progression) + "</p>"
            : "") +
        '<div class="fb-cols">' +
        '<div class="fb-box"><h3><span class="fb-icon-up" aria-hidden="true">▲</span>Points forts</h3>' +
        skillList(fb.strengths) + "</div>" +
        '<div class="fb-box"><h3><span class="fb-icon-down" aria-hidden="true">▼</span>Points faibles</h3>' +
        skillList(fb.weaknesses) + "</div>" +
        "</div>" +
        (fb.improvements && fb.improvements.length
            ? "<h3>Ce que vous pouvez améliorer</h3><ol class=\"fb-steps\">" +
              fb.improvements.map((s) => "<li>" + esc(s) + "</li>").join("") +
              "</ol>"
            : "") +
        (rework ? "<h3>Chapitres à retravailler</h3><div class=\"fb-rework\">" + rework + "</div>" : "") +
        '<div class="fb-meta"><span>' + esc(source) + (date ? " · " + esc(date) : "") + "</span>" +
        (R.canRegenerate
            ? '<button type="button" id="fb-regen">' +
              (fb.source === "ai" ? "Régénérer" : "Réessayer avec l'IA") +
              "</button>"
            : "") +
        "</div>";

    const regen = $("fb-regen");
    if (regen) regen.addEventListener("click", () => loadFeedback(true));
}

function loadFeedback(regenerate) {
    const box = $("feedback-body");
    box.innerHTML =
        '<p class="fb-loading"><span class="fb-spinner" aria-hidden="true"></span>' +
        "Analyse de votre parcours" + (R.previous ? " et de vos sessions précédentes" : "") + "…</p>";
    postJSON(R.feedbackUrl, { regenerate: !!regenerate }).then(
        (data) => {
            R.feedback = data.feedback;
            R.canRegenerate = R.canRegenerate || data.feedback.source !== "ai";
            renderFeedback(data.feedback);
        },
        (err) => {
            box.innerHTML =
                '<p class="form-error">Le feedback n\'a pas pu être chargé : ' + esc(err.message) + "</p>" +
                '<div class="fb-meta"><span></span><button type="button" id="fb-retry">Réessayer</button></div>';
            $("fb-retry").addEventListener("click", () => loadFeedback(false));
        }
    );
}

if (R.session.status === "completed") {
    if (R.feedback) renderFeedback(R.feedback);
    else loadFeedback(false);
}
