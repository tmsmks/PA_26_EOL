// Graphiques des pages de suivi — HTML/SVG natifs, sans dépendance.
//
// - skillBars : profil des 7 compétences, trié, avec repère de comparaison ;
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

/* --- Profil de compétences --- */

/**
 * @param {HTMLElement} el
 * @param {{skills: string[], labels: object, current: object, compare?: object,
 *          compareLabel?: string, currentLabel?: string,
 *          strengths?: string[], weaknesses?: string[]}} opts
 */
export function skillBars(el, opts) {
    const current = opts.current || {};
    const compare = opts.compare || null;
    const strengths = opts.strengths || [];
    const weaknesses = opts.weaknesses || [];
    const rows = opts.skills
        .filter((k) => current[k] !== null && current[k] !== undefined)
        .sort((a, b) => current[b] - current[a]);
    const missing = opts.skills.filter((k) => current[k] === null || current[k] === undefined);

    el.innerHTML = "";
    const wrap = document.createElement("div");
    wrap.className = "skill-bars";
    rows.forEach((k) => {
        const v = current[k];
        const p = compare ? compare[k] : null;
        const hasPrev = p !== null && p !== undefined;
        const row = document.createElement("div");
        row.className = "skill-row";
        row.tabIndex = 0;
        let tag = "";
        if (strengths.includes(k)) tag = '<span class="up" aria-hidden="true">▲</span> Point fort';
        else if (weaknesses.includes(k)) tag = '<span class="down" aria-hidden="true">▼</span> À travailler';
        row.innerHTML =
            '<span class="skill-label">' + esc(opts.labels[k] || k) + "</span>" +
            '<span class="skill-track">' +
            '<span class="skill-fill" style="width:' + Math.max(0.5, v) + '%"></span>' +
            (hasPrev ? '<span class="skill-prev" style="left:' + p + '%"></span>' : "") +
            "</span>" +
            '<span class="skill-value">' + fmt(v) + "</span>" +
            '<span class="skill-tag">' + tag + "</span>";
        const label = opts.labels[k] || k;
        row.setAttribute(
            "aria-label",
            label + " : " + fmt(v) + " sur 100" +
                (hasPrev ? ", " + (opts.compareLabel || "comparaison") + " " + fmt(p) : "")
        );
        bindTip(
            row,
            "<b>" + esc(label) + "</b><br>" +
                esc(opts.currentLabel || "Cette session") + " : <b>" + fmt(v) + "</b>/100" +
                (hasPrev
                    ? "<br>" + esc(opts.compareLabel || "Comparaison") + " : " + fmt(p) +
                      " (" + signed(v - p) + ")"
                    : "")
        );
        wrap.appendChild(row);
    });

    const axis = document.createElement("div");
    axis.className = "skill-axis";
    axis.innerHTML =
        "<span></span>" +
        '<span class="skill-axis-ticks"><span>0</span><span>25</span><span>50</span><span>75</span><span>100</span></span>' +
        "<span></span><span></span>";
    wrap.appendChild(axis);
    el.appendChild(wrap);

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
