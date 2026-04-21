#!/usr/bin/env python3
"""
End of Life - graph_viewer.py
Génère des pages HTML par chapitre avec vis-network.
Mode édition : modification Text, Name, SceneIntroduction, scores.
Mode parcours joueur : parcours interactif, chemin en vert, scores finaux.
"""
import json
import os
import re

from graph_builder import load_chapters, build_scene_graph

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(BASE_DIR, "data", "chapters")
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "graphes")

# Liste centrale des livres disponibles. Chaque livre est généré dans son
# propre sous-dossier pour éviter toute collision de noms de chapitres.
BOOKS = [
    {
        "slug": "end_of_life",
        "title": "End of Life",
        "subtitle": "Communication en fin de vie — EMS",
        "description": (
            "Le livre historique du projet. Le joueur incarne Claude, "
            "infirmier·ère en EMS, confronté·e à des situations de fin de "
            "vie : rencontre, deuil, représentations collectives, "
            "accompagnement des proches. Destiné aux professionnel·le·s "
            "soignant·e·s en formation continue."
        ),
        "audience": "Soignant·e·s en formation continue",
        "json": "Chapters_v3-4-c_emotional-illustration.json",
    },
    {
        "slug": "medstudents_y2",
        "title": "MedStudents Y2",
        "subtitle": "Scénarios pédagogiques — 2ᵉ année de médecine",
        "description": (
            "Un livre conçu pour les étudiant·e·s en 2ᵉ année de médecine. "
            "Le joueur incarne Alex, en stage d'immersion hospitalière, et "
            "travaille les compétences communicationnelles et éthiques "
            "fondamentales du cursus pré-clinique (anamnèse, consentement, "
            "secret médical)."
        ),
        "audience": "Étudiant·e·s en 2ᵉ année de médecine",
        "json": "MedStudents_Y2_v1.json",
    },
]


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def _html_escape(s: str) -> str:
    if not s:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    ).replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")


def render_html(
    chapter: dict,
    scenes_data: list,
    chapter_links: list,
    current_filename: str,
    book: dict,
) -> str:
    """Génère le HTML complet pour un chapitre."""
    chapter_id = chapter["Id"]
    chapter_name = chapter.get("Name", "")
    book_slug = book["slug"]
    book_title = book["title"]
    book_json = book["json"]

    scenes_json = json.dumps(scenes_data, ensure_ascii=False)
    chapters_json = json.dumps({"Chapters": [chapter]}, ensure_ascii=False)

    sidebar_buttons = ""
    for i, sd in enumerate(scenes_data):
        title = _html_escape(sd.get("title", ""))
        sidebar_buttons += f'<button class="scene-btn" data-idx="{i}">{title}</button>\n'

    chapter_options = ""
    for item in chapter_links:
        selected = " selected" if item["filename"] == current_filename else ""
        chapter_options += (
            f'<option value="{_html_escape(item["filename"])}"{selected}>'
            f'Chapitre {item["id"]} — {_html_escape(item["name"])}</option>'
        )

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>End of Life — Chapitre {chapter_id} : {_html_escape(chapter_name)}</title>
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: system-ui, -apple-system, sans-serif; background: #0f0f14; color: #e4e4e7; display: flex; height: 100vh; overflow: hidden; -webkit-font-smoothing: antialiased; }}
#network {{ -webkit-font-smoothing: antialiased; }}
.sidebar {{ width: 320px; background: #18181b; padding: 14px; border-right: 1px solid #27272a; display: flex; flex-direction: column; }}
.sidebar h3 {{ margin: 0 0 10px; font-size: 11px; color: #71717a; text-transform: uppercase; letter-spacing: 0.05em; }}
.home-link {{ display: inline-block; text-decoration: none; color: #a1a1aa; font-size: 12px; margin-bottom: 8px; padding: 4px 8px; border: 1px solid #3f3f46; border-radius: 6px; }}
.home-link:hover {{ color: #fff; border-color: #38bdf8; background: #1e293b; }}
.book-badge {{ display: inline-block; background: linear-gradient(90deg,#38bdf8,#a855f7); color: #0f0f14; padding: 4px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; letter-spacing: 0.02em; margin: 0 0 14px 8px; vertical-align: middle; }}
.sidebar-top {{ flex: 1; min-height: 0; overflow-y: auto; }}
.sidebar-actions {{ border-top: 1px solid #27272a; margin-top: 10px; padding-top: 10px; }}
.chapter-select {{ width: 100%; padding: 8px 10px; margin-bottom: 12px; background: #27272a; border: 1px solid #3f3f46; border-radius: 6px; color: #fff; font-size: 12px; }}
.search {{ width: 100%; padding: 8px 10px; margin-bottom: 10px; background: #27272a; border: 1px solid #3f3f46; border-radius: 6px; color: #fff; font-size: 12px; }}
.search::placeholder {{ color: #71717a; }}
.scene-btn {{ display: block; width: 100%; background: transparent; color: #d4d4d8; border: none; padding: 9px 12px; margin-bottom: 2px; cursor: pointer; text-align: left; border-radius: 6px; font-size: 13px; }}
.scene-btn:hover {{ background: #27272a; color: #fff; }}
.scene-btn.active {{ background: #3f3f46; color: #38bdf8; font-weight: 500; }}
.sidebar.hidden-panel {{ display: none; }}
.main {{ flex: 1; position: relative; min-width: 0; min-height: 0; }}
#network {{ position: absolute; top: 0; left: 0; right: 0; bottom: 40px; width: 100%; background: #0f0f14; min-height: 350px; }}
.hint {{ position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); color: #52525b; font-size: 11px; }}
.panel-toggles {{ position: absolute; top: 10px; left: 10px; right: 10px; display: flex; justify-content: space-between; z-index: 5; pointer-events: none; }}
.panel-toggle-btn {{ pointer-events: auto; border: 1px solid #3f3f46; background: rgba(24,24,27,0.9); color: #d4d4d8; border-radius: 8px; padding: 6px 10px; font-size: 12px; cursor: pointer; }}
.panel-toggle-btn:hover {{ color: #fff; border-color: #38bdf8; }}
.editor {{ width: 640px; background: #18181b; padding: 14px; border-left: 1px solid #27272a; overflow-y: auto; }}
.editor.hidden-panel {{ display: none; }}
.editor h3 {{ margin: 0 0 10px; font-size: 13px; color: #38bdf8; }}
.scene-intro {{ margin-bottom: 14px; }}
.scene-intro label {{ display: block; font-size: 10px; color: #71717a; margin-bottom: 4px; }}
.scene-intro textarea {{ width: 100%; padding: 10px; font-size: 14px; font-weight: 500; background: #27272a; color: #f9fafb; border: 1px solid #4b5563; border-radius: 8px; resize: vertical; }}
.block {{ margin-bottom: 18px; padding: 16px; background: #27272a; border-radius: 10px; border: 1px solid #3f3f46; }}
.block.active {{ border-color: #38bdf8; box-shadow: 0 0 0 1px #38bdf8 inset; }}
.block .header {{ margin-bottom: 8px; font-weight: 600; color: #38bdf8; font-size: 12px; }}
.block label {{ display: block; font-size: 10px; color: #71717a; margin: 6px 0 3px; }}
.block textarea {{ width: 100%; padding: 9px; font-size: 14px; font-weight: 500; background: #18181b; color: #f9fafb; border: 1px solid #4b5563; border-radius: 8px; resize: vertical; }}
.resp {{ margin: 10px 0; padding-left: 10px; border-left: 2px solid #3f3f46; }}
.scores {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 12px; row-gap: 8px; margin-top: 8px; }}
.scores .score-item {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; column-gap: 5px; }}
.scores .score-item input.score {{ display: none; }}
.scores .score-item label {{ font-size: 10px; color: #e5e7eb; margin: 0; white-space: nowrap; }}
.score-stepper {{ display: inline-flex; align-items: center; gap: 2px; justify-self: start; }}
.score-btn {{ width: 20px; height: 20px; border: 1px solid #4b5563; background: #18181b; color: #e5e7eb; border-radius: 6px; cursor: pointer; font-size: 12px; line-height: 1; padding: 0; }}
.score-btn:hover {{ border-color: #38bdf8; color: #38bdf8; }}
.score-value {{ min-width: 14px; text-align: center; font-size: 10px; color: #f9fafb; font-weight: 600; }}
.next-id-item {{ display: flex; align-items: center; justify-content: flex-start; gap: 6px; }}
.next-id-item label {{ margin: 0; color: #a1a1aa; font-size: 10px; }}
.next-id-item input.next-id {{ width: 64px; height: 22px; padding: 0 4px; font-size: 11px; text-align: center; background: #18181b; color: #f9fafb; border: 1px solid #4b5563; border-radius: 6px; }}
.block.highlight-edge {{ box-shadow: 0 0 0 2px #38bdf8; background: #1f2933; }}
.export {{ background: #38bdf8; color: #0f0f14; border: none; padding: 12px; cursor: pointer; border-radius: 8px; width: 100%; font-weight: 600; margin-top: 12px; font-size: 13px; }}
.export:hover {{ background: #0ea5e9; }}
.export-secondary {{ background: #3f3f46; margin-top: 8px; }}
.export-secondary:hover {{ background: #52525b; }}
.save-ok {{ margin-top: 10px; padding: 10px; background: #166534; border-radius: 6px; font-size: 12px; color: #22c55e; }}
.save-err {{ margin-top: 10px; padding: 10px; background: #7f1d1d; border-radius: 6px; font-size: 12px; color: #ef4444; }}
.validation {{ margin-top: 10px; padding: 10px; background: #1c1917; border-radius: 6px; font-size: 12px; color: #fbbf24; }}
.validation.ok {{ color: #22c55e; }}
.empty {{ color: #71717a; font-style: italic; padding: 24px; text-align: center; }}
.crud-btn {{ border: none; cursor: pointer; border-radius: 6px; font-size: 12px; font-weight: 500; transition: all 0.15s; }}
.crud-delete-interaction {{ float: right; background: #7f1d1d; color: #fca5a5; padding: 3px 8px; }}
.crud-delete-interaction:hover {{ background: #991b1b; color: #fff; }}
.crud-delete-response {{ background: #7f1d1d; color: #fca5a5; padding: 2px 7px; font-size: 11px; }}
.crud-delete-response:hover {{ background: #991b1b; color: #fff; }}
.crud-add-response {{ display: block; width: 100%; background: #1e3a5f; color: #93c5fd; padding: 8px; margin-top: 10px; border: 1px dashed #3b82f6; }}
.crud-add-response:hover {{ background: #1e40af; color: #fff; border-style: solid; }}
.crud-add-interaction {{ display: block; width: 100%; background: #14532d; color: #86efac; padding: 10px; margin-top: 8px; border: 1px dashed #22c55e; font-size: 13px; }}
.crud-add-interaction:hover {{ background: #166534; color: #fff; border-style: solid; }}
.add-interaction-container {{ margin-top: 12px; }}
.resp-header {{ display: flex; justify-content: space-between; align-items: center; }}
.resp-header label {{ margin: 0; }}
.block .header {{ display: flex; justify-content: space-between; align-items: center; }}
.confirm-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); display: flex; align-items: center; justify-content: center; z-index: 100; }}
.confirm-box {{ background: #27272a; border: 1px solid #3f3f46; border-radius: 10px; padding: 24px; max-width: 400px; text-align: center; }}
.confirm-box p {{ margin: 0 0 16px; font-size: 14px; color: #e4e4e7; }}
.confirm-box .confirm-actions {{ display: flex; gap: 10px; justify-content: center; }}
.confirm-box button {{ padding: 8px 20px; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 500; }}
.confirm-box .confirm-yes {{ background: #dc2626; color: #fff; }}
.confirm-box .confirm-yes:hover {{ background: #ef4444; }}
.confirm-box .confirm-no {{ background: #3f3f46; color: #d4d4d8; }}
.confirm-box .confirm-no:hover {{ background: #52525b; }}
.mode-tabs {{ display: flex; gap: 6px; margin-bottom: 12px; }}
.mode-tabs button {{ padding: 8px 14px; border: 1px solid #3f3f46; background: #27272a; color: #a1a1aa; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 500; }}
.mode-tabs button:hover {{ color: #fff; background: #3f3f46; }}
.mode-tabs button.active {{ background: #38bdf8; color: #0f0f14; border-color: #38bdf8; }}
.panel-edit {{ display: block; }}
.panel-parcours {{ display: none; flex-direction: column; }}
.panel-edit.hidden {{ display: none; }}
.panel-parcours.active {{ display: flex; }}
.parcours-card {{ background: #27272a; border-radius: 10px; padding: 16px; margin-bottom: 12px; border: 1px solid #3f3f46; }}
.parcours-card .parcours-image {{ width: 100%; max-width: 200px; height: auto; border-radius: 8px; margin-bottom: 12px; display: block; object-fit: cover; }}
.parcours-card .actor {{ display: inline-block; background: #38bdf8; color: #0f0f14; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-bottom: 10px; }}
.parcours-card .text {{ font-size: 14px; line-height: 1.5; margin-bottom: 16px; color: #e4e4e7; }}
.parcours-choice {{ display: block; width: 100%; text-align: left; padding: 12px 14px; margin-bottom: 8px; background: #3f3f46; border: 1px solid #52525b; color: #e4e4e7; border-radius: 8px; cursor: pointer; font-size: 13px; transition: all 0.15s; }}
.parcours-choice:hover {{ background: #52525b; border-color: #38bdf8; }}
.parcours-end {{ color: #71717a; font-style: italic; padding: 20px; text-align: center; }}
.parcours-restart {{ background: #71717a; color: #fff; border: none; padding: 10px 14px; cursor: pointer; border-radius: 8px; font-size: 12px; margin-top: 8px; }}
.parcours-restart:hover {{ background: #52525b; }}
.parcours-totals {{ margin-top: 16px; padding: 14px; background: #18181b; border-radius: 8px; border: 1px solid #22c55e; }}
.parcours-totals h4 {{ margin: 0 0 10px; font-size: 12px; color: #22c55e; }}
.parcours-totals .score-line {{ display: flex; justify-content: space-between; padding: 4px 0; font-size: 13px; }}
.parcours-totals .score-line.positive {{ color: #22c55e; }}
.parcours-totals .score-line.negative {{ color: #ef4444; }}
.parcours-totals .score-line.zero {{ color: #71717a; }}
.crud-ai-response {{ display: block; width: 100%; background: #3b1361; color: #d8b4fe; padding: 8px; margin-top: 8px; border: 1px dashed #a855f7; }}
.crud-ai-response:hover {{ background: #581c87; color: #fff; border-style: solid; }}
.ai-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.65); display: flex; align-items: center; justify-content: center; z-index: 200; padding: 20px; }}
.ai-modal {{ background: #18181b; border: 1px solid #3f3f46; border-radius: 12px; padding: 22px; width: 100%; max-width: 640px; max-height: 92vh; overflow-y: auto; color: #e4e4e7; box-shadow: 0 20px 60px rgba(0,0,0,0.6); }}
.ai-modal h3 {{ margin: 0 0 6px; font-size: 16px; color: #c084fc; }}
.ai-modal .ai-sub {{ margin: 0 0 16px; font-size: 12px; color: #a1a1aa; }}
.ai-modal .ai-context {{ background: #27272a; border: 1px solid #3f3f46; border-radius: 8px; padding: 10px 12px; font-size: 12px; color: #d4d4d8; margin-bottom: 14px; }}
.ai-modal .ai-context strong {{ color: #a5b4fc; }}
.ai-section-title {{ margin: 10px 0 6px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: #71717a; }}
.ai-orientation {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px 14px; margin-bottom: 8px; }}
.ai-orientation .ai-ori-item {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; column-gap: 6px; padding: 4px 0; }}
.ai-orientation .ai-ori-item label {{ font-size: 11px; color: #e5e7eb; margin: 0; }}
.ai-orientation .score-stepper {{ justify-self: end; }}
.ai-modal textarea.ai-guidance {{ width: 100%; padding: 10px; font-size: 13px; background: #27272a; color: #f9fafb; border: 1px solid #4b5563; border-radius: 8px; resize: vertical; min-height: 60px; }}
.ai-modal select.ai-next {{ width: 100%; padding: 9px 10px; font-size: 13px; background: #27272a; color: #f9fafb; border: 1px solid #4b5563; border-radius: 8px; }}
.ai-next-hint {{ font-size: 11px; color: #71717a; margin-top: 4px; }}
.ai-modal .ai-actions {{ display: flex; gap: 10px; justify-content: flex-end; margin-top: 14px; }}
.ai-modal .ai-btn {{ padding: 10px 16px; border: none; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: 600; }}
.ai-btn-primary {{ background: #a855f7; color: #fff; }}
.ai-btn-primary:hover {{ background: #9333ea; }}
.ai-btn-primary[disabled] {{ background: #52525b; cursor: not-allowed; opacity: 0.8; }}
.ai-btn-secondary {{ background: #3f3f46; color: #d4d4d8; }}
.ai-btn-secondary:hover {{ background: #52525b; color: #fff; }}
.ai-status {{ margin-top: 10px; padding: 10px; border-radius: 6px; font-size: 12px; }}
.ai-status.loading {{ background: #1e293b; color: #93c5fd; border: 1px solid #1d4ed8; }}
.ai-status.err {{ background: #7f1d1d; color: #fecaca; border: 1px solid #b91c1c; }}
.ai-proposals {{ margin-top: 14px; display: flex; flex-direction: column; gap: 10px; }}
.ai-proposal {{ background: #27272a; border: 1px solid #3f3f46; border-radius: 10px; padding: 12px; }}
.ai-proposal .ai-cat {{ display: inline-block; font-size: 10px; padding: 2px 8px; border-radius: 999px; background: #1e3a5f; color: #93c5fd; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.04em; }}
.ai-proposal .ai-cat.exemplaire {{ background: #14532d; color: #86efac; }}
.ai-proposal .ai-cat.problematique {{ background: #7f1d1d; color: #fca5a5; }}
.ai-proposal .ai-text {{ font-size: 14px; line-height: 1.45; color: #f9fafb; margin-bottom: 8px; }}
.ai-proposal .ai-rationale {{ font-size: 11px; color: #a1a1aa; font-style: italic; margin-bottom: 8px; }}
.ai-proposal .ai-scores {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px 14px; margin-bottom: 10px; font-size: 11px; }}
.ai-proposal .ai-scores .sc {{ display: flex; justify-content: space-between; color: #d4d4d8; }}
.ai-proposal .ai-scores .sc .v.pos {{ color: #22c55e; font-weight: 600; }}
.ai-proposal .ai-scores .sc .v.neg {{ color: #ef4444; font-weight: 600; }}
.ai-proposal .ai-scores .sc .v.zero {{ color: #71717a; }}
.ai-proposal .ai-accept {{ background: #16a34a; color: #fff; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 600; }}
.ai-proposal .ai-accept:hover {{ background: #15803d; }}
</style>
</head>
<body>
<div class="sidebar">
    <div class="sidebar-top">
        <a href="../index.html" class="home-link" title="Retour à la page d'accueil">← Accueil</a>
        <div class="book-badge">{_html_escape(book_title)}</div>
        <h3>Choix du chapitre</h3>
        <select id="chapter-select" class="chapter-select">
            {chapter_options}
        </select>
        <h3>Scénarios du chapitre {chapter_id}</h3>
        <input type="text" class="search" id="search" placeholder="EG-3 : Recherche par texte">
        {sidebar_buttons}
    </div>
    <div class="sidebar-actions">
        <button class="export" id="save-btn">Valider et sauvegarder dans {_html_escape(book_json)}</button>
        <button class="export export-secondary" id="export-btn">Télécharger (JSON)</button>
        <div id="save-status"></div>
    </div>
</div>
<div class="main">
    <div class="panel-toggles">
        <button class="panel-toggle-btn" id="toggle-left-panel" type="button">Masquer</button>
        <button class="panel-toggle-btn" id="toggle-right-panel" type="button">Masquer</button>
    </div>
    <div id="network"></div>
    <div class="hint">Molette : zoom — Glisser : déplacer — Survol nœud : infobulle complète</div>
</div>
<div class="editor">
    <div class="mode-tabs">
        <button class="mode-btn active" data-mode="edit">Édition</button>
        <button class="mode-btn" data-mode="parcours">Parcours joueur</button>
    </div>
    <div class="panel-edit" id="panel-edit">
        <h3 id="ed-title">Sélectionnez un scénario</h3>
        <div id="ed-content"><div class="empty">Cliquez sur un scénario à gauche.</div></div>
        <div id="validation"></div>
    </div>
    <div class="panel-parcours" id="panel-parcours">
        <h3 id="parcours-title">Parcours joueur</h3>
        <div id="parcours-content">
            <div class="parcours-card">
                <div class="parcours-end">Sélectionnez un scénario puis choisissez vos réponses. Votre chemin s'affichera en vert sur le graphe.</div>
            </div>
        </div>
        <button class="parcours-restart" id="parcours-restart" style="display:none">Recommencer</button>
    </div>
</div>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js" crossorigin="anonymous"></script>
<script>
var chapterId = "{chapter_id}";
var bookSlug = "{book_slug}";
var chaptersData = {{"Chapters":[]}};
var scenesData = [];
try {{
    chaptersData = {chapters_json};
    scenesData = {scenes_json};
}} catch (e) {{
    console.error("Erreur chargement données:", e);
}}
var container = document.getElementById("network");
var network = null;
var nodesDS = null;
var edgesDS = null;
var currentSceneIdx = 0;
var currentMode = "edit";
var leftPanelHidden = false;
var rightPanelHidden = false;
var sceneNodePositions = {{}};
var cacheSaveTimer = null;
var cacheKey = "eol_graph_cache_v4_book_" + String(bookSlug || "default") + "_chapter_" + String(chapterId || "");
var SCORE_SKILLS = ["RespectAndDignity", "Empathy", "Compassion", "EmotionalRegulation", "CommunicationClarity", "ProfessionalBoundaries", "InterprofessionalCollaboration"];
var parcoursPath = {{ nodes: [], edges: [] }};
var parcoursCurrent = null;
var parcoursScores = {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }};

function getScenePositionKey(idx) {{
    var s = scenesData[idx];
    if (!s) return String(idx || 0);
    return s.scene_id != null ? String(s.scene_id) : String(idx || 0);
}}

function scheduleCacheSave() {{
    if (cacheSaveTimer) clearTimeout(cacheSaveTimer);
    cacheSaveTimer = setTimeout(function() {{
        saveCacheToLocalStorage();
    }}, 120);
}}

function saveCacheToLocalStorage() {{
    try {{
        var payload = {{
            version: 1,
            chapterId: chapterId,
            currentSceneIdx: currentSceneIdx,
            currentMode: currentMode,
            leftPanelHidden: leftPanelHidden,
            rightPanelHidden: rightPanelHidden,
            chaptersData: chaptersData,
            sceneNodePositions: sceneNodePositions
        }};
        localStorage.setItem(cacheKey, JSON.stringify(payload));
    }} catch (err) {{
        console.warn("saveCacheToLocalStorage:", err);
    }}
}}

function restoreCacheFromLocalStorage() {{
    try {{
        var raw = localStorage.getItem(cacheKey);
        if (!raw) return;
        var parsed = JSON.parse(raw);
        if (!parsed || parsed.chapterId !== chapterId) return;
        if (parsed.chaptersData && parsed.chaptersData.Chapters && parsed.chaptersData.Chapters.length > 0) {{
            chaptersData = parsed.chaptersData;
        }}
        if (parsed.sceneNodePositions && typeof parsed.sceneNodePositions === "object") {{
            sceneNodePositions = parsed.sceneNodePositions;
        }}
        if (typeof parsed.currentSceneIdx === "number") {{
            currentSceneIdx = parsed.currentSceneIdx;
        }}
        if (parsed.currentMode === "edit" || parsed.currentMode === "parcours") {{
            currentMode = parsed.currentMode;
        }}
        leftPanelHidden = !!parsed.leftPanelHidden;
        rightPanelHidden = !!parsed.rightPanelHidden;
    }} catch (err) {{
        console.warn("restoreCacheFromLocalStorage:", err);
    }}
}}

function saveCurrentScenePositions() {{
    try {{
        if (!network || !nodesDS) return;
        var ids = nodesDS.getIds();
        if (!ids || ids.length === 0) return;
        var key = getScenePositionKey(currentSceneIdx);
        sceneNodePositions[key] = network.getPositions(ids);
        scheduleCacheSave();
    }} catch (err) {{
        console.warn("saveCurrentScenePositions:", err);
    }}
}}

function applyCurrentScenePositions(idx) {{
    try {{
        if (!network || !nodesDS) return;
        var key = getScenePositionKey(idx);
        var pos = sceneNodePositions[key];
        if (!pos) return;
        Object.keys(pos).forEach(function(nodeId) {{
            var p = pos[nodeId];
            if (p && typeof p.x === "number" && typeof p.y === "number") {{
                network.moveNode(nodeId, p.x, p.y);
            }}
        }});
    }} catch (err) {{
        console.warn("applyCurrentScenePositions:", err);
    }}
}}

function updatePanelToggleButtons() {{
    var leftBtn = document.getElementById("toggle-left-panel");
    var rightBtn = document.getElementById("toggle-right-panel");
    if (leftBtn) leftBtn.textContent = leftPanelHidden ? "Afficher" : "Masquer";
    if (rightBtn) rightBtn.textContent = rightPanelHidden ? "Afficher" : "Masquer";
}}

function applyPanelVisibility() {{
    var sidebar = document.querySelector(".sidebar");
    var editor = document.querySelector(".editor");
    if (sidebar) sidebar.classList.toggle("hidden-panel", leftPanelHidden);
    if (editor) editor.classList.toggle("hidden-panel", rightPanelHidden);
    updatePanelToggleButtons();
}}

function setMode(mode) {{
    currentMode = mode;
    document.querySelectorAll(".mode-btn").forEach(function(b) {{ b.classList.toggle("active", b.dataset.mode === mode); }});
    document.getElementById("panel-edit").classList.toggle("hidden", mode !== "edit");
    document.getElementById("panel-parcours").classList.toggle("active", mode === "parcours");
    if (mode === "parcours" && scenesData.length > 0) {{
        parcoursPath = {{ nodes: [], edges: [] }};
        parcoursCurrent = null;
        parcoursScores = {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }};
        showParcoursScene(currentSceneIdx);
    }} else {{
        parcoursPath = {{ nodes: [], edges: [] }};
        parcoursCurrent = null;
        if (nodesDS && edgesDS) highlightPath();
    }}
    scheduleCacheSave();
}}

function showParcoursScene(idx) {{
    var s = scenesData[idx];
    document.getElementById("parcours-title").textContent = s.title + " — Parcours joueur";
    if (!s.parcours || s.parcours.length === 0) {{
        document.getElementById("parcours-content").innerHTML = '<div class="parcours-card"><div class="parcours-end">Aucune interaction dans ce scénario.</div></div>';
        document.getElementById("parcours-restart").style.display = "none";
        return;
    }}
    parcoursPath = {{ nodes: [], edges: [] }};
    parcoursScores = {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }};
    parcoursCurrent = s.parcours[0];
    renderParcours(s);
    highlightPath();
}}

function esc(s) {{ if (!s) return ""; return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }}
function renderParcours(s) {{
    var ia = parcoursCurrent;
    if (!ia) {{
        var totalsHtml = '<div class="parcours-card"><div class="parcours-end">Fin de cette branche.</div>';
        if (parcoursPath.nodes.length > 0) {{
            totalsHtml += '<div class="parcours-totals"><h4>Score total du parcours</h4>';
            var labels = {{ RespectAndDignity: "Respect et dignité", Empathy: "Empathie", Compassion: "Compassion", EmotionalRegulation: "Régulation émotionnelle", CommunicationClarity: "Clarté communication", ProfessionalBoundaries: "Frontières pro.", InterprofessionalCollaboration: "Collab. interpro." }};
            for (var k in parcoursScores) {{
                var v = parcoursScores[k];
                var cls = v > 0 ? "positive" : (v < 0 ? "negative" : "zero");
                totalsHtml += '<div class="score-line ' + cls + '">' + (labels[k] || k) + ': ' + (v >= 0 ? '+' : '') + v + '</div>';
            }}
            totalsHtml += '</div>';
        }}
        totalsHtml += '</div>';
        document.getElementById("parcours-content").innerHTML = totalsHtml;
        document.getElementById("parcours-restart").style.display = parcoursPath.nodes.length > 0 ? "block" : "none";
        return;
    }}
    var imgHtml = (ia.image) ? '<img class="parcours-image" src="/api/data/images/' + esc(ia.image) + '" alt="" />' : '';
    var html = '<div class="parcours-card">' + imgHtml + '<span class="actor">' + esc(ia.actor) + '</span><div class="text">' + esc(ia.text || "—") + '</div>';
    if (ia.responses && ia.responses.length > 0) {{
        ia.responses.forEach(function(r, i) {{
            var label = r.text || ("→ I" + r.next_id);
            var scores = {{ RespectAndDignity: r.RespectAndDignity||0, Empathy: r.Empathy||0, Compassion: r.Compassion||0, EmotionalRegulation: r.EmotionalRegulation||0, CommunicationClarity: r.CommunicationClarity||0, ProfessionalBoundaries: r.ProfessionalBoundaries||0, InterprofessionalCollaboration: r.InterprofessionalCollaboration||0 }};
            html += '<button class="parcours-choice" data-next="' + r.next_id + '" data-target="' + esc(r.target_node_id || "") + '" data-edge="' + esc(r.edge_id || "") + '" data-scores="' + esc(JSON.stringify(scores)) + '">' + esc(label) + '</button>';
        }});
    }} else {{
        html += '<div class="parcours-end">Fin de cette branche.</div>';
    }}
    html += '</div>';

    // Affichage du score courant du parcours (mise à jour en direct)
    var labels = {{ RespectAndDignity: "Respect et dignité", Empathy: "Empathie", Compassion: "Compassion", EmotionalRegulation: "Régulation émotionnelle", CommunicationClarity: "Clarté communication", ProfessionalBoundaries: "Frontières pro.", InterprofessionalCollaboration: "Collab. interpro." }};
    var liveTotals = '<div class="parcours-totals"><h4>Score courant du parcours</h4>';
    for (var k in parcoursScores) {{
        var v = parcoursScores[k] || 0;
        var cls = v > 0 ? "positive" : (v < 0 ? "negative" : "zero");
        liveTotals += '<div class="score-line ' + cls + '">' + (labels[k] || k) + ': ' + (v >= 0 ? '+' : '') + v + '</div>';
    }}
    liveTotals += '</div>';
    html += liveTotals;
    document.getElementById("parcours-content").innerHTML = html;
    document.getElementById("parcours-restart").style.display = parcoursPath.nodes.length > 0 ? "block" : "none";
    document.querySelectorAll(".parcours-choice").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            var scores = JSON.parse(this.dataset.scores || "{{}}");
            for (var k in scores) parcoursScores[k] = (parcoursScores[k] || 0) + (parseInt(scores[k]) || 0);
            var nextId = this.dataset.next;
            var edgeId = this.dataset.edge;
            if (parcoursCurrent && parcoursCurrent.node_id) parcoursPath.nodes.push(parcoursCurrent.node_id);
            if (edgeId) parcoursPath.edges.push(edgeId);
            parcoursCurrent = s.id_to_parcours && nextId !== "-1" && nextId !== "" ? s.id_to_parcours[nextId] : null;
            if (parcoursCurrent) parcoursPath.nodes.push(parcoursCurrent.node_id);
            renderParcours(s);
            highlightPath();
        }});
    }});
}}

function highlightPath() {{
    try {{
        if (!nodesDS || !edgesDS) return;
        var pathNodes = parcoursPath.nodes || [];
        var pathEdges = parcoursPath.edges || [];
        var curNode = parcoursCurrent ? parcoursCurrent.node_id : null;
        nodesDS.getIds().forEach(function(nid) {{
            var node = nodesDS.get(nid) || {{}};
            var isRoot = !!node.is_root;
            var inPath = pathNodes.indexOf(nid) >= 0;
            var isCurrent = curNode === nid;
            var bg;
            var border;
            if (inPath) {{
                bg = "#166534";
                border = isCurrent ? "#fbbf24" : "#22c55e";
            }} else if (isRoot) {{
                bg = "#451a1a";
                border = "#f97373";
            }} else {{
                bg = "#27272a";
                border = "#38bdf8";
            }}
            nodesDS.update({{ id: nid, color: {{ background: bg, border: border }} }});
        }});
        edgesDS.getIds().forEach(function(eid) {{
            var inPath = pathEdges.indexOf(eid) >= 0;
            edgesDS.update({{ id: eid, color: inPath ? "#4ade80" : "#9ca3af" }});
        }});
    }} catch (err) {{ console.warn("highlightPath:", err); }}
}}

function showOnlySelectedBlock(interactionId) {{
    var blocks = Array.prototype.slice.call(document.querySelectorAll("#ed-content .block"));
    if (!blocks.length) return;
    var target = interactionId ? String(interactionId) : "";
    var selected = null;
    blocks.forEach(function(block) {{
        var isMatch = target && block.dataset.interactionId === target;
        block.style.display = isMatch ? "block" : "none";
        block.classList.toggle("active", isMatch);
        if (isMatch) selected = block;
    }});
    if (!selected) {{
        selected = blocks[0];
        selected.style.display = "block";
        selected.classList.add("active");
    }}
}}

function getInteractionIdFromNodeId(nodeId) {{
    if (!nodeId || !nodesDS) return "";
    var node = nodesDS.get(nodeId);
    if (node && node.interaction_id != null) return String(node.interaction_id);
    var raw = String(nodeId);
    var pos = raw.lastIndexOf("_I");
    if (pos >= 0) return raw.substring(pos + 2);
    return "";
}}

function showScene(idx) {{
    if (idx < 0 || idx >= scenesData.length) return;
    if (network && nodesDS && idx !== currentSceneIdx) saveCurrentScenePositions();
    currentSceneIdx = idx;
    scheduleCacheSave();
    document.querySelectorAll(".scene-btn").forEach(function(b) {{
        b.classList.toggle("active", parseInt(b.dataset.idx) === idx);
    }});
    var s = scenesData[idx];
    document.getElementById("ed-title").textContent = s.title;

    rebuildSceneGraph(idx);
    rebuildEditorHtml(idx);
    showOnlySelectedBlock(null);

    var opts = {{
        nodes: {{ font: {{ size: 38, color: "#f9fafb", face: "system-ui, -apple-system, sans-serif", bold: true }}, shape: "box", color: {{ background: "#18181b", border: "#38bdf8" }}, margin: 32, borderWidth: 2, widthConstraint: {{ minimum: 260, maximum: 360 }} }},
        edges: {{
            arrows: "to",
            width: 2,
            hoverWidth: 3,
            selectionWidth: 5,
            smooth: {{ enabled: true, type: "dynamic", roundness: 0.35 }},
            color: "#9ca3af",
            font: {{
                color: "#a5b4fc",
                size: 14,
                align: "top",
                face: "system-ui, sans-serif",
                strokeWidth: 0
            }}
        }},
        layout: {{ hierarchical: {{ enabled: true, direction: "UD", sortMethod: "directed", levelSeparation: 420, nodeSpacing: 560, treeSpacing: 520, blockShifting: true, edgeMinimization: true, parentCentralization: true }} }},
        physics: {{ enabled: false }},
        interaction: {{ zoomView: true, dragView: true, zoomSpeed: 0.35 }}
    }};

    if (!network) {{
        nodesDS = new vis.DataSet(scenesData[idx].nodes);
        edgesDS = new vis.DataSet(scenesData[idx].edges);
        network = new vis.Network(container, {{ nodes: nodesDS, edges: edgesDS }}, opts);
        network.once("afterDrawing", function() {{ network.fit({{ animation: {{ duration: 400 }}, scale: 1.6 }}); }});
        setTimeout(function() {{ if (network) {{ network.redraw(); network.fit({{ scale: 1.6 }}); }} }}, 300);
        setTimeout(function() {{ applyCurrentScenePositions(idx); }}, 360);
        network.on("click", function(params) {{
            if (params.nodes && params.nodes.length > 0) {{
                var nid = String(params.nodes[0]);
                var iaId = getInteractionIdFromNodeId(nid);
                if (iaId) {{
                    showOnlySelectedBlock(iaId);
                    var block = document.querySelector('.block[data-interaction-id="' + iaId + '"]');
                    if (block) {{
                        block.scrollIntoView({{ behavior: "smooth", block: "start" }});
                    }}
                }}
            }} else if (params.edges && params.edges.length > 0) {{
                var eid = String(params.edges[0]);
                focusResponseByEdgeId(eid);
            }}
        }});
        network.on("dragEnd", function(params) {{
            if (params && params.nodes && params.nodes.length > 0) saveCurrentScenePositions();
        }});
    }} else {{
        setTimeout(function() {{
            if (network) {{
                network.fit({{ animation: {{ duration: 300 }}, scale: 1.3 }});
                applyCurrentScenePositions(idx);
            }}
        }}, 220);
    }}

    updateValidation();
    if (document.getElementById("panel-parcours").classList.contains("active")) {{
        parcoursPath = {{ nodes: [], edges: [] }};
        parcoursCurrent = null;
        showParcoursScene(idx);
    }} else {{
        highlightPath();
    }}
}}

function hydrateEditorFieldsFromData(idx) {{
    var chapter = (chaptersData && chaptersData.Chapters && chaptersData.Chapters[0]) ? chaptersData.Chapters[0] : null;
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];
    var intro = document.querySelector('#ed-content textarea.edit[data-type="intro"]');
    if (intro) intro.value = sc.SceneIntroduction || "";
    (sc.Interactions || []).forEach(function(ia, i) {{
        var nameEl = document.querySelector('#ed-content textarea.edit[data-type="name"][data-i="' + i + '"]');
        if (nameEl) nameEl.value = ia.Name || "";
        var textEl = document.querySelector('#ed-content textarea.edit[data-type="text"][data-i="' + i + '"]');
        if (textEl) textEl.value = ia.Text || "";
        (ia.Responses || []).forEach(function(r, rIdx) {{
            var respEl = document.querySelector('#ed-content textarea.edit[data-type="response"][data-i="' + i + '"][data-r="' + rIdx + '"]');
            if (respEl) respEl.value = r.Text || "";
            var nextEl = document.querySelector('#ed-content .next-id[data-i="' + i + '"][data-r="' + rIdx + '"]');
            if (nextEl) {{
                var nextVal = r.NextInteractionID;
                nextEl.value = (nextVal == null) ? "" : String(nextVal);
            }}
            SCORE_SKILLS.forEach(function(skill) {{
                var v = parseInt(r[skill], 10);
                if (isNaN(v)) v = 0;
                var hidden = document.querySelector('#ed-content .score[data-i="' + i + '"][data-r="' + rIdx + '"][data-skill="' + skill + '"]');
                if (hidden) hidden.value = String(v);
                var valueEl = document.querySelector('#ed-content .score-value[data-i="' + i + '"][data-r="' + rIdx + '"][data-skill="' + skill + '"]');
                if (valueEl) valueEl.textContent = String(v);
            }});
        }});
    }});
}}

function escapeHtml(s) {{
    if (!s) return '';
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}}

function focusResponseByEdgeId(edgeId) {{
    try {{
        if (!edgeId) return;
        var edge = edgesDS ? edgesDS.get(edgeId) : null;
        if (!edge) return;
        var iaId = getInteractionIdFromNodeId(edge.from);
        var m = String(edgeId).match(/_R(\\d+)_>/);
        var rIdx = m ? parseInt(m[1], 10) : -1;
        if (!iaId || rIdx < 0) return;
        showOnlySelectedBlock(iaId);
        var block = document.querySelector('.block[data-interaction-id="' + iaId + '"]');
        if (!block) return;
        var textarea = block.querySelector('textarea.edit[data-type="response"][data-r="' + rIdx + '"]');
        if (!textarea) return;
        textarea.scrollIntoView({{ behavior: "smooth", block: "center" }});
        textarea.focus();
        block.classList.add("highlight-edge");
        setTimeout(function() {{ block.classList.remove("highlight-edge"); }}, 1500);
    }} catch (e) {{
        console.warn("focusResponseByEdgeId:", e);
    }}
}}

function attachEditors(idx) {{
    var ch = chaptersData.Chapters[0];
    var sc = ch.Scenes[idx];
    document.querySelectorAll("#ed-content .edit").forEach(function(el) {{
        el.addEventListener("input", function() {{
            var type = this.dataset.type;
            var i = parseInt(this.dataset.i);
            if (type === "intro") {{
                sc.SceneIntroduction = this.value;
            }} else if (type === "name") {{
                sc.Interactions[i].Name = this.value;
            }} else if (type === "text") {{
                sc.Interactions[i].Text = this.value;
                sc.Interactions[i].Name = this.value.substring(0, 50);
            }} else if (type === "response") {{
                var r = parseInt(this.dataset.r);
                sc.Interactions[i].Responses[r].Text = this.value;
                sc.Interactions[i].Responses[r].Name = this.value.substring(0, 80);
            }}
            scheduleCacheSave();
        }});
    }});
    document.querySelectorAll("#ed-content .score-btn").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            var i = parseInt(this.dataset.i), r = parseInt(this.dataset.r), skill = this.dataset.skill;
            var hidden = document.querySelector('.score[data-i="' + i + '"][data-r="' + r + '"][data-skill="' + skill + '"]');
            var valueEl = document.querySelector('.score-value[data-i="' + i + '"][data-r="' + r + '"][data-skill="' + skill + '"]');
            if (!hidden || !valueEl) return;
            var v = parseInt(hidden.value) || 0;
            v += this.classList.contains("score-plus") ? 1 : -1;
            if (v < -3) v = -3;
            if (v > 3) v = 3;
            hidden.value = String(v);
            valueEl.textContent = String(v);
            var resp = sc.Interactions[i].Responses[r];
            resp[skill] = v;
            if (resp.SoftSkillDimensions) resp.SoftSkillDimensions[skill] = v;
            scheduleCacheSave();
        }});
    }});
    document.querySelectorAll("#ed-content .next-id").forEach(function(el) {{
        el.addEventListener("change", function() {{
            var i = parseInt(this.dataset.i), r = parseInt(this.dataset.r);
            var raw = (this.value || "").trim();
            if (raw === "") {{
                delete sc.Interactions[i].Responses[r].NextInteractionID;
                scheduleCacheSave();
                return;
            }}
            var v = parseInt(raw, 10);
            if (isNaN(v)) {{
                this.value = "";
                delete sc.Interactions[i].Responses[r].NextInteractionID;
                scheduleCacheSave();
                return;
            }}
            sc.Interactions[i].Responses[r].NextInteractionID = v;
            scheduleCacheSave();
        }});
    }});
}}

function updateValidation() {{
    var errs = [];
    var ch = chaptersData.Chapters[0];
    ch.Scenes.forEach(function(sc) {{
        var ids = {{}};
        sc.Interactions.forEach(function(ia) {{ ids[ia.Id] = true; }});
        sc.Interactions.forEach(function(ia) {{
            (ia.Responses || []).forEach(function(r) {{
                var nid = r.NextInteractionID;
                if (nid != null && nid !== -1 && !ids[nid]) errs.push("EG-7: NextInteractionID " + nid + " invalide (scène " + sc.Title + ")");
            }});
        }});
    }});
    var div = document.getElementById("validation");
    if (errs.length > 0) {{
        div.className = "validation";
        div.textContent = errs.join(" ; ");
    }} else {{
        div.className = "validation ok";
        div.textContent = "EG-7 : Validation OK — NextInteractionID valides.";
    }}
}}

document.querySelectorAll(".scene-btn").forEach(function(b) {{
    b.addEventListener("click", function() {{ showScene(parseInt(this.dataset.idx)); }});
}});

document.getElementById("chapter-select").addEventListener("change", function() {{
    var target = (this.value || "").trim();
    if (target) {{
        saveCurrentScenePositions();
        saveCacheToLocalStorage();
        window.location.href = target;
    }}
}});

document.querySelectorAll(".mode-btn").forEach(function(b) {{
    b.addEventListener("click", function() {{ setMode(this.dataset.mode); }});
}});

document.getElementById("toggle-left-panel").addEventListener("click", function() {{
    leftPanelHidden = !leftPanelHidden;
    applyPanelVisibility();
    scheduleCacheSave();
}});

document.getElementById("toggle-right-panel").addEventListener("click", function() {{
    rightPanelHidden = !rightPanelHidden;
    applyPanelVisibility();
    scheduleCacheSave();
}});

document.getElementById("parcours-restart").addEventListener("click", function() {{
    if (scenesData.length > 0) showParcoursScene(currentSceneIdx);
}});

document.getElementById("search").addEventListener("input", function() {{
    var q = (this.value || "").toLowerCase();
    document.querySelectorAll(".scene-btn").forEach(function(b) {{
        b.style.display = q && b.textContent.toLowerCase().indexOf(q) < 0 ? "none" : "block";
    }});
    if (scenesData && scenesData.length > 0) {{
        var vis = (this.value || "").toLowerCase();
        if (vis && nodesDS && edgesDS) {{
            var nodeIds = nodesDS.getIds();
            nodeIds.forEach(function(nid) {{
                var node = nodesDS.get(nid);
                var match = (node.label && node.label.toLowerCase().indexOf(vis) >= 0) || (node.title && node.title.toLowerCase().indexOf(vis) >= 0);
                nodesDS.update({{ id: nid, hidden: !match }});
            }});
        }} else if (nodesDS) {{
            nodesDS.getIds().forEach(function(nid) {{ nodesDS.update({{ id: nid, hidden: false }}); }});
        }}
    }}
}});

window.addEventListener("beforeunload", function() {{
    saveCurrentScenePositions();
    saveCacheToLocalStorage();
}});

document.getElementById("save-btn").addEventListener("click", function() {{
    var btn = this;
    var statusEl = document.getElementById("save-status");
    btn.disabled = true;
    statusEl.className = "";
    statusEl.textContent = "Enregistrement…";
    fetch("/api/save", {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ book_slug: bookSlug, Chapters: chaptersData.Chapters }})
    }}).then(function(r) {{ return r.json().then(function(d) {{ return {{ ok: r.ok, data: d }}; }}); }})
    .then(function(result) {{
        btn.disabled = false;
        if (result.ok) {{
            statusEl.className = "save-ok";
            statusEl.textContent = result.data.message || "Sauvegardé.";
        }} else {{
            statusEl.className = "save-err";
            statusEl.textContent = result.data.error || "Erreur. Utilisez python app.py pour activer la sauvegarde directe.";
        }}
    }}).catch(function(err) {{
        btn.disabled = false;
        statusEl.className = "save-err";
        statusEl.textContent = "Erreur réseau. Lancez python app.py puis ouvrez http://localhost:8765";
    }});
}});

document.getElementById("export-btn").addEventListener("click", function() {{
    var blob = new Blob([JSON.stringify(chaptersData, null, 2)], {{ type: "application/json" }});
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "Chapitre_" + chapterId + "_modified.json";
    a.click();
}});

function confirmDialog(msg) {{
    return new Promise(function(resolve) {{
        var ov = document.createElement("div");
        ov.className = "confirm-overlay";
        ov.innerHTML = '<div class="confirm-box"><p>' + escapeHtml(msg) + '</p><div class="confirm-actions"><button class="confirm-yes">Supprimer</button><button class="confirm-no">Annuler</button></div></div>';
        document.body.appendChild(ov);
        ov.querySelector(".confirm-yes").addEventListener("click", function() {{ document.body.removeChild(ov); resolve(true); }});
        ov.querySelector(".confirm-no").addEventListener("click", function() {{ document.body.removeChild(ov); resolve(false); }});
    }});
}}

function getNextInteractionId(sc) {{
    var maxId = 0;
    (sc.Interactions || []).forEach(function(ia) {{ if (ia.Id > maxId) maxId = ia.Id; }});
    return maxId + 1;
}}

function getNextResponseId(ia) {{
    var maxId = 0;
    (ia.Responses || []).forEach(function(r) {{ if (r.Id > maxId) maxId = r.Id; }});
    return maxId + 1;
}}

function rebuildSceneGraph(idx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];
    var chId = chapter.Id;
    var interactions = sc.Interactions || [];
    var idToIa = {{}};
    interactions.forEach(function(ia) {{ idToIa[ia.Id] = ia; }});

    var newNodes = [];
    var newEdges = [];
    interactions.forEach(function(ia) {{
        var actorName = (ia.Actor || {{}}).Name || "?";
        var text = ia.Text || "";
        var name = ia.Name || text.substring(0, 50);
        var nodeId = "C" + chId + "_S" + sc.Id + "_I" + ia.Id;
        var baseLabel = name || text || "—";
        if (baseLabel.length > 38) baseLabel = baseLabel.substring(0, 37) + "…";
        var label = ia.Id + " — " + baseLabel;
        var title = "[" + actorName + "] " + (text || name);
        newNodes.push({{ id: nodeId, label: label, title: title, interaction_id: String(ia.Id) }});
        var respList = ia.Responses || [];
        var respCount = respList.length;
        respList.forEach(function(r, rIdx) {{
            var nextId = r.NextInteractionID;
            if (nextId == null || nextId === -1) return;
            if (!idToIa[nextId]) return;
            var targetNodeId = "C" + chId + "_S" + sc.Id + "_I" + nextId;
            var edgeId = nodeId + "_R" + rIdx + "_>" + targetNodeId;
            var rText = (r.Text || "").trim();
            var edgeTitle = "Réponse " + (rIdx + 1);
            if (rText) edgeTitle += " — " + rText;

            // Courbure latérale par flèche : on alterne curvedCW / curvedCCW
            // et on fait croître le rayon avec l'index de la réponse, pour que
            // plusieurs flèches partant du même bloc (ou allant vers la même
            // cible) soient visuellement séparées au lieu de se superposer.
            var direction = (rIdx % 2 === 0) ? "curvedCW" : "curvedCCW";
            var roundness;
            if (respCount <= 1) {{
                roundness = 0.2;
            }} else {{
                // 0.20, 0.35, 0.50, 0.65... plafonné à 0.85
                roundness = 0.20 + (Math.floor(rIdx / 2) * 0.15);
                if (roundness > 0.85) roundness = 0.85;
            }}
            // Boucle arrière ou latérale (cible <= source) : on force un rayon
            // plus grand pour que la flèche passe franchement sur le côté.
            var isBackOrLateral = parseInt(nextId, 10) <= parseInt(ia.Id, 10);
            if (isBackOrLateral) {{
                roundness = Math.max(roundness, 0.55 + (rIdx * 0.1));
                if (roundness > 0.95) roundness = 0.95;
            }}

            newEdges.push({{
                id: edgeId,
                from: nodeId,
                to: targetNodeId,
                label: "R" + (rIdx + 1),
                title: edgeTitle,
                smooth: {{ enabled: true, type: direction, roundness: roundness }}
            }});
        }});
    }});

    var targets = {{}};
    newEdges.forEach(function(e) {{ targets[e.to] = true; }});
    var firstNodeId = interactions.length > 0 ? "C" + chId + "_S" + sc.Id + "_I" + interactions[0].Id : null;
    newNodes.forEach(function(n) {{
        if (!targets[n.id] && n.id !== firstNodeId) {{
            n.is_root = true;
            n.color = {{ background: "#451a1a", border: "#f97373" }};
        }} else {{
            n.color = {{ background: "#27272a", border: "#38bdf8" }};
        }}
    }});

    scenesData[idx].nodes = newNodes;
    scenesData[idx].edges = newEdges;

    if (nodesDS && edgesDS) {{
        nodesDS.clear();
        edgesDS.clear();
        newNodes.forEach(function(n) {{ nodesDS.add(n); }});
        newEdges.forEach(function(e) {{ edgesDS.add(e); }});
    }}
    highlightPath();
    updateValidation();
}}

function rebuildEditorHtml(idx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];

    var introValue = sc.SceneIntroduction || "";
    var introHtml = '<div class="scene-intro"><label>EG-4 : SceneIntroduction</label><textarea class="edit" data-type="intro" rows="3">' + escapeHtml(introValue) + '</textarea></div>';

    var blocksHtml = "";
    var skills = SCORE_SKILLS;
    (sc.Interactions || []).forEach(function(ia, i) {{
        var actor = (ia.Actor || {{}}).Name || "";
        var text = ia.Text || "";
        var name = ia.Name || text.substring(0, 50);
        var b = '<div class="block" data-interaction-id="' + ia.Id + '" data-i="' + i + '">';
        b += '<div class="header"><span>Interaction ' + ia.Id + ' — ' + escapeHtml(actor) + '</span>';
        b += '<button type="button" class="crud-btn crud-delete-interaction" data-i="' + i + '" title="Supprimer cette interaction">✕</button></div>';
        b += '<label>EG-4 : Name</label>';
        b += '<textarea class="edit" data-type="name" data-i="' + i + '" rows="1">' + escapeHtml(name) + '</textarea>';
        b += '<label>EG-4 : Text</label>';
        b += '<textarea class="edit" data-type="text" data-i="' + i + '" rows="3">' + escapeHtml(text) + '</textarea>';
        b += '<div class="responses-container" data-i="' + i + '">';
        (ia.Responses || []).forEach(function(r, rIdx) {{
            var rtext = r.Text || "";
            var nextId = r.NextInteractionID;
            b += '<div class="resp" data-i="' + i + '" data-r="' + rIdx + '">';
            b += '<div class="resp-header"><label>Réponse ' + (rIdx + 1) + ' — Text</label>';
            b += '<button type="button" class="crud-btn crud-delete-response" data-i="' + i + '" data-r="' + rIdx + '" title="Supprimer cette réponse">✕</button></div>';
            b += '<textarea class="edit" data-type="response" data-i="' + i + '" data-r="' + rIdx + '" rows="2">' + escapeHtml(rtext) + '</textarea>';
            b += '<div class="scores">';
            skills.forEach(function(sk) {{
                var dims = r.SoftSkillDimensions || {{}};
                var val = dims[sk] != null ? dims[sk] : (r[sk] != null ? r[sk] : 0);
                b += '<div class="score-item"><label>' + sk + '</label>';
                b += '<div class="score-stepper">';
                b += '<button type="button" class="score-btn score-minus" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '">-</button>';
                b += '<input type="hidden" class="score" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '" value="' + val + '">';
                b += '<span class="score-value" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '">' + val + '</span>';
                b += '<button type="button" class="score-btn score-plus" data-i="' + i + '" data-r="' + rIdx + '" data-skill="' + sk + '">+</button>';
                b += '</div></div>';
            }});
            b += '<div class="score-item next-id-item"><label>Next Id</label>';
            b += '<input type="number" class="next-id" data-i="' + i + '" data-r="' + rIdx + '" value="' + (nextId != null ? nextId : "") + '"></div>';
            b += '</div></div>';
        }});
        b += '</div>';
        b += '<button type="button" class="crud-btn crud-add-response" data-i="' + i + '">+ Ajouter une réponse</button>';
        b += '<button type="button" class="crud-btn crud-ai-response" data-i="' + i + '" data-ia-id="' + ia.Id + '">✨ Proposer une réponse avec IA</button>';
        b += '</div>';
        blocksHtml += b;
    }});
    blocksHtml += '<div class="add-interaction-container"><button type="button" class="crud-btn crud-add-interaction">+ Ajouter une interaction</button></div>';

    document.getElementById("ed-content").innerHTML = introHtml + blocksHtml;
    scenesData[idx].editor = blocksHtml;
    attachEditors(idx);
    attachCrudHandlers(idx);
}}

function addInteraction(idx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];
    var newId = getNextInteractionId(sc);
    var firstActor = (sc.Interactions && sc.Interactions.length > 0 && sc.Interactions[0].Actor)
        ? JSON.parse(JSON.stringify(sc.Interactions[0].Actor)) : {{ Id: 0, Name: "Nouveau" }};
    var newIa = {{
        Id: newId,
        Name: "Nouvelle interaction " + newId,
        Actor: firstActor,
        Text: "",
        AgentFacialExpression: "",
        Responses: []
    }};
    sc.Interactions.push(newIa);
    scheduleCacheSave();
    rebuildEditorHtml(idx);
    rebuildSceneGraph(idx);
    showOnlySelectedBlock(String(newId));
    var block = document.querySelector('.block[data-interaction-id="' + newId + '"]');
    if (block) block.scrollIntoView({{ behavior: "smooth", block: "start" }});
}}

function deleteInteraction(idx, iIdx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];
    var ia = sc.Interactions[iIdx];
    if (!ia) return;
    var deletedId = ia.Id;
    confirmDialog("Supprimer l'interaction " + deletedId + " et toutes ses réponses ?").then(function(ok) {{
        if (!ok) return;
        sc.Interactions.splice(iIdx, 1);
        sc.Interactions.forEach(function(otherIa) {{
            (otherIa.Responses || []).forEach(function(r) {{
                if (r.NextInteractionID === deletedId) {{
                    r.NextInteractionID = -1;
                }}
            }});
        }});
        scheduleCacheSave();
        rebuildEditorHtml(idx);
        rebuildSceneGraph(idx);
        showOnlySelectedBlock(null);
    }});
}}

function addResponse(idx, iIdx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];
    var ia = sc.Interactions[iIdx];
    if (!ia) return;
    if (!ia.Responses) ia.Responses = [];
    var newRespId = getNextResponseId(ia);
    var newResp = {{
        Id: newRespId,
        Name: "",
        Text: "",
        NextInteractionID: -1,
        SoftSkillDimensions: {{ RespectAndDignity: 0, Empathy: 0, Compassion: 0, EmotionalRegulation: 0, CommunicationClarity: 0, ProfessionalBoundaries: 0, InterprofessionalCollaboration: 0 }}
    }};
    SCORE_SKILLS.forEach(function(sk) {{ newResp[sk] = 0; }});
    ia.Responses.push(newResp);
    scheduleCacheSave();
    rebuildEditorHtml(idx);
    rebuildSceneGraph(idx);
    showOnlySelectedBlock(String(ia.Id));
}}

function deleteResponse(idx, iIdx, rIdx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[idx]) return;
    var sc = chapter.Scenes[idx];
    var ia = sc.Interactions[iIdx];
    if (!ia || !ia.Responses || !ia.Responses[rIdx]) return;
    confirmDialog("Supprimer la réponse " + (rIdx + 1) + " de l'interaction " + ia.Id + " ?").then(function(ok) {{
        if (!ok) return;
        ia.Responses.splice(rIdx, 1);
        scheduleCacheSave();
        rebuildEditorHtml(idx);
        rebuildSceneGraph(idx);
        showOnlySelectedBlock(String(ia.Id));
    }});
}}

var SKILL_LABELS_FR = {{
    RespectAndDignity: "Respect et dignité",
    Empathy: "Empathie",
    Compassion: "Compassion",
    EmotionalRegulation: "Régulation émotionnelle",
    CommunicationClarity: "Clarté communication",
    ProfessionalBoundaries: "Frontières pro.",
    InterprofessionalCollaboration: "Collab. interpro."
}};

function buildOrientationStepper(skill) {{
    var html = '<div class="ai-ori-item">';
    html += '<label>' + (SKILL_LABELS_FR[skill] || skill) + '</label>';
    html += '<div class="score-stepper">';
    html += '<button type="button" class="score-btn ai-ori-minus" data-skill="' + skill + '">-</button>';
    html += '<input type="hidden" class="ai-ori" data-skill="' + skill + '" value="0">';
    html += '<span class="score-value ai-ori-value" data-skill="' + skill + '">0</span>';
    html += '<button type="button" class="score-btn ai-ori-plus" data-skill="' + skill + '">+</button>';
    html += '</div></div>';
    return html;
}}

function renderAiProposalCard(p) {{
    var cat = (p.Category || "").toLowerCase();
    var catClass = cat === "exemplaire" ? "exemplaire" : (cat === "problématique" || cat === "problematique" ? "problematique" : "neutre");
    var catLabel = p.Category || "neutre";
    var dims = p.SoftSkillDimensions || {{}};
    var html = '<div class="ai-proposal">';
    html += '<span class="ai-cat ' + catClass + '">' + escapeHtml(catLabel) + '</span>';
    html += '<div class="ai-text">' + escapeHtml(p.Text || "") + '</div>';
    if (p.Rationale) {{
        html += '<div class="ai-rationale">' + escapeHtml(p.Rationale) + '</div>';
    }}
    html += '<div class="ai-scores">';
    SCORE_SKILLS.forEach(function(sk) {{
        var v = parseInt(dims[sk], 10);
        if (isNaN(v)) v = 0;
        var vcls = v > 0 ? "pos" : (v < 0 ? "neg" : "zero");
        var sign = v > 0 ? "+" : "";
        html += '<div class="sc"><span>' + (SKILL_LABELS_FR[sk] || sk) + '</span><span class="v ' + vcls + '">' + sign + v + '</span></div>';
    }});
    html += '</div>';
    html += '<button type="button" class="ai-accept">Accepter et ajouter comme nouvelle réponse</button>';
    html += '</div>';
    return html;
}}

function openAiProposalModal(sceneIdx, iIdx) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[sceneIdx]) return;
    var sc = chapter.Scenes[sceneIdx];
    var ia = sc.Interactions[iIdx];
    if (!ia) return;

    var actorName = (ia.Actor || {{}}).Name || "?";
    var orientationHtml = '';
    SCORE_SKILLS.forEach(function(sk) {{ orientationHtml += buildOrientationStepper(sk); }});

    var nextOptionsHtml = '<option value="-1">-1 — Fin de branche (aucune suite)</option>';
    (sc.Interactions || []).forEach(function(otherIa) {{
        if (otherIa.Id === ia.Id) return;
        var preview = (otherIa.Text || otherIa.Name || "").substring(0, 80);
        var otherActor = (otherIa.Actor || {{}}).Name || "?";
        nextOptionsHtml += '<option value="' + otherIa.Id + '">#' + otherIa.Id + ' [' + escapeHtml(otherActor) + '] ' + escapeHtml(preview) + (otherIa.Text && otherIa.Text.length > 80 ? "…" : "") + '</option>';
    }});

    var ov = document.createElement("div");
    ov.className = "ai-overlay";
    ov.innerHTML =
        '<div class="ai-modal">' +
            '<h3>✨ Proposer une réponse avec IA</h3>' +
            '<p class="ai-sub">Le LLM analyse le contexte et propose une nouvelle réplique de l\\'acteur, orientée selon vos choix. Aucune insertion n\\'est faite tant que vous n\\'avez pas cliqué sur « Accepter ».</p>' +
            '<div class="ai-context">' +
                '<div><strong>Scène</strong> : ' + escapeHtml(sc.Title || "") + '</div>' +
                '<div><strong>Interaction</strong> #' + ia.Id + ' (' + escapeHtml(actorName) + ') : ' + escapeHtml((ia.Text || "").substring(0, 140)) + (ia.Text && ia.Text.length > 140 ? "…" : "") + '</div>' +
            '</div>' +
            '<div class="ai-section-title">Prochain bloc (NextInteractionID)</div>' +
            '<select class="ai-next">' + nextOptionsHtml + '</select>' +
            '<div class="ai-next-hint">La réponse générée sera rédigée pour mener naturellement à ce bloc, et sera liée à lui une fois acceptée.</div>' +
            '<div class="ai-section-title">Orientation soft skills (-3 à +3)</div>' +
            '<div class="ai-orientation">' + orientationHtml + '</div>' +
            '<div class="ai-section-title">Consigne libre (optionnel)</div>' +
            '<textarea class="ai-guidance" placeholder="Ex : « Ton plus direct, pas de paternalisme »"></textarea>' +
            '<div class="ai-actions">' +
                '<button type="button" class="ai-btn ai-btn-secondary ai-cancel">Fermer</button>' +
                '<button type="button" class="ai-btn ai-btn-primary ai-generate">Générer avec IA</button>' +
            '</div>' +
            '<div class="ai-status" style="display:none"></div>' +
            '<div class="ai-proposals"></div>' +
        '</div>';
    document.body.appendChild(ov);

    function closeModal() {{ if (ov.parentNode) ov.parentNode.removeChild(ov); }}

    ov.querySelector(".ai-cancel").addEventListener("click", closeModal);
    ov.addEventListener("click", function(e) {{ if (e.target === ov) closeModal(); }});

    ov.querySelectorAll(".ai-ori-minus, .ai-ori-plus").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            var skill = this.dataset.skill;
            var hidden = ov.querySelector('.ai-ori[data-skill="' + skill + '"]');
            var valueEl = ov.querySelector('.ai-ori-value[data-skill="' + skill + '"]');
            if (!hidden || !valueEl) return;
            var v = parseInt(hidden.value) || 0;
            v += this.classList.contains("ai-ori-plus") ? 1 : -1;
            if (v < -3) v = -3;
            if (v > 3) v = 3;
            hidden.value = String(v);
            valueEl.textContent = (v > 0 ? "+" : "") + String(v);
        }});
    }});

    ov.querySelector(".ai-generate").addEventListener("click", function() {{
        var genBtn = this;
        var statusEl = ov.querySelector(".ai-status");
        var proposalsEl = ov.querySelector(".ai-proposals");
        proposalsEl.innerHTML = "";

        var orientation = {{}};
        ov.querySelectorAll(".ai-ori").forEach(function(inp) {{
            var v = parseInt(inp.value, 10);
            if (!isNaN(v) && v !== 0) orientation[inp.dataset.skill] = v;
        }});
        var guidance = (ov.querySelector(".ai-guidance").value || "").trim();
        var nextSelect = ov.querySelector(".ai-next");
        var nextId = nextSelect ? parseInt(nextSelect.value, 10) : -1;
        if (isNaN(nextId)) nextId = -1;

        var payload = {{
            book_slug: bookSlug,
            chapter_id: parseInt(chapterId, 10),
            scene_id: sc.Id,
            interaction_id: ia.Id,
            orientation: orientation,
            guidance: guidance,
            n: 1,
            next_interaction_id: nextId
        }};

        genBtn.disabled = true;
        statusEl.style.display = "block";
        statusEl.className = "ai-status loading";
        statusEl.textContent = "Appel du LLM en cours… (cela peut prendre quelques secondes)";

        fetch("/api/enrich", {{
            method: "POST",
            headers: {{ "Content-Type": "application/json" }},
            body: JSON.stringify(payload)
        }}).then(function(r) {{ return r.json().then(function(d) {{ return {{ ok: r.ok, data: d }}; }}); }})
        .then(function(result) {{
            genBtn.disabled = false;
            if (!result.ok) {{
                statusEl.className = "ai-status err";
                statusEl.textContent = (result.data && result.data.error) ? result.data.error : "Erreur lors de l'appel IA.";
                return;
            }}
            var proposals = (result.data && result.data.proposals) || [];
            if (proposals.length === 0) {{
                statusEl.className = "ai-status err";
                statusEl.textContent = "Aucune proposition (tout a été filtré comme doublon ?).";
                return;
            }}
            statusEl.style.display = "none";
            proposals.forEach(function(p, pIdx) {{
                var card = document.createElement("div");
                card.innerHTML = renderAiProposalCard(p);
                var node = card.firstChild;
                proposalsEl.appendChild(node);
                node.querySelector(".ai-accept").addEventListener("click", function() {{
                    acceptAiProposal(sceneIdx, iIdx, p, nextId);
                    closeModal();
                }});
            }});
        }}).catch(function(err) {{
            genBtn.disabled = false;
            statusEl.className = "ai-status err";
            statusEl.textContent = "Erreur réseau. Vérifiez que `python app.py` est lancé.";
        }});
    }});
}}

function acceptAiProposal(sceneIdx, iIdx, proposal, nextInteractionId) {{
    var chapter = chaptersData.Chapters[0];
    if (!chapter || !chapter.Scenes || !chapter.Scenes[sceneIdx]) return;
    var sc = chapter.Scenes[sceneIdx];
    var ia = sc.Interactions[iIdx];
    if (!ia) return;
    if (!ia.Responses) ia.Responses = [];
    var newRespId = getNextResponseId(ia);
    var dims = proposal.SoftSkillDimensions || {{}};
    var nextId = (nextInteractionId == null || isNaN(parseInt(nextInteractionId, 10))) ? -1 : parseInt(nextInteractionId, 10);
    var newResp = {{
        Id: newRespId,
        Name: (proposal.Text || "").substring(0, 80),
        Text: proposal.Text || "",
        NextInteractionID: nextId,
        Category: proposal.Category || "neutre",
        Rationale: proposal.Rationale || "",
        GeneratedByAI: true,
        SoftSkillDimensions: {{}},
        LegacyDimensions: proposal.LegacyDimensions || {{}}
    }};
    SCORE_SKILLS.forEach(function(sk) {{
        var v = parseInt(dims[sk], 10);
        if (isNaN(v)) v = 0;
        if (v < -3) v = -3;
        if (v > 3) v = 3;
        newResp[sk] = v;
        newResp.SoftSkillDimensions[sk] = v;
    }});
    ia.Responses.push(newResp);
    scheduleCacheSave();
    rebuildEditorHtml(sceneIdx);
    rebuildSceneGraph(sceneIdx);
    showOnlySelectedBlock(String(ia.Id));
    var block = document.querySelector('.block[data-interaction-id="' + ia.Id + '"]');
    if (block) block.scrollIntoView({{ behavior: "smooth", block: "start" }});
}}

function attachCrudHandlers(idx) {{
    document.querySelectorAll("#ed-content .crud-add-interaction").forEach(function(btn) {{
        btn.addEventListener("click", function() {{ addInteraction(idx); }});
    }});
    document.querySelectorAll("#ed-content .crud-add-response").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            addResponse(idx, parseInt(this.dataset.i));
        }});
    }});
    document.querySelectorAll("#ed-content .crud-delete-interaction").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            deleteInteraction(idx, parseInt(this.dataset.i));
        }});
    }});
    document.querySelectorAll("#ed-content .crud-delete-response").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            deleteResponse(idx, parseInt(this.dataset.i), parseInt(this.dataset.r));
        }});
    }});
    document.querySelectorAll("#ed-content .crud-ai-response").forEach(function(btn) {{
        btn.addEventListener("click", function() {{
            openAiProposalModal(idx, parseInt(this.dataset.i));
        }});
    }});
}}

function init() {{
    if (typeof vis === "undefined") {{
        container.innerHTML = "<p style='color:#ef4444;padding:20px'>vis-network non chargé. Vérifiez votre connexion et rechargez.</p>";
        return;
    }}
    restoreCacheFromLocalStorage();
    applyPanelVisibility();
    if (scenesData && scenesData.length > 0) {{
        if (currentSceneIdx < 0 || currentSceneIdx >= scenesData.length) currentSceneIdx = 0;
        try {{
            showScene(currentSceneIdx);
            setMode(currentMode);
        }} catch (err) {{
            console.error("showScene:", err);
            container.innerHTML = "<p style='color:#ef4444;padding:20px'>Erreur: " + String(err.message || err) + "</p>";
        }}
    }} else {{
        document.getElementById("ed-content").innerHTML = "<div class='empty'>Aucune donnée (erreur de chargement?).</div>";
    }}
}}
function runInit() {{
    if (typeof vis !== "undefined") {{ init(); return; }}
    var n = 0;
    var t = setInterval(function() {{
        n++;
        if (typeof vis !== "undefined") {{ clearInterval(t); init(); }}
        else if (n > 60) {{ clearInterval(t); container.innerHTML = "<p style='color:#ef4444;padding:20px'>vis-network timeout.</p>"; }}
    }}, 100);
}}
window.addEventListener("load", function() {{ setTimeout(runInit, 80); }});
</script>
</body>
</html>
'''


def generate_book(book: dict) -> dict:
    """
    Génère les pages HTML d'un livre dans output/graphes/<slug>/.
    Retourne un résumé (nb de chapitres/scènes/interactions + 1er chapitre)
    utilisable par la page de garde.
    """
    book_slug = book["slug"]
    book_output_dir = os.path.join(OUTPUT_DIR, book_slug)
    os.makedirs(book_output_dir, exist_ok=True)

    json_path = os.path.join(CHAPTERS_DIR, book["json"])
    data = load_chapters(json_path)

    links = []
    for ch in data.get("Chapters", []):
        chapter_id = ch["Id"]
        chapter_name = ch.get("Name", "")
        slug = _slug(chapter_name)
        filename = f"chapitre_{chapter_id}_{slug}.html"
        links.append({"id": chapter_id, "name": chapter_name, "filename": filename})

    total_scenes = 0
    total_interactions = 0
    for ch in data.get("Chapters", []):
        chapter_id = ch["Id"]
        chapter_name = ch.get("Name", "")
        scenes_data = []
        for scene in ch.get("Scenes", []):
            scenes_data.append(build_scene_graph(chapter_id, scene))
            total_scenes += 1
            total_interactions += len(scene.get("Interactions", []))

        slug = _slug(chapter_name)
        filename = f"chapitre_{chapter_id}_{slug}.html"
        filepath = os.path.join(book_output_dir, filename)
        html = render_html(ch, scenes_data, links, filename, book)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Généré : {filepath}")

    book_index_html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8"><title>{_html_escape(book["title"])} — Chapitres</title>
<style>
body{{font-family:system-ui,sans-serif;padding:32px;background:#0f0f14;color:#e4e4e7;margin:0}}
h1{{color:#38bdf8;margin:0 0 6px}} .sub{{color:#a1a1aa;margin:0 0 24px}}
a.back{{color:#a1a1aa;text-decoration:none;font-size:13px;display:inline-block;margin-bottom:16px;padding:4px 10px;border:1px solid #3f3f46;border-radius:6px}}
a.back:hover{{color:#fff;border-color:#38bdf8}}
ul{{list-style:none;padding:0;margin:0}}
li a{{display:block;padding:14px 16px;margin-bottom:8px;background:#18181b;border:1px solid #27272a;border-radius:10px;color:#e4e4e7;text-decoration:none}}
li a:hover{{border-color:#38bdf8;background:#1e293b}}
</style></head>
<body>
<a class="back" href="../index.html">← Page d'accueil</a>
<h1>{_html_escape(book["title"])}</h1>
<p class="sub">{_html_escape(book["subtitle"])}</p>
<ul>
"""
    for item in links:
        book_index_html += (
            f'<li><a href="{_html_escape(item["filename"])}">'
            f'Chapitre {item["id"]} — {_html_escape(item["name"])}</a></li>\n'
        )
    book_index_html += "</ul></body></html>"
    with open(os.path.join(book_output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(book_index_html)

    return {
        "book": book,
        "n_chapters": len(links),
        "n_scenes": total_scenes,
        "n_interactions": total_interactions,
        "first_chapter_filename": links[0]["filename"] if links else None,
    }


def render_landing_page(summaries: list[dict]) -> str:
    """Génère la page de garde avec une carte par livre."""
    cards = ""
    for s in summaries:
        b = s["book"]
        first = s["first_chapter_filename"] or "index.html"
        href = f'{b["slug"]}/{first}'
        cards += f'''
<a class="book-card book-card-{b["slug"]}" href="{_html_escape(href)}">
  <div class="card-header">
    <span class="card-tag">Livre</span>
    <h2>{_html_escape(b["title"])}</h2>
    <p class="card-subtitle">{_html_escape(b["subtitle"])}</p>
  </div>
  <p class="card-desc">{_html_escape(b["description"])}</p>
  <div class="card-meta">
    <span class="meta-audience">{_html_escape(b["audience"])}</span>
  </div>
  <div class="card-stats">
    <div><span class="n">{s["n_chapters"]}</span><span class="l">chapitres</span></div>
    <div><span class="n">{s["n_scenes"]}</span><span class="l">scènes</span></div>
    <div><span class="n">{s["n_interactions"]}</span><span class="l">interactions</span></div>
  </div>
  <div class="card-cta">Ouvrir le graphe →</div>
</a>'''

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>End of Life — Serious games pour la formation en santé</title>
<style>
* {{ box-sizing: border-box; }}
body {{
    margin: 0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: radial-gradient(ellipse at top, #1e1b4b 0%, #0f0f14 55%, #000 100%);
    color: #e4e4e7; min-height: 100vh; -webkit-font-smoothing: antialiased;
}}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 64px 28px 80px; }}
header {{ text-align: center; margin-bottom: 56px; }}
.eyebrow {{
    display: inline-block; padding: 6px 14px; border-radius: 999px;
    background: rgba(56,189,248,0.12); color: #7dd3fc; border: 1px solid rgba(56,189,248,0.35);
    font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 600;
    margin-bottom: 22px;
}}
h1 {{
    margin: 0 0 14px; font-size: 52px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.05;
    background: linear-gradient(120deg, #38bdf8 0%, #a855f7 60%, #f472b6 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}}
.tagline {{ max-width: 760px; margin: 0 auto; color: #a1a1aa; font-size: 17px; line-height: 1.55; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 22px; }}
.book-card {{
    display: flex; flex-direction: column; gap: 14px;
    text-decoration: none; color: #e4e4e7;
    background: linear-gradient(180deg, rgba(24,24,27,0.92), rgba(15,15,20,0.92));
    border: 1px solid #27272a; border-radius: 18px; padding: 26px 24px;
    transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;
}}
.book-card:hover {{
    transform: translateY(-3px); border-color: #38bdf8;
    box-shadow: 0 20px 60px -20px rgba(56,189,248,0.35);
}}
.book-card-medstudents_y2:hover {{
    border-color: #a855f7; box-shadow: 0 20px 60px -20px rgba(168,85,247,0.45);
}}
.card-header h2 {{
    margin: 6px 0 4px; font-size: 26px; font-weight: 700;
    background: linear-gradient(90deg, #38bdf8, #a855f7);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}}
.book-card-medstudents_y2 .card-header h2 {{
    background: linear-gradient(90deg, #a855f7, #f472b6);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}}
.card-tag {{
    display: inline-block; font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase;
    color: #a1a1aa; padding: 3px 8px; border: 1px solid #3f3f46; border-radius: 6px;
}}
.card-subtitle {{ margin: 0; color: #cbd5e1; font-size: 13px; font-weight: 500; }}
.card-desc {{ margin: 0; color: #a1a1aa; line-height: 1.55; font-size: 14px; }}
.card-meta {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.meta-audience {{
    font-size: 11px; color: #fde68a; background: rgba(253,230,138,0.08);
    border: 1px solid rgba(253,230,138,0.25); padding: 4px 10px; border-radius: 999px;
}}
.card-stats {{
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;
    padding: 14px 10px; background: rgba(39,39,42,0.5);
    border: 1px solid #27272a; border-radius: 12px;
}}
.card-stats div {{ display: flex; flex-direction: column; align-items: center; gap: 2px; }}
.card-stats .n {{ font-size: 22px; font-weight: 700; color: #f9fafb; line-height: 1; }}
.card-stats .l {{ font-size: 10px; color: #71717a; text-transform: uppercase; letter-spacing: 0.08em; }}
.card-cta {{
    margin-top: auto; align-self: flex-start;
    background: #38bdf8; color: #0f0f14; padding: 10px 18px; border-radius: 10px;
    font-weight: 700; font-size: 13px; letter-spacing: 0.01em;
}}
.book-card-medstudents_y2 .card-cta {{ background: #a855f7; color: #fff; }}
footer {{
    margin-top: 60px; text-align: center; color: #52525b; font-size: 12px; line-height: 1.7;
}}
footer code {{ color: #a1a1aa; background: #18181b; padding: 2px 6px; border-radius: 4px; font-size: 11px; }}
@media (max-width: 640px) {{
    h1 {{ font-size: 38px; }}
    .wrap {{ padding: 44px 18px 60px; }}
}}
</style>
</head>
<body>
<div class="wrap">
    <header>
        <span class="eyebrow">Serious games · Éditeur graphique</span>
        <h1>End of Life — Atelier des scénarios</h1>
        <p class="tagline">
            Une plateforme d'édition et de visualisation des scénarios de simulation
            pédagogique. Chaque livre réunit plusieurs chapitres, scènes et interactions
            pour travailler les compétences relationnelles et éthiques en santé.
        </p>
    </header>
    <main class="cards">
        {cards}
    </main>
    <footer>
        Données JSON stockées dans <code>data/chapters/</code> · Sauvegarde via <code>/api/save</code> ·
        Enrichissement IA via <code>/api/enrich</code> (backend OpenAI ou Ollama local)
    </footer>
</div>
</body>
</html>
'''


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Nettoyage des anciens fichiers à plat (legacy) pour éviter la confusion.
    for fname in os.listdir(OUTPUT_DIR):
        fpath = os.path.join(OUTPUT_DIR, fname)
        if os.path.isfile(fpath) and fname.startswith("chapitre_") and fname.endswith(".html"):
            try:
                os.remove(fpath)
            except OSError:
                pass

    summaries = []
    for book in BOOKS:
        summary = generate_book(book)
        summaries.append(summary)

    landing_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(landing_path, "w", encoding="utf-8") as f:
        f.write(render_landing_page(summaries))
    print(f"Page de garde : {landing_path}")


if __name__ == "__main__":
    main()
