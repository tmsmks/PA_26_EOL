"""Chapitre 4 — Hors script (février-mars).

Six scènes jouées, sept écrites :
  4.1 Le patient standardisé · 4.2 Hors script · 4.3 Le portfolio · 4.4 1 h 07
  4.5 branche parallèle : « La rééducation » (l'alerte a été rapide)
      ou « Vingt-trois minutes » (l'alerte a tardé)
  4.6 Les pieds qui ne savent plus
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 4.1 Le patient standardisé
# ---------------------------------------------------------------------------
S4_1 = S(1, "4.1 Le patient standardisé",
    "Début février. Centre de simulation, couloir des box de consultation. Chaque box a une "
    "vitre sans tain ; derrière, la table 14 observe, avec la Dre Chevalley. Aujourd'hui : "
    "anamnèse avec un patient standardisé. Sur la fiche : « M. Rossier, 63 ans, maux de "
    "tête ». En réalité, Bernard Gilliéron, 66 ans, ancien comédien, dix ans de patients "
    "simulés.",
    focus=("cc", "em", "rd"),
    nodes=[
        I(1, "chevalley", "neutral",
          "Avant d'entrer, la Dre Chevalley vous donne la consigne. « Quinze minutes. "
          "Anamnèse d'un mal de tête, pas d'examen. Bernard joue le patient, il ne sort jamais "
          "de son rôle. » Elle tapote la porte. « Une seule exception : si l'un de vous, ou "
          "lui, dit « Pause réelle », tout s'arrête. Ça veut dire : ce qui se passe n'est plus "
          "un exercice. Vous ne le direz sans doute jamais. Mais retenez-le. »", [
            R("« Pause réelle. Et dans ce cas, qui fait quoi ? »", 2, "cc2 ic2"),
            R("Noter « Pause réelle » en haut de votre feuille.", 2, "cc1"),
            R("« Ça arrive vraiment ? »", 3, "cc1 er1"),
            R("« On n'est pas à l'armée. »", 2, "ic-2 rd-1"),
            R("Hocher la tête distraitement, en relisant vos questions.", 2, "cc-1"),
        ]),
        I(2, "bernard", "neutral",
          "Box 4. Un homme d'une soixantaine d'années, veste en velours, lunettes au bout du "
          "nez, se masse les tempes. Il lève les yeux. Il est M. Rossier, maintenant, "
          "entièrement. « Bonjour… C'est vous, le docteur ? J'ai un mal de tête qui ne me "
          "lâche pas depuis trois semaines. »", [
            R("« Bonjour, Monsieur Rossier. Je suis Alex, étudiant·e en médecine. Je vais vous "
              "poser quelques questions pour le médecin. Racontez-moi ce mal de tête. »",
              4, "rd2 cc2 pb1"),
            R("Ouvrir la grille d'anamnèse sur la tablette : « Localisation ? Intensité, de 1 à "
              "10 ? »", 5, "cc-1 rd-1 em-1"),
            R("« Trois semaines ? Vous auriez dû venir plus tôt. »", 6, "rd-2 em-1"),
            R("« Oui, c'est moi, le docteur. »", 6, "pb-3 cc-1"),
            R("S'asseoir à sa hauteur, poser la tablette, et attendre qu'il continue.",
              4, "em2 rd2 cc1"),
        ]),
        I(3, "chevalley", "neutral",
          "« Deux fois en dix ans. Une fois, un étudiant qui a fait un malaise. Une fois, une "
          "patiente simulée qui a appris en pleine station que sa sœur venait d'avoir un "
          "accident. » Elle vous regarde. « Le script, c'est un outil. Pas une religion. »",
          [go(2)]),
        I(4, "bernard", "sad",
          "« Ça a commencé après le décès de ma femme. Enfin, non. Un peu avant. » Il se tait, "
          "regarde ses mains. « Le matin, surtout. Ça cogne derrière les yeux. Ma fille dit "
          "que c'est le chagrin. Moi, je ne sais pas. »", [
            R("« Votre femme est décédée… Je suis désolé·e. Vous voulez m'en dire un peu plus, "
              "sur ces dernières semaines ? »", 7, "em3 rd1 cc1"),
            R("« Le matin, derrière les yeux… Vous avez déjà fait contrôler votre "
              "tension ? »", 7, "cc2"),
            R("« Votre fille a sûrement raison. »", 7, "cc-2 em-1 pb-1"),
            R("Taper « deuil » dans la grille, et passer à la question suivante.",
              5, "em-2 rd-1"),
            R("« Ça cogne derrière les yeux, le matin. Et vous, qu'est-ce que vous craignez "
              "que ce soit ? »", 7, "cc3 em2"),
        ]),
        I(5, "bernard", "annoyed",
          "M. Rossier regarde la tablette, puis vous. « Sept. Partout. Je ne sais pas. » Il "
          "répond de plus en plus court. Au bout de dix minutes, vous avez rempli toutes les "
          "cases, et il ne vous a rien dit.", [
            R("Poser la tablette. « Pardon. Je vous ai interrogé comme un formulaire. Qu'est-ce "
              "qui vous inquiète, vous ? »", 7, "rd2 em2 er1 cc1"),
            R("Continuer la grille jusqu'au bout.", 8, "em-1 cc-1"),
            R("« Vous pourriez être un peu plus précis ? »", 8, "rd-1 em-1"),
            R("Regarder l'heure.", 8, "rd-1"),
        ]),
        I(6, "bernard", "cold-anger",
          "M. Rossier se redresse sur sa chaise. « Ah. » Pendant cinq minutes, il ne dit plus "
          "rien d'utile : il est devenu exactement le patient qu'on perd. Derrière la vitre, "
          "on entend presque la Dre Chevalley soupirer.", [
            R("« Excusez-moi. Je me suis mal présenté·e : je suis étudiant·e, pas médecin. Je "
              "suis là pour vous écouter. Je reprends ? »", 4, "pb2 rd2 er1"),
            R("Enchaîner les questions de la grille.", 8, "cc-1 em-1"),
            R("« Vous ne m'aidez pas beaucoup, Monsieur. »", 8, "rd-2 em-2"),
            R("Se taire, et attendre.", 4, "er1 em1"),
        ]),
        I(7, "bernard", "anxious",
          "« Ce que je crains ? » Il ôte ses lunettes. « Mon frère a fait une attaque à "
          "soixante-cinq ans. Il était devant la télé. Il a perdu la parole d'un coup, au "
          "milieu d'une phrase. » Il remet ses lunettes. « Et moi, le matin, j'ai l'impression "
          "que ma tête va éclater. »", [
            R("« Vous avez peur de faire une attaque, comme votre frère. Je comprends que ces "
              "maux de tête vous inquiètent. Je vais tout transmettre au médecin, y compris "
              "pour votre frère : c'est important. »", 9, "em2 cc3 rd1 ic1"),
            R("« Ça n'a sûrement rien à voir. »", 9, "cc-2 em-1 pb-1"),
            R("« Vous prenez un traitement pour la tension ? »", 9, "cc2 em-1"),
            R("« Une attaque, ça se voit sur le visage : vous n'avez rien de tout ça. »",
              9, "cc-1 pb-2"),
            R("Laisser un silence, puis : « Et vous en avez parlé à votre fille, de cette "
              "peur-là ? »", 9, "em3 cc1"),
        ]),
        I(8, "bernard", "neutral",
          "La sonnerie retentit. Bernard ôte ses lunettes, s'étire, et redevient Bernard : une "
          "voix plus grave, un accent vaudois qu'il cachait. « Bon. On débriefe ? » Il sort un "
          "petit carnet. « Vous m'avez regardé… » il compte « … trois fois. Votre tablette, "
          "quarante. Vous savez ce que ça fait, à un patient ? »", [
            R("« Que je ne vous écoutais pas. Vous avez raison. Qu'est-ce que j'aurais dû "
              "faire ? »", 10, "er2 rd2 cc1"),
            R("« La grille est obligatoire pour l'examen. »", 10, "er-1 ic-1"),
            R("« Vous êtes dur. C'est une simulation. »", 10, "er-2 rd-1"),
            R("Noter « contact visuel » dans votre carnet.", 10, "er1 cc1"),
        ]),
        I(9, "bernard", "happy",
          "La sonnerie retentit. Bernard ôte ses lunettes, s'étire, et redevient Bernard : une "
          "voix plus grave, un accent vaudois qu'il cachait. « Bon. On débriefe ? » Il sort un "
          "petit carnet. « Vous avez posé votre tablette. Vous m'avez laissé finir mes "
          "phrases. Quand j'ai parlé de mon frère, vous n'avez pas sauté dessus. » Il sourit. "
          "« Une chose : vous ne m'avez jamais demandé quels médicaments je prenais. Rossier "
          "en prend trois. »", [
            R("« C'est vrai. J'étais tellement dans l'écoute que j'en ai oublié la structure. "
              "Merci. »", 10, "er2 cc2"),
            R("« C'était dans la grille, je l'aurais fait à la fin. »", 10, "er-1 cc-1"),
            R("« Merci. Vous jouez incroyablement bien. »", 10, "rd1 er1"),
            R("« Et vous, Bernard, vous prenez des médicaments ? Vous avez l'air "
              "fatigué. »", 11, "pb-1 em1"),
        ]),
        I(10, "chevalley", "neutral",
          "Derrière la vitre, la Dre Chevalley reprend les points avec le groupe. Bernard "
          "remet sa veste de velours. En passant, il vous glisse : « La semaine prochaine, je "
          "rejoue M. Rossier, avec vous. Trois semaines plus tard dans sa vie. Il ira mieux, "
          "ou pas : ça dépendra de ce qu'on a fait de lui aujourd'hui. » Il cligne de l'œil."),
        I(11, "bernard", "neutral",
          "Bernard rit. « Moi ? Je suis en bois, comme les vieux chênes. » Il se masse la "
          "nuque, un instant, puis range son carnet. « Ma femme dit que je devrais faire "
          "contrôler ma tension. Ma femme dit beaucoup de choses. »", [go(10)]),
    ],
)

# ---------------------------------------------------------------------------
# 4.2 Hors script
# ---------------------------------------------------------------------------
_INTRO_42 = (
    "Une semaine plus tard. Box 4, deuxième station : « M. Rossier, trois semaines plus "
    "tard ». Les maux de tête continuent, il revient. Bernard est déjà dans son rôle, veste "
    "en velours, un verre d'eau à la main. Derrière la vitre : la Dre Chevalley, Maëlle, "
    "Noah, Léo, Yasmine."
)

S4_2 = S(2, "4.2 Hors script", _INTRO_42,
    focus=("er", "ic", "cc", "pb"),
    entries=[
        Entry(20, when(all=["leo_allie", "yasmine_alliee"]), _INTRO_42),
        Entry(30, when(all=["leo_allie"]), _INTRO_42),
        Entry(40, when(all=["yasmine_alliee"]), _INTRO_42),
    ],
    debriefs=[
        Debrief(when(all=["bernard_retard"]), tone="hard", lead=(
            "Les signes étaient ceux du manuel : la parole qui s'emmêle, la bouche qui tombe "
            "d'un côté, la main qui lâche, d'un coup. Pour un AVC, le temps, c'est du "
            "cerveau : on note l'heure du début, on appelle le 144, on ne donne rien à boire. "
            "Et en simulation, le mot d'arrêt existe pour ça : mieux vaut interrompre dix "
            "exercices pour rien que rater une seule vraie urgence.")),
        Debrief(when(all=["bernard_rapide"]), tone="good", lead=(
            "Vous êtes sorti·e du script à temps. Interrompre une simulation, c'est accepter "
            "de se tromper devant tout le monde ; c'est exactement ce qu'il fallait faire. "
            "L'heure de début que vous avez notée a permis la thrombolyse : c'est souvent la "
            "seule information que personne d'autre ne peut donner.")),
    ],
    nodes=[
        I(1, "bernard", "anxious",
          "« Bonjour, docteur. Toujours ce mal de tête. » Bernard joue parfaitement. À la "
          "sixième minute, au milieu d'une phrase sur sa fille, sa voix change. « Elle m'a "
          "dit… que je… dev… » Les mots s'emmêlent. Son verre lui glisse de la main droite et "
          "se renverse sur la table. Il le regarde, étonné. Le coin droit de sa bouche "
          "tombe.", [
            R("Se lever : « Pause réelle ! » Puis : « Bernard, vous m'entendez ? Souriez-moi. "
              "Levez les deux bras. » Et regarder l'heure : 14 h 06.", 2, "er3 cc2 ic2 pb1"),
            R("Continuer l'anamnèse : c'est sûrement le scénario, il joue un AVC.",
              3, "er-1 ic-2 pb-1"),
            R("Regarder vers la vitre, pour voir si les autres réagissent.", 4, "er-1 ic1"),
            R("« Monsieur Rossier, ça fait partie de votre histoire, ça ? »", 4, "cc1 er-1"),
            R("Éponger l'eau renversée, puis reprendre.", 3, "er-2 cc-1"),
        ]),
        I(2, "chevalley", "anxious",
          "La porte s'ouvre : la Dre Chevalley est déjà là, Yasmine derrière elle. « Qu'est-ce "
          "que vous voyez ? »", [
            R("« Il ne trouve plus ses mots, la bouche tombe à droite, il a lâché le verre de la "
              "main droite. Début à 14 h 06. Il faut appeler le 144 : AVC possible. »",
              5, "cc3 ic3 er2", sets=["bernard_rapide"]),
            R("« Je crois qu'il fait un malaise. »", 5, "cc-1 ic1", sets=["bernard_rapide"]),
            R("« Je ne sais pas, ça a commencé d'un coup. »", 5, "cc-1",
              sets=["bernard_rapide"]),
            R("« Il fait peut-être une hypoglycémie : on lui donne du sucre ? »",
              5, "cc-1 pb-2", sets=["bernard_rapide"]),
            R("L'allonger par terre, sans rien dire.", 5, "ic-1 cc-2",
              sets=["bernard_rapide"]),
        ]),
        I(3, "bernard", "confused",
          "Vous reprenez : « Et votre fille, elle vous a dit quoi ? » Bernard vous regarde. Il "
          "essaie de répondre. Ce qui sort n'est pas une phrase. Il lève la main gauche vers "
          "sa bouche, comme pour la remettre en place. Derrière la vitre, quelqu'un rit : « Il "
          "est trop fort. » Deux minutes ont passé. Peut-être trois.", [
            R("« Pause réelle ! » Se lever, et frapper à la vitre : « Il ne joue pas ! »",
              6, "er2 ic2 cc1"),
            R("« Prenez votre temps, Monsieur Rossier. »", 7, "er-1 em1 pb-1"),
            R("Rire nerveusement, en regardant la vitre.", 7, "er-2 rd-1"),
            R("Noter « aphasie (simulée) » dans la grille.", 7, "er-2 cc-1 pb-1"),
            R("« Vous voulez un verre d'eau ? »", 7, "pb-1 cc-1"),
        ]),
        I(4, "bernard", "confused",
          "Derrière la vitre, vous ne voyez que votre reflet. Bernard ne répond pas à votre "
          "question. Il fixe le verre renversé, puis vous. Sa main droite pend le long de la "
          "chaise. Il dit quelque chose qui ressemble à « pas… pas… » — « pas normal », "
          "peut-être.", [
            R("« Pause réelle ! » Puis à Bernard : « Souriez-moi. Levez les bras. » Et noter "
              "l'heure.", 2, "er2 cc2 ic2"),
            R("« Ça fait partie du scénario ? Hochez la tête si oui. »", 3, "cc1 er-1"),
            R("Attendre que la Dre Chevalley intervienne : c'est son centre.",
              7, "ic-2 er-1 pb-1"),
            R("Sortir chercher quelqu'un, en laissant Bernard seul sur sa chaise.",
              6, "ic1 pb-1 er-1"),
        ]),
        I(5, "narr", "",
          "La Dre Chevalley appelle le 144, haut-parleur allumé, et répète vos mots : heure de "
          "début, parole, bouche, bras. On apporte le chariot d'urgence. Bernard est allongé "
          "sur le côté, la tête un peu relevée. Les ambulanciers sont là en neuf minutes. Le "
          "dernier mot que Bernard arrive à dire, en vous regardant, ressemble à « merci ». Ou "
          "à « mercredi ». Personne ne sait.", [
            R("Rester à côté de lui jusqu'au départ de l'ambulance, et lui dire ce qui se "
              "passe.", 9, "em2 rd2 er1"),
            R("Retourner derrière la vitre.", 9, "er-1 em-1"),
            R("Chercher dans son sac le numéro de sa femme, pour la prévenir vous-même.",
              9, "pb-2 ic-1"),
            R("Raconter la scène aux autres, qui arrivent en courant.", 9, "pb-1 er-1"),
            R("Ramasser son carnet de feedback, tombé par terre, et le glisser dans la poche de "
              "sa veste.", 9, "rd2 em1"),
        ]),
        I(6, "chevalley", "anxious",
          "La Dre Chevalley entre en trois pas. Elle regarde Bernard, vous, le verre. "
          "« Qu'est-ce que vous avez vu, et depuis quand ? »", [
            R("« Depuis 14 h 06, à peu près : il ne trouve plus ses mots, la bouche tombe à "
              "droite, il a lâché son verre de la main droite. »", 5, "cc3 ic2 er1",
              sets=["bernard_rapide"]),
            R("« Quelques minutes. Je pensais qu'il jouait. »", 5, "cc1 er-1",
              sets=["bernard_rapide"]),
            R("« Je ne sais pas. »", 5, "cc-2", sets=["bernard_rapide"]),
            R("« C'est le scénario qui m'a induit·e en erreur. »", 5, "er-1 pb-1 ic-1",
              sets=["bernard_rapide"]),
        ]),
        I(7, "chevalley", "anxious",
          "Quinze minutes. La sonnerie de fin de station retentit. Bernard n'a pas bougé. Il "
          "vous regarde avec une sorte de colère muette. La Dre Chevalley entre pour le "
          "débriefing, le sourire aux lèvres, et s'arrête net. Elle voit la bouche, la main, le "
          "verre. « Bernard ? » Il ne répond pas. Elle se tourne vers vous : « Depuis "
          "quand ? »", [
            R("« Depuis la sixième minute. J'ai cru qu'il jouait. Je n'ai pas dit « Pause "
              "réelle ». »", 8, "pb3 cc2 er1", sets=["bernard_retard"]),
            R("« Je ne sais pas. »", 8, "cc-2 pb-2", sets=["bernard_retard"]),
            R("« Ça vient de commencer. »", 8, "pb-3 cc-3 rd-1", sets=["bernard_retard"]),
            R("« Derrière la vitre non plus, personne n'a rien vu ! »", 8, "pb-2 ic-2",
              sets=["bernard_retard"]),
            R("Se taire.", 8, "cc-2 er-1", sets=["bernard_retard"]),
        ]),
        I(8, "chevalley", "anxious",
          "La Dre Chevalley est déjà au téléphone avec le 144. « Début des symptômes il y a "
          "environ vingt minutes. » Elle s'agenouille près de Bernard. Derrière la vitre, "
          "personne ne rit plus. Les ambulanciers arrivent. En partant, l'un d'eux demande "
          "l'heure exacte du début. La Dre Chevalley vous regarde : c'est vous qui la "
          "savez.", [
            R("« 14 h 06. Exactement. »", 9, "cc3 pb2"),
            R("« Vers 14 h 20. »", 9, "pb-3 cc-3"),
            R("« Je ne sais pas exactement. Peut-être 14 h 10. »", 9, "cc-1 pb-1"),
            R("Se tourner vers Léo, qui chronométrait la station.", 9, "ic2 cc1"),
        ]),
        I(9, "chevalley", "sad",
          "Le box 4 est vide. Le verre est toujours renversé sur la table ; l'eau a séché en "
          "auréole. La Dre Chevalley s'assied sur la chaise de Bernard. « Pendant des années, "
          "on vous apprend à rester dans le script. On oublie de vous apprendre à en sortir. » "
          "Elle se frotte le visage. « Ce n'est pas votre faute, d'avoir cru. Ce sera la nôtre, "
          "si on n'en tire rien. »"),
        I(20, "bernard", "anxious",
          "« Bonjour, docteur. Toujours ce mal de tête. » À la sixième minute, au milieu d'une "
          "phrase, la voix de Bernard change. Les mots s'emmêlent. Son verre lui glisse de la "
          "main droite. Le coin droit de sa bouche tombe. Au même instant, on frappe à la "
          "vitre : Yasmine, les deux mains à plat sur le verre. Et la voix de Léo, dans "
          "l'interphone : « Alex. Das ist kein Theater. Ce n'est pas du théâtre. »", [
            R("« Pause réelle ! » Et à Bernard : « Souriez-moi. Levez les bras. » 14 h 06.",
              2, "er3 cc2 ic3"),
            R("« Yasmine, viens ! » Et commencer à examiner Bernard.", 2, "ic3 er2"),
            R("Hésiter : le scénario veut peut-être tester les étudiants.", 6, "er-1 ic-1"),
            R("Continuer l'anamnèse malgré tout.", 6, "er-2 ic-3"),
        ]),
        I(30, "bernard", "anxious",
          "« Bonjour, docteur. Toujours ce mal de tête. » À la sixième minute, au milieu d'une "
          "phrase, la voix de Bernard change. Les mots s'emmêlent. Son verre lui glisse de la "
          "main droite. Dans l'interphone, la voix de Léo, très calme : « Alex. Sa bouche. "
          "Regarde sa bouche. Das ist kein Theater. »", [
            R("« Pause réelle ! » Et à Bernard : « Souriez-moi. Levez les bras. » 14 h 06.",
              2, "er3 cc2 ic2"),
            R("« Léo, va chercher la Dre Chevalley ! » Et examiner Bernard.", 2, "ic3 er1 cc1"),
            R("« Léo, arrête : il joue. »", 3, "ic-2 er-1"),
            R("Continuer l'anamnèse.", 3, "er-2 ic-2"),
        ]),
        I(40, "bernard", "anxious",
          "« Bonjour, docteur. Toujours ce mal de tête. » À la sixième minute, au milieu d'une "
          "phrase, la voix de Bernard change. Les mots s'emmêlent. Son verre lui glisse de la "
          "main droite. Derrière la vitre, deux coups secs : Yasmine frappe le verre du plat de "
          "la main. Elle articule, sans le son : « A-V-C. »", [
            R("« Pause réelle ! » Et à Bernard : « Souriez-moi. Levez les bras. » 14 h 06.",
              2, "er3 cc2 ic2"),
            R("Lui faire signe d'entrer, et examiner Bernard ensemble.", 2, "ic3 er1"),
            R("Hausser les épaules vers la vitre : c'est le scénario.", 3, "ic-2 er-1"),
            R("Continuer l'anamnèse.", 3, "er-2 ic-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.3 Le portfolio
# ---------------------------------------------------------------------------
_INTRO_43 = (
    "Fin février. À la sortie du cours de neuroanatomie, Noah vous attend, livide. Il vous "
    "tend son téléphone : un mail de la commission d'intégrité. « Analyse de similarité — "
    "portfolio APP — convocation, 16 h, bureau du Pr Lambelet. »"
)
_INTRO_43_TEXTE = (
    "Fin février. Un mail de la commission d'intégrité, adressé à Noah et à vous : « Analyse "
    "de similarité — portfolio APP — convocation, 16 h, bureau du Pr Lambelet. » Le logiciel "
    "a retrouvé trois paragraphes de votre réflexion de portfolio, reformulés par une IA, "
    "dans celle de Noah."
)

S4_3 = S(3, "4.3 Le portfolio", _INTRO_43,
    focus=("pb", "ic", "er"),
    entries=[
        Entry(10, when(all=["texte_partage"]), _INTRO_43_TEXTE),
        Entry(14, when(all=["signature_noah"]), _INTRO_43),
    ],
    debriefs=[
        Debrief(when(all=["mensonge_portfolio"]), tone="hard", lead=(
            "Vous avez menti à la commission. La loyauté envers un camarade ne passe jamais "
            "par une fausse déclaration à l'institution : elle ajoute une faute à la sienne, "
            "et elle vous engage, vous. Être à côté de Noah, l'aider à réécrire, l'orienter "
            "vers de l'aide : c'était possible sans mentir.")),
        Debrief(when(all=["texte_partage"]), tone="mixed", lead=(
            "Vous avez dit la vérité. Mais votre texte était dans celui de Noah : prêter son "
            "travail personnel à quelqu'un qui est débordé, c'est rarement l'aider. Le plagiat "
            "et l'usage non déclaré d'une IA générative sont traités de la même manière, que "
            "l'on soit l'auteur·e ou la source.")),
        Debrief(when(all=["signature_noah"]), tone="mixed", lead=(
            "Vous avez dit la vérité sur le portfolio. La commission a aussi retrouvé la "
            "feuille de présence de septembre, signée de votre main pour Noah : un rappel à "
            "l'ordre pour vous aussi. Une signature de complaisance, même pour un ami qui va "
            "mal, est une fausse déclaration ; l'aider, c'était aller le chercher.")),
    ],
    nodes=[
        I(1, "noah", "anxious",
          "« Ils disent que mon texte est écrit par une IA. » Noah vous attrape le bras. "
          "« Viens avec moi. S'il te plaît. Dis que c'est toi qui m'as aidé à le "
          "reformuler. »", [
            R("« Je ne dirai pas ça, Noah, parce que ce n'est pas vrai. Mais je viens avec toi, "
              "et je reste à côté de toi. »", 2, "pb3 em2"),
            R("« D'accord. Je dirai que je t'ai aidé. »", 3, "pb-3 cc-2 ic-1",
              sets=["mensonge_portfolio"]),
            R("« T'as utilisé un chatbot ? Franchement, t'es pas malin. »", 4, "em-2 rd-1"),
            R("« Qu'est-ce qui s'est passé, exactement ? »", 5, "em2 cc1"),
            R("« Démerde-toi. »", 6, "em-3 co-2"),
        ]),
        I(2, "lambelet", "neutral",
          "Bureau du Pr Lambelet. Il fait entrer Noah, puis vous regarde. « Vous êtes ? — Un·e "
          "ami·e. — Entrez aussi, si M. Berthoud le souhaite. » Noah hoche la tête. Le "
          "Pr Lambelet pose un rapport sur la table. « Selon notre outil, votre réflexion de "
          "portfolio a été générée à 94 % par une intelligence artificielle. Monsieur Berthoud, "
          "je vous écoute. » Noah vous regarde.", [
            R("Ne rien dire : c'est à Noah de parler. Juste rester là, à côté de lui.",
              7, "pb2 em1 rd1"),
            R("« Il ne va pas bien en ce moment, monsieur. Il dort quatre heures par nuit. »",
              7, "pb-2 em1"),
            R("« C'est moi qui l'ai aidé à reformuler. »", 8, "pb-3 cc-3",
              sets=["mensonge_portfolio"]),
            R("Poser une main sur l'épaule de Noah.", 7, "em2 co1"),
            R("« Tout le monde utilise des IA, ce n'est pas si grave. »", 8, "pb-2 cc-1"),
        ]),
        I(3, "lambelet", "neutral",
          "Bureau du Pr Lambelet. Le rapport est sur la table : 94 % de texte généré par une "
          "IA. Noah dit, d'une voix blanche : « Alex m'a aidé à reformuler. » Le Pr Lambelet se "
          "tourne vers vous. « C'est exact ? Vous l'avez aidé à écrire ce texte ? »", [
            R("« Non. Je lui avais promis de le dire, et je ne peux pas. Je ne l'ai pas aidé. "
              "Pardon, Noah. »", 7, "pb3 cc2 er1", clears=["mensonge_portfolio"]),
            R("« Oui. »", 9, "pb-3 cc-3 rd-1"),
            R("« Un peu. »", 9, "pb-2 cc-2"),
            R("« Je préférerais ne pas répondre. »", 7, "pb-1 cc-2",
              clears=["mensonge_portfolio"]),
        ]),
        I(4, "noah", "hurt",
          "« Merci. Super utile. » Noah range son téléphone. « J'y vais seul. » Il s'éloigne "
          "vers l'ascenseur.", [
            R("Le rattraper : « Pardon. Je viens avec toi. Je ne mentirai pas pour toi, mais je "
              "serai là. »", 2, "em2 pb2 rd1"),
            R("Le laisser partir.", 6, "em-1"),
            R("« Bon courage ! »", 6, "em-1 co-1"),
            R("« Tu aurais dû y penser avant. »", 6, "em-2 rd-1"),
        ]),
        I(5, "noah", "ashamed",
          "« J'avais trois révisions en retard. Mon père m'appelait tous les soirs. J'ai "
          "demandé au chatbot de m'aider à « structurer ». Et puis j'ai tout copié. Il était "
          "trois heures du matin. » Il se passe la main sur le visage. « Je vais me faire "
          "virer. Mon père va me tuer. »", [
            R("« Tu ne vas pas te faire virer pour un portfolio, Noah. Dis-leur la vérité, comme "
              "tu viens de me la dire. Je t'accompagne. »", 2, "pb2 em2 cc1"),
            R("« Dis que c'est moi qui t'ai aidé, ça passera mieux. »", 3, "pb-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("« Ton père va surtout devoir t'écouter, pour une fois. »", 2, "em1 rd-1"),
            R("« Tu veux qu'on appelle d'abord la consultation psychologique ? »",
              2, "ic2 em1 pb1"),
        ]),
        I(6, "noah", "sad",
          "Noah va seul au bureau du Pr Lambelet. Le soir, il vous écrit : « avertissement. je "
          "dois réécrire le portfolio. ils préviennent le tuteur ». Puis : « merci pour "
          "rien ». Puis, à 1 h du matin : « désolé. je suis crevé ».", [
            R("« Pardon de t'avoir laissé seul. Demain, on réécrit ton portfolio ensemble — avec "
              "tes mots à toi. »", END, "em2 pb1 rd1", sets=["verite_portfolio"]),
            R("Ne pas répondre.", END, "em-2", sets=["verite_portfolio"]),
            R("« Un avertissement, c'est rien. Dors. »", END, "em1 cc-1",
              sets=["verite_portfolio"]),
            R("« Tu l'as un peu cherché, non ? »", END, "em-3 co-1",
              sets=["verite_portfolio"]),
        ]),
        I(7, "noah", "ashamed",
          "Noah prend une longue inspiration. « J'ai utilisé un chatbot. J'ai tout copié. Il "
          "était trois heures du matin, je n'avais pas dormi depuis deux jours. » Sa voix se "
          "casse. « Je suis désolé. » Le Pr Lambelet le regarde longtemps. « Merci de votre "
          "franchise. C'est plus rare que vous ne le croyez. »", [
            R("Rester silencieux·se, à côté de lui.", 11, "rd2 em1 pb1",
              sets=["verite_portfolio"]),
            R("« Il traverse une période très difficile. »", 11, "pb-1 em1",
              sets=["verite_portfolio"]),
            R("« Je l'avais prévenu. »", 11, "em-2 ic-1", sets=["verite_portfolio"]),
            R("Serrer le bras de Noah.", 11, "em2 co1", sets=["verite_portfolio"]),
        ]),
        I(8, "lambelet", "cold-anger",
          "Le Pr Lambelet pose son stylo. « Vous l'avez aidé à reformuler un texte rédigé à "
          "94 % par une IA ? Ou vous voulez dire que vous l'avez écrit à sa place ? » Noah "
          "fixe la table. Cette fois, il ne vous a rien demandé.", [
            R("« Ni l'un ni l'autre. Je voulais le protéger. Ce que j'ai dit est faux. "
              "Pardon. »", 7, "pb3 cc2 er1", clears=["mensonge_portfolio"]),
            R("« Je l'ai aidé. C'est tout ce que je peux dire. »", 9, "pb-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("« Je ne sais plus. »", 9, "cc-2 pb-1", sets=["mensonge_portfolio"]),
            R("« C'est une question de vocabulaire, monsieur. »", 9, "pb-2 rd-1",
              sets=["mensonge_portfolio"]),
        ]),
        I(9, "lambelet", "neutral",
          "Le Pr Lambelet note quelque chose. « Je vais demander vos deux portfolios et vos "
          "brouillons. Si votre version se confirme, vous serez tous les deux concernés par la "
          "procédure. » Il se lève. « Mon expérience, c'est que les versions qui protègent "
          "quelqu'un se confirment rarement. » Dans le couloir, Noah ne vous regarde pas. "
          "« Merci », dit-il, sans que vous sachiez s'il le pense.", [
            R("Retourner frapper à la porte : « Monsieur, je vous ai menti. Je ne l'ai pas "
              "aidé. »", 11, "pb3 cc2 er1", clears=["mensonge_portfolio"],
              sets=["verite_portfolio"]),
            R("« De rien. On est dans le même bateau, maintenant. »", 12, "pb-2 em1"),
            R("« Tu me dois une fière chandelle. »", 12, "pb-2 em-1"),
            R("« Il faudra que tu dises la vérité, Noah. Moi, je ne tiendrai pas ce "
              "mensonge. »", 12, "pb1 cc1 em1"),
            R("Partir, sans un mot.", 12, "er-1"),
        ]),
        I(10, "lambelet", "neutral",
          "Bureau du Pr Lambelet. Deux chaises. Sur la table, deux textes côte à côte, surlignés "
          "en jaune. « Expliquez-moi. » Noah ouvre la bouche, la referme. Il vous regarde.", [
            R("« Je lui ai envoyé mon texte quand il me l'a demandé. Je savais qu'il risquait de "
              "s'en servir. C'est une faute de ma part aussi. »", 7, "pb3 cc2 er1 ic1"),
            R("« Il me l'a volé sur mon ordinateur. »", 13, "pb-3 ic-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("« Je l'ai aidé à reformuler. »", 9, "pb-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("Se taire, et attendre que Noah parle.", 7, "pb-1 ic-1"),
            R("« On travaille ensemble : c'est normal que nos textes se ressemblent. »",
              9, "pb-2 cc-2", sets=["mensonge_portfolio"]),
        ]),
        I(11, "lambelet", "neutral",
          "Le Pr Lambelet referme le dossier. « Un avertissement pour le plagiat, et une "
          "nouvelle réflexion à rendre dans deux semaines. Écrite par vous, avec vos mots, même "
          "maladroits. » Il regarde Noah. « Et je vais vous donner le numéro de la consultation "
          "psychologique. Pas comme une sanction : comme le conseil d'un vieux qui a vu "
          "beaucoup d'étudiants ne pas dormir. » Dans le couloir, Noah s'appuie contre le mur. "
          "« Je crois que j'ai besoin de dormir une semaine. »"),
        I(12, "narr", "",
          "Deux semaines plus tard, la commission a comparé les brouillons, les historiques de "
          "versions, les dates. Vous recevez un avertissement pour fausse déclaration ; Noah, "
          "un second, pour le plagiat. Le Pr Lambelet a ajouté une ligne à la main : « La "
          "loyauté envers un camarade ne passe jamais par le mensonge à l'institution. »"),
        I(13, "noah", "hurt",
          "Noah tourne la tête vers vous, lentement. Il ne dit rien. Le Pr Lambelet : « Volé. "
          "Sur votre ordinateur. » Il note. « Monsieur Berthoud ? » Noah regarde la table. "
          "« Oui. Je l'ai pris. » Il ment pour vous, ou il ne se bat plus.", [
            R("« Non. C'est faux. Je le lui ai envoyé moi-même. Pardon, Noah. »",
              7, "pb3 cc2 er1", clears=["mensonge_portfolio"]),
            R("Se taire.", 12, "pb-2 em-2"),
            R("« Vous voyez. »", 12, "em-3 rd-2"),
            R("Sortir du bureau.", 12, "er-1 em-1"),
        ]),
        I(14, "noah", "anxious",
          "« Ils disent que mon portfolio est écrit par une IA. Et ils ont ressorti les "
          "feuilles de présence de la dissection : le 22 septembre, ma signature, c'est ton "
          "écriture. » Noah vous attrape le bras. « Dis que tu m'as aidé à reformuler, et pour "
          "la signature, on dira que tu t'es trompé·e de ligne. S'il te plaît. »", [
            R("« Je ne vais pas mentir, Noah. Ni pour le portfolio, ni pour la signature. Mais "
              "je viens avec toi, et je dirai ma part. »", 2, "pb3 em2 cc1"),
            R("« D'accord. On dit ça. »", 3, "pb-3 cc-2 ic-1", sets=["mensonge_portfolio"]),
            R("« Tu m'as mis dans la merde avec toi. »", 4, "em-2 ic-1"),
            R("« Qu'est-ce qui s'est passé, avec le portfolio ? »", 5, "em2 cc1"),
            R("« La signature, c'était pour te rendre service. Débrouille-toi avec le "
              "reste. »", 6, "em-2 pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.4 1 h 07
# ---------------------------------------------------------------------------
_INTRO_44 = (
    "Mi-mars, la veille de l'examen de neurosciences. 1 h 07. Votre téléphone vibre sur la "
    "table de nuit. Noah."
)

S4_4 = S(4, "4.4 1 h 07", _INTRO_44,
    focus=("em", "co", "er", "pb"),
    entries=[
        Entry(20, when(all=["promesse_noah"]), _INTRO_44),
        Entry(30, when(all=["noah_confie"]), _INTRO_44),
    ],
    debriefs=[
        Debrief(when(all=["noah_seul"]), tone="hard", lead=(
            "Quand quelqu'un dit qu'il veut « tout arrêter », la seule façon de savoir, c'est "
            "de poser la question directement : « Est-ce que tu penses au suicide ? » Poser la "
            "question ne donne pas l'idée ; elle ouvre la porte. Ensuite : ne pas laisser la "
            "personne seule, l'éloigner du danger, appeler de l'aide (144 en cas de danger "
            "immédiat, urgences psychiatriques, 143 La Main Tendue), et ne jamais promettre le "
            "secret. Noah est vivant. Ce n'est pas grâce à cette nuit.")),
        Debrief(when(all=["noah_aide"]), tone="good", lead=(
            "Vous avez pris au sérieux un message qu'on aurait pu lire comme de la fatigue. "
            "Demander directement, rester en ligne, éloigner Noah de la fenêtre, appeler de "
            "l'aide sans lui demander la permission : c'est ce qui sauve. Et vous n'avez pas "
            "porté ça seul·e — c'est aussi ce qui vous protège, vous.")),
    ],
    nodes=[
        I(1, "noah", "sad",
          "« t'es réveillé·e ? » Puis : « je crois que je vais tout arrêter ». Puis : "
          "« tout ». Puis plus rien. Noah est toujours en ligne.", [
            R("L'appeler, tout de suite.", 2, "em3 er1"),
            R("« Arrêter quoi ? La médecine ? »", 3, "em1 cc1"),
            R("« Dors, Noah. Ça ira mieux demain, après l'examen. »", 9, "em-3 co-2 cc-2"),
            R("« Arrête ton cinéma, il est 1 h du matin. »", 9, "em-3 rd-2 co-2"),
            R("« Noah, quand tu dis « tout », est-ce que tu penses à te tuer ? »",
              4, "cc3 em2 pb1"),
        ]),
        I(2, "noah", "sad",
          "Il décroche à la cinquième sonnerie. Il ne dit rien. Vous entendez sa respiration, "
          "et le bruit d'une fenêtre ouverte, la ville en bas. « J'ai raté. » Sa voix est très "
          "calme, trop calme. « L'examen, demain, je vais le rater. Mon père le saura avant "
          "midi. Je suis fatigué, Alex. Tellement fatigué. »", [
            R("« Noah, je t'entends. Je vais te poser une question directe : est-ce que tu "
              "penses à te suicider ? »", 4, "cc3 em2 er1"),
            R("« Tu ne vas pas rater, tu es le meilleur de la table. »", 5, "cc-1 em-1"),
            R("« Ferme la fenêtre, s'il te plaît. »", 6, "cc2 em1"),
            R("« On en parle demain, ok ? Repose-toi. »", 9, "em-3 co-2"),
            R("« Tu es où, exactement ? »", 6, "cc2 ic1"),
        ]),
        I(3, "noah", "sad",
          "« la médecine. tout » « je suis pas fait pour ça. je suis fait pour rien » « mon père "
          "le dira mieux que moi demain à midi ». Les trois messages arrivent coup sur coup.", [
            R("L'appeler, maintenant.", 2, "em3 er1"),
            R("« Quand tu dis « tout », tu penses à te tuer ? »", 4, "cc3 em2"),
            R("« Tu es fatigué, c'est tout. Dors. »", 9, "em-2 cc-2"),
            R("« C'est ton père qui parle, pas toi. »", 5, "em1 cc-1"),
        ]),
        I(4, "noah", "vulnerable",
          "Un long silence. Puis : « Je regarde la fenêtre depuis une heure. » Vous l'entendez "
          "avaler sa salive. « Je n'ai pas de plan. Je regarde juste la fenêtre. » Puis, très "
          "bas : « Ne raccroche pas. »", [
            R("« Je ne raccroche pas. Je reste avec toi. Est-ce que tu peux t'éloigner de la "
              "fenêtre, et t'asseoir par terre, dans le couloir ? »", 6, "em3 cc2 co2 er1 ic1"),
            R("« Tu ne vas pas faire ça, hein ? Promets-moi. »", 5, "cc-1 em1 pb-1"),
            R("« J'appelle le 144. » Et raccrocher pour composer le numéro.",
              7, "ic2 em-2 pb1"),
            R("« Tu me fais peur, Noah. Arrête. »", 5, "er-2 em-1"),
            R("« J'arrive. Ne bouge pas. » Et partir en courant, sans prévenir personne.",
              8, "em2 ic-2 pb-1"),
        ]),
        I(5, "noah", "cold-anger",
          "« Laisse tomber. » Sa voix se ferme. « Je n'aurais pas dû t'écrire. Oublie. » Vous "
          "l'entendez bouger. La fenêtre, peut-être.", [
            R("« Non, Noah. Je ne laisse pas tomber. Je reste au téléphone avec toi. Et je vais "
              "demander de l'aide, parce que tu comptes trop pour que je porte ça seul·e. »",
              6, "em3 pb2 ic2 er1"),
            R("« Ok. Bonne nuit. »", 9, "em-3 co-3"),
            R("« Tu promets que tu vas dormir ? »", 9, "cc-2 pb-1"),
            R("L'appeler en boucle, sans savoir quoi lui dire.", 6, "em1 er-1"),
        ]),
        I(6, "noah", "vulnerable",
          "Noah s'est assis par terre, dans le couloir de son appartement, dit-il. Sa "
          "colocataire dort à côté. Sa respiration ralentit un peu. « Et maintenant ? »", [
            R("« Maintenant, je reste avec toi, et on appelle quelqu'un ensemble. Ta coloc "
              "d'abord, pour que tu ne sois pas seul. Puis le 144, ou les urgences "
              "psychiatriques : ils sont là pour ça, la nuit. »", 10, "ic3 cc2 em2 pb1",
              sets=["noah_aide"]),
            R("« Maintenant, tu dors, et demain tu vas voir un psy. »", 11, "cc-1 em-1 pb-1",
              sets=["noah_seul"]),
            R("« Maintenant, j'arrive. Garde le téléphone contre ton oreille. » Et appeler le "
              "144 depuis un autre téléphone, en lui parlant.", 10, "ic2 em2 er1",
              sets=["noah_aide"]),
            R("« Appelle La Main Tendue, au 143. Ils sont mieux que moi pour ça. »",
              11, "ic1 em-1", sets=["noah_seul"]),
            R("« On n'en parle à personne, d'accord ? C'est entre nous. »",
              11, "pb-3 em-1 ic-2", sets=["noah_seul"]),
        ]),
        I(7, "narr", "",
          "La régulatrice du 144 vous demande l'adresse de Noah ; vous la connaissez à peu "
          "près. Elle vous dit : « Rappelez-le. Restez en ligne avec lui jusqu'à ce que nous "
          "arrivions. » Vous le rappelez. Il ne décroche pas. Une fois. Deux fois. À la "
          "troisième, il décroche.", [
            R("« Noah. Je suis là. Je ne raccroche plus. Des gens arrivent pour t'aider. »",
              10, "em3 er1 ic1", sets=["noah_aide"]),
            R("« Pourquoi tu ne répondais pas ?! »", 10, "er-2 em-1", sets=["noah_aide"]),
            R("« Ouvre la porte quand ils sonneront, d'accord ? »", 10, "cc2 ic1",
              sets=["noah_aide"]),
            R("« Pardon d'avoir raccroché. Il fallait que j'appelle. »", 10, "cc2 em1 pb1",
              sets=["noah_aide"]),
        ]),
        I(8, "narr", "",
          "Vous courez dans la rue, le téléphone à l'oreille. Noah ne parle plus. Vous lui "
          "parlez quand même. Au bout de vingt minutes, essoufflé·e, vous arrivez devant son "
          "immeuble. La porte est fermée. Vous ne connaissez pas le code.", [
            R("Appeler le 144 avec l'adresse exacte, puis rappeler Noah aussitôt.",
              10, "ic2 cc1 er1", sets=["noah_aide"]),
            R("Sonner chez tous les voisins, au hasard.", 10, "ic1 er-1", sets=["noah_aide"]),
            R("Attendre devant la porte que quelqu'un sorte.", 11, "er-2 ic-2",
              sets=["noah_seul"]),
            R("Appeler la colocataire de Noah, dont vous avez le numéro grâce au groupe.",
              10, "ic3 er1", sets=["noah_aide"]),
        ]),
        I(9, "noah", "sad",
          "« ok » « t'as raison » « bonne nuit ». Noah n'est plus en ligne.", [
            R("L'appeler immédiatement, encore et encore. Puis, sans réponse, appeler le 144.",
              12, "ic2 em2 er1", sets=["noah_aide"]),
            R("Poser le téléphone. Il a dit bonne nuit.", 11, "em-3 co-2",
              sets=["noah_seul"]),
            R("Lui écrire : « courage pour demain ! »", 11, "em-2 cc-2", sets=["noah_seul"]),
            R("Écrire à Maëlle : « Noah m'envoie des trucs bizarres. » Et se recoucher.",
              11, "pb-2 ic-1", sets=["noah_seul"]),
        ]),
        I(10, "narr", "",
          "À 2 h 40, la colocataire de Noah ouvre la porte aux ambulanciers. Noah descend "
          "l'escalier entre eux, en chaussettes, une couverture sur les épaules. « Désolé », "
          "dit-il, à vous ou à personne. Aux urgences psychiatriques, une infirmière vous dit "
          "qu'il va rester quelques jours. « Vous avez bien fait de ne pas le laisser seul. Et "
          "maintenant, allez dormir : vous aussi, vous avez un examen. »"),
        I(11, "narr", "",
          "Vous finissez par vous endormir, le téléphone dans la main. À 7 h, rien. Noah n'est "
          "pas à l'examen. À 11 h, Maëlle vous appelle : sa colocataire l'a trouvé ce matin, "
          "recroquevillé sur le sol de la salle de bains, incapable de parler. Il est aux "
          "urgences psychiatriques. Il est vivant."),
        I(12, "narr", "",
          "Vous appelez Noah onze fois. Puis le 144, avec son adresse. À 2 h 15, une ambulance "
          "est devant son immeuble ; sa colocataire leur ouvre. Noah était assis dans le "
          "couloir, la fenêtre de sa chambre grande ouverte. Il va rester quelques jours aux "
          "urgences psychiatriques. Au téléphone, l'infirmière vous dit : « Vous avez bien "
          "fait d'appeler. »"),
        I(20, "noah", "sad",
          "« t'es réveillé·e ? » « tu te souviens, en septembre, tu m'as promis de jamais rien "
          "dire à personne. quoi qu'il arrive » « je crois que je vais tout arrêter. tout »", [
            R("L'appeler, tout de suite.", 2, "em3 er1"),
            R("« Noah, cette promesse-là, je ne peux pas la tenir si tu es en danger. Est-ce que "
              "tu penses à te tuer ? »", 4, "cc3 em2 pb2"),
            R("« Promis, je ne dirai rien. Parle-moi. »", 3, "pb-2 em1"),
            R("« Dors, Noah. »", 9, "em-3 co-2 cc-2"),
        ]),
        I(30, "noah", "sad",
          "« t'es réveillé·e ? » « en septembre tu m'as dit que si j'allais vraiment mal tu "
          "m'aiderais à trouver quelqu'un » « je crois que c'est maintenant » « je regarde la "
          "fenêtre depuis une heure »", [
            R("L'appeler immédiatement : « Je suis là. Tu as bien fait d'écrire. »",
              4, "em3 er1 cc1"),
            R("« Est-ce que tu penses à te tuer ? »", 4, "cc3 em1"),
            R("« Attends, je cherche un numéro. »", 6, "ic2 em-1"),
            R("« Il est 1 h, Noah. On en parle demain ? »", 9, "em-3 co-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.5 La rééducation — branche « l'alerte a été rapide »
# ---------------------------------------------------------------------------
S4_5A = S(5, "4.5 La rééducation",
    "Fin mars. Une demi-journée d'observation en physiothérapie, avec Laura Steiner, au "
    "centre de réadaptation. Dans la salle d'ergothérapie, un homme en survêtement essaie de "
    "saisir un gobelet en plastique : Bernard.",
    focus=("rd", "ic", "co"),
    slot="4.5",
    cond=when(all=["bernard_rapide"]),
    nodes=[
        I(1, "laura", "neutral",
          "« Toi, tu le connais, je crois ? » Laura vous fait asseoir dans un coin. "
          "« Thrombolyse dans l'heure. Il récupère vite. Il lui reste des mots qui se cachent, "
          "et une main droite qui ne fait pas toujours ce qu'il lui dit. » Elle vous regarde. "
          "« Ici, une seule règle : on ne fait rien à sa place. Même si ça prend dix "
          "minutes. »", [
            R("« D'accord. Je regarde, et je ne fais rien à sa place. »", 2, "rd2 ic2"),
            R("« Je peux l'aider à tenir le gobelet ? »", 3, "rd-1 ic-1"),
            R("« Il va récupérer complètement ? »", 2, "cc1 ic1"),
            R("« C'est grâce à moi qu'il a eu la thrombolyse à temps. »", 2, "pb-2 rd-1 ic-1"),
            R("Saluer Bernard d'un signe, sans s'imposer.", 2, "rd2 em1"),
        ]),
        I(2, "bernard", "happy",
          "Bernard vous aperçoit. Il pose le gobelet, cherche ses mots. « Le… le petit… de la… "
          "box. » Il rit, fâché contre sa propre bouche. « Je joue un AVC… pour de vrai, "
          "maintenant. Bon… réalisme. »", [
            R("« Le meilleur rôle de votre carrière, alors. » Et attendre, pour le laisser "
              "finir.", 4, "em2 rd2"),
            R("Finir ses phrases à sa place, quand il cherche un mot.", 3, "rd-2 em-1"),
            R("« Ne parlez pas, ça vous fatigue. »", 3, "rd-2 cc-1"),
            R("« Je suis tellement content·e de vous voir. »", 4, "em2 co1"),
            R("« Vous m'avez fait peur, Bernard. »", 4, "em1 er1"),
        ]),
        I(3, "laura", "cold-anger",
          "Laura vous touche le bras. « Laisse-le. Chaque mot que tu dis à sa place, c'est un "
          "mot qu'il ne réapprend pas. » Bernard vous regarde, les sourcils froncés, et finit "
          "sa phrase lui-même, lentement, très fier.", [
            R("« Pardon. Je laisse faire. »", 4, "rd2 ic2 er1"),
            R("« Je voulais juste l'aider. »", 4, "er-1 ic-1"),
            R("« Il met trop de temps. »", 4, "rd-3 em-2"),
            R("Se taire, les mains sur les genoux.", 4, "rd1 er1"),
        ]),
        I(4, "bernard", "vulnerable",
          "Laura s'éloigne vers un autre patient. Bernard vous fait signe d'approcher. « La "
          "Dre Chevalley… veut me revoir. Dans un mois. Comme… patient standardisé. » Il lève "
          "sa main droite, qui tremble. « Je jouerai… M. Rossier… après l'AVC. Sans… "
          "script. » Il vous fixe. « Vous… vous viendrez ? Vous entraîner. Sur moi. »", [
            R("« Si vous voulez de moi, je viendrai. Et cette fois, si quelque chose cloche, je "
              "dirai « Pause réelle » à la première seconde. »", 5, "rd2 er2 em1"),
            R("« Vous êtes sûr ? Ce n'est pas trop tôt ? »", 5, "em1 pb1"),
            R("« Je ne sais pas si je pourrai. »", 5, "er-1 em-1"),
            R("« Votre femme est d'accord ? »", 5, "pb-1 rd-1"),
            R("« À votre âge, vous devriez arrêter. »", 5, "rd-3 em-1"),
        ]),
        I(5, "laura", "neutral",
          "Fin de matinée. Laura range les cônes. « Tu sais ce que je fais, moi, en vrai ? Je "
          "lui réapprends à se servir de son corps, comme s'il était neuf. Les médecins sauvent "
          "le cerveau en une heure ; nous, on passe six mois à lui rendre ses mains. » Elle "
          "vous regarde. « Qu'est-ce que tu as appris, ce matin ? »", [
            R("« Que la guérison se fait ici, pas aux urgences. Et que ne rien faire à sa place, "
              "c'est le soin. »", END, "ic3 rd2"),
            R("« La plasticité cérébrale, en vrai. »", END, "cc1"),
            R("« Que la physio, c'est surtout de la patience. »", END, "ic1 rd1"),
            R("« Pas grand-chose, j'ai surtout regardé. »", END, "ic-2 rd-1"),
            R("« Que je ne savais pas ce que tu faisais, avant aujourd'hui. Merci. »",
              END, "ic3 er1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.5 Vingt-trois minutes — branche « l'alerte a tardé »
# ---------------------------------------------------------------------------
S4_5B = S(6, "4.5 Vingt-trois minutes",
    "Fin mars. Une demi-journée d'observation en physiothérapie, avec Laura Steiner, au "
    "centre de réadaptation. Elle vous a prévenu·e au téléphone : « M. Gilliéron est dans "
    "mon planning. Tu peux refuser. » Vous n'avez pas refusé.",
    focus=("rd", "co", "pb", "cc"),
    slot="4.5",
    cond=when(none=["bernard_rapide"]),
    nodes=[
        I(1, "narr", "",
          "Bernard est dans un fauteuil roulant, le bras droit posé dans une gouttière. Il ne "
          "parle plus. Il comprend presque tout, dit Laura. Quand il vous voit, son visage "
          "change. Une femme aux cheveux blancs, assise à côté de lui, se lève : Odile, sa "
          "femme.", [
            R("S'approcher, se présenter à Odile, puis dire bonjour à Bernard en le regardant, "
              "lui.", 2, "rd3 em1"),
            R("Rester près de la porte.", 2, "er-1 rd-1"),
            R("Parler de Bernard à Odile comme s'il n'était pas là.", 2, "rd-3 em-1"),
            R("Saluer Bernard d'un geste maladroit, et détourner les yeux.", 2, "rd-1 er-1"),
            R("Faire demi-tour.", 6, "er-2 rd-1 co-1"),
        ]),
        I(2, "odile", "cold-anger",
          "Odile vous regarde longtemps. « C'est vous. L'étudiant·e du box. » Elle ne crie pas. "
          "« On m'a dit qu'il s'est passé vingt-trois minutes entre le moment où il a lâché son "
          "verre et celui où quelqu'un a appelé. Vingt-trois minutes. » Elle s'arrête. "
          "« Pourquoi personne n'a rien fait pendant vingt-trois minutes ? »", [
            R("« Parce que j'ai cru qu'il jouait. C'était à moi de dire « Pause réelle », et je "
              "ne l'ai pas dit. Je suis désolé·e, Madame. »", 3, "pb3 rd2 co2 cc1"),
            R("« Tout le monde a cru qu'il jouait. Même derrière la vitre. »", 4, "pb-2 co-1"),
            R("« La thrombolyse n'aurait peut-être rien changé. »", 4, "pb-2 cc-2 em-2"),
            R("« Je ne peux pas vous répondre : il y a une revue d'incident en cours. »",
              4, "pb1 em-2 co-1"),
            R("Baisser les yeux, sans rien dire.", 4, "er-1"),
        ]),
        I(3, "odile", "sad",
          "Odile se rassied. Elle prend la main gauche de Bernard. « Il jouait si bien, vous "
          "savez. Trente ans de théâtre. Les gens pleuraient. » Elle sourit, une seconde. "
          "« Même quand il mourait sur scène, c'était lui qui me rassurait, après, en "
          "coulisses. » Bernard serre sa main. Il vous regarde. Il fait un geste vers vous, "
          "puis vers sa bouche.", [
            R("« Vous voulez me dire quelque chose ? Prenez votre temps. Je reste. »",
              5, "rd2 em2 co1"),
            R("Demander à Odile : « Il veut dire qu'il ne m'en veut pas ? »", 5, "rd-2 pb-1"),
            R("Lui tendre un crayon et un carnet.", 5, "rd2 cc1 em1"),
            R("« Je reviendrai quand il ira mieux. »", 6, "em-1 rd-1"),
        ]),
        I(4, "odile", "cold-anger",
          "Odile secoue la tête. « On m'avait dit que les étudiants en médecine apprenaient à "
          "reconnaître une attaque dès la deuxième année. » Elle ramasse son sac. « Bernard, on "
          "y va. » Bernard ne bouge pas. Il vous regarde. Il fait un geste vers vous, puis vers "
          "sa bouche.", [
            R("« Madame, pardon. Je me suis caché·e derrière les autres. La vérité, c'est que "
              "j'avais les signes sous les yeux, et que je n'ai pas osé sortir du script. »",
              3, "pb3 rd2 er1"),
            R("« Il veut dire quelque chose. » Et lui tendre un carnet et un crayon.",
              5, "rd2 cc1"),
            R("Les laisser partir.", 6, "er-1 co-1"),
            R("« Vous devriez vous plaindre au centre, pas à moi. »", 6, "rd-2 ic-2 co-1"),
        ]),
        I(5, "bernard", "neutral",
          "De la main gauche, très lentement, Bernard écrit dans le carnet. Des lettres "
          "énormes, de travers. Il vous le tend. Il a écrit : « PAUSE RÉELLE. » Et dessous, "
          "après un long moment : « APPRENEZ-LE AUX AUTRES. »", [
            R("« Je vous le promets. »", 7, "rd2 co2 er1"),
            R("Pleurer, sans pouvoir rien dire.", 7, "co1 er-1"),
            R("« Ce n'est pas à moi de faire les formations. »", 7, "rd-2 ic-1"),
            R("« Je le dirai à la revue d'incident, mot pour mot. »", 7, "ic2 pb1 co1"),
        ]),
        I(6, "narr", "",
          "Vous ressortez du centre. Sur le parking, vous restez longtemps dans votre voiture, "
          "les mains sur le volant, sans démarrer.", [go(7)]),
        I(7, "chevalley", "neutral",
          "Deux jours plus tard, salle de réunion du centre de simulation. Revue d'incident : "
          "la Dre Chevalley, la responsable qualité, deux formateurs, les étudiant·e·s présents "
          "ce jour-là. Au tableau, une chronologie minute par minute. 14 h 06 : premiers "
          "signes. 14 h 29 : premier appel. « On ne cherche pas un coupable, dit la "
          "Dre Chevalley. On cherche ce qui, chez nous, a rendu vingt-trois minutes "
          "possibles. » Elle se tourne vers vous. « Alex, de l'intérieur du box : qu'est-ce qui "
          "vous a empêché·e de sortir du script ? »", [
            R("« J'ai vu les signes. J'ai cru que c'était joué, parce que tout est joué, ici. "
              "Et personne ne m'avait jamais vraiment entraîné·e à dire « Pause réelle ». "
              "J'aurais dû le dire quand même. »", 8, "pb3 cc3 ic2 er1"),
            R("« Les rires, derrière la vitre. »", 8, "ic-2 pb-1"),
            R("« Je ne sais pas. »", 8, "cc-2 er-1"),
            R("« Bernard avait l'air de jouer : c'est un très bon comédien. »", 8, "pb-2 rd-1"),
            R("« Le scénario parlait de son frère et d'une attaque : j'ai cru que c'était "
              "voulu. Je pense qu'il faudrait le changer. »", 8, "cc2 ic2 pb1"),
        ]),
        I(8, "chevalley", "neutral",
          "La Dre Chevalley écrit au tableau : « Briefing : pause réelle répétée, et "
          "exercée. » « Scénarios : jamais de signes neurologiques non annoncés aux "
          "observateurs. » « Patients standardisés : bilan de santé proposé. » Elle pose le "
          "feutre. « Et Bernard a demandé une chose : qu'on raconte son histoire à chaque "
          "nouvelle volée. Avec son nom. » Elle vous regarde. « Il a demandé que ce soit vous "
          "qui la racontiez. »", [
            R("« Je la raconterai. Avec ce que j'ai mal fait, pas seulement ce qu'il a "
              "perdu. »", END, "pb2 co2 cc2 er1"),
            R("« Je la raconterai. »", END, "co2 ic2 rd1"),
            R("« Je ne suis pas sûr·e d'en être capable. »", END, "er1"),
            R("« Pourquoi moi ? »", END, "er-1"),
            R("« Il veut me punir ? »", END, "er-2 rd-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.6 Les pieds qui ne savent plus
# ---------------------------------------------------------------------------
S4_6 = S(7, "4.6 Les pieds qui ne savent plus",
    "Mi-mars, Montchéry. Thierry a trouvé Jeannine par terre dans la cuisine, à 8 h, assise "
    "contre le fourneau, un bleu sur la hanche. Rien de cassé. Elle était tombée à 6 h. La "
    "Dre Golay a demandé une évaluation à domicile par Laura Steiner, la physiothérapeute, "
    "et vous envoie avec elle.",
    focus=("ic", "rd", "cc"),
    nodes=[
        I(1, "jeannine", "resigned",
          "« Ah. La cavalerie. » Jeannine est dans son fauteuil, une poche de glace sur la "
          "hanche. « Je suis tombée comme une vache sur la glace. Deux heures assise par terre, "
          "à compter les mouches. » Laura pose son sac. « Racontez-moi comment c'est "
          "arrivé. »", [
            R("Rester en retrait, et laisser Laura mener l'évaluation : c'est son domaine.",
              2, "ic3 rd1"),
            R("« Vous auriez dû appeler quelqu'un ! »", 3, "rd-2 em-1"),
            R("S'asseoir près de Jeannine : « Deux heures par terre… Vous avez eu peur ? »",
              2, "em3 rd1"),
            R("Examiner la hanche avant que Laura ait commencé.", 3, "ic-2 pb-2"),
            R("« Vous avez un bracelet d'alarme ? »", 2, "cc1 ic1"),
        ]),
        I(2, "jeannine", "neutral",
          "« Je me suis levée pour la tisane. Et mes pieds… » Elle cherche. « Mes pieds ne "
          "savaient plus où était le sol. Comme si je marchais sur du coton. Depuis l'hiver, "
          "c'est comme ça. » Laura hoche la tête, lui enlève ses pantoufles et sort un "
          "diapason de son sac.", [
            R("Observer Laura tester la sensibilité, et noter ce qu'elle dit à Jeannine.",
              4, "ic2 cc1 rd1"),
            R("Dire à voix haute : « C'est une neuropathie diabétique. »", 5, "pb-2 cc-1 rd-1"),
            R("« Sur du coton… Et pieds nus, vous sentez le sol ? »", 4, "cc2 em1"),
            R("Regarder votre téléphone pendant le test.", 4, "rd-2 ic-1"),
        ]),
        I(3, "laura", "neutral",
          "Laura vous jette un regard, sans reproche, mais sans sourire non plus. « On commence "
          "par écouter comment c'est arrivé. Le reste, après, et dans l'ordre. » Elle "
          "s'accroupit devant Jeannine. « Racontez-moi, Madame Pittet. »", [go(2)]),
        I(4, "laura", "neutral",
          "Laura pose le diapason sur la cheville de Jeannine. « Vous sentez la vibration ? » — "
          "« Quelle vibration ? » Puis l'équilibre : debout, pieds joints, yeux ouverts, puis "
          "fermés. Les yeux fermés, Jeannine part en arrière ; Laura la rattrape. « Vos pieds "
          "ne vous disent plus où ils sont. Ce sont vos yeux qui font tout le travail. La nuit, "
          "sans lumière, vous tombez. » Elle se tourne vers vous. « Qu'est-ce que tu "
          "proposerais, toi, dans cette maison ? »", [
            R("« De la lumière la nuit, entre la chambre et la cuisine. Enlever les tapis. Et un "
              "bracelet d'alarme, pour ne plus jamais rester deux heures par terre. »",
              6, "ic3 cc2 em1"),
            R("« Un EMS, peut-être ? »", 7, "rd-2 pb-2"),
            R("« Je ne sais pas, c'est ton domaine. »", 6, "ic-1 cc-1"),
            R("« Qu'elle arrête de se lever la nuit. »", 7, "rd-2 em-1"),
            R("« Qu'est-ce qui compte le plus pour vous, Madame Pittet, dans cette "
              "maison ? »", 6, "rd3 em2 cc1"),
        ]),
        I(5, "laura", "cold-anger",
          "Laura range son diapason. « Le diagnostic, c'est la Dre Golay qui le pose. Moi, je "
          "mesure ce que ça change dans la vie de Mme Pittet. Toi, tu observes. » Jeannine "
          "lève les yeux au ciel. « Ça promet. »", [
            R("« Pardon. J'observe. »", 4, "ic2 pb2"),
            R("« C'est ce qu'on apprend en cours, pourtant. »", 4, "ic-1 er-1"),
            R("Se taire, vexé·e.", 4, "er-1"),
            R("« Désolé·e, Madame Pittet. »", 4, "rd1 ic1"),
        ]),
        I(6, "jeannine", "happy",
          "« Un bracelet d'alarme ? » Jeannine éclate de rire. « Une laisse, vous voulez dire. "
          "Comme pour les vaches. » Elle croise les bras. « J'ai mis au monde six cents enfants "
          "sans téléphone. Je ne vais pas me promener avec un bouton rouge autour du cou. »", [
            R("« Ce n'est pas une laisse : c'est pour que, la prochaine fois, ce soit vous qui "
              "décidiez quand on vient vous chercher. Pas deux heures plus tard. »",
              8, "cc3 rd2 em1"),
            R("« Si vous refusez, vous finirez en EMS. »", 7, "rd-3 pb-2"),
            R("« C'est votre choix. » Et passer à autre chose.", 9, "rd1 em-1"),
            R("« Daniel serait rassuré. »", 8, "em1 rd-1"),
            R("Rire avec elle, puis : « Et une vache qui tombe, on la retrouve comment ? »",
              8, "em2 cc2 rd1"),
        ]),
        I(7, "jeannine", "cold-anger",
          "Jeannine se raidit. « L'EMS. » Elle vous regarde comme on regarde un intrus. « Vous "
          "voulez savoir pourquoi je me lève la nuit, petit ? Pour la tisane, et pour regarder "
          "la cour. Mon mari est mort dans ce talus. Je ne quitterai pas cette maison. » Laura "
          "pose une main sur votre bras.", [
            R("« Pardon. Je suis allé·e beaucoup trop vite. Ce qu'on cherche, c'est comment "
              "vous pouvez rester ici, en sécurité. »", 8, "rd3 er1 cc1"),
            R("« C'était juste une idée. »", 9, "er-1 rd-1"),
            R("« Pourtant, ce serait plus sûr. »", 9, "rd-2 pb-1"),
            R("Se taire.", 9, "er1"),
        ]),
        I(8, "jeannine", "neutral",
          "Jeannine regarde la fenêtre, la cour, la grange. Longtemps. « Et ça sonne où, votre "
          "bouton ? » Laura explique : chez une centrale, qui appelle Thierry, ou Daniel, ou le "
          "144. Jeannine hoche la tête, lentement. « Daniel… » Elle soupire. « D'accord. Mais "
          "rouge, pas question. »", [
            R("« On demandera s'ils en ont en bleu. » Et sourire.", 10, "em2 rd1 cc1",
              sets=["alarme_posee"]),
            R("« Merci, Madame Pittet. Je le dis à la Dre Golay, pour qu'elle l'organise avec "
              "Thierry. »", 10, "ic3 cc1", sets=["alarme_posee"]),
            R("« Enfin raisonnable. »", 10, "rd-2 em-1", sets=["alarme_posee"]),
            R("Ne rien dire, et laisser Laura tout organiser.", 10, "ic1",
              sets=["alarme_posee"]),
        ]),
        I(9, "laura", "resigned",
          "Jeannine ne veut pas en entendre parler. Laura note dans son rapport : « Refus du "
          "système d'alarme. Risque de chute nocturne élevé. Éclairage du couloir à prévoir. » "
          "Sur le pas de la porte, elle vous dit à voix basse : « Elle a le droit de refuser. "
          "Notre travail, c'est qu'elle refuse en sachant. Et qu'on revienne lui reposer la "
          "question. »"),
        I(10, "laura", "neutral",
          "Dans la voiture, Laura rédige son rapport sur ses genoux. « Bracelet, lumière dans "
          "le couloir, tapis enlevés, et deux séances d'équilibre par semaine. » Elle relit. "
          "« Tu sais ce qu'on fait, nous, les physios ? On transforme une maison en terrain "
          "d'entraînement. » Elle range son stylo. « On ne gagne jamais contre le diabète. On "
          "gagne quelques mois debout. »"),
    ],
)

CH4 = C(4, "Hors script",
    situation=(
        "Février et mars. À la fac, les neurosciences, et des stations avec un patient "
        "standardisé : Bernard Gilliéron, ancien comédien. Noah ne dort plus, et son portfolio "
        "a été écrit par un chatbot. À Montchéry, Jeannine tombe, parce que ses pieds ne "
        "savent plus où est le sol."
    ),
    objectives=(
        "mener une anamnèse centrée sur la personne et recevoir un feedback ; sortir d'un "
        "scénario de simulation quand un signe réel apparaît (mot d'arrêt, heure de début, "
        "appel à l'aide) ; reconnaître les signes d'un AVC ; dire la vérité à une institution "
        "sans trahir ni couvrir un camarade ; demander directement à quelqu'un s'il pense au "
        "suicide, ne pas le laisser seul, appeler de l'aide, ne pas promettre le secret ; "
        "participer à une revue d'incident dans une culture juste ; collaborer avec une "
        "physiothérapeute en respectant son domaine ; respecter le refus d'une patiente tout "
        "en l'aidant à décider en connaissance de cause."
    ),
    anchoring=(
        "UNIL BMed2.3 (neurosciences) et BMed2.8 (système nerveux, pratique simulée avec "
        "patient standardisé) · UNIGE compétences cliniques (stations formatives), "
        "enseignement interprofessionnel 1 (facteurs humains), identité professionnelle, "
        "plagiat et IA générative · UZH Humanbiologie II (ZNS, Sinnesorgane), Klinischer "
        "Untersuchungskurs II (statut neurologique), Workshadowing Physiotherapie."
    ),
    focus=("er", "ic", "cc", "pb"),
    scenes=[S4_1, S4_2, S4_3, S4_4, S4_5A, S4_5B, S4_6],
)
