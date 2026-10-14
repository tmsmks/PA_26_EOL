# Protocole du pilote : calibrer et valider le scoring

*13 octobre 2026. Ce protocole prépare l'étape C de la proposition v3
([Scoring_v3_proposition.md](Scoring_v3_proposition.md), § 5). Il décrit ce qu'il faut faire
avec de vrais étudiant·e·s. Tout ce qui pouvait se faire sans elles et eux est déjà en
place (journal, § 2.33 et § 2.34).*

## 1. Ce que le pilote doit trancher

Le scoring repose sur des **valeurs de départ** qu'aucun article ne fixe. Le pilote les
mesure.

| Valeur provisoire | Où | Comment la fixer |
|---|---|---|
| Seuils des bandes (60, 75, 90) | `BAND_THRESHOLDS` | Angoff par 3 juges ou plus avant le pilote (outil `/trainer/cle/`), puis vérification par régression sur les cas limites (§ 4.6) |
| Choix « trop rapide » : 2 secondes, plus d'un quart des choix | `FAST_CHOICE_MS`, `FAST_SHARE` | 5ᵉ centile des temps de réponse (§ 4.3) |
| Demi-vie du poids d'un passage : 90 jours | `LEVEL_HALF_LIFE_DAYS` | La pondération qui prédit le mieux le passage suivant (§ 4.4) |
| 8 choix au moins pour noter une compétence | `MIN_SKILL_EVIDENCE` | Étude de généralisabilité (§ 4.2) |
| 7 jours entre deux passages comptés | `PASSAGE_SPACING_DAYS` | Gain au 2ᵉ passage sur un chapitre rejoué, comparé à un chapitre jamais rejoué (§ 4.5) |

Il doit aussi apporter les premières preuves de validité, selon le cadre de Kane (Cook &
Hatala 2016) :
- **la cotation** : la clé et ses réponses départagent-elles les étudiant·e·s ?
- **la généralisation** : la note est-elle stable d'un passage et d'une scène à l'autre ?
- **l'extrapolation** : dit-elle quelque chose en dehors du jeu ?
- **les conséquences** : le feedback est-il compris et utile, sans stress inutile ?

## 2. Avant le pilote

1. **Relecture ciblée de la clé** par 2 ou 3 enseignant·e·s : la grille ciblée de
   `/trainer/cle/`, soit 186 réponses. Elle contient les deux réponses en concurrence aux 36
   choix où la clé actuelle diffère de l'auteur, et les 114 réponses critiques. On importe les
   grilles, on lit l'accord (ICC) et on corrige la clé (`data/keys/MedStudents_Y2_v2_cle.json`).
2. **Seuils par Angoff.** Au moins 3 juges remplissent la grille des seuils (même page). Pour
   chaque point de choix, ils indiquent la réponse que choisirait un·e étudiant·e de 2ᵉ année
   « tout juste compétent·e ». Les seuils s'appliquent d'eux-mêmes dès 3 juges (Dwyer et al.
   2016). Pour alléger, prendre un échantillon de 15 points de choix par chapitre.
3. **Base de données neuve** pour le pilote (`DATABASE_URL`), et un compte par personne.
4. **Information et consentement** (§ 6).

## 3. Participant·e·s et calendrier

- **Groupe principal** : 30 à 40 étudiant·e·s de 2ᵉ année (UNIL, UNIGE), volontaires.
- **Groupe de comparaison** : 8 à 10 personnes plus avancées (6ᵉ année ou médecins
  assistant·e·s), pour une comparaison de groupes contrastés. Ce n'est pas l'argument
  principal de validité (Cook & Hatala 2016), mais un jeu dont la note ne distingue pas
  novices et expert·e·s ne doit pas servir à noter (Blanié et al. 2020).
- **Tuteurs et tutrices** : un jugement global sur un échantillon d'étudiant·e·s
  (« insuffisant », « limite », « compétent »), pour vérifier les seuils (§ 4.6).

| Semaine | Groupe principal | Groupe de comparaison |
|---|---|---|
| 1 | Lire « Comment est-ce noté ? » (`/notation`), puis chapitres 1 et 2 (1ᵉʳ passage) | Chapitres 1 et 2 |
| 2 | Chapitres 3, 4 et 5 (1ᵉʳ passage) | — |
| 3 et plus, au moins 7 jours après | Chapitres 1 et 2 rejoués (2ᵉ passage). Le chapitre 3 n'est **pas** rejoué : il sert de témoin | — |
| 4 | Court questionnaire (§ 4.8) | — |

Le chapitre 3, jamais rejoué, sert de témoin. Un progrès qui se voit aussi là où l'on n'a pas
rejoué est la meilleure preuve d'apprentissage, car changer de contexte change la mesure
(Lievens & Sackett 2007).

## 4. Analyses

Toutes les données viennent de l'export de l'espace formateur, pseudonymisé (P001…). Les
colonnes sont décrites dans la feuille « lisez-moi ».

### 4.1 Cotation : la clé départage-t-elle ?
- Pour chaque point de choix, on compare quelle réponse choisissent le tiers le plus fort
  et le tiers le plus faible (feuille `choix` : `reponse_no`, `qualite`).
- Une réponse que les meilleur·e·s choisissent autant que les plus faibles ne discrimine pas.
  Elle est récrite ou neutralisée (Patterson et al. 2016).
- On compare la note graduée (`qualite`) et la cotation dichotomique
  (`taux_meilleure_reponse`), et on garde celle qui a les meilleures preuves de validité
  (Weng et al. 2018 ; de Leng et al. 2017).

### 4.2 Généralisation : combien de situations faut-il ?
- **Étude G** : variance participant × scène × choix (feuille `scenes`). On en tire la
  fiabilité absolue Φ, celle qui compte pour un seuil (Trejo-Mejía et al. 2016).
- **Étude D** : combien de chapitres ou de passages faut-il pour un Φ suffisant ? La réponse
  dira si l'on peut donner une bande après un seul chapitre, et si 8 choix suffisent par
  compétence.

### 4.3 Seuil du passage « trop rapide »
- On prend la distribution de `temps_s` (feuille `choix`) sur les vrais choix
  (`nb_options` > 1).
- Le seuil devient le 5ᵉ centile. On vérifie ensuite la part des passages signalés
  (`trop_rapide`), qui devrait rester faible. Aucun article ne fixe ce seuil (Baker et al.
  2004).

### 4.4 Pondération des passages dans le temps
On compare plusieurs règles pour prédire la note du passage suivant, et on garde celle qui
fait la plus petite erreur quadratique moyenne (Pelánek 2017) :
- l'ancienne règle de rang, 1 + 0,25 × (n − 1) ;
- des demi-vies de 60, 90 et 180 jours ;
- une moyenne mobile exponentielle.

Avec deux passages par personne, cette analyse ne sera qu'indicative. Il faudra une deuxième
période pour la confirmer.

### 4.5 Progrès et effet de répétition
- **Gain au 2ᵉ passage des chapitres rejoués** : `gain_points` et `progres` (feuille
  `niveaux`) ; *d* de Cohen du groupe dans le tableau de bord (Nissen et al. 2018).
- **Comparaison avec le chapitre 3, jamais rejoué** : la part du gain qui tient à la
  répétition (Lievens et al. 2005 ; Hausknecht et al. 2007). Si le gain des chapitres
  rejoués dépasse nettement celui du chapitre témoin, le délai de 7 jours est à revoir.
- **Fidélité test-retest** : corrélation entre 1ᵉʳ et 2ᵉ passage des chapitres rejoués.

### 4.6 Seuils des bandes
- On vérifie les seuils Angoff par la régression sur les cas limites. On régresse la note sur
  le jugement global des tuteurs, puis on lit la note prédite au niveau « limite »
  (Dwyer et al. 2016).
- Pour le livre, on fixe le nombre minimal de chapitres réussis par la méthode 4 de Homer &
  Russell (2021). Il remplace la règle provisoire « aucun chapitre insuffisant ».

### 4.7 Extrapolation et équité
- **Extrapolation** : corrélation entre la note du livre et une mesure externe, si elle est
  disponible (station ECOS de communication, jugement des tuteurs). Elle est attendue
  positive et sans doute modeste.
- **Groupes contrastés** : différence entre la 2ᵉ année et le groupe de comparaison.
- **Équité** : si des données démographiques sont recueillies avec le consentement (langue
  maternelle, genre), on compare les notes et on réexamine les scènes qui désavantagent un
  groupe à niveau égal (de Leng et al. 2017 ; Patterson et al. 2016).

### 4.8 Conséquences : ce que les étudiant·e·s en retirent
Un questionnaire de 5 minutes :
- la page « Comment est-ce noté ? » est-elle comprise ?
- le retour « ce qui était attendu, et pourquoi » est-il utile ?
- la note a-t-elle causé du stress ?
- les réponses critiques ont-elles été comprises ?

Une évaluation à faible enjeu doit être vécue comme une aide, pas comme un examen (Heeneman
et al. 2021). Le feedback a d'autant plus d'effet qu'il porte sur la tâche (Wisniewski et al.
2020).

## 5. Règles de décision après le pilote

| Constat | Décision |
|---|---|
| Φ trop bas pour un chapitre seul | Ne donner la bande qu'au niveau du livre, ou après plusieurs passages |
| Une réponse ne discrimine pas, ou discrimine à l'envers | La récrire ou la neutraliser, puis rebuilder le livre |
| Les seuils Angoff et la régression sur les cas limites divergent de plus de 5 points | Nouveau tour de juges sur ces chapitres |
| Plus de 10 % de passages signalés « trop rapides » | Revoir le seuil de temps |
| Gain des chapitres rejoués bien au-dessus du chapitre témoin | Allonger le délai entre deux passages comptés |
| Le questionnaire montre une note mal comprise ou stressante | Revoir la page d'explication et l'écran de fin |

Chaque décision et chaque nouvelle valeur sont inscrites au journal de développement.

## 6. Éthique et données

- **Participation volontaire**, sans effet sur les notes officielles : la note du jeu reste
  formative.
- **Consentement éclairé**. L'information dit ce qui est enregistré (choix, temps de
  réponse) et comment c'est analysé : export pseudonymisé, sans nom.
- **Minimisation** : pas de donnée démographique sans nécessité ni consentement explicite.
- **Commission d'éthique** : vérifier auprès de la commission cantonale compétente (Vaud ou
  Genève) si le projet demande une autorisation ou une simple déclaration de non-compétence.
  Une recherche en pédagogie n'entre en général pas dans le champ de la loi relative à la
  recherche sur l'être humain, mais c'est à la commission d'en juger.
- **Durée de conservation** des données fixée à l'avance, puis suppression des comptes.

## 7. Limites du pilote

- Avec 30 à 40 personnes, les corrélations et les variances seront estimées avec une large
  marge : le pilote donne des **premières estimations**, pas des valeurs définitives.
- Deux passages par personne suffisent pour la fidélité test-retest, mais pas pour comparer
  finement les règles de pondération dans le temps.
- Les seuils restent ceux d'une année d'études : un autre public demandera un nouvel Angoff.
