"""Scoring des parcours joueur — logique pure, sans accès base ni HTTP.

Scoring v2 (docs/Scoring_v2_recherche_et_plan.md, § 3) :

1. `replay_scene` rejoue côté serveur les choix envoyés par le navigateur :
   les scores ne sont jamais pris tels quels du client. Chaque pas de la
   trace garde les bornes des réponses proposées à ce moment-là.
2. **Score d'un choix** : la réponse choisie est comparée aux réponses
   proposées au même moment, gain = choisi − pire, écart = meilleur − pire.
   Par compétence, seulement quand elle est en jeu (écart > 0).
3. **Qualité des choix** d'un ensemble de choix = Σ gains / Σ écarts × 100 :
   100 = la meilleure réponse à chaque fois, 0 = la pire, ≈ 50 au hasard.
   Un choix décisif (grand écart) pèse plus qu'un choix anodin. La note
   globale porte sur le total des 7 compétences ; le profil, sur chacune.
   Une compétence n'est notée que si au moins `MIN_SKILL_EVIDENCE` choix
   la mettent en jeu (spécificité du cas : trop peu de choix = note fragile).
4. **Passage** = une partie complète d'un chapitre, l'unité de note.
   `chapter_level` combine les passages comptés d'un chapitre ; fiabilité =
   demi-largeur de l'intervalle à 95 %.
5. `book_profile` : la note du livre est la moyenne des niveaux des
   chapitres évalués (poids égaux) ; le profil par compétence est pondéré
   par le nombre de choix qui mettent chaque compétence en jeu.
6. Feedback : chaque pas de la trace garde la justification de la clé
   (`rationale`) de la réponse choisie et de la meilleure, et le drapeau
   « critique ». `scene_review` en tire le retour de fin de scène ; le bilan
   liste les réponses critiques (`critical_choices`).

Scoring v3, étape A (docs/Scoring_v3_proposition.md, § 2.3 à 2.6 et § 5) :

7. **Poids selon l'âge** : un passage pèse 2^(−âge / 90 jours), au lieu de
   son rang ; « à rafraîchir » si le dernier passage compté a plus de 90 jours.
8. **Progression en points** : gain = moyenne pondérée des passages suivants −
   1ᵉʳ passage, avec sa marge ; « progrès net » seulement au-delà de la marge
   et d'un tiers d'écart-type de la cohorte. Le changement normalisé reste
   calculé une version, pour l'export.
9. **Bandes** (Insuffisant, À consolider, Compétent, Avancé ; seuils
   provisoires 60, 75, 90), données avec leur marge : « entre A et B » si
   l'intervalle déborde d'une bande.
10. **Erreur critique non compensable** : si le dernier passage compté d'un
    chapitre contient une réponse critique, sa bande ne dépasse pas « À
    consolider », quelle que soit la note ; un passage suivant sans réponse
    critique lève le plafond. Au livre, « Compétent » ou plus demande aussi
    qu'aucun chapitre ne soit « Insuffisant » (règle conjonctive provisoire).
11. **Temps de réponse** : un passage où plus d'un quart des choix sont faits
    en moins de 2 secondes est « trop rapide » et ne compte pas.
Les valeurs chiffrées sont des valeurs de départ, à calibrer sur un pilote.
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from math import sqrt
from typing import Any, Iterable, Mapping

from domain.models import Chapter, Response, Scene
from domain.soft_skills import SOFT_SKILLS
from services.graph_service import entry_point_ids

SESSION_WEIGHT_STEP = 0.25
TEXT_MAX = 400
# Nombre minimal de choix mettant une compétence en jeu pour la noter.
MIN_SKILL_EVIDENCE = 8
# Intervalle de confiance à 95 % de la fiabilité.
Z_95 = 1.96

# Seuils pour les « moments clés » transmis au feedback.
MISSED_MIN_GAP = 3
GOOD_MIN_TOTAL = 4

# Scoring v3, étape A : valeurs de départ, provisoires, à calibrer sur le pilote.
LEVEL_HALF_LIFE_DAYS = 90  # poids d'un passage = 2^(−âge / 90 j) (oubli : Legoux et al. 2021)
REFRESH_AFTER_DAYS = 90  # « à rafraîchir » au-delà
BANDS = ("Insuffisant", "À consolider", "Compétent", "Avancé")
BAND_THRESHOLDS = (60, 75, 90)  # en attendant un Angoff modifié (Dwyer et al. 2016)
CRITICAL_CAP_BAND = 1  # « À consolider » : bande maximale avec une erreur critique non résolue
FAST_CHOICE_MS = 2000  # choix fait en moins de 2 s
FAST_SHARE = 0.25  # passage trop rapide : plus d'un quart de choix trop rapides (Baker et al. 2004)
FAST_MIN_TIMED = 8  # pas de jugement sur moins de 8 choix chronométrés
NET_GAIN_SD_FRACTION = 1 / 3  # gain dû à la seule répétition (Lievens et al. 2005)
COHORT_MIN = 10  # écart-type de la cohorte utilisé à partir de 10 personnes

Scores = dict[str, int]


class InvalidPathError(ValueError):
    """Les choix reçus ne décrivent pas un parcours possible de la scène."""


@dataclass
class SceneRun:
    raw: Scores
    lo: Scores
    hi: Scores
    trace: list[dict[str, Any]]


def _zero() -> Scores:
    return {k: 0 for k in SOFT_SKILLS}


def response_scores(r: Response) -> Scores:
    out: Scores = {}
    for k in SOFT_SKILLS:
        try:
            out[k] = int(r.score(k) or 0)
        except (TypeError, ValueError):
            out[k] = 0
    return out


def total(scores: Mapping[str, int]) -> int:
    return sum(int(scores.get(k, 0) or 0) for k in SOFT_SKILLS)


def quoted(text: str) -> str:
    """Entoure de guillemets français, sauf si la réplique les porte déjà.

    Un geste suivi d'une parole (« Poser la main… « Range-le. » ») garde ses
    propres guillemets : on ne l'entoure pas une seconde fois.
    """
    text = str(text or "").strip()
    if "«" not in text:
        return f"« {text} »"
    # Réplique tronquée : le guillemet fermant a sauté.
    return text if text.count("«") <= text.count("»") else text + " »"


def _clip(text: str) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= TEXT_MAX else text[: TEXT_MAX - 1] + "…"


def _rationale(r: Response) -> str:
    """Justification d'une phrase de la clé de cotation (vide si le livre n'en a pas)."""
    return _clip(r._extra.get("Rationale") or "")


def _next_id(r: Response) -> int | None:
    nid = r.NextInteractionID
    return None if nid is None or nid == -1 else int(nid)


def valid_entry_ids(scene: Scene) -> set[int]:
    """Interactions par lesquelles le parcours joueur peut entrer dans la scène."""
    ids = set(entry_point_ids(scene))
    if scene.Interactions:
        ids.add(scene.Interactions[0].Id)
    targets = {_next_id(r) for ia in scene.Interactions for r in ia.Responses}
    ids.update(ia.Id for ia in scene.Interactions if ia.Id not in targets)
    return ids


def skill_bounds(scene: Scene, entry_id: int) -> tuple[Scores, Scores]:
    """(pire, meilleur) total atteignable par compétence depuis `entry_id`.

    Même règle que le moteur joueur (`bestPath`) : un retour en arrière dans
    le graphe coupe le chemin, une interaction sans réponse termine la scène.
    """
    by_id = {ia.Id: ia for ia in scene.Interactions}
    memo: dict[int, tuple[Scores, Scores]] = {}
    on_stack: set[int] = set()

    def visit(iid: int | None) -> tuple[Scores, Scores]:
        if iid is None or iid not in by_id or iid in on_stack:
            return _zero(), _zero()
        if iid in memo:
            return memo[iid]
        on_stack.add(iid)
        lo: Scores | None = None
        hi: Scores | None = None
        for r in by_id[iid].Responses:
            sc = response_scores(r)
            nlo, nhi = visit(_next_id(r))
            cand_lo = {k: sc[k] + nlo[k] for k in SOFT_SKILLS}
            cand_hi = {k: sc[k] + nhi[k] for k in SOFT_SKILLS}
            lo = cand_lo if lo is None else {k: min(lo[k], cand_lo[k]) for k in SOFT_SKILLS}
            hi = cand_hi if hi is None else {k: max(hi[k], cand_hi[k]) for k in SOFT_SKILLS}
        on_stack.discard(iid)
        result = (lo or _zero(), hi or _zero())
        memo[iid] = result
        return result

    return visit(entry_id)


def option_stats(responses: list[Response]) -> dict[str, Any]:
    """Bornes des réponses proposées à un point de choix, et gain moyen au hasard.

    `bounds` : [pire, meilleur] par compétence ; `total_bounds` : idem sur le
    total ; `chance` : gain moyen (total − pire) d'une réponse tirée au hasard.
    """
    opts = [response_scores(r) for r in responses]
    totals = [total(o) for o in opts]
    if not opts:
        return {"bounds": {k: [0, 0] for k in SOFT_SKILLS}, "total_bounds": [0, 0], "chance": 0.0}
    worst = min(totals)
    return {
        "bounds": {k: [min(o[k] for o in opts), max(o[k] for o in opts)] for k in SOFT_SKILLS},
        "total_bounds": [worst, max(totals)],
        "chance": round(sum(t - worst for t in totals) / len(totals), 4),
    }


def enrich_trace(scene: Scene, trace: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Ajoute les bornes des réponses aux pas d'une trace enregistrée avant le v2.

    Les bornes viennent du livre actuel ; un pas dont l'interaction a disparu
    ou n'a plus le même nombre de réponses reste sans bornes (non noté).
    """
    by_id = {ia.Id: ia for ia in scene.Interactions}
    out = []
    for st in trace or []:
        ia = by_id.get(st.get("interaction_id"))
        if "bounds" not in st and ia is not None and len(ia.Responses) == st.get("n_options"):
            st = {**st, **option_stats(ia.Responses)}
        out.append(st)
    return out


def replay_scene(scene: Scene, entry_id: int, choices: list[int]) -> SceneRun:
    """Rejoue une suite d'indices de réponses depuis `entry_id`.

    Lève InvalidPathError si le point d'entrée n'existe pas, si un indice est
    hors limites, ou si le parcours s'arrête avant la fin de la scène.
    """
    if entry_id not in valid_entry_ids(scene):
        raise InvalidPathError(f"Point d'entrée {entry_id} invalide pour la scène {scene.Id}.")
    by_id = {ia.Id: ia for ia in scene.Interactions}
    raw = _zero()
    trace: list[dict[str, Any]] = []
    current: int | None = entry_id

    for step, idx in enumerate(choices):
        ia = by_id.get(current) if current is not None else None
        if ia is None:
            raise InvalidPathError(f"Choix n°{step + 1} après la fin de la scène.")
        if not isinstance(idx, int) or not 0 <= idx < len(ia.Responses):
            raise InvalidPathError(f"Réponse {idx!r} inexistante pour l'interaction {ia.Id}.")
        chosen = ia.Responses[idx]
        sc = response_scores(chosen)
        for k in SOFT_SKILLS:
            raw[k] += sc[k]
        totals = [total(response_scores(r)) for r in ia.Responses]
        best_idx = max(range(len(totals)), key=lambda i: (totals[i], -i))
        trace.append({
            "interaction_id": ia.Id,
            "actor": ia.Actor.Name,
            "prompt": _clip(ia.Text),
            "n_options": len(ia.Responses),
            "choice": {
                "index": idx,
                "text": _clip(chosen.Text),
                "scores": sc,
                "total": totals[idx],
                "critical": bool(chosen._extra.get("Critical")),
                "rationale": _rationale(chosen),
            },
            "best": {
                "index": best_idx,
                "text": _clip(ia.Responses[best_idx].Text),
                "total": totals[best_idx],
                "rationale": _rationale(ia.Responses[best_idx]),
            },
            **option_stats(ia.Responses),
        })
        nid = _next_id(chosen)
        current = nid if nid in by_id else None

    if current is not None and by_id[current].Responses:
        raise InvalidPathError("Parcours incomplet : la scène n'est pas terminée.")

    lo, hi = skill_bounds(scene, entry_id)
    return SceneRun(raw=raw, lo=lo, hi=hi, trace=trace)


# --- Qualité des choix ----------------------------------------------------

def mean_score(scores: Mapping[str, float | None]) -> float | None:
    values = [v for v in scores.values() if v is not None]
    return round(sum(values) / len(values), 1) if values else None


def _pct(part: float, whole: float) -> float | None:
    return round(100 * part / whole, 1) if whole > 0 else None


def choice_quality(steps: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """Qualité d'un ensemble de choix (pas de trace) : Σ gains / Σ écarts.

    - `global` : sur le total des 7 compétences, de 0 à 100 ;
    - `chance_corrected` : (gain − gain au hasard) / (écart − gain au hasard),
      0 = hasard, 100 = meilleur choix, négatif = pire que le hasard ;
    - `best_rate` : part des choix où la meilleure réponse a été choisie (%) ;
    - `scores` : par compétence, None si moins de MIN_SKILL_EVIDENCE choix la
      mettent en jeu ; `raw_scores` : sans ce seuil (pour agréger plus haut) ;
    - `steps` : [gain, écart] du total pour chaque choix (fiabilité).
    """
    gain = {k: 0 for k in SOFT_SKILLS}
    span = {k: 0 for k in SOFT_SKILLS}
    evidence = {k: 0 for k in SOFT_SKILLS}
    t_gain = t_span = t_chance = 0.0
    n_best = 0
    pairs: list[list[float]] = []
    for st in steps:
        bounds = st.get("bounds")
        if not bounds:  # trace v1 non enrichie : pas notable
            continue
        points = (st.get("choice") or {}).get("scores") or {}
        for k in SOFT_SKILLS:
            lo, hi = bounds.get(k, [0, 0])
            if hi > lo:
                gain[k] += int(points.get(k, 0) or 0) - lo
                span[k] += hi - lo
                evidence[k] += 1
        lo, hi = st.get("total_bounds") or [0, 0]
        if hi > lo:
            g = st["choice"]["total"] - lo
            t_gain += g
            t_span += hi - lo
            t_chance += float(st.get("chance") or 0)
            n_best += st["choice"]["total"] >= hi
            pairs.append([g, hi - lo])
    raw_scores = {k: _pct(gain[k], span[k]) for k in SOFT_SKILLS}
    return {
        "global": _pct(t_gain, t_span),
        "chance_corrected": _pct(t_gain - t_chance, t_span - t_chance),
        # Taux de meilleure réponse (cotation dichotomique), calculé à côté de la qualité
        # pour le pilote : au hasard, environ 20 % sur le livre 2 (Weng et al. 2018).
        "best_rate": _pct(n_best, len(pairs)),
        "scores": {k: v if evidence[k] >= MIN_SKILL_EVIDENCE else None for k, v in raw_scores.items()},
        "raw_scores": raw_scores,
        "evidence": evidence,
        "detail": {k: {"gain": gain[k], "span": span[k], "evidence": evidence[k]} for k in SOFT_SKILLS},
        "n_choices": len(pairs),
        "steps": pairs,
    }


def _steps(attempts: Iterable[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [st for a in attempts for st in a.get("trace") or []]


def rank_skills(scores: Mapping[str, float | None]) -> tuple[list[str], list[str]]:
    """(forces, faiblesses) : jusqu'à 3 de chaque, sans recouvrement.

    Relatif au profil du participant : une force est au-dessus de sa moyenne,
    une faiblesse en dessous (au moins une de chaque dès 2 compétences notées).
    Les faiblesses sont listées de la plus faible à la moins faible.
    """
    ranked = sorted(
        (k for k in SOFT_SKILLS if scores.get(k) is not None),
        key=lambda k: (-(scores[k] or 0), SOFT_SKILLS.index(k)),
    )
    if len(ranked) < 2:
        return ranked, []
    mean = sum(scores[k] for k in ranked) / len(ranked)
    half = len(ranked) // 2
    strengths = [k for k in ranked[: min(3, half)] if scores[k] >= mean] or ranked[:1]
    rest = [k for k in reversed(ranked) if k not in strengths]
    weaknesses = [k for k in rest[:3] if scores[k] < mean] or rest[:1]
    return strengths, weaknesses


def chapters_to_rework(
    chapters: list[dict[str, Any]], weaknesses: list[str], limit: int = 2
) -> list[int]:
    """Chapitres les plus faibles sur les compétences à travailler."""
    ranked: list[tuple[float, int]] = []
    for ch in chapters:
        values = [ch["scores"][k] for k in weaknesses if ch["scores"].get(k) is not None]
        basis = sum(values) / len(values) if values else ch["global"]
        if basis is not None:
            ranked.append((basis, ch["id"]))
    ranked.sort()
    return [cid for _, cid in ranked[:limit]]


def _located_steps(attempts: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Pas des traces, avec leur chapitre, leur scène et l'écart au meilleur choix."""
    return [
        {
            **st,
            "chapter_id": a["chapter_id"],
            "scene_title": a.get("scene_title", ""),
            "gap": st["best"]["total"] - st["choice"]["total"],
        }
        for a in attempts
        for st in a.get("trace") or []
    ]


def critical_choices(attempts: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Réponses critiques choisies, dans l'ordre du jeu (proposition v3 : listées)."""
    return [s for s in _located_steps(attempts) if s["choice"].get("critical")]


def key_moments(
    attempts: Iterable[Mapping[str, Any]],
    n_missed: int = 5,
    n_good: int = 3,
    exclude_critical: bool = False,
) -> dict[str, list[dict[str, Any]]]:
    """Occasions manquées (plus gros écart au meilleur choix) et réussites.

    `exclude_critical` : les réponses critiques, listées à part, ne sont pas
    reprises parmi les occasions manquées.
    """
    steps = _located_steps(attempts)
    missed = sorted(
        (
            s for s in steps
            if s["gap"] >= MISSED_MIN_GAP and not (exclude_critical and s["choice"].get("critical"))
        ),
        key=lambda s: -s["gap"],
    )[:n_missed]
    good = sorted(
        (s for s in steps if s["gap"] <= 0 and s["choice"]["total"] >= GOOD_MIN_TOTAL),
        key=lambda s: -s["choice"]["total"],
    )[:n_good]
    return {"missed": missed, "good": good}


def scene_review(trace: Iterable[Mapping[str, Any]], limit: int = 3) -> list[dict[str, Any]]:
    """Retour de fin de scène : les choix les plus décisifs, avec la justification.

    Feedback d'abord (proposition v3, § 2.7) : ce qui était attendu et pourquoi.
    Seuls les choix dont la clé donne une justification sont retenus. Toutes les
    réponses critiques d'abord, puis les écarts au meilleur choix (du plus grand
    au plus petit), jusqu'à `limit` ; sans écart, le choix le plus décisif.
    """
    steps = [st for st in trace if (st.get("choice") or {}).get("rationale")]

    def gap(st: Mapping[str, Any]) -> int:
        return st["best"]["total"] - st["choice"]["total"]

    def span(st: Mapping[str, Any]) -> int:
        lo, hi = st.get("total_bounds") or [0, 0]
        return hi - lo

    critical = [st for st in steps if st["choice"].get("critical")]
    missed = sorted(
        (st for st in steps if gap(st) > 0 and not st["choice"].get("critical")),
        key=lambda st: (-gap(st), -span(st)),
    )
    picked = critical + missed[: max(0, limit - len(critical))]
    if not picked and steps:
        picked = [max(steps, key=span)]
    return [
        {
            "scene_title": st.get("scene_title") or "",
            "actor": st.get("actor") or "",
            "prompt": st.get("prompt") or "",
            "is_best": gap(st) <= 0,
            "choice": {
                "text": st["choice"]["text"],
                "critical": bool(st["choice"].get("critical")),
                "rationale": st["choice"]["rationale"],
            },
            "best": {"text": st["best"]["text"], "rationale": st["best"].get("rationale") or ""},
        }
        for st in picked
    ]


def chapter_review(attempts: Iterable[Mapping[str, Any]], limit: int = 3) -> list[dict[str, Any]]:
    """Retour de fin de chapitre : les choix les plus décisifs de tout le passage,
    avec leur scène (mêmes règles que `scene_review`)."""
    steps = [
        {**st, "scene_title": a.get("scene_title", "")}
        for a in attempts
        for st in a.get("trace") or []
    ]
    return scene_review(steps, limit)


def session_results(
    chapters: list[Chapter], attempts: list[Mapping[str, Any]]
) -> dict[str, Any]:
    """Instantané d'une session : qualité des choix, chapitres, moments clés.

    `attempts` : tentatives notées, sous forme de dicts
    {chapter_id, scene_id, scene_title, trace}.
    """
    q = choice_quality(_steps(attempts))
    chapter_rows: list[dict[str, Any]] = []
    for ch in chapters:
        ch_attempts = [a for a in attempts if a["chapter_id"] == ch.Id]
        cq = choice_quality(_steps(ch_attempts))
        chapter_rows.append({
            "id": ch.Id,
            "name": ch.Name,
            "scores": cq["scores"],
            "global": cq["global"],
            "n_scenes": len(ch_attempts),
            "n_choices": cq["n_choices"],
        })

    strengths, weaknesses = rank_skills(q["scores"])
    return {
        "version": 2,
        "scores": q["scores"],
        "detail": q["detail"],
        "global": q["global"],
        "chance_corrected": q["chance_corrected"],
        "best_rate": q["best_rate"],
        "n_choices": q["n_choices"],
        "chapters": chapter_rows,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "chapters_to_rework": chapters_to_rework(chapter_rows, weaknesses),
        "critical": critical_choices(attempts),
        "moments": key_moments(attempts, exclude_critical=True),
        "n_scenes": len(attempts),
    }


def passage_results(attempts: list[Mapping[str, Any]]) -> dict[str, Any]:
    """Instantané d'un passage de chapitre (tentatives notées du passage)."""
    q = choice_quality(_steps(attempts))
    strengths, weaknesses = rank_skills(q["scores"])
    return {
        "version": 2,
        "global": q["global"],
        "chance_corrected": q["chance_corrected"],
        "best_rate": q["best_rate"],
        "scores": q["scores"],
        "raw_scores": q["raw_scores"],
        "evidence": q["evidence"],
        "n_choices": q["n_choices"],
        "n_scenes": len(attempts),
        "steps": q["steps"],
        "strengths": strengths,
        "weaknesses": weaknesses,
        "moments": key_moments(attempts, n_missed=2, n_good=1),
        "n_critical": len(critical_choices(attempts)),
        "timing": passage_timing(attempts),
    }


def passage_timing(attempts: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """Temps de réponse des choix d'un passage, et drapeau « trop rapide ».

    Seuls comptent les vrais choix (au moins deux réponses) dont le navigateur a
    envoyé le temps (`time_ms`). Trop rapide : au moins `FAST_MIN_TIMED` choix
    chronométrés, dont plus de `FAST_SHARE` en moins de `FAST_CHOICE_MS`.
    """
    times = [
        float(st["time_ms"])
        for a in attempts
        for st in a.get("trace") or []
        if (st.get("n_options") or 0) > 1 and isinstance(st.get("time_ms"), (int, float))
    ]
    n_fast = sum(1 for t in times if t < FAST_CHOICE_MS)
    return {
        "n_timed": len(times),
        "n_fast": n_fast,
        "median_ms": round(statistics.median(times)) if times else None,
        "threshold_ms": FAST_CHOICE_MS,
        "too_fast": len(times) >= FAST_MIN_TIMED and n_fast > FAST_SHARE * len(times),
    }


# --- Niveau d'un chapitre sur plusieurs passages ---------------------------

def as_datetime(value: Any) -> datetime | None:
    """Date d'un passage (datetime ou texte ISO) ; sans fuseau = UTC (SQLite)."""
    if value is None:
        return None
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value)
        except ValueError:
            return None
    if not isinstance(value, datetime):
        return None
    return value if value.tzinfo is not None else value.replace(tzinfo=timezone.utc)


def age_weight(completed_at: Any, now: datetime) -> float:
    """Poids d'un passage selon son âge : 1 aujourd'hui, 0,5 à 90 jours, 0,25 à 180."""
    done = as_datetime(completed_at)
    if done is None:
        return 1.0
    age_days = max(0.0, (now - done).total_seconds() / 86400)
    return 2 ** (-age_days / LEVEL_HALF_LIFE_DAYS)


def band_index(value: float, thresholds: Iterable[float] = BAND_THRESHOLDS) -> int:
    return sum(1 for t in thresholds if value >= t)


def band(
    level: float | None,
    margin: float | None,
    capped: bool = False,
    thresholds: Iterable[float] | None = None,
) -> dict[str, Any] | None:
    """Bande d'un niveau, donnée avec sa marge.

    Si l'intervalle niveau ± marge tient dans une bande, on la donne ; sinon
    « entre A et B ». `capped` (erreur critique non résolue) : jamais au-dessus
    de « À consolider ». `thresholds` : seuils fixés par des juges (Angoff) pour
    ce chapitre, sinon les seuils provisoires.
    """
    if level is None:
        return None
    th = tuple(thresholds) if thresholds else BAND_THRESHOLDS
    m = margin or 0.0
    lo = band_index(max(0.0, level - m), th)
    hi = band_index(min(100.0, level + m), th)
    limited = capped and hi > CRITICAL_CAP_BAND
    if capped:
        lo, hi = min(lo, CRITICAL_CAP_BAND), min(hi, CRITICAL_CAP_BAND)
    return {
        "low": BANDS[lo],
        "high": BANDS[hi],
        "label": BANDS[lo] if lo == hi else f"entre {BANDS[lo]} et {BANDS[hi]}",
        "settled": lo == hi,
        "capped": limited,
        "thresholds": list(th),
        "angoff": bool(thresholds),
    }


PROGRESS_LABELS = {
    "net_gain": "progrès net",
    "possible_gain": "progrès probable, pas encore démontré",
    "net_loss": "baisse nette",
    "stable": "pas de changement démontré",
}


def progress_status(gain: float, gain_margin: float | None, cohort_sd: float | None = None) -> dict[str, Any]:
    """Un gain n'est « net » que s'il dépasse sa marge et le tiers d'un écart-type
    de la cohorte (ce que rapporte la simple répétition). Sans cohorte assez
    grande, seule la marge s'applique."""
    sd_min = NET_GAIN_SD_FRACTION * cohort_sd if cohort_sd else None
    clear = gain_margin is not None and abs(gain) > gain_margin and (sd_min is None or abs(gain) > sd_min)
    if gain > 0:
        status = "net_gain" if clear else "possible_gain"
    elif gain < 0 and clear:
        status = "net_loss"
    else:
        status = "stable"
    return {
        "status": status,
        "label": PROGRESS_LABELS[status],
        "sd_min": round(sd_min, 1) if sd_min else None,
    }


def normalized_change(pre: float | None, post: float | None) -> float | None:
    """Changement normalisé (Marx & Cummings 2007), en % de ce qui restait.

    Hausse : (après − avant) / (100 − avant) ; baisse : (après − avant) / avant.
    None si indéfini (avant = après = 0 ou 100, ou valeur manquante).
    """
    if pre is None or post is None:
        return None
    if post > pre:
        return round(100 * (post - pre) / (100 - pre), 1)
    if post < pre:
        return round(100 * (post - pre) / pre, 1)
    return None if pre in (0, 100) else 0.0


def level_margin(passages: list[Mapping[str, Any]], weights: list[float]) -> float | None:
    """Demi-largeur de l'intervalle à 95 % du niveau, en points.

    Chaque choix est une observation (qualité = gain / écart) ; un passage pèse
    son poids, réparti entre ses choix selon leur écart. Plus il y a de choix
    et de passages, plus l'intervalle se resserre.
    """
    obs: list[tuple[float, float]] = []
    for w_p, p in zip(weights, passages):
        pairs = [(g, s) for g, s in p.get("steps") or [] if s > 0]
        span = sum(s for _, s in pairs)
        obs += [(w_p * s / span, g / s) for g, s in pairs] if span else []
    sw = sum(w for w, _ in obs)
    sw2 = sum(w * w for w, _ in obs)
    if not obs or sw2 == 0:
        return None
    n_eff = sw * sw / sw2
    if n_eff < 2:
        return None
    mean = sum(w * q for w, q in obs) / sw
    var = sum(w * (q - mean) ** 2 for w, q in obs) / sw
    return round(100 * Z_95 * (var / n_eff) ** 0.5, 1)


def chapter_level(
    passages: list[Mapping[str, Any]],
    now: datetime | None = None,
    cohort_sd: float | None = None,
    thresholds: Iterable[float] | None = None,
) -> dict[str, Any] | None:
    """Niveau d'un chapitre à partir des résultats de ses passages comptés.

    `passages` : du plus ancien au plus récent, avec `completed_at` et
    `n_critical`. Chaque passage pèse 2^(−âge / 90 j). None si aucun passage
    n'a de note. `cohort_sd` : écart-type des 1ᵉʳˢ passages de la cohorte.
    """
    rated = [p for p in passages if p.get("global") is not None]
    if not rated:
        return None
    now = now or datetime.now(timezone.utc)
    weights = [age_weight(p.get("completed_at"), now) for p in rated]
    level = round(sum(w * p["global"] for w, p in zip(weights, rated)) / sum(weights), 1)

    raw_scores: dict[str, float | None] = {}
    evidence: dict[str, float] = {}
    for k in SOFT_SKILLS:
        num = den = 0.0
        for w, p in zip(weights, rated):
            v = (p.get("raw_scores") or {}).get(k)
            if v is not None:
                num += w * v
                den += w
        raw_scores[k] = round(num / den, 1) if den else None
        evidence[k] = sum((p.get("evidence") or {}).get(k, 0) for p in rated) / len(rated)
    margin = level_margin(rated, weights)

    gain = gain_margin = progress = None
    if len(rated) > 1:
        rest, w_rest = rated[1:], weights[1:]
        after = sum(w * p["global"] for w, p in zip(w_rest, rest)) / sum(w_rest)
        gain = round(after - rated[0]["global"], 1)
        m_first = level_margin(rated[:1], [1.0])
        m_rest = level_margin(rest, w_rest)
        if m_first is not None and m_rest is not None:
            gain_margin = round(sqrt(m_first ** 2 + m_rest ** 2), 1)
        progress = progress_status(gain, gain_margin, cohort_sd)

    last = rated[-1]
    n_critical_open = int(last.get("n_critical") or 0)
    last_at = as_datetime(last.get("completed_at"))
    return {
        "level": level,
        "scores": {
            k: v if evidence[k] >= MIN_SKILL_EVIDENCE else None for k, v in raw_scores.items()
        },
        "raw_scores": raw_scores,
        "evidence": evidence,
        "first": rated[0]["global"],
        "last": last["global"],
        "gain": gain,
        "gain_margin": gain_margin,
        "progress": progress,
        # Ancien indicateur (changement normalisé), gardé une version pour l'export.
        "progression": normalized_change(rated[0]["global"], level) if len(rated) > 1 else None,
        "margin": margin,
        "band": band(level, margin, capped=n_critical_open > 0, thresholds=thresholds),
        "n_critical_open": n_critical_open,
        "critical_capped": n_critical_open > 0,
        "refresh": bool(last_at and (now - last_at).days > REFRESH_AFTER_DAYS),
        "last_at": last_at.isoformat() if last_at else None,
        "n_passages": len(rated),
        "n_choices": sum(p.get("n_choices") or 0 for p in rated),
        "weights": [round(w, 3) for w in weights],
        "points": [{"number": i, "global": p["global"]} for i, p in enumerate(rated, start=1)],
    }


def book_profile(levels: Mapping[int, Mapping[str, Any] | None], n_chapters: int) -> dict[str, Any]:
    """Profil du livre à partir des niveaux de ses chapitres.

    Note = moyenne des niveaux des chapitres évalués (poids égaux) ; profil
    par compétence pondéré par le nombre de choix qui la mettent en jeu ;
    marge = √(Σ marges²) / nombre de chapitres. Bande du livre : règle
    conjonctive, pas au-dessus de « À consolider » si un chapitre est
    « Insuffisant » ou garde une erreur critique non résolue.
    """
    rated = {cid: lv for cid, lv in levels.items() if lv}
    scores: dict[str, float | None] = {}
    for k in SOFT_SKILLS:
        num = den = 0.0
        for lv in rated.values():
            v, ev = lv["raw_scores"].get(k), lv["evidence"].get(k, 0)
            if v is not None and ev:
                num += ev * v
                den += ev
        scores[k] = round(num / den, 1) if den >= MIN_SKILL_EVIDENCE else None
    strengths, weaknesses = rank_skills(scores)
    n = len(rated)
    global_ = round(sum(lv["level"] for lv in rated.values()) / n, 1) if n else None

    margins = [lv.get("margin") for lv in rated.values()]
    margin = round(sqrt(sum(m * m for m in margins)) / n, 1) if n and all(m is not None for m in margins) else None
    insufficient = sorted(cid for cid, lv in rated.items() if (lv.get("band") or {}).get("high") == BANDS[0])
    open_critical = sorted(cid for cid, lv in rated.items() if lv.get("critical_capped"))
    # Seuils du livre : moyenne des seuils de ses chapitres (Angoff ou provisoires).
    chapter_th = [(lv.get("band") or {}).get("thresholds") for lv in rated.values()]
    custom = any((lv.get("band") or {}).get("angoff") for lv in rated.values())
    book_th = (
        [round(sum(t[i] for t in chapter_th) / len(chapter_th), 1) for i in range(len(BAND_THRESHOLDS))]
        if custom and all(chapter_th) else None
    )
    book_band = band(global_, margin, capped=bool(insufficient or open_critical), thresholds=book_th)

    gains = [lv for lv in rated.values() if lv.get("gain") is not None]
    progress = None
    if gains:
        gain = round(sum(lv["gain"] for lv in gains) / len(gains), 1)
        gm = [lv.get("gain_margin") for lv in gains]
        gain_margin = round(sqrt(sum(m * m for m in gm)) / len(gains), 1) if all(m is not None for m in gm) else None
        sds = [(lv.get("progress") or {}).get("sd_min") for lv in gains]
        sd = 3 * sum(sds) / len(sds) if all(sds) else None
        progress = {"gain": gain, "gain_margin": gain_margin, "n_chapters": len(gains),
                    **progress_status(gain, gain_margin, sd)}
    progressions = [lv["progression"] for lv in rated.values() if lv.get("progression") is not None]
    return {
        "global": global_,
        "margin": margin,
        "band": book_band,
        "insufficient_chapters": insufficient,
        "critical_chapters": open_critical,
        "scores": scores,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "n_evaluated": n,
        "n_chapters": n_chapters,
        "complete": bool(rated) and n >= n_chapters,
        "n_passages": sum(lv["n_passages"] for lv in rated.values()),
        "progress": progress,
        # Ancien indicateur (moyenne des changements normalisés), gardé une version.
        "progression": round(sum(progressions) / len(progressions), 1) if progressions else None,
    }


def group_change(pairs: list[tuple[float, float]]) -> dict[str, Any] | None:
    """Progrès d'un groupe entre le 1ᵉʳ et le dernier passage compté d'un chapitre.

    *d* de Cohen = (moyenne du dernier − moyenne du 1ᵉʳ) / écart-type moyen
    √((s₁² + s₂²) / 2), avec la corrélation entre les deux passages, comme le
    recommandent Nissen et al. (2018) plutôt que le gain normalisé. None si
    moins de 2 personnes ont deux passages comptés.
    """
    if len(pairs) < 2:
        return None
    first = [a for a, _ in pairs]
    last = [b for _, b in pairs]
    s1, s2 = statistics.stdev(first), statistics.stdev(last)
    pooled = sqrt((s1 * s1 + s2 * s2) / 2)
    m1, m2 = statistics.fmean(first), statistics.fmean(last)
    r = None
    if len(pairs) >= 3 and s1 > 0 and s2 > 0:
        r = round(statistics.correlation(first, last), 2)
    return {
        "n": len(pairs),
        "mean_first": round(m1, 1),
        "mean_last": round(m2, 1),
        "sd_first": round(s1, 1),
        "sd_last": round(s2, 1),
        "r": r,
        "d": round((m2 - m1) / pooled, 2) if pooled > 0 else None,
    }


# --- Pondération entre sessions -------------------------------------------

def session_weight(rank: int) -> float:
    """Poids du Nᵉ passage compté (ou de la Nᵉ session terminée) : 1 ; 1,25 ; 1,5 ; …"""
    return 1 + SESSION_WEIGHT_STEP * (max(1, rank) - 1)


def weighted_profile(results: list[Mapping[str, Any]]) -> dict[str, Any] | None:
    """Note pondérée à partir des résultats des sessions terminées.

    `results` est ordonné chronologiquement (1ʳᵉ session en premier).
    Par compétence : moyenne pondérée des scores de session ; la note
    globale est la moyenne des compétences.
    """
    if not results:
        return None
    weights = [session_weight(i) for i in range(1, len(results) + 1)]
    scores: dict[str, float | None] = {}
    for k in SOFT_SKILLS:
        num = den = 0.0
        for w, res in zip(weights, results):
            v = (res.get("scores") or {}).get(k)
            if v is not None:
                num += w * v
                den += w
        scores[k] = round(num / den, 1) if den else None
    return {
        "scores": scores,
        "global": mean_score(scores),
        "n_sessions": len(results),
        "weights": weights,
    }


def score_deltas(
    current: Mapping[str, float | None], previous: Mapping[str, float | None]
) -> dict[str, float | None]:
    """Écart par compétence entre deux sessions (None si non comparable)."""
    out: dict[str, float | None] = {}
    for k in SOFT_SKILLS:
        a, b = current.get(k), previous.get(k)
        out[k] = round(a - b, 1) if a is not None and b is not None else None
    return out
