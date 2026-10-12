// Lecture audio — préparation du texte pour la synthèse vocale du navigateur.
//
// Fonctions pures, sans accès au DOM (testées par tests/js/speech_text.test.mjs).
// Une voix lit mal l'écriture inclusive (« seul·e »), les abréviations (« Dre »),
// les heures (« 22 h 07 »), les cris en capitales et les emojis : on les remet
// en toutes lettres avant de lire. Le texte affiché, lui, ne change pas.

/** Terminaisons féminines qui remplacent la fin du masculin. */
const FEMININE_ENDINGS = [
    ["rice", "eur"], // médiateur·rice → médiatrice
    ["euse", "eur"], // joueur·euse → joueuse
    ["ère", "er"], // fier·ère → fière
    ["ète", "et"], // inquiet·ète → inquiète
    ["ve", "f"], // fictif·ve → fictive
    ["se", "x"], // heureux·se → heureuse
];

export function feminine(base, suffix) {
    for (const [ending, masculine] of FEMININE_ENDINGS) {
        if (suffix === ending && base.endsWith(masculine)) {
            return base.slice(0, -masculine.length) + ending;
        }
    }
    return base + suffix; // seul·e → seule, gentil·le → gentille, franc·he → franche
}

/**
 * Écriture inclusive → une seule forme : « seul·e » se lit « seule » (accords au
 * féminin, `agreement` = "f") ou « seul » (au masculin, "m") ; le pluriel est
 * gardé (« étudiant·e·s » → « étudiantes » ou « étudiants »).
 */
export function resolveInclusive(text, agreement) {
    return text.replace(/(\p{L}+)·(\p{Ll}*)(?:·(\p{Ll}+))?/gu, (match, base, suffix, last) => {
        let ending = suffix;
        let plural = "";
        if (last === "s") plural = "s";
        else if (last) ending = suffix + last;
        if (!last && suffix === "es") {
            ending = "e"; // étudiant·es
            plural = "s";
        }
        if (!last && suffix === "s") return base + "s";
        return (agreement === "m" ? base : feminine(base, ending)) + plural;
    });
}

const TITLES = [
    [/(^|[^\p{L}])Dre(?=\s)/gu, "$1Docteure"],
    [/(^|[^\p{L}])Dr(?=\s)/gu, "$1Docteur"],
    [/(^|[^\p{L}])Pre(?=\s)/gu, "$1Professeure"],
    [/(^|[^\p{L}])Pr(?=\s)/gu, "$1Professeur"],
    [/(^|[^\p{L}])Mme(?=\s)/gu, "$1Madame"],
    [/(^|[^\p{L}])Mlle(?=\s)/gu, "$1Mademoiselle"],
    [/(^|[^\p{L}])M\.(?=\s+\p{Lu})/gu, "$1Monsieur"],
    [/(^|[^\p{L}])Me(?=\s+\p{Lu}\p{Ll})/gu, "$1Maître"],
    [/n°\s*/gu, "numéro "],
    [/(\d)\s*°C/gu, "$1 degrés"],
    [/(\d+)\s*\/\s*100\b/gu, "$1 sur 100"],
    [/±\s*/gu, "plus ou moins "],
];

export function expandAbbreviations(text) {
    return TITLES.reduce((t, [pattern, spoken]) => t.replace(pattern, spoken), text);
}

function hourWords(hours) {
    const n = parseInt(hours, 10);
    if (n === 0) return "minuit";
    if (n === 1) return "une heure";
    return n + " heures";
}

/** « 22 h 07 » → « 22 heures 7 », « 0 h 32 » → « minuit 32 », « 1 h » → « une heure ». */
export function spokenTimes(text) {
    return text
        .replace(/(?<![\d,.])(\d{1,2})\s?h\s?(\d{2})(?!\d)/gu, (m, h, mm) => {
            const minutes = parseInt(mm, 10);
            return hourWords(h) + (minutes ? " " + minutes : "");
        })
        .replace(/(?<![\d,.])(\d{1,2})\s?h(?![\p{L}\d])/gu, (m, h) => hourWords(h));
}

/** Sigles à garder tels quels (la voix les épelle, c'est voulu). */
const ACRONYMS = new Set([
    "UNIL", "UNIGE", "UZH", "CHUV", "HUG", "EMS", "CMS", "IRM", "VIH", "AVC", "BLS",
    "ECG", "OK", "USA", "CFF", "APP", "QCM", "SMS", "ASSC", "IA", "CRP", "RDV", "OFSP",
    "POL", "AMC", "OAP", "ECOS", "SMUR", "ORL", "PDF", "TP",
]);

function letters(token) {
    return token.replace(/[^\p{L}]/gu, "");
}

function isCaps(token) {
    const l = letters(token);
    return l.length > 0 && l === l.toUpperCase() && l !== l.toLowerCase();
}

/**
 * Les passages criés en capitales (« RETIRE ÇA AVANT QUE JE LE SIGNALE »,
 * « PAUSE RÉELLE ») sont mis en minuscules : certaines voix les épellent lettre
 * à lettre. Les sigles isolés (« IRM », « l'EMS ») ne bougent pas.
 */
export function softenCaps(text) {
    const tokens = text.split(/(\s+)/);
    const runs = [];
    let run = [];
    const close = () => {
        if (run.length) runs.push(run);
        run = [];
    };
    tokens.forEach((tok, i) => {
        if (!tok.trim()) return; // espace : ne coupe pas une suite
        if (isCaps(tok)) run.push(i);
        else if (!letters(tok)) return; // ponctuation ou nombre : ne coupe pas non plus
        else close();
    });
    close();
    for (const idxs of runs) {
        const words = idxs.map((i) => letters(tokens[i]));
        const total = words.reduce((n, w) => n + w.length, 0);
        const shout =
            (idxs.length >= 2 && total >= 6 && !words.every((w) => ACRONYMS.has(w))) ||
            (idxs.length === 1 && words[0].length >= 5 && !ACRONYMS.has(words[0]));
        if (shout) idxs.forEach((i) => (tokens[i] = tokens[i].toLowerCase()));
    }
    return tokens.join("");
}

/** Emojis, guillemets et séparateurs que la voix lirait ou buterait dessus. */
export function stripSymbols(text) {
    return text
        .replace(/[\p{Extended_Pictographic}\p{Co}️‍]/gu, "")
        .replace(/[«»“”"]/g, "")
        .replace(/\s*=\s*/g, " égal ")
        .replace(/\s*[·•]\s*/g, ", ")
        .replace(/\s+([,.;:!?…])/g, "$1")
        .replace(/\s{2,}/g, " ")
        .trim();
}

/** Texte affiché → texte à lire. `agreement` : "f" (défaut) ou "m". */
export function toSpeech(text, options) {
    const agreement = (options && options.agreement) || "f";
    let t = String(text || "");
    t = resolveInclusive(t, agreement);
    t = expandAbbreviations(t);
    t = spokenTimes(t);
    t = softenCaps(t);
    t = stripSymbols(t);
    return t;
}

function sentences(text) {
    if (typeof Intl !== "undefined" && Intl.Segmenter) {
        const seg = new Intl.Segmenter("fr", { granularity: "sentence" });
        return Array.from(seg.segment(text), (s) => s.segment.trim()).filter(Boolean);
    }
    return (text.match(/[^.!?…]+(?:[.!?…]+|$)/g) || [text]).map((s) => s.trim()).filter(Boolean);
}

/**
 * Découpe en morceaux de `max` caractères au plus, aux fins de phrase (puis aux
 * virgules) : certains navigateurs coupent une lecture de plus de 15 secondes,
 * et la pause ou la relecture reprennent au début du morceau.
 */
export function splitForSpeech(text, max) {
    const limit = max || 180;
    const out = [];
    let cur = "";
    const push = () => {
        if (cur.trim()) out.push(cur.trim());
        cur = "";
    };
    for (const s of sentences(text)) {
        if (s.length > limit) {
            push();
            for (const piece of s.split(/(?<=[,;:])\s+/)) {
                if (cur && (cur + " " + piece).length > limit) push();
                cur += (cur ? " " : "") + piece;
            }
            continue;
        }
        if (cur && (cur + " " + s).length > limit) push();
        cur += (cur ? " " : "") + s;
    }
    push();
    return out;
}

const NOVELTY_VOICES =
    /\b(Albert|Bad News|Bahh|Bells|Boing|Bubbles|Cellos|Eddy|Flo|Fred|Good News|Grandma|Grandpa|Jester|Junior|Kathy|Organ|Ralph|Reed|Rocko|Sandy|Shelley|Superstar|Trinoids|Whisper|Wobble|Zarvox)\b/i;

/**
 * Voix françaises, la plus naturelle d'abord : français de Suisse, puis de
 * France ; voix « naturelles » ou « premium » avant les voix compactes ; voix
 * fantaisie (Grandma, Zarvox…) en dernier.
 */
export function rankVoices(voices) {
    const french = (voices || []).filter((v) => /^fr([-_]|$)/i.test(v.lang || ""));
    const score = (v) => {
        const lang = String(v.lang || "").toLowerCase().replace("_", "-");
        const name = String(v.name || "");
        let s = { "fr-ch": 30, "fr-fr": 20, "fr-be": 12, "fr-ca": 8 }[lang] || 4;
        if (/natural|neural|premium|enhanced|siri|online/i.test(name)) s += 15;
        if (/google/i.test(name)) s += 6;
        if (NOVELTY_VOICES.test(name)) s -= 25;
        if (v.default) s += 1;
        return s;
    };
    return french
        .map((v) => [score(v), v])
        .sort((a, b) => b[0] - a[0] || String(a[1].name).localeCompare(String(b[1].name), "fr"))
        .map(([, v]) => v);
}
