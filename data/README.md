# Dossier data

- **chapters/** — Fichiers JSON des livres (`chapter.json`, `MedStudents_Y2_v2.json`, `MedStudents_Y4_v2.json`). `MedStudents_Y2_v2.json` est généré par `scripts/build_medstudents_y2_v2.py` à partir de `scripts/medstudents_y2_v2/` ; `MedStudents_Y2_v1.json` est l'ancienne version, conservée pour référence. `MedStudents_Y4_v2.json` est généré par `scripts/build_medstudents_y4_v2.py` à partir de `scripts/medstudents_y4_v2/` ; `MedStudents_Y4_v1.json` est l'ancienne version, conservée pour référence. Archives dans `history/` : `chapter_<YY-MM-DD>.json`.
- **keys/** — Clés de cotation appliquées par-dessus les scores des sources au build. `MedStudents_Y2_v2_cle.json` : cotes, drapeau critique et justification de chaque réponse des points de choix du livre 2, cotées par Claude en deux tours (méthode et limites : `docs/MedStudents_Y2_v2_cle.md`).
- **images/** — Illustrations des personnages (Agathe_*, Claude_*, Pascal_*) pour le parcours joueur.
