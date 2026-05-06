# End of Life — Éditeur graphique

Outil de visualisation et d'édition des scénarios du serious game **End of Life** (formation en soins palliatifs). Phase 0 du projet d'intégration IA.

## Architecture (Clean Architecture)

```
PA_26_EOL/
├── app.py                            # Entry point Flask (factory pattern)
├── books.py                          # Source de vérité unique des livres
│
├── domain/                           # Modèles métier purs (zéro dépendance)
│   ├── models.py                     # Chapter, Scene, Interaction, Response, Actor
│   └── soft_skills.py                # Constantes des dimensions
│
├── repositories/                     # Pattern Repository (persistance)
│   └── chapters.py                   # Lecture / écriture atomique des JSON
│
├── services/                         # Logique métier
│   ├── graph_service.py              # Construction du graphe vis-network
│   ├── validation_service.py         # Validation EG-7 (NextInteractionID)
│   └── enrichment/                   # Service IA (sous-package)
│       ├── service.py                # EnrichmentService (façade)
│       ├── context.py                # Construction du contexte LLM
│       ├── prompt.py                 # System message + format orientation
│       ├── filtering.py              # Filtrage des doublons
│       └── backends/                 # Strategy pattern (OpenAI / Ollama)
│           ├── base.py               # Protocol LLMBackend
│           ├── openai_backend.py
│           └── ollama_backend.py
│
├── views/                            # Controllers Flask (Blueprints)
│   ├── pages.py                      # Pages HTML (rendu Jinja dynamique)
│   └── api.py                        # APIs /api/save, /api/enrich, /api/data/images
│
├── exporters/
│   └── mermaid.py                    # Export Markdown Mermaid d'un livre
│
├── templates/                        # Templates Jinja2
│   ├── landing.html.jinja
│   ├── book_index.html.jinja
│   └── chapter.html.jinja
│
├── static/                           # Assets client
│   ├── landing.css
│   ├── book_index.css
│   ├── chapter.css
│   └── chapter/                      # JS découpé en modules ES6
│       ├── main.js                   # Entry point, wiring DOM events
│       ├── store.js                  # Store singleton (state global)
│       ├── network.js                # vis-network + highlight + scenes
│       ├── editor.js                 # Mode édition + CRUD
│       ├── parcours.js               # Mode parcours joueur
│       ├── ai-modal.js               # Modale IA (proposer une réponse)
│       ├── persistence.js            # localStorage + /api/save + export
│       └── utils.js                  # Helpers (escape, confirm dialog…)
│
├── tests/                            # Tests pytest
│   ├── test_domain_models.py
│   ├── test_chapter_repository.py
│   ├── test_graph_service.py
│   ├── test_validation_service.py
│   ├── test_enrichment_filtering.py
│   └── test_enrichment_request.py
│
├── data/
│   ├── chapters/                     # JSON sources des livres
│   └── images/                       # Illustrations des personnages
│
├── docs/
├── scripts/
└── output/                           # Exports Mermaid (--book <slug>)
```

## Démarrage

```bash
pip install -r requirements.txt
python app.py
```

→ http://localhost:8765

## Routes

| Méthode | URL | Description |
|---|---|---|
| `GET` | `/` | Page de garde (cards par livre) |
| `GET` | `/books/<slug>/` | Liste des chapitres d'un livre |
| `GET` | `/books/<slug>/chapters/<id>` | Éditeur graphique d'un chapitre |
| `POST` | `/api/save` | Sauvegarde atomique d'un chapitre |
| `POST` | `/api/enrich` | Propositions IA (OpenAI ou Ollama) |
| `GET` | `/api/data/images/<filename>` | Images des personnages |

## Fonctionnalités

- **Mode Édition** : modification de `SceneIntroduction`, `Name`, `Text`, scores soft skills (-3 à +3) et `NextInteractionID`. Ajout/suppression d'interactions et de réponses. Validation EG-7 en direct.
- **Mode Parcours joueur** : navigation interactive du scénario, chemin marqué en vert sur le graphe, scores cumulés affichés en direct et à la fin.
- **Recherche** (EG-3) : filtrage des scénarios et des nœuds par texte.
- **Sauvegarde** : bouton « Valider et sauvegarder » → écriture atomique dans `data/chapters/<book>.json`. Téléchargement JSON également disponible.
- **Enrichissement IA** : modale par interaction → orientation soft skills, consigne libre, sélection du `NextInteractionID`. Backend configurable par `ENRICH_BACKEND=openai|ollama`.

## Ajouter un livre

1. Déposer le JSON dans `data/chapters/`.
2. Ajouter une entrée dans `BOOKS` (fichier `books.py`) avec `slug`, `title`, `subtitle`, `description`, `audience`, `json`.
3. C'est tout. Tous les modules consomment cette source unique.

## Variables d'environnement

| Variable | Défaut | Description |
|---|---|---|
| `OPENAI_API_KEY` | — | Clé OpenAI (si `ENRICH_BACKEND=openai`) |
| `ENRICH_BACKEND` | `openai` | `openai` ou `ollama` |
| `ENRICH_OPENAI_MODEL` | `gpt-4.1-mini` | Modèle OpenAI |
| `ENRICH_OLLAMA_URL` | `http://localhost:11434/v1/chat/completions` | URL Ollama |
| `ENRICH_OLLAMA_MODEL` | `llama3.1:8b` | Modèle Ollama |
| `ENRICH_OLLAMA_TIMEOUT` | `300` | Timeout Ollama (secondes) |

## Tests

```bash
pytest
```

Couverture actuelle : domain models (round-trip), repository (atomicité), graph service, validation EG-7, filtrage doublons, normalisation des requêtes IA.

## Export Mermaid

```bash
python -m exporters.mermaid                       # livre par défaut
python -m exporters.mermaid --book medstudents_y2 # autre livre
```

Génère `output/graphes_<slug>.md`.

## Spécifications

Voir `docs/Cahier_des_charges_IA_EndOfLife.md` (Phase 0 — Éditeur graphique, EG-1 à EG-7).

## Stack technique

- **Backend** : Python 3.11+, Flask, Jinja2
- **Frontend** : ES Modules natifs, vis-network (CDN)
- **Tests** : pytest
