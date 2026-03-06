# Cahier des charges
## Intégration de l'IA dans le jeu sérieux End of Life

| **Projet** | End of Life v2.0 — Serious Game soins palliatifs |
| --- | --- |
| **Sous-projet** | Outils IA pour auteurs de scénarios |
| **Version** | 1.0 |
| **Date** | Février 2025 |
| **Statut** | Préparation déploiement réel |

---

## Résumé exécutif

Ce document définit les exigences pour l'intégration d'outils d'IA dans le projet **End of Life**, un jeu sérieux de formation en soins palliatifs. Les outils visent à **assister les formateurs** dans la création et la maintenance des scénarios, et non à modifier l'expérience des joueurs en temps réel.

**Étape préalable :** Construction et visualisation du graphe des scénarios (interactions → réponses).

**Deux fonctionnalités principales :**
1. **Enrichissement** — Générer de nouvelles réponses possibles pour enrichir les interactions.
2. **Paramétrage assisté (scoring)** — Proposer des scores (5 compétences soft) pour chaque réponse du scénario, avec justification.

**Dépendance :** Le scoring s'applique aux réponses existantes et à celles générées par l'enrichissement.

---

## Table des matières

1. [Contexte](#1-contexte)
2. [Acteurs et bénéficiaires](#2-acteurs-et-b%C3%A9n%C3%A9ficiaires)
3. [Objectifs et périmètre](#3-objectifs-et-p%C3%A9rim%C3%A8tre)
4. [Fonctionnalités détaillées](#4-fonctionnalit%C3%A9s-d%C3%A9taill%C3%A9es)
5. [Spécifications techniques](#5-sp%C3%A9cifications-techniques)
6. [Livrables](#6-livrables)
7. [Annexes](#7-annexes)

---

## 1. Contexte

### 1.1 Le jeu End of Life

End of Life est un **roman visuel interactif 3D** qui forme le personnel soignant aux situations de fin de vie en EMS. Le joueur incarne « Claude », un(e) soignant(e), et fait des choix de réponses lors de dialogues avec des patients (ex. Agathe) ou collègues.

Chaque choix modifie **cinq compétences** :
- **Authenticité** — Cohérence parole/posture professionnelle
- **Respect** — Considération de l'autonomie et de la dignité
- **Compassion** — Reconnaissance de la souffrance
- **Espoir** — Lien sans faux espoirs
- **Empathie** — Validation des émotions de l'autre

### 1.2 Données du projet

Les scénarios sont stockés dans **`Chapters_v3-3-b_polishNarratif.json`** :

```
Chapters → Scenes → Interactions → Responses
```

Chaque réponse contient : `Text`, `Authenticity`, `Respect`, `Compassion`, `Hope`, `Empathy`, `NextInteractionID`.

---

## 2. Acteurs et bénéficiaires

| Rôle | Description | Usage des outils IA |
| --- | --- | --- |
| **Formateur / Auteur** | Expert métier (soins palliatifs, pédagogie) | Validation des scores, génération de nouvelles réponses, édition du JSON |
| **Développeur** | Maintenance technique, intégration | Déploiement, évolution des scripts et prompts |
| **Joueur / Étudiant** | Utilisateur final du jeu | N'utilise pas les outils IA (expérience inchangée) |

---

## 3. Objectifs et périmètre

### 3.1 Objectifs

| Priorité | Objectif |
| --- | --- |
| **P0** | Construction du graphe et visualisation des scénarios |
| **P1** | Générer de nouvelles réponses plausibles pour enrichir les interactions |
| **P1** | Proposer des scores + justifications pour toute réponse (existante ou nouvelle) |
| **P1** | Permettre un audit en lot du JSON actuel |
| **P2** | Interface web pour validation/correction (optionnel) |

### 3.2 Périmètre inclus

- Construction et visualisation du graphe des scénarios
- Outils d'assistance à l'édition du scénario (enrichissement, scoring)
- Intégration avec `Chapters_v3-3-b_polishNarratif.json`
- Documentation formateur
- Déploiement en environnement exploitable

---

## 4. Fonctionnalités détaillées

### 4.1 Étape du graphe

**Objectif :** Construire et visualiser la structure des scénarios sous forme de graphe (nœuds = interactions, arêtes = réponses), avec édition directe et parcours simulateur.

**Composants développés :**

| Fichier | Rôle |
| --- | --- |
| **graph_builder.py** | Charge `Chapters_v3-3-b_polishNarratif.json`, construit nœuds (interactions) et arêtes (réponses avec `NextInteractionID`). Génère le panneau d'édition (Name, Text, scores) et la structure parcours joueur. Valide les `NextInteractionID` (EG-7 : -1 = fin de branche). |
| **graph_viewer.py** | Génère des pages HTML par chapitre avec vis-network (layout hiérarchique). Sidebar : liste des scénarios, recherche par texte (EG-3). Mode **Édition** : modification `SceneIntroduction`, Name, Text, scores des interactions/réponses ; boutons « Valider et sauvegarder » (API), « Télécharger JSON ». Mode **Parcours joueur** : simulation interactive, choix de réponses, chemin en vert sur le graphe, cumul des scores finaux. |
| **graph_to_md.py** | Export vers `output/graphes_end_of_life.md` au format Mermaid (flowchart TD) : un diagramme par scène (nœuds, arêtes). |
| **app.py** | Serveur Flask (port 8765) : sert `output/graphes/` (index + pages chapitre) ; API POST `/api/save` pour persister les modifications dans `Chapters_v3-3-b_polishNarratif.json`. |

| Élément | Détail |
| --- | --- |
| **Entrées** | JSON `Chapters_v3-3-b_polishNarratif.json` |
| **Sorties** | Pages HTML interactives (`output/graphes/*.html`), index de navigation, fichier Markdown Mermaid (`output/graphes_end_of_life.md`) |
| **Règles** | `NextInteractionID` -1 = fin de branche (EG-7) ; sauvegarde uniquement via API si serveur lancé |

### 4.2 Module d'enrichissement

**Objectif :** Générer de nouvelles réponses plausibles pour une interaction donnée.

| Élément | Détail |
| --- | --- |
| **Entrées** | Contexte scène (`SceneIntroduction`, `Title`), texte interaction, profil acteur (`Actor`), liste des réponses existantes |
| **Sorties** | Liste de réponses + scores associés + catégorie (« exemplaire », « neutre », « problématique ») |
| **Règles** | Conformité déontologique ; aucune insertion sans validation humaine ; pas de duplication des réponses existantes |

### 4.3 Module de scoring (paramétrage)

**Objectif :** Proposer automatiquement des scores et une justification pour toute réponse (existante ou nouvellement générée).

| Élément | Détail |
| --- | --- |
| **Entrées** | Contexte scène (`SceneIntroduction`, `Title`), texte interaction, profil acteur (`Actor`), texte de la réponse |
| **Sorties** | Vecteur `{ Authenticity, Respect, Compassion, Hope, Empathy }` (-3 à +3), justification textuelle |
| **Règles** | Stabilité sur appels répétés ; scores explicables ; réponses inadaptées clairement négatives |

### 4.4 Référentiel pédagogique (échelle -3 à +3)

| Compétence | Positif (+2/+3) | Neutre (0) | Négatif (-2/-3) |
| --- | --- | --- | --- |
| **Authenticité** | Honnêteté, alignement | Neutre | Mensonge, déni |
| **Respect** | Autonomie, consentement | Formel | Imposition, infantilisation |
| **Compassion** | Présence, bienveillance | Distance | Indifférence, jugement |
| **Espoir** | Lien sans promesses | Équilibré | Faux espoirs, abattement |
| **Empathie** | Validation des émotions | Écoute neutre | Invalidation, centrage sur soi |

---

## 5. Spécifications techniques

### 5.1 Stack

| Composant | Technologie |
| --- | --- |
| Backend | Python 3.x |
| LLM | API (OpenAI, Anthropic) ou local (Ollama) |
| Données | JSON (`Chapters_v3-3-b_polishNarratif.json`) |
| Interface | CLI ou Web (Streamlit/Gradio) |

### 5.2 Contraintes

- **CT-1** — Préservation de l'intégrité du JSON (`NextInteractionID`, Id uniques)
- **CT-2** — Traçabilité des appels LLM ; mode batch possible
- **CT-3** — RGPD : choix d'API conforme ou modèle local pour données sensibles
- **CT-4** — Versioning du JSON et des propositions IA

### 5.3 Architecture (flux simplifié)

```
JSON (Chapters) → Graphe (construction + visualisation)
                         ↓
              Extraction contexte → LLM (enrichissement → scoring)
                         ↓
              Nouvelles réponses + proposition scores
                         ↓
              Validation formateur → Export JSON mis à jour
```
---


## 6. Livrables

| ID | Livrable |
| --- | --- |
| L1 | Script Python : lecture/écriture du JSON |
| L2 | Module graphe : `graph_builder.py`, `graph_viewer.py`, `graph_to_md.py`, `app.py` — construction, visualisation HTML (vis-network), export Mermaid, serveur Flask et API save |
| L3 | Module enrichissement : génération de nouvelles réponses |
| L4 | Module scoring : appel LLM, sortie scores + justification |
| L5 | Prompts et schéma JSON pour l'enrichissement et le scoring |
| L6 | Pipeline : enrichissement → scoring → export |

---

## 7. Annexes

### A. Structure JSON (rappel)

```
Chapters[]
  └─ Scenes[]
       └─ Interactions[]
            └─ Responses[]
                 └─ { Id, Name, Text, Authenticity, Respect, Compassion, Hope, Empathy, NextInteractionID }
```

### B. Références

- `Chapters_v3-3-b_polishNarratif.json` — Structure des scénarios
- `PA_2023_rapport_H-Jaton.pdf` — Rapport projet End of Life (Master HES-SO)

---

*Cahier des charges — Intégration IA End of Life — Version 1.0 — Février 2025*
