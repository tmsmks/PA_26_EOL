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
| **6 oct. →** | Un scoring fondé sur la recherche | Journal de développement · scoring v2, étape 1 : note par choix (100 atteignable, ≈ 50 au hasard), passage de chapitre comme unité de note, niveau, progression et fiabilité par chapitre · étape 2 : outils de validation de la clé par un panel d'experts (grille à l'aveugle, ICC, Delphi) · livre 2 refondu en 5 chapitres (509 interactions), clé de notation auditée et contrôlée au build · bibliographie réduite à 27 articles en libre accès et utiles au scoring, proposition de scoring v3 · clé du livre 2 cotée par Claude (2 017 réponses) |

### 1.2 Avant / après en chiffres

**Contenu des livres**

| Livre | Avant (mi-septembre) | Après (10 octobre) |
|---|---|---|
| `end_of_life` (référence historique) | 5 ch. · 17 scènes · 416 interactions · 1 378 réponses | inchangé |
| `medstudents_y2` (livre 2) | v1 pilote : 3 ch. · 4 scènes · 22 interactions · 51 réponses | **v2 « Le corps donné » : 5 ch. · 36 scènes · 509 interactions · 2 068 réponses** (refonte du 10 oct. ; 6 ch. · 43 scènes · 463 interactions le 4 oct.) |
| `medstudents_y4` (livre 4) | n'existait pas | v1 (18 sept.) : 4 ch. · 12 scènes · 217 interactions · 577 réponses → **v2 (27 sept.) : 6 ch. · 42 scènes · 576 interactions · 2 446 réponses** |

**Application**

| Indicateur | Avant | Après |
|---|---|---|
| Tests automatisés | 29 | **123** (tous verts au 10 octobre) |
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
- **Fichier.** [docs/Scoring_v2_recherche_et_plan.md](Scoring_v2_recherche_et_plan.md), avec 41
  références vérifiées une à une (annoncées 35 par erreur à l'époque). Les 12 principales sont en annexe A.

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

### 2.21 — 6 oct. · Scoring v2, étape 2 : outils de validation de la clé par des experts

- **Contexte.** Le travail a été commité par l'étudiant avant cette étape (commit `1f5a86b`).
- **Besoin.** Les points des réponses (−3…+3 sur 7 compétences) ont été écrits par l'auteur
  seul. La littérature sur les tests de jugement situationnel demande une clé établie par un
  panel d'experts, avec un accord mesuré (plan de scoring, § 3.1). Il faut donc outiller cette
  validation.
- **Réalisation.**
  1. **Grille ancrée provisoire** (`domain/expert_rubric.py`). Pour chaque compétence, ce que
     valent −3, 0 et +3, ancré dans PROFILES, Kalamazoo et Calgary-Cambridge. S'y ajoute une
     définition de la réponse « critique ».
  2. **Grille Excel pour les experts**, téléchargeable depuis la nouvelle page « Clé de
     cotation » de l'espace formateur (`/trainer/cle/`).
     - Le périmètre se choisit : tout le livre, un chapitre, ou un échantillon de points de
       choix tiré au hasard (graine fixe, le même pour tous les experts).
     - La grille contient les consignes, la grille ancrée, puis une ligne par réponse avec sa
       situation.
     - Elle ne montre **pas les points de l'auteur** : la cotation se fait à l'aveugle.
     - La saisie est contrôlée (entier de −3 à +3) ; colonnes « critique », « justification »
       et « commentaire ».
  3. **Import des grilles remplies**, plusieurs à la fois. Le nom de l'expert et le tour sont
     lus dans la grille. Les erreurs sont signalées avec la ligne et la compétence concernées.
     Réimporter la grille d'un expert remplace ses cotes de ce tour. Nouvelle table
     `expert_ratings`.
  4. **Accord entre experts**, par compétence et sur le total :
     - ICC(2,1) et ICC(2,k) (deux facteurs, effets aléatoires, accord absolu) ;
     - seuils de Koo & Li ;
     - réponses à revoir : experts écartés de 3 points ou plus, ou médiane écartée de l'auteur
       de 2 points ou plus ;
     - réponses jugées critiques par la majorité.
  5. **Synthèse Excel** d'un tour (feuilles « accord » et « reponses ») pour préparer le tour
     suivant de la méthode Delphi.
  6. **Champs `Critical` et `Rationale`** d'une réponse : lus par le jeu et ajoutés au
     mini-langage du livre Y2. Le marqueur critique de la réponse choisie est gardé dans la
     trace et exporté, avec un repère provisoire (total ≤ −7).
  7. **Mention « clé provisoire »** sur la fin de chapitre, l'historique et le bilan de session.
- **Choix et justifications.**
  - **Cotation à l'aveugle**, pour que les experts ne s'alignent pas sur l'auteur.
  - **ICC à accord absolu**, et non à cohérence : c'est la valeur des points qui compte, pas
    seulement leur ordre.
  - **ICC calculé sur les réponses cotées par tous les experts du tour.**
  - **Une compétence laissée vide sur une réponse cotée vaut 0** (neutre ou pas en jeu), sinon
    les grilles seraient très longues à remplir.
  - **Charge de travail.** Le livre Y2 compte 1 776 réponses aux points de choix, soit 230 à
    400 par chapitre. La page propose donc de répartir les chapitres entre experts (au moins 3
    par chapitre) ou de travailler sur un échantillon.
- **Résultats.** Trois experts simulés ont coté le chapitre 2 du Y2 (303 réponses), avec des
  écarts aléatoires de ±1 autour de l'auteur.
  - L'accord est bon à excellent sur la plupart des compétences, et sur le total (ICC(2,1) =
    0,87).
  - Il est faible pour la compassion (0,27) et la régulation émotionnelle (0,38). Ces
    compétences valent souvent 0 dans la clé : le moindre écart y pèse donc lourd. C'est le
    même constat que pour leur faible présence dans les choix (§ 2.18).
- **Vérification.**
  - **116 tests verts** (+ 6), dont le calcul de l'ICC vérifié sur l'exemple publié de Shrout &
    Fleiss (1979) : ICC(2,1) = 0,29 et ICC(2,4) = 0,62. Les autres tests couvrent :
    - la grille à l'aveugle et son aller-retour (remplie, puis relue) ;
    - les valeurs refusées et les réponses d'une autre version du livre ;
    - les divergences, les écarts à l'auteur et la majorité critique ;
    - les droits d'accès, l'import, la synthèse et la suppression ;
    - le marqueur critique dans l'export.
  - **Dans le navigateur, sur une base jetable** : page « Clé de cotation » avec les cotes des
    trois experts simulés.
- **Limites.**
  - La grille ancrée est un **brouillon** à faire valider par le panel.
  - La **clé consensuelle n'est pas encore appliquée au livre** : les points du jeu restent ceux
    de l'auteur.
  - Il n'y a pas encore de grille de tour 2 pré-remplie avec la médiane du groupe.
  - Les justifications des 1 776 réponses aux points de choix restent à écrire ; celles des
    experts pourront servir de base.
  - Le panel d'experts reste à constituer.
- **Fichiers.**
  - Nouveaux :
    - `domain/expert_rubric.py`, `services/expert_key_service.py` ;
    - `exporters/expert_key.py`, `repositories/expert_ratings.py`, `views/expert_key.py` ;
    - `templates/expert_key.html.jinja`, `tests/test_expert_key.py`.
  - Modifiés, code :
    - `repositories/orm.py`, `services/scoring_service.py`, `services/export_service.py` ;
    - `views/__init__.py`, `app.py`, `scripts/medstudents_y2_v2/dsl.py`.
  - Modifiés, pages :
    - `templates/trainer_dashboard`, `account_history`, `session_report`, `play` ;
    - `static/account.css`.
  - Modifiés, documentation :
    - `README.md`, `docs/Scoring_v2_recherche_et_plan.md`.

### 2.22 — 7 oct. · Bibliographie du scoring en PDF

- **Besoin.** Avoir à part, dans un PDF, les recherches sur lesquelles repose le scoring (pour le
  rapport et le mémoire).
- **Réalisation.** [Scoring_v2_bibliographie.pdf](Scoring_v2_bibliographie.pdf), 5 pages :
  - les 43 références, classées en 10 thèmes selon ce à quoi elles ont servi ;
  - pour chacune, la référence complète, un lien cliquable (41 sur 43, dont les DOI vérifiés),
    et une ligne « Ce que nous en retenons ».
- **Correction au passage.** Le nombre de références avait été annoncé à 35 ; il y en avait 41
  dans le plan, plus 2 sur l'ICC ajoutées le 6 oct., soit 43 (§ 6).
- **Vérification.**
  - Le PDF a été relu page par page en images, et ses 41 liens comptés.
  - Les espaces insécables français sont en place (« », :, ;).
- **Limites.**
  - Le PDF est généré par un script temporaire (reportlab, hors du projet), à partir de la
    bibliographie de `Scoring_v2_recherche_et_plan.md` (§ 7).
  - Si cette bibliographie change, il faudra régénérer le PDF.
- **Fichiers.** `docs/Scoring_v2_bibliographie.pdf` (nouveau).

### 2.23 — 10 oct. · Livre 2 : cinq chapitres, 509 interactions, et audit de la clé de notation

- **Besoin.** Demande de l'étudiant, pour le livre 2 « Le corps donné » :
  - 5 chapitres d'environ 5 ou 6 scénarios, avec beaucoup d'interactions : environ 500 en tout ;
  - rester fidèle au programme de 2ᵉ année des trois facultés, et à ce public ;
  - des compétences bien réparties entre les réponses ;
  - « prendre le temps de bien vérifier » le rejeu du score : comment les points sont répartis
    entre les réponses, et si c'est juste.
- **Audit du score, avant toute réécriture.** Des joueur·euse·s simulé·e·s ont joué tout le livre,
  et chaque parcours a été rejoué par le vrai calcul serveur (`replay_scene`, puis
  `choice_quality`).
  - **Le rejeu est juste.** Le serveur rejoue les indices d'origine des réponses (l'ordre mélangé
    à l'écran ne change rien) ; toujours la meilleure réponse = 100, toujours la pire = 0, au
    hasard ≈ 48.
  - **La clé de notation, elle, avait trois défauts :**
    1. **Un indice de longueur.** La meilleure réponse était la plus longue dans 80 % des points
       de choix. Choisir toujours la réponse la plus longue rapportait **89,5/100**, sans lire.
    2. **La Compassion sous-mesurée** : 6 % des points positifs. Avec la Régulation
       émotionnelle, elle restait parfois sous le seuil de 8 choix, donc non notée.
    3. **Des parcours trop courts** : certains chapitres se finissaient avec trop peu de choix
       pour noter chaque compétence.
- **Réalisation.**
  1. **Cinq chapitres** au lieu de six : 36 scènes écrites sur 30 emplacements (27 obligatoires,
     3 annexes), soit 5 ou 6 scénarios joués par chapitre.
     - Le vaccin et le téléphone deviennent une seule journée (2.1) ; le BLS passe au chapitre 2,
       le patient standardisé au chapitre 3.
     - La fermeture du cabinet, la chute et la dénutrition se rejoignent en 4.5 ; l'appel de
       23 h passe au chapitre 4.
     - L'examen et la dernière visite se rejoignent en 5.3 ; septembre devient l'épilogue de la
       cérémonie. L'atelier de recherche et l'annexe du balcon sont retirés.
  2. **509 interactions** (463 avant), 2 068 réponses, 424 points de choix.
     - Chaque scène réécrite et allongée ; des rattrapages (le 144 appelé à minuit à Noël, le
       réveil à 3 h 12 après le « bonne nuit » de Noah).
     - Des nœuds d'entrée selon la mémoire : la lettre de 5.5 combine six post-scriptum et trois
       issues de la nuit de Noah (27 points d'entrée générés par le code).
  3. **Ancrage dans les programmes revu chapitre par chapitre** (modules BMed2 de l'UNIL, unités
     de l'UNIGE, Humanbiologie et cours cliniques de l'UZH). Alex reste à sa place de 2ᵉ année :
     écouter, transmettre, vérifier une identité, appeler le 144, dire « pause réelle ».
  4. **Clé rééquilibrée.**
     - Longueur des réponses : le rang de longueur de la meilleure réponse est réparti de 1 à 6.
     - Une seule meilleure réponse par point de choix.
     - Compassion : 48 gestes de soin concrets (rester auprès, prendre la main, accompagner,
       appeler les secours) passent d'un point d'Empathie à un point de Compassion, à total
       égal ; 36 meilleures réponses qui soulagent quelqu'un gagnent +1 en Compassion.
     - Les parcours les plus courts sont allongés.
  5. **Le build vérifie désormais la clé** (`scripts/build_medstudents_y2_v2.py`) et échoue si :
     - un point de choix a deux meilleures réponses ;
     - une stratégie fondée sur la longueur des réponses dépasse 62/100 sur un chapitre ;
     - une compétence est en jeu dans moins de 8 choix sur le parcours le plus court d'un
       chapitre.
     Le rapport `docs/MedStudents_Y2_v2_soft_skills.md` gagne une section « Audit du score » :
     tout le livre est joué (meilleure, pire, plus longue, plus courte, 100 parties au hasard
     avec une graine fixe), puis rejoué par le calcul serveur.
  6. **Lancement sur base jetable** : configuration `eol-jetable` dans `.claude/launch.json`,
     qui crée une base SQLite neuve dans un dossier temporaire à chaque démarrage.
- **Choix et justifications.**
  - Le moteur ne fait varier une scène qu'à son début. Les fusions de scènes et les croisements
    de mémoires passent donc par des points d'entrée, générés par le code quand deux dimensions
    se croisent.
  - Équilibrer les longueurs plutôt que raccourcir toutes les bonnes réponses : une première
    correction (bonne réponse jamais la plus longue) avait créé l'indice inverse, « toujours la
    2ᵉ plus longue » donnant 93/100.
  - Compassion : reclassement à total constant (l'ordre des réponses ne bouge pas), puis +1
    seulement sur des meilleures réponses (aucun ex aequo possible).
  - Seuil de 62 : au hasard, on obtient environ 47 ; au-delà de 62, la forme des réponses
    rapporterait 15 points de plus que le hasard.
  - Rien n'a changé dans le calcul serveur, et aucun point n'est donné pour le nombre de
    passages : seule la clé (le contenu) a été corrigée.
- **Résultats (livre entier, rejeu serveur).**

  | Mesure | Avant | Après |
  |---|---:|---:|
  | Toujours la réponse la plus longue | **89,5**/100 | 46,4 |
  | La meilleure réponse est la plus longue | 80 % des points de choix | 29 % |
  | Au hasard (moyenne de 100 parties) | ≈ 48 | 46,7 |
  | Toujours la meilleure / la pire | 100 / 0 | 100 / 0 |
  | Part de la Compassion dans les points positifs | 6 % | 11 % |
  | Compétences non notées dans les parties au hasard | oui (CO, ER) | aucune |

  - Points positifs du livre : Respect 15 %, Empathie 18 %, Compassion 11 %, Régulation
    émotionnelle 11 %, Clarté 14 %, Limites professionnelles 16 %, Collaboration 15 %.
  - Partie réelle du chapitre 5 : 86/100 ; la note stockée (85,8) est retrouvée à l'identique
    en rejouant hors ligne les choix enregistrés.
- **Vérification.**
  - Build : 0 erreur, 0 avertissement.
  - **123 tests verts** (+ 7) : 5 chapitres de 5 ou 6 scénarios, environ 500 interactions,
    meilleure / pire / hasard par chapitre, indice de longueur, preuves par compétence,
    répartition entre 10 et 20 %, et deux tests qui vérifient que le build refuse un ex aequo
    et un indice de longueur.
  - **Dans le navigateur, sur une base jetable** : chapitre 5 joué en entier (écran de départ,
    branche « famille apaisée », examen quitté, fourgon, lettre, cérémonie avec le nom prononcé,
    épilogue). Six incohérences relevées en jouant ont été corrigées (§ 6).
  - Base locale lue en lecture seule : aucune partie ni cotation d'expert sur le livre 2, donc
    aucune donnée à reprendre après la refonte.
- **Limites.**
  - Les chapitres 1 à 4 de la nouvelle version sont vérifiés par le build et les parties
    simulées, pas encore joués à la main.
  - La clé reste provisoire : elle doit être validée par le panel d'experts (étape 2).
  - Au second passage par une boucle « on recommence », le simulateur essaie une autre réponse ;
    un·e vrai·e joueur·euse peut tourner plus longtemps.
  - Portraits : 138 images à produire.
- **Fichiers.**
  - Contenu : `scripts/medstudents_y2_v2/ch1.py` à `ch5.py` (réécrits), `book.py` ;
    `ch6.py` supprimé.
  - Outillage : `scripts/build_medstudents_y2_v2.py` (règles de la clé, audit du score) ;
    `.claude/launch.json` (configuration `eol-jetable`).
  - Générés : `data/chapters/MedStudents_Y2_v2.json`, `docs/MedStudents_Y2_v2_soft_skills.md`
    et `.json`, `docs/MedStudents_Y2_v2_assets.md`.
  - Tests : `tests/test_medstudents_y2_v2.py`.
  - Documentation : `docs/MedStudents_Y2_v2_bible.md` (réécrite pour 5 chapitres),
    `docs/Scoring_v2_recherche_et_plan.md` (§ 3.1, point 6 : aucun indice de forme),
    `README.md` (contrôle de la clé).

### 2.24 — 10 oct. · Lecture audio du parcours joueur

- **Besoin.** Demande de l'étudiant : un participant peut préférer écouter plutôt que lire les
  longs paragraphes ; la lecture audio rend le parcours plus fluide.
- **Réalisation.**
  - Bouton « Écouter » dans la barre du haut du jeu, avec pause, relecture et un panneau de
    réglages : voix, vitesse, lire aussi les réponses proposées, accords de l'écriture inclusive
    (« seul·e » lu au féminin ou au masculin). Raccourcis : L (écouter / arrêter), P (pause),
    R (relire), Échap.
  - Sont lus : l'accueil du chapitre, l'écran de départ, l'intro de chaque scénario, chaque
    réplique (le nom du personnage seulement quand il change), le bilan de scène et la note du
    chapitre ; les réponses en option, dans l'ordre affiché, avec leur numéro.
  - `static/play/speech_text.js` (fonctions pures) prépare le texte : écriture inclusive,
    titres (« Dre » → « Docteure »), heures (« 22 h 07 » → « 22 heures 7 »), cris en
    capitales, emojis ; découpage en phrases de 180 caractères au plus.
  - `static/play/audio.js` : lecteur (file de phrases, pause et reprise, relance d'une phrase
    « perdue » par Safari ou Chrome, déverrouillage au premier geste pour iOS), meilleure voix
    française choisie d'office, réglages gardés dans le navigateur.
- **Choix et justifications.**
  - Synthèse vocale du navigateur (Web Speech API) : gratuite, sans serveur ni clé, rien
    n'est envoyé ; elle marche sur ordinateur et téléphone. Revers : la voix dépend de l'appareil.
  - Accords au féminin par défaut, réglables (la majorité des étudiant·e·s en médecine sont des
    femmes) ; le texte affiché ne change pas.
  - Commandes cachées si le navigateur ne sait pas lire à voix haute.
- **Vérification.**
  - 8 tests JavaScript (`tests/js/speech_text.test.mjs`, lancés par pytest avec Node), dont un
    balayage de tous les textes des trois livres : aucun « · », aucune abréviation, aucune
    heure abrégée ni emoji dans le texte lu.
  - Navigateur, base jetable : 180 voix détectées, « Thomas » choisie ; lecture réelle
    phrase par phrase (événements de début et de fin), pause et reprise, écran de départ lu,
    réglages mémorisés après rechargement. Corrigé au passage : Échap ne fermait pas le panneau
    quand le focus était sur une case à cocher.
- **Limites.** Une scène entière n'a pas été écoutée de bout en bout dans le navigateur ; pas de
  vérification sur iPhone ni Android ; la qualité de la voix dépend de l'appareil (une synthèse
  neuronale côté serveur serait meilleure, mais demande un service payant).
- **Fichiers.** Nouveaux : `static/play/speech_text.js`, `static/play/audio.js`,
  `tests/js/speech_text.test.mjs`, `tests/test_play_audio.py`. Modifiés :
  `static/play/main.js`, `templates/play.html.jinja`, `static/play.css`.

### 2.25 — 12 oct. · Voix naturelles pour la lecture audio

- **Besoin.** Retour de l'étudiant : la voix « est trop robotisée » ; il veut une voix plus
  fluide et plus agréable pour l'auditeur.
- **Diagnostic.** La lecture utilisait les voix du navigateur. Sur l'appareil testé, la
  meilleure voix française était « Thomas », une voix compacte du système : c'est elle qui
  sonnait robotique. La qualité dépendait donc de chaque appareil.
- **Pistes écartées.**
  - `edge-tts` (voix d'Edge, gratuites) : accès non officiel ; Microsoft le refusait le jour même
    (erreur 403, horloge vérifiée). Trop fragile pour un vrai déploiement.
  - Voix Piper « tom » : modèle sous AGPL-3.0.
- **Réalisation.**
  1. **Voix neuronales locales (Piper)**, choisies par défaut : *Siwis* (féminine, corpus
     sous CC BY 4.0), *Pierre* et *Jessica* (corpus UPMC, CC BY-SA 4.0). Gratuites, hors ligne :
     le texte ne quitte pas le serveur. Débit un peu plus posé et court silence entre les phrases.
  2. **Option Azure** (voix les plus naturelles, dont le français de Suisse : Ariane, Fabrice) :
     il suffit de définir `AZURE_SPEECH_KEY` et `AZURE_SPEECH_REGION` ; le texte part alors
     chez Microsoft. Les voix du navigateur restent le repli.
  3. **Service** `services/tts_service.py` : cache des MP3 (même voix et même texte = un seul
     fichier, `instance/tts/cache`), une seule synthèse pour deux demandes simultanées, texte
     de 3 000 caractères au plus, 40 synthèses par minute et par participant, plafond quotidien
     (`TTS_DAILY_CHARS`), chemins de cache vérifiés.
  4. **Piper dans un processus séparé** (`scripts/tts_piper_worker.py`, sous GPL-3.0 comme
     Piper) : les modèles restent chargés, une réplique se synthétise en moins de 0,1 s. Le
     modèle est préchauffé à l'ouverture de la page de jeu.
  5. **API** (`views/tts.py`, connexion requise) : liste des voix, synthèse, et extrait audio
     servi par morceaux (requêtes partielles, nécessaires à Safari), en cache privé.
  6. **Lecteur** (`static/play/audio.js`) : chaque écran est lu d'une traite par la voix
     naturelle ; une première phrase courte fait démarrer la lecture vite, la suite et les
     réponses se préparent et se téléchargent pendant ce temps. Pause et reprise exactes, vitesse
     réglable sans changer le timbre, choix entre voix naturelles et voix de l'appareil,
     repli automatique si le serveur ne répond pas.
  7. Commande `flask --app app tts-install` pour télécharger les voix (environ 140 Mo).
- **Résultats (navigateur, base jetable).** Entre le clic et le début de la voix : 0,76 s sur
  un écran jamais lu, création de la session comprise (premier extrait prêt en 0,34 s) ;
  contre 2 à 3 s avant le préchauffage et le découpage.
- **Vérification.**
  - **138 tests verts** (+ 12) : cache, validation, limites, chemins, choix du moteur, requête
    Azure simulée (SSML, échappement, en-têtes), API (connexion, erreurs, requêtes partielles),
    et une vraie synthèse Piper quand elle est installée.
  - Navigateur, base jetable : voix *Siwis* choisie d'office, synthèse puis lecture (206),
    pause et reprise sans nouvelle requête, réglages et repli vérifiés ; le processus Piper
    s'arrête avec le serveur.
- **Limites.**
  - Piper est nettement plus naturel que les voix système, mais reste en dessous des voix
    Azure ; le choix d'Azure (coût, envoi du texte chez Microsoft) revient à l'équipe.
  - Un seul processus Piper : en classe entière, les premières lectures d'un même texte se
    suivent. Le cache absorbe ensuite la charge ; un préremplissage du cache pour tout le livre
    reste à faire.
  - Le plafond et le compteur par minute sont en mémoire : ils valent par processus serveur.
  - Pas encore écouté sur iPhone ni Android.
- **Fichiers.** Nouveaux : `services/tts_service.py`, `views/tts.py`,
  `scripts/tts_piper_worker.py`, `tests/test_tts.py`. Modifiés : `static/play/audio.js`,
  `templates/play.html.jinja`, `static/play.css`, `app.py`, `views/__init__.py`,
  `requirements.txt`, `README.md`, `tests/test_play_audio.py`.

### 2.26 — 12 oct. · Bibliographie du scoring : articles à comité de lecture, en libre accès

- **Besoin.** Deux demandes successives de l'étudiant :
  1. ne garder que de « vrais papiers de recherche », publiés et validés, sans forums ni blogs ;
  2. puis ne garder que des articles **gratuits** : le jury doit pouvoir cliquer sur le lien et
     lire directement le PDF, sans payer ni passer par une page intermédiaire.
- **Méthode.**
  - Chaque référence a été contrôlée dans trois bases :
    - Crossref : type de publication, revue, volume, pages, correctifs ;
    - OpenAlex : versions en libre accès, rétractation ;
    - PubMed : type d'article (étude, revue, commentaire…).
  - **Critère 1, la publication.** Article d'une revue à comité de lecture, ou des actes d'une
    conférence à comité de lecture (CHI). Sont acceptés les études empiriques, les
    méta-analyses, les revues et les articles méthodologiques. Sont exclus les commentaires, les
    chapitres de livres, les rapports techniques et les mini-revues d'opinion.
  - **Critère 2, l'accès.** Un PDF gratuit et légitime : éditeur en libre accès, PubMed Central,
    dépôt d'université, archive HAL ou page universitaire de l'auteur·e. Sont exclus
    ResearchGate, Academia.edu, Semantic Scholar, gwern.net et les copies déposées sur des sites
    de cours ou des sites personnels sans lien avec les auteur·e·s.
  - Quand un article payant n'avait pas de version gratuite, il a été remplacé par un article
    en libre accès qui appuie la même idée. Si aucun ne convenait, l'article a été retiré et le
    texte du plan ajusté.
- **Résultat : 43 → 33 références, toutes gratuites.**
  - **Premier tri (publication).** 3 textes retirés, qui n'étaient pas des articles de
    recherche :
    - Eva (2003) : commentaire de 2 pages ;
    - Shute (2011) : chapitre de livre, et le lien menait à un autre texte ;
    - Cheng et al. (2026) : mini-revue. La phrase citée était un avis des auteurs ; un seul
      relecteur, acceptée en 15 jours, jamais citée.
  - **Second tri (accès).** 22 articles payants retirés. 13 articles en libre accès les
    remplacent :

    | Idée du plan | Article payant retiré | Remplaçant gratuit |
    |---|---|---|
    | Evidence-Centered Design | Mislevy et al. (2003) | Arieli-Attali et al. (2019), *Frontiers in Psychology* |
    | Évaluation furtive | Shute (2011) | Shute et al. (2016), PDF de l'autrice |
    | Spécificité du cas, généralisabilité | Eva (2003), Norman et al. (2006), Bloch & Norman (2012) | Trejo-Mejía et al. (2016), PubMed Central |
    | Évaluation programmatique | van der Vleuten et al. (2012) | Heeneman et al. (2021), libre accès |
    | Courbes d'apprentissage | Pusic et al. (2015) | Howard et al. (2023), PubMed Central |
    | Gain et changement normalisés | Hake (1998), Marx & Cummings (2007) | Nissen et al. (2018), libre accès |
    | Oubli | Arthur et al. (1998) | Legoux et al. (2021), PubMed Central |
    | Méthode Delphi | Humphrey-Murto et al. (2017) | Jünger et al. (2017, CREDES), version acceptée |
    | Kalamazoo | Makoul (2001) | Joyce et al. (2010), PubMed Central |
    | Calgary-Cambridge | Kurtz et al. (2003) | Simmenroth-Nayda et al. (2014), libre accès |
    | Erreurs non compensables | Payne et al. (2008) | Homer & Russell (2021), version acceptée |
    | Seuils (Angoff) | McKinley & Norcini (2014) | Dwyer et al. (2016), libre accès |
    | Validité (Kane) | Cook et al. (2015) | Cook & Hatala (2016), libre accès |
    | Feedback | Hattie & Timperley (2007) | Wisniewski, Zierer & Hattie (2020), méta-analyse en libre accès |

    Retirés sans remplaçant, car l'idée reste appuyée par un autre article de la liste :
    - Motowidlo et al. (1990) : l'origine du format est décrite par Patterson et al. (2016) ;
    - Bergman et al. (2006) et McDaniel et al. (2011) : la cotation est traitée par de Leng et
      al. (2017) et Weng et al. (2018) ;
    - Shrout & Fleiss (1979) et McGraw & Wong (1996) : les formes de l'ICC sont décrites par
      Koo & Li (2016) ;
    - Cohen et al. (1999), sur l'échelle en pourcentage du maximum, et McGaghie et al. (2014),
      sur la maîtrise : les deux points ont été reformulés sans citation.
  - **Liens trouvés pour des articles déjà présents.**
    - Les 5 articles de Lievens, Weng et Kepes ont un PDF direct au dépôt de la Singapore
      Management University. Le lien de Lievens et al. (2005) mène à un manuscrit de l'auteur.
    - Frary (1988) : module PDF sur le site du NCME, l'association qui édite la revue.
    - Lee et al. (2020) : PDF en accès libre chez Wiley.
  - **Liens erronés corrigés.** Pusic et al. (2015) et Michaud & Jucker-Kupper (2016) menaient
    à un autre article ; Mislevy et al. (2003), à un rapport technique.
- **Texte du plan ajusté** pour suivre les nouvelles sources : statut, § 2.1 à 2.9, § 3.1
  (point 5), § 3.4 (tableau), § 3.6, § 7.
- **Textes de l'application alignés.** Trois textes visibles citaient des articles retirés : la
  définition d'une erreur critique (`domain/expert_rubric.py`), les remarques de l'export de la
  clé d'experts (`exporters/expert_key.py`) et la colonne « progression » de l'export
  (`services/export_service.py`). Les commentaires internes du code gardent les auteurs
  d'origine des formules (Marx & Cummings, Shrout & Fleiss), qui sont l'attribution exacte ; le
  test de l'ICC repose sur l'exemple publié par Shrout & Fleiss.
- **Vérification.**
  - Les 33 DOI existent, et aucun article n'est rétracté. Les correctifs publiés sont signalés
    (erratum de Koo & Li 2016).
  - **Les 33 liens ouvrent un PDF**, contrôlés un par un : 17 avec un simple téléchargement,
    les 16 autres dans un navigateur, parce que ces sites bloquent les robots (SMU, PubMed
    Central, BMC, HAL, Hogrefe, Taylor & Francis, Wiley). PubMed Central et HAL font d'abord une
    vérification automatique de quelques secondes, sans rien à cliquer.
  - Le PDF (5 pages) a été relu en images ; ses 33 liens sont identiques à ceux du § 7 et à
    ceux qui ont été vérifiés.
  - Les affirmations du plan ont été recontrôlées sur les résumés des articles, en particulier
    pour les 13 nouveaux.
  - **138 tests verts** (base jetable).
- **Limites.**
  - 7 liens mènent à une version acceptée (texte relu par les pairs, sans la mise en page de la
    revue) et 1 à un manuscrit de l'auteur (Lievens et al. 2005). Ils sont signalés comme tels.
  - Plusieurs remplaçants sont plus récents et moins cités que les classiques retirés. Ceux-ci
    restent les sources d'origine ; on peut les citer dans le mémoire en précisant qu'ils sont
    payants.
  - Le PDF est encore produit par un script temporaire (reportlab, hors du projet), à partir
    de la même liste que le § 7.
- **Fichiers.** `docs/Scoring_v2_recherche_et_plan.md`, `docs/Scoring_v2_bibliographie.pdf`
  (refait), `docs/Journal_de_developpement.md` (annexes A et B), `domain/expert_rubric.py`,
  `exporters/expert_key.py`, `services/export_service.py`.

### 2.27 — 12 oct. · Proposition de scoring v3, fondée sur la lecture des 33 articles

- **Besoin.** Demande de l'étudiant : analyser les PDF de la bibliographie (« ces 32 PDF » ; la
  liste en compte 33) et proposer un scoring adapté au modèle du jeu, bien expliqué, en
  disant pour chaque choix sur quel article il s'appuie et pourquoi.
- **Lecture.**
  - Les 33 articles ont été lus en texte intégral : résumé, méthode utile, résultats et
    discussion.
  - Sources du texte :
    - 22 PDF téléchargés, dont un scan passé en reconnaissance de caractères (Corbett &
      Anderson) ;
    - 8 textes de PubMed Central via Europe PMC ;
    - 11 dans le navigateur (dépôt SMU, Hogrefe, Taylor & Francis, Wiley, PubMed Central).
  - Correction trouvée au passage : l'article de Corbett & Anderson porte la date de **1995**,
    pas 1994. Elle est corrigée dans le § 7 du plan, dans le texte du plan et dans le PDF.
- **Simulation sur le livre 2** (base jetable, vrai calcul serveur), pour chiffrer la
  proposition :
  - 35 à 46 choix notés par passage de chapitre ;
  - marge à 95 % du niveau : ±11,8 points avec 1 passage, ±8,4 avec 2, ±6,9 avec 3 ;
  - au hasard, la meilleure réponse est choisie dans 20,6 % des cas ;
  - fidélité moitié-moitié simulée de 0,85 : c'est un plafond, pas une mesure.
- **Proposition** : [Scoring_v3_proposition.md](Scoring_v3_proposition.md). Elle garde
  l'essentiel du v2 et en corrige trois points.
  1. **Progression.** Gain en points, avec un « progrès net » seulement au-delà de la marge
     et de l'effet de répétition attendu (un tiers d'écart-type). Elle remplace le gain
     normalisé, qui est biaisé (Nissen et al. 2018).
  2. **Bandes.** Seuils fixés par Angoff modifié, par année d'études (Dwyer et al. 2016). Une
     bande n'est donnée que si la marge d'erreur tient dedans ; sinon, l'écran affiche
     « entre deux bandes ».
  3. **Affichage.** Le feedback riche en information d'abord, la note à la demande, aucune
     comparaison entre étudiant·e·s (Wisniewski et al. 2020 ; Shute 2008).

  Elle précise aussi :
  - la clé : formation des cotateurs, médiane, consensus défini à l'avance ;
  - la pondération selon l'âge du passage, avec une demi-vie de 90 jours (Legoux et al. 2021) ;
  - le profil par compétence, présenté comme une tendance (Joyce et al. 2010) ;
  - l'erreur critique : plafond, débriefing, puis levée par un passage propre.

  Elle ajoute :
  - le temps de réponse et les passages trop rapides (Baker et al. 2004) ;
  - le taux de meilleure réponse, calculé en parallèle ;
  - une règle conjonctive pour le livre (Homer & Russell 2021) ;
  - un plan de validation chiffré selon Kane ;
  - un tableau des paramètres et de leur calibrage ;
  - une table des 33 articles, avec où et pourquoi chacun sert.
- **Statut.** Proposition, **rien n'est implémenté**. Le plan v2 renvoie à ce document.
- **Limites.**
  - Aucun article ne porte sur un jeu à embranchements noté sur 7 compétences ; les choix
    d'une scène ne sont pas indépendants, donc les marges sont sans doute sous-estimées.
  - Les études sur la cotation portent sur des échelles de Likert : leurs leçons sont
    transposées, sans preuve directe.
  - La demi-vie, le seuil de temps et l'effet de répétition sont des points de départ, à
    mesurer sur le pilote.
- **Fichiers.**
  - Nouveau : `docs/Scoring_v3_proposition.md`.
  - Modifiés : `docs/Scoring_v2_recherche_et_plan.md` (statut, Corbett 1995, § 7) et
    `docs/Scoring_v2_bibliographie.pdf` (Corbett 1995).

### 2.28 — 12 oct. · Clé de cotation du livre 2, cotée par Claude

- **Besoin.** Demande de l'étudiant : faire coter les réponses par un panel prendrait trop de
  temps, il y en a beaucoup trop. Claude doit donc estimer lui-même les points de chaque
  réponse, en analysant les systèmes de scoring, les chapitres et les programmes.
- **Ampleur.** 424 points de choix, **2 017 réponses**. Pour chacune :
  - 7 compétences cotées de −3 à +3 ;
  - un drapeau « critique » ;
  - une justification d'une phrase.
- **Tour 1, à l'aveugle.**
  - Le texte de chaque chapitre est coté sans aucun point, avec la grille ancrée
    (`domain/expert_rubric.py`) et une consigne écrite.
  - Chaque fichier est contrôlé : complet, lisible, justifié, sans ex aequo au meilleur.
- **Comparaison avec la clé de l'auteur** (ICC(2,1), Koo & Li 2016) :
  - ICC du total : **0,90** (de 0,87 à 0,92 selon le chapitre) ;
  - même meilleure réponse dans **83 %** des points de choix ;
  - la compassion est la seule compétence à l'accord modéré (0,51) ;
  - 163 points de choix sont à revoir.
- **Tour 2.** Revue des 163 points, la clé de l'auteur étant visible : 254 réponses révisées.
  Règles harmonisées :
  - appeler le 144 ou alerter relève de la collaboration, de la clarté et du rôle ; la
    compassion est réservée à la présence et au soulagement ;
  - mentir à l'institution est critique ;
  - quand un autre professionnel mène, rester en retrait ;
  - lever l'anonymat d'un donneur pour de bon est critique ;
  - trahir le secret d'une mineure capable de discernement est critique.
- **Tour 3, contraintes du build** : 28 réponses.
  - La compassion (ch. 2, 4, 5) et la collaboration (ch. 5) étaient en jeu dans moins de 8
    choix sur le parcours le plus court. La compétence a été ajoutée là où l'ancre de la
    grille est réalisée et où l'auteur la mettait déjà en jeu.
  - Les chapitres 1 à 3 ont retrouvé une réponse ≥ +9.
- **Application au livre.**
  - La clé est dans `data/keys/MedStudents_Y2_v2_cle.json`. Pour chaque réponse : cotes,
    critique, justification, tour, et pour la traçabilité la cote de l'auteur et celle du
    tour 1.
  - `scripts/medstudents_y2_v2/key.py` l'applique à l'assemblage du livre (`book.py`). Les
    sources ch1…ch5 gardent la clé de l'auteur.
  - Si une réponse a été réécrite, ajoutée ou retirée depuis la cotation, le build s'arrête.
  - Le JSON du livre porte maintenant `Critical` (114 réponses) et `Rationale` (toutes les
    réponses des points de choix).
- **Résultat.**
  - Clé finale contre auteur : ICC 0,93 et même meilleure réponse dans 92 %. Ces chiffres ne
    sont pas indépendants, car le tour 2 a vu l'auteur.
  - Audit du score : au hasard ≈ 46/100 ; stratégies fondées sur la longueur ≤ 59/100 ;
    chaque compétence notée sur tous les parcours.
  - L'échelle est plus serrée que celle de l'auteur : meilleure réponse +4,8 en moyenne,
    contre +6,1. D'où 49 avertissements « éventail étroit ». La note n'en dépend pas : elle
    est relative à chaque point de choix.
  - 140 tests verts (2 nouveaux : la clé couvre toutes les réponses ; une réponse réécrite
    arrête le build).
- **Limites.**
  - Un seul cotateur, une IA, qui avait aussi aidé à écrire la clé de l'auteur : les biais
    peuvent être partagés.
  - Le tour 2 n'est pas à l'aveugle.
  - Le tour 3 a été guidé par le build.
  - La clé reste **provisoire**. Il est recommandé de faire relire par 2 ou 3
    enseignant·e·s les 36 points dont la meilleure réponse a changé et les 114 réponses
    critiques.
- **Fichiers.**
  - Nouveaux : `data/keys/MedStudents_Y2_v2_cle.json`, `scripts/medstudents_y2_v2/key.py`,
    `docs/MedStudents_Y2_v2_cle.md`.
  - Modifiés :
    - `scripts/medstudents_y2_v2/book.py` (applique la clé) ;
    - `tests/test_medstudents_y2_v2.py` (2 tests) ;
    - `templates/expert_key.html.jinja` (la clé du jeu n'est plus forcément celle de
      l'auteur) ;
    - `data/README.md` ;
    - `docs/Scoring_v2_recherche_et_plan.md` (statut).
  - Régénérés par le build : `data/chapters/MedStudents_Y2_v2.json`,
    `docs/MedStudents_Y2_v2_soft_skills.md` et `.json`.
- **Suite (13 oct.).** La justification et le marquage critique sont montrés au joueur :
  voir § 2.29.

### 2.29 — 13 oct. · Le joueur voit la justification de la clé et les réponses critiques

- **Besoin.**
  - Depuis le § 2.28, chaque réponse du livre 2 a une justification d'une phrase
    (`Rationale`) et, pour 114 d'entre elles, un drapeau « critique ». Le joueur ne les
    voyait pas.
  - La proposition v3 (§ 2.27, « feedback d'abord ») demande de montrer d'abord ce qui était
    attendu et pourquoi, la note ensuite. Une réponse critique doit être signalée clairement.
  - Le plafond de note en cas de réponse critique n'est **pas** appliqué : la décision est en
    attente.
- **Réalisation.**
  - **Trace de chaque choix** (`replay_scene`) : la justification de la réponse choisie et
    celle de la meilleure réponse s'ajoutent au drapeau critique, déjà présent. Pour un livre
    sans clé, la justification est vide : rien n'est inventé.
  - **Fin de scène** (« Ce qui était attendu ») :
    - l'API d'enregistrement d'une scène renvoie les choix les plus décisifs
      (`scene_review`) ;
    - d'abord toutes les réponses critiques, puis les plus grands écarts au meilleur choix,
      3 au plus ;
    - si tous les choix étaient les meilleurs, le plus décisif, avec son « pourquoi » ;
    - pour chacun : la réplique, la réponse choisie, sa justification, puis la réponse la
      plus ajustée et sa justification ;
    - la carte d'une réponse critique a un liseré rouge, l'étiquette « Critique » et une
      définition en une phrase ;
    - le bloc vient avant les barres de points ; la lecture audio le lit aussi.
  - **Bilan de session** :
    - une carte « Réponses critiques », avec leur nombre, vient **avant** les chiffres
      clés : réponse choisie, réponse attendue, et pourquoi, sans points ;
    - les moments clés (occasions manquées, réussites) affichent la justification sous
      chaque réponse ;
    - une réponse critique n'est pas répétée parmi les occasions manquées.
  - **Feedback IA de fin de livre** : le prompt reçoit les justifications des moments clés et
    les réponses critiques (8 au plus), avec une consigne : les nommer et expliquer pourquoi,
    sans dramatiser ni juger la personne.
  - **Export** : nouvelle colonne `justification` dans la table `choix`, à côté de
    `critique`.
- **Choix et justifications.**
  - Le retour de fin de scène est calculé par le serveur, à partir de la scène rejouée. Il
    n'est pas recalculé par le navigateur : une seule logique, testée en Python.
  - Feedback après l'essai, riche en information (le quoi et le pourquoi) : Shute (2008),
    Wisniewski et al. (2020).
  - Formulation neutre : « Votre réponse », « Plus ajustée », « Pourquoi ». Pas de « vous
    êtes », pas de comparaison entre étudiant·e·s.
  - La définition d'une réponse critique est reprise de la grille
    (`domain/expert_rubric.py`). La phrase sur la règle non compensatoire est omise : le
    plafond n'existe pas encore.
- **Corrections faites en vérifiant.**
  - **Haut de l'écran inaccessible** : l'écran de fin de scène, plus haut que la fenêtre avec
    le nouveau bloc, était centré verticalement. Son haut (titre, verdict) était coupé, sans
    défilement possible. Le centrage passe par des marges automatiques.
  - **Guillemets doublés** : un geste suivi d'une parole (« Poser la main… « Range-le. » »)
    était entouré une seconde fois. Corrigé dans `quoted` (serveur) et dans le jeu.
- **Résultats.**
  - **146 tests verts** (6 nouveaux, 2 adaptés) :
    - la trace garde les justifications ;
    - l'ordre du retour de fin de scène ;
    - rien pour un livre sans clé ;
    - réponses critiques à part des occasions manquées ;
    - guillemets ;
    - parcours complet : API, bilan, prompt IA, export.
- **Vérification.**
  - Navigateur, base jetable (`eol-jetable`) : scène 1.1 du livre 2 jouée avec une réponse
    critique (« Envoie-la-moi aussi, pour réviser. ») et deux réponses moyennes.
  - Le retour de fin de scène montre 3 cartes : la critique d'abord.
  - Le bilan (session en cours) montre la carte « Réponses critiques » avant les notes, et
    les justifications dans les moments clés.
  - Mise en page vérifiée sur ordinateur et sur mobile (375 px, sans défilement horizontal).
    Aucune erreur dans la console.
- **Limites.**
  - Les choix enregistrés avant le 13 oct. n'ont pas de justification dans leur trace : ni
    le bilan ni l'export ne la montrent pour eux. Les bilans de sessions déjà terminées
    n'ont pas la carte « Réponses critiques ».
  - Pas de plafond de note, pas d'alerte de débriefing pour le formateur (proposition v3,
    étape A, points 6 et 8, en attente de décision).
  - Le verdict de fin de scène (« Bon parcours dans l'ensemble… ») ne tient pas compte d'une
    réponse critique.
  - Les justifications sont celles de la clé provisoire, cotée par Claude (§ 2.28).
- **Problème relevé, hors périmètre.** Flask n'échappe pas le HTML des gabarits
  `.html.jinja` (l'échappement automatique ne vaut que pour `.html`). Un nom affiché
  contenant du HTML s'exécuterait dans le tableau de bord du formateur. La nouvelle
  justification est échappée explicitement ; le reste est à corriger (§ 7.1).
- **Fichiers.**
  - Modifiés :
    - `services/scoring_service.py` : `rationale` dans la trace, `critical_choices`,
      `scene_review`, `key_moments(exclude_critical=…)`, `quoted` ;
    - `views/session_api.py` : `review` dans la réponse d'enregistrement d'une scène ;
    - `services/feedback/prompt.py`, `services/export_service.py` ;
    - `templates/session_report.html.jinja`, `templates/play.html.jinja` ;
    - `static/play/main.js`, `static/play.css`, `static/account.css` ;
    - `README.md` ;
    - tests : `tests/test_scoring_service.py`, `tests/test_session_flow.py`,
      `tests/test_passages.py`.

### 2.30 — 13 oct. · Test de bout en bout de la clé et du bilan, gardé en base

- **Besoin.** Demande de l'étudiant : tester le nouveau système sur une vraie partie, et
  **garder** le résultat pour le voir sur la fiche de performance d'un joueur.
- **Réalisation.**
  - La base locale `instance/eol.db` a d'abord été sauvegardée dans
    `instance/eol-backup-2026-10-13-avant-test-cle.db`.
  - Un compte participant `test.cle.y2` (« Test clé Y2 (joueur simulé) ») a été créé. Il
    utilise le mot de passe commun des comptes de démo, déjà dans
    `instance/demo_credentials.txt`, où le compte est ajouté à la liste.
  - Une partie complète du livre 2 a été jouée via l'API, comme le navigateur (mêmes
    règles que `seed_demo.py`) : 5 chapitres, 30 scénarios notés, 208 choix. Le joueur
    simulé ressemble à un·e étudiant·e moyen-bon :
    - 110 fois la meilleure réponse ;
    - 49 fois la 2ᵉ ;
    - 41 fois une réponse moyenne ;
    - 8 fois la pire.
- **Résultats** (session n° 15, page `/sessions/15`) :
  - note de la session 76/100, note du livre 75,7 ;
  - chapitres de 69 (ch. 4) à 79 (ch. 3) ;
  - point fort : frontières professionnelles (83) ; à travailler : compassion (51) ;
  - **3 réponses critiques** affichées en tête du bilan, chacune avec sa justification et la
    réponse attendue : demander la photo du tatouage en 1.1, et deux fois laisser Noah seul
    en 4.3 ;
  - occasions manquées et réussites, toutes avec leur justification.
- **Vérification.**
  - Les pages `/me` et `/sessions/15` ont été rendues par le serveur pour ce compte (statut
    200, contenu relu).
  - La fiche a ensuite été ouverte dans le navigateur, sur le serveur habituel (`eol`) : pas
    d'erreur dans la console.
  - À l'ouverture, le bilan a produit le feedback automatique par règles (« IA
    indisponible »), car aucune clé d'API n'est configurée.
- **Limites.** C'est un joueur simulé, pas un·e étudiant·e : il teste la chaîne (clé, rejeu
  serveur, notes, bilan), pas la difficulté réelle du livre.
- **Fichiers.** Aucun fichier du dépôt n'est modifié. Seule la base locale change (compte et
  session de test), ainsi que `instance/demo_credentials.txt`, qui n'est pas versionné.

### 2.31 — 13 oct. · Profil de compétences en diagramme en rose

- **Besoin.** Demande de l'étudiant, avec une image modèle : sur les fiches des participants,
  remplacer les histogrammes du profil de compétences par un diagramme « camembert » du même
  style, avec le pourcentage de chaque compétence.
- **Réalisation.** Le profil devient un diagramme en rose (diagramme de Nightingale) : 7 parts
  égales, une par compétence. `skillRose` (`static/account/charts.js`) remplace `skillBars`.
  - **Rayon.** Il est proportionnel au score sur 100. Cercles pointillés à 25, 50, 75 et
    100 %, avec un axe gradué.
  - **Couleurs.** Celles du modèle, dans l'ordre 1 à 7 : rouge, orange, jaune, vert, bleu,
    indigo, violet. Contour foncé.
  - **Étiquettes.** Chaque compétence a son étiquette autour du cercle : numéro, nom,
    **pourcentage** dans sa couleur, et « ▲ Point fort » / « ▼ À travailler ». Un trait de
    rappel coloré part d'un point posé sur la part.
  - **Comparaison.** La session précédente est montrée par un arc pointillé dans chaque part.
  - **Non évalué.** Une compétence non évaluée est une part grisée, marquée « non évalué ».
  - **Lecture.** Chaque part a une infobulle et se lit au clavier (focus, `aria-label`).
- **Choix et justifications.**
  - Le rayon est linéaire, avec des cercles également espacés, comme dans le modèle : on lit
    directement le pourcentage sur la grille.
  - Pour le texte, chaque couleur a une variante plus foncée, lisible sur fond clair (le
    jaune en particulier).
  - Sous 560 px de large, le texte du SVG deviendrait illisible. Les étiquettes laissent
    alors la place à des pastilles numérotées, avec une liste colorée sous le graphique
    (nom, pourcentage, point fort ou à travailler).
  - Le cadre du SVG se resserre sur le dessin (`getBBox`).
  - L'apparition est animée, sauf si la personne a demandé de réduire les animations.
  - Cela revient sur la décision 22 du § 4 (barres triées), à la demande de l'étudiant.
- **Où.**
  - Le bilan de session (`/sessions/<id>`), dont la légende montre une pastille aux 7
    couleurs et un arc pointillé.
  - La page « Mon parcours » (`/me`), que le formateur voit aussi pour chaque participant.
- **Vérification.**
  - Dans le navigateur, sur la session de test du § 2.30 : bureau et mobile (375 px, liste
    sous le graphique, pas de défilement horizontal), sans erreur dans la console.
  - Avec des valeurs fictives, injectées dans la page puis retirées : arcs de comparaison et
    part non évaluée.
  - 146 tests verts.
- **Fichiers.**
  - `static/account/charts.js`, `static/account/report.js`, `static/account/history.js` ;
  - `static/account.css` : styles de la rose ; ceux des barres sont retirés ;
  - `templates/session_report.html.jinja` : légende.

### 2.32 — 13 oct. · Bibliographie réduite aux articles qui servent au scoring (33 → 27)

- **Besoin.** Question de l'étudiant : « est-ce qu'on utilise vraiment toutes les
  références ? » Réponse : non. Après examen de chaque article face au code :
  - 16 justifient une règle en place ;
  - 7 l'ont inspirée en partie ;
  - 4 fondent une étape prévue (plafond critique, seuils Angoff, validation, pilote) ;
  - 6 ne servaient que de contexte. Sur recommandation, l'étudiant a demandé de retirer ces 6.
- **Articles retirés.**
  - Arieli-Attali et al. 2019 (Evidence-Centered Design étendu) ;
  - Shute et al. 2016 (évaluation furtive) ;
  - Lievens & Sackett 2012 (validité prédictive des SJT) ;
  - Kepes et al. 2025 (revue des SJT) ;
  - Harenbrock et al. 2023 (fidélité test-retest) ;
  - Pelánek 2016 (système Elo).
- **Réalisation.**
  - **Plan de scoring.**
    - Le § 7 est régénéré : 27 références, avec un troisième critère, « sert au scoring ».
    - Les phrases du § 2 qui citaient les articles retirés sont supprimées ou reformulées.
    - Le statut est mis à jour.
  - **PDF de la bibliographie** régénéré : 27 articles, 4 pages, daté du 13 oct.
  - **Proposition v3.**
    - Titre et introduction corrigés.
    - Constats 1, 2, 4, 9 et 10 sans les articles retirés.
    - § 2.2, § 2.3 et § 2.6 sans les articles retirés.
    - Plan de validation : la cible de fidélité test-retest devient « à mesurer » (source :
      Hausknecht et al. 2007) ; l'extrapolation n'a plus de chiffre tiré de la littérature
      (source : Cook & Hatala 2016).
    - Étape D sans le système Elo.
    - Tableau final : 27 articles.
- **Choix.**
  - Les entrées historiques du journal (§ 2.26 et § 2.27) restent telles quelles : elles
    décrivent ce qui a été fait le 12 oct.
  - Les valeurs chiffrées du jeu (8 choix, 7 jours, poids 0,25) ne viennent d'aucun article :
    les articles justifient le principe, et les valeurs restent à calibrer sur un pilote.
- **Limites.**
  - Deux articles gardés vont en partie contre le système actuel :
    - Nissen et al. 2018 critique le gain normalisé, utilisé pour la progression ;
    - Weng et al. 2018 trouve peu valide la cote brute.
  - Ils restent dans la liste, car la proposition v3 s'appuie sur eux pour corriger ces deux
    points.
- **Fichiers.** `docs/Scoring_v2_recherche_et_plan.md`, `docs/Scoring_v2_bibliographie.pdf`,
  `docs/Scoring_v3_proposition.md`, `docs/Journal_de_developpement.md` (annexes A et B, § 1.1).

### 2.33 — 13 oct. · Scoring v3, étape A : bandes, plafond critique, progression en points, temps de réponse

- **Besoin.** Demande de l'étudiant : faire toutes les tâches de scoring possibles tout de
  suite, sans enseignant·e·s ni étudiant·e·s. Ce sont les points 1 à 6 de l'étape A de la
  proposition v3 (§ 2.27).
- **Réalisation.**
  1. **Plafond en cas d'erreur critique.**
     - Si le dernier passage compté d'un chapitre contient une réponse critique, la bande du
       chapitre ne dépasse pas « À consolider », quelle que soit la note. La note elle-même
       ne change pas.
     - Un passage compté suivant, sans réponse critique, lève le plafond.
     - Le formateur voit une carte « À débriefer » dans son tableau de bord, avec les
       réponses en cause, et un « ! » dans la matrice des chapitres.
     - Le participant voit une carte « Réponses critiques à revoir », avec le pourquoi.
  2. **Progression en points.**
     - Gain = moyenne pondérée des passages suivants − 1ᵉʳ passage, avec sa marge.
     - « Progrès net » seulement si le gain dépasse sa marge et un tiers de l'écart-type de
       la cohorte (cohorte d'au moins 10 personnes). Sinon : « progrès probable, pas encore
       démontré », « baisse nette » ou « pas de changement démontré ».
     - Le changement normalisé, critiqué par Nissen et al. 2018, n'est plus affiché. Il
       reste une version dans l'export, avec une note.
  3. **Bandes** Insuffisant, À consolider, Compétent, Avancé (seuils provisoires 60, 75, 90).
     - Elles sont données avec leur marge : « entre À consolider et Compétent » si
       l'intervalle déborde d'une bande.
     - Au livre, la règle conjonctive s'applique : pas au-dessus d'« À consolider » si un
       chapitre est « Insuffisant » ou garde une réponse critique.
  4. **Temps de réponse.**
     - Le navigateur mesure le temps entre l'affichage des réponses et le clic, et l'envoie
       avec chaque scène. Il est gardé dans la trace et dans l'export.
     - Un passage où plus d'un quart des choix sont faits en moins de 2 secondes (sur au
       moins 8 choix chronométrés) est « trop rapide ». Il ne compte pas, et le suivant peut
       compter tout de suite.
     - Le formateur voit ces passages dans « À débriefer ».
  5. **Poids selon l'âge.**
     - Un passage pèse 2^(−âge / 90 jours) au lieu de 1 + 0,25 × (n − 1) : 1 aujourd'hui,
       0,5 à 90 jours.
     - « À rafraîchir » s'affiche si le dernier passage compté a plus de 90 jours.
  6. **Fin de scène.** Une réponse critique donne un bilan « dur », même si la note de la
     scène est bonne : « Une réponse critique dans ce scénario… Voyez ci-dessous ce qui était
     attendu. » Le drapeau critique est maintenant envoyé au navigateur avec chaque réponse ;
     les points l'étaient déjà.
- **Où cela se voit.**
  - Page « Mon parcours » : bande et marge du livre, progression en points, colonne
    « Bande », « à rafraîchir », passages trop rapides, réponses critiques à revoir.
  - Sommaire du livre : bande de chaque chapitre.
  - Fin de chapitre : bande, plafond, progression, passage trop rapide.
  - Bilan de session : bande du livre.
  - Tableau de bord du formateur.
  - Export : `bande`, `plafond_critique`, `gain_points`, `marge_gain`, `progres`,
    `a_rafraichir`, `trop_rapide`, `choix_rapides`, `temps_median_s`, `reponses_critiques`,
    `temps_s`.
- **Choix et justifications.**
  - Le plafond porte sur la bande, pas sur la note : un décompte d'erreurs est moins fiable
    qu'une note, et on ne décide rien sur un seul point de mesure (Homer & Russell 2021 ;
    Heeneman et al. 2021). Le débriefing humain est l'ingrédient efficace (Lee et al. 2020).
  - Seuil de 2 secondes, 25 % des choix et 8 choix au minimum : valeurs de départ. Aucun
    article ne fixe de seuil (Baker et al. 2004) : elles se calibrent sur le pilote.
  - Les passages notés avant aujourd'hui gardent leurs résultats. Leurs réponses critiques
    sont recomptées depuis les traces.
  - Le texte des gabarits ajoutés est échappé explicitement (`| e`). L'échappement
    automatique reste à activer (§ 7.1).
- **Vérification.**
  - **158 tests verts** (12 nouveaux) :
    - poids selon l'âge, gain et marge, statut du progrès, bandes et marge ;
    - plafond critique et sa levée, règle conjonctive du livre, « à rafraîchir » ;
    - passage trop rapide (unité et parcours complet), temps mal formés ignorés ;
    - plafond et débriefing de bout en bout ;
    - fin de scène critique (test JavaScript).
  - Dans le navigateur, sur la base locale (serveur `eol`) :
    - le joueur de test du § 2.30 a une note de livre de 75,7 ± 4, plafonnée à « À
      consolider » par ses réponses critiques des chapitres 1 et 4 ;
    - le tableau de bord du formateur de démo liste ces 3 réponses dans « À débriefer » ;
    - la page de jeu se charge sans erreur, et le moteur donne un bilan « dur » après une
      réponse critique.
- **Limites.**
  - Les seuils des bandes, du temps et du progrès net sont provisoires : Angoff et pilote.
  - L'écart-type de cohorte n'existe qu'à partir de 10 personnes ; avant, seule la marge
    décide du « progrès net ».
  - Restent dans l'étape A :
    - le point 7 : taux de meilleure réponse et *d* de Cohen du groupe ;
    - le point 8 : écran « feedback d'abord, note à la demande » et page qui explique la
      notation.
- **Fichiers.**
  - Code : `services/scoring_service.py`, `services/history_service.py`,
    `services/session_service.py`, `services/graph_service.py`, `services/export_service.py`,
    `views/session_api.py`, `views/account.py`, `views/pages.py`.
  - Interface : `static/play/engine.js`, `static/play/main.js`, `static/account.css`,
    `templates/account_history.html.jinja`, `templates/trainer_dashboard.html.jinja`,
    `templates/play_book.html.jinja`, `templates/session_report.html.jinja`.
  - Tests : `tests/test_scoring_service.py`, `tests/test_passages.py`,
    `tests/js/engine.test.mjs`, `tests/test_play_engine.py` (nouveaux pour les deux derniers).
  - Documents : `docs/Scoring_v3_proposition.md`, `docs/Scoring_v2_recherche_et_plan.md`
    (statuts).

### 2.34 — 13 oct. · Scoring v3, fin de l'étape A et outils des étapes B et C

- **Besoin.** Demande de l'étudiant : « fais le reste ». C'est tout ce qui peut se faire sans
  enseignant·e·s ni étudiant·e·s ; pas de sauvegarde dans git, à sa demande.
- **Réalisation.**
  1. **Taux de meilleure réponse** (étape A, point 7), calculé à côté de la qualité : part des
     choix où la meilleure réponse a été choisie (cotation dichotomique, environ 20 % au
     hasard). Il est dans les résultats de chaque passage et dans l'export
     (`taux_meilleure_reponse`).
  2. **Progrès du groupe** (point 7) : dans le tableau de bord du formateur, par chapitre, le
     *d* de Cohen entre le 1ᵉʳ et le dernier passage, avec les moyennes, les écarts-types et
     la corrélation (Nissen et al. 2018).
  3. **Feedback d'abord** (point 8).
     - **Fin de scène** : « Ce qui était attendu » vient en premier ; les points de la scène
       sont repliés sous « Voir les points ».
     - **Fin de chapitre**, dans l'ordre :
       - « Ce qu'il faut retenir de ce chapitre » : les 3 choix les plus décisifs du
         passage, les réponses critiques d'abord, avec leur scène et le pourquoi ;
       - la bande, et la mention de progrès ;
       - les points forts et à travailler ;
       - la note sur 100 et les points, seulement sous « Voir la note ».
     - Pas de comparaison avec les autres (Shute 2008 ; Wisniewski et al. 2020).
  4. **Page « Comment est-ce noté ? »** (`/notation`, point 8). Elle reprend les valeurs du
     code (seuils, délais, temps), avec des exemples et les formules. Elle est accessible depuis
     l'écran d'entrée de chaque chapitre, la fin de chapitre, « Mon parcours » et le
     sommaire. Il faut dire comment le test est noté (Frary 1988), dans un climat où la note
     sert à apprendre (Heeneman et al. 2021).
  5. **Grille de relecture ciblée** (étape B) dans `/trainer/cle/` : 186 réponses. Ce sont les
     deux réponses en concurrence aux 36 points où la clé actuelle diffère de l'auteur, et
     les 114 réponses critiques ; elles sont lues dans `data/keys/`.
  6. **Seuils par la méthode d'Angoff** (étape B), dans la même page.
     - Une grille Excel à l'aveugle : pour chaque point de choix, chaque juge indique la
       réponse que choisirait un·e étudiant·e « tout juste compétent·e ».
     - Import des grilles, nouvelle table `angoff_ratings`.
     - Le seuil d'un·e juge est la qualité des choix de cet·te étudiant·e imaginaire. La
       médiane des juges devient le seuil « Compétent » du chapitre dès 3 juges ;
       « À consolider » et « Avancé » restent à 15 points de part et d'autre.
     - Ces seuils s'appliquent partout : bandes des chapitres et du livre, fin de chapitre,
       sommaire, tableau de bord, export. Les seuils du livre sont la moyenne de ceux de ses
       chapitres.
  7. **Protocole du pilote** (étape C) :
     [Pilote_protocole.md](Pilote_protocole.md). Il décrit les valeurs à calibrer, les
     participant·e·s, le calendrier (avec un chapitre témoin jamais rejoué), les analyses
     faites à partir de l'export, les règles de décision et l'éthique.
- **Choix et justifications.**
  - **Angoff « réponse la plus probable »** plutôt que des probabilités par réponse : une
    seule décision par point de choix, plus rapide pour les juges, et qui se calcule comme
    la note d'un joueur.
  - **Un seul seuil jugé, les deux autres à 15 points** : c'est l'écart des seuils
    provisoires. Ce choix est à revoir si le pilote le contredit.
  - La note sur 100 reste accessible : elle est cachée, pas supprimée.
- **Vérification.** **166 tests verts** (8 nouveaux) :
  - relecture ciblée ;
  - seuils Angoff (calcul, 3 juges au minimum ; aller-retour de la grille, application aux
    bandes, grille invalide refusée) ;
  - bandes avec seuils de juges ;
  - taux de meilleure réponse ;
  - *d* de Cohen ;
  - page d'explication ;
  - retour de fin de chapitre ;
  - progrès du groupe.
- **Limites.** Les étapes B et C demandent des personnes : la relecture de la clé, au moins
  3 juges pour les seuils, et le pilote.
- **Fichiers.**
  - Nouveaux :
    - `services/angoff_service.py`, `repositories/angoff_ratings.py`, `exporters/angoff.py`,
      `views/scoring_context.py` ;
    - `templates/scoring_explained.html.jinja`, `docs/Pilote_protocole.md`.
  - Modifiés :
    - `repositories/orm.py` (table `angoff_ratings`) ;
    - services : `scoring_service`, `history_service`, `expert_key_service`, `export_service` ;
    - vues : `views/expert_key.py`, `views/account.py`, `views/pages.py`, `views/session_api.py` ;
    - gabarits : `templates/play.html.jinja`, `expert_key`, `trainer_dashboard`,
      `account_history`, `play_book` ;
    - interface : `static/play/main.js`, `static/shared/skills.js`, `static/play.css`,
      `static/account.css` ;
    - tests : `tests/test_expert_key.py`, `tests/test_scoring_service.py`,
      `tests/test_passages.py` ;
    - documents : `docs/MedStudents_Y2_v2_cle.md` (relecture ciblée : 186 réponses, grille
      disponible), `docs/Scoring_v3_proposition.md` (statut : étape A faite, outils des
      étapes B et C en place) et `docs/Scoring_v2_recherche_et_plan.md` (statut : renvoi au
      § 2.34 et au protocole du pilote).

---

## 3. Architecture technique au 6 octobre 2026

### 3.1 Couches (Clean Architecture, héritée du commit du 6 mai et étendue)

| Couche | Ajouts pendant la période |
|---|---|
| **Domaine** (`domain/`) | Le format des livres s'enrichit, sans casser la compatibilité : états narratifs, conditions, emplacements, points d'entrée, bilans par issue, choix de départ, annexes, réponses critiques et justifications ; `expert_rubric.py` (grille ancrée provisoire) |
| **Dépôts** (`repositories/`) | `database.py` (moteur SQLAlchemy, SQLite ou PostgreSQL), `orm.py` (modèles `User`, `BookSession`, `ChapterPassage`, `SceneAttempt`, `ExpertRating`), `users.py`, `sessions.py`, `passages.py`, `expert_ratings.py` |
| **Services** (`services/`) | `scoring_service` (qualité des choix, niveaux, profil du livre), `session_service` (sessions et passages), `history_service`, `scoring_upgrade` (reprise des données v1), `expert_key_service` (grille d'experts, accord ICC), `auth_service`, `feedback/` (IA et règles de secours), `export_service` ; extension de `graph_service` (contenu narratif servi au jeu) et de `validation_service` (points d'entrée) |
| **Vues** (`views/`) | `auth`, `guards` (connexion, rôle, CSRF), `session_api`, `account` (historique, bilans, espace formateur, export), `expert_key` (validation de la clé) ; routes `/play/…` dans `pages` |
| **Exporteurs** (`exporters/`) | `tables.py` : écriture xlsx, csv et json ; `expert_key.py` : grille d'experts et synthèse |
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
| `/trainer/cle/` | validation de la clé de cotation par des experts |

### 3.3 Base de données

| Table | Contenu |
|---|---|
| `users` | identifiant, nom affiché, mot de passe haché, rôle |
| `book_sessions` | n° de session, statut, chapitres terminés, résultats figés, feedback |
| `scene_attempts` | choix, scores, bornes des réponses proposées, tentative notée ou non |
| `chapter_passages` | passage de chapitre : noté ou d'entraînement, dates, états de départ, résultats (scoring v2) |
| `passage_attempts` | scènes jouées pendant chaque passage |
| `expert_ratings` | cotes des experts : réponse, expert, tour, points, critique, justification |

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
    *Remplacé le 13 oct. par un diagramme en rose, à la demande de l'étudiant (§ 2.31).*

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
| 6 oct. (scoring v2) | 110 | qualité des choix, passages, règle d'espacement, niveaux, reprise v1 |
| 6 oct. (clé d'experts) | 116 | ICC (exemple de Shrout & Fleiss), grille à l'aveugle, import, synthèse, marqueur critique |
| 10 oct. (Y2 refondu) | 123 | 5 chapitres de 5-6 scénarios, ~500 interactions, audit du score (meilleure, pire, hasard, longueur, preuves par compétence), le build refuse ex aequo et indice de longueur |

| 10 oct. (lecture audio) | 126 | page de jeu avec la lecture audio, modules servis, 8 tests JavaScript de préparation du texte (via Node) |
| 12 oct. (voix naturelles) | 138 | voix serveur : cache, validation, limites, choix du moteur, Azure simulé, API, synthèse Piper réelle |
| 12 oct. (clé IA du Y2) | 140 | la clé couvre toutes les réponses des points de choix ; une réponse réécrite depuis la cotation arrête le build |
| 13 oct. (justification au joueur) | 146 | justification dans la trace, retour de fin de scène, réponses critiques dans le bilan, prompt IA et export, guillemets |
| 13 oct. (scoring v3, étape A) | 158 | poids selon l'âge, progression en points, bandes et marge, plafond critique et sa levée, règle conjonctive, passages trop rapides, fin de scène critique (JavaScript) |

| 13 oct. (fin de l'étape A, outils B et C) | **166** | relecture ciblée, seuils Angoff, taux de meilleure réponse, *d* de Cohen, page d'explication, retour de fin de chapitre |

Vérifié le 13 octobre : `166 passed`.

### 5.2 Validation automatique des livres (au build)

- Liens entre interactions (règle EG-7) et points d'entrée.
- Atteignabilité de chaque interaction, et terminaison de chaque chemin.
- Cohérence des états : aucun état lu sans être posé ; aucun état posé dans plusieurs chapitres.
- Une seule scène jouable par emplacement, pour toutes les combinaisons d'états possibles.
- Chaque issue d'une scène clé pose exactement un état de son groupe.
- 4 à 6 réponses par point de choix.
- Au moins une réponse très bonne (≥ +9) et une très mauvaise (≤ −7) par chapitre.
- Rapport des soft skills régénéré à chaque build, et un test vérifie qu'il est à jour.
- Depuis le 10 octobre (livre 2) : une seule meilleure réponse par point de choix ; aucune
  stratégie fondée sur la longueur des réponses au-delà de 62/100 ; chaque compétence en jeu
  dans au moins 8 choix sur le parcours le plus court ; audit du score (rejeu serveur) dans le
  rapport.
- Depuis le 12 octobre (livre 2) : la clé de cotation (`data/keys/`) est appliquée à
  l'assemblage ; le build s'arrête si une réponse a changé depuis la cotation.

### 5.3 Vérifications dans le navigateur

- Toujours faites sur une **base de données jetable**, pour ne pas toucher la base locale.
- Faites : jeu complet (Y4 v2 voies erreur et évitée, Y2 v2 chapitre 1), historique, bilan,
  espace formateur, CSRF, palette, mise en page sur ordinateur et mobile, export.
- Faites le 6 octobre (scoring v2) : espace formateur, matrice des chapitres, historique et
  courbes, bilan de session, chapitre 4 du Y2 joué en entier puis rejoué en entraînement.
- Faites le 10 octobre (Y2 refondu) : chapitre 5 joué en entier, puis ses choix rejoués hors
  ligne pour retrouver la note stockée.
- Faites le 13 octobre (justification au joueur) : scène 1.1 du Y2 jouée avec une réponse
  critique ; retour de fin de scène et bilan de session, sur ordinateur et sur mobile.
- **Non faites** :
  - chapitres 1 à 4 du livre Y2 refondu joués à la main (build et parties simulées seulement) ;
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
| 7 oct. | Le nombre de références du plan de scoring était annoncé à 35 ; il y en avait 41 | Corrigé : 43 avec les 2 références sur l'ICC |
| 10 oct. | Clé du Y2 : choisir toujours la réponse la plus longue donnait 89,5/100 | Longueurs équilibrées ; règle bloquante au build (§ 2.23) |
| 10 oct. | Première correction trop forte : « toujours la 2ᵉ plus longue » donnait 93/100 | Rangs de longueur répartis de 1 à 6 |
| 10 oct. | Boucle « on recommence » du BLS : un·e joueur·euse simulé·e tournait à l'infini | Au second passage, le simulateur essaie une autre réponse |
| 10 oct. | Six incohérences au chapitre 5, relevées en jouant (intro de la grange, fenêtre, invitation à la cérémonie, retour chez la Pre Vautier, capture d'écran, âge de Mme Rapin) | Corrigées |
| 13 oct. | Fin de scène plus haute que la fenêtre : le haut (titre, verdict) était coupé, sans défilement | Centrage par marges automatiques (§ 2.29) |
| 13 oct. | Guillemets doublés autour d'un geste suivi d'une parole | `quoted` ne réentoure plus un texte qui a ses guillemets (§ 2.29) |
| 13 oct. | Gabarits `.html.jinja` rendus sans échappement HTML | Relevé, non corrigé (§ 7.1) |

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
- [ ] **Activer l'échappement HTML des gabarits** (`.html.jinja`) : un nom affiché contenant
  du HTML s'exécute aujourd'hui dans les pages du formateur. Relevé le 13 oct. (§ 2.29).

### 7.2 Contenu

- [ ] **Portraits à produire** : 138 pour le Y2 v2, en priorité, et 135 pour le Y4 v2 si ce
  livre est conservé. Aucun n'existe : le jeu affiche les initiales.
- [ ] **Relecture éthique** des scènes sensibles : échographie, erreur médicale, crise
  suicidaire, grossesse d'une mineure, anonymat du don.
- [ ] **Validation par un·e référent·e pédagogique par faculté**, en particulier pour l'UNIGE,
  dont le détail de B2-B3 n'est pas public.
- [ ] Jouer les chapitres 1 à 4 du Y2 refondu dans le navigateur (le chapitre 5 l'a été le
  10 oct.).
- [x] Écart entre la bible et le texte du Y2 (Bernard et Noah à la cérémonie) : bible réécrite
  avec la refonte du 10 oct. (§ 2.23).
- [ ] Livres 1, 3, 5 et 6 du plan, à faire. Le livre 5 « Fin de vie » est identifié comme
  prioritaire.
- [ ] Supprimer le livre Y4, comme prévu par l'étudiant.

### 7.3 Scoring et évaluation

- [x] Étape 1 du scoring v2 : note par choix, passage de chapitre, niveau, progression,
  fiabilité, profil du livre (§ 2.20).
- [x] Étape 2, outils : grille d'experts à l'aveugle, import, accord (ICC), synthèse Delphi,
  champs « critique » et « justification », points affichés comme provisoires (§ 2.21).
- [x] Audit de la clé du Y2 par simulation : indice de longueur supprimé, Compassion
  rééquilibrée, chaque compétence notée sur tous les parcours ; contrôlé à chaque build
  (§ 2.23).
- [x] Clé du livre 2 cotée par Claude (tour à l'aveugle, revue des divergences, calibrage) et
  appliquée au jeu, à titre provisoire (§ 2.28).
- [ ] Faire relire par 2 ou 3 enseignant·e·s la grille ciblée de la clé du livre 2 (186
  réponses : 36 points dont la meilleure réponse diffère de l'auteur, et les 114 réponses
  critiques). La grille est prête dans `/trainer/cle/` (§ 2.34).
- [x] Afficher la justification de la clé et le marquage critique au joueur : fin de scène,
  bilan de session, feedback IA et export (§ 2.29).
- [x] Appliquer le plafond en cas d'erreur critique, avec l'alerte de débriefing pour le
  formateur (§ 2.33).
- [x] Scoring v3, étape A, points 1 à 6 : temps de réponse, gain en points, poids selon
  l'âge, bandes avec marge, règle conjonctive, plafond critique (§ 2.33).
- [x] Scoring v3, étape A, points 7 et 8 : taux de meilleure réponse et *d* de Cohen ;
  écran « feedback d'abord » et page d'explication de la notation (§ 2.34).
- [x] Outils des étapes B et C : grille ciblée, seuils Angoff, protocole du pilote (§ 2.34).
- [ ] Faire valider la grille ancrée ; coter de même le livre 4.
- [ ] Étape 3 : bandes de niveau (Angoff), plafond en cas d'erreur critique, calibrage du
  coefficient 0,25, du délai de 7 jours et du seuil de 8 choix sur un pilote.
- [ ] Faire remplir la grille des seuils par au moins 3 juges (Angoff), puis mener le pilote
  selon [Pilote_protocole.md](Pilote_protocole.md) pour calibrer les valeurs provisoires.
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
| **Validation et résultats** | Évolution des tests (§ 5.1), validation automatique (§ 5.2), chiffres des livres (§ 1.2), répartition des soft skills (§ 2.8), audit de la clé de notation par joueur·euse·s simulé·e·s (§ 2.23) |
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

La liste complète est dans [Scoring_v2_recherche_et_plan.md](Scoring_v2_recherche_et_plan.md),
§ 7 : 27 articles à comité de lecture, chacun avec un lien vers son PDF gratuit et une utilité
pour le scoring (§ 2.32). Il y avait 43 références au 7 oct. (41 au 5 oct., plus 2 sur l'ICC le
6 oct.), 33 après le tri du 12 oct. (§ 2.26).

**Noter les réponses**

1. Patterson, Zibarras & Ashworth (2016). *Situational judgement tests in medical education and
   training: AMEE Guide No. 100.* Medical Teacher, 38(1), 3-17.
2. Weng, Yang, Lievens & McDaniel (2018). *Optimizing the validity of situational judgment
   tests: The importance of scoring methods.* Journal of Vocational Behavior, 104, 199-209.
3. de Leng et al. (2017). *Scoring method of a Situational Judgment Test: influence on internal
   consistency reliability, adverse impact and correlation with personality?* Advances in
   Health Sciences Education, 22(2), 243-265.

**Établir la clé avec des experts**

4. Jünger, Payne, Brine, Radbruch & Brearley (2017). *Guidance on Conducting and REporting
   DElphi Studies (CREDES) in palliative care.* Palliative Medicine, 31(8), 684-706.
5. Koo & Li (2016). *A guideline of selecting and reporting intraclass correlation coefficients
   for reliability research.* Journal of Chiropractic Medicine, 15(2), 155-163.

**Fiabilité**

6. Trejo-Mejía et al. (2016). *Reliability analysis of the objective structured clinical
   examination using generalizability theory.* Medical Education Online, 21, 31650.

**Suivre la progression**

7. Howard, Edwards, Boutis, Alexander & Pusic (2023). *Twelve tips for using learning curves in
   health professions education research.* MedEdPublish, 13, 269.
8. Nissen, Talbot, Nasim Thompson & Van Dusen (2018). *Comparison of normalized gain and
   Cohen's d for analyzing gains on concept inventories.* Physical Review Physics Education
   Research, 14(1), 010115.
9. Pelánek (2017). *Bayesian knowledge tracing, logistic models, and beyond: an overview of
   learner modeling techniques.* User Modeling and User-Adapted Interaction, 27, 313-350.
10. Lievens, Buyse & Sackett (2005). *Retest effects in operational selection settings:
    Development and test of a framework.* Personnel Psychology, 58(4), 981-1007.

**Erreurs critiques et validité**

11. Homer & Russell (2021). *Conjunctive standards in OSCEs: The why and the how of number of
    stations passed criteria.* Medical Teacher, 43(4), 448-455.
12. Cook & Hatala (2016). *Validation of educational assessments: a primer for simulation and
    beyond.* Advances in Simulation, 1, 31.

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
| [Scoring_v2_bibliographie.pdf](Scoring_v2_bibliographie.pdf) | Les 27 articles du scoring (33 avant le 13 oct.), à comité de lecture et en libre accès, classés par usage, chacun avec le lien de son PDF (7 oct., refait le 12 oct.) |
| [Scoring_v3_proposition.md](Scoring_v3_proposition.md) | Proposition de scoring v3 fondée sur la lecture des 33 articles, non implémentée (12 oct.) |
| [Pilote_protocole.md](Pilote_protocole.md) | Protocole du pilote : valeurs à calibrer, calendrier avec chapitre témoin, analyses depuis l'export, règles de décision, éthique (13 oct.) |
| [MedStudents_Y2_v2_cle.md](MedStudents_Y2_v2_cle.md) | Clé de cotation du livre 2 cotée par Claude : méthode en trois tours, accord avec l'auteur, application au build, limites (12 oct.) |
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
