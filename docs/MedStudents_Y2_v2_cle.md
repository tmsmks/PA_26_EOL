# Clé de cotation de MedStudents Y2 v2, cotée par Claude

*12 octobre 2026. Statut : **clé provisoire**. Elle remplace dans le jeu les points écrits par
l'auteur, mais elle n'a pas été validée par des enseignant·e·s.*

## 1. Pourquoi cette clé

Le plan de scoring v2 (étape 2) prévoyait qu'un panel d'experts cote chaque réponse.
Le livre 2 compte **424 points de choix** et **2 017 réponses** à coter sur 7 compétences.
C'est trop pour des personnes. L'étudiant a donc demandé que Claude estime lui-même les
points de chaque réponse, en s'appuyant sur les systèmes de scoring, les chapitres et les
programmes.

Chaque réponse d'un point de choix a reçu :
- une cote de −3 à +3 pour chacune des 7 compétences (seules celles qui sont vraiment en jeu
  sont notées) ;
- un drapeau **critique** quand la réponse met en danger ou viole une règle essentielle ;
- une **justification** d'une phrase.

## 2. Méthode

La démarche suit, en version réduite, celle prévue pour le panel :
1. on cote à l'aveugle ;
2. on compare avec la clé existante ;
3. on revoit les divergences, comme dans un tour de Delphi (Jünger et al. 2017).

### Tour 1 : à l'aveugle (2 017 réponses)

- **Matériel.** Le texte du livre, chapitre par chapitre, **sans aucun point** : situation,
  répliques, puis les réponses numérotées.
- **Grille.** La grille ancrée de `domain/expert_rubric.py` : ce que valent −3, 0 et +3 pour
  chaque compétence. Ses ancrages viennent de PROFILES (Michaud & Jucker-Kupper 2016), de
  Kalamazoo et de Calgary-Cambridge.
- **Consigne.**
  - On cote ce que fait la réponse dans la situation, pour un·e étudiant·e de 2ᵉ année.
  - Ce qu'on attend : écouter, transmettre mot pour mot, vérifier l'identité, appeler le 144,
    dire « pause réelle », poser la question directe du suicide, se taire quand un autre
    professionnel mène.
  - Ce qu'on n'attend pas : un diagnostic, un traitement, un résultat donné, une promesse
    intenable.
- **Règles de cotation.**
  - ±3 : l'ancre est clairement réalisée ; ±2 : nettement ; ±1 : légèrement.
  - Une compétence n'est cotée que si la réponse la met vraiment en jeu (2 à 4 par réponse).
  - Une seule meilleure réponse par point de choix.
  - Le barème du livre (très bon ≥ +9 … très mauvais ≤ −7) sert de repère, pas de cible.
- **Contrôle.** Chaque fichier est contrôlé automatiquement :
  - toutes les réponses sont cotées ;
  - les cotes sont lisibles ;
  - chaque cote a une justification ;
  - il n'y a pas d'ex aequo au meilleur.

### Comparaison avec la clé de l'auteur

L'accord est mesuré par l'ICC(2,1) (deux facteurs, effets aléatoires, accord absolu ;
Koo & Li 2016), avec le calcul de `services/expert_key_service.icc`.

| Chapitre | ICC du total | rd | em | co | er | cc | pb | ic | Même meilleure réponse |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0,87 | 0,81 | 0,79 | 0,49 | 0,66 | 0,58 | 0,80 | 0,75 | 80 % |
| 2 | 0,88 | 0,71 | 0,84 | 0,55 | 0,70 | 0,72 | 0,79 | 0,84 | 81 % |
| 3 | 0,92 | 0,76 | 0,89 | 0,52 | 0,76 | 0,74 | 0,76 | 0,71 | 85 % |
| 4 | 0,92 | 0,79 | 0,76 | 0,49 | 0,53 | 0,66 | 0,81 | 0,71 | 78 % |
| 5 | 0,91 | 0,80 | 0,66 | 0,53 | 0,70 | 0,69 | 0,76 | 0,67 | 95 % |
| **Livre** | **0,90** | 0,78 | 0,80 | **0,51** | 0,68 | 0,68 | 0,79 | 0,76 | **83 %** (353/424) |

- **Accord global.** Il est excellent sur le total. Il est bon sur la plupart des compétences,
  mais seulement modéré sur la **compassion** (0,51).
- **Divergences.** 163 points de choix sont à revoir :
  - 71 ont une meilleure réponse différente ;
  - 156 réponses ont un écart de total ≥ 4, une compétence à ≥ 3 d'écart, ou des totaux de
    signe opposé.

### Tour 2 : revue des divergences, avec la clé de l'auteur visible

Les 163 points ont été relus un à un : 254 réponses ont été révisées.

**Quand la meilleure réponse diffère** (71 points), le choix est tranché point par point.
Il suit l'auteur quand son argument est plus fidèle à la grille ou à l'objectif de la scène.
Il garde la cote du tour 1 sinon.

**Règles harmonisées au passage :**
1. **Appeler le 144, dire « pause réelle », alerter.** C'est de la *collaboration* (ic), de la
   *clarté* (cc) et le *respect du rôle* (pb). La *compassion* est réservée à la présence et
   au soulagement direct. Au tour 1, ces gestes étaient cotés en compassion : c'est l'écart
   principal avec l'auteur.
2. **Compassion.** On la cote dès que l'ancre +3 de la grille est réalisée (« présence,
   geste, aide concrète, orientation vers un soutien »). Le tour 1 en avait coté trop peu.
3. **Mensonges.**
   - Refuser de mentir à l'institution relève des frontières professionnelles (pb +).
   - Mentir à l'institution, c'est pb −3, avec le drapeau critique.
4. **Quand un autre professionnel mène** (médecin, physiothérapeute, régulatrice du 144),
   rester en retrait vaut mieux qu'intervenir, même avec une bonne question.
5. **Anonymat des donneurs.**
   - Lever l'anonymat pour de bon est **critique** : dire le nom, donner des détails
     identifiants en public, publier la lettre.
   - Annoncer l'intention de le faire est très négatif, mais pas critique.
6. **Secret d'une mineure capable de discernement.** Le trahir est **critique**.
7. **Réponses extrêmes.** Les plus graves ont été rapprochées du barème du livre (par
   exemple « Ce n'est qu'un corps » : −4 → −6). On n'a pas ajouté de compétences pour
   atteindre un total.

### Tour 3 : contraintes de mesure du build (28 réponses)

Le build refuse un chapitre si une compétence est en jeu dans **moins de 8 choix** sur son
parcours le plus court. Sous ce seuil, le serveur ne la note pas.

- **Ce qui bloquait.** Avec la clé du tour 2, cela touchait :
  - la compassion aux chapitres 2, 4 et 5 ;
  - la collaboration au chapitre 5.
- **Ce qui a été fait.** Les points des parcours les plus pauvres ont été relus. La
  compétence a été ajoutée seulement là où l'ancre de la grille est réalisée et où l'auteur
  la mettait déjà en jeu. Exemples :
  - « Je ne mentirai pas. Mais je viens avec toi » : co +1 ;
  - « Appeler Yasmine, ou Léo, pour ne pas rester seul·e ce soir » : ic +1.
- **Chapitres 1 à 3.** Ils n'avaient plus de réponse « très bonne » (≥ +9), exigée par le
  livre. La meilleure réponse d'un moment charnière a été relue, et les compétences
  clairement en jeu ont été ajoutées :
  - la story (1.2) ;
  - le résumé à la médecin (2.1) ;
  - l'appel au 144 (3.1).

## 3. Résultat

| | Clé de l'auteur | Tour 1 | Clé finale |
|---|---:|---:|---:|
| Accord avec l'auteur (ICC du total) | — | 0,90 | 0,93 * |
| Même meilleure réponse que l'auteur | — | 83 % | 92 % * |
| Moyenne de la meilleure réponse | +6,1 | +4,6 | +4,8 |
| Moyenne de la pire réponse | −4,5 | −3,4 | −3,6 |
| Réponses ≥ +9 / ≤ −7 | 19 / 51 | 1 / 4 | 6 / 12 |
| Réponses critiques | 0 | 115 | 114 |
| Avertissements « éventail de choix étroit » | 0 | 61 | 49 |

\* Le tour 2 a vu la clé de l'auteur : ces deux chiffres ne sont pas une mesure indépendante.

- **Critiques par chapitre** : 17 / 14 / 20 / 55 / 8. Le chapitre 4 en concentre la moitié :
  l'AVC en simulation, la nuit de Noah et l'appel de 23 h sont des urgences vitales.
- **Échelle plus serrée que celle de l'auteur.** Les deux clés n'ont pas la même densité :
  - la clé finale ne cote que les compétences vraiment en jeu ;
  - l'auteur en cotait davantage par réponse.

  Pour la note, cela ne change rien : elle est relative à chaque point de choix,
  (choisie − pire) / (meilleure − pire). En revanche, 49 points de choix ont un éventail
  « étroit » (meilleure < +4 ou pire > −2). Ce n'est qu'un avertissement du build.
- **Audit du score**, recalculé par le build
  ([MedStudents_Y2_v2_soft_skills.md](MedStudents_Y2_v2_soft_skills.md)) :
  - toujours la meilleure réponse = 100, toujours la pire = 0, au hasard ≈ 46 ;
  - les stratégies fondées sur la longueur des réponses restent sous le seuil de 62/100
    (au plus 59) ;
  - la meilleure réponse est la plus longue dans 30 % des points ;
  - chaque compétence est notée sur tous les parcours.

## 4. Comment la clé est appliquée

- **Fichier de la clé** : `data/keys/MedStudents_Y2_v2_cle.json`.
  - Une entrée par réponse, repérée par `c{chapitre}-s{scène}-i{interaction}-r{rang}`, avec :
    `cotes`, `critique`, `justification`, `tour` (1, 2 ou 3), `auteur` (la cote de
    l'auteur) et `tour1`.
  - `texte` garde le début de la réponse.
- **Application** : `scripts/medstudents_y2_v2/key.py`, appelé par `book.py`, remplace les
  scores des points de choix au moment de l'assemblage.
  - Les sources ch1…ch5 gardent la clé de l'auteur, intacte.
  - Le JSON du livre porte la clé finale, avec `Critical` et `Rationale`.
- **Garde-fou** : si une réponse a été ajoutée, retirée ou réécrite depuis la cotation, le
  build s'arrête et liste les références à mettre à jour. Une cote ne peut donc pas glisser
  sur la mauvaise réponse.
- **Modifier une cote** : changer `cotes` (ou `critique`) dans le fichier, puis lancer
  `.venv/bin/python scripts/build_medstudents_y2_v2.py`. Le build revérifie toute la clé :
  pas d'ex aequo, pas d'indice de longueur, preuves par compétence.
- **Revenir à la clé de l'auteur** : retirer `apply_key(...)` dans `book.py`, puis rebuilder.
- **Ce qui utilise déjà la clé** : la note de chaque choix, le profil par compétence et
  l'export (colonne « critique »).
- **Ce qui ne l'utilise pas encore** : la justification n'est pas encore montrée au joueur,
  et l'erreur critique ne plafonne pas encore la note. Les deux sont prévus par la
  proposition v3 ([Scoring_v3_proposition.md](Scoring_v3_proposition.md)).

## 5. Limites

1. **Un seul cotateur, et c'est une IA.** Ce n'est pas un panel : il n'y a pas de fidélité
   entre juges indépendants à rapporter. La clé de l'auteur a elle aussi été écrite avec
   Claude. L'accord de 0,90 peut donc refléter des biais partagés autant que la justesse
   des cotes.
2. **Le tour 2 n'est pas à l'aveugle.** L'accord final avec l'auteur (0,93) est gonflé par
   construction.
3. **Le tour 3 a été guidé par les contraintes du build.** Les 28 modifications sont
   défendables par la grille, mais elles n'auraient pas été faites sans le seuil de preuves.
4. **Seule l'inférence de cotation est étayée** (Kane ; Cook & Hatala 2016). Rien ne montre
   encore que la note prédise le comportement d'un·e étudiant·e en stage.

**Recommandation.** Faire relire par 2 ou 3 enseignant·e·s un échantillon ciblé plutôt que
les 2 017 réponses, soit **186 réponses** :
- aux **36 points** où la meilleure réponse finale diffère de celle de l'auteur, les deux
  réponses en concurrence (72 réponses) ;
- les **114 réponses critiques**.

Depuis le 13.10.2026, l'outil `/trainer/cle/` produit cette grille à l'aveugle (« Télécharger
la grille ciblée »). Tant que cette relecture n'est pas faite, la clé reste **provisoire**.
