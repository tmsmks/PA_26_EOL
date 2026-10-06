# -*- coding: utf-8 -*-
"""
Script oral (notes orateur) — PA 2026 / MSE HES-SO — Thomas Maksimous
Document PDF separe du .pptx, aligne sur le deck minimaliste de 20 slides.
Les slides ne portent que des appuis visuels : tout le discours est ici.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                Table, TableStyle, KeepTogether)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

NAVY = HexColor("#12284C"); BLUE = HexColor("#0069B4")
INK = HexColor("#26333F"); MUTED = HexColor("#8A97A4"); LINE = HexColor("#D6E1EC")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Title"], fontName="Helvetica-Bold",
                    fontSize=22, textColor=NAVY, spaceAfter=4, alignment=TA_LEFT, leading=26)
SUB = ParagraphStyle("SUB", fontName="Helvetica", fontSize=11.5, textColor=INK, spaceAfter=2, leading=15)
META = ParagraphStyle("META", fontName="Helvetica", fontSize=9.5, textColor=MUTED, leading=13)
EYE = ParagraphStyle("EYE", fontName="Helvetica-Bold", fontSize=8, textColor=MUTED, leading=11)
SH = ParagraphStyle("SH", fontName="Helvetica-Bold", fontSize=14, textColor=NAVY, leading=18, spaceAfter=2)
DUR = ParagraphStyle("DUR", fontName="Helvetica-Bold", fontSize=9, textColor=BLUE, leading=12, alignment=2)
BODY = ParagraphStyle("BODY", fontName="Helvetica", fontSize=10.5, textColor=INK, leading=15.5,
                      alignment=TA_JUSTIFY, spaceAfter=5)
TRANS = ParagraphStyle("TRANS", fontName="Helvetica-Oblique", fontSize=10, textColor=BLUE,
                       leading=14, spaceBefore=2, leftIndent=10)
NOTE = ParagraphStyle("NOTE", fontName="Helvetica-Oblique", fontSize=9.5, textColor=MUTED, leading=13)

# (numero, duree, eyebrow, titre slide, [paragraphes a dire], transition)
S = [
("1", "~30 s", "PAGE DE TITRE", "Accueil & cadrage",
 ["Bonjour à toutes et à tous, merci de votre présence. Je m'appelle Thomas Maksimous et je vous "
  "présente mon projet d'approfondissement du Master MSE HES-SO : un livre interactif destiné au "
  "personnel médical qui accompagne les patients en fin de vie, autour du storytelling et de la "
  "cohérence des soft-skills assistés par l'IA.",
  "C'est une collaboration entre la HES-SO, le CHUV et l'Université de Lausanne, sous la supervision "
  "du Prof. Stéphane Gobron et avec l'expertise clinique de la Dre Claudia Gamondi."],
 "→ Pour comprendre d'où vient ce projet, revenons trois ans en arrière."),

("2", "~55 s", "INTRODUCTION", "Un mois en EHPAD",
 ["Il y a trois ans, j'ai eu la chance de travailler un mois dans un EHPAD, auprès de patients "
  "atteints d'Alzheimer. Et honnêtement, je ne savais pas comment m'y prendre : comment parler, "
  "comment réagir.",
  "Des personnes qui refusaient de répondre, d'autres en colère sans raison, une patiente qui me "
  "prenait pour son fils. Aucune de ces situations n'était dans le manuel. C'est là que ce sujet "
  "m'a profondément intéressé."],
 "→ Première prise de conscience : la nature même de ces compétences."),

("3", "~50 s", "INTRODUCTION", "Soft-skills la vraie difficulté",
 ["En soins palliatifs, les soins moraux — les soft-skills — sont souvent plus durs à maîtriser que "
  "les soins techniques, les hard-skills.",
  "Les hard-skills s'apprennent à l'école, par cœur : c'est factuel. Les soft-skills, eux, ne "
  "s'apprennent pas par cœur, varient selon chaque patient et demandent une forte adaptation : "
  "c'est une véritable boîte noire."],
 "→ Pour structurer cela, le modèle des 3 S."),

("4", "~40 s", "INTRODUCTION", "Du savoir-être aux soft-skills",
 ["Sur les 3 S — savoir-faire, savoir-vivre, savoir-être — le savoir-faire correspond aux "
  "hard-skills, le factuel ; et le savoir-être, bien plus complexe, correspond aux soft-skills."],
 "→ Ces soft-skills, nous les appelons les SOSK."),

("5", "~35 s", "INTRODUCTION", "Les 7 SOSK",
 ["Les SOSK sont les sept compétences relationnelles servant de base au scoring : respect et "
  "dignité, empathie, compassion, régulation émotionnelle, clarté de communication, frontières "
  "professionnelles et collaboration interprofessionnelle. Chacune est notée de -3 à +3. Gardez-les "
  "en tête, on les retrouve partout."],
 "→ Reste à savoir comment les entraîner à grande échelle."),

("6", "~50 s", "CONTEXTE", "Former sans terrain à risque",
 ["Le projet vise le personnel nouvellement formé : jeunes diplômés, débutants en soins palliatifs "
  "— d'où la présence de l'UniL et de sa Faculté de médecine.",
  "On entraîne classiquement ces compétences par des jeux de rôle : efficaces mais chronophages et "
  "difficiles à mettre à l'échelle. D'où le besoin d'un environnement interactif et sûr, pour "
  "s'exercer avant le réel. Trois expertises se réunissent : HES-SO, CHUV et UniL."],
 "→ Avant de construire, voyons ce qui existe déjà."),

("7", "~60 s", "ÉTAT DE L'ART", "Trois approches incomplètes",
 ["Trois approches proches de la nôtre. LDR, un serious game de répétition sécurisée en soins "
  "palliatifs : efficace, mais figé, sans éditeur, sans scoring soft-skills, sans IA. Twine et les "
  "récits dont vous êtes le héros : excellente édition en graphe, mais générique et sans IA. PERCS, "
  "une référence d'entraînement aux soft-skills validée sur douze ans, mais présentielle et "
  "chronophage.",
  "Chacune excelle sur un axe. Notre projet les combine et y ajoute l'IA."],
 "→ Le quatrième repère, c'est notre propre historique."),

("8", "~40 s", "ÉTAT DE L'ART", "De V1 à la V3",
 ["La V1 : les histoires et les SOSK — cinq définis, trois utilisés — au format texte. La V2, le jeu "
  "End of Life : immersion 3D avec Unity et des avatars MetaHuman, mais contenu figé en JSON et "
  "scoring limité à trois axes. La V3, que nous présentons, lève ces limites."],
 "→ Voici donc cette solution."),

("9", "~40 s", "SOLUTION", "Deux verrous levés",
 ["La V3 lève deux verrous. D'abord l'accessibilité : une interface d'administration en graphe pour "
  "créer et modifier les scénarios sans programmer. Ensuite l'évaluation : un module d'IA qui assiste "
  "la génération orientée soft-skills et le scoring. Et un principe : human-in-the-loop, aucune "
  "proposition de l'IA n'entre sans validation humaine."],
 "→ Entrons dans le développement."),

("10", "~45 s", "DÉVELOPPEMENT", "Le scénario devient un graphe",
 ["Le scénario s'organise en chapitres, scènes, interactions et réponses. Cela se prête à un graphe "
  "orienté : chaque interaction devient un nœud, chaque réponse une arête. Le champ NextInteractionID "
  "relie les nœuds, et -1 marque une fin de branche. Plusieurs onglets et options de lecture rendent "
  "visibles les embranchements et les incohérences."],
 "→ Un éditeur, oui, mais des histoires qui restent cohérentes."),

("11", "~40 s", "DÉVELOPPEMENT", "Des histoires cohérentes",
 ["La validation EG-7 vérifie que chaque réponse pointe vers une cible valide, et signale les "
  "branches cassées. La sauvegarde atomique évite toute corruption du JSON. Le mode parcours joueur "
  "permet de rejouer une branche et de voir les scores cumulés, sans relancer Unity. Le round-trip "
  "JSON garantit la compatibilité avec le moteur existant."],
 "→ Venons-en au cœur du projet, l'IA."),

("12", "~50 s", "DÉVELOPPEMENT", "Créer et scorer par IA",
 ["La génération orientée : l'auteur fixe une cible de -3 à +3 sur les sept SOSK, plus une consigne "
  "libre, et l'IA propose des réponses cohérentes avec la branche. Le scoring assisté : l'IA propose "
  "sept scores avec une justification explicable. Le tout repose sur un pattern Strategy — backend "
  "OpenAI distant ou Ollama local — et reste sous validation humaine."],
 "→ Tout cela a été mesuré."),

("13", "~35 s", "RÉSULTATS", "Conformité parfaite",
 ["Sur une campagne de cinquante générations orientées avec OpenAI, cent pour cent de conformité, "
  "sans aucun échec de format. À cela s'ajoutent vingt-sept tests automatisés qui passent et deux "
  "livres réels de 438 interactions validés par round-trip JSON."],
 "→ Et le scoring ?"),

("14", "~50 s", "RÉSULTATS", "Scoring proche de l'humain",
 ["Le scoring assisté obtient une MAE globale de 0,77 sur sept niveaux. Les dimensions les plus "
  "explicites sont les mieux prédites — la collaboration interprofessionnelle à 0,13 — tandis que "
  "les plus subjectives, l'empathie et la compassion, restent les plus difficiles, autour de 1,1 à "
  "1,3. C'est cohérent avec la littérature, et la référence vient d'un seul annotateur."],
 "→ Reste le choix du backend."),

("15", "~45 s", "RÉSULTATS", "Cloud rapide ou local privé",
 ["OpenAI atteint 100 % de conformité en 9 secondes ; Ollama 91 % mais en 98 secondes, en local. Le "
  "choix dépend de la priorité : OpenAI pour la rapidité et la qualité, Ollama pour l'exécution "
  "locale et la confidentialité RGPD. J'y reviens en discussion."],
 "→ Plutôt qu'un discours, voyons-le en direct."),

("16", "~live", "DÉMONSTRATION", "Démonstration live",
 ["Démonstration en direct : je charge un livre, je navigue dans le graphe et ses onglets, j'édite "
  "une réponse et je valide les références EG-7, je lance le mode parcours joueur, puis je génère une "
  "réponse orientée SOSK avec l'IA et j'observe le scoring assisté et sa justification.",
  "[Filet de sécurité : des captures de secours sont prêtes en cas de souci technique.]"],
 "→ Prenons maintenant du recul, avec un regard critique."),

("17", "~45 s", "DISCUSSION", "Parmi les moins chers",
 ["Sur le choix du modèle : gpt-4.1-mini est un très bon compromis qualité-prix. Si on compare tous "
  "les modèles connus, du moins cher — Llama local, DeepSeek, gpt-4o-mini — au plus cher — Gemini "
  "Pro, Claude Sonnet, GPT-5.5 — notre choix se situe dans le bas de la grille, tout en gardant "
  "100 % de conformité. À l'échelle d'un hôpital, le vrai enjeu n'est pas le coût du token, mais le "
  "passage à l'échelle et la conformité des données."],
 "→ Ce qui m'amène au RGPD et à l'éthique."),

("18", "~50 s", "DISCUSSION", "Données et responsabilité",
 ["OpenAI, serveur externe : rapide et performant, mais les données quittent l'hôpital — acceptable "
  "pour des scénarios fictifs. Ollama, serveur local : les données restent sur place, indispensable "
  "le jour où l'on manipulera de vraies données patients. Le pattern Strategy permet de basculer de "
  "l'un à l'autre sans toucher au code.",
  "J'assume les limites : pas encore de test utilisateur formel, une référence à un seul annotateur, "
  "et une IA qui ne lit que le texte. Elle assiste, l'humain reste responsable."],
 "→ Concluons."),

("19", "~55 s", "CONCLUSION", "Bilan et perspectives",
 ["Ce projet transforme un jeu sérieux figé en plateforme éditable. Trois acquis : une interface en "
  "graphe pour éditer sans programmer ; un module IA de génération orientée et de scoring explicable, "
  "sous validation humaine ; et une architecture durable, Clean Architecture, 27 tests, double "
  "backend.",
  "Les perspectives constitueront mon travail de Master : un scoring dynamique côté joueur en temps "
  "réel pour un vrai tuteur intelligent, et un modèle de machine learning local fine-tuné sur des "
  "données internes du CHUV, déployé via Ollama, pour combiner performance et conformité RGPD."],
 "→ Je termine."),

("20", "~10 s", "PAGE DE CLÔTURE", "Merci & questions",
 ["Merci de votre attention, je suis à votre disposition pour vos questions."],
 None),
]

def slide_block(n, dur, eye, title, says, trans):
    flow = []
    head = Table([[Paragraph(eye, EYE), Paragraph(dur, DUR)]], colWidths=[13.2*cm, 3.2*cm])
    head.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                              ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                              ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    flow.append(head)
    flow.append(Paragraph(f'<font color="#0069B4">{n} ·</font> {title}', SH))
    flow.append(Spacer(1, 3))
    for p in says:
        flow.append(Paragraph(p, BODY))
    if trans:
        flow.append(Paragraph(trans, TRANS))
    flow.append(Spacer(1, 7))
    flow.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=2, spaceAfter=9))
    return [KeepTogether(flow[:4])] + flow[4:]

def build():
    out = "/Users/thomaks/DEV/PA_26_EOL/output/PA_2026_EOL_script_oral_v3.pdf"
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=2.2*cm, rightMargin=2.2*cm,
                            topMargin=1.9*cm, bottomMargin=1.7*cm,
                            title="Script oral — PA 2026 EOL", author="Thomas Maksimous")
    story = [
        Paragraph("Script oral — déroulé de la présentation", H1),
        Paragraph("Livre interactif pour le personnel médical accompagnant les patients en fin de "
                  "vie · PA MSE HES-SO", SUB),
        Paragraph("Thomas Maksimous  ·  Lausanne, 16 juin 2026", META),
        Spacer(1, 6),
        Paragraph("Deck minimaliste de 20 slides : les diapositives ne portent que des appuis "
                  "visuels, tout le discours est ici. Durée de parole estimée ~14 min hors "
                  "démonstration ; viser ~20 min avec la démo. La slide 2 (storytelling EHPAD) est "
                  "le moment fort : prendre son temps, regarder le jury.", NOTE),
        HRFlowable(width="100%", thickness=1, color=NAVY, spaceBefore=10, spaceAfter=12),
    ]
    for (n, dur, eye, title, says, trans) in S:
        story.extend(slide_block(n, dur, eye, title, says, trans))
    doc.build(story)
    print("WROTE", out)

if __name__ == "__main__":
    build()
