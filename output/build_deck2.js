const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.defineLayout({ name: "W", width: 13.333, height: 7.5 });
p.layout = "W";

const _slides = [];
function newSlide(){ const sl = p.addSlide(); _slides.push(sl); return sl; }

// ---- Palette (Slidesgo "Public Health" : medical + AI) ----
const NAVY  = "001B58"; // deep navy — titres / texte fort
const ROYAL = "385CB0"; // bleu royal — primaire
const LBLUE = "76A3EE"; // bleu clair
const PALE  = "E3EDFF"; // bleu pâle — fonds
const TEAL  = "0097A7"; // accent teal
const WHITE = "FFFFFF";
const INK   = "33415C"; // corps de texte
const MUTE  = "8893AE"; // gris doux

const RR = p.ShapeType.roundRect, EL = p.ShapeType.ellipse, LN = p.ShapeType.line, RC = p.ShapeType.rect;

const HF = "Archivo";   // header font
const BF = "Assistant"; // body font

// ---------- decorative helpers ----------
function frame(s){
  // thin rounded blue border (signature Slidesgo frame)
  s.addShape(RR, { x:0.16, y:0.16, w:13.01, h:7.18, fill:{ type:"none" }, line:{ color:ROYAL, width:1.5 }, rectRadius:0.12 });
}
function cross(s, x, y, sz, color){
  const t = sz*0.34;
  s.addShape(RR, { x:x+(sz-t)/2, y, w:t, h:sz, fill:{color}, line:{type:"none"}, rectRadius:t*0.28 });
  s.addShape(RR, { x:x, y:y+(sz-t)/2, w:sz, h:t, fill:{color}, line:{type:"none"}, rectRadius:t*0.28 });
}
function dots(s, x, y, n, color, active){
  for(let i=0;i<n;i++) s.addShape(EL, { x:x+i*0.22, y, w:0.09, h:0.09, fill:{color: i===active?color:LBLUE}, line:{type:"none"} });
}
function iconCircle(s, x, y, d, fill, glyph, gColor){
  s.addShape(EL, { x, y, w:d, h:d, fill:{color:fill}, line:{type:"none"} });
  if(glyph==="+"){ cross(s, x+d*0.28, y+d*0.28, d*0.44, gColor||WHITE); }
  else s.addText(glyph, { x, y, w:d, h:d, fontFace:HF, fontSize:d*22, bold:true, color:gColor||WHITE, align:"center", valign:"middle" });
}
function header(s, kicker, title){
  iconCircle(s, 0.62, 0.62, 0.5, ROYAL, "+");
  s.addText(kicker.toUpperCase(), { x:1.3, y:0.58, w:11, h:0.3, fontFace:BF, fontSize:12, color:TEAL, bold:true, charSpacing:3 });
  s.addText(title, { x:1.3, y:0.86, w:11.3, h:0.7, fontFace:HF, fontSize:28, color:NAVY, bold:true });
}
function pageNum(s, n){
  dots(s, 10.75, 6.92, 5, ROYAL, (n-1)%5);
  s.addText(String(n), { x:0.6, y:6.85, w:0.6, h:0.35, fontFace:BF, fontSize:11, color:MUTE });
}
// corner decorations (quarter circles + scattered crosses)
function corners(s, variant){
  if(variant!==2){
    s.addShape(EL, { x:-1.7, y:-1.7, w:3.2, h:3.2, fill:{color:PALE}, line:{type:"none"} });
  }
  s.addShape(EL, { x:12.0, y:5.7, w:2.6, h:2.6, fill:{color:variant===2?PALE:LBLUE}, line:{type:"none"} });
  cross(s, 12.35, 0.7, 0.34, LBLUE);
  cross(s, 0.62, 6.0, 0.3, PALE);
}

// =========================================================
// SLIDE 1 — TITLE
// =========================================================
let s = newSlide(); s.background={color:WHITE}; frame(s);
s.addShape(EL, { x:-2.0, y:-2.0, w:4.2, h:4.2, fill:{color:PALE}, line:{type:"none"} });
s.addShape(EL, { x:-1.1, y:-1.1, w:2.4, h:2.4, fill:{color:LBLUE}, line:{type:"none"} });
s.addShape(EL, { x:11.7, y:5.4, w:3.1, h:3.1, fill:{color:ROYAL}, line:{type:"none"} });
s.addShape(EL, { x:12.5, y:6.2, w:1.6, h:1.6, fill:{color:LBLUE}, line:{type:"none"} });
cross(s, 11.4, 0.95, 0.4, LBLUE); cross(s, 10.3, 1.9, 0.28, PALE); cross(s, 0.45, 4.6, 0.3, PALE);
dots(s, 1.0, 2.0, 5, ROYAL, 0);

iconCircle(s, 1.0, 2.45, 0.62, ROYAL, "+");
s.addText("PROJET D'APPROFONDISSEMENT (PA) · MSE HES-SO · Nº 2026-01", { x:1.0, y:3.25, w:11, h:0.35, fontFace:BF, fontSize:13, color:TEAL, bold:true, charSpacing:2 });
s.addText("Interactive Book for Medical Staff\ndealing with End-of-life Patients", { x:1.0, y:3.6, w:10.6, h:1.6, fontFace:HF, fontSize:38, color:NAVY, bold:true, lineSpacingMultiple:1.0 });
s.addText("Storytelling & soft-skills consistencies using AI", { x:1.02, y:5.2, w:10, h:0.5, fontFace:BF, fontSize:19, color:ROYAL, italic:true });
s.addText([
  { text:"Thomas Maksimous", options:{ bold:true, color:NAVY, fontSize:15, breakLine:true } },
  { text:"Sup. Prof. Stéphane Gobron (HES-SO)  ·  Experte Dre Claudia Gamondi, MD (CHUV)", options:{ color:INK, fontSize:12, breakLine:true } },
  { text:"HES-SO Master · CHUV · UniL   |   Lausanne, juin 2026", options:{ color:MUTE, fontSize:12 } },
], { x:1.02, y:5.95, w:11, h:1.1, fontFace:BF, lineSpacingMultiple:1.3 });

// =========================================================
// SLIDE 2 — CONTEXTE
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,1);
header(s, "Contexte", "Former à la communication en fin de vie");
const ctx = [
  ["Un défi humain", "Au-delà du clinique, les soignants mobilisent empathie, respect et compassion face au deuil et à la détresse.", "+"],
  ["Méthode actuelle", "Jeux de rôle en petits groupes : efficaces, mais chronophages et difficiles à mettre à l'échelle.", "+"],
  ["Serious game « End of Life »", "Simulation 3D développée à la HES-SO avec le CHUV — la base de ce projet.", "+"],
];
ctx.forEach((c,i)=>{
  const y = 1.95 + i*1.45;
  iconCircle(s, 0.7, y+0.1, 0.7, [ROYAL,LBLUE,TEAL][i], "+");
  s.addText(c[0], { x:1.65, y:y, w:6.4, h:0.42, fontFace:HF, fontSize:17, bold:true, color:NAVY });
  s.addText(c[1], { x:1.65, y:y+0.45, w:6.5, h:0.85, fontFace:BF, fontSize:13.5, color:INK, lineSpacingMultiple:1.1 });
});
s.addShape(RR, { x:8.55, y:1.95, w:4.15, h:4.45, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.14 });
cross(s, 11.9, 2.2, 0.4, LBLUE);
s.addText("LE CONSTAT", { x:8.9, y:2.3, w:3.6, h:0.35, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:2 });
s.addText("« Que signifie soigner lorsque guérir n'est plus l'objectif ? »", { x:8.9, y:2.75, w:3.5, h:1.5, fontFace:HF, fontSize:20, italic:true, bold:true, color:NAVY, lineSpacingMultiple:1.05 });
s.addText("La fin de vie expose à des situations sans réponse unique : il faut un cadre d'apprentissage immersif et sécurisé avant l'exposition réelle.", { x:8.9, y:4.5, w:3.5, h:1.7, fontFace:BF, fontSize:13, color:INK, lineSpacingMultiple:1.2 });
pageNum(s,2);

// =========================================================
// SLIDE 3 — VERROUS
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Problématique", "Deux verrous de l'application existante");
const locks = [
  ["01","Contenu figé & inaccessible","Scénarios stockés dans des fichiers JSON statiques. Impossible à modifier pour un médecin non-informaticien.", ROYAL],
  ["02","Évaluation superficielle","Scoring limité à 3 axes fixes (empathie, respect, compassion), sans analyse sémantique des choix.", TEAL],
];
locks.forEach((l,i)=>{
  const x = 0.7 + i*6.2;
  s.addShape(RR, { x, y:2.1, w:5.8, h:3.7, fill:{color:i?WHITE:PALE}, line:{color:LBLUE,width:1.25}, rectRadius:0.14 });
  s.addShape(EL, { x:x+0.45, y:2.55, w:1.1, h:1.1, fill:{color:l[3]}, line:{type:"none"} });
  s.addText(l[0], { x:x+0.45, y:2.55, w:1.1, h:1.1, fontFace:HF, fontSize:28, bold:true, color:WHITE, align:"center", valign:"middle" });
  s.addText(l[1], { x:x+0.45, y:3.85, w:4.95, h:0.5, fontFace:HF, fontSize:19, bold:true, color:NAVY });
  s.addText(l[2], { x:x+0.45, y:4.4, w:4.95, h:1.3, fontFace:BF, fontSize:14, color:INK, lineSpacingMultiple:1.18 });
});
s.addText("Besoin : une infrastructure flexible + une IA pour épauler créateurs de contenu et apprenants.", { x:0.7, y:6.15, w:12, h:0.5, fontFace:BF, fontSize:14, italic:true, bold:true, color:ROYAL });
pageNum(s,3);

// =========================================================
// SLIDE 4 — OBJECTIFS (navy divider style)
// =========================================================
s = newSlide(); s.background={color:NAVY};
s.addShape(RR, { x:0.16, y:0.16, w:13.01, h:7.18, fill:{type:"none"}, line:{color:LBLUE,width:1.5}, rectRadius:0.12 });
s.addShape(EL, { x:-1.6, y:5.3, w:3.4, h:3.4, fill:{color:ROYAL}, line:{type:"none"} });
s.addShape(EL, { x:11.9, y:-1.6, w:3.2, h:3.2, fill:{color:ROYAL}, line:{type:"none"} });
cross(s, 12.3, 2.4, 0.4, LBLUE); cross(s, 0.42, 3.3, 0.3, LBLUE); cross(s, 11.0, 6.3, 0.3, LBLUE);
s.addText("PROJET D'APPROFONDISSEMENT (PA) · MA CONTRIBUTION", { x:0.9, y:0.62, w:11, h:0.35, fontFace:BF, fontSize:13, color:LBLUE, bold:true, charSpacing:3 });
s.addText("Deux briques que j'ai développées", { x:0.9, y:0.98, w:11.5, h:0.7, fontFace:HF, fontSize:28, color:WHITE, bold:true });
s.addText([
  { text:"Base existante (Prof. Gobron / CHUV) : ", options:{ bold:true, color:LBLUE } },
  { text:"le jeu sérieux 3D « End of Life » (Unity).   ", options:{ color:PALE } },
  { text:"Sur cette base, ma contribution PA :", options:{ bold:true, color:WHITE } },
], { x:0.9, y:1.78, w:11.6, h:0.5, fontFace:BF, fontSize:14, valign:"middle" });
const obj = [
  ["Interface d'administration en graphe","Un outil web visuel pour créer, modifier et supprimer blocs narratifs et branches — sans aucune compétence en programmation.", LBLUE],
  ["Module d'Intelligence Artificielle","Côté création : générer des réponses orientées. Côté évaluation : un scoring sémantique explicable des choix de l'apprenant.", TEAL],
];
obj.forEach((o,i)=>{
  const x = 0.9 + i*6.0;
  s.addShape(RR, { x, y:2.55, w:5.6, h:3.6, fill:{color:"0A2A66"}, line:{type:"none"}, rectRadius:0.14 });
  iconCircle(s, x+0.4, 2.9, 0.85, o[2], String(i+1), NAVY);
  s.addText(o[0], { x:x+0.4, y:4.0, w:4.85, h:0.85, fontFace:HF, fontSize:19, bold:true, color:WHITE });
  s.addText(o[1], { x:x+0.4, y:4.85, w:4.85, h:1.2, fontFace:BF, fontSize:13.5, color:PALE, lineSpacingMultiple:1.18 });
});
s.addText("Fil conducteur : un design « human-in-the-loop » — l'IA assiste, l'humain valide.", { x:0.9, y:6.45, w:11.5, h:0.4, fontFace:BF, fontSize:13.5, italic:true, color:LBLUE });

// =========================================================
// SLIDE 5 — ÉTAT DE L'ART (2x2)
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "État de l'art", "Quatre axes convergent vers le projet");
const sota = [
  ["Apps pour soignants","Aide à la décision, mindfulness anti burn-out — mais peu entraînent activement les soft skills.", ROYAL],
  ["Serious games fin de vie","Cadre LDR « Live, Die, Repeat » : 88 % des résidents plus confiants après simulation.", LBLUE],
  ["Livres dont on est le héros","Récits à embranchements (Twine, CYOA) : chaque choix devient une arête d'un graphe.", TEAL],
  ["Soft skills & profilage","Cadres PERCS, échelles IRI / JSE ; évaluation comportementale par Machine Learning.", ROYAL],
];
sota.forEach((c,i)=>{
  const col=i%2, row=Math.floor(i/2);
  const x = 0.7 + col*6.2, y = 1.95 + row*2.1;
  s.addShape(RR, { x, y, w:5.8, h:1.85, fill:{color: row+col? WHITE: PALE}, line:{color:LBLUE,width:1.1}, rectRadius:0.12 });
  iconCircle(s, x+0.35, y+0.35, 0.62, c[2], "+");
  s.addText(c[0], { x:x+1.2, y:y+0.3, w:4.4, h:0.5, fontFace:HF, fontSize:16, bold:true, color:NAVY });
  s.addText(c[1], { x:x+1.2, y:y+0.78, w:4.45, h:0.95, fontFace:BF, fontSize:13, color:INK, lineSpacingMultiple:1.12 });
});
s.addText("Lacune ciblée : un environnement narratif interactif qui entraîne ET évalue les compétences relationnelles.", { x:0.7, y:6.35, w:12, h:0.4, fontFace:BF, fontSize:13.5, italic:true, bold:true, color:ROYAL });
pageNum(s,5);

// =========================================================
// SLIDE 6 — MODÈLE DE DONNÉES
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Méthode · Modèle de données", "Du JSON hiérarchique au graphe orienté");
const chain=["Chapter","Scene","Interaction","Response"];
chain.forEach((c,i)=>{
  const y=2.0+i*0.92;
  s.addShape(RR, { x:0.75, y, w:2.7, h:0.62, fill:{color:[NAVY,ROYAL,LBLUE,TEAL][i]}, line:{type:"none"}, rectRadius:0.08 });
  s.addText(c, { x:0.75, y, w:2.7, h:0.62, fontFace:HF, fontSize:15, bold:true, color:WHITE, align:"center", valign:"middle" });
  if(i<3) s.addText("▼", { x:1.9, y:y+0.6, w:0.4, h:0.28, fontFace:BF, fontSize:11, color:LBLUE, align:"center" });
});
s.addText("Compatibilité JSON conservée\n(moteur Unity / Naninovel)", { x:0.7, y:5.85, w:2.85, h:0.7, fontFace:BF, fontSize:11.5, italic:true, color:MUTE, align:"center" });
s.addText("graph_service →", { x:3.75, y:3.45, w:1.45, h:0.4, fontFace:BF, fontSize:12, bold:true, color:TEAL, align:"center" });
const gx=6.1, gy=2.05;
const nodes={ I1:[gx+2.0,gy], I2:[gx,gy+1.15], I3:[gx+4.0,gy+1.15], I4:[gx+2.0,gy+2.3] };
[["I1","I2"],["I1","I3"],["I2","I4"],["I3","I4"]].forEach(([a,b])=>{
  s.addShape(LN, { x:nodes[a][0]+0.45, y:nodes[a][1]+0.45, w:nodes[b][0]-nodes[a][0], h:nodes[b][1]-nodes[a][1], line:{color:LBLUE,width:2} });
});
Object.entries(nodes).forEach(([k,[x,y]])=>{
  s.addShape(EL, { x, y, w:0.9, h:0.9, fill:{color:ROYAL}, line:{color:NAVY,width:1.5} });
  s.addText(k, { x, y, w:0.9, h:0.9, fontFace:HF, fontSize:15, bold:true, color:WHITE, align:"center", valign:"middle" });
});
s.addText("Chaque Interaction = nœud · chaque Response = arête (NextInteractionID).  « -1 » = fin de branche.", { x:5.5, y:5.5, w:7.2, h:0.4, fontFace:BF, fontSize:12, color:INK, align:"center" });
s.addShape(RR, { x:5.5, y:6.05, w:7.2, h:0.8, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Scoring étendu : 3 → 7 dimensions soft skills (échelle −3 à +3)", { x:5.6, y:6.1, w:7.0, h:0.33, fontFace:HF, fontSize:13, bold:true, color:NAVY, align:"center", valign:"middle" });
s.addText("Respect · Empathie · Compassion · Régulation émo. · Clarté · Frontières pro. · Collaboration", { x:5.6, y:6.43, w:7.0, h:0.33, fontFace:BF, fontSize:10.5, color:INK, align:"center", valign:"middle" });
pageNum(s,6);

// =========================================================
// SLIDE 7 — ARCHITECTURE
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Méthode · Architecture", "Clean Architecture en couches");
const layers=[
  ["Présentation","Views / Controllers — pages.py (Jinja) · api.py (REST)", NAVY],
  ["Application","Services — graph_service · validation_service · enrichment/", ROYAL],
  ["Infrastructure","Repositories — ChapterRepository : lecture / écriture JSON", LBLUE],
  ["Domaine","Models métier purs — Chapter · Scene · Interaction · Response · Actor", TEAL],
];
layers.forEach((l,i)=>{
  const y=1.95+i*1.02;
  s.addShape(RR, { x:0.75, y, w:7.6, h:0.88, fill:{color:l[2]}, line:{type:"none"}, rectRadius:0.09 });
  s.addText(l[0], { x:1.05, y:y+0.1, w:3, h:0.4, fontFace:HF, fontSize:16, bold:true, color:WHITE });
  s.addText(l[1], { x:1.05, y:y+0.48, w:7.1, h:0.34, fontFace:"Consolas", fontSize:11.5, color:"EAF1FF" });
});
s.addShape(RR, { x:2.7, y:6.4, w:3.7, h:0.55, fill:{color:WHITE}, line:{color:MUTE,width:1.25,dashType:"dash"}, rectRadius:0.06 });
s.addText("JSON files (Unity)", { x:2.7, y:6.4, w:3.7, h:0.55, fontFace:HF, fontSize:13, bold:true, color:INK, align:"center", valign:"middle" });
s.addShape(RR, { x:8.7, y:1.95, w:3.95, h:4.95, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.14 });
s.addText("POURQUOI ?", { x:9.0, y:2.2, w:3.4, h:0.35, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:2 });
[
  "Modèles métier indépendants du web, de l'IA et de la persistance",
  "Composants remplaçables (ex. backend IA) sans toucher au domaine",
  "Stack : Python / Flask · Jinja2 · JS ES Modules · vis-network",
  "Code testable, maintenable et extensible au-delà du projet",
].forEach((t,i)=>{
  const y=2.65+i*1.02;
  cross(s, 9.0, y+0.03, 0.22, ROYAL);
  s.addText(t, { x:9.35, y, w:3.05, h:0.95, fontFace:BF, fontSize:12.5, color:INK, lineSpacingMultiple:1.1 });
});
pageNum(s,7);

// =========================================================
// SLIDE 8 — PLATEFORME
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Résultats · Plateforme", "Interface d'administration livrée");
s.addShape(RR, { x:0.75, y:1.95, w:6.5, h:4.55, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.12 });
s.addText("Éditeur de graphe narratif", { x:1.0, y:2.15, w:6, h:0.4, fontFace:HF, fontSize:14, bold:true, color:NAVY });
const fn=[[1.45,3.0],[3.2,3.0],[5.05,3.0],[2.3,4.25],[4.15,4.25],[3.2,5.35]];
[[0,1],[1,2],[1,3],[1,4],[3,5],[4,5]].forEach(([a,b])=> s.addShape(LN,{ x:fn[a][0]+0.35, y:fn[a][1]+0.18, w:fn[b][0]-fn[a][0], h:fn[b][1]-fn[a][1], line:{color:LBLUE,width:1.5} }));
fn.forEach(([x,y],i)=> s.addShape(RR,{ x, y, w:0.7, h:0.36, fill:{color:i===5?TEAL:ROYAL}, line:{color:NAVY,width:0.75}, rectRadius:0.05 }));
s.addText("Liste des scènes · graphe central · panneau de propriétés", { x:1.0, y:5.95, w:6.0, h:0.4, fontFace:BF, fontSize:12, italic:true, color:INK });
const feat=[
  ["Édition CRUD complète","Textes, noms, scores et références narratives"],
  ["Validation EG-7 temps réel","Détecte les NextInteractionID invalides (branches cassées)"],
  ["Sauvegarde atomique","Fichier temporaire + os.replace — zéro corruption"],
  ["Mode parcours joueur","Simule une session, scores cumulés, sans relancer Unity"],
  ["Export Mermaid","Représentation versionnable rendue dans GitHub"],
];
feat.forEach((f,i)=>{
  const y=2.0+i*0.92;
  iconCircle(s, 7.7, y, 0.42, ROYAL, "✓");
  s.addText(f[0], { x:8.25, y:y-0.04, w:4.5, h:0.36, fontFace:HF, fontSize:14.5, bold:true, color:NAVY });
  s.addText(f[1], { x:8.25, y:y+0.32, w:4.5, h:0.5, fontFace:BF, fontSize:12, color:INK });
});
pageNum(s,8);

// =========================================================
// SLIDE 9 — MODULE IA
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Résultats · Module IA", "Génération orientée & scoring assisté");
const pipe=["Paramètres IA\n(curseurs −3…+3)","build_ctx\n+ format_msg","LLM Backend\nOpenAI / Ollama","Filtrage\ndoublons","Validation\nhumaine"];
pipe.forEach((t,i)=>{
  const x=0.75+i*2.46;
  s.addShape(RR, { x, y:1.95, w:2.18, h:1.0, fill:{color:i===4?TEAL:ROYAL}, line:{type:"none"}, rectRadius:0.08 });
  s.addText(t, { x, y:1.95, w:2.18, h:1.0, fontFace:BF, fontSize:11.5, bold:true, color:WHITE, align:"center", valign:"middle" });
  if(i<4) s.addText("›", { x:x+2.15, y:2.18, w:0.34, h:0.5, fontFace:HF, fontSize:24, bold:true, color:LBLUE, align:"center" });
});
s.addText("Human-in-the-loop : aucune réponse IA n'entre dans un scénario sans validation de l'auteur.", { x:0.75, y:3.1, w:12, h:0.4, fontFace:BF, fontSize:13, italic:true, color:NAVY });
const fc=[
  ["Génération orientée","L'auteur fixe une cible sur les 7 dimensions. Le LLM propose des réponses cohérentes avec la branche + une justification.", ROYAL],
  ["Scoring assisté","Sur une réponse existante, le LLM propose un vecteur de scores sur 7 dimensions, avec une justification explicable.", TEAL],
];
fc.forEach((c,i)=>{
  const x=0.75+i*6.2;
  s.addShape(RR, { x, y:3.7, w:5.8, h:1.75, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.1 });
  iconCircle(s, x+0.3, y_2=3.95, 0.5, c[2], "+");
  s.addText(c[0], { x:x+0.95, y:3.92, w:4.6, h:0.5, fontFace:HF, fontSize:17, bold:true, color:NAVY });
  s.addText(c[1], { x:x+0.35, y:4.5, w:5.2, h:0.9, fontFace:BF, fontSize:12.5, color:INK, lineSpacingMultiple:1.15 });
});
var y_2;
s.addShape(RR, { x:0.75, y:5.7, w:11.9, h:1.05, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Pattern Strategy", { x:1.05, y:5.85, w:2.6, h:0.4, fontFace:HF, fontSize:15, bold:true, color:LBLUE });
s.addText("Backend choisi par variable d'environnement — OpenAI (qualité/rapidité) ou Ollama (local, RGPD) — sans modifier le code applicatif.", { x:1.05, y:6.22, w:11.4, h:0.45, fontFace:BF, fontSize:13, color:PALE });
pageNum(s,9);

// =========================================================
// SLIDE 10 — GÉNÉRATION DE RÉPONSES (détail)
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Ma contribution · Module IA", "Génération de nouvelles réponses avec l'IA");
// ① l'auteur oriente — 2x2 chips
s.addText("① L'AUTEUR ORIENTE LA GÉNÉRATION", { x:0.75, y:1.85, w:6.9, h:0.3, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:1 });
const gin=[
  "Interaction courante & interaction cible (NextInteractionID)",
  "7 curseurs soft skills · échelle −3 … +3",
  "Consigne libre (ton, objectif) — optionnelle",
  "Contexte narratif injecté auto (scène, personnage, réponses)",
];
gin.forEach((t,i)=>{
  const x=0.75+(i%2)*3.55, y=2.2+Math.floor(i/2)*0.92;
  s.addShape(RR, { x, y, w:3.35, h:0.82, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.08 });
  cross(s, x+0.16, y+0.31, 0.2, ROYAL);
  s.addText(t, { x:x+0.45, y:y+0.04, w:2.78, h:0.74, fontFace:BF, fontSize:10.8, color:INK, valign:"middle", lineSpacingMultiple:1.0 });
});
// ② pipeline
s.addText("② PIPELINE DE GÉNÉRATION", { x:0.75, y:4.18, w:6.9, h:0.3, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:1 });
const gp=["build_ctx","format_msg\n(system + user)","LLM backend","filtrage\ndoublons"];
gp.forEach((t,i)=>{
  const x=0.75+i*1.72;
  s.addShape(RR, { x, y:4.55, w:1.5, h:0.95, fill:{color:ROYAL}, line:{type:"none"}, rectRadius:0.08 });
  s.addText(t, { x, y:4.55, w:1.5, h:0.95, fontFace:BF, fontSize:10.5, bold:true, color:WHITE, align:"center", valign:"middle" });
  if(i<3) s.addText("›", { x:x+1.48, y:4.7, w:0.26, h:0.5, fontFace:HF, fontSize:20, bold:true, color:LBLUE, align:"center" });
});
// right: example proposition card
s.addShape(RR, { x:8.0, y:1.85, w:4.6, h:3.95, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.14 });
s.addText("PROPOSITION GÉNÉRÉE", { x:8.3, y:2.05, w:4.0, h:0.3, fontFace:BF, fontSize:11.5, bold:true, color:LBLUE, charSpacing:1 });
s.addText("« Je prends un instant pour m'assurer qu'Agathe est prête avant de l'interrompre. »", { x:8.3, y:2.4, w:4.0, h:1.0, fontFace:HF, fontSize:13.5, italic:true, color:WHITE, lineSpacingMultiple:1.05 });
s.addShape(RR, { x:8.3, y:3.5, w:1.55, h:0.4, fill:{color:TEAL}, line:{type:"none"}, rectRadius:0.2 });
s.addText("Exemplaire", { x:8.3, y:3.5, w:1.55, h:0.4, fontFace:BF, fontSize:11, bold:true, color:WHITE, align:"center", valign:"middle" });
s.addText("Empathie +3 · Respect +2 · Compassion +2 · Clarté +1", { x:8.3, y:4.05, w:4.0, h:0.5, fontFace:BF, fontSize:11.5, bold:true, color:PALE, lineSpacingMultiple:1.05 });
s.addText([{text:"Justification : ",options:{bold:true,color:LBLUE}},{text:"l'infirmière se synchronise au rythme de la patiente sans s'imposer.",options:{color:PALE}}], { x:8.3, y:4.6, w:4.0, h:1.05, fontFace:BF, fontSize:11.5, lineSpacingMultiple:1.12 });
// bottom strip
s.addShape(RR, { x:0.75, y:5.95, w:11.85, h:0.75, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.1 });
cross(s, 1.0, 6.18, 0.28, ROYAL);
s.addText("Human-in-the-loop : chaque proposition est relue puis acceptée ou rejetée — aucune insertion automatique dans le scénario.", { x:1.5, y:5.98, w:10.9, h:0.7, fontFace:BF, fontSize:12.5, bold:true, color:NAVY, valign:"middle" });
pageNum(s,10);

// =========================================================
// SLIDE 11 — SCORING ASSISTÉ (détail)
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Ma contribution · Module IA", "Scoring assisté d'une réponse");
// left: entrée + traitement
s.addText("① ENTRÉE", { x:0.75, y:1.9, w:5.0, h:0.3, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:1 });
s.addShape(RR, { x:0.75, y:2.25, w:4.95, h:0.85, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.08 });
s.addText("Le texte d'une réponse (existante ou proposée) + son contexte narratif (scène, personnage).", { x:1.0, y:2.3, w:4.55, h:0.75, fontFace:BF, fontSize:12, color:INK, valign:"middle", lineSpacingMultiple:1.05 });
s.addText("② L'IA ÉVALUE", { x:0.75, y:3.35, w:5.0, h:0.3, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:1 });
["Construction du prompt (réponse + contexte)","Appel LLM (OpenAI / Ollama)","Sortie JSON : 7 scores + justification"].forEach((t,i)=>{
  const y=3.7+i*0.66;
  s.addShape(RR, { x:0.75, y, w:4.95, h:0.55, fill:{color:ROYAL}, line:{type:"none"}, rectRadius:0.08 });
  s.addText((i+1)+".  "+t, { x:1.0, y, w:4.6, h:0.55, fontFace:BF, fontSize:11.5, bold:true, color:WHITE, valign:"middle" });
});
s.addText("Échelle −3 (problématique) … +3 (exemplaire)", { x:0.75, y:5.78, w:4.95, h:0.3, fontFace:BF, fontSize:11, italic:true, color:MUTE });
// right: vecteur de scores
s.addShape(RR, { x:6.0, y:1.9, w:6.6, h:4.3, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.14 });
s.addText("VECTEUR DE SCORES PROPOSÉ", { x:6.3, y:2.05, w:6.0, h:0.3, fontFace:BF, fontSize:11.5, bold:true, color:TEAL, charSpacing:1 });
const sc=[["Respect & dignité",2],["Empathie",3],["Compassion",2],["Régulation émotionnelle",1],["Clarté de communication",2],["Frontières professionnelles",1],["Collaboration interpro.",0]];
const scoreColor=v=> v>=2?TEAL : v===1?ROYAL : v===0?MUTE : "D9646B";
sc.forEach((d,i)=>{
  const y=2.5+i*0.4;
  s.addText(d[0], { x:6.3, y, w:3.6, h:0.36, fontFace:BF, fontSize:11.5, color:INK, valign:"middle" });
  // mini scale track
  s.addShape(RR, { x:10.0, y:y+0.12, w:1.7, h:0.12, fill:{color:"CBD8EE"}, line:{type:"none"}, rectRadius:0.06 });
  const frac=(d[1]+3)/6; // 0..1
  s.addShape(EL, { x:10.0+frac*1.7-0.09, y:y+0.04, w:0.28, h:0.28, fill:{color:scoreColor(d[1])}, line:{type:"none"} });
  s.addText((d[1]>0?"+":"")+d[1], { x:11.85, y, w:0.55, h:0.36, fontFace:HF, fontSize:13, bold:true, color:scoreColor(d[1]), valign:"middle" });
});
s.addShape(RR, { x:6.3, y:5.4, w:6.0, h:0.7, fill:{color:WHITE}, line:{color:LBLUE,width:1}, rectRadius:0.08 });
s.addText([{text:"Justification : ",options:{bold:true,color:NAVY}},{text:"reconnaît l'état émotionnel d'Agathe et adapte son approche ; frontières implicites → score modéré.",options:{color:INK}}], { x:6.5, y:5.45, w:5.6, h:0.6, fontFace:BF, fontSize:11, valign:"middle", lineSpacingMultiple:1.05 });
s.addText("L'auteur accepte, corrige ou rejette le score · cohérence mesurée : MAE 0,77 vs scores humains.", { x:0.75, y:6.45, w:11.8, h:0.35, fontFace:BF, fontSize:12.5, italic:true, bold:true, color:ROYAL });
pageNum(s,11);

// =========================================================
// SLIDE 12 — DÉMO LIVE (navy divider)
// =========================================================
s = newSlide(); s.background={color:NAVY};
s.addShape(RR, { x:0.16, y:0.16, w:13.01, h:7.18, fill:{type:"none"}, line:{color:LBLUE,width:1.5}, rectRadius:0.12 });
s.addShape(EL, { x:-1.8, y:-1.8, w:3.6, h:3.6, fill:{color:ROYAL}, line:{type:"none"} });
s.addShape(EL, { x:-1.0, y:-1.0, w:2.0, h:2.0, fill:{color:LBLUE}, line:{type:"none"} });
s.addShape(EL, { x:11.9, y:5.5, w:3.0, h:3.0, fill:{color:ROYAL}, line:{type:"none"} });
cross(s, 12.0, 1.0, 0.42, LBLUE); cross(s, 1.0, 5.9, 0.34, LBLUE); cross(s, 10.6, 6.0, 0.28, LBLUE);
// play icon in circle
s.addShape(EL, { x:6.07, y:1.5, w:1.2, h:1.2, fill:{color:LBLUE}, line:{type:"none"} });
s.addShape(p.ShapeType.triangle, { x:6.5, y:1.86, w:0.46, h:0.48, fill:{color:NAVY}, line:{type:"none"}, rotate:90 });
s.addText("DÉMONSTRATION", { x:0.9, y:2.95, w:11.5, h:0.4, fontFace:BF, fontSize:14, color:LBLUE, bold:true, charSpacing:4, align:"center" });
s.addText("Démo live de la plateforme", { x:0.9, y:3.35, w:11.5, h:0.9, fontFace:HF, fontSize:40, color:WHITE, bold:true, align:"center" });
s.addText("Édition d'un scénario en graphe  ·  génération IA orientée  ·  scoring assisté  ·  mode parcours joueur", { x:1.4, y:4.35, w:10.5, h:0.5, fontFace:BF, fontSize:16, italic:true, color:PALE, align:"center" });
const demoChips=["1.  Charger un livre & explorer le graphe","2.  Éditer une réponse + curseurs soft skills","3.  Générer avec l'IA & valider","4.  Tester en mode parcours joueur"];
demoChips.forEach((t,i)=>{
  const x=0.9+i*3.0;
  s.addShape(RR, { x, y:5.35, w:2.75, h:0.95, fill:{color:"0A2A66"}, line:{color:ROYAL,width:1}, rectRadius:0.1 });
  s.addText(t, { x:x+0.15, y:5.4, w:2.45, h:0.85, fontFace:BF, fontSize:12, bold:true, color:WHITE, align:"center", valign:"middle" });
});
s.addText("Plan B si pas de live : captures d'écran de secours intégrées.", { x:0.9, y:6.5, w:11.5, h:0.35, fontFace:BF, fontSize:11.5, italic:true, color:LBLUE, align:"center" });

// =========================================================
// SLIDE 11 — GÉNÉRATION (navy big numbers)
// =========================================================
s = newSlide(); s.background={color:NAVY};
s.addShape(RR, { x:0.16, y:0.16, w:13.01, h:7.18, fill:{type:"none"}, line:{color:LBLUE,width:1.5}, rectRadius:0.12 });
s.addShape(EL, { x:11.8, y:5.4, w:3.0, h:3.0, fill:{color:ROYAL}, line:{type:"none"} });
s.addShape(EL, { x:-1.5, y:-1.5, w:3.0, h:3.0, fill:{color:ROYAL}, line:{type:"none"} });
cross(s, 12.2, 0.9, 0.4, LBLUE); cross(s, 0.8, 5.9, 0.3, LBLUE);
s.addText("RÉSULTATS · ÉVALUATION IA", { x:0.9, y:0.7, w:11, h:0.35, fontFace:BF, fontSize:13, color:LBLUE, bold:true, charSpacing:3 });
s.addText("Génération orientée : 100 % de conformité", { x:0.9, y:1.05, w:11.5, h:0.7, fontFace:HF, fontSize:28, color:WHITE, bold:true });
const st=[["100 %","Conformité ±1 aux scores cibles"],["50 / 50","Générations réussies (0 erreur LLM)"],["4,6 s","Temps moyen par génération"]];
st.forEach((v,i)=>{
  const x=0.9+i*3.95;
  cross(s, x+0.05, 2.55, 0.5, LBLUE);
  s.addText(v[0], { x, y:3.05, w:3.6, h:1.0, fontFace:HF, fontSize:50, bold:true, color:WHITE });
  s.addText(v[1], { x:x+0.05, y:4.15, w:3.5, h:0.8, fontFace:BF, fontSize:14, color:PALE, lineSpacingMultiple:1.05 });
});
s.addShape(RR, { x:0.9, y:5.35, w:11.55, h:1.4, fill:{color:"0A2A66"}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Protocole : 50 générations · 10 interactions × 5 profils pédagogiques (OpenAI gpt-4.1-mini). Les profils « problématiques » produisent des formulations froides ; les « exemplaires », des réponses attentives. La validation humaine reste indispensable.", { x:1.2, y:5.5, w:11.0, h:1.1, fontFace:BF, fontSize:13.5, color:PALE, lineSpacingMultiple:1.2 });

// =========================================================
// SLIDE 11 — SCORING MAE
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Résultats · Évaluation IA", "Scoring assisté : MAE de 0,77 / 7 niveaux");
const mae=[["Collaboration interpro.",0.13],["Régulation émotionnelle",0.60],["Respect & dignité",0.67],["Clarté communication",0.73],["Frontières pro.",0.87],["Compassion",1.07],["Empathie",1.33]];
const cx=0.8, cy=2.0, rowH=0.6, maxV=1.4;
mae.forEach((m,i)=>{
  const y=cy+i*rowH;
  s.addText(m[0], { x:cx, y, w:2.85, h:rowH-0.1, fontFace:BF, fontSize:12.5, color:INK, align:"right", valign:"middle" });
  const bw=(m[1]/maxV)*4.2;
  const col=m[1]<0.7?TEAL:m[1]<1.0?ROYAL:LBLUE;
  s.addShape(RR, { x:cx+3.0, y:y+0.09, w:Math.max(bw,0.12), h:rowH-0.28, fill:{color:col}, line:{type:"none"}, rectRadius:0.03 });
  s.addText(m[1].toFixed(2), { x:cx+3.05+Math.max(bw,0.12), y:y+0.02, w:0.8, h:rowH-0.1, fontFace:HF, fontSize:12.5, bold:true, color:NAVY, valign:"middle" });
});
s.addShape(RR, { x:9.0, y:2.0, w:3.65, h:4.35, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.14 });
s.addText("0,77", { x:9.0, y:2.25, w:3.65, h:0.95, fontFace:HF, fontSize:52, bold:true, color:ROYAL, align:"center" });
s.addText("MAE globale (échelle −3 → +3)", { x:9.1, y:3.2, w:3.45, h:0.35, fontFace:BF, fontSize:12, color:INK, align:"center" });
s.addText([{text:"Mieux prédites : ",options:{bold:true,color:NAVY}},{text:"dimensions explicites (collaboration, régulation).",options:{color:INK}}], { x:9.25, y:3.7, w:3.25, h:1.0, fontFace:BF, fontSize:12.5, lineSpacingMultiple:1.15 });
s.addText([{text:"Plus difficiles : ",options:{bold:true,color:TEAL}},{text:"empathie & compassion — subjectives et souvent superposées.",options:{color:INK}}], { x:9.25, y:4.85, w:3.25, h:1.4, fontFace:BF, fontSize:12.5, lineSpacingMultiple:1.15 });
s.addText("Aide à l'évaluation — supervision humaine requise.", { x:0.8, y:6.4, w:8.0, h:0.4, fontFace:BF, fontSize:13, italic:true, bold:true, color:ROYAL });
pageNum(s,14);

// =========================================================
// SLIDE 12 — BACKENDS & VALIDATION
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Résultats · Backends & validation", "OpenAI vs Ollama — un compromis assumé");
const rows=[["Critère","OpenAI","Ollama"],["JSON valide","10 / 10","10 / 10"],["Conformité ±1","100 %","91,3 %"],["Temps moyen","9,2 s","98,2 s"],["Exécution locale","Non","Oui (RGPD)"]];
const tx=0.8, ty=2.0, cw=[2.6,1.8,1.8], rh=0.62;
rows.forEach((r,i)=>{
  let x=tx;
  r.forEach((cell,j)=>{
    const isH=i===0;
    s.addShape(RC, { x, y:ty+i*rh, w:cw[j], h:rh, fill:{color: isH?NAVY:(i%2?WHITE:PALE)}, line:{color:WHITE,width:1.5} });
    const hl=(j===1&&!isH&&(i===2||i===3))||(j===2&&i===4);
    s.addText(cell, { x:x+0.1, y:ty+i*rh, w:cw[j]-0.2, h:rh, fontFace: isH||j===0?HF:BF, fontSize:13.5, bold:isH||j===0, color: isH?WHITE:(hl?ROYAL:INK), align:j===0?"left":"center", valign:"middle" });
    x+=cw[j];
  });
});
s.addText("OpenAI : qualité & rapidité.  Ollama : confidentialité (données sur la machine du formateur).", { x:0.8, y:5.45, w:6.5, h:0.8, fontFace:BF, fontSize:13, italic:true, color:INK, lineSpacingMultiple:1.15 });
s.addShape(RR, { x:7.75, y:2.0, w:4.9, h:4.3, fill:{color:PALE}, line:{type:"none"}, rectRadius:0.14 });
s.addText("VALIDATION TECHNIQUE", { x:8.05, y:2.25, w:4.4, h:0.35, fontFace:BF, fontSize:12, bold:true, color:TEAL, charSpacing:2 });
const tv=[["27","tests pytest — 100 % de réussite"],["2","livres pédagogiques pris en charge"],["438","interactions · 1 232 arêtes"]];
tv.forEach((t,i)=>{
  const y=2.75+i*1.1;
  s.addText(t[0], { x:8.05, y, w:1.55, h:0.8, fontFace:HF, fontSize:36, bold:true, color:ROYAL });
  s.addText(t[1], { x:9.65, y:y+0.12, w:2.85, h:0.65, fontFace:BF, fontSize:13, color:INK, valign:"middle" });
});
s.addText("Round-trip JSON & écriture atomique validés sur les fichiers réels.", { x:8.05, y:5.95, w:4.4, h:0.35, fontFace:BF, fontSize:11, italic:true, color:MUTE });
pageNum(s,15);

// =========================================================
// SLIDE 13 — DISCUSSION
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Discussion", "Portée, limites et garde-fous éthiques");
const disc=[
  ["Conformité à interpréter avec prudence","Respecter un score ≠ porter l'intention narrative. Le ton, les silences, le non-verbal échappent à l'analyse textuelle.", ROYAL],
  ["Référence de scoring fragile","Scores humains fixés par un seul annotateur sur 15 réponses. Un accord inter-annotateurs (kappa) consoliderait le gold standard.", LBLUE],
  ["Pas encore de test utilisateur","L'ergonomie reste à mesurer avec des formateurs et cliniciens du CHUV (SUS / PSSUQ).", TEAL],
];
disc.forEach((d,i)=>{
  const y=1.95+i*1.48;
  s.addShape(RR, { x:0.7, y, w:7.55, h:1.32, fill:{color: i===1?PALE:WHITE}, line:{color:LBLUE,width:1.1}, rectRadius:0.1 });
  iconCircle(s, 0.95, y+0.32, 0.62, d[2], "+");
  s.addText(d[0], { x:1.8, y:y+0.16, w:6.3, h:0.42, fontFace:HF, fontSize:15.5, bold:true, color:NAVY });
  s.addText(d[1], { x:1.8, y:y+0.56, w:6.35, h:0.72, fontFace:BF, fontSize:12.5, color:INK, lineSpacingMultiple:1.12 });
});
s.addShape(RR, { x:8.5, y:1.95, w:4.2, h:4.45, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.14 });
cross(s, 11.9, 2.2, 0.4, LBLUE);
s.addText("ÉTHIQUE", { x:8.8, y:2.3, w:3.6, h:0.35, fontFace:BF, fontSize:12, bold:true, color:LBLUE, charSpacing:2 });
s.addText("Le human-in-the-loop est essentiel", { x:8.8, y:2.7, w:3.6, h:0.95, fontFace:HF, fontSize:20, bold:true, color:WHITE, lineSpacingMultiple:1.0 });
s.addText("Les scénarios touchent au deuil et à la détresse. Aucune proposition IA n'est intégrée automatiquement.\n\nL'IA propose réponses, scores et justifications — la responsabilité finale reste au formateur clinique.", { x:8.8, y:3.8, w:3.6, h:2.5, fontFace:BF, fontSize:13, color:PALE, lineSpacingMultiple:1.2 });
pageNum(s,16);

// =========================================================
// SLIDE 14 — CONCLUSION (navy)
// =========================================================
s = newSlide(); s.background={color:NAVY};
s.addShape(RR, { x:0.16, y:0.16, w:13.01, h:7.18, fill:{type:"none"}, line:{color:LBLUE,width:1.5}, rectRadius:0.12 });
s.addShape(EL, { x:-1.6, y:-1.6, w:3.2, h:3.2, fill:{color:ROYAL}, line:{type:"none"} });
s.addShape(EL, { x:12.0, y:5.6, w:2.8, h:2.8, fill:{color:ROYAL}, line:{type:"none"} });
cross(s, 12.3, 1.0, 0.4, LBLUE); cross(s, 0.8, 6.0, 0.3, LBLUE);
s.addText("CONCLUSION", { x:0.9, y:0.7, w:11, h:0.4, fontFace:BF, fontSize:13, color:LBLUE, bold:true, charSpacing:3 });
s.addText("Un jeu sérieux devenu plateforme intelligente et maintenable", { x:0.9, y:1.05, w:11.5, h:1.1, fontFace:HF, fontSize:27, color:WHITE, bold:true, lineSpacingMultiple:1.0 });
const cc=[
  ["Interface en graphe","Édition CRUD, validation EG-7, parcours joueur. 438 interactions, 1 232 arêtes. Round-trip Unity exact à 100 %.", LBLUE],
  ["Module IA explicable","100 % de conformité (OpenAI), MAE 0,77, justifications textuelles, double backend cloud/local RGPD.", TEAL],
  ["Architecture durable","Clean Architecture, modèles purs, 27 tests. Ajouter un livre = 2 étapes (JSON + books.py).", LBLUE],
];
cc.forEach((c,i)=>{
  const x=0.9+i*4.05;
  s.addShape(RR, { x, y:2.85, w:3.8, h:3.5, fill:{color:"0A2A66"}, line:{type:"none"}, rectRadius:0.12 });
  iconCircle(s, x+0.35, y3=3.15, 0.7, c[2], String(i+1), NAVY);
  s.addText(c[0], { x:x+0.35, y:4.0, w:3.15, h:0.8, fontFace:HF, fontSize:17, bold:true, color:WHITE });
  s.addText(c[1], { x:x+0.35, y:4.8, w:3.2, h:1.5, fontFace:BF, fontSize:12.5, color:PALE, lineSpacingMultiple:1.18 });
});
var y3;
s.addText("Objectifs atteints — exigences EG-1 à EG-7 et CT-1 à CT-3 du cahier des charges satisfaites.", { x:0.9, y:6.55, w:11.5, h:0.4, fontFace:BF, fontSize:13.5, italic:true, color:LBLUE });

// =========================================================
// SLIDE 15 — PERSPECTIVES
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s); corners(s,2);
header(s, "Perspectives", "Vers un tuteur intelligent");
const pp=[
  ["Court terme","Test d'utilisabilité (SUS/PSSUQ) · scoring en lot exportable · accord inter-annotateurs.", ROYAL],
  ["Scoring dynamique côté joueur","Le LLM analyse les réponses de l'apprenant en temps réel pendant la simulation → feedback formatif.", LBLUE],
  ["Fine-tuning spécialisé","Modèle entraîné sur des réponses annotées par les experts CHUV, déployé via Ollama (perf + RGPD).", TEAL],
  ["Extension & immersion","Autres contextes critiques (oncologie, urgences, gériatrie) · expressions MetaHuman pilotées par l'IA.", ROYAL],
];
pp.forEach((d,i)=>{
  const col=i%2,row=Math.floor(i/2);
  const x=0.7+col*6.2,y=1.95+row*2.15;
  s.addShape(RR, { x, y, w:5.8, h:1.9, fill:{color: row+col?WHITE:PALE}, line:{color:LBLUE,width:1.1}, rectRadius:0.12 });
  iconCircle(s, x+0.35, y+0.32, 0.62, d[2], "+");
  s.addText(d[0], { x:x+1.2, y:y+0.28, w:4.4, h:0.5, fontFace:HF, fontSize:16, bold:true, color:NAVY });
  s.addText(d[1], { x:x+1.2, y:y+0.78, w:4.45, h:1.0, fontFace:BF, fontSize:13, color:INK, lineSpacingMultiple:1.15 });
});
pageNum(s,18);

// =========================================================
// SLIDE 16 — MERCI
// =========================================================
s = newSlide(); s.background={color:WHITE}; frame(s);
s.addShape(EL, { x:-2.0, y:-2.0, w:4.2, h:4.2, fill:{color:PALE}, line:{type:"none"} });
s.addShape(EL, { x:-1.1, y:-1.1, w:2.4, h:2.4, fill:{color:LBLUE}, line:{type:"none"} });
s.addShape(EL, { x:11.7, y:5.4, w:3.1, h:3.1, fill:{color:ROYAL}, line:{type:"none"} });
cross(s, 11.2, 1.2, 0.42, LBLUE); cross(s, 1.3, 5.6, 0.34, LBLUE); cross(s, 10.0, 5.9, 0.28, PALE);
iconCircle(s, 6.17, 2.0, 1.0, ROYAL, "+");
s.addText("Merci de votre attention", { x:1.5, y:3.25, w:10.3, h:0.9, fontFace:HF, fontSize:42, bold:true, color:NAVY, align:"center" });
s.addText("Questions & discussion", { x:1.5, y:4.25, w:10.3, h:0.6, fontFace:BF, fontSize:20, italic:true, color:ROYAL, align:"center" });
dots(s, 6.13, 5.15, 5, TEAL, 2);
s.addText("Thomas Maksimous · MSE HES-SO · CHUV · UniL · Nº 2026-01", { x:1.5, y:5.6, w:10.3, h:0.4, fontFace:BF, fontSize:13, color:MUTE, align:"center" });

// ---------- speaker notes ----------
const NOTES = require("./notes.js");
_slides.forEach((sl,i)=>{ if(NOTES[i]) sl.addNotes(NOTES[i]); });

p.writeFile({ fileName: "/Users/thomaks/DEV/PA_26_EOL/output/PA_2026_EOL_presentation.pptx" }).then(f=> console.log("Saved:", f));
