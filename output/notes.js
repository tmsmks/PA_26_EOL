module.exports = [
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

// Slide 4 — Ma contribution (~60 s)
`Un point important sur le périmètre. Le jeu sérieux 3D « End of Life », développé sous Unity, est le projet existant du Professeur Gobron, avec le CHUV. C'est la base sur laquelle je me suis greffé.
Ma contribution, dans le cadre de ce projet d'approfondissement, ce sont deux briques que j'ai développées.
La première, c'est une interface d'administration en graphe : un outil web visuel qui permet de voir, créer, modifier et supprimer les blocs narratifs et les branches d'un scénario — sans écrire une ligne de code.
La seconde, et c'est le cœur de mon travail en Data Science, c'est le module d'intelligence artificielle, sur deux fronts. Côté création, l'IA génère des propositions de réponses orientées pédagogiquement. Côté évaluation, elle propose un scoring sémantique et explicable des choix.
Le fil rouge des deux : le principe « human-in-the-loop » — l'IA propose, mais c'est toujours l'humain qui valide.`,

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

// Slide 10 — Génération de réponses (~75 s)
`Entrons dans le détail de ma première fonctionnalité IA : la génération de nouvelles réponses.
Le principe, c'est que l'auteur ne demande pas seulement « une réponse plausible » : il oriente la génération. Concrètement, il fournit l'interaction courante et l'interaction cible, il règle les sept curseurs de soft skills entre moins trois et plus trois, et il peut ajouter une consigne libre sur le ton. À cela, le système ajoute automatiquement le contexte narratif : la scène, le personnage et les réponses déjà existantes.
Côté pipeline : je construis le contexte, je formate un message système et un message utilisateur, j'appelle le backend LLM, puis je filtre les propositions trop proches de réponses existantes pour éviter les doublons.
Le résultat, à droite, c'est une proposition complète : le texte, une catégorie — ici « exemplaire » — les scores obtenus, et surtout une justification. Et rien n'est inséré automatiquement : l'auteur relit, puis accepte ou rejette. C'est le human-in-the-loop.`,

// Slide 11 — Scoring assisté (~70 s)
`Ma seconde fonctionnalité IA, c'est le scoring assisté. Le module ne sert pas qu'à créer : il sait aussi évaluer.
En entrée, on lui donne le texte d'une réponse — existante ou fraîchement proposée — avec son contexte narratif. Le traitement est similaire : je construis un prompt, j'appelle le LLM, et j'obtiens en sortie un JSON structuré : un vecteur de sept scores plus une justification.
À droite, vous voyez ce vecteur sur les sept dimensions, chacune positionnée sur l'échelle de moins trois à plus trois. L'intérêt majeur, c'est la justification textuelle, en bas : elle explique pourquoi tel score a été attribué, ce qui rend l'évaluation transparente pour le formateur.
Là encore, l'auteur garde la main : il accepte, corrige ou rejette le score proposé. Et cette fonctionnalité, je l'ai validée sur le terrain — j'y reviens dans les résultats — avec une erreur absolue moyenne de 0,77 par rapport aux scores humains.`,

// Slide 12 — Démo live (~90 s, variable selon la démo)
`Plutôt que de vous décrire l'outil, je vous propose maintenant une démonstration en direct.
Je vais d'abord charger un livre pédagogique et vous montrer le scénario sous forme de graphe : on voit immédiatement les embranchements et les fins de branche. Ensuite, je sélectionne une interaction et j'édite une réponse, en ajustant les curseurs de soft skills. Puis je lance la génération assistée par l'IA : vous verrez les propositions arriver avec leurs scores et leur justification — et c'est moi qui valide ou rejette, c'est le principe du human-in-the-loop. Enfin, je bascule en mode parcours joueur pour suivre une branche et observer les scores cumulés, le tout sans relancer Unity.
[Si la démo live échoue, j'ai des captures d'écran de secours.] Revenons maintenant aux résultats chiffrés de ces fonctionnalités.`,

// Slide 11 — Résultats génération (~60 s)
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
