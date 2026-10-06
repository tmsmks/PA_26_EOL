#!/bin/bash
# Hook Stop : si des fichiers du projet ont changé depuis la dernière mise à
# jour de docs/Journal_de_developpement.md, empêche Claude de terminer tant que
# le journal n'a pas été complété.

input=$(cat)

# Évite la boucle : si Claude continue déjà à cause de ce hook, on le laisse finir.
if [ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false')" = "true" ]; then
  exit 0
fi

root="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
journal="$root/docs/Journal_de_developpement.md"
[ -f "$journal" ] || exit 0

# Fichiers plus récents que le journal, hors environnements, caches, base locale
# et archives automatiques des chapitres.
changed=$(cd "$root" && find . \
  \( -path ./.git -o -path ./.venv -o -path ./venv -o -path ./node_modules \
     -o -path ./instance -o -path ./.claude -o -path ./.pytest_cache \
     -o -path ./data/chapters/history -o -name __pycache__ \) -prune \
  -o -type f -newer "$journal" ! -name .DS_Store ! -name '*.pyc' -print \
  | sed 's|^\./||' | sort)

[ -z "$changed" ] && exit 0

count=$(printf '%s\n' "$changed" | wc -l | tr -d ' ')
list=$(printf '%s\n' "$changed" | head -20 | sed 's/^/- /')
[ "$count" -gt 20 ] && list="$list
- … et $((count - 20)) autre(s)"

reason="Journal de développement à compléter : $count fichier(s) du projet ont changé depuis la dernière mise à jour de docs/Journal_de_developpement.md :
$list

Avant de terminer, ajoute ou complète l'entrée datée du jour à la fin du § 2 (Besoin, Réalisation, Choix et justifications, Résultats, Vérification, Limites, Fichiers), puis mets à jour les § 5 (tests) et § 7 (reste à faire) si besoin. Si ces changements ne viennent pas de cette conversation, examine-les (git diff, contenu des fichiers) pour les décrire. Pour une modification mineure, une ligne suffit. N'écris jamais d'identifiant ni de mot de passe dans le journal."

jq -n --arg r "$reason" '{decision: "block", reason: $r}'
