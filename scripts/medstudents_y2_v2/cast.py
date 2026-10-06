"""Distribution du livre MedStudents Y2 v2 « Le corps donné ».

Chaque personnage a une clé courte utilisée dans les scènes (`I(1, "jeannine", ...)`).
Les images suivent la convention du projet : `<Base>.png` pour le portrait,
`<Base>_<émotion>.png` pour l'expression affichée à chaque interaction.
Alex, le joueur ou la joueuse, n'apparaît jamais à l'écran.
"""
from __future__ import annotations

from typing import Any

# clé -> (Id, Nom, Âge, Rôle, Histoire, base des images)
_CAST: dict[str, tuple[int, str, int | str, str, str, str]] = {
    # --- Narration (pas de portrait) --------------------------------------
    "narr": (0, "", "", "Narration", "", ""),

    # --- Montchéry : Jeannine et les siens ---------------------------------
    "jeannine": (
        101, "Jeannine Pittet", 81, "Patiente du cabinet de Montchéry, ancienne sage-femme",
        "Huitante et un ans, veuve depuis l'accident de tracteur de son mari en 1998. A mis "
        "au monde six cents enfants dans la région. Insuffisance cardiaque, diabète, reins "
        "fatigués. Drôle, têtue, lucide. A signé son don du corps à la faculté il y a deux "
        "ans et ne l'a dit qu'à sa médecin.",
        "JeanninePittet",
    ),
    "daniel": (
        102, "Daniel Pittet", 54, "Fils de Jeannine, agriculteur aux Combettes",
        "A repris la ferme à vingt-huit ans, le jour où il a trouvé son père sous le "
        "tracteur. Passe matin et soir pour les bêtes et pour sa mère. Aimant, débordé, en "
        "colère contre tout ce qui ressemble à une perte de contrôle.",
        "DanielPittet",
    ),
    "oceane": (
        103, "Océane Pittet", 17, "Petite-fille de Jeannine, apprentie fleuriste",
        "Fille de Daniel. Passe plus de temps chez sa grand-mère que chez son père. Cash, "
        "drôle, protège Jeannine comme une louve.",
        "OceanePittet",
    ),
    "jeanpaul": (
        104, "Jean-Paul Pittet", 58, "Cousin de Daniel, habitant de Montchéry",
        "Même nom, même village, même cabinet médical. Brouillé avec Jeannine depuis une "
        "histoire d'héritage en 1987. Le plus rapide du Café de la Gare quand il s'agit de "
        "raconter.",
        "JeanPaulPittet",
    ),

    # --- Le cabinet de Montchéry et le réseau de soins ---------------------
    "golay": (
        105, "Dre Golay", 56, "Médecin de famille à Montchéry",
        "Isabelle Golay soigne trois générations du village depuis vingt-cinq ans, visites à "
        "domicile comprises. Pas de successeur en vue. Accueille des étudiant·e·s parce "
        "qu'elle espère encore qu'un·e reviendra.",
        "DreGolay",
    ),
    "sandra": (
        106, "Sandra Nicolet", 38, "Assistante médicale au cabinet de Montchéry",
        "Tient l'agenda, le laboratoire, le téléphone et le moral du cabinet. Connaît chaque "
        "patient par son prénom et par sa date de naissance. Élève seule un fils de douze ans.",
        "SandraNicolet",
    ),
    "thierry": (
        107, "Thierry Bovet", 45, "Infirmier du CMS (soins à domicile)",
        "Vingt ans de soins à domicile dans la région. Passe chez Jeannine trois fois par "
        "semaine. Connaît l'état du frigo, le niveau du pilulier et l'humeur de la maison "
        "avant d'avoir ouvert la porte.",
        "ThierryBovet",
    ),
    "laura": (
        108, "Laura Steiner", 29, "Physiothérapeute",
        "Physio indépendante, entre visites à domicile et centre de réadaptation. Parle aux "
        "patients en marchant à côté d'eux.",
        "LauraSteiner",
    ),

    # --- La faculté ---------------------------------------------------------
    "vautier": (
        109, "Pre Vautier", 58, "Professeure d'anatomie, responsable des travaux de dissection",
        "Hélène Vautier dirige les travaux de dissection et le programme de don du corps. "
        "Sévère sur la dignité des donneuses et des donneurs, d'une patience infinie avec "
        "celles et ceux qui ont peur. Organise chaque année la cérémonie d'hommage.",
        "PreVautier",
    ),
    "chevalley": (
        110, "Dre Chevalley", 47, "Responsable du centre de simulation",
        "Anne-Laure Chevalley forme aux gestes d'urgence et à l'anamnèse avec des patients "
        "standardisés. Débriefe sans humilier, et n'oublie jamais qu'une simulation peut "
        "cacher une vraie urgence.",
        "DreChevalley",
    ),
    "bernard": (
        111, "Bernard Gilliéron", 66, "Patient standardisé, ancien comédien",
        "Trente ans de théâtre, dix ans de patients simulés. Joue les malades avec une "
        "précision redoutable et donne des retours cruels et justes. Hypertendu, et ne le "
        "dit à personne.",
        "BernardGillieron",
    ),
    "odile": (
        112, "Odile Gilliéron", 64, "Épouse de Bernard",
        "Costumière à la retraite. Connaît par cœur toutes les répliques de son mari.",
        "OdileGillieron",
    ),
    "ibarra": (
        113, "Dr Ibarra", 34, "Tuteur d'APP, médecin assistant en pédiatrie",
        "Tomás Ibarra anime le tutorat du jeudi. Laisse le groupe se débrouiller, ne dit "
        "presque rien, et voit tout.",
        "DrIbarra",
    ),

    # --- La table 14 --------------------------------------------------------
    "noah": (
        114, "Noah Berthoud", 20, "Camarade de volée, table 14",
        "Brillant, anxieux, fils d'un chirurgien qui compare tout. Ne dort plus beaucoup "
        "depuis la rentrée.",
        "NoahBerthoud",
    ),
    "maelle": (
        115, "Maëlle Dupasquier", 21, "Camarade de volée, table 14",
        "Drôle, rapide, mille huit cents abonnés. Poste tout, parce qu'une blague, ça ne "
        "fait pas peur.",
        "MaelleDupasquier",
    ),
    "yasmine": (
        116, "Yasmine Benkirane", 27, "Camarade de volée, table 14 — ancienne ambulancière",
        "Six ans d'ambulance avant la médecine. Connaît le terrain mieux que les assistants, "
        "corrige tout le monde, et ne parle jamais de la nuit qui l'a fait changer de métier.",
        "YasmineBenkirane",
    ),
    "leo": (
        117, "Léo Studer", 19, "Camarade de volée, table 14 — transféré de Zurich",
        "A fait sa première année à Zurich. Bilingue, timide, se perd dans le français "
        "médical et dans les codes de la volée. Voit ce que les autres ne voient pas.",
        "LeoStuder",
    ),

    # --- La famille d'Alex ----------------------------------------------------
    "philippe": (
        118, "Philippe", 54, "Père d'Alex",
        "Chef de chantier, fumeur, hypertendu, « jamais malade ». Fier de son enfant en "
        "médecine, et incapable de le lui dire.",
        "PhilippePapa",
    ),
    "nadia": (
        119, "Nadia", 52, "Mère d'Alex",
        "Enseignante de français. S'inquiète pour tout le monde, et croit que son enfant "
        "sait déjà tout.",
        "NadiaMaman",
    ),

    # --- Patient·e·s et proches de passage -----------------------------------
    "duc": (
        121, "Coralie Duc", 29, "Patiente du cabinet, mère d'Elio (2 mois)",
        "Vendeuse, maman pour la première fois. A beaucoup lu sur internet. Son neveu, "
        "autiste, a cessé de parler à quinze mois, et personne ne lui a jamais expliqué "
        "pourquoi.",
        "CoralieDuc",
    ),

    "ammann": (
        122, "Dre Ammann", 41, "Cardiologue, soins intensifs de cardiologie",
        "Des cernes de garde, une voix lente. Explique les artères avec les mains. A besoin "
        "de l'heure exacte du début des douleurs, et le dit sans jamais accuser.",
        "DreAmmann",
    ),
    "chappuis": (
        123, "M. Chappuis", 62, "Pharmacien de Montchéry",
        "Pharmacien du village depuis trente ans. Répète chaque ligne d'ordonnance à voix "
        "haute et ne délivre jamais rien sur un « je crois ».",
        "MChappuis",
    ),

    "lambelet": (
        124, "Pr Lambelet", 61, "Responsable de l'identité professionnelle, commission d'intégrité",
        "Marc Lambelet préside la commission qui traite les plagiats et les fausses "
        "déclarations. Lit tout, ne hausse jamais le ton, et a vu beaucoup d'étudiants ne "
        "pas dormir.",
        "PrLambelet",
    ),

    "aline": (
        125, "Aline Morel", 44, "Diététicienne du CMS",
        "Ne parle jamais de calories. Demande ce qu'on aimait manger enfant, ce qui passe "
        "encore, et avec qui on mange.",
        "AlineMorel",
    ),

    "buhler": (
        126, "Véronique Bühler", 52, "Infirmière, équipe mobile de soins palliatifs",
        "Vingt ans de soins palliatifs à domicile. Prépare les réserves de morphine et de "
        "midazolam, parle bas, et dit aux familles ce qu'elles ont le droit de faire : "
        "rester, partir, revenir.",
        "VeroniqueBuhler",
    ),

    # --- Madame 14 ------------------------------------------------------------
    "rapin": (
        120, "Mme Rapin", 55, "Fille de la donneuse de la table 14",
        "Françoise Rapin a mis du vernis rouge aux ongles de sa mère la veille de sa mort. "
        "Elle a respecté son choix de donner son corps, et son anonymat.",
        "MmeRapin",
    ),
}

CAST_KEYS = frozenset(_CAST)


def actor_dict(key: str) -> dict[str, Any]:
    """Actor au format JSON du livre."""
    aid, name, age, role, history, base = _CAST[key]
    return {
        "Id": aid,
        "Name": name,
        "Age": age,
        "Role": role,
        "History": history,
        "ImageName": f"{base}.png" if base else "",
    }


def expression_image(key: str, expr: str) -> str:
    """Nom du fichier d'expression (vide pour la narration)."""
    base = _CAST[key][5]
    if not base or not expr:
        return ""
    return f"{base}_{expr}.png"


def display_name(key: str) -> str:
    return _CAST[key][1] or "Narration"
