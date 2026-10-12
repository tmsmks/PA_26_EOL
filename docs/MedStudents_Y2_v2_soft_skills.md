# MedStudents Y2 v2 — Répartition des soft skills

> Généré par `scripts/build_medstudents_y2_v2.py` à partir des scores réels de
> chaque réponse. Ne pas éditer à la main.

**Lecture.** Pour chaque scène, la part (%) de chaque compétence dans le total
des points positifs *disponibles* (toutes réponses confondues) : c'est ce que
la scène permet de travailler. Le *focus visé* est l'intention de conception
(voir la bible). Les colonnes de choix comptent les réponses par catégorie :
TB très bon (≥ +9), B bon (+4 à +8), M moyen (−1 à +3), Ma mauvais (−6 à −2),
TM très mauvais (≤ −7). ⑂ = branche parallèle (jouée selon les choix
précédents), ✦ = histoire annexe (jouée seulement si elle est débloquée).

RD Respect et dignité · EM Empathie · CO Compassion · ER Régulation
émotionnelle · CC Clarté de communication · PB Frontières professionnelles ·
IC Collaboration interprofessionnelle.

## Vue d'ensemble du livre

| Chapitre | Focus visé | RD | EM | CO | ER | CC | PB | IC | Interactions | Réponses |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1. Madame 14 | RD, EM, PB, CC | **23** | **20** | 11 | 5 | 10 | 18 | 13 | 103 | 453 |
| 2. Deux Pittet | PB, CC, IC, EM | 10 | 17 | 9 | 11 | 12 | **21** | **20** | 105 | 433 |
| 3. Le cœur, en vrai | ER, CC, EM, CO | 9 | **26** | 14 | 15 | 15 | 9 | 11 | 90 | 356 |
| 4. Hors script | ER, IC, PB, EM | 11 | 18 | 14 | 11 | 15 | 10 | **21** | 114 | 461 |
| 5. Le corps donné | CO, RD, PB, ER | **28** | 16 | 11 | 13 | 12 | 13 | 7 | 97 | 365 |
| **Livre** | | **16** | **19** | **12** | **11** | **13** | **14** | **15** | | |

## Audit du score

Ce que vaut chaque façon de jouer, recalculée à chaque build. **Le build échoue** si
un point de choix a deux meilleures réponses, si une stratégie fondée sur la longueur
des réponses dépasse 62/100 sur un chapitre, ou si une compétence est en jeu
dans moins de 8 choix sur le parcours le plus court d'un chapitre
(`MIN_SKILL_EVIDENCE` : en dessous, le serveur ne note pas la compétence).

### Joueur·euse·s simulé·e·s (vrai rejeu serveur)

Tout le livre est joué avec ses états narratifs, puis chaque parcours est rejoué par
`replay_scene` et noté par `choice_quality`, comme une vraie partie : 0 = toujours la
pire réponse, 100 = toujours la meilleure. « Au hasard » : moyenne de 100
parties.

| Chapitre | Meilleure | Pire | Au hasard | Toujours la plus longue | Toujours la plus courte |
|---|---:|---:|---:|---:|---:|
| 1. Madame 14 | 100 | 0 | 47 | 43.8 | 28.6 |
| 2. Deux Pittet | 100 | 0 | 45.6 | 43.3 | 32.7 |
| 3. Le cœur, en vrai | 100 | 0 | 43.2 | 42.3 | 38.7 |
| 4. Hors script | 100 | 0 | 43.6 | 43.8 | 40.2 |
| 5. Le corps donné | 100 | 0 | 47.9 | 41.4 | 49.7 |
| **Livre** | 100 | 0 | 45.6 | 43 | 37.2 |

Compétences non notées faute de preuves, sur les 100 parties au hasard : **0**.

### Indices de forme (tous les points de choix, chacun compté une fois)

| Chapitre | Points de choix | Meilleure = la plus longue | Toujours la plus longue | Toujours la 2ᵉ plus longue | Toujours la 3ᵉ plus longue | Toujours la plus courte |
|---|---:|---:|---:|---:|---:|---:|
| 1. Madame 14 | 89 | 22 (25 %) | 41 | 58 | 53 | 40 |
| 2. Deux Pittet | 85 | 23 (27 %) | 44 | 40 | 59 | 35 |
| 3. Le cœur, en vrai | 74 | 26 (35 %) | 47 | 42 | 47 | 40 |
| 4. Hors script | 98 | 37 (38 %) | 53 | 51 | 42 | 32 |
| 5. Le corps donné | 78 | 21 (27 %) | 42 | 45 | 52 | 46 |

Rang de longueur de la meilleure réponse (1 = la plus longue) : 1 : 129 · 2 : 71 · 3 : 113 · 4 : 79 · 5 : 30 · 6 : 2.

### Preuves par compétence

Nombre de choix qui mettent chaque compétence en jeu : minimum sur un parcours complet
(borne basse : pire variante de chaque scène) et, entre parenthèses, minimum observé sur
les parties au hasard.

| Chapitre | RD | EM | CO | ER | CC | PB | IC |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1. Madame 14 | 29 (33) | 23 (24) | 11 (11) | 11 (13) | 19 (24) | 22 (26) | 20 (24) |
| 2. Deux Pittet | 13 (14) | 17 (18) | 8 (10) | 11 (14) | 19 (22) | 20 (22) | 22 (25) |
| 3. Le cœur, en vrai | 11 (13) | 14 (15) | 10 (11) | 10 (12) | 18 (20) | 18 (18) | 14 (14) |
| 4. Hors script | 12 (15) | 18 (22) | 9 (11) | 10 (12) | 16 (17) | 17 (19) | 20 (24) |
| 5. Le corps donné | 23 (27) | 20 (23) | 11 (14) | 13 (13) | 17 (20) | 19 (21) | 9 (10) |

## Chapitre 1 — Madame 14

Focus visé : **RD, EM, PB, CC**

| Scène | Focus visé | Dominantes réelles | RD | EM | CO | ER | CC | PB | IC | TB | B | M | Ma | TM |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.1 La salle froide | RD, ER, IC | RD, EM, CO | **25** | 17 | 16 | 16 | 6 | 4 | 16 | 0 | 13 | 29 | 27 | 1 |
| 1.2 La story | PB, RD, IC | RD, CC, EM | **34** | 18 | 4 | 1 | **20** | 10 | 13 | 1 | 18 | 27 | 27 | 0 |
| 1.3 Montchéry | CC, RD, IC | PB, EM, RD | 17 | **20** | 2 | 5 | 14 | **24** | 17 | 0 | 22 | 32 | 33 | 0 |
| 1.4 La ferme des Combettes | PB, EM, RD | PB, IC, RD | 18 | 9 | 2 | 2 | 9 | **39** | **21** | 0 | 19 | 24 | 28 | 1 |
| 1.5 La lettre ⑂ | RD, CO, PB | RD, PB, CO | **32** | 15 | 17 | 8 | 3 | **20** | 5 | 0 | 12 | 21 | 14 | 4 |
| 1.5 Le livre des donneurs ⑂ | RD, CO, ER | RD, EM, CO | **33** | **33** | 11 | 7 | 4 | 0 | 11 | 0 | 9 | 29 | 12 | 0 |
| 1.6 2 h 14 ✦ | EM, ER, PB | CO, EM, PB | 0 | **40** | **41** | 0 | 0 | 17 | 1 | 0 | 9 | 19 | 16 | 0 |
| **Total chapitre** | | **RD, EM, PB** | **23** | **20** | **11** | **5** | **10** | **18** | **13** | **1** | **102** | **181** | **157** | **6** |

Profil du meilleur parcours (points gagnés sur le chemin idéal) :

| Scène | Total | RD | EM | CO | ER | CC | PB | IC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.1 La salle froide | 47 | 15 | 6 | 2 | 8 | 4 | 2 | 10 |
| 1.2 La story | 28 | 5 | 2 | 1 | 0 | 7 | 6 | 7 |
| 1.3 Montchéry | 64 | 13 | 13 | 0 | 2 | 11 | 16 | 9 |
| 1.4 La ferme des Combettes | 49 | 8 | 6 | 1 | 0 | 6 | 17 | 11 |
| 1.5 La lettre | 36 | 13 | 7 | 8 | 3 | 0 | 5 | 0 |
| 1.5 Le livre des donneurs | 37 | 12 | 15 | 4 | 0 | 1 | 0 | 5 |
| 1.6 2 h 14 | 23 | 0 | 10 | 8 | 0 | 0 | 5 | 0 |

## Chapitre 2 — Deux Pittet

Focus visé : **PB, CC, IC, EM**

| Scène | Focus visé | Dominantes réelles | RD | EM | CO | ER | CC | PB | IC | TB | B | M | Ma | TM |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2.1 Le jour des vaccins | CC, PB, EM, IC | PB, CC, IC | 10 | 13 | 4 | 9 | 19 | **27** | 17 | 1 | 25 | 49 | 40 | 1 |
| 2.2 L'APP du jeudi | IC, CC, PB | IC, EM, PB | 0 | 19 | 16 | 5 | 13 | 17 | **30** | 0 | 18 | 27 | 26 | 0 |
| 2.3 Le Café de la Gare ⑂ | PB, RD, ER, IC | ER, IC, PB | 13 | 10 | 3 | **26** | 7 | 14 | **26** | 0 | 10 | 18 | 21 | 1 |
| 2.3 La créatinine ⑂ | RD, CC, CO, ER | PB, RD, EM | **21** | 18 | 4 | 18 | 5 | **25** | 10 | 0 | 12 | 24 | 12 | 1 |
| 2.4 Le dimanche aux Combettes | EM, RD, PB, CO | PB, EM, RD | 15 | **20** | 6 | 6 | 8 | **37** | 7 | 0 | 15 | 25 | 20 | 0 |
| 2.5 Léo ✦ | EM, IC, CO | EM, CO, IC | 7 | **40** | **21** | 5 | 2 | 5 | **21** | 0 | 7 | 14 | 7 | 0 |
| 2.6 BLS | IC, CC, ER, CO | IC, CC, CO | 5 | 12 | 18 | 15 | 19 | 0 | **31** | 0 | 10 | 22 | 17 | 0 |
| **Total chapitre** | | **PB, IC, EM** | **10** | **17** | **9** | **11** | **12** | **21** | **20** | **1** | **97** | **179** | **143** | **3** |

Profil du meilleur parcours (points gagnés sur le chemin idéal) :

| Scène | Total | RD | EM | CO | ER | CC | PB | IC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2.1 Le jour des vaccins | 58 | 9 | 12 | 1 | 2 | 15 | 12 | 7 |
| 2.2 L'APP du jeudi | 46 | 0 | 6 | 7 | 4 | 5 | 7 | 17 |
| 2.3 Le Café de la Gare | 30 | 6 | 3 | 1 | 6 | 4 | 3 | 7 |
| 2.3 La créatinine | 34 | 3 | 8 | 0 | 5 | 3 | 10 | 5 |
| 2.4 Le dimanche aux Combettes | 29 | 3 | 8 | 2 | 0 | 2 | 9 | 5 |
| 2.5 Léo | 22 | 2 | 8 | 1 | 1 | 1 | 2 | 7 |
| 2.6 BLS | 37 | 2 | 4 | 7 | 5 | 8 | 0 | 11 |

## Chapitre 3 — Le cœur, en vrai

Focus visé : **ER, CC, EM, CO**

| Scène | Focus visé | Dominantes réelles | RD | EM | CO | ER | CC | PB | IC | TB | B | M | Ma | TM |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3.1 Le repas de Noël | PB, CC, ER, CO | IC, CC, CO | 0 | 10 | **21** | 8 | **23** | 13 | **26** | 1 | 12 | 14 | 31 | 0 |
| 3.2 L'unité coronarienne ⑂ | ER, EM, CO, PB | EM, CO, PB | 11 | **43** | 17 | 8 | 4 | 13 | 4 | 0 | 12 | 13 | 17 | 0 |
| 3.2 Les soins intensifs ⑂ | ER, EM, PB, CO | ER, EM, CC | 7 | **25** | 14 | **26** | 18 | 7 | 3 | 0 | 14 | 13 | 19 | 0 |
| 3.3 Un cœur dans les mains | ER, RD, IC, CO | ER, EM, RD | 11 | 18 | 6 | **43** | 10 | 6 | 7 | 0 | 10 | 25 | 18 | 0 |
| 3.4 Le stéthoscope | CC, RD, IC, CO | RD, EM, CC | **27** | 18 | 8 | 4 | 18 | 10 | 16 | 0 | 17 | 28 | 25 | 1 |
| 3.5 L'ambulancière ✦ | EM, ER, CO, IC | EM, CO, ER | 0 | **54** | **25** | 10 | 2 | 0 | 8 | 0 | 6 | 17 | 10 | 0 |
| 3.6 Le patient standardisé | CC, EM, RD, IC | EM, CC, ER | 2 | **36** | 8 | 14 | **25** | 10 | 5 | 0 | 6 | 25 | 15 | 0 |
| **Total chapitre** | | **EM, ER, CC** | **9** | **26** | **14** | **15** | **15** | **9** | **11** | **1** | **77** | **135** | **135** | **1** |

Profil du meilleur parcours (points gagnés sur le chemin idéal) :

| Scène | Total | RD | EM | CO | ER | CC | PB | IC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 3.1 Le repas de Noël | 27 | 0 | 2 | 4 | 2 | 10 | 2 | 7 |
| 3.2 L'unité coronarienne | 33 | 6 | 15 | 2 | 2 | 1 | 5 | 2 |
| 3.2 Les soins intensifs | 34 | 4 | 6 | 5 | 10 | 6 | 2 | 1 |
| 3.3 Un cœur dans les mains | 33 | 4 | 3 | 1 | 16 | 5 | 2 | 2 |
| 3.4 Le stéthoscope | 46 | 8 | 6 | 5 | 0 | 13 | 5 | 9 |
| 3.5 L'ambulancière | 23 | 0 | 12 | 4 | 2 | 1 | 0 | 4 |
| 3.6 Le patient standardisé | 25 | 0 | 8 | 2 | 2 | 9 | 3 | 1 |

## Chapitre 4 — Hors script

Focus visé : **ER, IC, PB, EM**

| Scène | Focus visé | Dominantes réelles | RD | EM | CO | ER | CC | PB | IC | TB | B | M | Ma | TM |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.1 Hors script | ER, IC, CC, PB | IC, ER, CC | 2 | 7 | 5 | **26** | **26** | 2 | **32** | 0 | 16 | 16 | 27 | 0 |
| 4.2 Le portfolio | PB, IC, ER, EM | PB, EM, CO | 4 | **21** | 19 | 11 | 6 | **35** | 5 | 0 | 17 | 25 | 35 | 1 |
| 4.3 1 h 07 | EM, CO, ER, PB | CO, IC, EM | 1 | 18 | **35** | 5 | 16 | 5 | **20** | 1 | 22 | 14 | 26 | 0 |
| 4.4 La rééducation ⑂ | RD, IC, CO, EM | IC, RD, EM | **27** | **24** | 7 | 7 | 2 | 0 | **33** | 0 | 5 | 20 | 9 | 0 |
| 4.4 Vingt-trois minutes ⑂ | RD, CO, PB, IC | RD, CC, ER | **25** | 13 | 4 | 15 | 19 | 9 | 13 | 0 | 11 | 14 | 12 | 0 |
| 4.5 Les pieds qui ne savent plus | IC, RD, EM, CO | EM, IC, RD | 17 | **28** | 5 | 9 | 9 | 5 | **28** | 0 | 18 | 52 | 36 | 0 |
| 4.6 L'appel de 23 h ⑂ | PB, ER, IC, CO | CC, IC, PB | 0 | 9 | 16 | 4 | **25** | 19 | **25** | 0 | 11 | 8 | 16 | 0 |
| 4.6 La nuit sur le carrelage ⑂ | IC, PB, CC, CO | RD, EM, CC | **31** | **26** | 9 | 5 | 16 | 9 | 5 | 0 | 8 | 15 | 12 | 0 |
| **Total chapitre** | | **IC, EM, CC** | **11** | **18** | **14** | **11** | **15** | **10** | **21** | **1** | **108** | **164** | **173** | **1** |

Profil du meilleur parcours (points gagnés sur le chemin idéal) :

| Scène | Total | RD | EM | CO | ER | CC | PB | IC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.1 Hors script | 23 | 0 | 1 | 3 | 6 | 6 | 1 | 6 |
| 4.2 Le portfolio | 24 | 4 | 5 | 3 | 3 | 1 | 8 | 0 |
| 4.3 1 h 07 | 38 | 1 | 6 | 12 | 3 | 8 | 3 | 5 |
| 4.4 La rééducation | 23 | 4 | 7 | 1 | 1 | 1 | 0 | 9 |
| 4.4 Vingt-trois minutes | 37 | 8 | 4 | 3 | 6 | 7 | 4 | 5 |
| 4.5 Les pieds qui ne savent plus | 54 | 13 | 14 | 1 | 1 | 6 | 3 | 16 |
| 4.6 L'appel de 23 h | 29 | 0 | 2 | 3 | 2 | 7 | 10 | 5 |
| 4.6 La nuit sur le carrelage | 26 | 10 | 3 | 1 | 0 | 6 | 3 | 3 |

## Chapitre 5 — Le corps donné

Focus visé : **CO, RD, PB, ER**

| Scène | Focus visé | Dominantes réelles | RD | EM | CO | ER | CC | PB | IC | TB | B | M | Ma | TM |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.1 La table de la cuisine | IC, RD, PB, CO | RD, PB, EM | **27** | 14 | 5 | 12 | 12 | 19 | 10 | 0 | 12 | 25 | 19 | 0 |
| 5.2 La grange | EM, RD, PB, CO | RD, EM, PB | **32** | 17 | 11 | 3 | 11 | 17 | 9 | 1 | 10 | 20 | 21 | 0 |
| 5.3 La dernière visite | CO, ER, RD, PB | RD, ER, CC | **28** | 13 | 11 | **21** | 15 | 8 | 4 | 0 | 14 | 27 | 24 | 0 |
| 5.4 Le fourgon ⑂ | CO, IC, RD, ER | EM, CO, RD | **20** | **25** | **23** | 7 | 10 | 10 | 7 | 0 | 8 | 14 | 12 | 0 |
| 5.4 Vous ne l'emmènerez pas ⑂ | RD, PB, IC, ER | PB, RD, CO | **27** | 7 | 14 | 12 | 5 | **31** | 5 | 0 | 9 | 11 | 15 | 1 |
| 5.5 La lettre | CO, ER, RD, PB | RD, EM, ER | **29** | 19 | 11 | 14 | 14 | 7 | 6 | 0 | 12 | 24 | 15 | 0 |
| 5.6 La cérémonie | RD, CO, PB, ER | RD, EM, ER | **29** | 18 | 8 | 18 | 14 | 6 | 7 | 1 | 12 | 22 | 22 | 0 |
| **Total chapitre** | | **RD, EM, ER** | **28** | **16** | **11** | **13** | **12** | **13** | **7** | **2** | **77** | **143** | **128** | **1** |

Profil du meilleur parcours (points gagnés sur le chemin idéal) :

| Scène | Total | RD | EM | CO | ER | CC | PB | IC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.1 La table de la cuisine | 28 | 9 | 4 | 1 | 4 | 3 | 6 | 1 |
| 5.2 La grange | 22 | 7 | 3 | 3 | 0 | 2 | 5 | 2 |
| 5.3 La dernière visite | 37 | 13 | 5 | 4 | 5 | 5 | 3 | 2 |
| 5.4 Le fourgon | 29 | 7 | 7 | 4 | 0 | 5 | 3 | 3 |
| 5.4 Vous ne l'emmènerez pas | 27 | 10 | 1 | 1 | 0 | 3 | 10 | 2 |
| 5.5 La lettre | 18 | 7 | 2 | 1 | 0 | 4 | 4 | 0 |
| 5.6 La cérémonie | 36 | 13 | 6 | 2 | 2 | 8 | 3 | 2 |

