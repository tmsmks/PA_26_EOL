// Lecture audio du parcours joueur. Deux moteurs :
// - les voix naturelles du serveur (services/tts_service.py : Piper en local,
//   ou Azure) : chaque écran est lu d'une traite, en un seul extrait MP3 mis en
//   cache ; c'est le moteur par défaut quand le serveur en propose ;
// - les voix de l'appareil (Web Speech API), en repli : si le serveur n'a pas
//   de voix, s'il ne répond pas, ou si le participant les choisit.
//
// main.js décrit chaque écran avec `narrate({ parts, choices })` ; ce module le
// lit si la lecture est activée, et gère les boutons de la barre du haut. Les
// réglages restent dans le navigateur du participant.

import { postJSON } from "../shared/http.js";
import { rankVoices, splitForSpeech, toSpeech } from "./speech_text.js";

const STORE_KEY = "pa.play.audio";
const DEFAULTS = { enabled: false, rate: 1, voice: "", readChoices: false, agreement: "f" };
const RATES = [0.8, 0.9, 1, 1.1, 1.25, 1.5];
const SERVER_MAX = 2800; // caractères par extrait (le serveur en accepte 3000)
const SERVER_FIRST = 160; // premier extrait court : la lecture démarre vite

export function speechSupported() {
    return (
        typeof window !== "undefined" &&
        "speechSynthesis" in window &&
        typeof window.SpeechSynthesisUtterance === "function"
    );
}

function loadSettings() {
    try {
        const raw = window.localStorage.getItem(STORE_KEY);
        const s = { ...DEFAULTS, ...(raw ? JSON.parse(raw) : {}) };
        // Réglage d'avant les voix serveur : un identifiant de voix de l'appareil.
        if (s.voice && !/^(srv|dev):/.test(s.voice)) s.voice = "dev:" + s.voice;
        return s;
    } catch {
        return { ...DEFAULTS };
    }
}

function saveSettings(settings) {
    try {
        window.localStorage.setItem(STORE_KEY, JSON.stringify(settings));
    } catch {
        // navigation privée, stockage bloqué : les réglages valent pour cette page
    }
}

/** 50 ms de silence : sert à « déverrouiller » le lecteur audio sur iOS. */
function silentWav() {
    const rate = 8000;
    const n = 400;
    const buf = new ArrayBuffer(44 + n * 2);
    const v = new DataView(buf);
    const ascii = (offset, s) => [...s].forEach((c, i) => v.setUint8(offset + i, c.charCodeAt(0)));
    ascii(0, "RIFF");
    v.setUint32(4, 36 + n * 2, true);
    ascii(8, "WAVE");
    ascii(12, "fmt ");
    v.setUint32(16, 16, true);
    v.setUint16(20, 1, true);
    v.setUint16(22, 1, true);
    v.setUint32(24, rate, true);
    v.setUint32(28, rate * 2, true);
    v.setUint16(32, 2, true);
    v.setUint16(34, 16, true);
    ascii(36, "data");
    v.setUint32(40, n * 2, true);
    return URL.createObjectURL(new Blob([buf], { type: "audio/wav" }));
}

const $ = (id) => document.getElementById(id);

/** Lecteur muet, quand la page n'a pas les commandes audio. */
const SILENT = {
    narrate() {},
    setContent() {},
    append() {},
    stop() {},
    handleKey() {
        return false;
    },
    supported: false,
};

export function createAudio() {
    const ctl = $("audio-ctl");
    const init = window.PA_PLAY || {};
    const deviceOk = speechSupported();
    const serverPossible = !!(init.ttsVoicesUrl && typeof window.Audio === "function");
    if (!ctl || (!deviceOk && !serverPossible)) return SILENT;
    ctl.hidden = false;

    const synth = deviceOk ? window.speechSynthesis : null;
    const player = serverPossible ? new window.Audio() : null;
    if (player) player.preload = "auto";
    const server = { enabled: false, voices: [], default: null, broken: false };
    const settings = loadSettings();
    const toggleBtn = $("audio-toggle");
    const pauseBtn = $("audio-pause");
    const replayBtn = $("audio-replay");
    const details = $("audio-settings");
    const note = $("audio-engine-note");

    let content = { parts: [], choices: [] }; // écran affiché
    let items = []; // extraits à lire
    let index = 0; // extrait en cours
    let mode = "device"; // "server" | "device" : moteur de la lecture en cours
    let gen = 0; // génération : invalide les rappels d'une lecture annulée
    let state = "idle"; // idle | loading | speaking | paused | blocked
    let watchdog = null;
    let unlocked = false;
    let midClip = false; // pause au milieu d'un extrait du serveur : reprise exacte
    const urls = new Map(); // voix + texte → promesse de l'adresse du MP3

    function setState(next) {
        state = next;
        ctl.dataset.state = settings.enabled ? state : "off";
        toggleBtn.setAttribute("aria-pressed", settings.enabled ? "true" : "false");
        toggleBtn.title = settings.enabled
            ? "Lecture audio activée : cliquer pour l'arrêter (L)"
            : "Écouter les textes à voix haute (L)";
        pauseBtn.hidden = replayBtn.hidden = !settings.enabled;
        const busy = state === "speaking" || state === "loading";
        pauseBtn.setAttribute(
            "aria-label",
            busy ? "Mettre la lecture en pause (P)" : state === "paused" ? "Reprendre la lecture (P)" : "Lire (P)"
        );
        pauseBtn.title = pauseBtn.getAttribute("aria-label");
    }

    /* --- Choix du moteur et de la voix --- */

    function serverVoiceId() {
        if (settings.voice.startsWith("srv:")) {
            const id = settings.voice.slice(4);
            if (server.voices.some((v) => v.id === id)) return id;
        }
        return server.default;
    }

    function useServer() {
        return server.enabled && !server.broken && !settings.voice.startsWith("dev:");
    }

    function deviceVoice() {
        const all = synth ? synth.getVoices() : [];
        const uri = settings.voice.startsWith("dev:") ? settings.voice.slice(4) : "";
        return all.find((v) => v.voiceURI === uri) || rankVoices(all)[0] || null;
    }

    function spoken(texts) {
        return texts
            .filter(Boolean)
            .map((p) => toSpeech(p, { agreement: settings.agreement }))
            .filter(Boolean);
    }

    /**
     * Extraits à lire. Voix du serveur : une première phrase courte (la lecture
     * démarre vite), puis le reste de l'écran d'une traite, puis les réponses
     * proposées. Voix de l'appareil : phrase à phrase.
     */
    function itemsFor(c, forServer) {
        const main = spoken(c.parts || []);
        const choices =
            settings.readChoices && (c.choices || []).length ? spoken(["Réponses proposées.", ...c.choices]) : [];
        if (!forServer) return [...main, ...choices].flatMap((t) => splitForSpeech(t));
        const out = [];
        if (main.length) {
            const [first, ...rest] = splitForSpeech(main.join(" "), SERVER_FIRST);
            out.push(first);
            if (rest.length) out.push(...splitForSpeech(rest.join(" "), SERVER_MAX));
        }
        if (choices.length) out.push(...splitForSpeech(choices.join(" "), SERVER_MAX));
        return out;
    }

    /* --- Voix du serveur --- */

    function serverUrl(voiceId, text) {
        const k = voiceId + "\n" + text;
        if (!urls.has(k)) {
            const p = postJSON(init.ttsSpeakUrl, { voice: voiceId, text }).then((r) => r.url);
            p.catch(() => urls.delete(k));
            urls.set(k, p);
        }
        return urls.get(k);
    }

    function fallBack(g, reason) {
        // Le serveur ne lit plus : les voix de l'appareil prennent le relais.
        server.broken = true;
        if (note) {
            note.textContent = "Voix naturelle indisponible (" + reason + ") : voix de l'appareil utilisée.";
            note.hidden = false;
        }
        if (g !== gen || !synth) {
            if (g === gen) setState("idle");
            return;
        }
        play(content); // l'écran est relu en entier, avec la voix de l'appareil
    }

    async function playServer(g) {
        if (g !== gen) return;
        if (index >= items.length) {
            setState("idle");
            return;
        }
        const voiceId = serverVoiceId();
        // Les extraits suivants se préparent pendant que celui-ci est lu, et le
        // prochain est déjà téléchargé : l'enchaînement se fait sans attente.
        for (let j = index + 1; j < Math.min(items.length, index + 3); j++) {
            const next = serverUrl(voiceId, items[j]);
            if (j === index + 1) next.then((u) => fetch(u)).catch(() => {});
            else next.catch(() => {});
        }
        if (state !== "speaking") setState("loading");
        let url;
        try {
            url = await serverUrl(voiceId, items[index]);
        } catch (err) {
            if (g === gen) fallBack(g, err.message);
            return;
        }
        if (g !== gen) return;
        midClip = false;
        player.src = url;
        player.playbackRate = settings.rate;
        player.preservesPitch = true;
        player.onended = () => {
            if (g !== gen) return;
            index += 1;
            playServer(g);
        };
        player.onerror = () => {
            if (g === gen) fallBack(g, "audio illisible");
        };
        try {
            await player.play();
            if (g === gen) setState("speaking");
        } catch (err) {
            if (g !== gen) return;
            if (err && err.name === "NotAllowedError") setState("blocked");
            else if (!err || err.name !== "AbortError") fallBack(g, "lecture refusée");
        }
    }

    /* --- Voix de l'appareil --- */

    function speakItem(g, retried) {
        if (g !== gen) return;
        if (index >= items.length) {
            setState("idle");
            return;
        }
        const u = new window.SpeechSynthesisUtterance(items[index]);
        const voice = deviceVoice();
        if (voice) u.voice = voice;
        u.lang = voice ? voice.lang : "fr-FR";
        u.rate = settings.rate;
        let started = false;
        u.onstart = () => {
            started = true;
        };
        u.onend = () => {
            if (g !== gen) return;
            index += 1;
            speakItem(g, false);
        };
        u.onerror = (e) => {
            if (g !== gen || e.error === "interrupted" || e.error === "canceled") return;
            if (e.error === "not-allowed") {
                setState("blocked"); // le navigateur attend un clic ou une touche
                return;
            }
            index += 1;
            speakItem(g, false);
        };
        synth.speak(u);
        setState("speaking");
        // Safari et Chrome « perdent » parfois une lecture lancée juste après
        // une annulation (rien ne parle, rien n'attend) : on relance une fois.
        window.clearTimeout(watchdog);
        watchdog = window.setTimeout(() => {
            if (g !== gen || started || state !== "speaking" || synth.speaking || synth.pending) return;
            if (retried) {
                setState("idle");
                return;
            }
            synth.cancel();
            speakItem(g, true);
        }, 900);
    }

    /* --- Commandes --- */

    function cancel() {
        gen += 1;
        midClip = false;
        window.clearTimeout(watchdog);
        if (synth) synth.cancel();
        if (player) {
            player.onended = player.onerror = null;
            player.pause();
        }
    }

    function start() {
        if (mode === "server") playServer(gen);
        else speakItem(gen, false);
    }

    /** Lit un écran, depuis le début. */
    function play(c) {
        cancel();
        mode = useServer() ? "server" : "device";
        if (mode === "device" && !synth) {
            setState("idle");
            return;
        }
        items = itemsFor(c, mode === "server");
        index = 0;
        if (!items.length) {
            setState("idle");
            return;
        }
        start();
    }

    function append(c) {
        const more = itemsFor({ parts: c.parts || [] }, mode === "server");
        if (!more.length) return;
        if (state === "speaking" || state === "paused" || state === "loading") {
            items.push(...more);
            return;
        }
        play({ parts: c.parts || [] });
    }

    function pause() {
        if (state !== "speaking" && state !== "loading") return;
        if (mode === "server" && state === "speaking") {
            player.pause(); // reprend exactement là où elle s'est arrêtée
            midClip = true;
        } else {
            cancel(); // voix de l'appareil, ou extrait pas encore arrivé : on le relancera
        }
        setState("paused");
    }

    function resume() {
        if (state === "paused" || state === "blocked") {
            if (midClip && state === "paused") {
                player.play().then(
                    () => setState("speaking"),
                    () => setState("blocked")
                );
                return;
            }
            cancel();
            start();
        } else if (state === "idle") {
            play(content);
        }
    }

    // iOS n'autorise le son qu'à partir d'un geste : on « déverrouille » la voix
    // et le lecteur au premier clic ou à la première touche.
    let silence = null;
    function unlockNow() {
        if (synth) synth.speak(new window.SpeechSynthesisUtterance(""));
        if (player) {
            silence = silence || silentWav();
            player.src = silence;
            player.play().catch(() => {});
        }
    }
    function unlock() {
        if (unlocked || !settings.enabled) return;
        unlocked = true;
        unlockNow();
    }
    document.addEventListener("pointerdown", unlock, true);
    document.addEventListener("keydown", unlock, true);
    window.addEventListener("pagehide", () => cancel());

    function setEnabled(on) {
        settings.enabled = on;
        saveSettings(settings);
        if (on) {
            if (!unlocked) {
                unlocked = true;
                unlockNow(); // dans le geste qui active la lecture
            }
            play(content);
        } else {
            cancel();
            setState("idle");
        }
        setState(state);
    }

    /* --- Réglages --- */

    const voiceSelect = $("audio-voice");
    const rateSelect = $("audio-rate");
    const choicesBox = $("audio-choices");

    function fillVoices() {
        voiceSelect.innerHTML = "";
        const best = server.enabled
            ? (server.voices.find((v) => v.id === server.default) || {}).label
            : (rankVoices(synth ? synth.getVoices() : [])[0] || {}).name;
        voiceSelect.add(new Option(best ? "Automatique — " + best : "Automatique", ""));
        if (server.enabled) {
            const group = document.createElement("optgroup");
            group.label = "Voix naturelles";
            server.voices.forEach((v) => group.appendChild(new Option(v.label, "srv:" + v.id)));
            voiceSelect.appendChild(group);
        }
        const device = synth ? rankVoices(synth.getVoices()) : [];
        if (device.length) {
            const group = document.createElement("optgroup");
            group.label = "Voix de l'appareil";
            // « Eddy (français (France)) » porte déjà sa langue dans son nom.
            device.forEach((v) =>
                group.appendChild(new Option(v.name.includes("(") ? v.name : v.name + " (" + v.lang + ")", "dev:" + v.voiceURI))
            );
            voiceSelect.appendChild(group);
        }
        const values = Array.from(voiceSelect.options, (o) => o.value);
        voiceSelect.value = values.includes(settings.voice) ? settings.voice : "";
    }
    fillVoices();
    if (synth) {
        if (typeof synth.addEventListener === "function") synth.addEventListener("voiceschanged", fillVoices);
        else synth.onvoiceschanged = fillVoices;
    }

    async function loadServerVoices() {
        if (!serverPossible) return;
        try {
            const res = await fetch(init.ttsVoicesUrl, { headers: { Accept: "application/json" } });
            if (!res.ok) return;
            const data = await res.json();
            if (data.enabled && (data.voices || []).length) {
                Object.assign(server, { enabled: true, voices: data.voices, default: data.default });
                fillVoices();
            }
        } catch {
            // hors ligne : voix de l'appareil
        }
    }
    const ready = loadServerVoices();

    RATES.forEach((r) =>
        rateSelect.add(new Option(String(r).replace(".", ",") + " ×" + (r === 1 ? " (normale)" : ""), String(r)))
    );
    rateSelect.value = String(RATES.includes(settings.rate) ? settings.rate : 1);
    choicesBox.checked = !!settings.readChoices;
    document.querySelectorAll('input[name="audio-agreement"]').forEach((radio) => {
        radio.checked = radio.value === settings.agreement;
        radio.addEventListener("change", () => {
            if (!radio.checked) return;
            settings.agreement = radio.value;
            saveSettings(settings);
        });
    });

    voiceSelect.addEventListener("change", () => {
        settings.voice = voiceSelect.value;
        server.broken = false; // un nouveau choix redonne sa chance au serveur
        if (note) note.hidden = true;
        saveSettings(settings);
    });
    rateSelect.addEventListener("change", () => {
        settings.rate = parseFloat(rateSelect.value) || 1;
        if (player) player.playbackRate = settings.rate;
        saveSettings(settings);
    });
    choicesBox.addEventListener("change", () => {
        settings.readChoices = choicesBox.checked;
        saveSettings(settings);
    });
    $("audio-test").addEventListener("click", () => {
        if (!unlocked) {
            unlocked = true;
            unlockNow();
        }
        play({ parts: ["Bonjour. Voici la voix qui lira le parcours, à cette vitesse."] });
    });

    // Le panneau se ferme en cliquant ailleurs, ou avec Échap.
    document.addEventListener("click", (e) => {
        if (details.open && !details.contains(e.target)) details.open = false;
    });

    toggleBtn.addEventListener("click", () => setEnabled(!settings.enabled));
    pauseBtn.addEventListener("click", () => (state === "speaking" || state === "loading" ? pause() : resume()));
    replayBtn.addEventListener("click", () => play(content));

    setState("idle");

    return {
        supported: true,
        /** Promesse résolue quand les voix du serveur sont connues (tests). */
        ready,
        /** Nouvel écran : le lit si la lecture est activée. */
        narrate(c) {
            content = { parts: c.parts || [], choices: c.choices || [] };
            if (settings.enabled) play(content);
        },
        /** Écran affiché sans le lire (ex. avant le premier geste). */
        setContent(c) {
            content = { parts: c.parts || [], choices: c.choices || [] };
        },
        /** Complète l'écran (ex. la note du chapitre arrive du serveur). */
        append(c) {
            content = { parts: content.parts.concat(c.parts || []), choices: content.choices };
            if (settings.enabled) append(c);
        },
        stop() {
            cancel();
            setState("idle");
        },
        /** Raccourcis : L (lecture), P (pause), R (relire), Échap. Retourne true si traité. */
        handleKey(e) {
            if (e.ctrlKey || e.metaKey || e.altKey) return false;
            const key = e.key.length === 1 ? e.key.toLowerCase() : e.key;
            if (key === "Escape") {
                if (details.open) {
                    details.open = false;
                    details.querySelector("summary").focus();
                    return true;
                }
                if (state === "speaking" || state === "loading") {
                    pause();
                    return true;
                }
                return false;
            }
            if (key === "l") {
                setEnabled(!settings.enabled);
                return true;
            }
            if (!settings.enabled) return false;
            if (key === "p") {
                if (state === "speaking" || state === "loading") pause();
                else resume();
                return true;
            }
            if (key === "r") {
                play(content);
                return true;
            }
            return false;
        },
    };
}
