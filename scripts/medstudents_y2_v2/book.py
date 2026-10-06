"""Assemblage du livre MedStudents Y2 v2 « Le corps donné »."""
from __future__ import annotations

from .ch1 import CH1
from .ch2 import CH2
from .ch3 import CH3
from .ch4 import CH4
from .ch5 import CH5
from .ch6 import CH6

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]

# États mutuellement exclusifs : une combinaison qui en contient deux d'un même
# groupe ne peut pas se produire (utilisé pour valider les emplacements de scènes).
MUTEX: list[tuple[str, ...]] = [
    ("photo_virale", "photo_supprimee"),
    ("erreur_homonyme", "bon_pittet", "appel_rattrape"),
    ("aveu_homonyme", "esquive_homonyme"),
    ("papa_144", "papa_rassure"),
    ("bernard_rapide", "bernard_retard"),
    ("mensonge_portfolio", "verite_portfolio"),
    ("noah_aide", "noah_seul"),
    ("famille_apaisee", "famille_dechiree"),
    ("oceane_orientee", "oceane_trahie", "oceane_seule"),
    ("examen_quitte", "examen_fini"),
]

# Issues obligatoires : chaque parcours complet de la scène pose exactement un
# état de chaque groupe. Clé : titre de la scène.
OUTCOMES: dict[str, list[tuple[str, ...]]] = {
    "1.2 La story": [("photo_virale", "photo_supprimee")],
    "2.2 Le téléphone": [("erreur_homonyme", "bon_pittet", "appel_rattrape")],
    "2.4 Le Café de la Gare": [("aveu_homonyme", "esquive_homonyme")],
    "3.2 Le repas de Noël": [("papa_144", "papa_rassure")],
    "4.2 Hors script": [("bernard_rapide", "bernard_retard")],
    "4.3 Le portfolio": [("mensonge_portfolio", "verite_portfolio")],
    "4.4 1 h 07": [("noah_aide", "noah_seul")],
    "5.2 La table de la cuisine": [("famille_apaisee", "famille_dechiree")],
    "5.3 La grange": [("oceane_orientee", "oceane_trahie", "oceane_seule")],
    "6.1 L'examen": [("examen_quitte", "examen_fini")],
}
