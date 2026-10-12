// Tests de la préparation du texte pour la lecture audio (static/play/speech_text.js).
// Lancés par tests/test_play_audio.py : node --test tests/js/speech_text.test.mjs
import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

import {
    expandAbbreviations,
    rankVoices,
    resolveInclusive,
    softenCaps,
    splitForSpeech,
    spokenTimes,
    toSpeech,
} from "../../static/play/speech_text.js";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..");

test("écriture inclusive : une seule forme, au féminin ou au masculin", () => {
    const cases = [
        ["seul·e", "seule", "seul"],
        ["étudiant·e·s", "étudiantes", "étudiants"],
        ["heureux·se", "heureuse", "heureux"],
        ["silencieux·se", "silencieuse", "silencieux"],
        ["inquiet·ète", "inquiète", "inquiet"],
        ["fier·ère", "fière", "fier"],
        ["médiateur·rice", "médiatrice", "médiateur"],
        ["gentil·le", "gentille", "gentil"],
        ["franc·he", "franche", "franc"],
        ["L'étudiant·e", "L'étudiante", "L'étudiant"],
        ["un·e ami·e", "une amie", "un ami"],
        ["joueur·euse·s", "joueuses", "joueurs"],
        ["remercié·e·s", "remerciées", "remerciés"],
        ["Épuisé·e", "Épuisée", "Épuisé"],
        ["étudiant·es", "étudiantes", "étudiants"],
    ];
    for (const [text, fem, masc] of cases) {
        assert.equal(resolveInclusive(text, "f"), fem, text);
        assert.equal(resolveInclusive(text, "m"), masc, text);
    }
});

test("titres et abréviations en toutes lettres", () => {
    assert.equal(
        expandAbbreviations("La Dre Golay, le Dr Ibarra, la Pre Vautier, le Pr Lambelet, Mme Rapin et M. Chappuis."),
        "La Docteure Golay, le Docteur Ibarra, la Professeure Vautier, le Professeur Lambelet, Madame Rapin et Monsieur Chappuis."
    );
    assert.equal(expandAbbreviations("Prends le n°14."), "Prends le numéro 14.");
    assert.equal(expandAbbreviations("86/100 (± 10)"), "86 sur 100 (plus ou moins 10)");
    assert.equal(expandAbbreviations("Me Rochat"), "Maître Rochat");
    assert.equal(expandAbbreviations("Me voilà."), "Me voilà.");
});

test("heures lues comme on les dit", () => {
    assert.equal(spokenTimes("Lundi, 22 h 07."), "Lundi, 22 heures 7.");
    assert.equal(spokenTimes("à 0 h 32"), "à minuit 32");
    assert.equal(spokenTimes("1 h 07"), "une heure 7");
    assert.equal(spokenTimes("vers 14 h, puis 9 h 00"), "vers 14 heures, puis 9 heures");
    assert.equal(spokenTimes("dans les 4 h 30"), "dans les 4 heures 30");
    assert.equal(spokenTimes("deux heures"), "deux heures");
});

test("les cris en capitales sont adoucis, pas les sigles", () => {
    assert.equal(
        softenCaps("« T'ES SÉRIEUSE ? RETIRE ÇA AVANT QUE JE LE SIGNALE. »"),
        "« t'es sérieuse ? retire ça avant que je le signale. »"
    );
    assert.equal(softenCaps("« PAUSE RÉELLE. »"), "« pause réelle. »");
    assert.equal(softenCaps("Une IRM à l'EMS d'Orbe, le VIH, le BLS."), "Une IRM à l'EMS d'Orbe, le VIH, le BLS.");
    assert.equal(softenCaps("À 9 h, Alex arrive."), "À 9 h, Alex arrive.");
});

test("texte complet prêt à lire", () => {
    assert.equal(
        toSpeech("« PITTET J. = 2 ! DATE DE NAISSANCE ! »"),
        "pittet j. égal 2! date de naissance!"
    );
    assert.equal(
        toSpeech("Vous êtes venu·e seul·e voir la Dre Golay à 22 h 07 💀", { agreement: "m" }),
        "Vous êtes venu seul voir la Docteure Golay à 22 heures 7"
    );
});

test("découpage en morceaux courts, sans rien perdre", () => {
    const long =
        "Hier soir, vous avez ouvert l'enveloppe beige. Une feuille de cahier, l'écriture penchée de " +
        "Jeannine, datée de septembre, avec des ajouts à l'encre bleue. « Petit, ou petite — je n'ai " +
        "jamais su, avec vous, et ça m'est égal. Si vous lisez ceci, c'est que je suis partie, et que " +
        "mon corps est chez vous, à la fac, dans une salle que vous ne verrez pas, parce que c'est la " +
        "règle, que c'est bien, et que je l'ai voulu ainsi depuis longtemps, bien avant de vous connaître. »";
    const chunks = splitForSpeech(long, 180);
    assert.ok(chunks.length >= 3, chunks.length);
    for (const c of chunks) assert.ok(c.length <= 180, c);
    const words = (s) => s.split(/\s+/).filter(Boolean);
    assert.deepEqual(words(chunks.join(" ")), words(long));
});

test("voix : français de Suisse et voix naturelles d'abord, voix fantaisie en dernier", () => {
    const voices = [
        { name: "Samantha", lang: "en-US" },
        { name: "Grandma (Français (France))", lang: "fr-FR" },
        { name: "Thomas", lang: "fr-FR" },
        { name: "Microsoft Denise Online (Natural) - French (France)", lang: "fr-FR" },
        { name: "Amélie", lang: "fr-CA" },
        { name: "Voix suisse", lang: "fr-CH" },
    ];
    const names = rankVoices(voices).map((v) => v.name);
    assert.deepEqual(names, [
        "Microsoft Denise Online (Natural) - French (France)",
        "Voix suisse",
        "Thomas",
        "Amélie",
        "Grandma (Français (France))",
    ]);
});

test("tous les textes des livres se lisent sans symbole ni abréviation", () => {
    const dir = join(ROOT, "data", "chapters");
    const strings = [];
    const walk = (node, key) => {
        if (typeof node === "string") {
            if (!["Name", "ImageName", "AgentFacialExpression"].includes(key)) strings.push(node);
        } else if (Array.isArray(node)) node.forEach((n) => walk(n, key));
        else if (node && typeof node === "object") for (const [k, v] of Object.entries(node)) walk(v, k);
    };
    for (const file of readdirSync(dir).filter((f) => f.endsWith(".json"))) {
        walk(JSON.parse(readFileSync(join(dir, file), "utf-8")));
    }
    assert.ok(strings.length > 1000, strings.length);
    for (const agreement of ["f", "m"]) {
        for (const s of strings) {
            const spoken = toSpeech(s, { agreement });
            assert.ok(!spoken.includes("·"), spoken);
            assert.ok(!/(^|[^\p{L}])(Dre|Dr|Pre|Pr|Mme|Mlle)\s/u.test(spoken), spoken);
            assert.ok(!/\d\s?h(?![\p{L}\d])/u.test(spoken), spoken);
            assert.ok(!/\p{Extended_Pictographic}/u.test(spoken), spoken);
        }
    }
});
