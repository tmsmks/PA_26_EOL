/**
 * PA 2026 — Deck minimaliste : 1 slide = 1 concept + 1 illustration, <= 16 mots, sans ponctuation.
 * Palette bleu HES-SO, police Calibri, taille >= 20 pt. ~20 slides. Le discours est dans le script PDF.
 */
const path = require("path");
const PptxGenJS = require("pptxgenjs");
const A = (f) => path.join(__dirname, "assets", f);

const NAVY = "12284C", BLUE = "0069B4", INK = "26333F", MUTED = "8A97A4";
const ICE = "EAF1F8", ICE2 = "F4F8FC", LINE = "D6E1EC", WHITE = "FFFFFF", FONT = "Calibri";
const W = 13.333, H = 7.5, M = 0.62;
const S = pptx => pptx; // noop

const pptx = new PptxGenJS();
pptx.defineLayout({ name: "WIDE", width: W, height: H });
pptx.layout = "WIDE";
pptx.author = "Thomas Maksimous";
pptx.title = "Livre interactif — PA MSE HES-SO";

const FOOT = "Livre interactif · fin de vie — PA MSE HES-SO";
pptx.defineSlideMaster({ title: "COVER", background: { color: WHITE } });
pptx.defineSlideMaster({
  title: "C", background: { color: WHITE },
  objects: [{ text: { text: FOOT, options: { x: M, y: 7.08, w: 9, h: 0.3, fontFace: FONT, fontSize: 9, color: MUTED } } }],
  slideNumber: { x: 12.55, y: 7.06, w: 0.6, h: 0.3, fontFace: FONT, fontSize: 9, color: MUTED, align: "right" },
});

// ---- helpers ----
function head(s, eye, title) {
  s.addText(eye.toUpperCase(), { x: M, y: 0.5, w: 12, h: 0.35, fontFace: FONT, fontSize: 20, bold: true, color: MUTED, charSpacing: 1 });
  s.addText(title, { x: M, y: 0.95, w: 12.1, h: 0.95, fontFace: FONT, fontSize: 32, bold: true, color: NAVY, valign: "top" });
}
function chip(s, x, y, w, label, o = {}) {
  const h = o.h || 0.6;
  s.addShape(pptx.ShapeType.roundRect, { x, y, w, h, fill: { color: o.fill || ICE }, line: { color: o.line || LINE, width: 1 }, rectRadius: 0.12 });
  s.addText(label, { x, y, w, h, fontFace: FONT, fontSize: o.fs || 20, bold: !!o.bold, color: o.color || NAVY, align: "center", valign: "middle" });
}
function kw(s, x, y, w, runs, al) {
  s.addText(runs, { x, y, w, h: 0.5, fontFace: FONT, fontSize: 22, align: al || "center", valign: "middle" });
}
// barres horizontales = illustration "graphe"
function hbars(s, rows, c) {
  rows.forEach((r, i) => {
    const y = c.y0 + i * c.rh, hi = r.hi;
    s.addText(r.label, { x: c.lx, y: y - 0.04, w: c.lw, h: c.bh + 0.08, fontFace: FONT, fontSize: 20, bold: hi, color: hi ? BLUE : INK, align: "right", valign: "middle" });
    const bw = Math.max(0.06, (r.val / c.maxV) * c.bmax);
    s.addShape(pptx.ShapeType.roundRect, { x: c.bx, y, w: bw, h: c.bh, fill: { color: hi ? BLUE : ICE }, line: { color: hi ? BLUE : LINE, width: 1 }, rectRadius: 0.04 });
    s.addText(r.txt, { x: c.bx + bw + 0.12, y: y - 0.04, w: 1.7, h: c.bh + 0.08, fontFace: FONT, fontSize: 20, bold: hi, color: hi ? BLUE : MUTED, valign: "middle" });
  });
}

// =========================================================
// 1 — COVER (page de titre : exception au quota de mots)
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "COVER" });
  const hH = 0.62;
  s.addImage({ path: A("logo_hesso.png"), x: M, y: 0.55, h: hH, w: hH * 1074 / 694 });
  s.addImage({ path: A("logo_chuv.png"), x: 2.05, y: 0.58, h: hH * 0.92, w: hH * 0.92 * 1920 / 994 });
  s.addImage({ path: A("logo_unil.png"), x: 4.35, y: 0.66, h: hH * 0.62, w: hH * 0.62 * 1613 / 528 });
  s.addText("PROJET D'APPROFONDISSEMENT · MSE HES-SO", { x: M, y: 2.15, w: 12, h: 0.4, fontFace: FONT, fontSize: 20, bold: true, color: MUTED, charSpacing: 1 });
  s.addText([{ text: "Livre interactif pour le personnel médical", options: { color: NAVY } }, { text: "\naccompagnant les patients en fin de vie", options: { color: NAVY } }],
    { x: M, y: 2.65, w: 12.1, h: 1.7, fontFace: FONT, fontSize: 40, bold: true, valign: "top", lineSpacingMultiple: 1.02 });
  s.addText([{ text: "Storytelling et ", options: { color: INK } }, { text: "soft-skills", options: { color: BLUE, bold: true } }, { text: " assistés par IA", options: { color: INK } }],
    { x: M, y: 4.35, w: 12, h: 0.5, fontFace: FONT, fontSize: 22, valign: "top" });
  s.addText("Thomas Maksimous", { x: M, y: 5.35, w: 12, h: 0.45, fontFace: FONT, fontSize: 22, bold: true, color: NAVY });
  s.addText("Sup. Prof. Stéphane Gobron · Experte Dre Claudia Gamondi", { x: M, y: 5.85, w: 12.2, h: 0.4, fontFace: FONT, fontSize: 20, color: INK });
  s.addText("Lausanne · 16 juin 2026", { x: M, y: 6.28, w: 12, h: 0.4, fontFace: FONT, fontSize: 20, color: MUTED });
})();

// =========================================================
// 2 — Storytelling EHPAD
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Introduction", "Un mois en EHPAD");
  s.addShape(pptx.ShapeType.ellipse, { x: 5.42, y: 2.45, w: 2.5, h: 2.5, fill: { color: ICE }, line: { color: BLUE, width: 2 } });
  s.addText("?", { x: 5.42, y: 2.4, w: 2.5, h: 2.6, fontFace: FONT, fontSize: 120, bold: true, color: BLUE, align: "center", valign: "middle" });
  kw(s, 3.67, 5.35, 6.0, [{ text: "aucun mode d'emploi", options: { color: NAVY, bold: true } }]);
  kw(s, 3.67, 5.95, 6.0, [{ text: "Alzheimer", options: { color: MUTED } }]);
})();

// =========================================================
// 3 — Hard vs Soft
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Introduction", "Soft-skills la vraie difficulté");
  s.addShape(pptx.ShapeType.gear6, { x: 2.35, y: 2.7, w: 2.3, h: 2.3, fill: { color: NAVY } });
  s.addText("HARD SKILLS", { x: 1.5, y: 5.2, w: 4.0, h: 0.4, fontFace: FONT, fontSize: 22, bold: true, color: NAVY, align: "center" });
  s.addText("factuel", { x: 1.5, y: 5.65, w: 4.0, h: 0.4, fontFace: FONT, fontSize: 20, color: MUTED, align: "center" });
  s.addShape(pptx.ShapeType.heart, { x: 8.7, y: 2.7, w: 2.3, h: 2.3, fill: { color: BLUE } });
  s.addText("SOFT SKILLS", { x: 7.85, y: 5.2, w: 4.0, h: 0.4, fontFace: FONT, fontSize: 22, bold: true, color: BLUE, align: "center" });
  s.addText("boîte noire", { x: 7.85, y: 5.65, w: 4.0, h: 0.4, fontFace: FONT, fontSize: 20, color: MUTED, align: "center" });
  s.addText("vs", { x: 5.9, y: 3.5, w: 1.5, h: 0.7, fontFace: FONT, fontSize: 30, italic: true, color: MUTED, align: "center" });
})();

// =========================================================
// 4 — 3 S -> soft-skills
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Introduction", "Du savoir-être aux soft-skills");
  const boxes = [["Savoir-faire", ICE, NAVY], ["Savoir-vivre", ICE, NAVY], ["Savoir-être", "DCE7F4", BLUE]];
  let x = 0.85; const y = 3.15, bw = 2.55, bh = 1.5;
  boxes.forEach((b, i) => {
    s.addShape(pptx.ShapeType.roundRect, { x, y, w: bw, h: bh, fill: { color: b[1] }, line: { color: i === 2 ? BLUE : LINE, width: 1 }, rectRadius: 0.08 });
    s.addText(b[0], { x, y, w: bw, h: bh, fontFace: FONT, fontSize: 22, bold: true, color: b[2], align: "center", valign: "middle" });
    x += bw + 0.18;
  });
  s.addShape(pptx.ShapeType.rightArrow, { x: 9.0, y: 3.55, w: 0.9, h: 0.7, fill: { color: MUTED } });
  s.addShape(pptx.ShapeType.roundRect, { x: 10.0, y: 3.15, w: 2.7, h: 1.5, fill: { color: BLUE }, line: { color: BLUE, width: 1 }, rectRadius: 0.08 });
  s.addText("soft-skills", { x: 10.0, y: 3.15, w: 2.7, h: 1.5, fontFace: FONT, fontSize: 22, bold: true, color: WHITE, align: "center", valign: "middle" });
})();

// =========================================================
// 5 — Les 7 SOSK
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Introduction", "Les 7 SOSK");
  const sosk = ["Respect", "Empathie", "Compassion", "Régulation", "Clarté", "Frontières", "Collaboration"];
  const cols = 4, cw = 2.85, gap = 0.22, x0 = (W - (cols * cw + (cols - 1) * gap)) / 2;
  sosk.forEach((t, i) => {
    const c = i % cols, r = Math.floor(i / cols);
    chip(s, x0 + c * (cw + gap), 2.55 + r * 0.95, cw, t, { fill: ICE, color: NAVY, h: 0.7 });
  });
  // echelle -3 a +3
  s.addText([{ text: "−3", options: { color: NAVY, bold: true } }, { text: "      à      ", options: { color: MUTED } }, { text: "+3", options: { color: BLUE, bold: true } }],
    { x: 0, y: 5.0, w: W, h: 0.7, fontFace: FONT, fontSize: 30, align: "center" });
})();

// =========================================================
// 6 — Besoin / public
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Contexte", "Former sans terrain à risque");
  s.addShape(pptx.ShapeType.wedgeRoundRectCallout, { x: 5.4, y: 2.45, w: 2.55, h: 2.2, fill: { color: BLUE } });
  kw(s, 1.5, 5.45, 4.5, [{ text: "jeunes diplômés", options: { color: NAVY, bold: true } }]);
  kw(s, 7.3, 5.45, 4.5, [{ text: "jeux de rôle limités", options: { color: MUTED } }]);
})();

// =========================================================
// 7 — Etat de l'art (3 travaux, 1 strip d'images)
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "État de l'art", "Trois approches incomplètes");
  const works = [["work_ldr.png", 1.559, "LDR", "figé"], ["work_twine.png", 2.366, "Twine", "générique"], ["work_percs.png", 1.301, "PERCS", "présentiel"]];
  const colW = 3.85, gap = 0.27; let x = M; const y = 2.4, boxH = 2.4;
  works.forEach((wk) => {
    let iw = colW - 0.3, ih = iw / wk[1]; if (ih > boxH) { ih = boxH; iw = ih * wk[1]; }
    s.addImage({ path: A(wk[0]), x: x + (colW - iw) / 2, y: y + (boxH - ih) / 2, w: iw, h: ih });
    s.addText([{ text: wk[2] + "  ", options: { color: BLUE, bold: true } }, { text: wk[3], options: { color: MUTED } }],
      { x, y: y + boxH + 0.2, w: colW, h: 0.5, fontFace: FONT, fontSize: 22, align: "center" });
    x += colW + gap;
  });
})();

// =========================================================
// 8 — Historique V1 -> V2 -> V3
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "État de l'art", "De V1 à la V3");
  const st = [["V1", "texte", ICE, NAVY], ["V2", "3D figé", ICE, NAVY], ["V3", "éditable", "DCE7F4", BLUE]];
  let x = 1.4; const y = 3.0, bw = 2.9, bh = 1.7, gap = 1.05;
  st.forEach((d, i) => {
    s.addShape(pptx.ShapeType.roundRect, { x, y, w: bw, h: bh, fill: { color: d[2] }, line: { color: i === 2 ? BLUE : LINE, width: 1 }, rectRadius: 0.08 });
    s.addText(d[0], { x, y: y + 0.2, w: bw, h: 0.8, fontFace: FONT, fontSize: 40, bold: true, color: d[3], align: "center" });
    s.addText(d[1], { x, y: y + 1.0, w: bw, h: 0.6, fontFace: FONT, fontSize: 22, color: i === 2 ? NAVY : MUTED, align: "center" });
    if (i < 2) s.addShape(pptx.ShapeType.rightArrow, { x: x + bw + 0.08, y: y + bh / 2 - 0.3, w: gap - 0.16, h: 0.6, fill: { color: MUTED } });
    x += bw + gap;
  });
})();

// =========================================================
// 9 — Solution V3
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Solution", "Deux verrous levés");
  const ratio = 3360 / 1812, w = 7.4, h = w / ratio;
  s.addImage({ path: A("ui_3panels.png"), x: M, y: 2.1, w, h });
  let yy = 2.5;
  [["graphe éditable", BLUE], ["IA assistée", BLUE], ["validation humaine", NAVY]].forEach((d) => {
    chip(s, 8.5, yy, 4.2, d[0], { fill: ICE, color: d[1], bold: true, h: 0.7 }); yy += 0.95;
  });
})();

// =========================================================
// 10 — Graphe
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Développement", "Le scénario devient un graphe");
  const ratio = 3360 / 1812, w = 8.4, h = w / ratio;
  s.addImage({ path: A("ui_graph.png"), x: (W - w) / 2, y: 2.05, w, h });
  kw(s, 2.4, 2.05 + h + 0.15, 4.2, [{ text: "interaction ", options: { color: INK } }, { text: "→ nœud", options: { color: BLUE, bold: true } }]);
  kw(s, 6.7, 2.05 + h + 0.15, 4.2, [{ text: "réponse ", options: { color: INK } }, { text: "→ arête", options: { color: BLUE, bold: true } }]);
})();

// =========================================================
// 11 — Coherence
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Développement", "Des histoires cohérentes");
  const ratio = 3360 / 1812, w = 8.0, h = w / ratio;
  s.addImage({ path: A("ui_parcours.png"), x: (W - w) / 2, y: 2.05, w, h });
  kw(s, 2.4, 2.05 + h + 0.15, 4.2, [{ text: "validation ", options: { color: INK } }, { text: "EG-7", options: { color: BLUE, bold: true } }]);
  kw(s, 6.7, 2.05 + h + 0.15, 4.2, [{ text: "parcours ", options: { color: INK } }, { text: "joueur", options: { color: BLUE, bold: true } }]);
})();

// =========================================================
// 12 — IA creation + scoring
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Développement", "Créer et scorer par IA");
  const ratio = 1536 / 1166, w = 5.2, h = w / ratio;
  s.addImage({ path: A("ui_modale.png"), x: 7.2, y: 2.1, w, h });
  let yy = 2.7;
  [["génération orientée", BLUE], ["scoring expliqué", BLUE], ["humain valide", NAVY]].forEach((d) => {
    chip(s, M, yy, 5.4, d[0], { fill: ICE, color: d[1], bold: true, h: 0.75 }); yy += 1.05;
  });
})();

// =========================================================
// 13 — Conformite 100%
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Résultats", "Conformité parfaite");
  s.addShape(pptx.ShapeType.donut, { x: 2.0, y: 2.45, w: 3.0, h: 3.0, fill: { color: BLUE } });
  s.addText("100 %", { x: 2.0, y: 2.45, w: 3.0, h: 3.0, fontFace: FONT, fontSize: 40, bold: true, color: NAVY, align: "center", valign: "middle" });
  kw(s, 6.0, 3.3, 6.5, [{ text: "50 générations orientées", options: { color: NAVY, bold: true } }], "left");
  kw(s, 6.0, 3.95, 6.5, [{ text: "0 échec de format", options: { color: MUTED } }], "left");
})();

// =========================================================
// 14 — Scoring MAE (barres)
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Résultats", "Scoring proche de l'humain");
  const rows = [
    { label: "Collaboration", val: 0.13, txt: "0,13" }, { label: "Régulation", val: 0.60, txt: "0,60" },
    { label: "Respect", val: 0.67, txt: "0,67" }, { label: "Clarté", val: 0.73, txt: "0,73" },
    { label: "Frontières", val: 0.87, txt: "0,87" }, { label: "Compassion", val: 1.07, txt: "1,07" },
    { label: "Empathie", val: 1.33, txt: "1,33" },
  ];
  hbars(s, rows, { lx: M, lw: 2.7, bx: 3.55, bmax: 6.5, y0: 2.2, rh: 0.52, bh: 0.34, maxV: 1.4 });
  s.addText([{ text: "MAE ", options: { color: NAVY, bold: true } }, { text: "0,77", options: { color: BLUE, bold: true } }, { text: "  sur 7 niveaux", options: { color: MUTED } }],
    { x: M, y: 6.05, w: 8, h: 0.5, fontFace: FONT, fontSize: 22, valign: "middle" });
})();

// =========================================================
// 15 — OpenAI vs Ollama (vitesse)
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Résultats", "Cloud rapide ou local privé");
  hbars(s, [
    { label: "OpenAI", val: 9.2, txt: "9 s", hi: true },
    { label: "Ollama", val: 98.2, txt: "98 s" },
  ], { lx: M, lw: 2.6, bx: 3.5, bmax: 7.0, y0: 2.9, rh: 1.1, bh: 0.7, maxV: 100 });
  kw(s, M, 5.4, 6.0, [{ text: "rapide ", options: { color: BLUE, bold: true } }, { text: "et précis", options: { color: INK } }], "left");
  kw(s, M, 6.0, 7.0, [{ text: "local ", options: { color: NAVY, bold: true } }, { text: "et conforme RGPD", options: { color: INK } }], "left");
})();

// =========================================================
// 16 — Demo live
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Démonstration", "Démonstration live");
  s.addShape(pptx.ShapeType.ellipse, { x: 5.42, y: 2.55, w: 2.5, h: 2.5, fill: { color: ICE }, line: { color: BLUE, width: 2 } });
  s.addShape(pptx.ShapeType.triangle, { x: 6.35, y: 3.35, w: 1.0, h: 1.0, fill: { color: BLUE }, rotate: 90 });
  s.addText([{ text: "graphe      IA      scoring", options: { color: NAVY, bold: true } }],
    { x: 0, y: 5.45, w: W, h: 0.6, fontFace: FONT, fontSize: 24, align: "center" });
})();

// =========================================================
// 17 — Prix (barres, tous modeles)
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Discussion", "Parmi les moins chers");
  hbars(s, [
    { label: "Llama 3.1 8B", val: 0, txt: "local" }, { label: "DeepSeek V4", val: 0.28, txt: "0,28" },
    { label: "gpt-4o-mini", val: 0.60, txt: "0,60" }, { label: "gpt-4.1-mini", val: 1.60, txt: "1,60", hi: true },
    { label: "Gemini 2.5 Flash", val: 2.50, txt: "2,50" }, { label: "Gemini 2.5 Pro", val: 10, txt: "10" },
    { label: "Claude Sonnet 4.6", val: 15, txt: "15" }, { label: "GPT-5.5", val: 30, txt: "30" },
  ], { lx: M, lw: 2.9, bx: 3.7, bmax: 7.0, y0: 2.1, rh: 0.55, bh: 0.34, maxV: 30 });
  s.addText("$ / M tokens — sortie", { x: 3.7, y: 6.6, w: 6, h: 0.35, fontFace: FONT, fontSize: 14, italic: true, color: MUTED });
})();

// =========================================================
// 18 — RGPD / ethique
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Discussion", "Données et responsabilité");
  s.addShape(pptx.ShapeType.cloud, { x: 2.0, y: 2.6, w: 2.7, h: 2.0, fill: { color: ICE }, line: { color: BLUE, width: 2 } });
  s.addText("serveur externe", { x: 1.4, y: 4.85, w: 3.9, h: 0.5, fontFace: FONT, fontSize: 22, bold: true, color: NAVY, align: "center" });
  s.addShape(pptx.ShapeType.cube, { x: 8.7, y: 2.6, w: 2.3, h: 2.0, fill: { color: BLUE } });
  s.addText("serveur local", { x: 8.0, y: 4.85, w: 3.9, h: 0.5, fontFace: FONT, fontSize: 22, bold: true, color: BLUE, align: "center" });
  s.addText("vs", { x: 5.9, y: 3.3, w: 1.5, h: 0.7, fontFace: FONT, fontSize: 30, italic: true, color: MUTED, align: "center" });
  s.addText([{ text: "l'humain décide toujours", options: { color: MUTED, italic: true } }], { x: 0, y: 6.0, w: W, h: 0.5, fontFace: FONT, fontSize: 20, align: "center" });
})();

// =========================================================
// 19 — Conclusion + perspectives
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "C" });
  head(s, "Conclusion", "Bilan et perspectives");
  s.addText("LIVRÉ", { x: M, y: 2.2, w: 5.6, h: 0.4, fontFace: FONT, fontSize: 20, bold: true, color: MUTED });
  let yy = 2.75;
  ["graphe éditable", "IA assistée", "architecture durable"].forEach((t) => {
    chip(s, M, yy, 5.6, t, { fill: ICE, color: NAVY, h: 0.7 }); yy += 0.95;
  });
  s.addShape(pptx.ShapeType.rightArrow, { x: 6.25, y: 3.9, w: 0.85, h: 0.7, fill: { color: MUTED } });
  s.addText("VERS LE MASTER", { x: 7.3, y: 2.2, w: 5.4, h: 0.4, fontFace: FONT, fontSize: 20, bold: true, color: MUTED });
  yy = 2.75;
  ["scoring temps réel", "ML local CHUV"].forEach((t) => {
    chip(s, 7.3, yy, 5.4, t, { fill: "DCE7F4", color: BLUE, bold: true, line: BLUE, h: 0.7 }); yy += 0.95;
  });
})();

// =========================================================
// 20 — Merci
// =========================================================
(() => {
  const s = pptx.addSlide({ masterName: "COVER" });
  s.addText("Merci", { x: M, y: 2.7, w: 12.1, h: 1.0, fontFace: FONT, fontSize: 48, bold: true, color: NAVY });
  s.addText("Questions", { x: M, y: 3.85, w: 12, h: 0.6, fontFace: FONT, fontSize: 24, color: INK });
  const hH = 0.6;
  s.addImage({ path: A("logo_hesso.png"), x: M, y: 6.1, h: hH, w: hH * 1074 / 694 });
  s.addImage({ path: A("logo_chuv.png"), x: 2.05, y: 6.13, h: hH * 0.92, w: hH * 0.92 * 1920 / 994 });
  s.addImage({ path: A("logo_unil.png"), x: 4.35, y: 6.21, h: hH * 0.62, w: hH * 0.62 * 1613 / 528 });
})();

const OUT = path.join(__dirname, "PA_2026_EOL_v3.pptx");
pptx.writeFile({ fileName: OUT }).then(() => console.log("WROTE " + OUT));
