# Journal de développement — PA 26 « End of Life »

> **Objet.** Trace écrite de toutes les améliorations, modifications et développements réalisés
> sur le projet, pour servir de matière première à la rédaction du rapport et du mémoire.
>
> **Période couverte : depuis le 18 septembre 2026.** Du 18 septembre au 5 octobre, le journal a
> été reconstitué après coup, le 6 octobre. Depuis, il est tenu au fil du travail (§ 2.19).
>
> **Sources.** Ce journal a été reconstitué à partir de trois sources :
> - les 6 sessions de travail menées avec l'assistant de développement (Claude Code), relues en entier ;
> - les dates de modification des fichiers du projet ;
> - l'état actuel du code, dont la suite de tests (94 tests, tous verts le 6 octobre).
>
> **Attention : aucun commit git depuis le 6 mai 2026.** Tout le travail décrit ici est dans
> l'arbre de travail, non versionné. L'historique git ne permet donc pas de le retrouver : ce
> journal est pour l'instant la seule trace datée.

---

## Sommaire

0. [Comment utiliser ce journal](#0-comment-utiliser-ce-journal)
1. [Vue d'ensemble](#1-vue-densemble)
2. [Chronologie détaillée](#2-chronologie-détaillée)
3. [Architecture technique au 6 octobre 2026](#3-architecture-technique-au-6-octobre-2026)
4. [Décisions de conception et justifications](#4-décisions-de-conception-et-justifications)
5. [Validation et tests](#5-validation-et-tests)
6. [Problèmes rencontrés et corrections](#6-problèmes-rencontrés-et-corrections)
7. [Limites connues et travail restant](#7-limites-connues-et-travail-restant)
8. [Pistes pour la rédaction du mémoire](#8-pistes-pour-la-rédaction-du-mémoire)
9. [Annexes](#9-annexes)

---

## 0. Comment utiliser ce journal

Chaque entrée de la chronologie (§ 2) suit le même plan :

- **Besoin** : ce qui était demandé, et pourquoi.
- **Réalisation** : ce qui a été fait.
- **Choix et justifications** : les décisions prises, avec leurs raisons.
- **Résultats** : les chiffres et les livrables.
- **Vérification** : comment le résultat a été contrôlé.
- **Limites** : ce qui reste ouvert.
- **Fichiers** : où retrouver le travail dans le projet.

Les sections 4 à 8 regroupent ensuite ces informations par thème. Elles correspondent aux
chapitres habituels d'un mémoire : conception, validation, discussion, limites et perspectives.

**Pour la suite du projet :** chaque développement ou modification donne lieu à une entrée datée à
la fin du § 2, et les § 5 et 7 sont mis à jour. Depuis le 6 octobre, c'est automatique : un hook
Claude Code bloque la fin d'une réponse tant que le journal n'a pas été complété (§ 2.19).

---

## 1. Vue d'ensemble

### 1.1 En une phrase par semaine

| Semaine | Thème | Principaux livrables |
|---|---|---|
| **18 → 23 sept.** | Nouvelle mission : des livres pour les étudiant·e·s en médecine. Analyse des programmes de trois facultés. | 18 plans d'études officiels · indices de divergence entre facultés · plan de 6 livres · livre 4 v1 (217 interactions) · parcours joueur séparé de l'éditeur · support de présentation pour le professeur |
| **24 → 27 sept.** | Narration ambitieuse et suivi des joueur·euse·s | Livre 4 v2 (6 chapitres, erreur médicale et ses conséquences) · moteur d'« états narratifs » · 4 à 6 réponses par choix · tableaux comparatifs des matières · comptes, historique, note pondérée, feedback IA · données de démonstration |
| **28 sept. → 5 oct.** | Qualité, contenu et données | Palette d'interface tirée des trois universités · refonte ergonomique · diagnostic d'un bug de perte de données dans l'éditeur · livre 2 v2 « Le corps donné » (43 scènes) · export Excel/CSV/JSON · recherche bibliographique et plan de scoring v2 |
| **6 oct. →** | Un scoring fondé sur la recherche | Journal de développement · scoring v2, étape 1 : note par choix (100 atteignable, ≈ 50 au hasard), passage de chapitre comme unité de note, niveau, progression et fiabilité par chapitre |

### 1.2 Avant / après en chiffres

**Contenu des livres**

| Livre | Avant (mi-septembre) | Après (5 octobre) |
|---|---|---|
| `end_of_life` (référence historique) | 5 ch. · 17 scènes · 416 interactions · 1 378 réponses | inchangé |
| `medstudents_y2` (livre 2) | v1 pilote : 3 ch. · 4 scènes · 22 interactions · 51 réponses | **v2 « Le corps donné » : 6 ch. · 43 scènes · 463 interactions · 1 812 réponses** |
| `medstudents_y4` (livre 4) | n'existait pas | v1 (18 sept.) : 4 ch. · 12 scènes · 217 interactions · 577 réponses → **v2 (27 sept.) : 6 ch. · 42 scènes · 576 interactions · 2 446 réponses** |

**Application**

| Indicateur | Avant | Après |
|---|---|---|
| Tests automatisés | 29 | **110** (tous verts au 6 octobre) |
| Comptes utilisateur | aucun | participant·e / formateur·rice, mots de passe hachés |
| Suivi des joueur·euse·s | aucun | sessions et passages de chapitre en base de données, niveau et progression par chapitre, bilan avec feedback IA |
| Interface joueur | panneau « Parcours joueur » dans l'éditeur | pages `/play/…` dédiées, plein écran |
| Export de données | aucun | Excel, CSV, JSON, avec pseudonymisation |
| Identité visuelle | thème sombre à dégradés violets | thème clair tiré des couleurs UNIL, UNIGE et UZH |

**Volume de code.** Environ 20 600 lignes dans les fichiers créés ou réécrits pendant la période.
Environ 12 500 d'entre elles sont du contenu narratif écrit dans un mini-langage Python (§ 4.3).
Le reste, environ 8 000 lignes, se partage entre l'application, l'outillage et les tests.

---

## 2. Chronologie détaillée

Les heures sont en heure suisse.

### 2.1 — 18 sept. · Collecte des plans d'études des trois facultés

- **Besoin.** Récupérer le programme le plus détaillé possible du Bachelor (années 1 à 3) et du
  Master de médecine à l'UNIL, l'UNIGE et l'UZH.
- **Réalisation.**
  - 18 PDF officiels téléchargés depuis les sites des facultés (plans d'études 2025-2026 et
    2026-2027), puis leur texte extrait.
  - Synthèse année par année : modules, ECTS, heures ou leçons.
- **Constat de départ.** En Suisse, le Master de médecine dure **3 ans**, pas 2. Le cursus fait
  donc 3 + 3 = 6 ans partout, et le plan couvre M1 à M3.
- **Granularité inégale des sources**, une limite méthodologique à citer dans le mémoire :

  | Faculté | Documents | Niveau de détail |
  |---|---|---|
  | UNIL | 6 plans d'études B1 → M3 | module → cours → **heures** → responsable → ECTS |
  | UZH | 7 *Infobroschüren* (années 1 à 6) | module → *Themenblock* → **leçons** → ECTS |
  | UNIGE | plans réglementaires B et M + contenus B1 | unités et modalités ; **le détail de B2-B3 n'est pas public** (Moodle interne) |

- **Observation utile pour le sujet.** L'UNIGE est la seule faculté à nommer explicitement
  l'autonomie en fin de vie et la demande d'aide à mourir dès la 1ʳᵉ année (module PSS). À l'UNIL,
  les soins palliatifs apparaissent en M2.2 et en option B3.9. À l'UZH, ils ne forment pas un
  bloc identifiable : ils sont répartis dans le cluster longitudinal *Altersmedizin*.
- **Fichiers.**
  - [docs/programmes_medecine/](programmes_medecine/) : 18 PDF dans `UNIL/`, `UNIGE/` et `UZH/` ;
  - [SOURCES.md](programmes_medecine/SOURCES.md) : l'URL d'origine de chaque PDF.

### 2.2 — 18 sept. · Analyse comparative : quantifier la divergence entre programmes

- **Besoin.** Savoir si les programmes divergent beaucoup, de combien en pourcentage, et sur quoi.
- **Méthode.** Elle a été construite pour éviter un chiffre « au doigt mouillé » :
  1. **Axe chronologique.** 61 domaines d'enseignement ont été codés. Pour chacun, on relève
     l'année où il apparaît dans chaque faculté, puis on compte, par paire, les domaines
     enseignés la même année, à un an près, ou avec deux ans d'écart ou plus.
  2. **Axe structurel.** Les 360 ECTS de chaque cursus sont répartis en 7 catégories. La
     distance entre deux facultés est la part du cursus qu'il faudrait réorganiser pour passer
     de l'une à l'autre.
  3. **Sous-ensemble pertinent.** Le même calcul est refait sur les 15 domaines que le jeu
     mobilise : communication, éthique, secret médical, soins palliatifs, etc.
- **Résultats, axe chronologique (61 domaines).**

  | Paire | Même année | À ±1 an | Écart ≥ 2 ans |
  |---|---|---|---|
  | UNIL ↔ UZH | 57,4 % | 88,5 % | 11,5 % |
  | UNIL ↔ UNIGE | 37,7 % | 90,2 % | 9,8 % |
  | UNIGE ↔ UZH | 32,8 % | 90,2 % | 9,8 % |
  | **Les trois** | **21 %** | **79 %** | **21 %** |

- **Résultats, axe structurel (part des 360 ECTS).**

  | Catégorie | UNIL | UNIGE | UZH |
  |---|---|---|---|
  | Sciences fondamentales | 30,1 % | 24,7 % | 29,4 % |
  | Clinique enseignée | 21,5 % | 12,4 % | 25,0 % |
  | Immersion clinique à plein temps | 20,4 % | 44,1 % | 15,0 % |
  | Compétences cliniques / simulation | 12,7 % | 5,9 % | 13,1 % |
  | SHS / santé publique / éthique / droit | 7,7 % | 5,6 % | 5,8 % |
  | Recherche / mémoire | 5,5 % | 4,0 % | 4,2 % |
  | Options libres | 1,9 % | 3,2 % | 7,5 % |

  Part du cursus à réorganiser pour passer d'une faculté à l'autre : UNIL → UZH **9,4 %**,
  UNIL → UNIGE **24,9 %**, UNIGE → UZH **29,1 %**.
- **Conclusion.** **Le contenu converge, la chronologie et la pédagogie divergent.** Les trois
  facultés préparent au même examen fédéral et suivent le même référentiel national
  (**PROFILES**) : aucune ne peut omettre un domaine. En revanche, rien ne leur impose l'ordre,
  la méthode ni la part d'immersion clinique.
- **Divergences majeures.**
  1. La part d'immersion clinique (voir la réserve du § 2.6 sur ce chiffre).
  2. La densité de la 1ʳᵉ année à l'UNIGE : toute la physiologie des systèmes d'organes y est
     enseignée dès l'année 1.
  3. L'inversion des neurosciences : année 2 à l'UNIL et à l'UZH, année 3 à l'UNIGE.
  4. 13 domaines sur 61 ont un écart de 2 ans ou plus, dont les **soins palliatifs** (UNIL
     année 5, UNIGE année 4, UZH année 3), c'est-à-dire le cœur du projet.
- **Limites, à citer telles quelles.**
  - Le codage des 61 domaines est un choix de l'auteur : c'est un indice, pas une statistique
    officielle.
  - L'UNIGE est la faculté la moins bien documentée publiquement, et aussi celle qui ressort
    comme la plus divergente : une partie de l'écart peut venir de cette différence de
    documentation.
  - Les ECTS sont classés selon leur catégorie dominante : marge d'erreur estimée à ±3 points.

### 2.3 — 18 sept. · Décision de périmètre : UNIL + UNIGE, Zurich différé

- **Besoin.** La nouvelle mission consiste à créer des livres pour les étudiant·e·s des trois
  facultés. La question posée : **un livre par année suffit-il pour les trois, ou la divergence
  est-elle trop forte ?**
- **Analyse à trois facultés.** Sur les 15 domaines du jeu, l'alignement est encore plus faible
  que sur le cursus complet : 13,3 % des domaines tombent la même année, et 33,3 % ont un écart
  de 2 ans ou plus. Un premier modèle proposait donc **3 livres par palier de compétence** au
  lieu de 6 livres par année.
- **Décision prise par l'étudiant : retirer l'UZH.** Recalcul sur la paire UNIL + UNIGE :

  | Indice (15 domaines du jeu) | Les 3 facultés | UNIL + UNIGE |
  |---|---|---|
  | Alignés à ±1 an | 66,7 % | **86,7 %** |
  | Écart ≥ 2 ans | 33,3 % | **13,3 %** |
  | Même palier de compétence | 60,0 % | 73,3 % |

  Il ne reste que deux domaines mal alignés, urgences-réanimation et économie de la santé. Aucun
  des deux n'est au cœur d'un jeu sur la fin de vie. Si on les retire, **les 13 autres domaines
  sont tous alignés à un an près**.
- **Contrefactuel complet, calculé le 22 sept.** Que se passe-t-il si on retire chacune des
  trois facultés ?

  | Faculté retirée | Paire gardée | Alignement ±1 an | Écart structurel | Domaines bloquants |
  |---|---|---|---|---|
  | UNIL | UNIGE + UZH | 93,3 % | 29,1 % | 1 (droit médical) |
  | **UZH** | **UNIL + UNIGE** | **86,7 %** | **24,9 %** | **2 (urgences, économie)** |
  | UNIGE | UNIL + UZH | 66,7 % | 9,4 % | 5, dont soins palliatifs |

- **Justification honnête, à reprendre dans le mémoire.**
  - **La raison décisive est la langue.** L'UZH enseigne en allemand. Il ne s'agirait pas de
    traduire les livres mais de les **localiser** : personnages, institutions, système de santé
    cantonal, cadre juridique.
  - **Les données curriculaires seules n'auraient pas désigné Zurich.** L'UZH est la faculté la
    plus proche de l'UNIL sur la structure. C'est donc une **décision de faisabilité, validée a
    posteriori** par les chiffres : ils montrent qu'elle coûte peu.
  - La paire UNIL + UNIGE n'est jamais la pire : elle arrive 2ᵉ sur les deux critères.
  - **Zurich est différé, pas abandonné.**
- **Conséquence de conception.** UNIL et UNIGE restent la paire la plus éloignée sur la
  structure. À année égale, un·e étudiant·e genevois·e a beaucoup plus de contact avec des
  patient·e·s. Recommandation : **calibrer l'autonomie du joueur sur l'UNIL**.

### 2.4 — 18 sept. · Plan des six livres (un par année, UNIL + UNIGE)

- **Principe directeur.** Un protagoniste unique, **Alex**, suivi de la 1ʳᵉ à la 6ᵉ année. La
  progression narrative est la progression pédagogique. Chaque livre est placé là où
  l'étudiant·e a **déjà vu le contenu en cours** : le jeu renforce, il n'anticipe jamais.

| # | Livre | UNIL | UNIGE | Compétences dominantes |
|---|---|---|---|---|
| 1 | Avant la blouse | B1 | B1 | Respect, empathie |
| 2 | Le premier contact | B2 | B2 | Clarté, limites professionnelles |
| 3 | Au lit du malade | B3 | B3 → M1 ⚠️ | Clarté, respect |
| 4 | La mauvaise nouvelle | M1 | M1 | Compassion, régulation émotionnelle |
| 5 | Fin de vie ★ | M2 | M2 | les 7 |
| 6 | Porter la responsabilité | M3 | M3 | Régulation, limites, interprofessionnalité |

- ⚠️ Seul décalage réel : l'UNIL a 77,5 h au lit du malade en B3, alors que Genève ne bascule
  en clinique qu'en M1.
- **Restent spécifiques à chaque faculté :** le droit médical et le cadre légal, l'organisation
  du système de santé, et les dispositifs institutionnels de fin de vie.
- **Extension proposée du modèle `Book`** : champs `lang`, `year` et `curriculum_map`. Elle n'a
  pas été implémentée à ce jour.
- **Chemin critique identifié dès ce stade : les images.** Il faudra environ 250 à 300 portraits
  pour les 6 livres. Piste retenue : un **casting récurrent**, avec les mêmes personnages d'un
  livre à l'autre.

### 2.5 — 18 sept. · Livre 4 v1 « La mauvaise nouvelle » (M1)

- **Besoin.** Créer le livre 4 de manière complète, intégré à l'interface, en s'inspirant du
  format JSON existant.
- **Première livraison** : 4 chapitres, 9 scènes, 67 interactions. **L'étudiant l'a refusée** :
  le plan annonçait environ 200 interactions, et les scénarios étaient trop courts. Leçon de
  méthode : le volume avait été réduit en cours de route sans le signaler.
- **Version livrée le soir même** : 4 chapitres, 12 scènes, **217 interactions, 577 réponses**,
  13 personnages, environ 4 h de jeu.

  | Ch. | Titre | Situation | Ancrage M1 |
  |---|---|---|---|
  | 1 | Les mots qu'on n'a pas appris | M. Ferreira, 58 ans, cancer du poumon métastatique, puis la reprise le lendemain | UNIL M1.6-M1.7 · UNIGE AMC médecine interne et palliative |
  | 2 | Et si on ne disait rien ? | Mme Haddad, 74 ans ; sa fille Sofia exige le silence | UNIL M1.7 éthique de la décision · UNIGE médecine légale et éthique |
  | 3 | Le doute | Yann, céphalées et bilan normal ; Malick, dépistage VIH réactif non confirmé | UNIL M1.5-M1.6 tests diagnostiques |
  | 4 | L'enfant | Échographie de 22 SA ; Lina, 9 ans, diabète de type 1 | UNIL M1.2 Mère-enfant · UNIGE AMC gynéco et pédiatrie |

- **Principes de conception.**
  - Échelle de score −3 à +3 sur 7 compétences : **299 réponses sur 577 sont pénalisées** sur
    au moins une compétence.
  - Des **branches de rattrapage**, qui ramènent le joueur vers le bon geste.
  - Une infirmière récurrente porte la collaboration interprofessionnelle, la compétence la
    plus faible du pilote.
  - Une **nuance éthique** : le chapitre 2 récompense de *demander à la patiente ce qu'elle veut
    savoir*, pas de « tout dire ».
- **Exemples démonstratifs.**
  - Face au silence après l'annonce, la meilleure réponse est de **ne rien dire** (+14). « Je
    comprends ce que vous ressentez » coûte des points (−3).
  - Face à Sofia, les deux mauvaises réponses échouent dans des **directions opposées** : céder
    (−7) ou asséner le droit (−5). Le bon geste est un troisième chemin (+12).
- **Vérification.** Validation des liens (règle EG-7) : 0 erreur. Aller-retour modèle ↔ JSON
  identique, 0 interaction inatteignable, 29 tests verts, routes HTTP contrôlées.
- **Fichiers.**
  - [data/chapters/MedStudents_Y4_v1.json](../data/chapters/MedStudents_Y4_v1.json) : le livre ;
  - [docs/MedStudents_Y4_assets.md](MedStudents_Y4_assets.md) : les 72 images à produire ;
  - entrée `medstudents_y4` dans `books.py`.
- **Au passage.**
  - L'avertissement `vis.js` (`Invalid type received for "bold"`) existait déjà avant ce travail.
  - `.claude/launch.json` a été corrigé pour utiliser `.venv/bin/python`.

### 2.6 — 22-23 sept. · Préparer le point avec le professeur

- **Livrables.**
  - Un brief de présentation en 5 temps : fichiers trouvés, méthode de comparaison, ce qu'on a
    compris, déduit et retiré, plan des livres, livre 4.
  - Les questions probables du professeur, avec des réponses préparées.
  - Un **deck de 11 diapositives**, simplifié ensuite à **7 à la demande de l'étudiant**. C'est
    une page privée sur claude.ai : « Livres MedStudents — point hebdo ».
- **Correction importante du chiffre « immersion clinique » (23 sept.).** L'écart de 29 points
  dépend d'un choix de codage : les AMC genevois ont été comptés à 100 % comme de l'immersion,
  alors qu'ils comprennent des activités structurées le lundi et le vendredi. Analyse de
  sensibilité :

  | Hypothèse sur les AMC | UNIL | UNIGE | UZH | Écart |
  |---|---|---|---|---|
  | enseignement (0 %) | 20,6 % | 18,3 % | 15,0 % | 5,6 pts |
  | 3 jours cliniques sur 5 (60 %) | 20,6 % | 32,7 % | 15,0 % | **17,7 pts** |
  | immersion (100 %), le codage initial | 20,6 % | 42,2 % | 15,0 % | 27,2 pts |

  → **Annoncer environ 17 points, pas 29.** Le classement UNIGE > UNIL > UZH reste vrai quelle
  que soit l'hypothèse.
- **Version vulgarisée de la méthode**, pour un public non expert. L'image retenue : « trois
  trains vers la même gare terminus, mêmes arrêts obligatoires, mais pas dans le même ordre ».

### 2.7 — 22 sept. · Parcours joueur séparé de l'éditeur

- **Besoin.** Une page « parcours joueur » à part de l'interface d'édition, pour que les
  étudiant·e·s y accèdent directement, plus agréable et plus proche d'un jeu.
- **Réalisation.**
  - Nouvelles routes : `/play/<livre>/` pour le sommaire en cartes, `/play/<livre>/chapters/<id>`
    pour le jeu en plein écran.
  - Déroulé : intro du chapitre → intro de la scène → dialogue avec texte progressif → bilan de
    scène → bilan de chapitre.
  - Raccourcis clavier : 1 à 9 pour choisir une réponse, Entrée pour avancer.
- **Choix de conception.**
  1. **Les scores sont cachés pendant le jeu et révélés au bilan**, pour que l'étudiant·e
     raisonne cliniquement au lieu d'optimiser un score. Le bilan montre les 7 compétences en
     barres divergentes.
  2. **Portraits manquants** : un bloc avec les initiales du personnage remplace l'image. Le jeu
     reste jouable sans les images.
  3. **L'intro du chapitre est coupée en deux.** Le joueur ne voit que la mise en situation ;
     les objectifs pédagogiques et l'ancrage dans le cursus sont repliés.
  4. **Une seule définition des 7 compétences**, partagée par l'éditeur et le jeu, dans
     `static/shared/skills.js`.
- **Fichiers.** `templates/play*.html.jinja`, `static/play/engine.js`, `static/play/main.js`,
  `static/play.css`, `static/shared/skills.js`.

### 2.8 — 24-27 sept. · Livre 4 v2 : narration continue, entourage, erreur médicale

- **Besoin.**
  - Un storytelling qui marque, avec tout l'entourage : collègues, infirmières, famille, chef.
  - 5 ou 6 chapitres de 5 ou 6 scènes, avec des choix très bons, moyens et très mauvais.
  - Un scénario d'**erreur médicale grave**, avec des conséquences qui continuent : la famille,
    l'avocat.
  - La **répartition des soft skills** par chapitre et par scène.
- **Réalisation : une histoire continue.** Six semaines de stage d'Alex dans le même service de
  médecine interne. La v1 est conservée à côté.
  - **Entourage récurrent** : le chef (Dr Moreau), un assistant épuisé, l'infirmière référente,
    l'infirmier de nuit, une assistante en soins, un co-stagiaire. S'y ajoutent la responsable
    sécurité des patients, le juriste de l'hôpital, l'avocate de la famille et les familles des
    patients.
  - **Chapitres** :
    1. l'arrivée et la première annonce grave ;
    2. le pacte de silence ;
    3. annoncer sans diagnostic ;
    4. M. Ferreira revient pour mourir, avec le mariage de sa fille dans la chambre ;
    5. **« La nuit du 14 »** : une allergie à la pénicilline signalée par l'épouse du patient.
       Selon l'anamnèse, la relève et l'appel de 2 h 10, la perfusion est posée ou évitée. En cas
       d'erreur, le choc anaphylactique mène au décès, ou à la survie après 9 jours de
       réanimation ;
    6. **les conséquences** : entretien avec la famille, lettre de l'avocate, revue d'incident,
       audition. Sur la voie évitée : déclaration du quasi-accident, revue, erreur d'un
       collègue.
  - **Choix de crédibilité médicale** : la paralysie vient d'une faiblesse acquise en
    réanimation, pas d'une lésion définitive.
- **Innovation technique : le moteur d'« états narratifs ».** Un choix peut poser un état, qu'une
  scène plus loin, même dans un autre chapitre, lit pour changer. Les briques ajoutées au format
  et au moteur de jeu :

  | Brique | Rôle |
  |---|---|
  | `SetFlags` / `ClearFlags` (réponse) | poser ou retirer un état |
  | `Condition` (scène) | jouer la scène seulement si les états le permettent (all/any/none) |
  | `Slot` (scène) | deux versions d'une même scène, dont une seule est jouée |
  | `EntryPoints` (scène) | plusieurs débuts possibles selon les états |
  | `Debriefs` (scène) | un bilan narratif propre à l'issue |
  | `StartChoice` (chapitre) | une question de départ si le chapitre est joué sans les précédents |

  Exemples de mémoire des choix :
  - une phrase rassurante sur le mariage au chapitre 1 revient au chapitre 4 ;
  - une deuxième nuit de garde acceptée est évoquée par l'avocate au chapitre 6 ;
  - un dossier réécrit à 6 h 47 est trahi par l'historique.
- **Outillage d'écriture.**
  - Un **mini-langage Python (DSL)** pour écrire les scènes, plus lisible que le JSON.
  - Un **script de build** qui valide le livre (liens, atteignabilité, terminaison, cohérence
    des états, une seule scène jouable par emplacement, ordre de jeu), puis génère le JSON, le
    rapport des soft skills et la liste des images.
- **Résultats.** 6 chapitres, 42 scènes, 576 interactions, environ 5 h de jeu par parcours, 135
  portraits à produire. Répartition des points positifs disponibles, en % :

  | Ch. | Respect | Empathie | Compassion | Régulation | Clarté | Limites | Collab. |
  |---|---|---|---|---|---|---|---|
  | 1 | 21 | 16 | 8 | 10 | 20 | 12 | 11 |
  | 2 | 21 | 14 | 9 | 9 | 22 | 16 | 10 |
  | 3 | 17 | 10 | 7 | 10 | 28 | 21 | 6 |
  | 4 | 14 | 12 | 18 | 13 | 16 | 10 | 16 |
  | 5 | 8 | 4 | 4 | 11 | 24 | 28 | 22 |
  | 6 | 9 | 8 | 9 | 16 | 14 | 30 | 15 |

  Chaque chapitre contient des choix très bons (≥ +9) et très mauvais (≤ −7), ce qu'un test
  vérifie. 86 réponses ont été recalibrées pour respecter cette règle.
- **Bug corrigé.** Le cache navigateur de l'éditeur réappliquait un ancien chapitre (v1)
  par-dessus le nouveau (v2). Ce correctif s'est révélé insuffisant par la suite (§ 2.14).
- **Vérification.**
  - 44 puis 45 tests verts.
  - La voie « erreur » jouée de bout en bout dans le navigateur (chapitres 5 → 6).
  - L'écran de choix de départ et la voie « évitée » vérifiés.
- **Fichiers.**
  - `scripts/medstudents_y4_v2/` : DSL, distribution, chapitres 1 à 6 ;
  - `scripts/build_medstudents_y4_v2.py` : le build ;
  - [MedStudents_Y4_v2_bible.md](MedStudents_Y4_v2_bible.md) : la bible narrative ;
  - [MedStudents_Y4_v2_soft_skills.md](MedStudents_Y4_v2_soft_skills.md) : le rapport des soft
    skills ;
  - [MedStudents_Y4_v2_assets.md](MedStudents_Y4_v2_assets.md) : les images à produire.
- **Note (4 oct.).** L'étudiant a indiqué que le livre Y4 sera supprimé à terme. Il n'est donc
  plus maintenu.

### 2.9 — 27 sept. · Plus de trois réponses par choix, dans un ordre mélangé

- **Besoin.** Ne pas proposer seulement 3 réponses à chaque fois.
- **Réalisation.**
  - Chaque point de choix du livre 4 propose **4 à 6 réponses** : 359 interactions en ont 4,
    197 en ont 5, et 3 en ont 6. Le livre passe de 1 432 à **2 446 réponses**.
  - Les ajouts sont une option moyenne, une très mauvaise ou une autre bonne formulation. Ce
    peut être un geste non verbal : se taire, s'asseoir, tendre les mouchoirs.
  - **Ordre mélangé mais stable**, calculé à partir de l'identifiant de l'interaction. Avant, la
    meilleure réponse était souvent la première, et taper « 1 » suffisait presque.
  - Les nouvelles réponses posent les mêmes états narratifs que les réponses d'origine
    équivalentes.
- **Vérification.** 45 tests, dont un nouveau qui impose au moins 4 réponses par point de choix.

### 2.10 — 27 sept. · Tableaux comparatifs des matières (66 matières)

- **Besoin.** Un grand tableau donnant, pour chaque matière, l'année d'enseignement dans chaque
  université, et un tableau des matières communes à la même année.
- **Réalisation.**
  - Relecture complète des 18 PDF.
  - **66 matières** en 3 catégories : sciences de base ; systèmes et spécialités ; santé,
    société et profession.
- **Résultats.** 41 matières sont communes à la même année (51 lignes, certaines tombant la même
  année à plusieurs reprises) :

  | Année | B1 | B2 | B3 | M1 | M2 | M3 |
  |---|---|---|---|---|---|---|
  | Matières communes aux trois | 16 | 13 | 7 | 9 | 4 | 2 |

  - 16 matières sont enseignées partout, mais jamais la même année.
  - 9 matières sont absentes d'au moins un plan : chimie organique, droit médical et économie
    de la santé à l'UZH ; anesthésiologie et hygiène à l'UNIGE ; etc.
- **Page interactive.** Recherche insensible aux accents, filtre par catégorie, onglets. Un bug
  des filtres, signalé par l'étudiant, a été corrigé : les deux tableaux restaient affichés.
- **Fichiers.**
  - [COMPARATIF_MATIERES.md](programmes_medecine/COMPARATIF_MATIERES.md) ;
  - [comparatif_matieres.html](programmes_medecine/comparatif_matieres.html), qui s'ouvre sans
    serveur.
- ⚠️ **Deux codages différents coexistent** : 61 domaines (§ 2.2) et 66 matières (ce tableau).
  Dans le mémoire, il faut en retenir un, ou expliquer leur rôle respectif. Les 61 domaines
  servent aux indices de divergence, les 66 matières à la cartographie détaillée.

### 2.11 — 27 sept. · Comptes, historique des sessions, note pondérée et feedback IA

- **Besoin.**
  - Un compte par participant·e, avec l'historique de ses sessions et ses performances.
  - À la fin de chaque livre, un **feedback général** : points forts et faibles, conseils,
    chapitres à retravailler, avec un retour visuel.
  - Dès la 2ᵉ session, un feedback qui **tient compte des sessions précédentes**.
  - Un **score pondéré** selon le rang de la session : ×1, puis ×1,25, puis ×1,5…
- **Réalisation (architecture).**
  - **Base de données** avec SQLAlchemy : SQLite en local, PostgreSQL en production via
    `DATABASE_URL`, tables créées au démarrage. Trois tables : `users`, `book_sessions`,
    `scene_attempts`.
  - **Authentification** : inscription, connexion, mots de passe hachés, rôles participant·e et
    formateur·rice, commande `flask create-user`, **protection CSRF** sur toutes les requêtes
    qui modifient des données.
  - **Session de jeu** : un parcours complet d'un livre, reprenable sur plusieurs jours et
    plusieurs appareils. La progression passe du navigateur (`localStorage`) au serveur.
  - **Scoring v1** :
    - chaque compétence est notée sur 100 par rapport au pire et au meilleur total possibles
      depuis le point d'entrée ;
    - **seule la 1ʳᵉ tentative d'une scène compte** ; « Refaire » est de l'entraînement non
      noté ;
    - **le serveur rejoue les choix et recalcule les scores** : un participant ne peut pas
      falsifier sa note depuis le navigateur ;
    - **la note pondérée** donne un poids de 1 + 0,25 × (n − 1) à la n-ième session. Exemple :
      40, 60 et 75 donnent 60,7.
  - **Feedback IA** :
    - synthèse, points forts et faibles, conseils, chapitres à retravailler avec un lien ;
    - dès la 2ᵉ session, l'IA reçoit les scores et les conseils précédents ;
    - **aucun nom ni identifiant n'est envoyé à l'IA** ;
    - **version de secours par règles** si l'IA ne répond pas ;
    - backends OpenAI ou Ollama.
  - **Retour visuel** :
    - des **barres triées plutôt qu'un radar**, plus faciles à comparer, avec un repère pour la
      session précédente ;
    - une heatmap chapitres × compétences ;
    - les moments clés : la réponse donnée face à une réponse mieux ajustée ;
    - la courbe d'évolution.
  - **Pages** :
    - `/me` : « Mon parcours » ;
    - `/sessions/<id>` : le bilan d'une session ;
    - `/trainer/` : l'espace formateur, avec tous les participants, leurs bilans et la
      réinitialisation d'un mot de passe.
- **Changements de comportement.**
  - Le jeu exige une connexion.
  - L'éditeur, `/api/save` et `/api/enrich` sont réservés aux formateur·rice·s.
- **Vérification.**
  - 78 tests verts (33 nouveaux).
  - Parties réellement jouées dans le navigateur sur une base jetable.
  - CSRF vérifié : sans jeton, la requête est bloquée.
- **Mesure initiale.** Répondre au hasard donne environ 45/100, et le meilleur choix à chaque
  étape environ 85-90/100. Une mesure plus rigoureuse, au § 2.17, a révélé les limites de ce
  scoring.
- **Limites déclarées.**
  - Feedback IA **non testé avec un vrai modèle** : pas de clé API pendant le développement.
  - Pas de réinitialisation du mot de passe par e-mail.
  - Pas de limite sur les tentatives de connexion.
  - Pas d'outil de migration de la base (Alembic).
  - Pas de suppression de compte à la demande (RGPD).
- **Fichiers.**
  - `repositories/` : `database.py`, `orm.py`, `users.py`, `sessions.py` ;
  - `services/` : `scoring_service.py`, `session_service.py`, `history_service.py`,
    `auth_service.py`, `feedback/` ;
  - `views/` : `auth.py`, `guards.py`, `session_api.py`, `account.py` ;
  - `static/account/` : `charts.js`, `report.js`, `history.js` ;
  - le README, avec les sections « Comptes, sessions et feedback » et « Base de données ».

### 2.12 — 27 sept. · Données de démonstration

- Script `scripts/seed_demo.py`. Il crée un compte formateur et 6 participant·e·s fictif·ve·s,
  avec des profils variés : progression, régression, profil fort ou faible selon les
  compétences, sessions en cours. Leurs sessions du livre 4 passent par la vraie API du jeu, et
  les dates sont étalées du 24 août au 27 septembre.
- Le mot de passe des comptes de démonstration est dans `instance/demo_credentials.txt`, non
  versionné.
- **Limite.** Toutes les sessions ont pris la branche « évitée » au chapitre 5 : la branche
  « erreur » n'est pas représentée dans les données de démonstration.

### 2.13 — 1ᵉʳ oct. · Identité visuelle tirée des trois universités

- **Besoin.** Les couleurs de l'interface faisaient « trop IA ». Il fallait une palette tirée des
  trois universités, avec une couleur commune aux trois.
- **Méthode.** Extraction des couleurs dans les feuilles de style officielles des sites des
  facultés de médecine, puis analyse en HSL et OKLCH.

  | Université | Couleur principale | Autres |
  |---|---|---|
  | UNIGE | framboise `#D80669` | Faculté de médecine `#9A0050`, bleu `#046FCB`, ardoise `#425878` |
  | UNIL | bleu `#0037EB` | foncé `#002664`, gris bleutés |
  | UZH | bleu `#0028A5` | bleu sourd `#1B214A`, vert, rouge, orange |

- **Palette retenue.** Le bleu est la couleur commune : l'UNIL et l'UZH ont exactement la même
  teinte, seule la clarté change.
  - **Bleu commun `#0040BB`** pour l'action, **marine `#11254B`** pour les titres.
  - **Bordeaux UNIGE `#9A0050`** comme deuxième couleur, discrète.
  - Le vert, le rouge et l'orange de l'UZH pour les statuts.
  - Passage au **thème clair**, plus aucun dégradé ni halo.
  - Contraste des textes d'au moins 4,5:1 (norme WCAG AA).
  - Tout est centralisé dans `static/shared/theme.css`.

### 2.14 — 1ᵉʳ oct. · Revue ergonomique et refonte de la mise en page

- **Diagnostic** sur un écran de 1 366 px de large, puis tout a été corrigé :
  - **Bug du « Profil pondéré »** : la zone des barres faisait 23 px de large. Le graphique passe
    en pleine largeur et la zone fait maintenant 538 px.
  - **Éditeur** :
    - le graphe passe d'environ 400 px à 560 px ;
    - les scores sont repliés en pastilles avec des libellés français, au lieu de la grille de 7
      compétences aux noms anglais ;
    - les codes internes EG-3, EG-4 et EG-7 sont remplacés par des messages clairs ;
    - les zones de texte utilisent la même police que le reste de l'interface.
  - **Accueil** :
    - les cartes sont alignées et les descriptions limitées à 4 lignes ;
    - les chiffres sont des durées de jeu (2 h 30, 32 min, 5 h) au lieu de nombres
      d'interactions ;
    - le texte s'adresse aux étudiant·e·s, et le pied de page technique a été retiré.
  - **« Mon parcours » vide** : un message et un bouton « Commencer » remplacent 4 tuiles vides.
  - **Jeu** : un personnage sans portrait apparaît en petit avatar rond, au lieu d'un cadre de
    260 × 340 px contenant une seule lettre.
  - La légende de la heatmap a été corrigée, puisque l'échelle de couleurs avait été inversée.
- **Découverte d'un bug grave : perte de données dans l'éditeur.** L'éditeur affichait un ancien
  brouillon du navigateur au lieu du fichier :
  - chapitre 1 : 231 réponses dans le brouillon, 395 dans le fichier ;
  - chapitre 5 : 261 réponses dans le brouillon, 464 dans le fichier.

  Un clic sur « Sauvegarder » aurait écrasé le livre avec la vieille version. → Voir § 2.15.

### 2.15 — 1ᵉʳ-4 oct. · Correctif des brouillons de l'éditeur (préparé, non appliqué)

- **Correctif conçu dans une session séparée.**
  1. Le serveur calcule une **empreinte du contenu de chaque chapitre**. Un brouillon n'est
     réappliqué que si son empreinte correspond à celle du chapitre actuel.
  2. Les anciens caches ne sont plus jamais réappliqués.
  3. Un bandeau non bloquant propose de télécharger le brouillon écarté.
  4. Aucun brouillon n'est effacé sans l'accord de l'utilisateur.
  5. `/api/save` répond 409 si le chapitre a changé sur le serveur entre-temps.
- **Vérification.** Contrôle de syntaxe, 11 scénarios dans un banc d'essai Node avec les vraies
  données, `git apply --check` réussi.
- ⚠️ **Statut au 6 octobre : non appliqué, et le patch est perdu.** Il se trouvait dans un dossier
  temporaire qui a été effacé. Le code actuel n'a ni empreinte de chapitre ni bandeau.
  **Le risque d'écrasement existe donc toujours** : il faut refaire ce correctif.

### 2.16 — 4 oct. · Livre 2 v2 « Le corps donné » (2ᵉ année)

- **Besoin.**
  - Refaire tout le livre 2 à partir du programme de 2ᵉ année des trois universités.
  - Au moins 6 chapitres de 4 scénarios longs ou plus.
  - Des scénarios **non linéaires**, avec des branches parallèles et des histoires annexes.
  - Un **fil rouge**.
  - D'abord un plan et un schéma.
- **Analyse des programmes de 2ᵉ année.**
  - Les trois facultés enseignent le corps sain, système par système.
  - On y retrouve partout trois lieux : la salle de dissection, le centre de simulation avec des
    patients standardisés, et un premier contact avec la médecine de famille.
  - En 2ᵉ année, l'étudiant·e ne soigne pas encore. Le drame naît de l'écart entre ce qu'Alex
    sait et ce que son entourage lui demande.
  - Chaque chapitre suit le module du moment : le cœur en décembre, le rein en avril.
- **Le fil rouge.**
  - Le lundi, en dissection, « Madame 14 » : une donneuse anonyme, une hirondelle tatouée au
    poignet.
  - Le jeudi, au cabinet de Montchéry, Jeannine, 81 ans, ancienne sage-femme. Elle a donné son
    corps à la faculté sans le dire à son fils.
  - Pendant qu'Alex apprend le corps sain, celui de Jeannine lâche, organe par organe.
  - En juin, elle meurt, et Alex prend la parole à la cérémonie d'hommage aux donneurs.
  - Question transversale : **« qu'est-ce qu'on doit à un corps ? »**

| Ch. | Titre (période) | Branche parallèle | Histoire annexe | Matières exercées |
|---|---|---|---|---|
| 1 | Madame 14 (sept.) | la story circule ou non | Noah, 2 h 14 | anatomie (dissection), anamnèse, médecine de famille |
| 2 | Deux Pittet (oct.-nov.) | mauvais Pittet appelé ou non | Léo, isolé | immunité (vaccins), secret médical, APP, plagiat et IA |
| 3 | Le cœur, en vrai (déc.-janv.) | le père : 144 appelé ou non | Yasmine, ex-ambulancière | cœur et circulation, BLS, auscultation |
| 4 | Hors script (févr.-mars) | AVC du patient simulé reconnu à temps ou non | — | neurosciences, examen neurologique, facteurs humains |
| 5 | Ce que le village sait (avril) | appel de 23 h ou chute la nuit | le père refume | nutrition, rein, mineure capable de discernement |
| 6 | Le corps donné (juin, sept.) | famille apaisée ou déchirée | — | reproduction, soins palliatifs à domicile, hommage aux donneurs |

- **Résultats.**
  - **43 scènes écrites**, dont 6 branches parallèles et 4 annexes ; un parcours en joue 33 à 37.
  - **463 interactions, 1 812 réponses**, 4 à 6 réponses par choix.
  - Une validation du build sans aucune erreur ni aucun avertissement.
- **Les conséquences portent jusqu'à la fin.**
  - La **lettre de Jeannine** existe en six versions, selon les fautes ou les bons gestes d'Alex
    pendant l'année.
  - Le destin des personnages varie : Noah revient ou quitte la médecine, Bernard récupère ou
    reste aphasique, Océane remercie Alex ou l'évite.
  - À la cérémonie, Alex peut prononcer le nom de Jeannine, ce qui briserait l'anonymat qu'elle
    avait choisi.
- **Sujets sensibles, validés par l'étudiant avant l'écriture.**
  - **Crise suicidaire** : on pose la question directement et on oriente vers le 143 ou le 144.
  - **Grossesse d'une mineure de 17 ans** : le secret médical lui est dû, car elle est capable de
    discernement.
  - Repères juridiques suisses : art. 321 CP (secret médical), art. 370 ss CC (directives
    anticipées).
- **Évolutions de l'outillage.** Le livre 2 a son propre outillage, indépendant du Y4 à la
  demande de l'étudiant.
  - Nouvelle brique `Annex` : une histoire annexe débloquée par un état.
  - Validation `OUTCOMES` : chaque parcours complet d'une scène clé pose exactement un état de
    son groupe.
  - Validation des emplacements sur **toutes les combinaisons d'états**, en écartant les
    combinaisons impossibles (`MUTEX`).
- **Trois corrections du moteur de jeu**, utiles à tous les livres :
  1. le texte final d'une scène était sauté avant le bilan ;
  2. le compteur « Scénario x sur y » comptait les annexes non débloquées ;
  3. la touche Entrée valide maintenant un bouton « Continuer » seul.
- **Vérification.**
  - 89 tests verts.
  - **Chapitre 1 joué en entier dans le navigateur**, par un bon chemin et plusieurs mauvais.
  - **Chapitres 2 à 6 non joués dans le navigateur** : ils sont vérifiés par la validation du
    build et une simulation du moteur (écrans de départ, ordre des scènes, versions de la
    lettre).
- **Fichiers.**
  - `scripts/medstudents_y2_v2/` et `scripts/build_medstudents_y2_v2.py` ;
  - [data/chapters/MedStudents_Y2_v2.json](../data/chapters/MedStudents_Y2_v2.json) ;
  - [MedStudents_Y2_v2_bible.md](MedStudents_Y2_v2_bible.md) : la bible, avec la carte globale,
    la table des états et les repères suisses ;
  - [MedStudents_Y2_v2_soft_skills.md](MedStudents_Y2_v2_soft_skills.md) ;
  - [MedStudents_Y2_v2_assets.md](MedStudents_Y2_v2_assets.md) : 139 portraits à produire.
- **Écart connu** : la bible place Bernard et Noah à la cérémonie, mais le texte ne les y met pas.

### 2.17 — 5 oct. · Export des données brutes (Excel, CSV, JSON)

- **Besoin.** Rendre les données disponibles sous forme brute, pour les analyser dans Excel par
  exemple.
- **Réalisation.**
  - Un bloc « Données brutes » dans l'espace formateur et sur la fiche de chaque participant·e.
  - Un filtre par livre.
  - Trois formats : **Excel (.xlsx)**, **CSV (.zip)** et **JSON**.
  - Une option **« Pseudonymiser »** : les identifiants deviennent P001, P002…, avec un code
    stable d'un export à l'autre. Les dates restent : ce n'est pas une anonymisation complète.
  - Une feuille par table : `participants`, `sessions`, `chapitres`, `scenes`, `choix`, plus une
    feuille « lisez-moi » qui explique chaque colonne et le calcul des notes.
  - Dans la feuille `choix`, chaque ligne donne la réponse choisie, la meilleure réponse
    possible et l'écart entre les deux.
- **Choix et justifications.**
  - Le format .xlsx est recommandé pour Excel, car un CSV s'affiche différemment selon les
    réglages régionaux de l'ordinateur.
  - `reponse_no` suit l'ordre des réponses dans le livre, pas l'ordre affiché, qui est mélangé.
- **Vérification.**
  - 94 tests verts, dont 5 nouveaux.
  - Les trois formats ont été téléchargés depuis une base jetable.
  - La version pseudonymisée ne contient aucun nom.
- **Fichiers.** `services/export_service.py`, `exporters/tables.py`, `views/account.py`,
  `templates/_export_form.html.jinja`, et la dépendance `openpyxl`.

### 2.18 — 5 oct. · Recherche bibliographique et plan de scoring v2

- **Besoin.** Un scoring qui « tient la route », fondé sur la recherche et non sur des
  approximations. Il doit :
  - suivre la progression sur plusieurs sessions ;
  - être calculé **par chapitre**, pour qu'un·e étudiant·e puisse refaire quelques chapitres
    sans rejouer tout le livre.
- **Mesure du scoring actuel**, avec des joueur·euse·s simulé·e·s sur le livre Y2 :

  | Joueur·euse simulé·e | Note actuelle | Qualité des choix (proposée) |
  |---|---|---|
  | Au hasard | **48** (43-52) | 49 |
  | Moyen·ne | 64 | 74 |
  | Toujours la meilleure réponse | 80 | 100 |
  | Meilleur chemin possible | **83 (plafond)** | 100 |

  Ce que la mesure révèle :
  - il n'y a pas de zéro de référence ;
  - le plafond de 83 est inatteignable en pratique ;
  - les −3…+3 ont été écrits par l'auteur seul, sans grille ni validation ;
  - la note est liée à la session entière ;
  - certaines compétences sont peu mesurées par chapitre : la compassion ne repose que sur 5
    choix au chapitre 2.
- **Ce que dit la recherche.**
  - Les scènes du jeu sont des **tests de jugement situationnel (SJT)**.
  - La méthode de cotation change la fiabilité et la validité de la mesure.
  - La clé de cotation doit venir d'un **panel d'experts** (méthode Delphi), avec un accord
    mesuré.
  - Rejouer le même scénario **gonfle le score**, d'environ un tiers d'écart-type.
  - Les erreurs critiques doivent être traitées à part.
  - La validité d'une note se démontre avec le cadre de Kane.
- **Plan proposé, en 7 niveaux.**
  1. Une clé validée par des experts, avec une justification d'une phrase par réponse et un
     marqueur « critique ».
  2. Chaque choix noté par rapport aux réponses proposées à ce moment-là, sur une échelle de 0
     à 100 dont 100 est atteignable.
  3. **L'unité de note est le passage d'un chapitre.**
  4. Le suivi de chaque chapitre dans le temps avec trois indicateurs : niveau (pondéré
     1 + 0,25 × (n − 1)), progression normalisée et fiabilité.
  5. Un profil du livre qui est la moyenne des chapitres, avec un indicateur de couverture.
  6. Quatre niveaux (Insuffisant, À consolider, Compétent, Avancé). Une erreur critique empêche
     de dépasser « À consolider ».
  7. Une explication de chaque note.
- **Recommandation.** Ne pas ajouter de points pour le nombre de sessions : la note mesurerait
  alors l'assiduité plutôt que la compétence.
- **Statut.** **Proposition, non implémentée.** Cinq décisions sont en attente de l'étudiant :
  la pondération, le délai de 7 jours entre deux passages notés, le plafonnement en cas d'erreur
  critique, la composition du panel d'experts et le poids des chapitres.
- **Fichier.** [docs/Scoring_v2_recherche_et_plan.md](Scoring_v2_recherche_et_plan.md), avec 35
  références vérifiées une à une. Les 12 principales sont en annexe A.

### 2.19 — 6 oct. · Création du journal de développement et mise à jour automatique

- **Besoin.**
  - Garder une trace écrite de tout le développement, pour rédiger le rapport et le mémoire.
  - Ensuite : que **chaque développement ou modification futur** y soit inscrit.
- **Réalisation.**
  1. **Reconstitution des trois dernières semaines.** Lecture intégrale des 6 sessions de travail
     du 18 sept. au 5 oct., confrontée aux dates de modification des fichiers et à l'état du code
     (94 tests verts). Le résultat est ce journal.
  2. **Mise à jour automatique.** Un hook Claude Code de type « Stop » s'exécute chaque fois que
     l'assistant s'apprête à terminer une réponse. Si des fichiers du projet sont plus récents
     que le journal, il bloque la fin de la réponse et demande de compléter le journal d'abord.
- **Choix et justifications.**
  - **Un hook plutôt qu'une simple consigne.** Une consigne en mémoire peut être oubliée ; le
    hook rend le contrôle systématique.
  - **Le critère est la date de modification des fichiers**, et non l'historique git, car le
    travail n'est pas commité. Les modifications faites à la main en dehors de l'assistant sont
    aussi détectées, à la prochaine conversation.
  - **Fichiers exclus** : environnements Python, caches, base locale (`instance/`), réglages
    `.claude/` et archives automatiques des chapitres. Ils changent sans qu'il y ait de
    développement.
  - **Pas de boucle infinie** : le hook ne bloque qu'une fois de suite.
  - **Réglage personnel**, non versionné : il n'affecte pas d'autres contributeur·rice·s.
- **Vérification.** Le script a été testé sur un faux projet dans trois cas : fichier modifié →
  blocage avec la liste des fichiers ; second passage → pas de blocage ; journal à jour → pas de
  blocage. Il a ensuite été lancé sur le vrai projet, où il a détecté la modification de
  `.gitignore` de cette même séance.
- **Limites.**
  - Le hook se charge au démarrage d'une conversation : il est actif à partir de la prochaine.
  - Il ne vérifie pas la qualité de l'entrée écrite, seulement que le journal a été mis à jour.
- **Fichiers.**
  - `docs/Journal_de_developpement.md` : ce journal ;
  - `.claude/hooks/journal_check.sh` : le script de contrôle ;
  - `.claude/settings.local.json` : l'enregistrement du hook ;
  - `.gitignore` : exclusion de `.claude/settings.local.json`.

### 2.20 — 6 oct. · Scoring v2, étape 1 : note par choix, par chapitre et progression

- **Besoin.** Mettre en œuvre l'étape 1 du plan de scoring (§ 2.18), validée par l'étudiant
  (« go »), avec les réglages recommandés par défaut :
  - une note par **chapitre**, sans obliger à rejouer tout le livre ;
  - le suivi de la **progression** sur plusieurs passages.
- **Réalisation.**
  1. **Note par choix.** Chaque réponse est comparée aux réponses proposées au même moment.
     Qualité des choix = Σ (choisi − pire) / Σ (meilleur − pire) × 100 : 100 = la meilleure
     réponse à chaque fois, 0 = la pire, environ 50 au hasard. Cette note remplace les bornes de
     chemin du v1, qui donnaient 48/100 au hasard et plafonnaient à 83/100.
     - La note est aussi donnée **corrigée du hasard** : 0 = hasard.
     - Une compétence n'est notée que si **au moins 8 choix** la mettent en jeu.
     - Chaque pas de trace garde les bornes des réponses proposées, ce qui fige la note au
       moment du jeu.
  2. **Passage de chapitre**, nouvelle unité de note : un chapitre joué en entier, noté dès sa
     fin. Deux nouvelles tables, `chapter_passages` et `passage_attempts`, créées
     automatiquement. Les tables existantes ne sont pas modifiées : il n'y a toujours pas d'outil
     de migration.
  3. **Règle d'espacement.** Un passage compte s'il est le premier du chapitre, ou s'il commence
     au moins 7 jours après le dernier passage noté (`PASSAGE_SPACING_DAYS`). Sinon, c'est un
     passage d'entraînement, annoncé avant de jouer avec la date à partir de laquelle un passage
     comptera de nouveau.
  4. **Rejouer un chapitre seul.** Il repart des états narratifs du début de son dernier passage.
     Dans la session en cours, l'histoire continue normalement.
  5. **Niveau, progression, fiabilité par chapitre.**
     - Niveau : passages pondérés 1 + 0,25 × (n − 1).
     - Progression : changement normalisé de Marx & Cummings depuis le 1ᵉʳ passage.
     - Fiabilité : marge d'incertitude à 95 %, qui se resserre à chaque passage.
     - Note du livre : moyenne des chapitres évalués, avec la couverture.
  6. **Ordre des réponses** différent à chaque passage (jusqu'ici, toujours le même au rejeu).
  7. **Interfaces.**
     - Fin de chapitre : qualité des choix et niveau du chapitre.
     - Sommaire : niveau de chaque chapitre.
     - « Mon parcours » : note du livre, chapitres évalués, profil, tableau des chapitres avec
       « Rejouer → », une courbe par chapitre rejoué.
     - Espace formateur : note du livre et couverture, nouvelle matrice participant·e·s ×
       chapitres.
     - Bilan de session : note du livre.
  8. **Export.** Deux nouvelles feuilles, `niveaux` et `passages`. La qualité de chaque choix et
     de chaque scène est ajoutée. L'ancienne note v1 est conservée.
  9. **Reprise des parties v1** au démarrage, idempotente (`services/scoring_upgrade.py`).
     - Un passage est créé par chapitre joué.
     - Les traces sont complétées à partir du livre.
     - Les bilans sont recalculés ; l'ancien bilan est gardé dans `results["v1"]`.
- **Choix et justifications.**
  - **Note du livre = moyenne des chapitres à poids égal** : un chapitre = un module du
    programme.
  - **Profil par compétence pondéré par le nombre de choix** qui la mettent en jeu.
  - **Le nombre de passages n'ajoute pas de points.** Il apparaît dans la fiabilité, la courbe et
    la progression, mais pas dans la note, pour ne pas mesurer l'assiduité à la place de la
    compétence.
  - **La note globale porte sur le total des 7 compétences**, et non sur la moyenne des
    compétences. Une réponse ne peut pas être la meilleure sur toutes les compétences à la fois :
    avec la moyenne, 100 serait impossible.
- **Résultats (base jetable, joueur·euse·s fictif·ve·s sur le livre Y2).**
  - Les notes de chapitre vont d'environ 45 à 100.
  - Un profil en progression passe, au chapitre 1, de 59 à 81 puis 89 en trois passages,
    espacés de deux semaines.
  - La marge est de ± 17 après un passage et de ± 6 à 9 après trois.
- **Vérification.**
  - **110 tests verts** (+ 16) : qualité des choix (dont l'exemple du plan : 65 et 29), seuil de
    8 choix, traces v1, changement normalisé, niveau et marge, profil du livre, règle des
    7 jours, scène rejouée dans un passage, chapitre rejoué seul, abandon de session, pages
    joueur et formateur, reprise v1 idempotente, nouvelles feuilles d'export.
  - **Dans le navigateur, sur une base jetable :**
    - espace formateur et matrice des chapitres ;
    - historique avec courbes et bilan de session ;
    - chapitre 4 du Y2 joué en entier : note de fin de chapitre, puis passage d'entraînement
      annoncé au rejeu, avec un ordre des réponses différent.
- **Limites.**
  - La clé de cotation (les −3…+3) n'est toujours pas validée par des experts (étape 2).
  - Les bandes de niveau et le plafond en cas d'erreur critique ne sont pas faits (étape 3).
  - Le coefficient 0,25, le délai de 7 jours et le seuil de 8 choix sont des réglages par
    défaut, à calibrer sur les données d'un pilote.
  - Les feedbacks IA déjà générés citent les anciennes notes.
  - **Incident :** en vérifiant le démarrage de l'application, la reprise v1 a été exécutée sur
    la base locale `instance/eol.db` avant la fin des tests.
    - Cela a créé 65 passages, tous notés, et recalculé 10 bilans.
    - Les tentatives notées sont restées les mêmes.
    - Pour ces 10 bilans, seuls l'ancienne note et l'ancien profil v1 ont été conservés : la
      version corrigée garde désormais l'ancien bilan en entier.
    - Depuis, les tests utilisent toujours une base jetable (`tests/conftest.py`).
- **Fichiers.**
  - Nouveaux :
    - `repositories/passages.py`, `services/scoring_upgrade.py` ;
    - `tests/test_passages.py`.
  - Modifiés, côté serveur :
    - `services/scoring_service.py`, `session_service.py`, `history_service.py`,
      `export_service.py` ;
    - `repositories/orm.py`, `sessions.py` ;
    - `views/session_api.py`, `account.py`, `pages.py` ;
    - `app.py`.
  - Modifiés, pages et scripts du navigateur :
    - `templates/account_history`, `trainer_dashboard`, `session_report`, `play`,
      `play_book` ;
    - `static/play/main.js`, `static/account/history.js`, `charts.js`, `static/account.css`.
  - Modifiés, divers :
    - `scripts/seed_demo.py` ;
    - les tests `test_scoring_service`, `test_session_flow`, `test_export` et `conftest` ;
    - `README.md`, `docs/Scoring_v2_recherche_et_plan.md`.

---

## 3. Architecture technique au 6 octobre 2026

### 3.1 Couches (Clean Architecture, héritée du commit du 6 mai et étendue)

| Couche | Ajouts pendant la période |
|---|---|
| **Domaine** (`domain/`) | Le format des livres s'enrichit, sans casser la compatibilité : états narratifs, conditions, emplacements, points d'entrée, bilans par issue, choix de départ, annexes |
| **Dépôts** (`repositories/`) | `database.py` (moteur SQLAlchemy, SQLite ou PostgreSQL), `orm.py` (modèles `User`, `BookSession`, `ChapterPassage`, `SceneAttempt`), `users.py`, `sessions.py`, `passages.py` |
| **Services** (`services/`) | `scoring_service` (qualité des choix, niveaux, profil du livre), `session_service` (sessions et passages), `history_service`, `scoring_upgrade` (reprise des données v1), `auth_service`, `feedback/` (IA et règles de secours), `export_service` ; extension de `graph_service` (contenu narratif servi au jeu) et de `validation_service` (points d'entrée) |
| **Vues** (`views/`) | `auth`, `guards` (connexion, rôle, CSRF), `session_api`, `account` (historique, bilans, espace formateur, export) ; routes `/play/…` dans `pages` |
| **Exporteurs** (`exporters/`) | `tables.py` : écriture xlsx, csv et json |
| **Front** (`static/`) | `play/` (moteur et interface du jeu), `account/` (graphiques en JS natif, sans librairie), `shared/` (`skills.js`, `http.js` avec le jeton CSRF, `theme.css`) |
| **Outillage** (`scripts/`) | DSL et build des livres Y4 v2 et Y2 v2, `seed_demo.py` |

### 3.2 Routes principales ajoutées

| Route | Rôle |
|---|---|
| `/login`, `/register`, `/logout` | authentification |
| `/play/<livre>/` · `/play/<livre>/chapters/<id>` | sommaire et jeu |
| API de session | démarrer une session, ouvrir un passage de chapitre, enregistrer une scène, terminer un chapitre, générer le feedback |
| `/me` | « Mon parcours » |
| `/sessions/<id>` | bilan d'une session |
| `/trainer/` | espace formateur et export |

### 3.3 Base de données

| Table | Contenu |
|---|---|
| `users` | identifiant, nom affiché, mot de passe haché, rôle |
| `book_sessions` | n° de session, statut, chapitres terminés, résultats figés, feedback |
| `scene_attempts` | choix, scores, bornes des réponses proposées, tentative notée ou non |
| `chapter_passages` | passage de chapitre : noté ou d'entraînement, dates, états de départ, résultats (scoring v2) |
| `passage_attempts` | scènes jouées pendant chaque passage |

### 3.4 Dépendances ajoutées

SQLAlchemy et psycopg (base de données), openpyxl (export Excel).

---

## 4. Décisions de conception et justifications

Matière pour les chapitres « Conception » et « Discussion » du mémoire.

### 4.1 Pédagogie et contenu

1. **Un livre par année, et non par palier, pour UNIL + UNIGE.** C'est lisible pour les
   facultés, et défendable une fois Zurich retiré : 87 % des domaines du jeu sont alignés à un
   an près (§ 2.3).
2. **Zurich différé pour une raison de langue, pas de curriculum.** La justification est
   assumée explicitement (§ 2.3).
3. **Un protagoniste continu (Alex)**, pour que la progression narrative suive la progression
   pédagogique.
4. **Calibrer l'autonomie du joueur sur l'UNIL**, la faculté la moins exposée à la clinique à
   année égale.
5. **Placer chaque scène là où le contenu a déjà été enseigné** : le jeu renforce, il n'anticipe
   pas.
6. **Des mauvaises réponses vraiment pénalisées**, souvent dans des directions opposées (céder
   ou brusquer). Un livre où l'on peut cliquer au hasard sans se tromper n'apprend rien.
7. **Des branches de rattrapage** plutôt qu'un échec sec.
8. **Des erreurs graves aux conséquences durables** (états narratifs), pour marquer le joueur.
9. **4 à 6 réponses par choix, dans un ordre mélangé**, pour empêcher l'apprentissage par la
   position de la réponse.
10. **Un casting récurrent**, qui renforce l'arc narratif et réduit le coût graphique.
11. **Des sujets sensibles traités avec des repères réels** : 143 et 144, secret médical d'une
    mineure, anonymat du don du corps. Une **relecture par un·e référent·e en éthique clinique**
    est recommandée avant toute diffusion.

### 4.2 Expérience joueur

12. **Les scores sont cachés pendant le jeu et révélés au bilan**, pour que l'étudiant·e ne joue
    pas pour le score.
13. **Un parcours joueur séparé de l'éditeur** : les étudiant·e·s ne voient jamais le graphe ni
    les objectifs pédagogiques.
14. **Des portraits manquants dégradés proprement** (initiales, puis avatar) : le jeu reste
    jouable avant la production des images.
15. **Un thème clair aux couleurs institutionnelles**, plus crédible que l'esthétique « IA ».

### 4.3 Technique

16. **Écrire le contenu dans un DSL Python plutôt qu'en JSON brut.** Le texte est plus lisible,
    les identifiants restent cohérents, et le build valide automatiquement ce qu'aucune
    relecture humaine ne vérifierait sur 2 000 réponses : atteignabilité, terminaison,
    cohérence des états, une scène jouable par emplacement. Contrepartie : une modification
    faite dans l'éditeur web est écrasée au build suivant.
17. **Le serveur recalcule les scores** à partir des choix (anti-triche).
18. **Seule la 1ʳᵉ tentative d'une scène compte** : rejouer est de l'entraînement.
19. **Une même base de code pour SQLite (local) et PostgreSQL (production)**, grâce à
    SQLAlchemy et `DATABASE_URL`.
20. **Protection des données.**
    - Aucune donnée identifiante n'est envoyée à l'IA.
    - Un export pseudonymisé est disponible.
    - Les mots de passe sont hachés.
    - Toutes les requêtes qui modifient des données sont protégées par un jeton CSRF.
21. **Un feedback IA avec une version de secours par règles** : l'application ne dépend jamais
    de la disponibilité du modèle.
22. **Des barres triées plutôt qu'un radar** pour le profil : la comparaison est plus lisible.

---

## 5. Validation et tests

### 5.1 Évolution de la suite de tests

| Date | Tests verts | Ajouts |
|---|---|---|
| 18 sept. | 29 | état initial |
| 27 sept. (Y4 v2) | 44 → 45 | états narratifs, points d'entrée, livre Y4 v2, au moins 4 réponses par choix |
| 27 sept. (comptes) | 78 | scoring, feedback, parcours complet via le client de test Flask |
| 4 oct. (Y2 v2) | 89 | livre Y2 v2 (validation, branches, annexes, rapport à jour) |
| 5 oct. (export) | 94 | export xlsx, csv et json, pseudonymisation |
| 6 oct. (scoring v2) | **110** | qualité des choix, passages, règle d'espacement, niveaux, reprise v1 |

Vérifié le 6 octobre : `110 passed`.

### 5.2 Validation automatique des livres (au build)

- Liens entre interactions (règle EG-7) et points d'entrée.
- Atteignabilité de chaque interaction, et terminaison de chaque chemin.
- Cohérence des états : aucun état lu sans être posé ; aucun état posé dans plusieurs chapitres.
- Une seule scène jouable par emplacement, pour toutes les combinaisons d'états possibles.
- Chaque issue d'une scène clé pose exactement un état de son groupe.
- 4 à 6 réponses par point de choix.
- Au moins une réponse très bonne (≥ +9) et une très mauvaise (≤ −7) par chapitre.
- Rapport des soft skills régénéré à chaque build, et un test vérifie qu'il est à jour.

### 5.3 Vérifications dans le navigateur

- Toujours faites sur une **base de données jetable**, pour ne pas toucher la base locale.
- Faites : jeu complet (Y4 v2 voies erreur et évitée, Y2 v2 chapitre 1), historique, bilan,
  espace formateur, CSRF, palette, mise en page sur ordinateur et mobile, export.
- Faites le 6 octobre (scoring v2) : espace formateur, matrice des chapitres, historique et
  courbes, bilan de session, chapitre 4 du Y2 joué en entier puis rejoué en entraînement.
- **Non faites** :
  - chapitres 2, 3, 5 et 6 du livre Y2 v2 joués à la main (moteur et parties simulées seulement) ;
  - feedback IA avec un vrai modèle ;
  - affichage de la heatmap sur des données réelles avant la refonte.

---

## 6. Problèmes rencontrés et corrections

| Date | Problème | Correction |
|---|---|---|
| 18 sept. | Livre 4 livré trop court (67 interactions au lieu d'environ 200) | Réécrit au volume promis (217) |
| 18 sept. | Guillemets imbriqués qui cassaient le script Python | Corrigés |
| 18 sept. | `launch.json` lançait un Python sans Flask | Pointé sur `.venv/bin/python` |
| 22 sept. | Deux images étaient des JPEG renommés en `.png` (`Claude_happy.png`, `Pascal_angry.png`) | Signalé, non corrigé |
| 22 sept. | L'intro de chapitre montrait au joueur du contenu destiné aux enseignant·e·s | Découpage automatique côté serveur |
| 23 sept. | Chiffre d'immersion clinique sensible au codage (29 points) | Analyse de sensibilité, environ 17 points recommandés |
| 27 sept. | Le cache de l'éditeur réappliquait la v1 par-dessus la v2 | 1ʳᵉ garde (`isSameSource`), qui s'est révélée insuffisante |
| 27 sept. | Le titre de scène s'affichait avant le choix de départ | Corrigé |
| 27 sept. | Filtres de la page comparative inopérants (une règle CSS annulait le masquage) | Corrigé, recherche rendue insensible aux accents |
| 27 sept. | Le jeu ne chargeait pas la feuille de style des statuts de session | Corrigé |
| 1ᵉʳ oct. | Flask gardait les anciens templates en cache | Redémarrage du serveur |
| 1ᵉʳ oct. | Profil pondéré illisible (zone des barres de 23 px) | Graphique en pleine largeur |
| 1ᵉʳ oct. | Légende de la heatmap fausse après l'inversion des couleurs | Corrigée |
| 1ᵉʳ oct. | **Brouillons périmés de l'éditeur (risque d'écrasement)** | Correctif conçu le 4 oct., **non appliqué, patch perdu** |
| 4 oct. | Texte final d'une scène sauté avant le bilan | Corrigé |
| 4 oct. | Le compteur de scènes comptait les annexes non jouées | Corrigé |
| 4 oct. | Incohérences narratives au chapitre 1 du Y2 (transitions, répliques) | 5 corrections |
| 4 oct. | Aucun choix très mauvais au chapitre 5 du Y2 | 3 réponses durcies |
| 5 oct. | Le scoring v1 donne 48/100 au hasard et plafonne à 83 | Plan de scoring v2 (§ 2.18), étape 1 implémentée (§ 2.20) |
| 6 oct. | Reprise v1 exécutée par erreur sur la base locale avant la fin des tests | Résultat vérifié, cohérent ; la reprise garde désormais l'ancien bilan en entier ; tests isolés sur une base jetable |

**Contraintes de méthode.** Plusieurs sessions ont été interrompues par les limites
d'utilisation de l'assistant ou par des réponses coupées. Le travail a alors été découpé en
petites étapes, une scène à la fois, et validé à chaque étape.

---

## 7. Limites connues et travail restant

### 7.1 Bloquant ou urgent

- [ ] **Versionner le travail.** Aucun commit depuis le 6 mai 2026 : plusieurs semaines de
  travail ne sont protégées par aucun historique.
- [ ] **Refaire le correctif des brouillons de l'éditeur** (§ 2.15). En attendant, ne pas
  sauvegarder depuis l'éditeur un chapitre qui a été régénéré par un script.

### 7.2 Contenu

- [ ] **Portraits à produire** : 139 pour le Y2 v2, en priorité, et 135 pour le Y4 v2 si ce
  livre est conservé. Aucun n'existe : le jeu affiche les initiales.
- [ ] **Relecture éthique** des scènes sensibles : échographie, erreur médicale, crise
  suicidaire, grossesse d'une mineure, anonymat du don.
- [ ] **Validation par un·e référent·e pédagogique par faculté**, en particulier pour l'UNIGE,
  dont le détail de B2-B3 n'est pas public.
- [ ] Jouer les chapitres 2 à 6 du Y2 v2 dans le navigateur.
- [ ] Corriger l'écart entre la bible et le texte du Y2 (Bernard et Noah à la cérémonie).
- [ ] Livres 1, 3, 5 et 6 du plan, à faire. Le livre 5 « Fin de vie » est identifié comme
  prioritaire.
- [ ] Supprimer le livre Y4, comme prévu par l'étudiant.

### 7.3 Scoring et évaluation

- [x] Étape 1 du scoring v2 : note par choix, passage de chapitre, niveau, progression,
  fiabilité, profil du livre (§ 2.20).
- [ ] Étape 2 : exporter et réimporter la clé de cotation pour un panel d'experts, accord (ICC),
  champs « critique » et « justification », points affichés comme provisoires.
- [ ] Étape 3 : bandes de niveau (Angoff), plafond en cas d'erreur critique, calibrage du
  coefficient 0,25, du délai de 7 jours et du seuil de 8 choix sur un pilote.
- [ ] Constituer un panel d'experts pour valider la clé de cotation. En attendant, les points
  actuels doivent être présentés comme provisoires.

### 7.4 Application

- [ ] Tester le feedback IA avec un vrai modèle.
- [ ] Ajouter un outil de migration de la base (Alembic) avant la mise en production.
- [ ] Réinitialisation du mot de passe par e-mail, limitation des tentatives de connexion,
  suppression de compte (RGPD).
- [ ] Données de démonstration : ajouter des sessions sur la branche « erreur ».
- [ ] Production : `pip install -r requirements.txt` (openpyxl), et définir `SECRET_KEY`,
  `DATABASE_URL` et `SESSION_COOKIE_SECURE`.

---

## 8. Pistes pour la rédaction du mémoire

| Chapitre du mémoire | Matière disponible dans ce journal |
|---|---|
| **Contexte et problématique** | La nouvelle mission (livres pour les étudiant·e·s en médecine) et la question « un livre par année pour trois facultés ? » (§ 2.3) |
| **État de l'art** | SJT, cotation par experts, progression, effet de retest, validité selon Kane (§ 2.18, annexe A) ; serious games en santé ; référentiel PROFILES |
| **Méthodologie** | Comparaison curriculaire en trois mesures (§ 2.2), analyse de sensibilité (§ 2.6), contrefactuel (§ 2.3), mesure du scoring avec des joueur·euse·s simulé·e·s (§ 2.18) |
| **Conception** | Plan des 6 livres (§ 2.4), principes narratifs et pédagogiques (§ 4.1), états narratifs (§ 2.8), branches et annexes (§ 2.16), choix d'expérience joueur (§ 4.2) |
| **Implémentation** | Architecture (§ 3), DSL et build (§ 4.3), comptes, sessions et feedback (§ 2.11), export (§ 2.17), identité visuelle (§ 2.13) |
| **Validation et résultats** | Évolution des tests (§ 5.1), validation automatique (§ 5.2), chiffres des livres (§ 1.2), répartition des soft skills (§ 2.8) |
| **Discussion** | Honnêteté sur la décision de retirer Zurich (§ 2.3), fragilité du chiffre d'immersion (§ 2.6), limites du scoring v1 (§ 2.18), deux codages curriculaires (§ 2.10) |
| **Limites et perspectives** | § 7 : images, relecture éthique, référent·e·s, scoring v2, Zurich, mise en production |
| **Méthode de travail** | Développement assisté par une IA de programmation (Claude Code) : à mentionner par transparence, avec le rôle de l'étudiant dans les décisions (périmètre, refus du livre 4 trop court, validation des sujets sensibles, choix des couleurs) |

**Chiffres clés à citer.**

- **79 %** des domaines enseignés à un an près dans les trois facultés, mais **21 %** seulement
  la même année.
- **87 %** des domaines du jeu alignés à un an près pour UNIL + UNIGE, contre **67 %** à trois.
- **Soins palliatifs** : année 5 à l'UNIL, 4 à l'UNIGE, 3 à l'UZH.
- **Environ 17 points** d'écart d'immersion clinique, selon l'hypothèse défendable.
- Livre 2 : de **22 à 463 interactions** ; livre 4 v2 : **2 446 réponses**.
- Tests : de **29 à 94**.
- Scoring v1 : **48/100 au hasard**, plafond à **83/100**.

**Phrases fortes issues du travail.**

- « Le contenu converge, la chronologie et la pédagogie divergent. »
- « Un livre où l'on peut cliquer au hasard sans se tromper n'apprend rien. »
- « Une décision de faisabilité, validée a posteriori par les chiffres. »
- « On ne soigne jamais un corps. On soigne quelqu'un qui habite dedans, et ceux qui l'attendent
  dehors. » (lettre de Jeannine, livre 2)

---

## 9. Annexes

### Annexe A — Références principales pour le scoring

La liste complète, soit 35 références, est dans
[Scoring_v2_recherche_et_plan.md](Scoring_v2_recherche_et_plan.md).

**Noter les réponses**

1. Patterson, Zibarras & Ashworth (2016). *Situational judgement tests in medical education and
   training: AMEE Guide No. 100.* Medical Teacher, 38(1), 3-17.
2. Bergman, Drasgow et al. (2006). *Scoring situational judgment tests: Once you get the data,
   your troubles begin.* International Journal of Selection and Assessment, 14(3), 223-235.
3. Weng, Yang, Lievens & McDaniel (2018). *Optimizing the validity of situational judgment
   tests: The importance of scoring methods.* Journal of Vocational Behavior, 104, 199-209.
4. de Leng et al. (2017). *Scoring method of a Situational Judgment Test: influence on internal
   consistency reliability, adverse impact and correlation with personality?* Advances in
   Health Sciences Education, 22(2), 243-265.

**Établir la clé avec des experts**

5. Humphrey-Murto, Varpio, Gonsalves & Wood (2017). *Using consensus group methods such as
   Delphi and Nominal Group in medical education research.* Medical Teacher, 39(1), 14-19.

**Ramener les notes sur 100**

6. Cohen, Cohen, Aiken & West (1999). *The problem of units and the circumstance for POMP.*
   Multivariate Behavioral Research, 34(3), 315-346.

**Suivre la progression**

7. Pusic, Boutis, Hatala & Cook (2015). *Learning curves in health professions education.*
   Academic Medicine, 90(8), 1034-1042.
8. Marx & Cummings (2007). *Normalized change.* American Journal of Physics, 75(1), 87-91.
9. Pelánek (2017). *Bayesian knowledge tracing, logistic models, and beyond: an overview of
   learner modeling techniques.* User Modeling and User-Adapted Interaction, 27, 313-350.
10. Lievens, Buyse & Sackett (2005). *Retest effects in operational selection settings:
    Development and test of a framework.* Personnel Psychology.

**Erreurs critiques et validité**

11. Payne et al. (2008). *Sharpening the eye of the OSCE with critical action analysis.*
    Academic Medicine, 83(10).
12. Cook, Brydges, Ginsburg & Hatala (2015). *A contemporary approach to validity arguments: a
    practical guide to Kane's framework.* Medical Education, 49(6), 560-575.

### Annexe B — Documents produits pendant la période

| Document | Contenu |
|---|---|
| [programmes_medecine/](programmes_medecine/) | 18 plans d'études officiels et leurs sources |
| [programmes_medecine/COMPARATIF_MATIERES.md](programmes_medecine/COMPARATIF_MATIERES.md) · [.html](programmes_medecine/comparatif_matieres.html) | 66 matières × 3 universités, et les matières communes |
| [MedStudents_Y4_assets.md](MedStudents_Y4_assets.md) | Images du livre 4 v1 |
| [MedStudents_Y4_v2_bible.md](MedStudents_Y4_v2_bible.md) | Bible narrative du livre 4 v2 |
| [MedStudents_Y4_v2_soft_skills.md](MedStudents_Y4_v2_soft_skills.md) · `.json` | Répartition des soft skills du livre 4 v2 |
| [MedStudents_Y4_v2_assets.md](MedStudents_Y4_v2_assets.md) | 135 portraits à produire |
| [MedStudents_Y2_v2_bible.md](MedStudents_Y2_v2_bible.md) | Bible narrative du livre 2 v2 |
| [MedStudents_Y2_v2_soft_skills.md](MedStudents_Y2_v2_soft_skills.md) · `.json` | Répartition des soft skills du livre 2 v2 |
| [MedStudents_Y2_v2_assets.md](MedStudents_Y2_v2_assets.md) | 139 portraits à produire |
| [Scoring_v2_recherche_et_plan.md](Scoring_v2_recherche_et_plan.md) | Diagnostic, recherche et plan de scoring |
| [../README.md](../README.md) | Mis à jour : architecture, routes, comptes, base de données, export |

**Pages privées sur claude.ai** (à partager depuis leur menu « Partager » si besoin) :

- deck « Livres MedStudents — point hebdo » (22 sept.) : https://claude.ai/artifact/VUwF919MCj4cnYQE9YZXFv
- comparatif interactif des matières (27 sept.) : https://claude.ai/artifact/4yjXD4ZAT4cd3Z87gQNGKR

### Annexe C — Sessions de travail sources de ce journal

| Dates | Titre de la session | Contenu |
|---|---|---|
| 18 → 23 sept. | Programmes détaillés médecine Lausanne/Genève/Zurich | § 2.1 à 2.7 |
| 24 → 27 sept. | Book 4 storytelling et soft skills | § 2.8 à 2.10 |
| 27 sept. | Historique sessions et feedback utilisateur | § 2.11 et 2.12 |
| 1ᵉʳ oct. | Couleurs interface universités | § 2.13 et 2.14 |
| 1ᵉʳ → 4 oct. | Correctif des brouillons de l'éditeur (session séparée) | § 2.15 |
| 4 → 5 oct. | Refonte book 2 médecine | § 2.16 à 2.18 |

### Annexe D — Modifications non commitées antérieures à la période

Pour mémoire, l'arbre de travail contient aussi des fichiers modifiés **avant** le 14 septembre,
eux non plus jamais commités :

- les supports de la soutenance orale de juin 2026 (`output/PA_2026_EOL_*.pptx/.pdf`, scripts
  `output/build_*`) ;
- les scripts d'évaluation (`scripts/eval_ai_compliance.py`, `eval_backend_comparison.py`,
  `eval_scoring_mae.py`) et leurs résultats (`output/eval_*.json`) ;
- `docs/appendices_complete.tex` ;
- des changements dans `repositories/chapters.py`.

Une modification mineure de `static/chapter/utils.js`, datée du 29 septembre, n'apparaît dans
aucune session : la fonction `getInteractionIdFromNodeId` fonctionne désormais aussi sans le jeu
de nœuds du graphe.
