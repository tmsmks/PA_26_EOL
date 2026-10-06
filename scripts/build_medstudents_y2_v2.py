#!/usr/bin/env python3
"""
Génère MedStudents_Y2_v2.json à partir des sources de `scripts/medstudents_y2_v2/`.

« Le corps donné » : une année de 2ᵉ, de la salle de dissection au cabinet de
médecine de famille de Montchéry, avec des choix qui ont une mémoire (états
narratifs), des branches parallèles et des histoires annexes. Voir
`docs/MedStudents_Y2_v2_bible.md`.

Le script :
  1. assemble le livre (schéma Chapters > Scenes > Interactions > Responses) ;
  2. le valide : liens, points d'entrée, scènes atteignables et terminables,
     cohérence des états narratifs, une scène jouée par emplacement (zéro ou
     une pour une histoire annexe), issues obligatoires, éventail des choix ;
  3. écrit le JSON, le rapport de répartition des soft skills et la liste des
     images à produire.

Usage : .venv/bin/python scripts/build_medstudents_y2_v2.py [--check]
        (--check : valide sans rien écrire)
"""
from __future__ import annotations

import itertools
import json
import os
import sys
from collections import Counter, defaultdict
from typing import Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from domain.models import Chapter  # noqa: E402
from domain.soft_skills import SOFT_SKILLS, SOFT_SKILL_LABELS  # noqa: E402
from medstudents_y2_v2.book import CHAPTERS, MUTEX, OUTCOMES  # noqa: E402
from medstudents_y2_v2.cast import CAST_KEYS  # noqa: E402
from medstudents_y2_v2.dsl import CODE_OF_SKILL, C, S  # noqa: E402
from services.validation_service import (  # noqa: E402
    validate_entry_points,
    validate_next_interaction_ids,
)

OUT_JSON = os.path.join(ROOT, "data", "chapters", "MedStudents_Y2_v2.json")
OUT_REPORT = os.path.join(ROOT, "docs", "MedStudents_Y2_v2_soft_skills.md")
OUT_REPORT_JSON = os.path.join(ROOT, "docs", "MedStudents_Y2_v2_soft_skills.json")
OUT_ASSETS = os.path.join(ROOT, "docs", "MedStudents_Y2_v2_assets.md")
IMAGES_DIR = os.path.join(ROOT, "data", "images")

CATEGORIES = [
    ("Très bon", lambda t: t >= 9),
    ("Bon", lambda t: 4 <= t <= 8),
    ("Moyen", lambda t: -1 <= t <= 3),
    ("Mauvais", lambda t: -6 <= t <= -2),
    ("Très mauvais", lambda t: t <= -7),
]
SHORT = {"RespectAndDignity": "RD", "Empathy": "EM", "Compassion": "CO",
         "EmotionalRegulation": "ER", "CommunicationClarity": "CC",
         "ProfessionalBoundaries": "PB", "InterprofessionalCollaboration": "IC"}


def category(total: int) -> str:
    for name, test in CATEGORIES:
        if test(total):
            return name
    raise AssertionError(total)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _cond_flags(cond: dict[str, list[str]] | None) -> set[str]:
    return {f for k in ("all", "any", "none") for f in (cond or {}).get(k, [])}


def _eval(cond: dict[str, list[str]] | None, flags: set[str]) -> bool:
    cond = cond or {}
    if not all(f in flags for f in cond.get("all", [])):
        return False
    if cond.get("any") and not any(f in flags for f in cond["any"]):
        return False
    return not any(f in flags for f in cond.get("none", []))


def validate(chapters: list[C]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    book = {"Chapters": [c.to_dict() for c in chapters]}
    typed = [Chapter.from_dict(c) for c in book["Chapters"]]
    errors += [str(e) for e in validate_next_interaction_ids(typed)]
    errors += [str(e) for e in validate_entry_points(typed)]

    set_in: dict[str, set[int]] = defaultdict(set)   # état -> chapitres qui le posent
    read_in: dict[str, set[int]] = defaultdict(set)  # état -> chapitres qui le lisent

    titles = {sc.title for ch in chapters for sc in ch.scenes}
    for title in OUTCOMES:
        if title not in titles:
            errors.append(f"Issues déclarées pour une scène inconnue : {title}")

    for ch in chapters:
        if ch.start_choice:
            for _, flags in ch.start_choice.options:
                for f in flags:
                    read_in[f].add(ch.id)
            for f in ch.start_choice.unless_any:
                read_in[f].add(ch.id)
        seen_ids: set[int] = set()
        for sc in ch.scenes:
            where = f"[{sc.title}]"
            if sc.id in seen_ids:
                errors.append(f"{where} Id de scène en double : {sc.id}")
            seen_ids.add(sc.id)
            if sc.annex and not sc.cond:
                errors.append(f"{where} histoire annexe sans condition")
            for f in _cond_flags(sc.cond):
                read_in[f].add(ch.id)
            for e in sc.entries:
                for f in _cond_flags(e.cond):
                    read_in[f].add(ch.id)
            for d in sc.debriefs:
                for f in _cond_flags(d.cond):
                    read_in[f].add(ch.id)
            _validate_scene(sc, where, errors, warnings, set_in, ch.id)
            for group in OUTCOMES.get(sc.title, []):
                errors += _validate_outcome(sc, where, group)

    for flag, chs in sorted(read_in.items()):
        if flag not in set_in:
            errors.append(f"État « {flag} » lu (ch. {sorted(chs)}) mais jamais posé")
    for flag, chs in sorted(set_in.items()):
        if len(chs) > 1:
            errors.append(f"État « {flag} » posé dans plusieurs chapitres {sorted(chs)} "
                          "(rejouer un chapitre doit pouvoir l'effacer)")
        if flag not in read_in:
            warnings.append(f"État « {flag} » posé (ch. {sorted(chs)}) mais pas encore lu")

    errors += _validate_slots(chapters)
    return errors, warnings


def _validate_scene(sc: S, where: str, errors: list[str], warnings: list[str],
                    set_in: dict[str, set[int]], chapter_id: int) -> None:
    ids = [n.id for n in sc.nodes]
    if len(ids) != len(set(ids)):
        errors.append(f"{where} Id d'interaction en double")
    by_id = {n.id: n for n in sc.nodes}
    for n in sc.nodes:
        if n.actor not in CAST_KEYS:
            errors.append(f"{where} I{n.id} acteur inconnu : {n.actor}")
        if n.actor != "narr" and not n.expr:
            errors.append(f"{where} I{n.id} sans expression")
        totals = [r.total() for r in n.responses]
        for r in n.responses:
            r.soft()  # lève si score illisible
            for f in list(r.sets) + list(r.clears):
                set_in[f].add(chapter_id)
        if 1 < len(n.responses) < 4:
            errors.append(f"{where} I{n.id} : {len(n.responses)} réponses (minimum 4)")
        if len(n.responses) > 6:
            errors.append(f"{where} I{n.id} : {len(n.responses)} réponses (maximum 6)")
        if len(n.responses) >= 4 and (max(totals) < 4 or min(totals) > -2):
            warnings.append(f"{where} I{n.id} éventail de choix étroit {totals}")

    # Atteignabilité depuis l'entrée par défaut et les points d'entrée.
    starts = [sc.nodes[0].id] + [e.interaction for e in sc.entries]
    reached: set[int] = set()
    stack = list(starts)
    while stack:
        cur = stack.pop()
        if cur in reached or cur not in by_id:
            continue
        reached.add(cur)
        stack += [r.next for r in by_id[cur].responses if r.next != -1]
    for n in sc.nodes:
        if n.id not in reached:
            errors.append(f"{where} I{n.id} inatteignable")

    # Chaque interaction doit pouvoir mener à une fin de scène.
    can_end: set[int] = {n.id for n in sc.nodes
                         if not n.responses or any(r.next == -1 for r in n.responses)}
    changed = True
    while changed:
        changed = False
        for n in sc.nodes:
            if n.id not in can_end and any(r.next in can_end for r in n.responses):
                can_end.add(n.id)
                changed = True
    for n in sc.nodes:
        if n.id not in can_end:
            errors.append(f"{where} I{n.id} ne mène à aucune fin de scène")


def _validate_outcome(sc: S, where: str, group: tuple[str, ...]) -> list[str]:
    """Chaque parcours complet de la scène doit poser exactement un état du groupe."""
    errors: list[str] = []
    wanted = set(group)
    by_id = {n.id: n for n in sc.nodes}
    starts = [sc.nodes[0].id] + [e.interaction for e in sc.entries]
    seen: set[tuple[int, frozenset[str]]] = set()
    stack = [(s, frozenset()) for s in starts]
    bad: set[str] = set()

    def finish(state: frozenset[str], at: int) -> None:
        if len(state) != 1:
            bad.add(f"I{at} → {sorted(state) or 'aucun'}")

    while stack:
        nid, state = stack.pop()
        if (nid, state) in seen or nid not in by_id:
            continue
        seen.add((nid, state))
        node = by_id[nid]
        if not node.responses:
            finish(state, nid)
            continue
        for r in node.responses:
            nxt = frozenset((set(state) | (set(r.sets) & wanted)) - set(r.clears))
            if r.next == -1:
                finish(nxt, nid)
            else:
                stack.append((r.next, nxt))
    for b in sorted(bad):
        errors.append(f"{where} fin de parcours sans issue unique parmi {sorted(group)} : {b}")
    return errors


def _validate_slots(chapters: list[C]) -> list[str]:
    """Pour chaque combinaison possible des états qui conditionnent les scènes :
    une et une seule scène jouable par emplacement (zéro ou une pour une histoire
    annexe), et les scènes jouables se succèdent dans l'ordre des emplacements
    (le moteur avance dans la liste sans jamais revenir en arrière)."""
    errors: list[str] = []
    for ch in chapters:
        atoms = sorted({f for sc in ch.scenes for f in _cond_flags(sc.cond)})
        slots: dict[str, list[S]] = defaultdict(list)
        for sc in ch.scenes:
            slots[sc.slot_key].append(sc)
        order = list(slots)
        for n in range(len(atoms) + 1):
            for combo in itertools.combinations(atoms, n):
                flags = set(combo)
                if any(len(flags & set(g)) > 1 for g in MUTEX):
                    continue
                for slot, scenes in slots.items():
                    playable = sum(_eval(sc.cond, flags) for sc in scenes)
                    optional = all(sc.annex for sc in scenes)
                    if playable > 1 or (playable == 0 and not optional):
                        errors.append(f"Ch. {ch.id} emplacement {slot} : {playable} scène(s) "
                                      f"jouable(s) avec les états {sorted(flags)}")
                played = [sc.slot_key for sc in ch.scenes if _eval(sc.cond, flags)]
                if played != sorted(played, key=order.index):
                    errors.append(f"Ch. {ch.id} : ordre de jeu {played} incohérent "
                                  f"avec les états {sorted(flags)}")
    return errors


# ---------------------------------------------------------------------------
# Rapport soft skills
# ---------------------------------------------------------------------------

def _best_path(sc: S, start: int) -> tuple[int, dict[str, int]]:
    """Chemin de somme maximale depuis `start` : (total, points par dimension)."""
    by_id = {n.id: n for n in sc.nodes}
    memo: dict[int, tuple[int, dict[str, int]]] = {}

    def best(nid: int, stack: frozenset[int]) -> tuple[int, dict[str, int]]:
        if nid in memo:
            return memo[nid]
        node = by_id.get(nid)
        empty = {k: 0 for k in SOFT_SKILLS}
        if node is None or nid in stack or not node.responses:
            return 0, empty
        top: tuple[int, dict[str, int]] | None = None
        for r in node.responses:
            soft = r.soft()
            sub_total, sub = (0, empty) if r.next == -1 else best(r.next, stack | {nid})
            total = sum(soft.values()) + sub_total
            if top is None or total > top[0]:
                top = (total, {k: soft[k] + sub[k] for k in SOFT_SKILLS})
        assert top is not None
        memo[nid] = top
        return top

    return best(start, frozenset())


def _code_label(code: str) -> str:
    return next(s for s, c in CODE_OF_SKILL.items() if c == code)


def scene_stats(sc: S) -> dict[str, Any]:
    pos = {k: 0 for k in SOFT_SKILLS}
    neg = {k: 0 for k in SOFT_SKILLS}
    cats: Counter[str] = Counter()
    n_resp = 0
    for n in sc.nodes:
        for r in n.responses:
            n_resp += 1
            soft = r.soft()
            for k, v in soft.items():
                if v > 0:
                    pos[k] += v
                elif v < 0:
                    neg[k] += v
            if len(n.responses) > 1:
                cats[category(sum(soft.values()))] += 1
    total_pos = sum(pos.values()) or 1
    best_total, best_profile = _best_path(sc, sc.nodes[0].id)
    return {
        "title": sc.title,
        "slot": sc.slot_key,
        "condition": sc.cond or {},
        "annex": sc.annex,
        "focus": [SOFT_SKILL_LABELS[_code_label(code)] for code in sc.focus],
        "n_interactions": len(sc.nodes),
        "n_responses": n_resp,
        "positive_points": pos,
        "negative_points": neg,
        "share_percent": {k: round(100 * pos[k] / total_pos) for k in SOFT_SKILLS},
        "categories": {name: cats.get(name, 0) for name, _ in CATEGORIES},
        "best_path_total": best_total,
        "best_path_profile": best_profile,
    }


def build_report(chapters: list[C]) -> tuple[str, dict[str, Any]]:
    data: dict[str, Any] = {"chapters": []}
    lines: list[str] = [
        "# MedStudents Y2 v2 — Répartition des soft skills",
        "",
        "> Généré par `scripts/build_medstudents_y2_v2.py` à partir des scores réels de",
        "> chaque réponse. Ne pas éditer à la main.",
        "",
        "**Lecture.** Pour chaque scène, la part (%) de chaque compétence dans le total",
        "des points positifs *disponibles* (toutes réponses confondues) : c'est ce que",
        "la scène permet de travailler. Le *focus visé* est l'intention de conception",
        "(voir la bible). Les colonnes de choix comptent les réponses par catégorie :",
        "TB très bon (≥ +9), B bon (+4 à +8), M moyen (−1 à +3), Ma mauvais (−6 à −2),",
        "TM très mauvais (≤ −7). ⑂ = branche parallèle (jouée selon les choix",
        "précédents), ✦ = histoire annexe (jouée seulement si elle est débloquée).",
        "",
        "RD Respect et dignité · EM Empathie · CO Compassion · ER Régulation",
        "émotionnelle · CC Clarté de communication · PB Frontières professionnelles ·",
        "IC Collaboration interprofessionnelle.",
        "",
    ]
    head = ("| Scène | Focus visé | Dominantes réelles | "
            + " | ".join(SHORT[k] for k in SOFT_SKILLS) + " | TB | B | M | Ma | TM |")
    sep = "|---|---|---|" + "---:|" * len(SOFT_SKILLS) + "---:|---:|---:|---:|---:|"

    book_pos = {k: 0 for k in SOFT_SKILLS}
    overview: list[str] = []
    for ch in chapters:
        stats = [scene_stats(sc) for sc in ch.scenes]
        ch_pos = {k: sum(s["positive_points"][k] for s in stats) for k in SOFT_SKILLS}
        for k in SOFT_SKILLS:
            book_pos[k] += ch_pos[k]
        ch_total = sum(ch_pos.values()) or 1
        ch_share = {k: round(100 * ch_pos[k] / ch_total) for k in SOFT_SKILLS}
        ch_cats = {name: sum(s["categories"][name] for s in stats) for name, _ in CATEGORIES}
        focus = ", ".join(SHORT[_code_label(code)] for code in ch.focus)
        data["chapters"].append({
            "id": ch.id, "name": ch.name, "focus": focus, "share_percent": ch_share,
            "positive_points": ch_pos, "categories": ch_cats, "scenes": stats,
        })
        overview.append(
            f"| {ch.id}. {ch.name} | {focus} | "
            + " | ".join(_cell(ch_share[k]) for k in SOFT_SKILLS)
            + f" | {sum(s['n_interactions'] for s in stats)} | {sum(s['n_responses'] for s in stats)} |"
        )

        lines += [f"## Chapitre {ch.id} — {ch.name}", "", f"Focus visé : **{focus}**", "", head, sep]
        for s, sc in zip(stats, ch.scenes):
            mark = " ✦" if sc.annex else (" ⑂" if sc.cond else "")
            sfocus = ", ".join(SHORT[_code_label(code)] for code in sc.focus)
            lines.append(
                f"| {s['title']}{mark} | {sfocus} | {_dominant(s['share_percent'])} | "
                + " | ".join(_cell(s["share_percent"][k]) for k in SOFT_SKILLS)
                + " | " + " | ".join(str(s["categories"][n]) for n, _ in CATEGORIES) + " |"
            )
        lines.append(
            f"| **Total chapitre** | | **{_dominant(ch_share)}** | "
            + " | ".join(f"**{ch_share[k]}**" for k in SOFT_SKILLS)
            + " | " + " | ".join(f"**{ch_cats[n]}**" for n, _ in CATEGORIES) + " |"
        )
        lines += ["", "Profil du meilleur parcours (points gagnés sur le chemin idéal) :", "",
                  "| Scène | Total | " + " | ".join(SHORT[k] for k in SOFT_SKILLS) + " |",
                  "|---|---:|" + "---:|" * len(SOFT_SKILLS)]
        for s in stats:
            lines.append(f"| {s['title']} | {s['best_path_total']} | "
                         + " | ".join(str(s["best_path_profile"][k]) for k in SOFT_SKILLS) + " |")
        lines.append("")

    book_total = sum(book_pos.values()) or 1
    book_share = {k: round(100 * book_pos[k] / book_total) for k in SOFT_SKILLS}
    data["book_share_percent"] = book_share
    summary = [
        "## Vue d'ensemble du livre",
        "",
        "| Chapitre | Focus visé | " + " | ".join(SHORT[k] for k in SOFT_SKILLS) + " | Interactions | Réponses |",
        "|---|---|" + "---:|" * len(SOFT_SKILLS) + "---:|---:|",
        *overview,
        "| **Livre** | | " + " | ".join(f"**{book_share[k]}**" for k in SOFT_SKILLS) + " | | |",
        "",
    ]
    idx = lines.index("IC Collaboration interprofessionnelle.") + 2
    lines[idx:idx] = summary
    return "\n".join(lines) + "\n", data


def _dominant(share: dict[str, int], n: int = 3) -> str:
    """Les n compétences qui pèsent le plus dans la scène (ou le chapitre)."""
    top = sorted(SOFT_SKILLS, key=lambda k: -share[k])[:n]
    return ", ".join(SHORT[k] for k in top)


def _cell(pct: int) -> str:
    return f"**{pct}**" if pct >= 20 else str(pct)


def build_assets(book: dict[str, Any]) -> str:
    per_actor: dict[str, set[str]] = defaultdict(set)
    portraits: dict[str, str] = {}
    for ch in book["Chapters"]:
        for sc in ch["Scenes"]:
            for ia in sc["Interactions"]:
                name = ia["Actor"]["Name"]
                if not name:
                    continue
                portraits[name] = ia["Actor"]["ImageName"]
                if ia["AgentFacialExpression"]:
                    per_actor[name].add(ia["AgentFacialExpression"])
    existing = set(os.listdir(IMAGES_DIR)) if os.path.isdir(IMAGES_DIR) else set()
    lines = [
        "# MedStudents Y2 v2 — images à produire",
        "",
        "> Généré par `scripts/build_medstudents_y2_v2.py`. Convention : `<Acteur>.png`",
        "> pour le portrait, `<Acteur>_<émotion>.png` pour l'expression. Les fichiers vont",
        "> dans `data/images/`. Tant qu'une image manque, le parcours affiche les initiales.",
        "",
        "| Personnage | Portrait | Expressions | Présent |",
        "|---|---|---|---|",
    ]
    flat: list[str] = []
    total = present = 0
    for name in sorted(per_actor):
        files = [portraits[name]] + sorted(per_actor[name])
        here = sum(f in existing for f in files)
        total += len(files)
        present += here
        flat += files
        lines.append(f"| {name} | `{portraits[name]}` | "
                     + ", ".join(f"`{f}`" for f in sorted(per_actor[name]))
                     + f" | {here}/{len(files)} |")
    lines += ["", f"**Total : {total} images référencées, {total - present} à produire.**",
              "", "## Liste à plat", "", "```", *flat, "```", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------

def main() -> int:
    check_only = "--check" in sys.argv
    errors, warnings = validate(CHAPTERS)
    for w in warnings:
        print(f"  ! {w}")
    for e in errors:
        print(f"  ✗ {e}")
    if errors:
        print(f"{len(errors)} erreur(s), rien n'est écrit.")
        return 1

    book = {"Chapters": [c.to_dict() for c in CHAPTERS]}
    n_scenes = sum(len(c["Scenes"]) for c in book["Chapters"])
    n_inter = sum(len(s["Interactions"]) for c in book["Chapters"] for s in c["Scenes"])
    n_resp = sum(len(i["Responses"]) for c in book["Chapters"] for s in c["Scenes"]
                 for i in s["Interactions"])
    print(f"{len(CHAPTERS)} chapitre(s), {n_scenes} scènes, {n_inter} interactions, "
          f"{n_resp} réponses, {len(warnings)} avertissement(s).")
    if check_only:
        return 0

    report, data = build_report(CHAPTERS)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        f.write(report)
    with open(OUT_REPORT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(OUT_ASSETS, "w", encoding="utf-8") as f:
        f.write(build_assets(book))
    for path in (OUT_JSON, OUT_REPORT, OUT_REPORT_JSON, OUT_ASSETS):
        print(f"  → {os.path.relpath(path, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
