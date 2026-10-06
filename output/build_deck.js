const pptxgen = require("pptxgenjs");
const p = new pptxgen();

p.defineLayout({ name: "W", width: 13.333, height: 7.5 });
p.layout = "W";

const _slides = [];
function newSlide(){ const sl = p.addSlide(); _slides.push(sl); return sl; }

// ---- Palette (Ocean / medical-tech, calm & serious) ----
const NAVY = "10243B";   // deep background
const DEEP = "0E4D6E";   // deep teal-blue
const TEAL = "1C7293";   // teal
const SEA  = "2A9D8F";   // accent seafoam-green
const AMBER = "E9A23B";  // warm accent
const ICE  = "CFE3EF";   // light blue text
const CLOUD = "F4F8FB";  // light background
const SLATE = "33505F";  // body text on light
const MUTE = "6E8794";   // muted

const HFONT = "Georgia";
const BFONT = "Calibri";

const W = 13.333, H = 7.5;

function darkBg(s){ s.background = { color: NAVY }; }
function lightBg(s){ s.background = { color: CLOUD }; }

// kicker + title block for content slides
function header(s, kicker, title){
  s.addText(kicker.toUpperCase(), { x:0.6, y:0.42, w:12, h:0.3, fontFace:BFONT, fontSize:12, color:TEAL, bold:true, charSpacing:2 });
  s.addText(title, { x:0.6, y:0.72, w:12.1, h:0.85, fontFace:HFONT, fontSize:30, color:NAVY, bold:true });
}

function pageNum(s, n){
  s.addText(String(n), { x:12.5, y:6.95, w:0.6, h:0.35, fontFace:BFONT, fontSize:11, color:MUTE, align:"right" });
}

// small icon-circle bullet card
function card(s, x, y, w, h, fill){
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, fill:{ color:fill }, line:{ type:"none" }, rectRadius:0.1, shadow:{ type:"outer", color:"888888", opacity:0.25, blur:6, offset:2, angle:90 } });
}

// =========================================================
// SLIDE 1 — TITLE
// =========================================================
let s = newSlide(); darkBg(s);
// decorative arcs / nodes motif (graph theme)
s.addShape(p.ShapeType.ellipse, { x:10.4, y:-1.6, w:5.2, h:5.2, fill:{ color:DEEP }, line:{type:"none"} });
s.addShape(p.ShapeType.ellipse, { x:11.7, y:4.6, w:3.6, h:3.6, fill:{ color:TEAL }, line:{type:"none"} });
// graph node dots
const dots = [[10.9,1.2,SEA],[11.9,2.1,ICE],[10.4,2.6,AMBER],[12.4,1.0,ICE]];
dots.forEach(([x,y,c])=> s.addShape(p.ShapeType.ellipse,{x,y,w:0.18,h:0.18,fill:{color:c},line:{type:"none"}}));

s.addText("ADVANCED PROJECT (PA) · MSE HES-SO · Nº 2026-01", { x:0.7, y:0.7, w:10, h:0.4, fontFace:BFONT, fontSize:13, color:SEA, bold:true, charSpacing:2 });

s.addText("Interactive Book for Medical Staff\ndealing with End-of-life Patients", { x:0.7, y:1.9, w:10.6, h:1.7, fontFace:HFONT, fontSize:40, color:"FFFFFF", bold:true, lineSpacingMultiple:1.0 });
s.addText("Storytelling & soft-skills consistencies using AI", { x:0.72, y:3.55, w:10, h:0.6, fontFace:BFONT, fontSize:20, color:ICE, italic:true });

s.addShape(p.ShapeType.line, { x:0.75, y:4.5, w:4.2, h:0, line:{ color:AMBER, width:2.5 } });

s.addText([
  { text:"Thomas Maksimous", options:{ bold:true, color:"FFFFFF", fontSize:18, breakLine:true } },
  { text:"Superviseur — Prof. Stéphane Gobron (HES-SO)", options:{ color:ICE, fontSize:14, breakLine:true } },
  { text:"Experte — Dre Claudia Gamondi, MD (CHUV, soins palliatifs)", options:{ color:ICE, fontSize:14, breakLine:true } },
], { x:0.72, y:4.75, w:11, h:1.5, fontFace:BFONT, lineSpacingMultiple:1.25 });

s.addText("HES-SO Master · CHUV · UniL   |   Lausanne, juin 2026", { x:0.72, y:6.6, w:11, h:0.4, fontFace:BFONT, fontSize:13, color:MUTE });

// =========================================================
// SLIDE 2 — CONTEXTE & PROBLÉMATIQUE
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Contexte", "Former à la communication en fin de vie");
const ctx = [
  ["Un défi humain", "Au-delà du clinique, les soignants doivent mobiliser empathie, respect et compassion face au deuil et à la détresse."],
  ["Méthode actuelle", "Jeux de rôle en petits groupes : efficaces, mais chronophages, coûteux en formateurs et difficiles à mettre à l'échelle."],
  ["Le serious game « End of Life »", "Simulation 3D développée à la HES-SO avec le CHUV — base de ce projet."],
];
ctx.forEach((c,i)=>{
  const y = 1.9 + i*1.55;
  card(s, 0.6, y, 7.4, 1.35, "FFFFFF");
  s.addShape(p.ShapeType.roundRect,{ x:0.6, y, w:0.12, h:1.35, fill:{color:[TEAL,SEA,AMBER][i]}, line:{type:"none"}, rectRadius:0.05 });
  s.addText(c[0], { x:0.95, y:y+0.15, w:6.9, h:0.4, fontFace:BFONT, fontSize:16, bold:true, color:NAVY });
  s.addText(c[1], { x:0.95, y:y+0.55, w:6.9, h:0.7, fontFace:BFONT, fontSize:13, color:SLATE });
});
// right callout panel
s.addShape(p.ShapeType.roundRect,{ x:8.35, y:1.9, w:4.35, h:4.55, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.12 });
s.addText("Le constat", { x:8.7, y:2.15, w:3.7, h:0.4, fontFace:BFONT, fontSize:14, bold:true, color:SEA });
s.addText("« Que signifie soigner lorsque guérir n'est plus l'objectif ? »", { x:8.7, y:2.6, w:3.75, h:1.3, fontFace:HFONT, fontSize:20, italic:true, color:"FFFFFF", lineSpacingMultiple:1.05 });
s.addText("La fin de vie expose à des situations sans réponse unique : un cadre d'apprentissage immersif et sécurisé est nécessaire avant l'exposition réelle.", { x:8.7, y:4.2, w:3.75, h:1.8, fontFace:BFONT, fontSize:13, color:ICE, lineSpacingMultiple:1.2 });
pageNum(s,2);

// =========================================================
// SLIDE 3 — LES DEUX VERROUS
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Problématique", "Deux verrous de l'application existante");
const locks = [
  ["01", "Contenu figé & inaccessible", "Les scénarios sont stockés dans des fichiers JSON statiques (Chapters.json). Impossible pour un médecin ou un formateur non-informaticien de les modifier.", TEAL],
  ["02", "Évaluation superficielle", "Le scoring était limité à 3 axes fixes (empathie, respect, compassion), sans analyse sémantique des choix de l'apprenant.", AMBER],
];
locks.forEach((l,i)=>{
  const x = 0.6 + i*6.25;
  card(s, x, 2.05, 5.85, 3.9, "FFFFFF");
  s.addShape(p.ShapeType.ellipse,{ x:x+0.4, y:2.45, w:1.0, h:1.0, fill:{color:l[3]}, line:{type:"none"} });
  s.addText(l[0], { x:x+0.4, y:2.6, w:1.0, h:0.7, fontFace:HFONT, fontSize:26, bold:true, color:"FFFFFF", align:"center" });
  s.addText(l[1], { x:x+0.4, y:3.7, w:5.05, h:0.6, fontFace:BFONT, fontSize:19, bold:true, color:NAVY });
  s.addText(l[2], { x:x+0.4, y:4.35, w:5.05, h:1.4, fontFace:BFONT, fontSize:14, color:SLATE, lineSpacingMultiple:1.2 });
});
s.addText("Besoin : doter l'outil d'une infrastructure flexible et d'une IA capable d'épauler créateurs de contenu et apprenants.", { x:0.6, y:6.3, w:12, h:0.5, fontFace:BFONT, fontSize:14, italic:true, color:DEEP, bold:true });
pageNum(s,3);

// =========================================================
// SLIDE 4 — OBJECTIFS
// =========================================================
s = newSlide(); darkBg(s);
s.addText("OBJECTIFS", { x:0.6, y:0.55, w:12, h:0.4, fontFace:BFONT, fontSize:13, color:SEA, bold:true, charSpacing:3 });
s.addText("Transformer un jeu sérieux en plateforme\nintelligente pilotée par les données", { x:0.6, y:0.95, w:12, h:1.4, fontFace:HFONT, fontSize:30, color:"FFFFFF", bold:true, lineSpacingMultiple:1.0 });

const obj = [
  ["Interface d'administration en graphe", "Un outil web visuel pour visualiser, créer, modifier et supprimer blocs narratifs et branches — sans compétence en programmation.", SEA],
  ["Intégration de l'Intelligence Artificielle", "Côté création : assister la génération de réponses orientées. Côté évaluation : un scoring sémantique explicable des choix de l'apprenant.", AMBER],
];
obj.forEach((o,i)=>{
  const x = 0.6 + i*6.25;
  s.addShape(p.ShapeType.roundRect,{ x, y:2.85, w:5.85, h:3.5, fill:{color:DEEP}, line:{type:"none"}, rectRadius:0.12 });
  s.addShape(p.ShapeType.roundRect,{ x, y:2.85, w:5.85, h:0.16, fill:{color:o[2]}, line:{type:"none"}, rectRadius:0.05 });
  s.addText(String(i+1), { x:x+0.35, y:3.2, w:1.0, h:1.0, fontFace:HFONT, fontSize:48, bold:true, color:o[2] });
  s.addText(o[0], { x:x+0.4, y:4.35, w:5.1, h:0.8, fontFace:BFONT, fontSize:20, bold:true, color:"FFFFFF" });
  s.addText(o[1], { x:x+0.4, y:5.15, w:5.1, h:1.1, fontFace:BFONT, fontSize:14, color:ICE, lineSpacingMultiple:1.2 });
});
s.addText("Fil conducteur : un design « human-in-the-loop » — l'IA assiste, l'humain valide.", { x:0.6, y:6.65, w:12, h:0.4, fontFace:BFONT, fontSize:14, italic:true, color:AMBER });
pageNum(s,4);

// =========================================================
// SLIDE 5 — ÉTAT DE L'ART
// =========================================================
s = newSlide(); lightBg(s);
header(s, "État de l'art", "Quatre axes convergent vers le projet");
const sota = [
  ["Apps pour soignants", "Aide à la décision, télémédecine, mindfulness anti burn-out — mais peu entraînent activement les soft skills.", TEAL],
  ["Serious games fin de vie", "Cadre LDR « Live, Die, Repeat » : 88 % des résidents plus confiants après simulation.", SEA],
  ["Livres dont on est le héros", "Récits à embranchements (Twine, CYOA) : chaque choix devient une arête d'un graphe narratif.", DEEP],
  ["Soft skills & profilage", "Cadres PERCS, échelles IRI / JSE ; évaluation comportementale par Machine Learning (Marengo).", AMBER],
];
sota.forEach((c,i)=>{
  const col = i%2, row = Math.floor(i/2);
  const x = 0.6 + col*6.25, y = 1.95 + row*2.2;
  card(s, x, y, 5.85, 1.95, "FFFFFF");
  s.addShape(p.ShapeType.ellipse,{ x:x+0.35, y:y+0.32, w:0.55, h:0.55, fill:{color:c[2]}, line:{type:"none"} });
  s.addText(String.fromCharCode(97+i), { x:x+0.35, y:y+0.37, w:0.55, h:0.45, fontFace:HFONT, fontSize:18, bold:true, color:"FFFFFF", align:"center" });
  s.addText(c[0], { x:x+1.1, y:y+0.28, w:4.6, h:0.5, fontFace:BFONT, fontSize:17, bold:true, color:NAVY });
  s.addText(c[1], { x:x+1.1, y:y+0.78, w:4.6, h:1.0, fontFace:BFONT, fontSize:13, color:SLATE, lineSpacingMultiple:1.15 });
});
s.addText("Lacune ciblée : un environnement narratif interactif pour entraîner — et évaluer — les compétences relationnelles.", { x:0.6, y:6.5, w:12, h:0.4, fontFace:BFONT, fontSize:14, italic:true, bold:true, color:DEEP });
pageNum(s,5);

// =========================================================
// SLIDE 6 — MODÈLE DE DONNÉES & GRAPHE
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Méthode · Modèle de données", "Du JSON hiérarchique au graphe orienté");
// hierarchy chain left
const chain = ["Chapter","Scene","Interaction","Response"];
chain.forEach((c,i)=>{
  const y = 2.0 + i*0.95;
  s.addShape(p.ShapeType.roundRect,{ x:0.7, y, w:2.7, h:0.65, fill:{color:[DEEP,TEAL,SEA,AMBER][i]}, line:{type:"none"}, rectRadius:0.08 });
  s.addText(c, { x:0.7, y, w:2.7, h:0.65, fontFace:BFONT, fontSize:16, bold:true, color:"FFFFFF", align:"center", valign:"middle" });
  if(i<3) s.addText("▼", { x:1.85, y:y+0.62, w:0.4, h:0.3, fontFace:BFONT, fontSize:12, color:MUTE, align:"center" });
});
s.addText("Compatibilité JSON conservée\n(moteur Unity / Naninovel)", { x:0.7, y:5.95, w:2.8, h:0.7, fontFace:BFONT, fontSize:12, italic:true, color:MUTE, align:"center" });

// transform arrow
s.addText("graph_service →", { x:3.7, y:3.5, w:1.5, h:0.4, fontFace:BFONT, fontSize:12, bold:true, color:TEAL, align:"center" });

// graph nodes right
const gx=6.2, gy=2.0;
const nodes={ I1:[gx+2.0,gy], I2:[gx,gy+1.15], I3:[gx+4.0,gy+1.15], I4:[gx+2.0,gy+2.3] };
const edges=[["I1","I2"],["I1","I3"],["I2","I4"],["I3","I4"]];
edges.forEach(([a,b])=>{
  s.addShape(p.ShapeType.line,{ x:nodes[a][0]+0.45, y:nodes[a][1]+0.45, w:nodes[b][0]-nodes[a][0], h:nodes[b][1]-nodes[a][1], line:{color:TEAL,width:2} });
});
Object.entries(nodes).forEach(([k,[x,y]])=>{
  s.addShape(p.ShapeType.ellipse,{ x, y, w:0.9, h:0.9, fill:{color:NAVY}, line:{color:SEA,width:2} });
  s.addText(k, { x, y, w:0.9, h:0.9, fontFace:BFONT, fontSize:15, bold:true, color:"FFFFFF", align:"center", valign:"middle" });
});
s.addText("Chaque Interaction = nœud · chaque Response = arête (NextInteractionID).  « -1 » = fin de branche.", { x:5.6, y:5.55, w:7.1, h:0.5, fontFace:BFONT, fontSize:12.5, color:SLATE, align:"center" });

// 7 dimensions strip
s.addShape(p.ShapeType.roundRect,{ x:5.6, y:6.15, w:7.1, h:0.75, fill:{color:CLOUD}, line:{color:AMBER,width:1.5}, rectRadius:0.08 });
s.addText("Scoring étendu : 3 → 7 dimensions soft skills, échelle −3 à +3", { x:5.7, y:6.18, w:6.9, h:0.32, fontFace:BFONT, fontSize:13, bold:true, color:DEEP, align:"center", valign:"middle" });
s.addText("Respect · Empathie · Compassion · Régulation émo. · Clarté · Frontières pro. · Collaboration", { x:5.7, y:6.5, w:6.9, h:0.32, fontFace:BFONT, fontSize:10.5, color:SLATE, align:"center", valign:"middle" });
pageNum(s,6);

// =========================================================
// SLIDE 7 — ARCHITECTURE
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Méthode · Architecture", "Clean Architecture en couches");
const layers = [
  ["Présentation","Views / Controllers — pages.py (Jinja) · api.py (REST)", DEEP],
  ["Application","Services — graph_service · validation_service · enrichment/", TEAL],
  ["Infrastructure","Repositories — ChapterRepository : lecture / écriture JSON", SEA],
  ["Domaine","Models métier purs — Chapter · Scene · Interaction · Response · Actor", "5C7D4F"],
];
layers.forEach((l,i)=>{
  const y = 1.95 + i*1.05;
  s.addShape(p.ShapeType.roundRect,{ x:0.7, y, w:7.7, h:0.9, fill:{color:l[2]}, line:{type:"none"}, rectRadius:0.08 });
  s.addText(l[0], { x:1.0, y:y+0.12, w:3, h:0.4, fontFace:BFONT, fontSize:17, bold:true, color:"FFFFFF" });
  s.addText(l[1], { x:1.0, y:y+0.5, w:7.1, h:0.35, fontFace:"Consolas", fontSize:12, color:"EAF3F7" });
});
s.addShape(p.ShapeType.roundRect,{ x:2.8, y:6.45, w:3.5, h:0.55, fill:{color:"FFFFFF"}, line:{color:MUTE,width:1.5,dashType:"dash"}, rectRadius:0.05 });
s.addText("JSON files (Unity)", { x:2.8, y:6.45, w:3.5, h:0.55, fontFace:BFONT, fontSize:13, bold:true, color:SLATE, align:"center", valign:"middle" });

// right benefits panel
s.addShape(p.ShapeType.roundRect,{ x:8.75, y:1.95, w:3.95, h:5.05, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.12 });
s.addText("Pourquoi ?", { x:9.05, y:2.2, w:3.4, h:0.4, fontFace:BFONT, fontSize:15, bold:true, color:SEA });
[
  "Modèles métier indépendants du web, de l'IA et de la persistance",
  "Composants remplaçables (ex. backend IA) sans toucher au domaine",
  "Stack : Python / Flask · Jinja2 · JS ES Modules · vis-network",
  "Code testable, maintenable et extensible au-delà du projet",
].forEach((t,i)=>{
  const y=2.7+i*1.0;
  s.addShape(p.ShapeType.ellipse,{ x:9.05, y:y+0.05, w:0.18, h:0.18, fill:{color:AMBER}, line:{type:"none"} });
  s.addText(t, { x:9.35, y, w:3.15, h:0.95, fontFace:BFONT, fontSize:13, color:ICE, lineSpacingMultiple:1.1 });
});
pageNum(s,7);

// =========================================================
// SLIDE 8 — INTERFACE D'ADMINISTRATION (résultat)
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Résultats · Plateforme", "Interface d'administration livrée");
// mock graph editor panel
s.addShape(p.ShapeType.roundRect,{ x:0.7, y:1.95, w:6.6, h:4.55, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Éditeur de graphe narratif", { x:0.95, y:2.15, w:6, h:0.4, fontFace:BFONT, fontSize:14, bold:true, color:SEA });
// fake nodes
const fn=[[1.4,3.0],[3.2,3.0],[5.1,3.0],[2.3,4.3],[4.2,4.3],[3.2,5.4]];
const fe=[[0,1],[1,2],[1,3],[1,4],[3,5],[4,5]];
fe.forEach(([a,b])=> s.addShape(p.ShapeType.line,{ x:fn[a][0]+0.35, y:fn[a][1]+0.18, w:fn[b][0]-fn[a][0], h:fn[b][1]-fn[a][1], line:{color:TEAL,width:1.5} }));
fn.forEach(([x,y],i)=> { s.addShape(p.ShapeType.roundRect,{ x, y, w:0.7, h:0.36, fill:{color:i===5?AMBER:DEEP}, line:{color:SEA,width:1}, rectRadius:0.05 }); });
s.addText("Liste des scènes · graphe central · panneau de propriétés", { x:0.95, y:5.95, w:6.1, h:0.4, fontFace:BFONT, fontSize:12, italic:true, color:ICE });

// features list right
const feat = [
  ["Édition CRUD complète","Textes, noms, scores et références narratives"],
  ["Validation EG-7 temps réel","Détecte les NextInteractionID invalides (branches cassées)"],
  ["Sauvegarde atomique","Écriture via fichier temporaire + os.replace — zéro corruption"],
  ["Mode parcours joueur","Simule une session, scores cumulés, sans relancer Unity"],
  ["Export Mermaid","Représentation versionnable rendue dans GitHub"],
];
feat.forEach((f,i)=>{
  const y=2.0+i*0.92;
  s.addShape(p.ShapeType.ellipse,{ x:7.75, y:y+0.04, w:0.32, h:0.32, fill:{color:SEA}, line:{type:"none"} });
  s.addText("✓", { x:7.75, y:y+0.02, w:0.32, h:0.32, fontFace:BFONT, fontSize:14, bold:true, color:"FFFFFF", align:"center", valign:"middle" });
  s.addText(f[0], { x:8.2, y:y-0.04, w:4.5, h:0.36, fontFace:BFONT, fontSize:15, bold:true, color:NAVY });
  s.addText(f[1], { x:8.2, y:y+0.32, w:4.55, h:0.5, fontFace:BFONT, fontSize:12, color:SLATE });
});
pageNum(s,8);

// =========================================================
// SLIDE 9 — MODULE IA
// =========================================================
s = newSlide(); darkBg(s);
s.addText("RÉSULTATS · MODULE IA", { x:0.6, y:0.5, w:12, h:0.4, fontFace:BFONT, fontSize:13, color:SEA, bold:true, charSpacing:3 });
s.addText("Génération orientée & scoring assisté", { x:0.6, y:0.9, w:12, h:0.7, fontFace:HFONT, fontSize:30, color:"FFFFFF", bold:true });

// pipeline
const pipe=["Paramètres IA\n(curseurs −3…+3)","build_ctx\n+ format_msg","LLM Backend\nOpenAI / Ollama","Filtrage\ndoublons","Validation\nhumaine"];
pipe.forEach((t,i)=>{
  const x=0.6+i*2.5;
  s.addShape(p.ShapeType.roundRect,{ x, y:1.95, w:2.2, h:1.05, fill:{color:i===4?AMBER:DEEP}, line:{type:"none"}, rectRadius:0.08 });
  s.addText(t, { x, y:1.95, w:2.2, h:1.05, fontFace:BFONT, fontSize:12, bold:true, color:i===4?NAVY:"FFFFFF", align:"center", valign:"middle" });
  if(i<4) s.addText("›", { x:x+2.18, y:2.2, w:0.34, h:0.55, fontFace:BFONT, fontSize:26, bold:true, color:SEA, align:"center" });
});
s.addText("Human-in-the-loop : aucune réponse IA n'entre dans un scénario sans validation de l'auteur.", { x:0.6, y:3.15, w:12, h:0.4, fontFace:BFONT, fontSize:13.5, italic:true, color:ICE });

// two function cards
const fcards=[
  ["Génération orientée","L'auteur fixe une cible sur les 7 dimensions. Le LLM propose des réponses cohérentes avec la branche narrative + une justification textuelle.", SEA],
  ["Scoring assisté","Sur une réponse existante, le LLM propose un vecteur de scores sur 7 dimensions, accompagné d'une justification explicable.", AMBER],
];
fcards.forEach((c,i)=>{
  const x=0.6+i*6.25;
  s.addShape(p.ShapeType.roundRect,{ x, y:3.8, w:5.85, h:1.85, fill:{color:DEEP}, line:{type:"none"}, rectRadius:0.1 });
  s.addShape(p.ShapeType.roundRect,{ x, y:3.8, w:0.14, h:1.85, fill:{color:c[2]}, line:{type:"none"} });
  s.addText(c[0], { x:x+0.35, y:3.98, w:5.3, h:0.45, fontFace:BFONT, fontSize:18, bold:true, color:"FFFFFF" });
  s.addText(c[1], { x:x+0.35, y:4.5, w:5.3, h:1.1, fontFace:BFONT, fontSize:13, color:ICE, lineSpacingMultiple:1.18 });
});
// strategy pattern note
s.addShape(p.ShapeType.roundRect,{ x:0.6, y:5.9, w:12.1, h:1.0, fill:{color:"1A3A52"}, line:{type:"none"}, rectRadius:0.08 });
s.addText("Pattern Strategy", { x:0.9, y:6.05, w:2.5, h:0.4, fontFace:BFONT, fontSize:15, bold:true, color:SEA });
s.addText("Backend choisi par variable d'environnement — OpenAI (qualité/rapidité) ou Ollama (exécution locale, conformité RGPD) — sans modifier le code applicatif.", { x:0.9, y:6.42, w:11.5, h:0.45, fontFace:BFONT, fontSize:13, color:ICE });
pageNum(s,9);

// =========================================================
// SLIDE 10 — RÉSULTATS : GÉNÉRATION ORIENTÉE
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Résultats · Évaluation IA", "Génération orientée : 100 % de conformité");
// big stats
const stats=[
  ["100 %","Conformité (±1) aux\nscores cibles", SEA],
  ["50 / 50","Générations réussies\n(0 erreur LLM)", TEAL],
  ["4,6 s","Temps moyen par\ngénération (OpenAI)", AMBER],
];
stats.forEach((st,i)=>{
  const x=0.7+i*4.0;
  card(s, x, 2.1, 3.65, 2.4, "FFFFFF");
  s.addShape(p.ShapeType.roundRect,{ x, y:2.1, w:3.65, h:0.14, fill:{color:st[2]}, line:{type:"none"} });
  s.addText(st[0], { x, y:2.55, w:3.65, h:1.0, fontFace:HFONT, fontSize:46, bold:true, color:NAVY, align:"center" });
  s.addText(st[1], { x:x+0.2, y:3.6, w:3.25, h:0.8, fontFace:BFONT, fontSize:14, color:SLATE, align:"center", lineSpacingMultiple:1.05 });
});
s.addShape(p.ShapeType.roundRect,{ x:0.7, y:4.85, w:11.95, h:1.9, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.1 });
s.addText("Protocole : 50 générations · 10 interactions distinctes × 5 profils pédagogiques (backend OpenAI gpt-4.1-mini).", { x:1.0, y:5.05, w:11.3, h:0.5, fontFace:BFONT, fontSize:14, bold:true, color:"FFFFFF" });
s.addText("Les profils problématiques produisent des formulations froides/maladroites ; les profils exemplaires, des réponses attentives et respectueuses. La validation humaine reste indispensable pour la pertinence clinique et le ton.", { x:1.0, y:5.55, w:11.3, h:1.1, fontFace:BFONT, fontSize:13.5, color:ICE, lineSpacingMultiple:1.2 });
pageNum(s,10);

// =========================================================
// SLIDE 11 — RÉSULTATS : SCORING ASSISTÉ (MAE)
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Résultats · Évaluation IA", "Scoring assisté : MAE de 0,77 / 7 niveaux");
// MAE bar chart per dimension
const mae=[
  ["Collaboration interpro.",0.13],["Régulation émotionnelle",0.60],["Respect & dignité",0.67],
  ["Clarté communication",0.73],["Frontières pro.",0.87],["Compassion",1.07],["Empathie",1.33],
];
const cx=0.7, cy=2.05, cw=8.0, rowH=0.6, maxV=1.4;
mae.forEach((m,i)=>{
  const y=cy+i*rowH;
  s.addText(m[0], { x:cx, y, w:2.9, h:rowH-0.1, fontFace:BFONT, fontSize:12.5, color:SLATE, align:"right", valign:"middle" });
  const bw=(m[1]/maxV)*4.3;
  const col = m[1]<0.7?SEA : m[1]<1.0?TEAL : AMBER;
  s.addShape(p.ShapeType.roundRect,{ x:cx+3.05, y:y+0.08, w:Math.max(bw,0.12), h:rowH-0.26, fill:{color:col}, line:{type:"none"}, rectRadius:0.03 });
  s.addText(m[1].toFixed(2), { x:cx+3.1+Math.max(bw,0.12), y:y+0.02, w:0.8, h:rowH-0.1, fontFace:BFONT, fontSize:12.5, bold:true, color:NAVY, valign:"middle" });
});
// right interpretation panel
s.addShape(p.ShapeType.roundRect,{ x:9.0, y:2.05, w:3.7, h:4.4, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.12 });
s.addText("0,77", { x:9.0, y:2.25, w:3.7, h:0.9, fontFace:HFONT, fontSize:52, bold:true, color:SEA, align:"center" });
s.addText("MAE globale (échelle −3 → +3)", { x:9.1, y:3.15, w:3.5, h:0.4, fontFace:BFONT, fontSize:12, color:ICE, align:"center" });
s.addText([
  { text:"Mieux prédites : ", options:{bold:true, color:"FFFFFF"} },
  { text:"dimensions explicites (collaboration, régulation).", options:{color:ICE}},
], { x:9.25, y:3.7, w:3.3, h:1.0, fontFace:BFONT, fontSize:13, lineSpacingMultiple:1.15 });
s.addText([
  { text:"Plus difficiles : ", options:{bold:true, color:AMBER} },
  { text:"empathie & compassion — subjectives et souvent superposées.", options:{color:ICE}},
], { x:9.25, y:4.85, w:3.3, h:1.4, fontFace:BFONT, fontSize:13, lineSpacingMultiple:1.15 });
s.addText("Aide à l'évaluation — supervision humaine requise.", { x:0.7, y:6.55, w:8.0, h:0.4, fontFace:BFONT, fontSize:13, italic:true, color:DEEP, bold:true });
pageNum(s,11);

// =========================================================
// SLIDE 12 — OPENAI vs OLLAMA + TESTS
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Résultats · Backends & validation", "OpenAI vs Ollama — un compromis assumé");
// comparison table
const rows=[
  ["Critère","OpenAI","Ollama"],
  ["JSON valide","10 / 10","10 / 10"],
  ["Conformité ±1","100 %","91,3 %"],
  ["Temps moyen","9,2 s","98,2 s"],
  ["Exécution locale","Non","Oui (RGPD)"],
];
const tx=0.7, ty=2.05, colW=[2.6,1.85,1.85], rh=0.62;
rows.forEach((r,i)=>{
  let x=tx;
  r.forEach((cell,j)=>{
    const isH=i===0;
    s.addShape(p.ShapeType.rect,{ x, y:ty+i*rh, w:colW[j], h:rh, fill:{color: isH?NAVY : (i%2? "FFFFFF":"E6EEF3")}, line:{color:"FFFFFF",width:1.5} });
    const hl = (j===1 && !isH && (i===2||i===3)) || (j===2 && i===4);
    s.addText(cell, { x:x+0.1, y:ty+i*rh, w:colW[j]-0.2, h:rh, fontFace:BFONT, fontSize:13.5, bold:isH||j===0, color: isH?"FFFFFF": (hl?DEEP:SLATE), align: j===0?"left":"center", valign:"middle" });
    x+=colW[j];
  });
});
s.addText("OpenAI : qualité & rapidité.  Ollama : confidentialité (les données restent sur la machine du formateur).", { x:0.7, y:5.5, w:6.7, h:0.8, fontFace:BFONT, fontSize:13, italic:true, color:SLATE, lineSpacingMultiple:1.15 });

// right: technical validation
s.addShape(p.ShapeType.roundRect,{ x:7.7, y:2.05, w:5.0, h:4.35, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.12 });
s.addText("Validation technique", { x:8.0, y:2.25, w:4.4, h:0.4, fontFace:BFONT, fontSize:15, bold:true, color:SEA });
const tv=[["27","tests pytest — 100 % de réussite"],["2","livres pédagogiques pris en charge"],["438","interactions · 1 232 arêtes"]];
tv.forEach((t,i)=>{
  const y=2.8+i*1.15;
  s.addText(t[0], { x:8.0, y, w:1.5, h:0.8, fontFace:HFONT, fontSize:38, bold:true, color:AMBER, align:"left" });
  s.addText(t[1], { x:9.55, y:y+0.12, w:2.9, h:0.7, fontFace:BFONT, fontSize:13.5, color:ICE, valign:"middle" });
});
s.addText("Round-trip JSON & écriture atomique validés sur les fichiers réels.", { x:8.0, y:6.0, w:4.4, h:0.35, fontFace:BFONT, fontSize:11.5, italic:true, color:MUTE });
pageNum(s,12);

// =========================================================
// SLIDE 13 — DISCUSSION / LIMITES
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Discussion", "Portée, limites et garde-fous éthiques");
const disc=[
  ["Conformité à interpréter avec prudence","Respecter un score cible ≠ porter l'intention narrative. Le ton, les silences et le non-verbal échappent à une analyse purement textuelle.", TEAL],
  ["Référence de scoring fragile","Scores humains fixés par un seul annotateur sur 15 réponses. Un accord inter-annotateurs (kappa de Cohen) consoliderait le gold standard.", AMBER],
  ["Pas encore de test utilisateur","L'ergonomie réelle reste à mesurer avec des formateurs et cliniciens du CHUV (SUS / PSSUQ).", DEEP],
];
disc.forEach((d,i)=>{
  const y=1.95+i*1.5;
  card(s, 0.6, y, 7.6, 1.32, "FFFFFF");
  s.addShape(p.ShapeType.roundRect,{ x:0.6, y, w:0.12, h:1.32, fill:{color:d[2]}, line:{type:"none"} });
  s.addText(d[0], { x:0.95, y:y+0.14, w:7.1, h:0.4, fontFace:BFONT, fontSize:16, bold:true, color:NAVY });
  s.addText(d[1], { x:0.95, y:y+0.55, w:7.1, h:0.7, fontFace:BFONT, fontSize:13, color:SLATE, lineSpacingMultiple:1.12 });
});
// ethics panel
s.addShape(p.ShapeType.roundRect,{ x:8.45, y:1.95, w:4.25, h:4.5, fill:{color:NAVY}, line:{type:"none"}, rectRadius:0.12 });
s.addText("Éthique", { x:8.75, y:2.2, w:3.7, h:0.4, fontFace:BFONT, fontSize:15, bold:true, color:SEA });
s.addText("Le human-in-the-loop est essentiel", { x:8.75, y:2.65, w:3.7, h:0.9, fontFace:HFONT, fontSize:21, bold:true, color:"FFFFFF", lineSpacingMultiple:1.0 });
s.addText("Les scénarios touchent au deuil et à la détresse. Aucune proposition IA n'est intégrée automatiquement.\n\nL'IA propose réponses, scores et justifications — la responsabilité finale reste au formateur clinique.", { x:8.75, y:3.75, w:3.7, h:2.5, fontFace:BFONT, fontSize:13.5, color:ICE, lineSpacingMultiple:1.2 });
pageNum(s,13);

// =========================================================
// SLIDE 14 — CONCLUSION
// =========================================================
s = newSlide(); darkBg(s);
s.addText("CONCLUSION", { x:0.6, y:0.55, w:12, h:0.4, fontFace:BFONT, fontSize:13, color:SEA, bold:true, charSpacing:3 });
s.addText("Un jeu sérieux devenu plateforme\nintelligente et maintenable", { x:0.6, y:0.95, w:12, h:1.4, fontFace:HFONT, fontSize:30, color:"FFFFFF", bold:true, lineSpacingMultiple:1.0 });
const concl=[
  ["Interface en graphe","Édition CRUD, validation EG-7, mode parcours joueur. 438 interactions, 1 232 arêtes. Round-trip Unity exact à 100 %.", SEA],
  ["Module IA explicable","100 % de conformité (OpenAI), MAE de 0,77 pour le scoring, justifications textuelles, double backend cloud/local RGPD.", AMBER],
  ["Architecture durable","Clean Architecture, modèles métier purs, 27 tests. Ajouter un livre = 2 étapes (JSON + entrée books.py).", ICE],
];
concl.forEach((c,i)=>{
  const x=0.6+i*4.1;
  s.addShape(p.ShapeType.roundRect,{ x, y:2.85, w:3.85, h:3.55, fill:{color:DEEP}, line:{type:"none"}, rectRadius:0.12 });
  s.addShape(p.ShapeType.ellipse,{ x:x+0.35, y:3.15, w:0.65, h:0.65, fill:{color:c[2]}, line:{type:"none"} });
  s.addText(String(i+1), { x:x+0.35, y:3.18, w:0.65, h:0.6, fontFace:HFONT, fontSize:22, bold:true, color:NAVY, align:"center", valign:"middle" });
  s.addText(c[0], { x:x+0.35, y:4.0, w:3.2, h:0.85, fontFace:BFONT, fontSize:18, bold:true, color:"FFFFFF" });
  s.addText(c[1], { x:x+0.35, y:4.85, w:3.25, h:1.45, fontFace:BFONT, fontSize:13, color:ICE, lineSpacingMultiple:1.18 });
});
s.addText("Objectifs atteints — exigences EG-1 à EG-7 et CT-1 à CT-3 du cahier des charges satisfaites.", { x:0.6, y:6.65, w:12, h:0.4, fontFace:BFONT, fontSize:14, italic:true, color:AMBER });
pageNum(s,14);

// =========================================================
// SLIDE 15 — PERSPECTIVES
// =========================================================
s = newSlide(); lightBg(s);
header(s, "Perspectives", "Vers un tuteur intelligent");
const persp=[
  ["Court terme","Test d'utilisabilité (SUS/PSSUQ) · scoring en lot exportable · accord inter-annotateurs sur tout le livre.", TEAL],
  ["Scoring dynamique côté joueur","Le LLM analyse les réponses de l'apprenant en temps réel pendant la simulation Unity → feedback formatif personnalisé.", SEA],
  ["Fine-tuning spécialisé","Modèle entraîné sur des réponses annotées par les experts CHUV, déployé localement via Ollama (perf + RGPD).", AMBER],
  ["Extension & immersion","Autres contextes critiques (oncologie, urgences, gériatrie) · expressions faciales MetaHuman pilotées par l'IA.", DEEP],
];
persp.forEach((d,i)=>{
  const col=i%2,row=Math.floor(i/2);
  const x=0.6+col*6.25,y=1.95+row*2.25;
  card(s, x, y, 5.85, 2.0, "FFFFFF");
  s.addShape(p.ShapeType.roundRect,{ x, y, w:5.85, h:0.14, fill:{color:d[2]}, line:{type:"none"} });
  s.addText(d[0], { x:x+0.35, y:y+0.28, w:5.15, h:0.5, fontFace:BFONT, fontSize:17, bold:true, color:NAVY });
  s.addText(d[1], { x:x+0.35, y:y+0.82, w:5.15, h:1.1, fontFace:BFONT, fontSize:13.5, color:SLATE, lineSpacingMultiple:1.2 });
});
pageNum(s,15);

// =========================================================
// SLIDE 16 — MERCI / QUESTIONS
// =========================================================
s = newSlide(); darkBg(s);
s.addShape(p.ShapeType.ellipse, { x:-2.0, y:4.2, w:5.5, h:5.5, fill:{ color:DEEP }, line:{type:"none"} });
s.addShape(p.ShapeType.ellipse, { x:10.8, y:-1.8, w:4.6, h:4.6, fill:{ color:TEAL }, line:{type:"none"} });
[[11.3,1.4,SEA],[12.2,2.2,ICE],[10.6,2.4,AMBER]].forEach(([x,y,c])=> s.addShape(p.ShapeType.ellipse,{x,y,w:0.16,h:0.16,fill:{color:c},line:{type:"none"}}));
s.addText("Merci de votre attention", { x:0.8, y:2.6, w:11.5, h:1.0, fontFace:HFONT, fontSize:46, bold:true, color:"FFFFFF" });
s.addShape(p.ShapeType.line, { x:0.85, y:3.75, w:3.8, h:0, line:{ color:AMBER, width:2.5 } });
s.addText("Questions & discussion", { x:0.85, y:3.95, w:10, h:0.6, fontFace:BFONT, fontSize:22, italic:true, color:ICE });
s.addText("Thomas Maksimous · MSE HES-SO · CHUV · UniL · Nº 2026-01", { x:0.85, y:5.6, w:11, h:0.4, fontFace:BFONT, fontSize:14, color:MUTE });

// =========================================================
// SPEAKER NOTES (texte à dire, ~20 min)
// =========================================================
const NOTES = [
// Slide 1 — Titre (~40 s)
`Bonjour à toutes et à tous. Je m'appelle Thomas Maksimous et je vais vous présenter mon projet d'approfondissement de Master, intitulé « Interactive Book for Medical Staff dealing with End-of-life Patients ». L'idée centrale : utiliser la narration interactive et l'intelligence artificielle pour entraîner les soignants à la communication en fin de vie. Ce travail a été encadré par le Professeur Stéphane Gobron à la HES-SO, avec l'expertise clinique de la Docteure Claudia Gamondi, médecin en soins palliatifs au CHUV. C'est un projet à trois partenaires : la HES-SO, le CHUV et l'Université de Lausanne.`,

// Slide 2 — Contexte (~75 s)
`Commençons par le contexte. Prendre en charge un patient en fin de vie, ce n'est pas seulement une question de compétence clinique. Le soignant doit mobiliser des compétences relationnelles très fines — ce qu'on appelle les soft skills : l'empathie, le respect, la compassion — face au deuil et à la détresse.
Aujourd'hui, on enseigne ça surtout par des jeux de rôle en petits groupes. C'est efficace pédagogiquement, mais c'est lourd : ça prend du temps, ça demande des formateurs spécialisés, et c'est très difficile à mettre à l'échelle.
C'est là qu'interviennent les serious games. Mon projet part d'un jeu sérieux en 3D existant, « End of Life », développé à la HES-SO avec le CHUV. La question de fond qu'il pose est forte : que signifie soigner lorsque guérir n'est plus l'objectif ? L'enjeu est d'offrir un cadre d'entraînement immersif et sécurisé, avant la confrontation à de vraies situations.`,

// Slide 3 — Problématique (~70 s)
`Mais l'application existante présentait deux verrous majeurs, et ce sont eux qui définissent tout mon projet.
Premier verrou : le contenu était figé. Les scénarios étaient stockés dans des gros fichiers JSON statiques. Concrètement, un médecin ou un formateur qui n'est pas informaticien ne pouvait absolument pas modifier un dialogue ou ajouter une branche. Le contenu pédagogique était prisonnier du code.
Deuxième verrou : l'évaluation était superficielle. Le scoring se limitait à trois axes fixes — empathie, respect, compassion — sans aucune analyse sémantique des choix faits par l'apprenant.
Le besoin était donc double : rendre l'outil flexible et accessible aux experts métier, et lui donner une intelligence capable d'épauler à la fois les créateurs de contenu et les apprenants.`,

// Slide 4 — Objectifs (~55 s)
`De ces deux verrous découlent directement mes deux objectifs.
Le premier, c'est une interface d'administration en graphe : un outil web visuel qui permet de voir, créer, modifier et supprimer les blocs narratifs et les branches d'un scénario — et tout ça sans écrire une seule ligne de code.
Le second, c'est l'intégration de l'intelligence artificielle, sur deux fronts. Côté création, l'IA assiste l'auteur en générant des propositions de réponses orientées pédagogiquement. Côté évaluation, elle propose un scoring sémantique et explicable des choix.
Et le fil rouge de tout le projet, c'est le principe « human-in-the-loop » : l'IA propose, mais c'est toujours l'humain qui valide.`,

// Slide 5 — État de l'art (~75 s)
`Avant de construire, j'ai cadré l'état de l'art autour de quatre axes qui convergent vers le projet.
Premier axe, les applications pour soignants : il en existe beaucoup pour l'aide à la décision ou la gestion du burn-out, mais très peu entraînent activement les compétences relationnelles.
Deuxième axe, les serious games de fin de vie : le cadre « Live, Die, Repeat » est emblématique — dans une étude, 88 % des résidents se sentaient plus confiants après la simulation.
Troisième axe, les « livres dont vous êtes le héros » et des outils comme Twine : ils popularisent le récit à embranchements, où chaque choix devient une arête dans un graphe. C'est exactement la structure que je réutilise.
Quatrième axe, l'évaluation des soft skills : avec des cadres cliniques comme PERCS, des échelles validées comme l'IRI ou la Jefferson Scale, et des approches par machine learning.
La lacune que je cible se situe précisément à l'intersection : un environnement narratif interactif qui entraîne ET évalue les compétences relationnelles.`,

// Slide 6 — Modèle de données (~80 s)
`Passons à la méthode, en commençant par le modèle de données.
Le format narratif d'origine est hiérarchique : un Chapitre contient des Scènes, qui contiennent des Interactions, qui contiennent des Réponses. J'ai conservé cette structure JSON pour rester totalement compatible avec le moteur Unity existant — c'était une contrainte forte.
Mon apport, c'est de transformer cette hiérarchie en graphe orienté, via un service dédié, le graph_service. Chaque Interaction devient un nœud, et chaque Réponse devient une arête, grâce au champ « NextInteractionID » qui pointe vers l'interaction suivante. Quand ce champ vaut moins un, c'est une fin de branche. Cette représentation rend les embranchements, les retours et les impasses immédiatement visibles.
Deuxième évolution importante : j'ai étendu le scoring de trois à sept dimensions de soft skills — respect, empathie, compassion, régulation émotionnelle, clarté, frontières professionnelles et collaboration — chacune notée sur une échelle de moins trois à plus trois.`,

// Slide 7 — Architecture (~70 s)
`Sur le plan logiciel, j'ai fait le choix d'une Clean Architecture, organisée en couches.
Tout en bas, la couche Domaine contient des modèles métier purs — Chapter, Scene, Interaction, etc. — totalement indépendants du web, de l'IA et de la persistance. Au-dessus, l'Infrastructure gère la lecture-écriture des fichiers JSON via un Repository. Puis la couche Application porte la logique : construction du graphe, validation, enrichissement IA. Et enfin la Présentation expose les pages web et l'API REST.
L'intérêt, c'est qu'on peut remplacer un composant sans toucher au reste — par exemple changer de backend IA sans modifier le modèle de domaine.
Côté stack, c'est volontairement léger et mature : Python avec Flask, des templates Jinja2, du JavaScript natif sans étape de build, et la bibliothèque vis-network pour afficher les graphes. Le résultat, c'est un code testable et maintenable au-delà de la durée du projet.`,

// Slide 8 — Plateforme livrée (~75 s)
`Voici le premier livrable concret : l'interface d'administration. À gauche, l'éditeur affiche le scénario sous forme de graphe interactif, avec la liste des scènes, le graphe central, et un panneau de propriétés pour éditer.
L'auteur dispose d'une édition CRUD complète : il modifie les textes, les noms, les scores et les références narratives.
Trois fonctionnalités sont particulièrement importantes. D'abord, une validation en temps réel : si une réponse pointe vers une interaction qui n'existe pas, l'erreur est signalée visuellement, ce qui évite les branches cassées. Ensuite, une sauvegarde atomique : on écrit d'abord dans un fichier temporaire, puis on remplace l'original en une seule opération — donc aucune corruption possible si l'écriture est interrompue. Enfin, un mode parcours joueur, qui permet de simuler une session et de vérifier les scores cumulés directement dans le navigateur, sans relancer Unity.
J'ai aussi ajouté un export Mermaid, qui produit une version textuelle et versionnable du scénario, lisible directement sur GitHub.`,

// Slide 9 — Module IA (~80 s)
`Deuxième livrable, le cœur Data Science : le module d'intelligence artificielle.
Le flux est le suivant : l'auteur règle des paramètres — notamment des curseurs de moins trois à plus trois sur les sept dimensions. Le système construit le contexte narratif, formate le message, l'envoie à un backend LLM, filtre les propositions trop proches de réponses existantes, et — point essentiel — soumet le tout à la validation humaine. Aucune réponse générée n'entre automatiquement dans un scénario.
Le module rend deux services. La génération orientée : l'auteur fixe une cible sur les dimensions, et le LLM produit des réponses cohérentes avec la branche narrative, accompagnées d'une justification. Et le scoring assisté : sur une réponse existante, le LLM propose un vecteur de scores sur les sept dimensions, là aussi avec une justification explicable.
Enfin, j'ai utilisé un pattern Strategy : le backend se choisit par une simple variable d'environnement. On bascule entre OpenAI — orienté qualité et rapidité — et Ollama, un modèle local orienté confidentialité et conformité RGPD, sans modifier le code applicatif.`,

// Slide 10 — Résultats génération (~60 s)
`Passons aux résultats, en commençant par la génération orientée.
J'ai mené une campagne d'évaluation sur 50 générations : 10 interactions distinctes croisées avec 5 profils pédagogiques, avec le backend OpenAI.
Le résultat est net : 100 % de conformité aux scores cibles, 50 générations réussies sur 50, zéro erreur de format, et un temps moyen de 4,6 secondes par génération.
Qualitativement, c'est cohérent : les profils dits « problématiques » produisent des formulations froides ou maladroites, tandis que les profils « exemplaires » génèrent des réponses attentives et respectueuses. Mais je reste prudent : respecter un score ne garantit pas la pertinence clinique ni le bon ton — d'où l'importance de la validation humaine.`,

// Slide 11 — Résultats scoring (~70 s)
`Venons-en au scoring assisté, qui est la partie la plus exigeante.
J'ai comparé les scores proposés par l'IA aux scores humains de référence, sur 15 réponses déjà notées du livre End of Life. La métrique est l'erreur absolue moyenne, la MAE.
Le résultat global est une MAE de 0,77, sur une échelle de 7 niveaux allant de moins trois à plus trois. Mais le plus intéressant, c'est la lecture par dimension, sur ce graphique.
Les dimensions les plus explicites sont très bien prédites : la collaboration interprofessionnelle est à 0,13, la régulation émotionnelle à 0,60 — parce qu'elles reposent sur des indices textuels visibles.
À l'inverse, l'empathie et la compassion sont les plus difficiles, à 1,33 et 1,07. Et c'est cohérent avec la littérature : ce sont des notions subjectives et souvent partiellement superposées. Conclusion : l'IA est une vraie aide à l'évaluation, mais elle ne remplace pas le jugement de l'expert.`,

// Slide 12 — Backends & validation (~70 s)
`Comparons maintenant les deux backends, et faisons le point sur la validation technique.
Sur dix prompts identiques : les deux produisent du JSON valide à chaque fois. OpenAI atteint 100 % de conformité contre 91,3 % pour Ollama. La grande différence est le temps : 9 secondes pour OpenAI, contre 98 secondes pour Ollama en local. En contrepartie, Ollama garde toutes les données sur la machine du formateur — c'est l'argument RGPD. Le compromis est donc assumé : OpenAI pour la qualité et la rapidité, Ollama pour la confidentialité.
Côté validation technique, à droite : 27 tests automatisés avec pytest, tous au vert. Ils couvrent les composants critiques. La plateforme gère deux livres pédagogiques réels, soit 438 interactions et 1 232 arêtes. Et surtout, le round-trip JSON et la sauvegarde atomique ont été validés sur les fichiers réels du projet : on lit et on réécrit sans jamais perdre de données.`,

// Slide 13 — Discussion (~70 s)
`Quelques mots de recul critique, car c'est important.
Première limite : cette conformité de 100 % est à interpréter avec prudence. Respecter un score cible n'est pas la même chose que porter la bonne intention narrative. Et l'IA n'analyse que du texte : le ton, les silences, le non-verbal — pourtant essentiels en fin de vie — lui échappent.
Deuxième limite : ma référence de scoring est fragile. Les scores humains ont été fixés par un seul annotateur, sur seulement 15 réponses. Un accord inter-annotateurs, mesuré par exemple avec le kappa de Cohen, serait nécessaire pour établir un vrai gold standard.
Troisième limite : je n'ai pas encore mené de test utilisateur formel. L'ergonomie réelle reste à valider avec des formateurs et des cliniciens du CHUV.
Sur le plan éthique enfin, le point clé est le human-in-the-loop. Ces scénarios touchent au deuil et à la détresse. Aucune proposition de l'IA n'est intégrée automatiquement : l'IA propose des réponses, des scores et des justifications, mais la responsabilité finale reste entre les mains du formateur clinique.`,

// Slide 14 — Conclusion (~55 s)
`En conclusion, le projet a transformé un jeu sérieux figé en une plateforme intelligente et maintenable, autour de trois contributions.
Une : une interface en graphe, avec édition complète, validation en temps réel et mode parcours joueur, qui gère 438 interactions et 1 232 arêtes, avec un round-trip Unity exact à 100 %.
Deux : un module d'IA explicable, qui atteint 100 % de conformité en génération, une MAE de 0,77 pour le scoring, avec des justifications textuelles et un double backend cloud et local compatible RGPD.
Trois : une architecture durable, en couches, avec des modèles métier purs et 27 tests — au point qu'ajouter un nouveau livre ne demande que deux étapes.
Au final, les objectifs de départ et les exigences du cahier des charges sont atteints.`,

// Slide 15 — Perspectives (~55 s)
`Quelles perspectives ? Plusieurs pistes, du plus proche au plus ambitieux.
À court terme : mener un vrai test d'utilisabilité avec des questionnaires standardisés, ajouter un scoring en lot exportable, et consolider la référence avec un accord inter-annotateurs sur tout le livre.
Plus ambitieux : un scoring dynamique côté joueur, où le LLM analyserait les réponses de l'apprenant en temps réel pendant la simulation, pour fournir un feedback formatif personnalisé.
Ensuite, le fine-tuning d'un modèle spécialisé, entraîné sur des réponses annotées par les experts du CHUV et déployé localement via Ollama — ce qui combinerait performance et RGPD.
Et enfin, l'extension à d'autres contextes critiques — oncologie, urgences, gériatrie — et une immersion renforcée, avec des expressions faciales d'avatars pilotées par l'IA.`,

// Slide 16 — Merci (~20 s)
`Voilà qui conclut ma présentation. Je vous remercie pour votre attention, et je suis maintenant à votre disposition pour vos questions.`,
];
_slides.forEach((sl, i)=>{ if(NOTES[i]) sl.addNotes(NOTES[i]); });

p.writeFile({ fileName: "/Users/thomaks/DEV/PA_26_EOL/output/PA_2026_EOL_presentation.pptx" }).then(f=> console.log("Saved:", f));
