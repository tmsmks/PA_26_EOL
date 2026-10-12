// Parcours joueur — rendu et interactions. Le moteur vit dans engine.js.
//
// Chaque scène terminée est envoyée au serveur (indices des réponses choisies),
// qui la rejoue et la note : la session du participant suit ses choix et ses
// états narratifs d'un chapitre à l'autre, sur n'importe quel appareil.
// Jouer un chapitre = un passage (unité de note) : il est ouvert au clic sur
// « Commencer », et le serveur dit avec quels états narratifs repartir.

import { postJSON } from "../shared/http.js";
import { SKILL_LABELS_FR } from "../shared/skills.js";
import { createAudio } from "./audio.js";
import {
    SCORE_SKILLS,
    appraise,
    applyFlags,
    choose,
    createGame,
    enterChapter,
    flagList,
    goToNextScene,
    hasNextScene,
    needsStartChoice,
    resolveEntry,
    scene,
    sceneCount,
    sceneNumber,
    setFlags,
    startScene,
} from "./engine.js";

const init = window.PA_PLAY || {};
const meta = init.chapterMeta || {};
const IMAGES = init.imagesBaseUrl || "/api/data/images/";

// Session du livre en cours (null tant que le joueur n'a pas commencé).
let session = init.session || null;
// Passage du chapitre (ouvert au démarrage).
let passage = null;

const game = createGame(init.scenesData || [], {
    flags: session ? session.flags : [],
    ownedFlags: meta.owned_flags || [],
});

// Lecture audio (si le navigateur sait lire à voix haute) : chaque écran lui est
// décrit, il le lit quand le participant l'a activée.
const audio = createAudio();
// Dernier personnage annoncé : on ne répète pas son nom à chaque réplique.
let lastSpeaker = null;

/** Titre sans son numéro (« 5.1 La table de la cuisine » → « La table de la cuisine »). */
function spokenTitle(title) {
    return String(title || "").replace(/^\d+(?:\.\d+)*\s+/, "");
}

function numbered(texts) {
    return texts.map((t, i) => "Réponse " + (i + 1) + " : " + t);
}

/* --- Synchronisation serveur --- */

// Les envois partent dans l'ordre : une fin de chapitre n'est jamais
// enregistrée avant la dernière scène.
let queue = Promise.resolve();

function enqueue(task) {
    const run = queue.then(task);
    queue = run.catch(() => {});
    return run;
}

async function ensureSession() {
    if (session) return session;
    const data = await postJSON(init.startSessionUrl);
    session = data.session;
    setFlags(game, session.flags);
    return session;
}

async function startPassage() {
    const data = await postJSON(session.urls.passages, { chapter_id: init.chapterId });
    passage = data.passage;
    setFlags(game, passage.flags);
    return passage;
}

function fmtNote(v) {
    return v === null || v === undefined ? "—" : String(Math.round(v));
}

function setStatus(el, text, tone) {
    el.textContent = text;
    el.className = "save-status" + (tone ? " is-" + tone : "");
    el.hidden = !text;
}

// Fin de scène affichée en dernier : un retour arrivé en retard ne s'affiche
// pas sur le bilan de la scène suivante.
let reviewToken = 0;

function recordScene() {
    const s = scene(game);
    const status = $("save-status");
    const token = ++reviewToken;
    if (!session || !s || game.entryId === "") {
        setStatus(status, "", "");
        return;
    }
    const body = {
        chapter_id: init.chapterId,
        scene_id: s.scene_id,
        entry_id: parseInt(game.entryId, 10),
        choices: game.choices.slice(),
        flags: flagList(game),
        passage_id: passage ? passage.id : undefined,
    };
    const send = () => {
        setStatus(status, "Enregistrement…", "");
        enqueue(() => postJSON(session.urls.attempts, body)).then(
            (res) => {
                if (token === reviewToken) renderReview(res.review);
                setStatus(
                    status,
                    res.counted
                        ? "Scénario enregistré : il compte dans votre niveau du chapitre."
                        : passage && !passage.counted
                          ? "Passage d'entraînement : ce scénario est enregistré, sans être noté."
                          : "Scénario rejoué : seule votre première tentative est notée dans ce passage.",
                    res.counted ? "ok" : "info"
                );
            },
            (err) => {
                setStatus(status, "Non enregistré : " + err.message + " — cliquez pour réessayer.", "error");
                status.onclick = () => {
                    status.onclick = null;
                    send();
                };
            }
        );
    };
    send();
}

function completeChapter() {
    const status = $("end-status");
    const report = $("btn-report");
    report.hidden = true;
    if (!session) return;
    const send = () => {
        setStatus(status, "Enregistrement…", "");
        enqueue(() =>
            postJSON(session.urls.complete, { chapter_id: init.chapterId, flags: flagList(game) })
        ).then(
            (res) => {
                session = res.session;
                renderEndScore(res.passage, res.progress);
                const done = session.completed_chapters.length;
                if (res.book_completed) {
                    setStatus(status, "Livre terminé ! Votre bilan de la session " + session.number + " est prêt.", "ok");
                    report.href = session.urls.report;
                    report.hidden = false;
                    const nextLink = $("btn-next-chapter");
                    if (nextLink) nextLink.className = "ghost-btn";
                } else {
                    setStatus(
                        status,
                        "Session " + session.number + " · " + done + " chapitre" + (done > 1 ? "s" : "") +
                            " sur " + init.chapterCount + " terminé" + (done > 1 ? "s" : "") + ".",
                        "info"
                    );
                }
            },
            (err) => {
                setStatus(status, "Non enregistré : " + err.message + " — cliquez pour réessayer.", "error");
                status.onclick = () => {
                    status.onclick = null;
                    send();
                };
            }
        );
    };
    send();
}

function renderEndScore(p, progress) {
    const el = $("end-score");
    if (!p || p.global === null || p.global === undefined) {
        el.hidden = true;
        return;
    }
    let html = "Qualité de vos choix dans ce chapitre : <strong>" + fmtNote(p.global) + "/100</strong>.";
    if (!p.counted) {
        html += " Passage d'entraînement : il n'entre pas dans votre niveau.";
    } else if (progress) {
        html +=
            " Niveau du chapitre : <strong>" + fmtNote(progress.level) + "/100</strong>" +
            (progress.margin !== null && progress.margin !== undefined ? " (± " + fmtNote(progress.margin) + ")" : "") +
            (progress.n_passages > 1 ? ", " + progress.n_passages + " passages notés" : "") +
            (progress.progression !== null && progress.progression !== undefined
                ? ", progression " + (progress.progression > 0 ? "+" : "") + fmtNote(progress.progression) + " %"
                : "") +
            ".";
    }
    el.innerHTML = html;
    el.hidden = false;
    audio.append({ parts: [el.textContent] });
}

const $ = (id) => document.getElementById(id);
const SCREENS = [
    "screen-intro",
    "screen-start-choice",
    "screen-scene-intro",
    "screen-dialogue",
    "screen-debrief",
    "screen-end",
];

function esc(s) {
    if (s === null || s === undefined) return "";
    return String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}

function show(id) {
    SCREENS.forEach((s) => {
        $(s).hidden = s !== id;
    });
    $("keyhint").hidden = id !== "screen-dialogue";
}

// Tant que le chapitre n'a pas commencé, la scène dépend peut-être d'états
// encore inconnus (choix de départ) : on n'affiche pas de titre.
let entered = false;

function updateHud() {
    const s = entered ? scene(game) : null;
    $("hud-scene").textContent = s ? s.title : "";
    const pct = sceneCount(game)
        ? Math.round(((sceneNumber(game) - 1) / sceneCount(game)) * 100)
        : 0;
    $("hud-bar").style.width = pct + "%";
}

/* --- Portrait : dégrade proprement quand l'image n'existe pas encore --- */

function initials(name) {
    return String(name || "?")
        .replace(/^(Dr|Dre|M\.|Mme|Mlle)\s+/i, "")
        .split(/\s+/)
        .slice(0, 2)
        .map((w) => w.charAt(0).toUpperCase())
        .join("");
}

function renderPortrait(entry) {
    const el = $("portrait");
    el.innerHTML = "";
    el.classList.remove("has-image");
    const fallback = document.createElement("span");
    fallback.className = "portrait-initials";
    fallback.textContent = initials(entry.actor);
    el.appendChild(fallback);

    if (!entry.image) return;
    const img = new Image();
    img.alt = "";
    img.addEventListener("load", () => {
        el.innerHTML = "";
        el.appendChild(img);
        el.classList.add("has-image");
    });
    img.src = IMAGES + encodeURIComponent(entry.image);
}

/* --- Dialogue --- */

// Ordre d'affichage des réponses mélangé : la meilleure réponse n'est pas
// toujours la première. Stable dans un passage (graine = nœud + passage),
// différent d'un passage à l'autre : rejouer un chapitre ne se fait pas par
// cœur de position.
function seedOf(text) {
    let h = 2166136261;
    for (let i = 0; i < text.length; i++) {
        h ^= text.charCodeAt(i);
        h = Math.imul(h, 16777619);
    }
    return h >>> 0 || 1;
}

function stableShuffle(list, seed) {
    const out = list.slice();
    let x = seedOf(seed);
    for (let i = out.length - 1; i > 0; i--) {
        x ^= x << 13;
        x ^= x >>> 17;
        x ^= x << 5;
        x >>>= 0;
        const j = x % (i + 1);
        [out[i], out[j]] = [out[j], out[i]];
    }
    return out;
}

let typing = null;

function typeText(node, text) {
    if (typing) window.clearInterval(typing);
    const full = String(text || "—");
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        node.textContent = full;
        return;
    }
    node.textContent = "";
    let i = 0;
    typing = window.setInterval(() => {
        i += 2;
        node.textContent = full.slice(0, i);
        if (i >= full.length) {
            window.clearInterval(typing);
            typing = null;
        }
    }, 12);
}

function finishTyping() {
    if (!typing) return false;
    window.clearInterval(typing);
    typing = null;
    const s = game.current;
    $("dialogue-text").textContent = s ? s.text || "—" : "";
    return true;
}

function renderDialogue() {
    const entry = game.current;
    if (!entry) return renderDebrief();

    show("screen-dialogue");
    // Sans acteur, l'interaction est une narration : pas de portrait.
    $("screen-dialogue").classList.toggle("is-narration", !entry.actor);
    // Sans image prévue, un petit avatar à côté du nom plutôt qu'un grand cadre vide.
    $("screen-dialogue").classList.toggle("no-image", !!entry.actor && !entry.image);
    renderPortrait(entry);
    $("actor-name").textContent = entry.actor || "";
    typeText($("dialogue-text"), entry.text);

    const box = $("choices");
    box.innerHTML = "";
    const responses = entry.responses || [];
    const shuffled = stableShuffle(responses, (entry.node_id || "") + ":" + (passage ? passage.id : ""));

    // Le nom du personnage n'est lu que quand l'interlocuteur change.
    const announce = entry.actor && entry.actor !== lastSpeaker;
    lastSpeaker = entry.actor || null;
    audio.narrate({
        parts: [announce ? entry.actor + "." : "", entry.text],
        // Un seul bouton (« Continuer ») : rien à lire.
        choices: shuffled.length > 1 ? numbered(shuffled.map((r) => r.text)) : [],
    });

    if (!responses.length) {
        const btn = document.createElement("button");
        btn.className = "choice choice-continue";
        btn.textContent = "Continuer";
        btn.addEventListener("click", renderDebrief);
        box.appendChild(btn);
        return;
    }

    shuffled.forEach((r, idx) => {
        const btn = document.createElement("button");
        btn.className = "choice";
        btn.innerHTML =
            '<span class="choice-key">' + (idx + 1) + "</span>" +
            '<span class="choice-text">' + esc(r.text || "Continuer") + "</span>";
        btn.addEventListener("click", () => {
            choose(game, r);
            // Une interaction finale sans réponse est d'abord affichée (son texte
            // clôt la scène) ; son bouton « Continuer » mène au bilan.
            if (!game.current) renderDebrief();
            else renderDialogue();
        });
        box.appendChild(btn);
    });
}

/* --- Bilan --- */

/** Guillemets français, sauf si la réplique les porte déjà (comme quoted côté serveur). */
function quoted(text) {
    const t = String(text || "").trim();
    if (!t.includes("«")) return "« " + t + " »";
    const count = (c) => t.split(c).length - 1;
    return count("«") <= count("»") ? t : t + " »";
}

function clip(text, max) {
    const t = String(text || "");
    if (t.length <= max) return t;
    const cut = t.slice(0, max);
    const space = cut.lastIndexOf(" ");
    return (space > max * 0.6 ? cut.slice(0, space) : cut) + "…";
}

function reviewLine(who, text, critical) {
    return (
        '<p class="moment-line"><span class="who">' + esc(who) + "</span><span>" +
        esc(quoted(clip(text, 260))) +
        (critical ? ' <span class="crit-tag">Critique</span>' : "") +
        "</span></p>"
    );
}

function reviewWhy(rationale) {
    if (!rationale) return "";
    return '<p class="moment-why"><span class="who">Pourquoi</span><span>' + esc(rationale) + "</span></p>";
}

// Feedback d'abord (proposition v3) : les choix décisifs de la scène, la
// réponse attendue et sa justification, avant les points.
function renderReview(items) {
    const box = $("debrief-review");
    const list = $("review-list");
    list.innerHTML = "";
    items = Array.isArray(items) ? items : [];
    box.hidden = !items.length;
    $("review-critical-note").hidden = !items.some((it) => it.choice.critical);
    if (!items.length) return;
    const spoken = ["Ce qui était attendu."];
    items.forEach((it) => {
        const li = document.createElement("li");
        li.className = "moment" + (it.choice.critical ? " is-critical" : "");
        li.innerHTML =
            '<p class="moment-prompt">' + (it.actor ? esc(it.actor) + " : " : "") +
            esc(quoted(clip(it.prompt, 220))) + "</p>" +
            reviewLine(it.is_best ? "Votre réponse, la plus ajustée" : "Votre réponse", it.choice.text, it.choice.critical) +
            reviewWhy(it.choice.rationale) +
            (it.is_best ? "" : reviewLine("Plus ajustée", it.best.text, false) + reviewWhy(it.best.rationale));
        list.appendChild(li);
        spoken.push(
            "Votre réponse" + (it.choice.critical ? ", réponse critique" : "") + " : " + it.choice.text,
            it.choice.rationale ? "Pourquoi : " + it.choice.rationale : "",
            it.is_best ? "" : "Réponse la plus ajustée : " + it.best.text,
            !it.is_best && it.best.rationale ? "Pourquoi : " + it.best.rationale : ""
        );
    });
    audio.append({ parts: spoken });
}

function renderBars(container, scores) {
    const max = Math.max(
        3,
        ...SCORE_SKILLS.map((sk) => Math.abs(scores[sk] || 0))
    );
    container.innerHTML = "";
    SCORE_SKILLS.forEach((sk) => {
        const v = scores[sk] || 0;
        const pct = Math.round((Math.abs(v) / max) * 50);
        const row = document.createElement("div");
        row.className = "bar-row";
        row.innerHTML =
            '<span class="bar-label">' + esc(SKILL_LABELS_FR[sk] || sk) + "</span>" +
            '<span class="bar-track">' +
            '<span class="bar-fill ' + (v < 0 ? "neg" : "pos") + '"' +
            ' style="width:' + pct + "%;" + (v < 0 ? "right:50%" : "left:50%") + '"></span>' +
            "</span>" +
            '<span class="bar-value ' + (v < 0 ? "neg" : v > 0 ? "pos" : "") + '">' +
            (v > 0 ? "+" : "") + v + "</span>";
        container.appendChild(row);
    });
}

function renderDebrief() {
    finishTyping();
    const s = scene(game);
    const verdict = appraise(game.sceneScores, game.sceneBest, game);

    $("debrief-title").textContent = s ? s.title : "Scénario terminé";
    $("debrief-lead").textContent = verdict.lead;
    $("debrief-lead").className = "debrief-lead tone-" + verdict.tone;
    renderBars($("debrief-bars"), game.sceneScores);
    renderReview([]);

    $("btn-next").textContent = hasNextScene(game)
        ? "Scénario suivant"
        : "Terminer le chapitre";
    recordScene();
    show("screen-debrief");
    audio.narrate({ parts: ["Fin du scénario.", spokenTitle(s ? s.title : "") + ".", verdict.lead] });
}

function renderSceneIntro() {
    const s = scene(game);
    if (!s) return renderEnd();
    $("scene-counter").textContent =
        "Scénario " + sceneNumber(game) + " sur " + sceneCount(game);
    $("scene-title").textContent = s.title || "";
    const intro = resolveEntry(game).intro;
    $("scene-intro").textContent = intro;
    updateHud();
    show("screen-scene-intro");
    audio.narrate({
        parts: ["Scénario " + sceneNumber(game) + " sur " + sceneCount(game) + ".", spokenTitle(s.title) + ".", intro],
    });
}

function renderEnd() {
    $("end-title").textContent = init.chapterName || "Chapitre terminé";
    renderBars($("end-bars"), game.chapterScores);
    $("hud-bar").style.width = "100%";
    show("screen-end");
    audio.narrate({ parts: ["Chapitre terminé.", (init.chapterName || "") + "."] });
    completeChapter();
}

/* --- Choix de départ (chapitre qui dépend d'un chapitre non joué) --- */

function beginChapter() {
    entered = true;
    if (enterChapter(game)) renderSceneIntro();
    else renderEnd();
}

function renderStartChoice() {
    const sc = meta.start_choice;
    $("start-question").textContent = sc.question || "";
    const box = $("start-options");
    box.innerHTML = "";
    sc.options.forEach((opt, idx) => {
        const btn = document.createElement("button");
        btn.className = "choice";
        btn.innerHTML =
            '<span class="choice-key">' + (idx + 1) + "</span>" +
            '<span class="choice-text">' + esc(opt.label) + "</span>";
        btn.addEventListener("click", () => {
            applyFlags(game, opt.flags);
            beginChapter();
        });
        box.appendChild(btn);
    });
    show("screen-start-choice");
    audio.narrate({
        parts: ["Avant de commencer.", sc.question || ""],
        choices: numbered(sc.options.map((opt) => opt.label)),
    });
}

/* --- Câblage --- */

$("btn-start").addEventListener("click", async () => {
    const btn = $("btn-start");
    btn.disabled = true;
    try {
        await ensureSession();
        await startPassage();
    } catch (err) {
        setStatus($("start-status"), "Impossible de démarrer la session : " + err.message, "error");
        btn.disabled = false;
        return;
    }
    if (needsStartChoice(game, meta.start_choice)) renderStartChoice();
    else beginChapter();
});

$("btn-enter").addEventListener("click", () => {
    lastSpeaker = null;
    startScene(game);
    updateHud();
    if (!game.current) return renderDebrief();
    renderDialogue();
});

$("btn-replay").addEventListener("click", () => {
    lastSpeaker = null;
    startScene(game);
    renderDialogue();
});

$("btn-next").addEventListener("click", () => {
    if (goToNextScene(game)) renderSceneIntro();
    else renderEnd();
});

document.addEventListener("keydown", (e) => {
    const target = e.target instanceof Element ? e.target : null;
    // Dans un champ des réglages, les touches servent au champ (sauf Échap,
    // qui ferme le panneau).
    const inField = !!(target && target.closest("input, select, textarea"));
    if (inField && e.key !== "Escape") return;
    if (audio.handleKey(e)) {
        e.preventDefault();
        return;
    }
    if (inField) return;
    // Entrée ou Espace sur un bouton audio : le bouton s'en charge.
    if (target && target.closest(".audio-ctl") && (e.key === "Enter" || e.key === " ")) return;
    if (!$("screen-start-choice").hidden) {
        const n = parseInt(e.key, 10);
        const btns = document.querySelectorAll("#start-options .choice");
        if (n >= 1 && btns[n - 1]) {
            e.preventDefault();
            btns[n - 1].click();
        }
        return;
    }
    if (!$("screen-dialogue").hidden) {
        if (e.key === "Enter" || e.key === " ") {
            if (finishTyping()) {
                e.preventDefault();
                return;
            }
            // Texte affiché en entier et un seul bouton (« Continuer ») : Entrée le valide.
            const only = document.querySelectorAll("#choices .choice");
            if (only.length === 1) {
                e.preventDefault();
                only[0].click();
            }
            return;
        }
        const n = parseInt(e.key, 10);
        if (n >= 1 && n <= 9) {
            const btns = document.querySelectorAll("#choices .choice");
            if (btns[n - 1]) {
                e.preventDefault();
                btns[n - 1].click();
            }
        }
        return;
    }
    if (e.key === "Enter") {
        const visible = ["btn-start", "btn-enter", "btn-next"]
            .map($)
            .find((b) => b && b.offsetParent !== null);
        if (visible) {
            e.preventDefault();
            visible.click();
        }
    }
});

$("dialogue-text").addEventListener("click", finishTyping);

if (audio.supported) $("keyhint-audio").hidden = false;
audio.setContent({
    parts: [
        "Chapitre " + init.chapterId + ".",
        (init.chapterName || "") + ".",
        document.querySelector("#screen-intro .intro-text").textContent,
    ],
});

updateHud();
