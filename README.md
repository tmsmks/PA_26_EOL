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
│   ├── chapters.py                   # Lecture / écriture atomique des JSON
│   ├── database.py                   # Moteur SQL (DATABASE_URL : SQLite ou PostgreSQL)
│   ├── orm.py                        # User, BookSession, SceneAttempt
│   ├── users.py                      # Comptes
│   └── sessions.py                   # Sessions de livre et tentatives
│
├── services/                         # Logique métier
│   ├── graph_service.py              # Construction du graphe vis-network
│   ├── validation_service.py         # Validation EG-7 (NextInteractionID)
│   ├── auth_service.py               # Inscription, authentification
│   ├── scoring_service.py            # Rejeu serveur, notes /100, pondération
│   ├── session_service.py            # Cycle de vie d'une session de livre
│   ├── history_service.py            # Historique par participant
│   ├── feedback/                     # Feedback général de fin de livre
│   │   ├── service.py                # FeedbackService (IA + repli)
│   │   ├── prompt.py                 # Prompt (scores, moments clés, sessions précédentes)
│   │   └── rules.py                  # Feedback sans IA (repli)
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
│   ├── api.py                        # APIs /api/save, /api/enrich, /api/data/images
│   ├── auth.py                       # /login, /register, /logout
│   ├── account.py                    # /me, /sessions/<id>, /trainer/…
│   ├── session_api.py                # API des sessions de jeu
│   └── guards.py                     # Utilisateur courant, rôles, CSRF
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
├── instance/                         # Base SQLite locale + secret_key (non versionné)
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

Créer un compte formateur·rice (accès à l'éditeur et au suivi des participants) :

```bash
flask --app app create-user <identifiant> --role trainer
```

Les participant·e·s créent leur compte eux-mêmes sur `/register`.

### Lecture audio (voix naturelles)

Le parcours joueur peut lire les textes à voix haute (bouton « Écouter »). Par
défaut, il utilise des **voix neuronales locales** (Piper), gratuites et hors
ligne : le texte ne quitte pas le serveur. Pour les installer (environ 140 Mo,
dans `instance/tts/models`) :

```bash
flask --app app tts-install
```

Pour des voix encore plus naturelles, dont le **français de Suisse** (Ariane,
Fabrice), définir `AZURE_SPEECH_KEY` et `AZURE_SPEECH_REGION` (Azure AI Speech,
niveau gratuit de 500 000 caractères par mois) : le texte des écrans est alors
envoyé à Microsoft. Sans voix serveur, le jeu utilise les voix du navigateur.
Chaque extrait lu est gardé en cache (`instance/tts/cache`) : un même texte
n'est synthétisé qu'une fois.

Piper est sous licence GPL-3.0 : il tourne dans un processus séparé
(`scripts/tts_piper_worker.py`, lui aussi sous GPL-3.0). Voix : *siwis*
(CC BY 4.0) et *upmc* (Pierre, Jessica ; CC BY-SA 4.0).

## Routes

| Méthode | URL | Description |
|---|---|---|
| `GET` | `/` | Page de garde (cards par livre) |
| `GET/POST` | `/login`, `/register` · `POST /logout` | Comptes |
| `GET` | `/play/<slug>/` | Sommaire joueur + état de la session (connecté) |
| `GET` | `/play/<slug>/chapters/<id>` | Parcours joueur d'un chapitre (connecté) |
| `POST` | `/play/<slug>/restart` | Abandonne la session en cours |
| `GET` | `/me` | Historique du participant (sessions, note pondérée, évolution) |
| `GET` | `/sessions/<id>` | Bilan d'une session (graphiques + feedback) |
| `GET` | `/trainer/` · `/trainer/participants/<id>` | Suivi formateur·rice |
| `GET` | `/trainer/export?format=xlsx\|csv\|json` | Données brutes (filtres `book`, `user`, `pseudo=1`) (formateur) |
| `GET` · `POST` | `/trainer/cle/` | Validation de la clé de cotation : grille d'experts, import, accord (ICC), synthèse (formateur) |
| `GET` | `/books/<slug>/` | Liste des chapitres d'un livre (formateur) |
| `GET` | `/books/<slug>/chapters/<id>` | Éditeur graphique d'un chapitre (formateur) |
| `POST` | `/api/save` | Sauvegarde atomique d'un chapitre (formateur) |
| `POST` | `/api/enrich` | Propositions IA (OpenAI ou Ollama) (formateur) |
| `POST` | `/api/play/<slug>/session` | Reprend ou démarre la session du livre |
| `POST` | `/api/sessions/<id>/passages` | Ouvre (ou reprend) le passage d'un chapitre, renvoie les états de départ |
| `POST` | `/api/sessions/<id>/attempts` | Enregistre une scène (le serveur rejoue les choix) |
| `POST` | `/api/sessions/<id>/complete-chapter` | Clôture un chapitre (et le livre) |
| `POST` | `/api/sessions/<id>/feedback` | Feedback général (généré au 1er appel) |
| `GET` | `/api/data/images/<filename>` | Images des personnages |
| `GET` | `/api/tts/voices` | Voix naturelles disponibles (connecté) |
| `POST` | `/api/tts/speak` | Fait lire un texte d'écran, renvoie l'adresse du MP3 (connecté) |
| `GET` | `/api/tts/audio/<voix>/<clé>.mp3` | Extrait audio en cache (connecté) |

## Fonctionnalités

- **Mode Édition** : modification de `SceneIntroduction`, `Name`, `Text`, scores soft skills (-3 à +3) et `NextInteractionID`. Ajout/suppression d'interactions et de réponses. Validation EG-7 en direct.
- **Mode Parcours joueur** : navigation interactive du scénario, chemin marqué en vert sur le graphe, scores cumulés affichés en direct et à la fin.
- **Recherche** (EG-3) : filtrage des scénarios et des nœuds par texte.
- **Sauvegarde** : bouton « Valider et sauvegarder » → écriture atomique dans `data/chapters/<book>.json`. Téléchargement JSON également disponible.
- **Enrichissement IA** : modale par interaction → orientation soft skills, consigne libre, sélection du `NextInteractionID`. Backend configurable par `ENRICH_BACKEND=openai|ollama`.

## Comptes, sessions et feedback

Le calcul des notes suit le scoring v2 (`docs/Scoring_v2_recherche_et_plan.md`,
étape 1).

- **Session** = un parcours de l'histoire d'un livre par un participant, sur un
  ou plusieurs jours et sur n'importe quel appareil. Elle porte les états
  narratifs d'un chapitre à l'autre ; elle est terminée quand tous les
  chapitres le sont (dans l'ordre choisi par le joueur).
- **Passage** = un chapitre joué en entier : **c'est l'unité de note**. Un
  chapitre terminé est noté tout de suite, sans attendre la fin du livre, et
  on peut rejouer un chapitre seul : il repart des états narratifs du début de
  son dernier passage.
- **Passage noté ou d'entraînement** : un passage compte s'il est le premier du
  chapitre, ou s'il commence au moins `PASSAGE_SPACING_DAYS` jours (7 par
  défaut) après la fin du précédent passage noté de ce chapitre. Rejouer tout
  de suite gonfle le score par simple mémorisation : c'est de l'entraînement.
  Dans un passage, seule la 1ʳᵉ tentative d'une scène est notée ; l'ordre des
  réponses change d'un passage à l'autre.
- **Rejeu serveur** : le navigateur n'envoie que les indices des réponses
  choisies ; le serveur rejoue le parcours et calcule les scores.
- **Qualité des choix (note sur 100)** : chaque réponse est comparée aux
  réponses proposées au même moment, Σ (choisi − pire) / Σ (meilleur − pire).
  100 = la meilleure réponse à chaque fois, 0 = la pire, ≈ 50 au hasard
  (mesuré sur le livre Y2). La note globale porte sur le total des 7
  compétences ; le profil, sur chacune, notée seulement si au moins 8 choix la
  mettent en jeu.
- **Contrôle de la clé (livre 2)** : `scripts/build_medstudents_y2_v2.py`
  échoue si un point de choix a deux meilleures réponses, si choisir toujours
  la réponse la plus longue (ou la plus courte) dépasse 62/100 sur un chapitre,
  ou si une compétence est en jeu dans moins de 8 choix sur le parcours le plus
  court. L'audit (joueur·euse·s simulé·e·s rejoué·e·s par le serveur) est dans
  `docs/MedStudents_Y2_v2_soft_skills.md`.
- **Niveau d'un chapitre** : moyenne de ses passages notés, le n-ième pesant
  1 + 0,25 × (n − 1) ; avec la **progression** (changement normalisé depuis le
  1ᵉʳ passage, Marx & Cummings 2007) et une **marge** d'incertitude à 95 %
  qui se resserre à chaque passage.
- **Note du livre** : moyenne des niveaux des chapitres évalués (poids égaux),
  avec la couverture (« 4/6 chapitres évalués »).
- **Bilan de session** : le dernier passage de chaque chapitre joué dans la
  session.
- **Reprise des données v1** : au démarrage, les parties jouées avant le v2
  reçoivent leurs passages, et les bilans sont recalculés ; l'ancien bilan reste
  dans `results["v1"]` (`services/scoring_upgrade.py`, idempotent).
- **Feedback général** à la fin du livre : synthèse, points forts / faibles,
  conseils, chapitres à retravailler, et — dès la 2ᵉ session — comparaison
  avec les sessions précédentes (scores et conseils donnés alors). Aucune
  donnée personnelle n'est envoyée au LLM. Si le LLM est indisponible, un
  feedback par règles est affiché.

## Export des données

Dans l'espace formateur (`/trainer/`, et sur la page de chaque participant),
**Données brutes** télécharge tout ce qui a été joué, une ligne par objet :

| Table | Une ligne = | Contenu principal |
|---|---|---|
| `participants` | un compte | rôle, inscription, passages notés et d'entraînement, sessions |
| `niveaux` | un chapitre évalué d'un participant | niveau, marge, progression, 1ᵉʳ et dernier passage, 7 compétences |
| `passages` | un chapitre joué en entier | noté ou non, dates, qualité des choix (et corrigée du hasard), 7 compétences |
| `sessions` | un parcours de l'histoire d'un livre | statut, dates, bilan, ancienne note v1, états narratifs |
| `chapitres` | un chapitre dans le bilan d'une session | qualité des choix et 7 compétences |
| `scenes` | une scène jouée (tentative) | notée ou non, point d'entrée, qualité, points, gains et écarts par compétence |
| `choix` | une réponse donnée | réplique, réponse choisie et ses points, pire et meilleure réponse, qualité du choix |

- **Formats** : Excel `.xlsx` (une feuille par table + « lisez-moi »), CSV
  (archive zip, UTF-8 avec BOM, virgule, point décimal) ou JSON (dates ISO 8601).
  Chaque format contient un dictionnaire des colonnes.
- **Filtres** : un livre, un participant, et **Pseudonymiser** (identifiants et
  noms remplacés par un code stable `P` + n° du compte).
- Les sessions en cours ont des bilans **provisoires**, calculés sur les
  passages déjà joués ; les sessions terminées reprennent l'instantané figé.

## Validation de la clé de cotation

Les points des réponses (−3 à +3 sur 7 compétences) ont été écrits par l'auteur
seul : ils restent **provisoires** tant qu'un panel d'experts ne les a pas
validés (plan de scoring v2, § 3.1). La page `/trainer/cle/` outille cette
validation :

1. **Grille Excel pour les experts**, par livre, par chapitre ou sur un
   échantillon de points de choix tirés au hasard (le même pour tous). Elle
   contient les consignes, la grille ancrée (`domain/expert_rubric.py`,
   brouillon à valider) et une ligne par réponse, **sans les points de
   l'auteur** (cotation à l'aveugle). Saisie contrôlée de −3 à +3, colonnes
   « critique » et « justification ».
2. **Import des grilles remplies** : le nom de l'expert et le tour sont lus dans
   la grille ; réimporter remplace ses cotes de ce tour.
3. **Accord entre experts** par compétence et sur le total : ICC(2,1) et
   ICC(2,k), deux facteurs, effets aléatoires, accord absolu, avec les seuils de
   Koo & Li (2016). Liste des réponses à revoir (experts écartés de 3 points ou
   plus, ou médiane écartée de l'auteur de 2 points ou plus) et réponses jugées
   critiques par la majorité.
4. **Synthèse Excel** d'un tour, pour le tour suivant (méthode Delphi).

La clé consensuelle n'est pas encore appliquée au livre. Les champs `Critical`
et `Rationale` d'une réponse sont lus par le jeu : la trace de chaque choix
garde le marqueur critique et la justification de la réponse choisie et de la
meilleure. Le joueur les voit à la fin de chaque scène (« Ce qui était
attendu ») et dans le bilan de session (réponses critiques, puis moments
clés) ; l'export les reprend (colonnes `critique`, `critique_provisoire` — à
−7 ou moins au total — et `justification`). Aucun plafond de note n'est
appliqué en cas de réponse critique.

## Base de données

Les livres restent des fichiers JSON (`data/chapters/`). Les comptes, sessions
et scores sont dans une base SQL, choisie par `DATABASE_URL` :

- **absente** → SQLite dans `instance/eol.db` (développement, démo locale) ;
- **`postgresql://…`** → PostgreSQL hébergé (production). Les URLs
  `postgres://…` fournies par les hébergeurs sont acceptées telles quelles.

Les tables sont créées automatiquement au démarrage : rien à initialiser.
Le dossier `instance/` (base SQLite + clé `secret_key`) est ignoré par git.

| Table | Contenu |
|---|---|
| `users` | Comptes : identifiant, nom affiché, mot de passe haché, rôle (`participant` / `trainer`) |
| `book_sessions` | Un parcours de livre : n° de session, statut, chapitres terminés, états narratifs, résultats figés, feedback |
| `scene_attempts` | Une scène jouée : choix effectués, scores, bornes des réponses proposées à chaque choix, tentative notée ou non |
| `chapter_passages` | Un passage de chapitre : noté ou d'entraînement, dates, états narratifs de départ, résultats figés |
| `passage_attempts` | Les scènes jouées pendant chaque passage |
| `expert_ratings` | Cotes des experts : réponse, expert, tour, points par compétence, critique, justification |

### Opérations courantes (SQLite)

Créer un compte, ou changer le rôle / le mot de passe d'un compte existant :

```bash
flask --app app create-user <identifiant> --role trainer
```

Consulter les comptes (ou utiliser l'espace formateur `/trainer/`, ou l'outil
graphique *DB Browser for SQLite*) :

```bash
sqlite3 instance/eol.db "SELECT id, username, display_name, role FROM users;"
```

Sauvegarder (fonctionne serveur allumé) :

```bash
sqlite3 instance/eol.db ".backup instance/eol-backup.db"
```

Remettre à zéro : arrêter le serveur, supprimer `instance/eol.db`, relancer
(une base vide est recréée).

Supprimer un participant et toutes ses sessions. `PRAGMA foreign_keys=ON` est
indispensable : sans lui, le client `sqlite3` laisse les sessions orphelines.

```bash
sqlite3 instance/eol.db "PRAGMA foreign_keys=ON; DELETE FROM users WHERE username='identifiant';"
```

### Production

SQLite ne convient qu'à un seul serveur dont le disque est **persistant** ;
beaucoup d'hébergeurs (Render, Heroku…) effacent le disque à chaque
redéploiement. Pour une mise en ligne, utiliser PostgreSQL (Supabase en région
UE, Infomaniak, Neon…) — aucun changement de code :

```bash
DATABASE_URL="postgresql://utilisateur:motdepasse@hote:5432/nom_base" python app.py
```

Les sauvegardes sont alors gérées par le fournisseur. Penser aussi à fixer
`SECRET_KEY` (sinon les connexions sont perdues à chaque redéploiement) et
`SESSION_COOKIE_SECURE=1` derrière HTTPS.

### Limite : évolution du schéma

La création automatique **ajoute les tables manquantes mais ne modifie jamais
une table existante**. Ajouter un champ à un modèle (`repositories/orm.py`)
ne met donc pas à jour une base déjà en service : il faudra un outil de
migrations (Alembic), idéalement mis en place avant la mise en production.

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
| `FEEDBACK_BACKEND` | `ENRICH_BACKEND` | Backend du feedback de fin de livre (`openai` ou `ollama`) |
| `DATABASE_URL` | SQLite `instance/eol.db` | Base des comptes et sessions (`postgresql://…` en production) |
| `SECRET_KEY` | générée dans `instance/` | Signature des cookies de session (à fixer en production) |
| `SESSION_COOKIE_SECURE` | — | `1` derrière HTTPS |
| `REGISTRATION_CODE` | — | Si défini, code exigé à l'inscription |
| `APP_TIMEZONE` | `Europe/Zurich` | Fuseau d'affichage des dates |
| `PASSAGE_SPACING_DAYS` | `7` | Délai minimal entre deux passages notés d'un même chapitre |
| `TTS_ENGINE` | `auto` | Voix de lecture : `auto` (Azure si clé, sinon Piper s'il est installé), `piper`, `azure` ou `off` |
| `AZURE_SPEECH_KEY` · `AZURE_SPEECH_REGION` | — | Voix neuronales Azure (ex. région `switzerlandnorth`) |
| `TTS_MODELS_DIR` · `TTS_CACHE_DIR` | `instance/tts/models` · `instance/tts/cache` | Modèles Piper et extraits audio en cache |
| `TTS_DAILY_CHARS` | `400000` | Plafond de caractères synthétisés par jour (coût, abus) |

## Tests

```bash
pytest
```

Couverture actuelle : domain models (round-trip), repository (atomicité), graph service, validation EG-7, filtrage doublons, normalisation des requêtes IA, scoring (rejeu, bornes, pondération), feedback (validation IA, repli), parcours complet comptes → sessions → bilan → droits, export des données (Excel, CSV, JSON, filtres, pseudonymisation), scoring v2 (qualité des choix, passages, règle d'espacement, chapitre rejoué seul, niveaux, reprise des données v1), validation de la clé (ICC vérifié sur l'exemple de Shrout & Fleiss, grille à l'aveugle, import, synthèse), lecture audio (préparation du texte, testée avec Node ; voix serveur : cache, limites, API, Azure simulé, Piper réel s'il est installé).

## Export Mermaid

```bash
python -m exporters.mermaid                       # livre par défaut
python -m exporters.mermaid --book medstudents_y2 # autre livre
```

Génère `output/graphes_<slug>.md`.

## Spécifications

Voir `docs/Cahier_des_charges_IA_EndOfLife.md` (Phase 0 — Éditeur graphique, EG-1 à EG-7).

## Stack technique

- **Backend** : Python 3.11+, Flask, Jinja2, SQLAlchemy (SQLite / PostgreSQL)
- **Frontend** : ES Modules natifs, vis-network (CDN)
- **Tests** : pytest
