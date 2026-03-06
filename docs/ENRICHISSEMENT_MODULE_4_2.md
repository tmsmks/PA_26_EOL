# Module d'enrichissement (4.2)

Ce module propose automatiquement de **nouvelles réponses plausibles** pour une interaction donnée, en respectant le cahier des charges (section 4.2).

---

## 1. Rôle du module

Fichier principal : `enrichment.py`

- Extrait le **contexte complet** d’une interaction :
  - Chapitre (`Id`, `Name`)
  - Scène (`Id`, `Title`, `SceneIntroduction`, `Min`)
  - Interaction (`Id`, `Name`, `Text`, `Actor`)
  - Réponses existantes (`Text`, `SoftSkillDimensions`, `LegacyDimensions`, `NextInteractionID`)
- Envoie ce contexte à un **LLM** (OpenAI ou Ollama, au choix).
- Reçoit une liste de **nouvelles réponses candidates** :
  - `Text` (texte exact de la réplique)
  - `Category` : `exemplaire` \| `neutre` \| `problématique`
  - `SoftSkillDimensions` : scores v3 (RespectAndDignity, Empathy, …)
  - `LegacyDimensions` : scores `{ Authenticity, Respect, Compassion, Hope, Empathy }`
- Filtre les doublons pour ne **jamais dupliquer** une réponse existante (même texte).

Aucune insertion automatique n’est faite dans le JSON : le résultat est pensé pour être **relus et validés par un humain**.

---

## 2. Configuration des backends LLM

Le backend est choisi via la variable d’environnement **`ENRICH_BACKEND`** :

- `openai` : utilise l’API OpenAI.
- `ollama` : utilise un modèle local via Ollama.

### 2.1 OpenAI

Pré-requis : compte OpenAI avec crédit.

Dans le terminal :

```bash
export ENRICH_BACKEND="openai"
export OPENAI_API_KEY="sk-...votre_cle..."
export ENRICH_OPENAI_MODEL="gpt-4.1-mini"  # optionnel
```

En cas de **quota dépassé**, le module lève une erreur explicite et suggère de passer à `ENRICH_BACKEND=ollama`.

### 2.2 Ollama (modèle local)

Pré-requis : Ollama installé et en cours d’exécution.

1. Démarrer Ollama et tirer un modèle :

```bash
ollama serve
ollama pull llama3        # ou un autre modèle disponible
```

2. Configurer le backend :

```bash
export ENRICH_BACKEND="ollama"
export ENRICH_OLLAMA_MODEL="llama3"  # nom qui apparaît dans 'ollama list'
export ENRICH_OLLAMA_URL="http://localhost:11434/v1/chat/completions"
```

3. Vérifier que le serveur répond :

```bash
curl http://localhost:11434/api/tags
```

Si cette commande renvoie du JSON, `enrichment.py` peut utiliser Ollama.

---

## 3. Utilisation en ligne de commande

Depuis la racine du projet :

```bash
cd /Users/thomaks/DEV/PA_26_EOL
```

### 3.1 Voir le contexte seul

```bash
python enrichment.py --chapter 1 --scene 1 --interaction 1
```

Affiche un JSON contenant uniquement :

- `context` : toutes les informations nécessaires à l’enrichissement.

### 3.2 Contexte + exemple stub (sans LLM)

```bash
python enrichment.py --chapter 1 --scene 1 --interaction 1 --with-stub
```

Résultat :

- `context` : idem ci-dessus.
- `proposed_responses_stub` : une réponse exemple (hardcodée), **filtrée pour éviter les doublons**.

### 3.3 Contexte + vrai LLM

```bash
python enrichment.py --chapter 1 --scene 1 --interaction 1 --with-llm
```

Selon `ENRICH_BACKEND` :

- OpenAI : appel à `chat.completions.create` avec `response_format={"type": "json_object"}`.
- Ollama : POST HTTP vers `ENRICH_OLLAMA_URL` avec le même format de messages.

Résultat :

- `context` : contexte complet.
- `proposed_responses_llm` : tableau de nouvelles réponses, déjà filtrées contre les textes existants.

---

## 4. Intégration future

Le module est conçu pour être facilement branché :

- dans une **UI Web** (ex. ajouter un bouton « Proposer des réponses IA » dans `graph_viewer`),
- ou dans un **workflow batch** (générer des propositions pour tout un chapitre).

Étapes possibles :

1. Appeler `get_interaction_context(...)` côté serveur ou CLI.
2. Appeler `call_llm_for_enrichment(context)` (ou passer par l’option `--with-llm`).
3. Afficher `proposed_responses_llm` à l’utilisateur, avec :
   - le texte,
   - la catégorie,
   - les scores proposés.
4. Après validation humaine, écrire les réponses choisies dans le JSON des chapitres (nouvelle fonction à ajouter).

