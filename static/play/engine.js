// Moteur du parcours joueur — état et règles, sans aucun accès au DOM.
// Consomme le payload produit par services/graph_service.build_all_scenes.
//
// États narratifs : une réponse peut poser/effacer des états (set_flags,
// clear_flags) ; une scène peut être conditionnelle (condition) et avoir
// plusieurs points d'entrée (entry_points). Les états posés par un chapitre
// sont effacés quand on le rejoue ; « Refaire ce scénario » restaure ceux qui
// existaient à l'entrée de la scène.

import { SCORE_SKILLS, emptyScores } from "../shared/skills.js";

export { SCORE_SKILLS };

function addScores(target, source) {
    for (const sk of SCORE_SKILLS) {
        target[sk] = (target[sk] || 0) + (parseInt(source[sk], 10) || 0);
    }
    return target;
}

/** Une condition vide est toujours vraie. */
export function evalCondition(cond, flags) {
    if (!cond) return true;
    const all = cond.all || [];
    const any = cond.any || [];
    const none = cond.none || [];
    if (!all.every((f) => flags.has(f))) return false;
    if (any.length && !any.some((f) => flags.has(f))) return false;
    if (none.some((f) => flags.has(f))) return false;
    return true;
}

function slotOf(s) {
    return s.slot || "#" + s.scene_id;
}

export function createGame(scenes, options) {
    const opts = options || {};
    const owned = new Set(opts.ownedFlags || []);
    const list = scenes || [];
    return {
        scenes: list,
        /** Emplacements déjà commencés dans ce chapitre. */
        playedSlots: new Set(),
        sceneIdx: 0,
        current: null,
        visited: [],
        owned: owned,
        flags: new Set((opts.flags || []).filter((f) => !owned.has(f))),
        /** Scène en cours, pour l'enregistrement : entrée et indices des réponses. */
        entryId: "",
        choices: [],
        /** Temps de réponse de chaque choix (ms), envoyés avec la scène. */
        times: [],
        /** Réponses critiques choisies dans la scène en cours. */
        sceneCritical: 0,
        snapshots: {},
        sceneScores: emptyScores(),
        chapterScores: emptyScores(),
        /** Meilleur total atteignable sur la scène, pour calibrer les barres. */
        sceneBest: 0,
    };
}

export function scene(game) {
    return game.scenes[game.sceneIdx] || null;
}

/**
 * Emplacements comptés dans la progression, dans l'ordre du chapitre : ceux
 * déjà joués, celui en cours, et les suivants qui ont une scène jouable avec
 * les états actuels. Une histoire annexe pas (encore) débloquée n'est pas
 * comptée ; les alternatives d'un même emplacement comptent une fois.
 */
function countedSlots(game) {
    const cur = scene(game);
    const curSlot = cur ? slotOf(cur) : null;
    const out = [];
    game.scenes.forEach((s, i) => {
        const slot = slotOf(s);
        if (out.includes(slot)) return;
        if (game.playedSlots.has(slot) || slot === curSlot) {
            out.push(slot);
        } else if (i > game.sceneIdx && evalCondition(s.condition, game.flags)) {
            out.push(slot);
        }
    });
    return out;
}

/** Nombre de scènes jouées dans le chapitre (les alternatives comptent une fois). */
export function sceneCount(game) {
    return countedSlots(game).length;
}

/** Rang (1-based) de la scène courante dans le chapitre. */
export function sceneNumber(game) {
    const s = scene(game);
    const slots = countedSlots(game);
    if (!s) return slots.length;
    return slots.indexOf(slotOf(s)) + 1;
}

export function flagList(game) {
    return Array.from(game.flags).sort();
}

/** Remplace les états (ceux posés par ce chapitre repartent de zéro). */
export function setFlags(game, flags) {
    game.flags = new Set((flags || []).filter((f) => !game.owned.has(f)));
}

export function applyFlags(game, flags) {
    for (const f of flags || []) game.flags.add(f);
}

/** L'écran de choix de départ s'affiche si aucun état attendu n'est connu. */
export function needsStartChoice(game, startChoice) {
    if (!startChoice || !(startChoice.options || []).length) return false;
    return !(startChoice.unless_any || []).some((f) => game.flags.has(f));
}

function isPlayable(game, idx) {
    const s = game.scenes[idx];
    return !!s && evalCondition(s.condition, game.flags);
}

function nextPlayable(game, from) {
    for (let i = from; i < game.scenes.length; i++) {
        if (isPlayable(game, i)) return i;
    }
    return -1;
}

/** Positionne le jeu sur la première scène jouable. Retourne false si aucune. */
export function enterChapter(game) {
    const idx = nextPlayable(game, 0);
    game.playedSlots = new Set();
    game.sceneIdx = idx === -1 ? game.scenes.length : idx;
    return idx !== -1;
}

/** Point d'entrée de la scène courante selon les états : {id, intro}. */
export function resolveEntry(game) {
    const s = scene(game);
    if (!s) return { id: "", intro: "" };
    for (const ep of s.entry_points || []) {
        if (evalCondition(ep.condition, game.flags)) {
            return { id: ep.interaction_id, intro: ep.intro || s.scene_intro || "" };
        }
    }
    const fallback = s.parcours && s.parcours.length ? s.parcours[0].node_id.split("_I").pop() : "";
    return { id: s.default_entry || fallback, intro: s.scene_intro || "" };
}

/** Démarre (ou redémarre) la scène courante. */
export function startScene(game) {
    const s = scene(game);
    const key = String(game.sceneIdx);
    if (key in game.snapshots) game.flags = new Set(game.snapshots[key]);
    else game.snapshots[key] = Array.from(game.flags);
    if (s) game.playedSlots.add(slotOf(s));

    game.sceneScores = emptyScores();
    game.visited = [];
    game.choices = [];
    game.times = [];
    game.sceneCritical = 0;
    const entry = resolveEntry(game);
    game.current = s && s.id_to_parcours ? s.id_to_parcours[entry.id] || null : null;
    if (!game.current && s && s.parcours && s.parcours.length) game.current = s.parcours[0];
    game.entryId = game.current ? game.current.node_id.split("_I").pop() : "";
    game.sceneBest = s && game.current ? bestPath(s, entry.id) : 0;
    return game.current;
}

/** Applique un choix et avance. Retourne la nouvelle interaction, ou null.
 * `ms` : temps de réponse depuis l'affichage des réponses (repère les passages trop rapides). */
export function choose(game, response, ms) {
    const s = scene(game);
    addScores(game.sceneScores, response);
    addScores(game.chapterScores, response);
    for (const f of response.clear_flags || []) game.flags.delete(f);
    for (const f of response.set_flags || []) game.flags.add(f);
    if (game.current) game.visited.push(game.current.node_id);
    game.choices.push(response.idx);
    game.times.push(Number.isFinite(ms) ? Math.round(ms) : null);
    if (response.critical) game.sceneCritical += 1;

    const nextId = String(response.next_id || "-1");
    game.current =
        s && s.id_to_parcours && nextId !== "-1" && nextId !== ""
            ? s.id_to_parcours[nextId] || null
            : null;
    return game.current;
}

export function isSceneOver(game) {
    return !game.current || !(game.current.responses || []).length;
}

export function hasNextScene(game) {
    return nextPlayable(game, game.sceneIdx + 1) !== -1;
}

export function goToNextScene(game) {
    const idx = nextPlayable(game, game.sceneIdx + 1);
    if (idx === -1) return false;
    game.sceneIdx = idx;
    return true;
}

/**
 * Meilleur total atteignable depuis le point d'entrée : chemin de somme
 * maximale dans le graphe de la scène (les retours en arrière sont coupés).
 */
function bestPath(s, startId) {
    const memo = new Map();
    const onStack = new Set();
    function best(id) {
        if (memo.has(id)) return memo.get(id);
        const entry = s.id_to_parcours[id];
        if (!entry || onStack.has(id)) return 0;
        onStack.add(id);
        let top = null;
        for (const r of entry.responses || []) {
            const nid = String(r.next_id || "-1");
            const v = totalOf(r) + (nid !== "-1" && nid !== "" ? best(nid) : 0);
            if (top === null || v > top) top = v;
        }
        onStack.delete(id);
        memo.set(id, top || 0);
        return top || 0;
    }
    return Math.max(1, best(String(startId)));
}

export function totalOf(scores) {
    let sum = 0;
    for (const sk of SCORE_SKILLS) sum += parseInt(scores[sk], 10) || 0;
    return sum;
}

/** Bilan narratif propre à une issue (ex. décès du patient), s'il y en a un. */
function outcomeDebrief(game) {
    const s = scene(game);
    for (const d of (s && s.debriefs) || []) {
        if (evalCondition(d.condition, game.flags)) return d;
    }
    return null;
}

/** Appréciation qualitative d'un parcours de scène. */
export function appraise(scores, best, game) {
    const total = totalOf(scores);
    const ratio = best > 0 ? total / best : 0;
    const weak = SCORE_SKILLS.filter((sk) => (scores[sk] || 0) < 0);

    const outcome = game ? outcomeDebrief(game) : null;
    // Une réponse critique ne se compense pas : le bilan le dit d'abord.
    if (game && game.sceneCritical > 0) {
        return {
            tone: "hard",
            lead:
                (game.sceneCritical > 1 ? "Des réponses critiques" : "Une réponse critique") +
                " dans ce scénario : elle met en danger la personne ou enfreint une règle " +
                "essentielle, et de bonnes réponses ailleurs ne la compensent pas. " +
                "Voyez ci-dessous ce qui était attendu." +
                (outcome ? " " + outcome.lead : ""),
            weak,
        };
    }
    if (outcome) {
        return { tone: outcome.tone || "hard", lead: outcome.lead, weak };
    }
    if (total <= 0) {
        return {
            tone: "hard",
            lead:
                "Ce parcours a coûté plus qu'il n'a apporté. Reprenez la scène : " +
                "les réponses qui semblent les plus rassurantes ne sont pas " +
                "toujours celles qui respectent le plus la personne en face.",
            weak,
        };
    }
    if (ratio < 0.45) {
        return {
            tone: "mixed",
            lead:
                "Vous avez tenu la situation, mais plusieurs choix ont fermé la " +
                "conversation au lieu de l'ouvrir.",
            weak,
        };
    }
    if (ratio < 0.75) {
        return {
            tone: "good",
            lead:
                "Bon parcours dans l'ensemble. Quelques réponses restent " +
                "perfectibles sur les dimensions en retrait ci-dessous.",
            weak,
        };
    }
    return {
        tone: "great",
        lead:
            "Parcours très solide : vous avez informé sans brusquer et accueilli " +
            "l'émotion sans la fuir.",
        weak,
    };
}
