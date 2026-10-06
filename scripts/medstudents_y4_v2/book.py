"""Assemblage du livre MedStudents Y4 v2."""
from __future__ import annotations

from .ch1 import CH1
from .ch2 import CH2
from .ch3 import CH3
from .ch4 import CH4
from .ch5 import CH5
from .ch6 import CH6

CHAPTERS = [CH1, CH2, CH3, CH4, CH5, CH6]

# États mutuellement exclusifs qui séparent des voies de scènes (slots).
MUTEX: list[tuple[str, ...]] = [("erreur", "evite")]
