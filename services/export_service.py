"""Export des données de jeu pour l'analyse (tableur, R, Python…).

Sept tables plates, une ligne par objet, avec les identifiants répétés pour
qu'on puisse filtrer chaque feuille seule :
- participants : un compte ;
- niveaux : un chapitre évalué d'un participant (niveau, progression, fiabilité) ;
- passages : une partie complète d'un chapitre (l'unité de note) ;
- sessions : un parcours de l'histoire d'un livre, avec son bilan ;
- chapitres : un chapitre joué dans une session (bilan de session) ;
- scenes : une scène jouée (tentative), qualité des choix par compétence ;
- choix : une réponse donnée, avec la meilleure réponse possible à cette étape.

Scoring v2 (docs/Scoring_v2_recherche_et_plan.md) : chaque choix est comparé
aux réponses proposées au même moment ; qualité = Σ gains / Σ écarts × 100.
"""
from __future__ import annotations

import os
import unicodedata
from datetime import datetime, timezone
from typing import Any
from zoneinfo import ZoneInfo

from books import get_book
from domain.models import Chapter
from domain.soft_skills import SOFT_SKILL_LABELS, SOFT_SKILLS
from exporters.tables import Table
from repositories.orm import BookSession, ChapterPassage, User
from services.history_service import chapter_progress, cohort_first_sds
from services.expert_key_service import CRITICAL_PROVISIONAL_TOTAL
from services.scoring_service import MIN_SKILL_EVIDENCE, TEXT_MAX, choice_quality
from services.session_service import as_utc, passage_attempt_dicts, results_from_passages


def _slug(label: str) -> str:
    plain = unicodedata.normalize("NFKD", label).encode("ascii", "ignore").decode()
    return "_".join(plain.lower().split())


# Colonne de chaque compétence : « Respect et dignité » → respect_et_dignite.
SKILL_COLUMNS: dict[str, str] = {k: _slug(SOFT_SKILL_LABELS[k]) for k in SOFT_SKILLS}


def _skills(description: str, suffix: str = "") -> list[tuple[str, str]]:
    return [
        (SKILL_COLUMNS[k] + suffix, description.format(skill=SOFT_SKILL_LABELS[k]))
        for k in SOFT_SKILLS
    ]


PARTICIPANT = ("participant", "Identifiant de connexion, ou code P + n° du compte si l'export est pseudonymisé.")
NAME = ("nom", "Nom affiché (vide si l'export est pseudonymisé).")
SESSION_ID = ("session_id", "Identifiant de la session : relie les tables entre elles.")
PASSAGE_ID = ("passage_id", "Identifiant du passage de chapitre : relie passages, scènes et choix.")
BOOK = ("livre", "Identifiant du livre.")
SESSION_NO = ("session_no", "Rang de la session pour ce participant et ce livre (1, 2, 3…).")
CHAPTER_ID = ("chapitre_id", "Numéro du chapitre.")
CHAPTER = ("chapitre", "Titre du chapitre.")
RESULTS = ("resultats", "definitifs (figés à la fin du livre) ou provisoires (session en cours).")
QUALITY = ("qualite", "Qualité des choix sur le total des 7 compétences, sur 100 : 100 = la meilleure "
                      "réponse à chaque fois, 0 = la pire, environ 50 au hasard.")
CHANCE = ("qualite_corrigee_hasard", "Même note corrigée du hasard : 0 = hasard, 100 = meilleur choix, "
                                     "négatif = pire que le hasard.")
SKILL_100 = ("{skill}, qualité des choix sur 100 (vide si moins de "
             f"{MIN_SKILL_EVIDENCE} choix mettent la compétence en jeu).")

PARTICIPANT_COLUMNS = [
    PARTICIPANT,
    NAME,
    ("role", "participant ou formateur."),
    ("inscription", "Création du compte."),
    ("derniere_connexion", "Dernière connexion."),
    ("passages_notes", "Passages de chapitre comptés dans les niveaux."),
    ("passages_entrainement", "Passages d'entraînement (trop proches d'un passage compté)."),
    ("sessions_terminees", "Sessions (histoire complète d'un livre) terminées."),
    ("sessions_en_cours", "Sessions en cours."),
]

LEVEL_COLUMNS = [
    PARTICIPANT,
    BOOK,
    CHAPTER_ID,
    CHAPTER,
    ("niveau", "Moyenne pondérée des passages comptés : un passage pèse 2^(−âge en jours / 90), "
               "1 aujourd'hui, 0,5 à 90 jours (depuis le 13.10.2026 ; avant : selon le rang)."),
    ("fourchette", "Demi-largeur de l'intervalle de confiance à 95 % du niveau, en points."),
    ("bande", "Bande de niveau (seuils provisoires 60, 75, 90, ou seuils Angoff du chapitre), donnée avec sa marge : « entre A et B » "
              "si l'intervalle déborde d'une bande ; jamais au-dessus de « À consolider » si le "
              "dernier passage compté contient une réponse critique."),
    ("plafond_critique", "1 si le dernier passage compté contient une réponse critique (bande plafonnée)."),
    ("gain_points", "Progression : moyenne pondérée des passages suivants − 1ᵉʳ passage, en points ; "
                    "vide avec un seul passage."),
    ("marge_gain", "Marge à 95 % du gain, en points."),
    ("progres", "progrès net (gain au-delà de sa marge et d'un tiers d'écart-type de la cohorte), "
                "progrès probable, pas encore démontré, baisse nette, ou pas de changement démontré."),
    ("a_rafraichir", "1 si le dernier passage compté a plus de 90 jours."),
    ("progression", "Ancien indicateur, gardé une version : changement normalisé en % de ce qui "
                    "restait à gagner. Il favorise ceux qui partent haut (Nissen et al. 2018) ; "
                    "remplacé par gain_points."),
    ("premier_passage", "Qualité des choix au 1ᵉʳ passage compté (« score à froid »)."),
    ("dernier_passage", "Qualité des choix au dernier passage compté."),
    ("passages_notes", "Passages comptés."),
    ("choix", "Choix notés, tous passages comptés."),
    *_skills(SKILL_100),
]

PASSAGE_COLUMNS = [
    PASSAGE_ID,
    PARTICIPANT,
    BOOK,
    CHAPTER_ID,
    CHAPTER,
    SESSION_ID,
    SESSION_NO,
    ("passage_no", "Rang du passage pour ce participant et ce chapitre (1, 2, 3…)."),
    ("compte", "1 si le passage compte dans le niveau (1ᵉʳ passage, ou assez espacé du précédent "
               "passage compté : voir le délai dans lisez-moi ; et pas joué trop vite), 0 = entraînement."),
    ("trop_rapide", "1 si plus d'un quart des choix chronométrés ont été faits en moins de 2 secondes "
                    "(seuil provisoire) : le passage ne compte pas."),
    ("choix_chronometres", "Choix dont le navigateur a envoyé le temps de réponse."),
    ("choix_rapides", "Choix faits en moins de 2 secondes."),
    ("temps_median_s", "Temps de réponse médian, en secondes."),
    ("reponses_critiques", "Réponses critiques choisies pendant le passage."),
    ("statut", "termine ou en_cours."),
    ("debut", "Début du passage."),
    ("fin", "Fin du passage (vide s'il est en cours)."),
    QUALITY,
    CHANCE,
    ("taux_meilleure_reponse", "Part des choix où la meilleure réponse a été choisie, en % "
                               "(cotation dichotomique, calculée à côté de la qualité ; environ 20 % au hasard)."),
    ("scenes", "Scènes notées (1ʳᵉ tentative de chaque scène dans le passage)."),
    ("choix", "Choix notés."),
    *_skills(SKILL_100),
    ("etats_depart", "États narratifs au début du passage."),
]

SESSION_COLUMNS = [
    SESSION_ID,
    PARTICIPANT,
    NAME,
    BOOK,
    ("livre_titre", "Titre du livre."),
    SESSION_NO,
    ("statut", "terminee ou en_cours."),
    ("debut", "Début de la session."),
    ("fin", "Fin de la session (vide si elle est en cours)."),
    ("derniere_activite", "Dernière scène jouée ou dernier chapitre terminé."),
    ("chapitres_termines", "Chapitres terminés dans la session."),
    ("chapitres_total", "Chapitres du livre."),
    ("scenes_notees", "Scènes notées dans le bilan (dernier passage de chaque chapitre)."),
    RESULTS,
    ("note_globale", "Qualité des choix de la session, sur 100."),
    CHANCE,
    *_skills(SKILL_100),
    ("note_v1", "Ancienne note (scoring v1, bornes de chemin) pour les sessions terminées avant le v2."),
    ("etats_narratifs", "États posés par les choix, qui suivent l'histoire d'un chapitre à l'autre."),
]

CHAPTER_COLUMNS = [
    SESSION_ID,
    PARTICIPANT,
    BOOK,
    SESSION_NO,
    RESULTS,
    CHAPTER_ID,
    CHAPTER,
    ("scenes_notees", "Scènes du chapitre notées dans le bilan de la session."),
    ("note_chapitre", "Qualité des choix dans le chapitre, sur 100."),
    *_skills(SKILL_100),
]

# Colonnes communes aux scènes et aux choix.
ATTEMPT_COLUMNS = [
    ("tentative_id", "Identifiant de la scène jouée : relie une scène à ses choix."),
    PASSAGE_ID,
    SESSION_ID,
    PARTICIPANT,
    BOOK,
    SESSION_NO,
    CHAPTER_ID,
    ("scene_id", "Numéro de la scène dans le chapitre."),
    ("scene", "Titre de la scène."),
    ("tentative_no", "1 = première fois que la scène est jouée dans le passage, 2 = rejouée, etc."),
    ("notee", "1 si la tentative est notée (passage compté et 1ʳᵉ tentative de la scène), sinon 0."),
    ("date", "Fin de la scène."),
]

SCENE_COLUMNS = ATTEMPT_COLUMNS + [
    ("point_entree", "Interaction par laquelle la scène a commencé (dépend des choix précédents)."),
    ("nb_choix", "Choix faits dans la scène."),
    QUALITY,
    *_skills("{skill}, qualité des choix dans la scène, sur 100 (sans seuil de nombre de choix)."),
    *_skills("{skill} : points obtenus dans la scène.", "_points"),
    *_skills("{skill} : Σ (points choisis − pire réponse proposée).", "_gain"),
    *_skills("{skill} : Σ (meilleure − pire réponse proposée) ; qualité = gain / écart.", "_ecart"),
]

CHOICE_COLUMNS = ATTEMPT_COLUMNS + [
    ("etape", "Rang du choix dans la scène (1, 2, 3…)."),
    ("interaction_id", "Identifiant de l'interaction dans la scène."),
    ("personnage", "Personnage qui parle."),
    ("replique", f"Texte de l'interaction ({TEXT_MAX} caractères au plus)."),
    ("nb_options", "Réponses proposées."),
    ("reponse_no", "Réponse choisie : rang dans la liste du livre (le joueur les voit mélangées)."),
    ("reponse", "Texte de la réponse choisie."),
    *_skills("{skill} : points de la réponse choisie (−3 à +3)."),
    ("total", "Somme des points de la réponse choisie."),
    ("pire_total", "Total de la pire réponse proposée à cette étape."),
    ("meilleure_reponse_no", "Réponse au meilleur total à cette étape (rang dans le livre)."),
    ("meilleure_reponse", "Texte de cette meilleure réponse."),
    ("meilleur_total", "Total de cette meilleure réponse."),
    ("ecart", "meilleur_total − total : 0 = meilleur choix possible à cette étape."),
    ("qualite", "Qualité du choix : (total − pire_total) / (meilleur_total − pire_total) × 100."),
    ("critique", "1 si la réponse choisie est marquée critique dans la clé du livre (champ Critical)."),
    ("critique_provisoire", "1 si elle est critique dans la clé, ou vaut −7 ou moins au total "
                            "(repère provisoire en attendant le panel d'experts)."),
    ("temps_s", "Temps de réponse en secondes, depuis l'affichage des réponses (vide avant le 13.10.2026)."),
    ("justification", "Justification de la réponse choisie dans la clé du livre (champ Rationale) ; "
                      "vide si la clé n'en donne pas, ou pour un choix enregistré avant le 13.10.2026."),
]

def _remarks(spacing_days: int) -> list[str]:
    return [
        "Scoring v2 : chaque choix est comparé aux réponses proposées au même moment. Qualité "
        "des choix = Σ (choisi − pire) / Σ (meilleur − pire) × 100 : 100 = la meilleure réponse à "
        "chaque fois, 0 = la pire, environ 50 au hasard. Un choix décisif pèse plus qu'un choix anodin.",
        f"Une compétence n'est notée que si au moins {MIN_SKILL_EVIDENCE} choix la mettent en jeu "
        "(sinon : vide).",
        "L'unité de note est le passage de chapitre. Un passage compte s'il est le premier du "
        f"chapitre, ou s'il commence au moins {spacing_days} jour(s) après la fin du précédent "
        "passage compté (sinon : entraînement). Dans un passage, seule la 1ʳᵉ tentative d'une "
        "scène est notée.",
        "Niveau d'un chapitre = moyenne pondérée de ses passages comptés (le n-ième pèse "
        "1 + 0,25 × (n − 1)) ; note du livre = moyenne des niveaux des chapitres évalués.",
        "Chaque réponse vaut de −3 à +3 points sur chacune des sept compétences (clé de cotation "
        "provisoire, en attente de validation par un panel d'experts).",
        "Textes et points des choix sont figés au moment du jeu : modifier un livre ensuite ne "
        "change pas l'historique.",
    ]


def _timezone() -> str:
    return os.getenv("APP_TIMEZONE", "Europe/Zurich")


def _local(value: datetime | None) -> datetime | None:
    """Heure locale, comme le filtre `date_fr` des pages."""
    if value is None:
        return None
    return as_utc(value).astimezone(ZoneInfo(_timezone()))


def _book_title(slug: str) -> str:
    try:
        return get_book(slug)["title"]
    except ValueError:  # livre retiré ou renommé depuis
        return slug


def participant_code(user: User, pseudonymize: bool) -> str:
    """Identifiant exporté ; le code pseudonyme reste le même d'un export à l'autre."""
    return f"P{user.id:03d}" if pseudonymize else user.username


def _skill_values(scores: dict[str, Any] | None, suffix: str = "") -> dict[str, Any]:
    scores = scores or {}
    return {SKILL_COLUMNS[k] + suffix: scores.get(k) for k in SOFT_SKILLS}


def _chapter_names(chapters_by_book: dict[str, list[Chapter]]) -> dict[tuple[str, int], str]:
    return {(slug, ch.Id): ch.Name for slug, chs in chapters_by_book.items() for ch in chs}


def build_export(
    users: list[User],
    sessions: list[BookSession],
    passages: list[ChapterPassage],
    chapters_by_book: dict[str, list[Chapter]],
    *,
    book_slug: str | None = None,
    participant: User | None = None,
    pseudonymize: bool = False,
    spacing_days: int = 7,
    now: datetime | None = None,
    thresholds: dict[str, dict[int, Any]] | None = None,
) -> tuple[list[Table], dict[str, Any]]:
    """Tables et métadonnées de l'export.

    `users`, `sessions` et `passages` sont déjà filtrés ; `book_slug` et
    `participant` décrivent ce filtre dans les métadonnées.
    """
    people = {u.id: u for u in users} | {s.user_id: s.user for s in sessions}
    code = {uid: participant_code(u, pseudonymize) for uid, u in people.items()}
    names = _chapter_names(chapters_by_book)
    session_no = {s.id: s.number for s in sessions}

    by_user_sessions: dict[int, list[BookSession]] = {}
    for s in sessions:
        by_user_sessions.setdefault(s.user_id, []).append(s)
    by_user_passages: dict[int, list[ChapterPassage]] = {}
    for p in passages:
        by_user_passages.setdefault(p.user_id, []).append(p)

    participants = [
        {
            "participant": code[u.id],
            "nom": None if pseudonymize else u.display_name,
            "role": "formateur" if u.is_trainer else "participant",
            "inscription": _local(u.created_at),
            "derniere_connexion": _local(u.last_login_at),
            "passages_notes": sum(1 for p in by_user_passages.get(u.id, []) if p.is_completed and p.counted),
            "passages_entrainement": sum(
                1 for p in by_user_passages.get(u.id, []) if p.is_completed and not p.counted
            ),
            "sessions_terminees": sum(1 for s in by_user_sessions.get(u.id, []) if s.is_completed),
            "sessions_en_cours": sum(1 for s in by_user_sessions.get(u.id, []) if not s.is_completed),
        }
        for u in sorted(people.values(), key=lambda u: code[u.id])
    ]

    # --- Passages et niveaux -------------------------------------------------
    passage_rows: list[dict[str, Any]] = []
    level_rows: list[dict[str, Any]] = []
    passage_of: dict[int, ChapterPassage] = {}
    cohorts: dict[str, dict[int, float | None]] = {}
    groups: dict[tuple[int, str, int], list[ChapterPassage]] = {}
    for p in passages:
        groups.setdefault((p.user_id, p.book_slug, p.chapter_id), []).append(p)
    for (user_id, slug, chapter_id), group in sorted(
        groups.items(), key=lambda kv: (code.get(kv[0][0], ""), kv[0][1], kv[0][2])
    ):
        group.sort(key=lambda p: (as_utc(p.started_at), p.id))
        for rank, p in enumerate(group, start=1):
            for a in p.attempts:
                passage_of[a.id] = p
            res = p.results or {}
            passage_rows.append({
                "passage_id": p.id,
                "participant": code[user_id],
                "livre": slug,
                "chapitre_id": chapter_id,
                "chapitre": names.get((slug, chapter_id)),
                "session_id": p.session_id,
                "session_no": session_no.get(p.session_id),
                "passage_no": rank,
                "compte": p.counted,
                "trop_rapide": bool((res.get("timing") or {}).get("too_fast")),
                "choix_chronometres": (res.get("timing") or {}).get("n_timed"),
                "choix_rapides": (res.get("timing") or {}).get("n_fast"),
                "temps_median_s": round((res.get("timing") or {})["median_ms"] / 1000, 1)
                if (res.get("timing") or {}).get("median_ms") is not None else None,
                "reponses_critiques": res.get("n_critical"),
                "statut": "termine" if p.is_completed else "en_cours",
                "debut": _local(p.started_at),
                "fin": _local(p.completed_at),
                "qualite": res.get("global"),
                "qualite_corrigee_hasard": res.get("chance_corrected"),
                "taux_meilleure_reponse": res.get("best_rate")
                if "best_rate" in res
                else choice_quality([st for a in passage_attempt_dicts(p) for st in a["trace"] or []])["best_rate"],
                "scenes": res.get("n_scenes"),
                "choix": res.get("n_choices"),
                **_skill_values(res.get("scores")),
                "etats_depart": ", ".join(p.flags_in or []),
            })
        level = chapter_progress(
            group,
            cohorts.setdefault(slug, cohort_first_sds(passages, slug)).get(chapter_id),
            thresholds=((thresholds or {}).get(slug) or {}).get(chapter_id),
        )
        if level:
            level_rows.append({
                "participant": code[user_id],
                "livre": slug,
                "chapitre_id": chapter_id,
                "chapitre": names.get((slug, chapter_id)),
                "niveau": level["level"],
                "fourchette": level["margin"],
                "bande": (level.get("band") or {}).get("label"),
                "plafond_critique": level.get("critical_capped"),
                "gain_points": level.get("gain"),
                "marge_gain": level.get("gain_margin"),
                "progres": (level.get("progress") or {}).get("label"),
                "a_rafraichir": level.get("refresh"),
                "progression": level["progression"],
                "premier_passage": level["first"],
                "dernier_passage": level["last"],
                "passages_notes": level["n_passages"],
                "choix": level["n_choices"],
                **_skill_values(level["scores"]),
            })

    # --- Sessions, chapitres, scènes, choix ----------------------------------
    session_rows: list[dict[str, Any]] = []
    chapter_rows: list[dict[str, Any]] = []
    scene_rows: list[dict[str, Any]] = []
    choice_rows: list[dict[str, Any]] = []
    for bs in sorted(sessions, key=lambda s: (code[s.user_id], s.book_slug, s.number)):
        chapters = chapters_by_book.get(bs.book_slug, [])
        if bs.is_completed and bs.results:
            results, status = bs.results, "definitifs"
        elif chapters:
            results, status = results_from_passages(bs, chapters), "provisoires"
        else:  # livre retiré : rien pour recalculer
            results, status = {}, None
        ref = {
            "session_id": bs.id,
            "participant": code[bs.user_id],
            "livre": bs.book_slug,
            "session_no": bs.number,
        }
        session_rows.append({
            **ref,
            "nom": None if pseudonymize else bs.user.display_name,
            "livre_titre": _book_title(bs.book_slug),
            "statut": "terminee" if bs.is_completed else "en_cours",
            "debut": _local(bs.started_at),
            "fin": _local(bs.completed_at),
            "derniere_activite": _local(bs.updated_at),
            "chapitres_termines": len(bs.completed_chapters or []),
            "chapitres_total": len(chapters) or None,
            "scenes_notees": results.get("n_scenes"),
            "resultats": status,
            "note_globale": results.get("global"),
            "qualite_corrigee_hasard": results.get("chance_corrected"),
            **_skill_values(results.get("scores")),
            "note_v1": (results.get("v1") or {}).get("global"),
            "etats_narratifs": ", ".join(bs.flags or []),
        })

        for ch in results.get("chapters") or []:
            if not ch.get("n_scenes"):  # chapitre pas encore joué
                continue
            chapter_rows.append({
                **ref,
                "resultats": status,
                "chapitre_id": ch["id"],
                "chapitre": ch["name"],
                "scenes_notees": ch["n_scenes"],
                "note_chapitre": ch["global"],
                **_skill_values(ch["scores"]),
            })

        for a in bs.attempts:
            passage = passage_of.get(a.id)
            attempt = {
                **ref,
                "tentative_id": a.id,
                "passage_id": passage.id if passage else None,
                "chapitre_id": a.chapter_id,
                "scene_id": a.scene_id,
                "scene": a.scene_title,
                "tentative_no": a.attempt_no,
                "notee": a.counted,
                "date": _local(a.created_at),
            }
            q = choice_quality(a.trace or [])
            detail = q["detail"]
            scene_rows.append({
                **attempt,
                "point_entree": a.entry_id,
                "nb_choix": len(a.trace or []),
                "qualite": q["global"],
                **_skill_values(q["raw_scores"]),
                **_skill_values(a.raw, "_points"),
                **{SKILL_COLUMNS[k] + "_gain": detail[k]["gain"] for k in SOFT_SKILLS},
                **{SKILL_COLUMNS[k] + "_ecart": detail[k]["span"] for k in SOFT_SKILLS},
            })
            for step, st in enumerate(a.trace or [], start=1):
                choice, best = st["choice"], st["best"]
                worst = (st.get("total_bounds") or [None, None])[0]
                span = best["total"] - worst if worst is not None else 0
                choice_rows.append({
                    **attempt,
                    "etape": step,
                    "interaction_id": st.get("interaction_id"),
                    "personnage": st.get("actor"),
                    "replique": st.get("prompt"),
                    "nb_options": st.get("n_options"),
                    "reponse_no": choice["index"] + 1,
                    "reponse": choice.get("text"),
                    **_skill_values({k: (choice.get("scores") or {}).get(k, 0) for k in SOFT_SKILLS}),
                    "total": choice["total"],
                    "pire_total": worst,
                    "meilleure_reponse_no": best["index"] + 1,
                    "meilleure_reponse": best.get("text"),
                    "meilleur_total": best["total"],
                    "ecart": best["total"] - choice["total"],
                    "qualite": round(100 * (choice["total"] - worst) / span, 1) if span > 0 else None,
                    "critique": bool(choice.get("critical")),
                    "critique_provisoire": bool(choice.get("critical"))
                    or choice["total"] <= CRITICAL_PROVISIONAL_TOTAL,
                    "temps_s": round(st["time_ms"] / 1000, 1) if isinstance(st.get("time_ms"), (int, float)) else None,
                    "justification": choice.get("rationale") or "",
                })

    tables = [
        Table("participants", "Un compte par ligne.", PARTICIPANT_COLUMNS, participants),
        Table("niveaux", "Un chapitre évalué d'un participant par ligne.", LEVEL_COLUMNS, level_rows),
        Table("passages", "Une partie complète d'un chapitre par ligne (unité de note).",
              PASSAGE_COLUMNS, passage_rows),
        Table("sessions", "Un parcours de l'histoire d'un livre par ligne, avec son bilan.",
              SESSION_COLUMNS, session_rows),
        Table("chapitres", "Un chapitre dans le bilan d'une session par ligne.", CHAPTER_COLUMNS, chapter_rows),
        Table("scenes", "Une scène jouée (tentative) par ligne.", SCENE_COLUMNS, scene_rows),
        Table("choix", "Une réponse donnée par ligne.", CHOICE_COLUMNS, choice_rows),
    ]
    meta = {
        "application": "End of Life",
        "exporte_le": _local(now or datetime.now(timezone.utc)),
        "livre": _book_title(book_slug) if book_slug else "Tous les livres",
        "participant": participant_code(participant, pseudonymize) if participant else "Tous",
        "pseudonymise": pseudonymize,
        "fuseau_horaire": _timezone(),
        "delai_entre_passages_notes_jours": spacing_days,
        "remarques": _remarks(spacing_days),
    }
    return tables, meta
