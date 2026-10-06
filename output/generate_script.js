const fs = require("fs");

// Real deck = 17 visible slides. [kicker, title, durationSec, scriptText]
const SLIDES = [
["Slide titre","Interactive Book for Medical Staff dealing with End-of-life Patients",45,
`Bonjour à toutes et à tous. Je m'appelle Thomas Maksimous, et je vais vous présenter mon projet d'approfondissement de Master, intitulé « Interactive Book for Medical Staff dealing with End-of-life Patients ».
En une phrase : utiliser la narration interactive et l'intelligence artificielle pour aider à former les soignants à la communication en fin de vie.
Le projet s'inscrit dans un consortium à trois partenaires : la HES-SO pour l'ingénierie et la Data Science, le CHUV — représenté par la Docteure Claudia Gamondi — pour la validation clinique, et l'Université de Lausanne. Il a été encadré par le Professeur Stéphane Gobron.
Je vais d'abord poser le contexte et la problématique, puis me concentrer sur le cœur de ma contribution : le module d'intelligence artificielle.`],

["Contexte","Former à la communication en fin de vie",75,
`Commençons par le contexte. Prendre en charge un patient en fin de vie, ce n'est pas seulement une question de compétence clinique. Le soignant doit mobiliser des compétences relationnelles très fines — ce qu'on appelle les soft skills : l'empathie, le respect profond, la compassion — face au deuil et à la détresse.
Aujourd'hui, on enseigne ça surtout par des jeux de rôle en petits groupes. C'est efficace pédagogiquement, mais c'est lourd : ça prend du temps, ça mobilise des formateurs spécialisés, et c'est difficile à mettre à l'échelle.
C'est là qu'interviennent les serious games. Mon travail part d'un jeu sérieux en 3D existant, « End of Life », développé à la HES-SO avec le CHUV. La question de fond qu'il pose est forte : que signifie soigner lorsque guérir n'est plus l'objectif ? L'idée est d'offrir un cadre d'entraînement immersif et sécurisé, où l'on peut tester des choix difficiles avant la confrontation à de vraies situations.`],

["Problématique","Deux verrous de l'application existante",70,
`Mais l'application existante présentait deux verrous majeurs — et ce sont eux qui définissent tout mon travail.
Premier verrou : le contenu était figé. Les scénarios étaient stockés dans de gros fichiers JSON statiques. Concrètement, un médecin ou un formateur qui n'est pas informaticien ne pouvait pas modifier un dialogue ni ajouter une branche : le contenu pédagogique était prisonnier du code.
Second verrou : l'évaluation était superficielle. Le scoring se limitait à trois axes fixes — empathie, respect, compassion — sans aucune analyse sémantique des choix faits par l'apprenant.
Le besoin était donc double : rendre l'outil flexible et accessible aux experts métier, et lui donner une intelligence capable d'épauler à la fois les créateurs de contenu et les apprenants.`],

["Ma contribution (PA)","Deux briques que j'ai développées",65,
`Un point important sur le périmètre. Le jeu sérieux 3D « End of Life », développé sous Unity, est le projet existant du Professeur Gobron, avec le CHUV. C'est la base sur laquelle je me suis greffé.
Ma contribution, dans le cadre de ce projet d'approfondissement, ce sont deux briques que j'ai développées.
La première : une interface d'administration en graphe — un outil web visuel pour voir, créer, modifier et supprimer les blocs narratifs et les branches d'un scénario, sans écrire une ligne de code.
La seconde, et c'est le cœur de mon travail en Data Science : le module d'intelligence artificielle, sur deux fronts. Côté création, l'IA génère de nouvelles réponses orientées pédagogiquement. Côté évaluation, elle propose un scoring sémantique et explicable des choix.
Le fil rouge des deux : le principe « human-in-the-loop » — l'IA propose, l'humain valide.`],

["État de l'art","Quatre axes convergent vers le projet",75,
`Avant de construire, j'ai cadré l'état de l'art autour de quatre axes qui convergent vers le projet.
Premier axe, les applications pour soignants : il en existe beaucoup pour l'aide à la décision ou la gestion du burn-out, mais très peu entraînent activement les compétences relationnelles.
Deuxième axe, les serious games de fin de vie : le cadre « Live, Die, Repeat » est emblématique — dans une étude citée, 88 % des résidents se sentaient plus confiants après la simulation.
Troisième axe, les « livres dont vous êtes le héros » et des outils comme Twine : ils popularisent le récit à embranchements, où chaque choix devient une arête d'un graphe. C'est exactement la structure que je réutilise.
Quatrième axe, l'évaluation des soft skills : avec des cadres cliniques comme PERCS, des échelles validées comme l'IRI ou la Jefferson Scale, et des approches par machine learning.
La lacune que je cible se situe à l'intersection : un environnement narratif interactif qui entraîne — et évalue — les compétences relationnelles.`],

["Méthode · Modèle de données","Du JSON hiérarchique au graphe orienté",80,
`Passons à la méthode, en commençant par le modèle de données.
Le format d'origine est hiérarchique : un Chapitre contient des Scènes, qui contiennent des Interactions, qui contiennent des Réponses. J'ai conservé cette structure JSON pour rester totalement compatible avec le moteur Unity — c'était une contrainte forte.
Mon apport, c'est de transformer cette hiérarchie en graphe orienté, via un service dédié. Chaque Interaction devient un nœud, et chaque Réponse devient une arête, grâce au champ NextInteractionID qui pointe vers l'interaction suivante. Quand il vaut moins un, c'est une fin de branche.
Deux points clés. D'abord, j'ai étendu le scoring de trois à sept dimensions de soft skills, sur une échelle de moins trois à plus trois ; et j'ai gardé en parallèle les anciennes dimensions, pour la rétrocompatibilité Unity. Ensuite, le round-trip JSON préserve même les champs que je ne modélise pas explicitement — comme les expressions faciales de l'avatar — pour ne rien perdre côté moteur de jeu.`],

["Méthode · Architecture","Clean Architecture en couches",70,
`Sur le plan logiciel, j'ai choisi une Clean Architecture, organisée en couches.
Tout en bas, la couche Domaine contient des modèles métier purs — Chapter, Scene, Interaction, Response, Actor — indépendants du web, de l'IA et de la persistance. Au-dessus, l'Infrastructure gère la lecture-écriture JSON via un Repository. Puis la couche Application porte la logique : construction du graphe, validation des références, et tout le sous-package d'enrichissement IA. Enfin, la Présentation expose les pages web et une API REST.
L'intérêt, c'est qu'on remplace un composant sans toucher au reste — par exemple changer de backend IA sans modifier le domaine.
Côté technologies, c'est volontairement léger et mature : Python avec Flask, des templates Jinja2, du JavaScript natif sans étape de build, et la bibliothèque vis-network pour afficher les graphes. Résultat : un code testable et maintenable au-delà du projet.`],

["Résultats · Plateforme","Interface d'administration livrée",75,
`Premier livrable concret : l'interface d'administration. À gauche, l'éditeur affiche le scénario sous forme de graphe interactif — liste des scènes, graphe central, et panneau de propriétés pour éditer.
L'auteur dispose d'une édition complète : textes, noms, scores, références narratives.
Trois fonctionnalités sont importantes. D'abord, une validation en temps réel : si une réponse pointe vers une interaction qui n'existe pas, l'erreur est signalée visuellement — ça évite les branches cassées. Ensuite, une sauvegarde atomique : j'écris d'abord dans un fichier temporaire, puis je remplace l'original en une seule opération, donc aucune corruption possible si l'écriture est interrompue. Enfin, un mode parcours joueur, pour simuler une session et vérifier les scores cumulés, sans relancer Unity.
J'ai aussi un export Mermaid, qui donne une version textuelle et versionnable lisible sur GitHub. Aujourd'hui, la plateforme gère deux livres pédagogiques réels — soit 438 interactions et plus de 1 200 arêtes.`],

["Ma contribution · Module IA","Vue d'ensemble : génération & scoring",80,
`J'arrive au cœur de mon travail : le module d'intelligence artificielle. Il rend deux services complémentaires : la génération de nouvelles réponses, et le scoring assisté.
Architecturalement, tout est isolé dans un sous-package d'enrichissement, organisé autour d'une façade. Cette façade coordonne trois composants : un qui construit le contexte narratif, un qui formate les messages envoyés au modèle, et un qui filtre les propositions trop proches de l'existant.
Point central : les appels au LLM passent par un pattern Strategy. J'ai défini une interface commune, et deux implémentations — OpenAI, un backend distant, et Ollama, un modèle local. On bascule de l'un à l'autre par une simple variable d'environnement, sans modifier le code applicatif. C'est ce qui me permet de répondre à la contrainte RGPD : un modèle local quand les données sont sensibles.
Et dans tous les cas, le principe reste le human-in-the-loop : l'IA propose, l'auteur valide.`],

["Ma contribution · Module IA","Génération de nouvelles réponses avec l'IA",85,
`Entrons dans le détail de la première fonctionnalité : la génération de nouvelles réponses.
Le principe, c'est que l'auteur n'attend pas seulement « une réponse plausible » : il oriente la génération. Il fournit l'interaction courante et l'interaction cible, il règle les sept curseurs de soft skills entre moins trois et plus trois, et il peut ajouter une consigne libre sur le ton. Le système y ajoute automatiquement le contexte narratif : la scène, le profil du personnage et les réponses déjà existantes.
Côté prompt, j'utilise deux messages. Un message système fixe, qui définit le rôle — un assistant pédagogique spécialisé en fin de vie — et impose le format de sortie : pour chaque proposition, le texte, une catégorie (exemplaire, neutre ou problématique), les sept scores, et une justification, le tout en JSON strict. Et un message utilisateur construit dynamiquement, qui assemble jusqu'à quatre sections : le nombre de propositions, la suite narrative — en demandant de ne pas divulgâcher l'interaction suivante — l'orientation soft skills avec une tolérance de plus ou moins un, et la consigne libre.
Enfin, je filtre les doublons, et rien n'est inséré sans relecture. À droite, vous avez un exemple complet de proposition générée.`],

["Ma contribution · Module IA","Scoring assisté d'une réponse",80,
`Seconde fonctionnalité : le scoring assisté. Le module ne sert pas qu'à créer, il sait aussi évaluer.
En entrée, on lui donne le texte d'une réponse — existante ou fraîchement proposée — avec son contexte narratif. En sortie, j'obtiens un JSON structuré : un vecteur de sept scores entre moins trois et plus trois, et surtout une justification textuelle.
Cette justification, c'est l'élément clé pour le formateur. Par exemple, sur la réponse « je frappe doucement et j'attends un instant pour respecter son rythme », le modèle attribue un plus trois en respect de la dignité, un plus deux en empathie, et explique : attendre en silence traduit une bonne maîtrise émotionnelle et une communication non intrusive. L'évaluation devient donc transparente, pas une boîte noire.
Là encore, l'auteur garde la main : il accepte, corrige ou rejette. Et j'ai validé cette fonctionnalité sur le terrain — j'y reviens à la slide suivante — avec une erreur moyenne de 0,77 par rapport aux scores humains.`],

["Démonstration","Démo live de la plateforme",90,
`Plutôt que de tout décrire, je vous propose une démonstration en direct.
Je vais d'abord charger un livre et afficher le scénario sous forme de graphe : on voit immédiatement les embranchements et les fins de branche. Ensuite, je sélectionne une interaction et j'édite une réponse, en réglant les curseurs de soft skills. Puis je lance la génération assistée par l'IA : vous verrez les propositions arriver, avec leur catégorie, leurs scores et leur justification — et c'est moi qui valide ou rejette. Je montrerai aussi le scoring sur une réponse existante. Enfin, je bascule en mode parcours joueur pour suivre une branche et observer les scores cumulés, sans relancer Unity.
[Si la démo live échoue, j'ai des captures d'écran de secours.] Revenons ensuite aux résultats chiffrés.`],

["Résultats · Évaluation IA","Scoring assisté : MAE de 0,77 / 7 niveaux",80,
`Place aux résultats, sur deux campagnes d'évaluation.
D'abord la génération orientée. Je l'ai évaluée sur 50 cas — dix interactions croisées avec cinq profils pédagogiques, du « très empathique » au « problématique ». Le résultat est net : 100 % de conformité aux scores cibles, exacte comme à plus ou moins un, 50 réussites sur 50, zéro erreur de format, zéro doublon, et 4,6 secondes en moyenne par génération.
Ensuite, le scoring assisté, affiché à l'écran. J'ai comparé les scores de l'IA aux scores humains de référence, sur 15 réponses du livre End of Life. La métrique est l'erreur absolue moyenne : 0,77 sur une échelle de sept niveaux.
La lecture par dimension est instructive. Les dimensions explicites sont très bien prédites — la collaboration interprofessionnelle à 0,13, la régulation émotionnelle à 0,60. À l'inverse, l'empathie et la compassion sont les plus difficiles, à 1,33 et 1,07 : ce sont des notions subjectives et souvent superposées. Conclusion : l'IA est une vraie aide à l'évaluation, mais elle ne remplace pas le jugement de l'expert.`],

["Résultats · Backends & validation","OpenAI vs Ollama — un compromis assumé",75,
`Comparons maintenant les deux backends, puis la validation technique.
Sur dix prompts identiques : les deux produisent du JSON valide à chaque fois. Avec OpenAI — le modèle gpt-4.1-mini — j'obtiens 100 % de conformité ; avec Ollama, en local — le modèle llama3.1:8b — 91,3 %. La grande différence, c'est le temps : environ 9 secondes pour OpenAI, contre près de 100 secondes pour Ollama. En contrepartie, Ollama garde toutes les données sur la machine du formateur : c'est l'argument RGPD. Le compromis est donc assumé — qualité et rapidité d'un côté, confidentialité de l'autre — et le pattern Strategy permet de basculer sans rien changer au code.
Côté validation, à droite : une suite de tests automatisés, tous au vert, qui couvre les composants critiques — round-trip JSON, construction du graphe, validation des références, filtrage IA. Et surtout, ce round-trip et la sauvegarde atomique ont été validés sur les fichiers réels du projet : on lit et on réécrit sans jamais perdre de données.`],

["Conclusion","Un jeu sérieux devenu plateforme intelligente",55,
`En conclusion, mon travail a transformé un jeu sérieux figé en une plateforme intelligente et maintenable, autour de trois contributions.
Une : une interface en graphe, avec édition complète, validation en temps réel et mode parcours joueur, qui gère 438 interactions, avec un round-trip Unity exact.
Deux, le cœur Data Science : un module d'IA explicable, qui atteint 100 % de conformité en génération, une erreur moyenne de 0,77 pour le scoring, avec des justifications textuelles et un double backend cloud et local compatible RGPD.
Trois : une architecture durable, en couches, testée — au point qu'ajouter un nouveau livre ne demande que deux étapes.
Au final, les objectifs de départ et les exigences du cahier des charges sont atteints.`],

["Perspectives","Vers un tuteur intelligent",55,
`Quelles perspectives ? Plusieurs pistes, du plus proche au plus ambitieux.
À court terme : mener un vrai test d'utilisabilité avec des formateurs du CHUV, ajouter un scoring en lot exportable, et consolider la référence d'évaluation avec un accord inter-annotateurs sur l'ensemble du livre.
Plus ambitieux : un scoring dynamique côté joueur, où le modèle analyserait les réponses de l'apprenant en temps réel pendant la simulation, pour fournir un feedback formatif personnalisé.
Ensuite, le fine-tuning d'un modèle spécialisé, entraîné sur des réponses annotées par les experts, et déployé localement via Ollama — ce qui combinerait performance et RGPD.
Et enfin, l'extension à d'autres contextes critiques — oncologie, urgences, gériatrie — avec des expressions faciales d'avatars pilotées par l'IA.`],

["Clôture","Merci de votre attention",20,
`Voilà qui conclut ma présentation. Je vous remercie pour votre attention, et je suis à votre disposition pour vos questions.`],
];

const NAVY="#001B58", ROYAL="#385CB0", TEAL="#0097A7", PALE="#E3EDFF", INK="#2b3650", MUTE="#7a869c";
const totalSec = SLIDES.reduce((a,m)=>a+m[2],0);
const mm = Math.floor(totalSec/60), ss = totalSec%60;
function esc(t){ return t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

let blocks = SLIDES.map((m,i)=>{
  const [kicker,title,dur,txt]=m;
  const paras = txt.split("\n").map(p=>p.trim()).filter(Boolean).map(p=>`<p>${esc(p)}</p>`).join("\n");
  return `
  <section class="slide">
    <div class="head">
      <div class="num">${i+1}</div>
      <div class="titles"><div class="kicker">${esc(kicker)}</div><div class="title">${esc(title)}</div></div>
      <div class="dur">~${dur}s</div>
    </div>
    <div class="body">${paras}</div>
  </section>`;
}).join("\n");

const html = `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
  @page { size: A4; margin: 16mm 15mm 14mm 15mm; }
  html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  * { box-sizing: border-box; }
  body { font-family:"Assistant","Calibri","Helvetica Neue",Arial,sans-serif; color:${INK}; font-size:11.2pt; line-height:1.5; margin:0; }
  h1 { font-family:"Archivo","Georgia",serif; color:${NAVY}; font-size:24pt; margin:0 0 2pt 0; }
  .cover { border-left:6px solid ${ROYAL}; padding:6pt 0 10pt 14pt; margin-bottom:14pt; }
  .cover .sub { color:${TEAL}; font-weight:700; letter-spacing:1px; text-transform:uppercase; font-size:10pt; }
  .cover .meta { color:${MUTE}; font-size:10pt; margin-top:8pt; }
  .cover .total { display:inline-block; margin-top:8pt; background:${PALE}; color:${NAVY}; font-weight:700; padding:5pt 12pt; border-radius:14pt; font-size:10.5pt; }
  .slide { page-break-inside: avoid; margin:0 0 13pt 0; padding:10pt 12pt; border:1px solid #d8e2f2; border-radius:9pt; }
  .head { display:flex; align-items:flex-start; gap:11pt; border-bottom:1px solid #e7eef9; padding-bottom:7pt; margin-bottom:7pt; }
  .num { flex:0 0 auto; width:30pt; height:30pt; border-radius:50%; background:${ROYAL}; color:#fff; font-family:"Archivo",sans-serif; font-weight:700; font-size:14pt; display:flex; align-items:center; justify-content:center; }
  .titles { flex:1 1 auto; }
  .kicker { color:${TEAL}; font-weight:700; text-transform:uppercase; letter-spacing:.8px; font-size:8.6pt; }
  .title { font-family:"Archivo","Georgia",serif; color:${NAVY}; font-weight:700; font-size:14pt; line-height:1.2; }
  .dur { flex:0 0 auto; color:${ROYAL}; background:${PALE}; font-weight:700; font-size:9.5pt; padding:3pt 9pt; border-radius:11pt; white-space:nowrap; }
  .body p { margin:0 0 6pt 0; text-align:justify; }
  .body p:last-child { margin-bottom:0; }
</style></head><body>
  <div class="cover">
    <div class="sub">Oral PA · MSE HES-SO · Nº 2026-01</div>
    <h1>Script de présentation — slide par slide</h1>
    <div style="color:${ROYAL};font-weight:700;font-size:12.5pt;">Interactive Book for Medical Staff dealing with End-of-life Patients</div>
    <div class="meta">Thomas Maksimous · Sup. Prof. Stéphane Gobron (HES-SO) · Experte Dre Claudia Gamondi (CHUV)<br>
    17 slides visibles · texte à dire intégral et minuté</div>
    <div class="total">Durée totale visée : ≈ ${mm} min ${ss<10?"0"+ss:ss} s (hors démo & questions)</div>
  </div>
  ${blocks}
</body></html>`;

fs.writeFileSync("/Users/thomaks/DEV/PA_26_EOL/output/script_oral.html", html);
console.log("HTML written. Slides:", SLIDES.length, "Total:", mm+"m"+ss+"s");
