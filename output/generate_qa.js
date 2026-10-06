const fs = require("fs");

// [section, [ [question, answer], ... ] ]
const QA = [
["Choix techniques — IA & LLM", [
["Pourquoi avoir choisi gpt-4.1-mini ?",
"Parce qu'il offre le meilleur compromis qualité / latence / coût pour cette tâche : il produit un JSON structuré fiable, respecte les consignes, et reste rapide — 4,6 secondes en moyenne par génération. Un modèle plus lourd n'apportait pas de gain mesurable sur mes 7 dimensions, et grâce au pattern Strategy je peux en changer par une simple variable d'environnement si besoin."],
["Comment garantissez-vous que le JSON renvoyé est toujours valide ?",
"Le format est imposé explicitement dans le message système — je demande une réponse STRICTEMENT en JSON, avec un schéma précis (texte, catégorie, 7 scores, justification). Côté code, toute erreur réseau, quota ou format lève une exception dédiée. Dans mes évaluations, j'ai obtenu 50 générations valides sur 50, et 10 sur 10 pour les deux backends."],
["Comment fonctionne le filtrage des doublons ?",
"Avant d'afficher une proposition, je la compare aux réponses déjà existantes : correspondance exacte, mais aussi insensible à la casse et aux espaces superflus. C'est couvert par des tests dédiés. Sur mes 50 générations, zéro doublon n'a été laissé passer."],
["Pourquoi une échelle de −3 à +3 et 7 dimensions ?",
"L'échelle symétrique est lisible par un humain : le négatif marque une réponse problématique, le positif une réponse exemplaire, et zéro le neutre. Les 7 dimensions étendent les 3 axes d'origine (empathie, respect, compassion) ; elles ont été définies selon les objectifs pédagogiques et validées par la Dre Gamondi, en cohérence avec des cadres comme PERCS."],
]],

["Évaluation & rigueur scientifique", [
["Une conformité de 100 %, n'est-ce pas trivial puisque vous donnez les scores cibles dans le prompt ?",
"C'est une remarque juste, et je l'assume dans le rapport. Cette conformité mesure que le modèle reproduit fidèlement l'orientation demandée — pas la validité clinique absolue du texte. C'est exactement pourquoi je propose en perspective une expérience sans orientation explicite, pour mesurer la capacité réelle du modèle, et pourquoi la validation humaine reste indispensable."],
["Votre échantillon — 50 générations, 15 réponses scorées — n'est-il pas trop petit ?",
"Oui, c'est une limite que je reconnais : il s'agit d'une première validation, pas d'une étude à grande échelle. En perspective, je propose d'étendre le scoring à tout le livre et d'ajouter des intervalles de confiance plus robustes sur la MAE."],
["Pourquoi la MAE comme métrique, et pas autre chose ?",
"Parce qu'elle est directement interprétable : 0,77 signifie qu'en moyenne l'IA s'écarte de 0,77 point des scores humains, sur la même échelle de 7 niveaux. C'est parlant pour un formateur. Je la compléterais volontiers par un accord inter-annotateurs, mesuré au kappa de Cohen — c'est dans mes perspectives."],
["Vos scores humains de référence ont été fixés par une seule personne. N'est-ce pas un biais ?",
"Tout à fait, c'est la principale fragilité de ma référence. Pour établir un vrai gold standard, il faudrait faire annoter les mêmes réponses par plusieurs experts cliniques et mesurer leur accord. Je le mentionne explicitement comme étape nécessaire."],
["Pourquoi l'empathie et la compassion sont-elles les moins bien prédites ?",
"Parce que ce sont des notions subjectives et souvent partiellement superposées — la littérature le confirme. De plus, le LLM n'analyse que du texte : il n'a pas accès au ton, aux silences ni au non-verbal, qui sont justement essentiels en fin de vie."],
]],

["Éthique, RGPD & sécurité", [
["Comment évitez-vous qu'une réponse IA cliniquement inappropriée soit utilisée ?",
"Par le principe du human-in-the-loop : aucune proposition n'est insérée automatiquement, l'auteur relit et valide chaque réponse. Le message système impose le respect de la déontologie infirmière, et chaque proposition est catégorisée — exemplaire, neutre ou problématique. Enfin, les scénarios et dimensions ont été validés cliniquement par la Dre Gamondi."],
["Pourquoi proposer un backend local Ollama ?",
"Pour la conformité RGPD. Même si les scénarios sont fictifs, une version future pourrait s'inspirer de cas réels du CHUV. Le backend local garde alors toutes les données sur la machine du formateur. C'est une contrainte explicite du cahier des charges, et le pattern Strategy permet d'y répondre sans modifier le code."],
["Un mauvais score proposé par l'IA ne risque-t-il pas d'induire un mauvais apprentissage ?",
"C'est précisément pour ça que l'IA reste un assistant, pas un décideur. Elle propose un score et une justification ; le formateur accepte, corrige ou rejette. La responsabilité pédagogique finale reste humaine."],
]],

["Architecture & ingénierie", [
["Quel est le bénéfice concret du pattern Strategy ?",
"Il rend le module IA indépendant du fournisseur. J'ai une interface commune et deux implémentations — OpenAI et Ollama — interchangeables par configuration. Ça me donne la flexibilité RGPD, ça facilite les tests, et ça rendra l'ajout d'un futur modèle trivial."],
["Comment garantissez-vous la compatibilité avec le moteur Unity existant ?",
"Je conserve le format JSON hiérarchique d'origine, et mon round-trip préserve même les champs que je ne modélise pas, comme les expressions faciales de l'avatar. C'est validé par des tests sur les fichiers réels du projet : on lit et on réécrit sans rien perdre."],
["Pourquoi une sauvegarde atomique, et comment ?",
"Parce que le JSON est la source de vérité utilisée par Unity : une écriture interrompue ne doit jamais le corrompre. J'écris d'abord dans un fichier temporaire, puis je le renomme sur le fichier cible en une seule opération atomique. En cas d'échec, l'original reste intact."],
["Pourquoi Flask et du JavaScript natif plutôt qu'un framework plus lourd ?",
"Par souci de simplicité et de maintenabilité. Flask est léger et mature pour le JSON, les tests et l'intégration LLM ; le front en modules JavaScript natifs évite toute chaîne de compilation complexe. L'objectif était un outil durable, pas une usine à gaz."],
]],

["Produit, limites & perspectives", [
["Qu'est-ce qui distingue votre outil d'un éditeur comme Twine ?",
"Twine partage l'idée du récit en graphe, mais mon outil est orienté médical : scoring multidimensionnel des soft skills, assistance IA pour la génération et l'évaluation, et compatibilité directe avec le moteur Unity. C'est cette combinaison qui constitue la contribution."],
["Qui utilise réellement ces outils IA ?",
"Les formateurs et auteurs de scénarios — des experts métier. Le joueur, lui, n'utilise pas les outils IA : il joue le serious game 3D. Mes outils servent à créer et maintenir le contenu en amont."],
["Quelle est la principale limite de votre travail ?",
"Que l'IA n'analyse que du texte, alors que la communication en fin de vie passe aussi par le ton, les silences et le non-verbal. Et sur le plan méthodologique, l'absence encore d'un test utilisateur formel avec des cliniciens et d'un accord inter-annotateurs."],
["Le scoring dynamique côté joueur, est-ce réaliste ?",
"Techniquement oui : il s'agirait d'appeler le LLM en temps réel sur les réponses de l'apprenant pendant la simulation. Les défis sont la latence et la validation de la qualité. C'est ma perspective la plus ambitieuse, qui transformerait l'assistant en véritable tuteur intelligent."],
]],
];

const NAVY="#001B58", ROYAL="#385CB0", TEAL="#0097A7", PALE="#E3EDFF", INK="#2b3650", MUTE="#7a869c";
function esc(t){ return t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
const totalQ = QA.reduce((a,s)=>a+s[1].length,0);

let body = QA.map(([sec,items])=>{
  const cards = items.map(([q,a])=>`
    <div class="qa">
      <div class="q"><span class="qb">Q</span><span>${esc(q)}</span></div>
      <div class="a">${esc(a)}</div>
    </div>`).join("\n");
  return `<div class="section"><div class="sec-h">${esc(sec)}</div>${cards}</div>`;
}).join("\n");

const html = `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
  @page { size:A4; margin:16mm 15mm 14mm 15mm; }
  html { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  * { box-sizing:border-box; }
  body { font-family:"Assistant","Calibri","Helvetica Neue",Arial,sans-serif; color:${INK}; font-size:11pt; line-height:1.45; margin:0; }
  h1 { font-family:"Archivo","Georgia",serif; color:${NAVY}; font-size:23pt; margin:0 0 2pt 0; }
  .cover { border-left:6px solid ${ROYAL}; padding:6pt 0 10pt 14pt; margin-bottom:13pt; }
  .cover .sub { color:${TEAL}; font-weight:700; letter-spacing:1px; text-transform:uppercase; font-size:10pt; }
  .cover .meta { color:${MUTE}; font-size:10pt; margin-top:8pt; }
  .cover .total { display:inline-block; margin-top:8pt; background:${PALE}; color:${NAVY}; font-weight:700; padding:5pt 12pt; border-radius:14pt; font-size:10.5pt; }
  .section { margin-bottom:6pt; }
  .sec-h { font-family:"Archivo",sans-serif; color:#fff; background:${ROYAL}; font-weight:700; font-size:12pt;
           padding:6pt 12pt; border-radius:7pt; margin:10pt 0 8pt 0; page-break-after:avoid; }
  .qa { page-break-inside:avoid; border:1px solid #d8e2f2; border-radius:8pt; padding:8pt 11pt; margin-bottom:8pt; }
  .q { display:flex; gap:8pt; align-items:flex-start; font-family:"Archivo","Georgia",serif; font-weight:700; color:${NAVY}; font-size:11.5pt; }
  .qb { flex:0 0 auto; width:18pt; height:18pt; border-radius:50%; background:${TEAL}; color:#fff; font-size:10pt;
        display:flex; align-items:center; justify-content:center; margin-top:1pt; }
  .a { margin-top:5pt; padding-left:26pt; text-align:justify; }
  .a::before { content:"R "; color:${ROYAL}; font-weight:700; }
</style></head><body>
  <div class="cover">
    <div class="sub">Oral PA · MSE HES-SO · Nº 2026-01</div>
    <h1>Questions probables du jury — réponses prêtes</h1>
    <div style="color:${ROYAL};font-weight:700;font-size:12pt;">Interactive Book for Medical Staff dealing with End-of-life Patients · Module IA</div>
    <div class="meta">Thomas Maksimous · ${totalQ} questions · 5 thèmes (IA · évaluation · éthique/RGPD · architecture · produit)</div>
    <div class="total">À relire la veille — repérer les 4-5 questions les plus probables et les formuler à voix haute</div>
  </div>
  ${body}
</body></html>`;

fs.writeFileSync("/Users/thomaks/DEV/PA_26_EOL/output/qa_jury.html", html);
console.log("QA HTML written. Questions:", totalQ);
