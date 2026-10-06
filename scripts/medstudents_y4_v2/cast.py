"""Distribution du livre MedStudents Y4 v2 — l'entourage d'Alex au 3ᵉ étage.

Chaque personnage a une clé courte utilisée dans les scènes (`I(1, "moreau", ...)`).
Les images suivent la convention du projet : `<Base>.png` pour le portrait,
`<Base>_<émotion>.png` pour l'expression affichée à chaque interaction.
"""
from __future__ import annotations

from typing import Any

# clé -> (Id, Nom, Âge, Rôle, Histoire, base des images)
_CAST: dict[str, tuple[int, str, int | str, str, str, str]] = {
    # --- Narration (pas de portrait) --------------------------------------
    "narr": (0, "", "", "Narration", "", ""),

    # --- L'équipe du 3ᵉ étage ---------------------------------------------
    "moreau": (
        11, "Dr Moreau", 42, "Médecin-chef, service de médecine interne",
        "Médecin interniste depuis 15 ans, pédagogue reconnu·e. Dr Moreau encadre "
        "les étudiants en stage avec bienveillance mais exige rigueur et respect des "
        "règles déontologiques. Aime les questions pertinentes et valorise "
        "l'humilité professionnelle. Protège ses équipes sans jamais les couvrir.",
        "DrMoreau",
    ),
    "neuhaus": (
        60, "Dr Neuhaus", 31, "Médecin assistant, 3ᵉ année — médecine interne",
        "Samuel Neuhaus est brillant, drôle et épuisé. Il enchaîne les gardes pour "
        "boucler sa formation, protège les étudiants qu'il apprécie et coupe les "
        "virages quand il est débordé. Déteste être contredit devant l'équipe — et "
        "le sait.",
        "DrNeuhaus",
    ),
    "ines": (
        43, "Inès Rey", 36, "Infirmière référente, unité de médecine interne",
        "Douze ans de service. Connaît les patients mieux que les médecins de "
        "passage. Supporte mal qu'on annonce sans prévenir l'équipe soignante, "
        "parce que c'est elle qui reste dans la chambre après.",
        "InesRey",
    ),
    "kevin": (
        61, "Kevin Da Silva", 34, "Infirmier de nuit, unité de médecine interne",
        "Dix ans de nuits au 3ᵉ. Calme, fiable, père de deux enfants. Fait tourner "
        "le service la nuit avec une seule collègue pour vingt-quatre lits. Ne "
        "hausse jamais la voix, et c'est pour ça qu'on l'écoute.",
        "KevinDaSilva",
    ),
    "fatou": (
        62, "Fatou Diallo", 55, "ASSC (assistante en soins et santé communautaire)",
        "Trente ans d'hôpital. Connaît les familles par leur prénom et entend ce "
        "qu'elles ne disent pas aux médecins. Personne ne lui demande jamais son "
        "avis ; elle le donne quand même, à voix basse.",
        "FatouDiallo",
    ),
    "jonas": (
        63, "Jonas Meier", 24, "Étudiant en 1ʳᵉ année de Master, co-stagiaire d'Alex",
        "Même volée qu'Alex. Brillant aux examens, pratique l'humour noir comme "
        "une armure et compte les gestes techniques comme des trophées. Plus "
        "fragile qu'il ne le montre.",
        "JonasMeier",
    ),
    "keller": (
        42, "Dre Keller", 51, "Oncologue, consultante du service",
        "Oncologue expérimentée, directe, parfois perçue comme brusque. Considère "
        "que l'information due au patient n'est pas négociable, mais que le rythme "
        "de sa délivrance l'est.",
        "DreKeller",
    ),
    "mathilde": (
        64, "Mathilde Favre", 47, "Infirmière spécialisée, équipe mobile de soins palliatifs",
        "Vingt ans de soins palliatifs. Sait nommer la mort sans la brandir, et "
        "rappeler aux équipes qu'un patient qui arrête un traitement n'arrête pas "
        "d'être soigné.",
        "MathildeFavre",
    ),
    "imhof": (
        73, "Dre Imhof", 39, "Cheffe de clinique, équipe de réanimation",
        "Dirige l'équipe d'urgence intra-hospitalière. Parle peu et fort pendant "
        "une réanimation, beaucoup et doucement après.",
        "DreImhof",
    ),
    "perrin": (
        65, "Nathalie Perrin", 50, "Responsable sécurité des patients",
        "Ancienne infirmière aux soins intensifs, formée à l'analyse des "
        "incidents. Défend une culture juste : chercher ce qui, dans le système, "
        "a rendu l'erreur possible, sans excuser les manquements.",
        "NathaliePerrin",
    ),
    "rochat": (
        66, "M. Rochat", 58, "Juriste de l'hôpital",
        "Pierre-Alain Rochat a traité trente ans de dossiers de responsabilité. "
        "Parle lentement, choisit chaque mot, et rappelle que la vérité est "
        "toujours la meilleure défense.",
        "PierreAlainRochat",
    ),
    "dufaux": (
        67, "Me Dufaux", 46, "Avocate de la famille Jaquier",
        "Claire Dufaux défend des patients et des familles depuis quinze ans. "
        "Précise, pas cruelle. Veut les faits, heure par heure, et repère "
        "immédiatement une réponse préparée.",
        "ClaireDufaux",
    ),

    # --- M. Ferreira et sa famille (ch. 1 et 4) ----------------------------
    "ferreira": (
        41, "M. Ferreira", 58, "Patient, chambre 312 — adénocarcinome pulmonaire",
        "António Ferreira, carreleur, arrivé du Portugal à 20 ans, veuf depuis "
        "quatre ans, deux filles adultes et une petite-fille. Homme pudique, "
        "habitué à ne pas se plaindre. Sa cadette se marie en septembre.",
        "MFerreira",
    ),
    "carla": (
        49, "Carla Ferreira", 31, "Fille aînée de M. Ferreira, mère de Lina",
        "Assistante de direction, organisée, en surcharge. Gère les papiers de son "
        "père depuis le décès de sa mère. Élève seule sa fille Lina. Traduit "
        "parfois pour son père alors qu'il comprend très bien le français.",
        "CarlaFerreira",
    ),
    "joana": (
        68, "Joana Ferreira", 27, "Fille cadette de M. Ferreira",
        "Infirmière en EMS, la « petite » de la famille. Se marie en septembre "
        "avec Tiago. Pleure facilement et ne cède jamais sur l'essentiel.",
        "JoanaFerreira",
    ),
    "lina": (
        47, "Lina", 9, "Petite-fille de M. Ferreira, fille de Carla",
        "Neuf ans, vive et observatrice. Appelle son grand-père « Vovô ». Comprend "
        "qu'on lui cache quelque chose et pose des questions directes aux adultes.",
        "Lina",
    ),

    # --- Mme Haddad et sa fille (ch. 2 et 6) ------------------------------
    "haddad": (
        44, "Mme Haddad", 74, "Patiente, chambre 308 — masse pancréatique",
        "Ancienne institutrice, veuve, lucide et curieuse. Hospitalisée pour un "
        "ictère. L'imagerie montre une masse pancréatique très probablement "
        "maligne. Sa fille a demandé qu'on ne lui dise rien.",
        "MmeHaddad",
    ),
    "sofia": (
        45, "Sofia Haddad", 45, "Fille de Mme Haddad",
        "Vit à vingt minutes de l'hôpital, présente tous les jours. A perdu son "
        "père d'un cancer annoncé brutalement il y a six ans et en garde un "
        "souvenir traumatique. Veut protéger sa mère à tout prix.",
        "SofiaHaddad",
    ),

    # --- Policlinique (ch. 3) ---------------------------------------------
    "yann": (
        46, "Yann Dubois", 26, "Patient, policlinique de médecine interne",
        "Développeur, sportif, jamais malade. Consulte pour des céphalées et des "
        "paresthésies intermittentes depuis trois mois. Bilan et IRM non "
        "concluants. A beaucoup lu sur internet et attend une réponse.",
        "YannDubois",
    ),
    "malick": (
        50, "Malick Sow", 31, "Patient, policlinique de médecine interne",
        "Éducateur en foyer, en couple depuis deux ans avec Chloé. Est venu pour "
        "un bilan de routine incluant un dépistage qu'il a demandé lui-même. Le "
        "test de dépistage VIH est revenu réactif ; la confirmation est en cours.",
        "MalickSow",
    ),
    "chloe": (
        69, "Chloé Martin", 29, "Compagne de Malick Sow",
        "Graphiste, directe, peu patiente avec les détours. Aime Malick et "
        "supporte mal d'être tenue à l'écart.",
        "ChloeMartin",
    ),

    # --- La famille Jaquier (ch. 5 et 6) ----------------------------------
    "roland": (
        70, "M. Jaquier", 71, "Patient, chambre 304 — pneumonie communautaire",
        "Roland Jaquier, aiguilleur CFF à la retraite, fibrillation auriculaire "
        "sous bêtabloquant. Minimise tout, par principe. À quarante ans, une "
        "injection de pénicilline l'a fait « gonfler » et passer une nuit en "
        "observation ; il n'en parle jamais.",
        "RolandJaquier",
    ),
    "monique": (
        71, "Monique Jaquier", 69, "Épouse de M. Jaquier",
        "Mariée à Roland depuis quarante-six ans. Tient le calendrier des "
        "médicaments, les rendez-vous et la mémoire du couple. Se tait quand son "
        "mari parle — pas quand ça compte.",
        "MoniqueJaquier",
    ),
    "olivier": (
        72, "Olivier Jaquier", 43, "Fils de M. et Mme Jaquier",
        "Ingénieur, méthodique, habitué à ce que les problèmes aient une cause et "
        "un responsable. Aime son père plus qu'il ne sait le dire.",
        "OlivierJaquier",
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


def portrait_image(key: str) -> str:
    base = _CAST[key][5]
    return f"{base}.png" if base else ""


def display_name(key: str) -> str:
    return _CAST[key][1] or "Narration"
