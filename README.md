# End of Life — Éditeur graphique

Outil de visualisation et d’édition des scénarios du serious game **End of Life** (formation en soins palliatifs). Phase 0 du projet d’intégration IA.

## Structure du projet

```
├── data/
│   └── Chapters_v2-1.json    # Données des chapitres (Chapters → Scenes → Interactions → Responses)
├── docs/
│   └── Cahier_des_charges_IA_EndOfLife.md
├── output/
│   ├── graphes/               # Pages HTML interactives par chapitre
│   │   ├── index.html
│   │   ├── chapitre_1_la_rencontre.html
│   │   ├── chapitre_2_vivre_en_ems.html
│   │   └── chapitre_3_la_fin_de_vie.html
│   └── graphes_end_of_life.md  # Export Mermaid
├── graph_builder.py            # Construction nœuds/arêtes, validation (EG-7)
├── graph_viewer.py             # Génération des pages HTML avec vis-network
├── graph_to_md.py              # Export Markdown Mermaid
├── app.py                      # Serveur Flask (port 8765)
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

### 1. Régénérer les graphes

```bash
python graph_builder.py    # Validation EG-7 des NextInteractionID
python graph_viewer.py     # Génère output/graphes/*.html
python graph_to_md.py      # Génère output/graphes_end_of_life.md
```

### 2. Démarrer le serveur (édition et sauvegarde)

```bash
python app.py
```

Puis ouvrir **http://localhost:8765** dans le navigateur.

### Fonctionnalités

- **Mode Édition** : modification des textes (interactions, réponses), `SceneIntroduction`, `Name`, et des scores (Authenticité, Respect, Compassion, Espoir, Empathie).
- **Mode Parcours joueur** : parcours interactif du scénario, chemin marqué en vert sur le graphe, scores cumulés affichés à la fin.
- **Recherche** (EG-3) : filtrage des scénarios et des nœuds par texte.
- **Sauvegarde** : bouton « Valider et sauvegarder » pour enregistrer dans `data/Chapters_v2-1.json`, ou téléchargement JSON.

## Spécifications

Voir `docs/Cahier_des_charges_IA_EndOfLife.md` pour les exigences détaillées (Phase 0 — Éditeur graphique, EG-1 à EG-7).

## Technologies

- **Python 3.x** — Scripts de génération
- **Flask** — Serveur web
- **vis-network** — Rendu des graphes (chargé via CDN dans le navigateur)
