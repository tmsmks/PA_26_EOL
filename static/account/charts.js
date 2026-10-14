// Graphiques des pages de suivi — HTML/SVG natifs, sans dépendance.
//
// - skillRose : profil des 7 compétences en diagramme en rose, avec repère de comparaison ;
// - heatmap   : chapitres × compétences (rampe séquentielle bleue) ;
// - trendLine : note globale par session.
// Chaque graphique a une infobulle (survol + focus clavier) et les valeurs
// restent lisibles sans elle (étiquettes directes ou tableau).

const SVG = "http://www.w3.org/2000/svg";

// Rampe séquentielle sur le bleu commun (OKLCH 262°), du plus proche de la
// surface claire au plus foncé.
const RAMP = [
    "#ebf2fe", "#d0dcf3", "#b5c7e7", "#9ab2db", "#809ccf", "#6787c3",
    "#4e72b6", "#365daa", "#1d489c", "#073389", "#001e74",
];
const RAMP_LIGHT_TEXT_FROM = 6; // à partir de cet indice, texte blanc

export function esc(s) {
    if (s === null || s === undefined) return "";
    return String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}

export function fmt(v, digits) {
    if (v === null || v === undefined) return "—";
    return Number(v).toLocaleString("fr-CH", {
        minimumFractionDigits: digits || 0,
        maximumFractionDigits: digits || 0,
    });
}

export function signed(v) {
    if (v === null || v === undefined) return "";
    const r = Math.round(v);
    return (r > 0 ? "+" : r < 0 ? "−" : "±") + Math.abs(r);
}

/* --- Infobulle partagée --- */

let tipEl = null;

function tip() {
    if (!tipEl) {
        tipEl = document.createElement("div");
        tipEl.className = "chart-tip";
        tipEl.setAttribute("role", "tooltip");
        tipEl.hidden = true;
        document.body.appendChild(tipEl);
    }
    return tipEl;
}

function showTip(html, x, y) {
    const el = tip();
    el.innerHTML = html;
    el.hidden = false;
    const w = el.offsetWidth;
    const h = el.offsetHeight;
    const left = Math.min(window.innerWidth - w - 8, Math.max(8, x + 14));
    const top = y - h - 12 < 8 ? y + 16 : y - h - 12;
    el.style.left = left + "px";
    el.style.top = top + "px";
}

function hideTip() {
    if (tipEl) tipEl.hidden = true;
}

/** Infobulle au survol et au focus clavier d'un élément. */
function bindTip(el, html) {
    el.addEventListener("mousemove", (e) => showTip(html, e.clientX, e.clientY));
    el.addEventListener("mouseleave", hideTip);
    el.addEventListener("focus", () => {
        const r = el.getBoundingClientRect();
        showTip(html, r.left + r.width / 2, r.top);
    });
    el.addEventListener("blur", hideTip);
}

/* --- Profil de compétences (diagramme en rose) --- */

// Une couleur par compétence, dans l'ordre du profil (1 à 7) : `fill` pour le
// secteur, `ink` (plus foncée) pour le pourcentage et le trait de rappel, lisible
// sur fond clair — le jaune, en particulier, ne l'est pas tel quel.
const ROSE = {
    RespectAndDignity: { fill: "#ef2b2d", ink: "#c8161c", lines: ["Respect", "et dignité"] },
    Empathy: { fill: "#f8891f", ink: "#c2610a", lines: ["Empathie"] },
    Compassion: { fill: "#fbd122", ink: "#8f6d00", lines: ["Compassion"] },
    EmotionalRegulation: { fill: "#17a548", ink: "#0f7d35", lines: ["Régulation", "émotionnelle"] },
    CommunicationClarity: { fill: "#0b6cf4", ink: "#0a57c4", lines: ["Clarté de", "communication"] },
    ProfessionalBoundaries: { fill: "#55269a", ink: "#4a1f88", lines: ["Frontières", "professionnelles"] },
    InterprofessionalCollaboration: { fill: "#a828e4", ink: "#8618bd", lines: ["Collaboration", "interprofessionnelle"] },
};
const ROSE_FALLBACK = { fill: "#6787c3", ink: "#365daa" };
const ROSE_NARROW = 560; // en dessous (px), étiquettes dans une liste sous le graphique

function svgNode(tag, attrs, parent) {
    const n = document.createElementNS(SVG, tag);
    Object.entries(attrs || {}).forEach(([k, v]) => n.setAttribute(k, v));
    if (parent) parent.appendChild(n);
    return n;
}

/** Point à la distance `r` du centre, angle en degrés compté depuis midi, sens horaire. */
function polar(cx, cy, r, deg) {
    const a = (deg * Math.PI) / 180;
    return [cx + r * Math.sin(a), cy - r * Math.cos(a)];
}

function sectorPath(cx, cy, r, a0, a1) {
    const [x0, y0] = polar(cx, cy, r, a0);
    const [x1, y1] = polar(cx, cy, r, a1);
    return "M" + cx + " " + cy + " L" + x0 + " " + y0 + " A" + r + " " + r + " 0 0 1 " + x1 + " " + y1 + " Z";
}

function arcPath(cx, cy, r, a0, a1) {
    const [x0, y0] = polar(cx, cy, r, a0);
    const [x1, y1] = polar(cx, cy, r, a1);
    return "M" + x0 + " " + y0 + " A" + r + " " + r + " 0 0 1 " + x1 + " " + y1;
}

/**
 * Profil des 7 compétences en diagramme en rose (secteurs égaux, rayon = score
 * sur 100), chaque compétence avec sa couleur, son numéro et son pourcentage.
 * Option `compare` : arc pointillé au niveau de la session de comparaison.
 *
 * @param {HTMLElement} el
 * @param {{skills: string[], labels: object, current: object, compare?: object,
 *          compareLabel?: string, currentLabel?: string,
 *          strengths?: string[], weaknesses?: string[]}} opts
 */
export function skillRose(el, opts) {
    const draw = () => renderRose(el, opts, el.clientWidth > 0 && el.clientWidth < ROSE_NARROW);
    draw();
    if (typeof ResizeObserver === "function" && !el._roseObserver) {
        let narrow = el.clientWidth < ROSE_NARROW;
        el._roseObserver = new ResizeObserver(() => {
            const now = el.clientWidth < ROSE_NARROW;
            if (now !== narrow) {
                narrow = now;
                draw();
            }
        });
        el._roseObserver.observe(el);
    }
}

function renderRose(el, opts, narrow) {
    const current = opts.current || {};
    const compare = opts.compare || null;
    const strengths = opts.strengths || [];
    const weaknesses = opts.weaknesses || [];
    const skills = opts.skills;
    const has = (o, k) => o && o[k] !== null && o[k] !== undefined;
    const step = 360 / skills.length;
    const R = 215; // rayon du 100 %

    // Grand format : étiquettes autour du cercle. Petit format : numéros autour,
    // étiquettes dans une liste sous le graphique (le texte du SVG serait illisible).
    // Le cadre est resserré sur le dessin une fois celui-ci en place (getBBox).
    const W = narrow ? 2 * (R + 34) : 1000;
    const H = narrow ? 2 * (R + 34) : 760;
    const cx = W / 2;
    const cy = H / 2;

    el.innerHTML = "";
    const wrap = document.createElement("div");
    wrap.className = "skill-rose" + (narrow ? " is-narrow" : "");
    const svg = svgNode("svg", {
        viewBox: "0 0 " + W + " " + H,
        role: "group",
        "aria-label": "Profil de compétences : diagramme en rose, une part par compétence, le rayon donne le score sur 100",
    }, wrap);

    // Grille : cercles à 25, 50, 75 et 100 %, rayons entre les parts.
    const grid = svgNode("g", { class: "rose-grid", "aria-hidden": "true" }, svg);
    [25, 50, 75, 100].forEach((p) => svgNode("circle", { cx, cy, r: (R * p) / 100 }, grid));
    skills.forEach((_, i) => {
        const [x, y] = polar(cx, cy, R + 12, i * step);
        svgNode("line", { x1: cx, y1: cy, x2: x, y2: y }, grid);
    });

    // Parts.
    const sectors = svgNode("g", { class: "rose-sectors", style: "transform-origin:" + cx + "px " + cy + "px" }, svg);
    skills.forEach((k, i) => {
        const c = ROSE[k] || ROSE_FALLBACK;
        const a0 = i * step;
        const a1 = (i + 1) * step;
        const label = opts.labels[k] || k;
        const v = has(current, k) ? current[k] : null;
        const p = has(compare, k) ? compare[k] : null;
        const g = svgNode("g", { class: "rose-part", tabindex: "0" }, sectors);
        if (v === null) {
            svgNode("path", { d: sectorPath(cx, cy, R, a0, a1), class: "rose-empty" }, g);
        } else {
            svgNode("path", {
                d: sectorPath(cx, cy, Math.max(2, (R * v) / 100), a0, a1),
                fill: c.fill,
                class: "rose-fill",
            }, g);
        }
        if (p !== null) {
            svgNode("path", { d: arcPath(cx, cy, Math.max(2, (R * p) / 100), a0, a1), class: "rose-prev" }, g);
        }
        g.setAttribute(
            "aria-label",
            (i + 1) + ". " + label + " : " + (v === null ? "non évalué" : fmt(v) + " %") +
                (p !== null ? ", " + (opts.compareLabel || "comparaison") + " " + fmt(p) + " %" : "")
        );
        bindTip(
            g,
            "<b>" + (i + 1) + ". " + esc(label) + "</b><br>" +
                (v === null
                    ? "Non évalué : pas assez de choix la mettent en jeu"
                    : esc(opts.currentLabel || "Cette session") + " : <b>" + fmt(v) + " %</b>") +
                (p !== null
                    ? "<br>" + esc(opts.compareLabel || "Comparaison") + " : " + fmt(p) + " %" +
                      (v !== null ? " (" + signed(v - p) + ")" : "")
                    : "")
        );
    });

    // Axe gradué, au-dessus des parts.
    const axis = svgNode("g", { class: "rose-axis", "aria-hidden": "true" }, svg);
    svgNode("line", { x1: cx, y1: cy, x2: cx, y2: cy - R - 14 }, axis);
    [25, 50, 75, 100].forEach((p) => {
        const t = svgNode("text", { x: cx + 6, y: cy - (R * p) / 100 - 5, "text-anchor": "start" }, axis);
        t.textContent = p + " %";
    });

    // Étiquettes : point sur le bord de la part, trait de rappel, nom et pourcentage.
    const labels = svgNode("g", { class: "rose-labels" }, svg);
    skills.forEach((k, i) => {
        const c = ROSE[k] || ROSE_FALLBACK;
        const mid = (i + 0.5) * step;
        const v = has(current, k) ? current[k] : null;
        const rv = v === null ? R : Math.max(10, (R * v) / 100 - 8);
        const [dx, dy] = polar(cx, cy, rv, mid);

        if (narrow) {
            const [bx, by] = polar(cx, cy, R + 20, mid);
            svgNode("line", { x1: dx, y1: dy, x2: bx, y2: by, stroke: c.ink, class: "rose-leader" }, labels);
            svgNode("circle", { cx: bx, cy: by, r: 13, fill: c.ink, class: "rose-badge" }, labels);
            const t = svgNode("text", { x: bx, y: by + 5, "text-anchor": "middle", class: "rose-badge-num" }, labels);
            t.textContent = String(i + 1);
            svgNode("circle", { cx: dx, cy: dy, r: 6, fill: c.ink, class: "rose-dot" }, labels);
            return;
        }

        const s = Math.sin((mid * Math.PI) / 180);
        const side = s > 0.2 ? 1 : s < -0.2 ? -1 : 0;
        const [ex, ey] = polar(cx, cy, R + 30, mid);
        const tx = side === 0 ? ex : ex + side * 26;
        const lines = ((ROSE[k] && ROSE[k].lines) || [opts.labels[k] || k]).slice();
        lines[0] = i + 1 + ". " + lines[0];
        let tag = "";
        if (strengths.includes(k)) tag = "▲ Point fort";
        else if (weaknesses.includes(k)) tag = "▼ À travailler";
        const rows = lines.length + 1 + (tag ? 1 : 0);
        const lh = 21;
        // Bloc centré sur le coude ; sous le coude pour la part du bas.
        const top = side === 0 ? ey + 22 : ey - ((rows - 1) * lh) / 2 + 6;

        svgNode("polyline", {
            points: dx + "," + dy + " " + ex + "," + ey + " " + (side === 0 ? ex + "," + (ey + 4) : tx - side * 6 + "," + ey),
            stroke: c.ink,
            class: "rose-leader",
        }, labels);
        svgNode("circle", { cx: dx, cy: dy, r: 7, fill: c.ink, class: "rose-dot" }, labels);

        const anchor = side === 1 ? "start" : side === -1 ? "end" : "middle";
        const text = svgNode("text", { x: tx, y: top, "text-anchor": anchor, class: "rose-label" }, labels);
        lines.forEach((line, j) => {
            const span = svgNode("tspan", { x: tx, dy: j === 0 ? 0 : lh }, text);
            span.textContent = line;
        });
        const pct = svgNode("tspan", { x: tx, dy: lh + 2, class: "rose-pct", fill: c.ink }, text);
        pct.textContent = v === null ? "non évalué" : fmt(v) + " %";
        if (v === null) pct.setAttribute("class", "rose-pct is-empty");
        if (tag) {
            const tg = svgNode("tspan", {
                x: tx,
                dy: lh - 2,
                class: "rose-tag " + (strengths.includes(k) ? "is-up" : "is-down"),
            }, text);
            tg.textContent = tag;
        }
    });

    el.appendChild(wrap);
    try {
        const bb = svg.getBBox();
        const pad = 6;
        if (bb.width > 0) {
            svg.setAttribute("viewBox", [bb.x - pad, bb.y - pad, bb.width + 2 * pad, bb.height + 2 * pad].join(" "));
        }
    } catch (e) {
        /* getBBox indisponible (élément masqué) : on garde le cadre par défaut. */
    }

    if (narrow) {
        const list = document.createElement("ol");
        list.className = "rose-list";
        skills.forEach((k) => {
            const c = ROSE[k] || ROSE_FALLBACK;
            const v = has(current, k) ? current[k] : null;
            let tag = "";
            if (strengths.includes(k)) tag = '<span class="rose-tag-html is-up">▲ Point fort</span>';
            else if (weaknesses.includes(k)) tag = '<span class="rose-tag-html is-down">▼ À travailler</span>';
            const li = document.createElement("li");
            li.innerHTML =
                '<i class="rose-swatch" style="background:' + c.fill + '" aria-hidden="true"></i>' +
                '<span class="rose-name">' + esc(opts.labels[k] || k) + "</span>" +
                '<span class="rose-val" style="color:' + c.ink + '">' + (v === null ? "—" : fmt(v) + " %") + "</span>" +
                tag;
            list.appendChild(li);
        });
        el.appendChild(list);
    }

    const missing = skills.filter((k) => !has(current, k));
    if (missing.length) {
        const note = document.createElement("p");
        note.className = "acc-hint";
        note.textContent =
            "Non évalué (pas assez de choix mettent cette compétence en jeu) : " +
            missing.map((k) => opts.labels[k] || k).join(", ") + ".";
        el.appendChild(note);
    }
}

/* --- Carte des chapitres --- */

const ABBR = {
    RespectAndDignity: "RD",
    Empathy: "EM",
    Compassion: "CO",
    EmotionalRegulation: "ER",
    CommunicationClarity: "CC",
    ProfessionalBoundaries: "PB",
    InterprofessionalCollaboration: "IC",
};

function rampIndex(v) {
    return Math.max(0, Math.min(RAMP.length - 1, Math.round(v / 10)));
}

function heatCell(v, tipHtml, extraClass) {
    const td = document.createElement("td");
    if (v === null || v === undefined) {
        td.className = "is-empty" + (extraClass ? " " + extraClass : "");
        td.textContent = "—";
        return td;
    }
    const i = rampIndex(v);
    td.className = extraClass || "";
    td.style.background = RAMP[i];
    td.style.color = i >= RAMP_LIGHT_TEXT_FROM ? "#ffffff" : "#192230";
    td.textContent = fmt(v);
    td.tabIndex = 0;
    bindTip(td, tipHtml);
    return td;
}

/**
 * @param {HTMLElement} el
 * @param {{chapters: object[], skills: string[], labels: object, rework?: number[]}} opts
 */
export function heatmap(el, opts) {
    const rework = opts.rework || [];
    el.innerHTML = "";
    const scroll = document.createElement("div");
    scroll.className = "heat-scroll";
    const table = document.createElement("table");
    table.className = "heat";

    const head = document.createElement("thead");
    let hr = "<tr><th scope=\"col\">Chapitre</th>";
    opts.skills.forEach((k) => {
        hr += '<th scope="col"><abbr title="' + esc(opts.labels[k] || k) + '">' + esc(ABBR[k] || k) + "</abbr></th>";
    });
    hr += '<th scope="col">Global</th></tr>';
    head.innerHTML = hr;
    table.appendChild(head);

    const body = document.createElement("tbody");
    opts.chapters.forEach((ch) => {
        const tr = document.createElement("tr");
        const th = document.createElement("th");
        th.scope = "row";
        th.innerHTML =
            esc(ch.id + ". " + ch.name) +
            (rework.includes(ch.id) ? '<span class="heat-rework">↻ À retravailler</span>' : "");
        tr.appendChild(th);
        opts.skills.forEach((k) => {
            const v = ch.scores ? ch.scores[k] : null;
            tr.appendChild(
                heatCell(
                    v,
                    "<b>Chapitre " + esc(ch.id) + "</b> · " + esc(opts.labels[k] || k) + "<br>" + fmt(v) + "/100"
                )
            );
        });
        tr.appendChild(
            heatCell(ch.global, "<b>Chapitre " + esc(ch.id) + "</b> · note du chapitre<br>" + fmt(ch.global) + "/100", "heat-global")
        );
        body.appendChild(tr);
    });
    table.appendChild(body);
    scroll.appendChild(table);
    el.appendChild(scroll);

    const scale = document.createElement("div");
    scale.className = "heat-scale";
    scale.innerHTML =
        "<span>0</span>" +
        '<span class="heat-scale-bar" style="background:linear-gradient(90deg,' + RAMP.join(",") + ')"></span>' +
        "<span>100</span><span>· — = pas assez de choix dans ce chapitre pour noter cette compétence</span>";
    el.appendChild(scale);
}

/* --- Courbe d'évolution --- */

function node(tag, attrs, parent) {
    const n = document.createElementNS(SVG, tag);
    for (const k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
}

/**
 * @param {HTMLElement} el
 * @param {{number: number, global: number}[]} points  — dans l'ordre des sessions
 * @param {{highlight?: number, prefix?: string, unit?: string, label?: string}} opts —
 *        numéro à marquer ; préfixe des abscisses (« S ») ; nom d'un point
 *        (« Session ») ; nom de la valeur (« Note globale »)
 */
export function trendLine(el, points, opts) {
    const options = opts || {};
    const prefix = options.prefix || "S";
    const unit = options.unit || "Session";
    const valueLabel = options.label || "Note globale";
    const pts = points.filter((p) => p.global !== null && p.global !== undefined);
    el.innerHTML = "";
    el.classList.add("trend");
    if (pts.length < 2) return;

    const draw = () => {
        el.innerHTML = "";
        const W = Math.max(280, el.clientWidth);
        const H = 220;
        const m = { top: 16, right: 46, bottom: 30, left: 34 };
        const pw = W - m.left - m.right;
        const ph = H - m.top - m.bottom;
        const x = (i) => m.left + (pts.length === 1 ? pw / 2 : (i / (pts.length - 1)) * pw);
        const y = (v) => m.top + ph - (v / 100) * ph;

        const svg = node("svg", { viewBox: "0 0 " + W + " " + H, height: H, role: "img" });
        svg.setAttribute(
            "aria-label",
            valueLabel + " par " + unit.toLowerCase() + " : " +
                pts.map((p) => unit.toLowerCase() + " " + p.number + " " + fmt(p.global)).join(", ")
        );
        [0, 25, 50, 75, 100].forEach((t) => {
            node("line", { x1: m.left, x2: W - m.right, y1: y(t), y2: y(t), stroke: t === 0 ? "var(--axis)" : "var(--grid)", "stroke-width": 1 }, svg);
            const lbl = node("text", { x: m.left - 8, y: y(t) + 4, "text-anchor": "end" }, svg);
            lbl.textContent = t;
        });
        pts.forEach((p, i) => {
            const lbl = node("text", { x: x(i), y: H - 8, "text-anchor": "middle" }, svg);
            lbl.textContent = prefix + p.number;
        });

        const d = pts.map((p, i) => (i ? "L" : "M") + x(i).toFixed(1) + " " + y(p.global).toFixed(1)).join(" ");
        node("path", { d: d, fill: "none", stroke: "var(--series-1)", "stroke-width": 2, "stroke-linejoin": "round", "stroke-linecap": "round" }, svg);

        const cross = node("line", { y1: m.top, y2: m.top + ph, stroke: "var(--axis)", "stroke-width": 1, visibility: "hidden" }, svg);
        pts.forEach((p, i) => {
            const isHi = options.highlight === p.number;
            node("circle", {
                cx: x(i), cy: y(p.global), r: isHi ? 6 : 4.5,
                fill: "var(--series-1)", stroke: "var(--acc-card)", "stroke-width": 2,
            }, svg);
        });
        const last = pts[pts.length - 1];
        const end = node("text", { x: x(pts.length - 1) + 10, y: y(last.global) + 4, class: "trend-end" }, svg);
        end.textContent = fmt(last.global);

        // Couche de survol : point le plus proche en x.
        const hit = node("rect", { x: m.left - 10, y: 0, width: pw + 20, height: H, fill: "transparent" }, svg);
        hit.addEventListener("mousemove", (e) => {
            const r = svg.getBoundingClientRect();
            const mx = ((e.clientX - r.left) / r.width) * W;
            let best = 0;
            pts.forEach((_, i) => {
                if (Math.abs(x(i) - mx) < Math.abs(x(best) - mx)) best = i;
            });
            const p = pts[best];
            cross.setAttribute("x1", x(best));
            cross.setAttribute("x2", x(best));
            cross.setAttribute("visibility", "visible");
            const prev = best > 0 ? pts[best - 1] : null;
            showTip(
                "<b>" + unit + " " + p.number + "</b><br>" + valueLabel + " : <b>" + fmt(p.global) + "</b>/100" +
                    (prev ? "<br>" + signed(p.global - prev.global) + " vs " + unit.toLowerCase() + " " + prev.number : ""),
                e.clientX,
                e.clientY
            );
        });
        hit.addEventListener("mouseleave", () => {
            cross.setAttribute("visibility", "hidden");
            hideTip();
        });
        el.appendChild(svg);
    };

    draw();
    if ("ResizeObserver" in window) {
        let last = el.clientWidth;
        new ResizeObserver(() => {
            if (Math.abs(el.clientWidth - last) > 4) {
                last = el.clientWidth;
                draw();
            }
        }).observe(el);
    }
}
