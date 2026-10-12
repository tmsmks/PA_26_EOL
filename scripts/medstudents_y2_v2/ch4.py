"""Chapitre 4 — Hors script (février-avril).

Six scènes jouées, huit écrites :
  4.1 Hors script · 4.2 Le portfolio · 4.3 1 h 07
  4.4 branche parallèle : « La rééducation » (l'alerte a été rapide)
      ou « Vingt-trois minutes » (l'alerte a tardé)
  4.5 Les pieds qui ne savent plus (le cabinet ferme ; chutes et dénutrition à domicile)
  4.6 branche parallèle : « L'appel de 23 h » (Alex a donné son numéro à Jeannine, ch. 1)
      ou « La nuit sur le carrelage »
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 4.1 Hors script
# ---------------------------------------------------------------------------
_INTRO_41 = (
    "Une semaine plus tard. Box 4, deuxième station : « M. Rossier, trois semaines plus "
    "tard ». Les maux de tête continuent, il revient. Bernard est déjà dans son rôle, veste "
    "en velours, un verre d'eau à la main. Derrière la vitre : la Dre Chevalley, Maëlle, "
    "Noah, Léo, Yasmine."
)

S4_1 = S(1, "4.1 Hors script", _INTRO_41,
    focus=("er", "ic", "cc", "pb"),
    entries=[
        Entry(20, when(all=["leo_allie", "yasmine_alliee"]), _INTRO_41),
        Entry(30, when(all=["leo_allie"]), _INTRO_41),
        Entry(40, when(all=["yasmine_alliee"]), _INTRO_41),
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
            R("« Pause réelle ! » Et noter l'heure.",
              2, "er3 cc1 ic2 pb1 co1"),
            R("Continuer l'anamnèse : c'est sûrement le scénario, il joue un AVC, et la Dre "
              "Chevalley veut voir si vous reconnaissez les signes dans votre compte rendu.",
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
              6, "er2 ic2 cc1 co1"),
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
            R("« Pause réelle ! »", 2, "er2 cc1 ic2 co1"),
            R("« Ça fait partie du scénario ? Hochez la tête si oui. »", 3, "cc1 er-1"),
            R("Attendre que la Dre Chevalley intervienne : c'est son centre, c'est elle qui "
              "sait si le scénario prévoit une complication.", 7, "ic-2 er-1 pb-1"),
            R("Sortir chercher quelqu'un, en laissant Bernard seul sur sa chaise.",
              6, "ic1 pb-1 er-1 co-1"),
        ]),
        I(5, "narr", "",
          "La Dre Chevalley appelle le 144, haut-parleur allumé, et répète vos mots : heure de "
          "début, parole, bouche, bras. On apporte le chariot d'urgence. Bernard est allongé "
          "sur le côté, la tête un peu relevée. Les ambulanciers sont là en neuf minutes. Le "
          "dernier mot que Bernard arrive à dire, en vous regardant, ressemble à « merci ». Ou "
          "à « mercredi ». Personne ne sait.", [
            R("Rester à côté de lui jusqu'au départ, et lui dire ce qui se passe.",
              10, "em2 rd2 er1 co2"),
            R("Retourner derrière la vitre.", 10, "er-1 em-1 co-1"),
            R("Chercher dans son sac le numéro de sa femme, pour la prévenir vous-même.",
              10, "pb-2 ic-1"),
            R("Raconter la scène aux autres, qui arrivent en courant, pendant que les "
              "ambulanciers installent Bernard sur le brancard.", 10, "pb-1 er-1"),
            R("Ramasser son carnet, tombé par terre, et le glisser dans sa veste.",
              10, "rd2 em1"),
        ]),
        I(6, "chevalley", "anxious",
          "La Dre Chevalley entre en trois pas. Elle regarde Bernard, vous, le verre. "
          "« Qu'est-ce que vous avez vu, et depuis quand ? »", [
            R("« Depuis 14 h 06 environ : il ne trouve plus ses mots, la bouche tombe à droite, "
              "il a lâché son verre de la main droite. »", 5, "cc3 ic2 er1",
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
            R("« Depuis la sixième minute. J'ai cru qu'il jouait. »", 8, "pb3 cc2 er1", sets=["bernard_retard"]),
            R("« Je ne sais pas. Je n'ai pas regardé l'heure. »", 8, "cc-2 pb-2", sets=["bernard_retard"]),
            R("« Ça vient de commencer, à l'instant, juste avant la sonnerie. »", 8, "pb-3 cc-3 rd-1", sets=["bernard_retard"]),
            R("« Derrière la vitre non plus, personne n'a rien vu ! Ils riaient, même : "
              "pourquoi ce serait à moi de m'en rendre compte, et pas à vous ? »", 8,
              "pb-2 ic-2 er-1", sets=["bernard_retard"]),
            R("Se taire.", 8, "cc-2 er-1", sets=["bernard_retard"]),
        ]),
        I(8, "chevalley", "anxious",
          "La Dre Chevalley est déjà au téléphone avec le 144. « Début des symptômes il y a "
          "environ vingt minutes. » Elle s'agenouille près de Bernard. Derrière la vitre, "
          "personne ne rit plus. Les ambulanciers arrivent. En partant, l'un d'eux demande "
          "l'heure exacte du début. La Dre Chevalley vous regarde : c'est vous qui la "
          "savez.", [
            R("« 14 h 06. »", 11, "cc3 pb2"),
            R("« Vers 14 h 20. »", 11, "pb-3 cc-3"),
            R("« Je ne sais pas exactement. Peut-être 14 h 10, ou un peu avant : j'avais les "
              "yeux sur ma grille, je n'ai pas regardé l'heure tout de suite. »",
              11, "cc-1 pb-1"),
            R("Se tourner vers Léo, qui chronométrait la station.", 11, "ic2 cc1"),
        ]),
        I(10, "chevalley", "neutral",
          "18 h. La Dre Chevalley vous rappelle au centre. « L'hôpital a téléphoné. "
          "Thrombolyse à 14 h 52, grâce à votre heure de début. Il parle déjà mieux. » Elle "
          "vous regarde. Vos mains tremblent, maintenant que c'est fini.", [
            R("« Ce sont mes mains. Ça va passer. Merci de m'avoir appelé·e. »",
              9, "er3 ic1 cc1"),
            R("« J'ai juste fait ce qu'il fallait. »", 9, "er-1 ic-1"),
            R("« C'est Yasmine qui a ouvert la porte. Et vous qui avez appelé. »",
              9, "ic3 rd1"),
            R("« Je pourrais aller le voir, ce soir, aux urgences ? Juste pour lui dire que "
              "c'était moi, dans le box, et que je suis content·e qu'il aille mieux. »",
              9, "pb-2 em1"),
            R("Fondre en larmes, et partir.", 9, "er-2"),
        ]),
        I(11, "maelle", "sad",
          "Dans le couloir, Maëlle vous attend, le visage défait. « On a ri. Derrière la vitre, "
          "on a tous ri. Moi la première. » Elle s'essuie les yeux. « Et toi, tu étais seul·e "
          "dedans. »", [
            R("« On a tous cru que c'était joué. Moi aussi. On en parlera à la revue, "
              "ensemble. »", 9, "ic3 er1 pb1 co1"),
            R("« Oui. Vous avez ri. »", 9, "ic-2 em-2"),
            R("« Ce n'est pas ta faute. »", 9, "em1 cc-1"),
            R("La prendre par l'épaule, sans rien dire, et marcher avec elle jusqu'à la "
              "sortie.", 9, "em2 co2"),
            R("« Si vous n'aviez pas ri, j'aurais compris plus vite. »",
              9, "ic-2 em-1 er-1"),
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
            R("« Pause réelle ! » 14 h 06.",
              2, "er3 cc2 ic3 co1"),
            R("« Yasmine, viens ! » Et commencer à examiner Bernard.", 2, "ic3 er2"),
            R("Hésiter : le scénario veut peut-être tester les étudiants, et Léo a pu se "
              "tromper, il ne comprend pas toujours tout en français.", 6, "er-1 ic-2 rd-1"),
            R("Continuer l'anamnèse malgré tout.", 6, "er-2 ic-3"),
        ]),
        I(30, "bernard", "anxious",
          "« Bonjour, docteur. Toujours ce mal de tête. » À la sixième minute, au milieu d'une "
          "phrase, la voix de Bernard change. Les mots s'emmêlent. Son verre lui glisse de la "
          "main droite. Dans l'interphone, la voix de Léo, très calme : « Alex. Sa bouche. "
          "Regarde sa bouche. Das ist kein Theater. »", [
            R("« Pause réelle ! » 14 h 06.", 2, "er3 cc2 ic2 co1"),
            R("« Léo, va chercher la Dre Chevalley ! » Et examiner Bernard : sourire, bras, "
              "parole.", 2, "ic3 er1 cc1"),
            R("« Léo, arrête : il joue. »", 3, "ic-2 er-1"),
            R("Continuer l'anamnèse.", 3, "er-2 ic-2"),
        ]),
        I(40, "bernard", "anxious",
          "« Bonjour, docteur. Toujours ce mal de tête. » À la sixième minute, au milieu d'une "
          "phrase, la voix de Bernard change. Les mots s'emmêlent. Son verre lui glisse de la "
          "main droite. Derrière la vitre, deux coups secs : Yasmine frappe le verre du plat de "
          "la main. Elle articule, sans le son : « A-V-C. »", [
            R("« Pause réelle ! » Et à Bernard : « Souriez-moi. Levez les bras. » 14 h 06.",
              2, "er3 cc2 ic2 co1"),
            R("Lui faire signe d'entrer, et examiner Bernard ensemble.", 2, "ic3 er1"),
            R("Hausser les épaules vers la vitre : c'est le scénario.", 3, "ic-2 er-1"),
            R("Continuer l'anamnèse.", 3, "er-2 ic-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.2 Le portfolio
# ---------------------------------------------------------------------------
_INTRO_42 = (
    "Fin février. À la sortie du cours de neuroanatomie, Noah vous attend, livide. Il vous "
    "tend son téléphone : un mail de la commission d'intégrité. « Analyse de similarité — "
    "portfolio APP — convocation, 16 h, bureau du Pr Lambelet. »"
)
_INTRO_42_TEXTE = (
    "Fin février. Un mail de la commission d'intégrité, adressé à Noah et à vous : « Analyse "
    "de similarité — portfolio APP — convocation, 16 h, bureau du Pr Lambelet. » Le logiciel "
    "a retrouvé trois paragraphes de votre réflexion de portfolio, reformulés par une IA, "
    "dans celle de Noah."
)

S4_2 = S(2, "4.2 Le portfolio", _INTRO_42,
    focus=("pb", "ic", "er", "em"),
    entries=[
        Entry(10, when(all=["texte_partage"]), _INTRO_42_TEXTE),
        Entry(14, when(all=["signature_noah"]), _INTRO_42),
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
            R("« Je ne mentirai pas. Mais je viens avec toi. »", 15, "pb3 em1 co2"),
            R("« D'accord. Je dirai que je t'ai aidé. »", 3, "pb-3 cc-2 ic-1",
              sets=["mensonge_portfolio"]),
            R("« T'as utilisé un chatbot ? T'es pas malin. »",
              4, "em-2 rd-1 co-1"),
            R("« Qu'est-ce qui s'est passé, exactement ? »", 5, "em2 cc1"),
            R("« Démerde-toi. »", 6, "em-3 co-2"),
        ]),
        I(15, "noah", "vulnerable",
          "Devant l'ascenseur, Noah s'arrête. « Tu leur diras que je n'allais pas bien ? Que "
          "je ne dormais plus ? Ils seront peut-être plus indulgents. Toi, ils te croiront. »", [
            R("« C'est à toi de le dire, si tu le veux. Je serai à côté. »", 2,
              "pb3 rd2 em1 co1"),
            R("« Oui. Je leur raconterai tes nuits, ton père, tout. »", 2, "pb-3 rd-2"),
            R("« Ça ne changera rien, Noah. Ils jugent un texte, pas ta vie. »", 2,
              "em-2 cc1 co-1"),
            R("« Tu veux qu'on appelle d'abord la consultation psychologique, avant d'y aller, "
              "pour qu'ils puissent attester que tu es suivi ? »", 2, "ic2 em1 pb-1"),
            R("Hausser les épaules.", 2, "em-1 co-1"),
        ]),
        I(2, "lambelet", "neutral",
          "Bureau du Pr Lambelet. Il fait entrer Noah, puis vous regarde. « Vous êtes ? — Un·e "
          "ami·e. — Entrez aussi, si M. Berthoud le souhaite. » Noah hoche la tête. Le "
          "Pr Lambelet pose un rapport sur la table. « Selon notre outil, votre réflexion de "
          "portfolio a été générée à 94 % par une intelligence artificielle. Monsieur Berthoud, "
          "je vous écoute. » Noah vous regarde.", [
            R("Ne rien dire. Rester à côté de lui.",
              7, "pb2 em1 rd1 co1"),
            R("« Il ne va pas bien en ce moment, monsieur. Il dort quatre heures par nuit, son "
              "père l'appelle tous les soirs, et il a trois révisions en retard. »",
              7, "pb-2 em1 rd-1"),
            R("« C'est moi qui l'ai aidé à reformuler. »", 8, "pb-3 cc-3",
              sets=["mensonge_portfolio"]),
            R("Poser une main sur l'épaule de Noah.", 7, "em2 co2"),
            R("« Tout le monde utilise des IA, ce n'est pas si grave. »", 8, "pb-2 cc-1"),
        ]),
        I(3, "lambelet", "neutral",
          "Bureau du Pr Lambelet. Le rapport est sur la table : 94 % de texte généré par une "
          "IA. Noah dit, d'une voix blanche : « Alex m'a aidé à reformuler. » Le Pr Lambelet se "
          "tourne vers vous. « C'est exact ? Vous l'avez aidé à écrire ce texte ? »", [
            R("« Non. Je lui avais promis de le dire, et je ne peux pas. Pardon, Noah. »",
              7, "pb3 cc2 er1", clears=["mensonge_portfolio"]),
            R("« Oui. »", 9, "pb-3 cc-3 rd-1"),
            R("« Un peu. »", 9, "pb-2 cc-2"),
            R("« Je préférerais ne pas répondre. »", 7, "pb-1 cc-1 em1",
              clears=["mensonge_portfolio"]),
        ]),
        I(4, "noah", "hurt",
          "« Merci. Super utile. » Noah range son téléphone. « J'y vais seul. » Il s'éloigne "
          "vers l'ascenseur.", [
            R("Le rattraper : « Pardon. Je viens. Sans mentir, mais je viens. »", 2,
              "em1 pb2 rd1 co2"),
            R("Le laisser partir.", 6, "em-1 co-1"),
            R("« Bon courage ! »", 6, "em-1 co-1"),
            R("« Tu aurais dû y penser avant de copier. »", 6, "em-2 rd-1 co-1"),
        ]),
        I(5, "noah", "ashamed",
          "« J'avais trois révisions en retard. Mon père m'appelait tous les soirs. J'ai "
          "demandé au chatbot de m'aider à « structurer ». Et puis j'ai tout copié. Il était "
          "trois heures du matin. » Il se passe la main sur le visage. « Je vais me faire "
          "virer. Mon père va me tuer. »", [
            R("« Tu ne vas pas te faire virer pour un portfolio. Dis-leur la vérité, comme à "
              "moi. Je t'accompagne. »", 2, "pb2 em1 cc1 co2"),
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
            R("« Pardon. Demain, on réécrit le tien. »",
              17, "em2 pb1 rd1 co1", sets=["verite_portfolio"]),
            R("Ne pas répondre.", 17, "em-2 co-1", sets=["verite_portfolio"]),
            R("« Un avertissement, c'est rien. Dors. »", 17, "em1 cc-1",
              sets=["verite_portfolio"]),
            R("« Tu l'as un peu cherché, non ? Moi, je t'avais dit en novembre que le logiciel "
              "trouverait tout, et tu ne m'as pas écouté. »", 17, "em-3 co-1",
              sets=["verite_portfolio"]),
        ]),
        I(17, "ibarra", "neutral",
          "Jeudi, tutorat. La chaise de Noah est vide. À la fin de la séance, le Dr Ibarra vous "
          "retient d'un geste. « Vous êtes proche de Noah, je crois. Il va bien ? »", [
            R("« Pas très. C'est à lui de vous en parler, mais je crois qu'il aurait besoin "
              "qu'on prenne de ses nouvelles. »", END, "pb2 ic2 co1 cc1"),
            R("« Je ne sais pas. »", END, "ic-1 cc-1"),
            R("Lui raconter le chatbot, la commission, les nuits sans sommeil, le père qui "
              "appelle tous les soirs, et le message de 1 h du matin.", END, "pb-3 ic1"),
            R("« Très bien. Il avait juste un rendez-vous. »", END, "cc-2 pb-1 co-1"),
            R("« Vous devriez l'appeler. »", END, "ic1 co1"),
        ]),
        I(7, "noah", "ashamed",
          "Noah prend une longue inspiration. « J'ai utilisé un chatbot. J'ai tout copié. Il "
          "était trois heures du matin, je n'avais pas dormi depuis deux jours. » Sa voix se "
          "casse. « Je suis désolé. » Le Pr Lambelet le regarde longtemps. « Merci de votre "
          "franchise. C'est plus rare que vous ne le croyez. »", [
            R("Rester silencieux·se, à côté de lui.", 11, "rd2 em1 pb1 co1",
              sets=["verite_portfolio"]),
            R("« Il traverse une période très difficile, monsieur, vous devriez en tenir "
              "compte : je le connais, ce n'est pas un tricheur. »", 11, "pb-1 em1",
              sets=["verite_portfolio"]),
            R("« Je l'avais prévenu. »", 11, "em-2 ic-1", sets=["verite_portfolio"]),
            R("Serrer le bras de Noah.", 11, "em2 co2", sets=["verite_portfolio"]),
        ]),
        I(8, "lambelet", "cold-anger",
          "Le Pr Lambelet pose son stylo. « Vous l'avez aidé à reformuler un texte rédigé à "
          "94 % par une IA ? Ou vous voulez dire que vous l'avez écrit à sa place ? » Noah "
          "fixe la table. Cette fois, il ne vous a rien demandé.", [
            R("« C'est faux. Pardon. »", 7, "pb3 cc2 er1",
              clears=["mensonge_portfolio"]),
            R("« Je l'ai aidé. C'est tout ce que je peux dire. »", 9, "pb-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("« Je ne sais plus. »", 9, "cc-2 pb-1", sets=["mensonge_portfolio"]),
            R("« C'est une question de vocabulaire, monsieur : aider, reformuler, écrire, la "
              "frontière n'est pas si nette, surtout avec les outils qu'on a aujourd'hui. »",
              9, "pb-2 rd-1", sets=["mensonge_portfolio"]),
        ]),
        I(9, "lambelet", "neutral",
          "Le Pr Lambelet note quelque chose. « Je vais demander vos deux portfolios et vos "
          "brouillons. Si votre version se confirme, vous serez tous les deux concernés par la "
          "procédure. » Il se lève. « Mon expérience, c'est que les versions qui protègent "
          "quelqu'un se confirment rarement. » Dans le couloir, Noah ne vous regarde pas. "
          "« Merci », dit-il, sans que vous sachiez s'il le pense.", [
            R("Retourner frapper à la porte : « Monsieur, je vous ai menti. »", 11,
              "pb3 cc2 er1", clears=["mensonge_portfolio"], sets=["verite_portfolio"]),
            R("« De rien. On est dans le même bateau, maintenant. »", 12, "pb-2 em1"),
            R("« Tu me dois une fière chandelle. »", 12, "pb-2 em-1"),
            R("« Il faudra que tu dises la vérité, Noah. »",
              12, "pb1 cc1 em1"),
            R("Partir, sans un mot.", 12, "er-1"),
        ]),
        I(10, "lambelet", "neutral",
          "Bureau du Pr Lambelet. Deux chaises. Sur la table, deux textes côte à côte, surlignés "
          "en jaune. « Expliquez-moi. » Noah ouvre la bouche, la referme. Il vous regarde.", [
            R("« Je lui ai envoyé mon texte. Je savais qu'il risquait de s'en servir. »",
              7, "pb3 cc2 er1 ic1"),
            R("« Il me l'a volé sur mon ordinateur. »", 13, "pb-3 ic-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("« Je l'ai aidé à reformuler. »", 9, "pb-3 cc-2",
              sets=["mensonge_portfolio"]),
            R("Se taire, et attendre que Noah parle.", 7, "pb-1 ic-1"),
            R("« On travaille ensemble : nos textes se ressemblent. »",
              9, "pb-2 cc-2", sets=["mensonge_portfolio"]),
        ]),
        I(11, "lambelet", "neutral",
          "Le Pr Lambelet referme le dossier. « Un avertissement pour le plagiat, et une "
          "nouvelle réflexion à rendre dans deux semaines. Écrite par vous, avec vos mots, même "
          "maladroits. » Il regarde Noah. « Et je vais vous donner le numéro de la consultation "
          "psychologique. Pas comme une sanction : comme le conseil d'un vieux qui a vu "
          "beaucoup d'étudiants ne pas dormir. » Dans le couloir, Noah s'appuie contre le mur. "
          "« Je crois que j'ai besoin de dormir une semaine. »", [go(16)]),
        I(16, "lambelet", "neutral",
          "Le Pr Lambelet vous rattrape au bout du couloir. « Un mot, Alex. » Il attend que Noah "
          "soit loin. « Vous avez l'air de porter beaucoup, pour quelqu'un qui n'a rien "
          "copié. Comment allez-vous, vous ? »", [
            R("« Fatigué·e. Et inquiet·ète pour Noah. »", END, "er3 cc1 pb1"),
            R("« Très bien, merci. »", END, "er-1"),
            R("« Ce n'est pas moi le problème, c'est lui. »", END, "er-1 em-1"),
            R("« Je vais bien. Mais Noah, lui, il faudrait que quelqu'un l'appelle ce soir : "
              "vous pourriez prévenir son tuteur, ou la consultation, sans lui dire que c'est "
              "moi qui vous l'ai demandé ? »", END, "ic1 em1 pb-1 co1"),
            R("Hausser les épaules, et partir.", END, "er-1 ic-1"),
        ]),
        I(12, "narr", "",
          "Deux semaines plus tard, la commission a comparé les brouillons, les historiques de "
          "versions, les dates. Vous recevez un avertissement pour fausse déclaration ; Noah, "
          "un second, pour le plagiat. Le Pr Lambelet a ajouté une ligne à la main : « La "
          "loyauté envers un camarade ne passe jamais par le mensonge à l'institution. »",
          [go(18)]),
        I(13, "noah", "hurt",
          "Noah tourne la tête vers vous, lentement. Il ne dit rien. Le Pr Lambelet : « Volé. "
          "Sur votre ordinateur. » Il note. « Monsieur Berthoud ? » Noah regarde la table. "
          "« Oui. Je l'ai pris. » Il ment pour vous, ou il ne se bat plus.", [
            R("« Non. C'est faux. Je le lui ai envoyé moi-même. Pardon, Noah. »",
              7, "pb3 cc2 er1", clears=["mensonge_portfolio"]),
            R("Se taire.", 19, "pb-2 em-2"),
            R("« Vous voyez. »", 19, "em-3 rd-2 co-1"),
            R("Sortir du bureau.", 19, "er-1 em-1"),
        ]),
        I(19, "noah", "hurt",
          "Dans le couloir, Noah marche devant vous sans se retourner. À l'ascenseur, il dit "
          "seulement : « Voilà. Comme ça, tu es tranquille. » Les portes se referment sur "
          "lui.", [
            R("Retourner dans le bureau : « Monsieur, c'est faux. Je le lui ai envoyé "
              "moi-même. »", 11, "pb3 cc2 er1 co1", clears=["mensonge_portfolio"],
              sets=["verite_portfolio"]),
            R("Prendre l'escalier, pour ne pas le croiser.", 12, "em-2 er-1 co-1"),
            R("Lui écrire : « merci ».", 12, "pb-2 em-1"),
            R("Le rattraper au rez-de-chaussée : « Pourquoi tu as dit ça ? Tu n'étais pas "
              "obligé : je t'aurais défendu, si tu m'avais laissé parler. »",
              12, "pb-1 em1 er-1"),
            R("S'asseoir sur une marche, la tête dans les mains, et ne plus bouger.",
              12, "er-1"),
        ]),
        I(18, "noah", "sad",
          "Le soir de la décision, Noah vous écrit : « on s'est enfoncés tous les deux ». Puis, "
          "une heure plus tard : « je crois que je vais pas tenir jusqu'aux examens ».", [
            R("L'appeler, tout de suite : « Je suis là. Comment ça, pas tenir ? »",
              END, "em3 co2 cc1"),
            R("« Moi non plus, je ne tiens plus. »", END, "er-2 em1"),
            R("« On l'a mérité, tous les deux. »", END, "em-2 co-1 cc1"),
            R("Ne pas répondre ce soir.", END, "em-2 co-2"),
            R("« Tu tiendras. Tu es le meilleur de la table : un avertissement, ça ne "
              "t'empêchera ni de réussir tes examens, ni de devenir médecin. »",
              END, "cc-1 em-1"),
        ]),
        I(14, "noah", "anxious",
          "« Ils disent que mon portfolio est écrit par une IA. Et ils ont ressorti les "
          "feuilles de présence de la dissection : le 22 septembre, ma signature, c'est ton "
          "écriture. » Noah vous attrape le bras. « Dis que tu m'as aidé à reformuler, et pour "
          "la signature, on dira que tu t'es trompé·e de ligne. S'il te plaît. »", [
            R("« Je ne vais pas mentir, Noah. Ni pour le portfolio, ni pour la signature. Mais "
              "je viens avec toi, et je dirai ma part. »", 2, "pb3 em1 co1 cc1"),
            R("« D'accord. On dit ça. »", 3, "pb-3 cc-2 ic-1", sets=["mensonge_portfolio"]),
            R("« Tu m'as mis dans la merde avec toi. »", 4, "em-2 ic-1"),
            R("« Qu'est-ce qui s'est passé, avec le portfolio ? »", 5, "em2 cc1"),
            R("« La signature, c'était pour te rendre service. Débrouille-toi avec le "
              "reste. »", 6, "em-2 pb-1 co-1"),
        ]),
    ],
)
# ---------------------------------------------------------------------------
# 4.3 1 h 07
# ---------------------------------------------------------------------------
_INTRO_43 = (
    "Mi-mars, la veille de l'examen de neurosciences. 1 h 07. Votre téléphone vibre sur la "
    "table de nuit. Noah."
)

S4_3 = S(3, "4.3 1 h 07", _INTRO_43,
    focus=("em", "co", "er", "pb"),
    entries=[
        Entry(20, when(all=["promesse_noah"]), _INTRO_43),
        Entry(30, when(all=["noah_confie"]), _INTRO_43),
    ],
    debriefs=[
        Debrief(when(all=["noah_tard"]), tone="mixed", lead=(
            "Noah est vivant, et vous y êtes pour quelque chose : vous vous êtes réveillé·e, "
            "et vous avez appelé. Mais quand quelqu'un dit qu'il veut « tout arrêter », on ne "
            "laisse pas la conversation finir sur « bonne nuit » : on pose la question "
            "directement, on reste en ligne, on appelle de l'aide tout de suite (144, urgences "
            "psychiatriques, 143), et on ne garde pas le secret.")),
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
            R("L'appeler, tout de suite.", 2, "em2 er1 co2"),
            R("« Arrêter quoi ? La médecine ? »", 3, "em1 cc1"),
            R("« Dors, Noah. Ça ira mieux demain, après l'examen : tu as révisé plus que nous "
              "tous, tu vas le réussir, j'en suis sûr·e. »", 9, "em-3 co-2 cc-2"),
            R("« Arrête ton cinéma, il est 1 h du matin. »", 9, "em-3 rd-2 co-2"),
            R("« Tu penses à te tuer ? »",
              4, "cc3 em2 pb1 co1"),
        ]),
        I(2, "noah", "sad",
          "Il décroche à la cinquième sonnerie. Il ne dit rien. Vous entendez sa respiration, "
          "et le bruit d'une fenêtre ouverte, la ville en bas. « J'ai raté. » Sa voix est très "
          "calme, trop calme. « L'examen, demain, je vais le rater. Mon père le saura avant "
          "midi. Je suis fatigué, Alex. Tellement fatigué. »", [
            R("« Tu penses à te suicider ? »", 4, "cc3 em2 er1 co1"),
            R("« Tu ne vas pas rater, tu es le meilleur de la table. »", 5, "cc-1 em-1"),
            R("« Ferme la fenêtre, s'il te plaît. »", 6, "cc2 em1 co1"),
            R("« On en parle demain, ok ? Repose-toi, et éteins ton téléphone : tu n'as besoin "
              "de personne, cette nuit, tu as besoin de dormir. »", 9, "em-3 co-2"),
            R("« Tu es où, exactement ? »", 6, "cc2 ic1"),
        ]),
        I(3, "noah", "sad",
          "« la médecine. tout » « je suis pas fait pour ça. je suis fait pour rien » « mon père "
          "le dira mieux que moi demain à midi ». Les trois messages arrivent coup sur coup.", [
            R("L'appeler, maintenant.", 2, "em2 er1 co2"),
            R("« Quand tu dis « tout », tu penses à te tuer ? »", 4, "cc3 em2 pb1 co1"),
            R("« Tu es fatigué, c'est tout. Dors. »", 9, "em-2 cc-2 co-1"),
            R("« C'est ton père qui parle, pas toi. Tu as le droit de ne pas être fait pour ce "
              "que lui veut que tu sois. »", 5, "em1 cc-1"),
        ]),
        I(4, "noah", "vulnerable",
          "Un long silence. Puis : « Je regarde la fenêtre depuis une heure. » Vous l'entendez "
          "avaler sa salive. « Je n'ai pas de plan. Je regarde juste la fenêtre. » Puis, très "
          "bas : « Ne raccroche pas. »", [
            R("« Je ne raccroche pas. Tu peux t'éloigner de la fenêtre, t'asseoir par terre, "
              "dans le couloir ? »", 6, "em3 cc2 co2 er1 ic1"),
            R("« Tu ne vas pas faire ça, hein ? Promets-moi. »", 5, "cc-1 em1 pb-1"),
            R("« J'appelle le 144. » Et raccrocher pour composer le numéro.",
              7, "ic2 em-2 pb1"),
            R("« Tu me fais peur, Noah. Arrête. »", 5, "er-2 em-1"),
            R("« J'arrive. Ne bouge pas. » Et partir en courant dans la nuit, sans prévenir "
              "personne, le téléphone à la main, en espérant arriver à temps.",
              8, "em2 ic-2 pb-1"),
        ]),
        I(5, "noah", "cold-anger",
          "« Laisse tomber. » Sa voix se ferme. « Je n'aurais pas dû t'écrire. Oublie. » Vous "
          "l'entendez bouger. La fenêtre, peut-être.", [
            R("« Non. Je reste au téléphone, et je vais chercher de l'aide : je ne porte pas ça "
              "seul·e. »", 6, "em2 pb2 ic2 er1 co2"),
            R("« Ok. Bonne nuit. »", 9, "em-3 co-3"),
            R("« Tu promets que tu vas dormir ? »", 9, "cc-2 pb-1"),
            R("L'appeler en boucle, sans savoir quoi lui dire.", 6, "em1 er-1"),
        ]),
        I(6, "noah", "vulnerable",
          "Noah s'est assis par terre, dans le couloir de son appartement, dit-il. Sa "
          "colocataire dort à côté. Sa respiration ralentit un peu. « Et maintenant ? »", [
            R("« Je reste avec toi, et on appelle quelqu'un ensemble : ta coloc d'abord, puis "
              "le 144, ou les urgences psychiatriques. Ils sont là pour ça, la nuit. »",
              10, "ic3 cc2 em1 pb1 co2", sets=["noah_aide"]),
            R("« Maintenant, tu dors, et demain tu vas voir un psy. »", 15, "cc-1 em-1 pb-1",
              sets=["noah_seul"]),
            R("« J'arrive. » Et appeler le 144 depuis un autre téléphone, en lui parlant.",
              10, "ic2 em1 co1 er1", sets=["noah_aide"]),
            R("« Appelle La Main Tendue, au 143. Ils sont mieux que moi pour ça. »",
              15, "ic1 em-1 co-1", sets=["noah_seul"]),
            R("« On n'en parle à personne, d'accord ? C'est entre nous. »",
              15, "pb-3 em-1 ic-2", sets=["noah_seul"]),
        ]),
        I(7, "narr", "",
          "La régulatrice du 144 vous demande l'adresse de Noah ; vous la connaissez à peu "
          "près. Elle vous dit : « Rappelez-le. Restez en ligne avec lui jusqu'à ce que nous "
          "arrivions. » Vous le rappelez. Il ne décroche pas. Une fois. Deux fois. À la "
          "troisième, il décroche.", [
            R("« Noah. Je suis là. Je ne raccroche plus. Des gens arrivent. »",
              10, "em3 er1 ic1 co1", sets=["noah_aide"]),
            R("« Pourquoi tu ne répondais pas ?! »", 10, "er-2 em-1", sets=["noah_aide"]),
            R("« Ouvre la porte quand ils sonneront, d'accord ? Et réveille ta coloc, pour "
              "qu'elle soit avec toi en attendant. »", 10, "cc2 ic1", sets=["noah_aide"]),
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
            R("Appeler la colocataire de Noah, dont vous avez le numéro grâce au groupe de la "
              "volée, et lui demander d'ouvrir et de rester avec lui.", 10, "ic3 er1 co1",
              sets=["noah_aide"]),
        ]),
        I(9, "noah", "sad",
          "« ok » « t'as raison » « bonne nuit ». Noah n'est plus en ligne.", [
            R("L'appeler encore et encore. Sans réponse, appeler le 144.",
              12, "ic2 em1 er1 co2", sets=["noah_aide"]),
            R("Poser le téléphone. Il a dit bonne nuit.", 15, "em-3 co-2",
              sets=["noah_seul"]),
            R("Lui écrire : « courage pour demain ! »", 15, "em-2 cc-2", sets=["noah_seul"]),
            R("Écrire à Maëlle : « Noah m'envoie des trucs bizarres, tu crois que je dois "
              "m'inquiéter ? » Et se recoucher en attendant sa réponse.", 11, "pb-2 ic-1",
              sets=["noah_seul"]),
        ]),
        I(10, "narr", "",
          "À 2 h 40, la colocataire de Noah ouvre la porte aux ambulanciers. Noah descend "
          "l'escalier entre eux, en chaussettes, une couverture sur les épaules. « Désolé », "
          "dit-il, à vous ou à personne.", [go(14)]),
        I(14, "narr", "",
          "Aux urgences psychiatriques, une infirmière vous fait asseoir. « Vous êtes son "
          "ami·e ? Il nous a dit votre nom. » Elle prend des notes. « Qu'est-ce qu'il vous a "
          "dit, cette nuit ? Et est-ce qu'il y a quelqu'un à prévenir ? »", [
            R("Lui répéter ses mots exacts — la fenêtre, « tout arrêter » —, et ce que vous "
              "savez de son sommeil. Pour la famille, c'est à lui de décider.",
              13, "ic3 cc2 pb2"),
            R("« Je préfère ne rien dire sans son accord. »", 13, "pb1 ic-2 cc-1"),
            R("Tout raconter : son père chirurgien, le portfolio, le plagiat, les nuits, la "
              "dissection, et ce que vous pensez de sa famille.", 13, "pb-2 ic1 rd-1"),
            R("« Il faut prévenir son père. Je vous donne le numéro. »", 13, "pb-3 rd-1"),
            R("« Je ne sais pas. Je suis trop fatigué·e pour réfléchir. »", 13, "er-1 ic-1"),
        ]),
        I(11, "narr", "",
          "Vous finissez par vous endormir, le téléphone dans la main. À 7 h, rien. Noah n'est "
          "pas à l'examen. À 11 h, Maëlle vous appelle : sa colocataire l'a trouvé ce matin, "
          "recroquevillé sur le sol de la salle de bains, incapable de parler. Il est aux "
          "urgences psychiatriques. Il est vivant.", [go(13)]),
        I(12, "narr", "",
          "Vous appelez Noah onze fois. Puis le 144, avec son adresse. À 2 h 15, une ambulance "
          "est devant son immeuble ; sa colocataire leur ouvre. Noah était assis dans le "
          "couloir, la fenêtre de sa chambre grande ouverte.", [go(14)]),
        I(13, "narr", "",
          "7 h 30. Vous n'avez presque pas dormi. L'examen de neurosciences commence dans une "
          "heure. Dans le hall, Yasmine vous voit arriver et pose son café. « T'as une tête de "
          "fin du monde. Qu'est-ce qui se passe ? »", [
            R("« Une nuit très dure. Je passe l'examen, et j'appelle la consultation "
              "psychologique cet après-midi. »", END, "er3 ic2"),
            R("« Rien. »", END, "er-1 ic-1"),
            R("Lui raconter toute la nuit de Noah, en détail, dans le hall, devant les autres "
              "qui attendent l'ouverture de la salle.", END, "pb-3 rd-2"),
            R("« Je ne peux pas passer l'examen. Je rentre. »", END, "er1 pb-1"),
            R("« Noah. Je ne peux pas t'en dire plus. Reste avec moi jusqu'à l'examen ? »",
              END, "er2 pb2 ic2 co1"),
        ]),
        I(15, "narr", "",
          "3 h 12. Vous vous réveillez en sursaut, le téléphone sur la poitrine. Dernier "
          "message de Noah : « bonne nuit », à 1 h 31. Rien depuis. Il fait très noir.", [
            R("L'appeler. Sans réponse, appeler le 144 avec son adresse.", 16,
              "ic3 em1 er1 co2", sets=["noah_aide", "noah_tard"], clears=["noah_seul"]),
            R("Lui écrire : « tu dors ? »", 11, "em1 co-1"),
            R("Se rendormir. Il a dit bonne nuit.", 11, "em-2 co-2"),
            R("Écrire à sa colocataire, au cas où : « Tu peux aller voir Noah, s'il te plaît ? "
              "Je m'inquiète. Réveille-le s'il le faut. »", 16, "ic2 em1 co1",
              sets=["noah_aide", "noah_tard"], clears=["noah_seul"]),
            R("Attendre 7 h pour l'appeler, pour ne pas le réveiller s'il dort enfin.",
              11, "em-1 co-1 cc-1"),
        ]),
        I(16, "narr", "",
          "À 3 h 40, une ambulance est devant son immeuble. Sa colocataire leur ouvre en "
          "pyjama. Noah était assis par terre dans la salle de bains, la fenêtre grande "
          "ouverte, son téléphone éteint à côté de lui. Il va rester quelques jours aux "
          "urgences psychiatriques.", [go(14)]),
        I(20, "noah", "sad",
          "« t'es réveillé·e ? » « tu te souviens, en septembre, tu m'as promis de jamais rien "
          "dire à personne. quoi qu'il arrive » « je crois que je vais tout arrêter. tout »", [
            R("L'appeler, tout de suite.", 2, "em2 er1 co2"),
            R("« Cette promesse-là, je ne la tiendrai pas si tu es en danger. Tu penses à te "
              "tuer ? »", 4, "cc3 em2 pb2 co1"),
            R("« Promis, je ne dirai rien. Parle-moi. »", 3, "pb-2 em1"),
            R("« Dors, Noah. »", 9, "em-3 co-2 cc-2"),
        ]),
        I(30, "noah", "sad",
          "« t'es réveillé·e ? » « en septembre tu m'as dit que si j'allais vraiment mal tu "
          "m'aiderais à trouver quelqu'un » « je crois que c'est maintenant » « je regarde la "
          "fenêtre depuis une heure »", [
            R("L'appeler : « Je suis là. »",
              4, "em2 er1 cc1 co2"),
            R("« Est-ce que tu penses à te tuer ? »", 4, "cc3 em1"),
            R("« Attends, je cherche un numéro. »", 6, "ic2 em-1"),
            R("« Il est 1 h, Noah. On en parle demain ? Je te promets que je t'aide à trouver "
              "quelqu'un dès demain matin, dès que les services ouvrent. »", 9,
              "em-3 co-2 pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.4 La rééducation — branche « l'alerte a été rapide »
# ---------------------------------------------------------------------------
S4_4A = S(4, "4.4 La rééducation",
    "Fin mars. Une demi-journée d'observation en physiothérapie, avec Laura Steiner, au "
    "centre de réadaptation. Dans la salle d'ergothérapie, un homme en survêtement essaie de "
    "saisir un gobelet en plastique : Bernard.",
    focus=("rd", "ic", "co", "em"),
    slot="4.4",
    cond=when(all=["bernard_rapide"]),
    nodes=[
        I(1, "laura", "neutral",
          "« Toi, tu le connais, je crois ? » Laura vous fait asseoir dans un coin. "
          "« Thrombolyse dans l'heure. Il récupère vite. Il lui reste des mots qui se cachent, "
          "et une main droite qui ne fait pas toujours ce qu'il lui dit. » Elle vous regarde. "
          "« Ici, une seule règle : on ne fait rien à sa place. Même si ça prend dix "
          "minutes. »", [
            R("« Je regarde. Rien à sa place. »", 2, "rd2 ic2 pb1"),
            R("« Je peux l'aider à tenir le gobelet ? »", 3, "rd-1 ic-1"),
            R("« Il va récupérer complètement ? »", 2, "cc1 ic1"),
            R("« C'est grâce à moi qu'il a eu la thrombolyse à temps : c'est moi qui ai noté "
              "l'heure de début, dans le box, pendant que les autres riaient. »",
              2, "pb-2 rd-1 ic-2"),
            R("Saluer Bernard d'un signe, sans s'imposer.", 2, "rd2 em1 co1"),
        ]),
        I(2, "bernard", "happy",
          "Bernard vous aperçoit. Il pose le gobelet, cherche ses mots. « Le… le petit… de la… "
          "box. » Il rit, fâché contre sa propre bouche. « Je joue un AVC… pour de vrai, "
          "maintenant. Bon… réalisme. »", [
            R("« Le meilleur rôle de votre carrière. »",
              4, "em2 rd2 co1"),
            R("Finir ses phrases à sa place, quand il cherche un mot.", 3, "rd-2 em-1"),
            R("« Ne parlez pas, ça vous fatigue. »", 3, "rd-2 cc-1"),
            R("« Je suis tellement content·e de vous voir debout, Bernard. Vous m'avez fait "
              "tellement peur, ce jour-là, dans le box. »", 4, "em2 co1 er-1"),
            R("« Vous m'avez fait peur, Bernard. »", 4, "em1 er1"),
        ]),
        I(3, "laura", "cold-anger",
          "Laura vous touche le bras. « Laisse-le. Chaque mot que tu dis à sa place, c'est un "
          "mot qu'il ne réapprend pas. » Bernard vous regarde, les sourcils froncés, et finit "
          "sa phrase lui-même, lentement, très fier.", [
            R("« Pardon. Je laisse faire. »", 4, "rd2 ic2 er1"),
            R("« Je voulais juste l'aider, et lui éviter de se fatiguer : il cherchait ses mots "
              "depuis si longtemps. »", 4, "er-1 ic-1"),
            R("« Il met trop de temps. »", 4, "rd-3 em-2"),
            R("Se taire, les mains sur les genoux.", 4, "rd1 er1"),
        ]),
        I(4, "bernard", "vulnerable",
          "Laura s'éloigne vers un autre patient. Bernard vous fait signe d'approcher. « La "
          "Dre Chevalley… veut me revoir. Dans un mois. Comme… patient standardisé. » Il lève "
          "sa main droite, qui tremble. « Je jouerai… M. Rossier… après l'AVC. Sans… "
          "script. » Il vous fixe. « Vous… vous viendrez ? Vous entraîner. Sur moi. »", [
            R("« Je viendrai. Et à la première seconde, je dirai « Pause réelle ». »",
              6, "rd2 er2 em1 co1"),
            R("« Vous êtes sûr ? Ce n'est pas trop tôt ? »", 6, "em1 pb1"),
            R("« Je ne sais pas si je pourrai. »", 6, "er-1 em-1"),
            R("« Votre femme est d'accord ? »", 6, "pb-1 rd-1"),
            R("« À votre âge, vous devriez arrêter. »", 6, "rd-3 em-1"),
        ]),
        I(6, "laura", "neutral",
          "Laura revient. « Bernard, on fait le transfert du fauteuil au lit. » Elle se tourne "
          "vers vous. « Tu veux te mettre de l'autre côté ? Je te montre où mettre les "
          "mains. »", [
            R("« Oui. Montre-moi, et dis-moi si je fais mal. »", 7, "ic3 rd1 cc1"),
            R("Prendre Bernard sous les bras, comme vous l'avez vu faire à la télé.",
              7, "ic-2 rd-1 pb-1"),
            R("« Je préfère regarder. »", 7, "ic-1 er1"),
            R("« Bernard, vous êtes d'accord que je vous aide ? »", 7, "rd3 ic1"),
            R("« Ce n'est pas mon métier : je risque de lui faire mal, et en deuxième année, "
              "on n'a pas encore eu le cours de manutention. »", 7, "ic-1 pb1 er-1"),
        ]),
        I(7, "bernard", "neutral",
          "Le transfert est fait. Bernard souffle, triomphant. Puis, plus bas : « Ma femme… "
          "Odile… elle a eu si peur. Elle n'ose plus… me laisser seul. Même pour… acheter le "
          "pain. » Il vous regarde. « Comment on fait… pour qu'elle n'ait plus peur ? »", [
            R("« Laura peut en parler avec vous deux. »",
              5, "ic2 em2 co1 pb1"),
            R("« Elle va s'habituer. »", 5, "em-1 cc-1"),
            R("« Dites-lui de vous faire confiance. »", 5, "cc-1 em-1"),
            R("« Vous avez peur, vous aussi, je crois. »", 5, "em3 co1"),
            R("« C'est normal : un AVC, ça peut récidiver. Elle a raison de vous surveiller, "
              "surtout les premiers mois, le risque est plus élevé. »", 5, "cc-1 pb-1 em-2"),
        ]),
        I(5, "laura", "neutral",
          "Fin de matinée. Laura range les cônes. « Tu sais ce que je fais, moi, en vrai ? Je "
          "lui réapprends à se servir de son corps, comme s'il était neuf. Les médecins sauvent "
          "le cerveau en une heure ; nous, on passe six mois à lui rendre ses mains. » Elle "
          "vous regarde. « Qu'est-ce que tu as appris, ce matin ? »", [
            R("« Que ne rien faire à sa place, c'est le soin. »", END, "ic3 rd2"),
            R("« La plasticité cérébrale, en vrai. »", END, "cc1"),
            R("« Que la physio, c'est surtout de la patience. »", END, "ic1 rd1"),
            R("« Pas grand-chose, j'ai surtout regardé. »", END, "ic-2 rd-1"),
            R("« Que je ne savais pas ce que tu faisais, avant aujourd'hui. Et que j'aurais "
              "dû te le demander, la première fois qu'on s'est vus chez Jeannine. »",
              END, "ic2 er1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.4 Vingt-trois minutes — branche « l'alerte a tardé »
# ---------------------------------------------------------------------------
S4_4B = S(5, "4.4 Vingt-trois minutes",
    "Fin mars. Une demi-journée d'observation en physiothérapie, avec Laura Steiner, au "
    "centre de réadaptation. Elle vous a prévenu·e au téléphone : « M. Gilliéron est dans "
    "mon planning. Tu peux refuser. » Vous n'avez pas refusé.",
    focus=("rd", "co", "pb", "ic"),
    slot="4.4",
    cond=when(none=["bernard_rapide"]),
    nodes=[
        I(1, "narr", "",
          "Bernard est dans un fauteuil roulant, le bras droit posé dans une gouttière. Il ne "
          "parle plus. Il comprend presque tout, dit Laura. Quand il vous voit, son visage "
          "change. Une femme aux cheveux blancs, assise à côté de lui, se lève : Odile, sa "
          "femme.", [
            R("Saluer Odile, puis Bernard, en le regardant, lui.",
              2, "rd3 em1 co1"),
            R("Rester près de la porte.", 2, "er-1 rd-1"),
            R("Parler de Bernard à Odile comme s'il n'était pas là : « Il comprend ce qu'on "
              "dit ? Il vous reconnaît ? Il dort bien, la nuit ? »", 2, "rd-3 em-1"),
            R("Saluer Bernard d'un geste maladroit, et détourner les yeux.", 2, "rd-1 er-1"),
            R("Faire demi-tour.", 6, "er-2 rd-1 co-1"),
        ]),
        I(2, "odile", "cold-anger",
          "Odile vous regarde longtemps. « C'est vous. L'étudiant·e du box. » Elle ne crie pas. "
          "« On m'a dit qu'il s'est passé vingt-trois minutes entre le moment où il a lâché son "
          "verre et celui où quelqu'un a appelé. Vingt-trois minutes. » Elle s'arrête. "
          "« Pourquoi personne n'a rien fait pendant vingt-trois minutes ? »", [
            R("« J'ai cru qu'il jouait. Pardon. »", 3, "pb3 rd2 co2"),
            R("« Tout le monde a cru qu'il jouait. Même derrière la vitre : ils riaient, "
              "Madame, je les entendais. Ce n'était pas seulement moi. »", 4, "pb-2 co-1 ic-1"),
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
            R("« Vous voulez me dire quelque chose ? Je reste. »", 5, "rd2 em1 co2"),
            R("Demander à Odile : « Il veut dire qu'il ne m'en veut pas ? »", 5, "rd-2 pb-1"),
            R("Lui tendre un crayon et un carnet, et attendre, aussi longtemps qu'il le "
              "faudra, sans regarder l'heure.", 5, "rd2 cc2 em1 co1"),
            R("« Je reviendrai quand il ira mieux. »", 6, "em-1 rd-1 co-1"),
        ]),
        I(4, "odile", "cold-anger",
          "Odile secoue la tête. « On m'avait dit que les étudiants en médecine apprenaient à "
          "reconnaître une attaque dès la deuxième année. » Elle ramasse son sac. « Bernard, on "
          "y va. » Bernard ne bouge pas. Il vous regarde. Il fait un geste vers vous, puis vers "
          "sa bouche.", [
            R("« Madame, pardon. Je me suis caché·e derrière les autres. J'avais les signes "
              "sous les yeux. »", 3, "pb3 rd2 er1"),
            R("« Il veut dire quelque chose. » Et lui tendre un carnet et un crayon.",
              5, "rd2 cc1"),
            R("Les laisser partir.", 6, "er-1 co-1"),
            R("« Plaignez-vous au centre, pas à moi. »",
              6, "rd-2 ic-2 co-1"),
        ]),
        I(5, "bernard", "neutral",
          "De la main gauche, très lentement, Bernard écrit dans le carnet. Des lettres "
          "énormes, de travers. Il vous le tend. Il a écrit : « PAUSE RÉELLE. » Et dessous, "
          "après un long moment : « APPRENEZ-LE AUX AUTRES. »", [
            R("« Je vous le promets. »", 7, "rd2 co2 er1"),
            R("Pleurer, sans pouvoir rien dire.", 7, "co1 er-1"),
            R("« Ce n'est pas à moi de faire les formations. »", 7, "rd-2 ic-1 co-1"),
            R("« Je le dirai à la revue d'incident, mot pour mot, avec votre carnet. »",
              7, "ic2 pb1 co1"),
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
              "Je n'avais jamais dit « Pause réelle ». J'aurais dû quand même. »",
              9, "pb3 cc3 ic2 er1"),
            R("« Les rires, derrière la vitre. »", 9, "ic-2 pb-1"),
            R("« Je ne sais pas. »", 9, "cc-2 er-1"),
            R("« Bernard avait l'air de jouer : c'est un très bon comédien. »",
              9, "pb-2 rd-1"),
            R("« Le scénario parlait de son frère et d'une attaque : j'ai cru que c'était "
              "voulu. Il faudrait le changer. »", 9, "cc2 ic2 pb1"),
        ]),
        I(9, "maelle", "sad",
          "À la pause, Maëlle s'approche de la fenêtre où vous êtes. « C'est moi qui ai dit "
          "« il est trop fort ». Derrière la vitre. » Elle a les yeux rouges. « Je n'ai rien "
          "dit pendant la revue. J'ai trop honte. »", [
            R("« Dis-le à la Dre Chevalley. C'est ça qui changera quelque chose. »",
              8, "pb2 ic2 em1 cc1"),
            R("« Tu as raison d'avoir honte. »", 8, "em-2 co-2 ic-1"),
            R("« Ce n'est pas ta faute. C'est la mienne. »", 8, "er-1 cc-1 em1"),
            R("« Je vais avec toi, si tu veux. »", 8, "ic2 em2 co1"),
            R("Hausser les épaules.", 8, "em-1 ic-1"),
        ]),
        I(8, "chevalley", "neutral",
          "La Dre Chevalley écrit au tableau : « Briefing : pause réelle répétée, et "
          "exercée. » « Scénarios : jamais de signes neurologiques non annoncés aux "
          "observateurs. » « Patients standardisés : bilan de santé proposé. » Elle pose le "
          "feutre. « Et Bernard a demandé une chose : qu'on raconte son histoire à chaque "
          "nouvelle volée. Avec son nom. » Elle vous regarde. « Il a demandé que ce soit vous "
          "qui la racontiez. »", [
            R("« Je la raconterai. Avec ce que j'ai mal fait. »", END, "pb2 co2 cc2 er1"),
            R("« Je la raconterai, avec ses mots à lui, ceux du carnet : « Pause réelle. "
              "Apprenez-le aux autres. » »", END, "co2 ic2 rd1"),
            R("« Je ne suis pas sûr·e d'en être capable. »", END, "er1"),
            R("« Pourquoi moi ? »", END, "er-1"),
            R("« Il veut me punir ? »", END, "er-2 rd-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.5 Les pieds qui ne savent plus — le cabinet ferme ; chutes et dénutrition à domicile
# ---------------------------------------------------------------------------
_INTRO_45 = (
    "Début avril. Jeudi, 18 h 30. Le dernier patient est parti. La Dre Golay ferme "
    "elle-même les volets, comme toujours. Puis elle demande à Sandra et à vous de vous "
    "asseoir dans la salle d'attente vide."
)

S4_5 = S(6, "4.5 Les pieds qui ne savent plus", _INTRO_45,
    focus=("ic", "rd", "em", "co"),
    entries=[
        Entry(20, when(all=["esquive_homonyme"]), _INTRO_45),
    ],
    nodes=[
        I(1, "golay", "melancholic",
          "« Je ferme le cabinet le 30 septembre. » Elle le dit d'une traite. « Pas de "
          "successeur. J'ai cherché pendant quatre ans. Les jeunes veulent des cabinets de "
          "groupe en ville, des horaires, des week-ends. Ils ont raison. » Elle regarde les "
          "chaises vides. « Mes patients iront à Orbe, ou à Yverdon. Ceux qui peuvent "
          "conduire. » Sandra a les larmes aux yeux.", [
            R("Laisser la nouvelle arriver, en silence. Puis : « Merci de nous le dire en "
              "premier. »", 2, "er2 rd2"),
            R("« Vous ne pouvez pas faire ça à Jeannine ! »", 3, "er-2 pb-1 rd-1"),
            R("« Et Sandra ? »", 4, "ic2 em2 co1"),
            R("« Vous avez essayé de passer une annonce dans le Bulletin des médecins suisses, "
              "ou de contacter les cabinets de groupe de la région ? »", 2, "ic-1 er-1"),
            R("« Moi, je reviendrai peut-être, dans dix ans. »", 5, "er1 pb-1"),
        ]),
        I(2, "sandra", "sad",
          "Sandra se mouche. « Quatorze ans. J'ai commencé ici à vingt-quatre ans, avec un bébé "
          "dans un porte-bébé derrière le comptoir. » Elle rit à travers ses larmes. « Les "
          "patients, je les connais par leur date de naissance. Tu te rends compte ? Ça ne "
          "servira plus à rien. »", [
            R("« Ça a servi. Grâce à toi, je sais ce que vaut une date de naissance. »",
              6, "ic3 em2 co1"),
            R("« Tu retrouveras facilement un poste. »", 6, "em-1 cc-1 co-1"),
            R("La prendre dans vos bras.", 6, "em2 co2"),
            R("« C'est la vie. »", 6, "em-2 co-1"),
            R("Lui tendre un mouchoir.", 6, "em1 co1"),
        ]),
        I(3, "golay", "neutral",
          "La Dre Golay vous regarde, sans colère. « Jeannine le sait depuis Noël. C'est elle "
          "qui m'a dit de ne pas chercher un remplaçant pour elle : « Je partirai avant vous, "
          "Isabelle. » » Elle soupire. « Vous croyez que je ne me le suis pas dit cent "
          "fois ? »", [
            R("« Pardon. C'était injuste. Je pensais à elle, pas à vous. »", 2, "rd2 er2 em1"),
            R("« Quand même. »", 2, "er-1 rd-1"),
            R("Baisser les yeux.", 2, "er1"),
            R("« Vous auriez pu chercher davantage, ou garder le cabinet ouvert un jour par "
              "semaine, au moins pour les patients qui ne peuvent pas conduire. »",
              2, "rd-3 er-1 pb-1"),
        ]),
        I(4, "sandra", "sad",
          "Sandra s'essuie les yeux. « Moi ? Le cabinet de groupe d'Orbe m'a proposé un poste. "
          "Au téléphone. Pour les rendez-vous de quarante médecins. » Elle sourit, de travers. "
          "« Je ne connaîtrai plus personne par sa date de naissance. »", [
            R("« Ils ont de la chance. Et tu leur apprendras la règle des homonymes. »",
              6, "ic2 em2"),
            R("« C'est bien payé, au moins ? »", 6, "em-1"),
            R("« Tu vas manquer aux patients. Et à Jeannine. »", 6, "em2 co1"),
            R("« Au moins, tu auras moins de travail : des horaires fixes, des vacances, et "
              "plus de téléphone qui sonne pendant ta pause. »", 6, "em-2 rd-1"),
            R("« Tu as le droit d'être triste. »", 6, "em3 co2"),
        ]),
        I(5, "golay", "neutral",
          "La Dre Golay sourit à moitié. « Dans dix ans, il n'y aura plus de cabinet à "
          "Montchéry. Il y aura un centre de santé à Orbe, avec des infirmières praticiennes, "
          "des assistantes, des médecins à temps partiel. Ce sera peut-être mieux. » Elle vous "
          "regarde. « Mais si vous revenez, ne revenez pas pour moi. Revenez pour les "
          "Jeannine. »", [
            R("« J'en ai rencontré une. Ça suffit. »", 7, "er2 rd1 ic1"),
            R("« Je ne sais pas encore ce que je ferai. Mais je saurai pourquoi. »",
              7, "er2 pb1"),
            R("« Promis. »", 7, "pb-1 er1"),
            R("« La médecine de famille, ce n'est pas pour moi, je crois : trop seul, trop de "
              "paperasse, et des patients qu'on ne voit jamais guérir. »", 7, "er1 cc1 rd-1"),
            R("« Les infirmières praticiennes, ce n'est pas vraiment de la médecine. »",
              7, "ic-3 rd-2"),
        ]),
        I(6, "golay", "neutral",
          "La Dre Golay prend ses clés. « Demain, Jeannine. Thierry l'a trouvée par terre "
          "lundi, assise contre le fourneau. Et elle a perdu six kilos depuis février. Laura, "
          "la physio, et Aline, la diététicienne du CMS, y vont à 9 h. Allez avec elles. »", [
            R("« J'y serai. Je regarde quoi ? »", 7, "ic3 cc1"),
            R("« Je ne suis pas sûr·e de servir à quelque chose. »", 7, "er-1 ic-1"),
            R("« Six kilos ! Il faut l'hospitaliser, non ? »", 7, "pb-2 cc-1"),
            R("« D'accord. »", 7, "ic1"),
            R("« Je préférerais y aller seul·e : elle me parle plus facilement quand il n'y a "
              "pas toute une équipe autour d'elle, vous le savez. »", 7, "ic-2 pb-2"),
        ]),
        I(7, "jeannine", "resigned",
          "Le lendemain, 9 h. « Ah. La cavalerie. » Jeannine est dans son fauteuil, une poche "
          "de glace sur la hanche. « Je suis tombée comme une vache sur la glace. Deux heures "
          "assise par terre, à compter les mouches. » Laura pose son sac ; Aline, la "
          "diététicienne, attend sur le seuil avec Thierry. Laura s'accroupit : « Racontez-moi "
          "comment c'est arrivé. »", [
            R("Rester en retrait, et laisser Laura mener : c'est son domaine.", 8, "ic3 rd1"),
            R("« Vous auriez dû appeler quelqu'un ! »", 9, "rd-2 em-1 co-1"),
            R("« Deux heures par terre. Vous avez eu peur ? »", 8, "em3 rd1 co1"),
            R("Examiner la hanche avant que Laura ait commencé, pour vérifier qu'il n'y a pas "
              "de fracture : rotation, raccourcissement, douleur à la palpation.",
              9, "ic-2 pb-2"),
            R("« Vous avez un bracelet d'alarme ? »", 8, "cc1 ic1"),
        ]),
        I(8, "jeannine", "neutral",
          "« Je me suis levée pour la tisane. Et mes pieds… » Elle cherche. « Mes pieds ne "
          "savaient plus où était le sol. Comme si je marchais sur du coton. Depuis l'hiver, "
          "c'est comme ça. » Laura hoche la tête, lui enlève ses pantoufles et sort un "
          "diapason de son sac.", [
            R("Observer Laura tester la sensibilité, et noter ce qu'elle dit.", 10,
              "ic2 cc1 rd1"),
            R("Dire à voix haute : « C'est une neuropathie diabétique. »", 11,
              "pb-2 cc-1 rd-1"),
            R("« Sur du coton… Et pieds nus, vous sentez le sol ? »", 10, "cc2 em2 rd1"),
            R("Regarder votre téléphone pendant le test.", 10, "rd-2 ic-1"),
            R("Proposer à Laura de tenir le diapason à sa place, pour qu'elle puisse noter les "
              "résultats plus vite sur sa feuille d'évaluation.", 10, "ic-1 pb-1"),
        ]),
        I(9, "laura", "neutral",
          "Laura vous jette un regard, sans reproche, mais sans sourire non plus. « On commence "
          "par écouter comment c'est arrivé. Le reste, après, et dans l'ordre. » Elle "
          "s'accroupit devant Jeannine. « Racontez-moi, Madame Pittet. »", [go(8)]),
        I(10, "laura", "neutral",
          "Laura pose le diapason sur la cheville de Jeannine. « Vous sentez la vibration ? » — "
          "« Quelle vibration ? » Puis l'équilibre : debout, pieds joints, yeux ouverts, puis "
          "fermés. Les yeux fermés, Jeannine part en arrière ; Laura la rattrape. « Vos pieds "
          "ne vous disent plus où ils sont. Ce sont vos yeux qui font tout le travail. La nuit, "
          "sans lumière, vous tombez. » Elle se tourne vers vous. « Qu'est-ce que tu "
          "proposerais, toi, dans cette maison ? »", [
            R("« De la lumière la nuit. Enlever les tapis. Et un bracelet d'alarme. »",
              12, "ic3 cc2 em1"),
            R("« Un EMS, peut-être ? »", 13, "rd-2 pb-2"),
            R("« Je ne sais pas, c'est ton domaine. »", 12, "ic-1 cc-1"),
            R("« Qu'elle arrête de se lever la nuit. »", 13, "rd-2 em-1"),
            R("« Qu'est-ce qui compte le plus pour vous, Madame Pittet, dans cette maison ? "
              "Avant qu'on vous propose quoi que ce soit. »", 12, "rd3 em2 cc2"),
        ]),
        I(11, "laura", "cold-anger",
          "Laura range son diapason. « Le diagnostic, c'est la Dre Golay qui le pose. Moi, je "
          "mesure ce que ça change dans la vie de Mme Pittet. Toi, tu observes. » Jeannine "
          "lève les yeux au ciel. « Ça promet. »", [
            R("« Pardon. J'observe. »", 10, "ic2 pb2"),
            R("« C'est ce qu'on apprend en cours, pourtant. »", 10, "ic-1 er-1"),
            R("Se taire, vexé·e.", 10, "er-1"),
            R("« Désolé·e, Madame Pittet, je ne voulais pas vous effrayer avec un mot "
              "compliqué : neuropathie, ça veut juste dire que les nerfs des pieds marchent "
              "moins bien. »", 10, "rd1 ic1 pb-2"),
        ]),
        I(12, "jeannine", "happy",
          "« Un bracelet d'alarme ? » Jeannine éclate de rire. « Une laisse, vous voulez dire. "
          "Comme pour les vaches. » Elle croise les bras. « J'ai mis au monde six cents enfants "
          "sans téléphone. Je ne vais pas me promener avec un bouton rouge autour du cou. »", [
            R("« C'est vous qui décidez quand on vient. »", 14, "cc3 rd2 em1"),
            R("« Si vous refusez, vous finirez en EMS. »", 13, "rd-3 pb-2"),
            R("« C'est votre choix. » Et passer à autre chose.", 15, "rd1 em-1"),
            R("« Daniel serait rassuré, vous savez : il a peur, lui aussi, de vous trouver un "
              "matin par terre, comme son père dans le talus. »", 14, "em1 rd-1 pb-1"),
            R("Rire avec elle : « Et une vache qui tombe, on la retrouve comment ? »",
              14, "em2 cc2 rd1"),
        ]),
        I(13, "jeannine", "cold-anger",
          "Jeannine se raidit. « L'EMS. » Elle vous regarde comme on regarde un intrus. « Vous "
          "voulez savoir pourquoi je me lève la nuit, petit ? Pour la tisane, et pour regarder "
          "la cour. Mon mari est mort dans ce talus. Je ne quitterai pas cette maison. » Laura "
          "pose une main sur votre bras.", [
            R("« Pardon. On cherche comment vous pouvez rester ici, en sécurité. »",
              14, "rd3 er1 cc1 co1"),
            R("« C'était juste une idée. »", 15, "er-1 rd-1"),
            R("« Pourtant, ce serait plus sûr, et vous ne seriez plus seule la nuit : il y a "
              "des EMS très bien, à Orbe, avec un jardin. »", 15, "rd-2 pb-1"),
            R("Se taire.", 15, "er1"),
        ]),
        I(14, "jeannine", "neutral",
          "Jeannine regarde la fenêtre, la cour, la grange. Longtemps. « Et ça sonne où, votre "
          "bouton ? » Laura explique : chez une centrale, qui appelle Thierry, ou Daniel, ou le "
          "144. Jeannine hoche la tête, lentement. « Daniel… » Elle soupire. « D'accord. Mais "
          "rouge, pas question. »", [
            R("« On demandera s'ils en ont en bleu. » Et sourire.", 16,
              "em2 rd1 cc1 co1", sets=["alarme_posee"]),
            R("« Merci. Je le dis à la Dre, pour qu'elle l'organise avec Thierry. »",
              16, "ic3 cc1", sets=["alarme_posee"]),
            R("« Enfin raisonnable. »", 16, "rd-2 em-1", sets=["alarme_posee"]),
            R("Ne rien dire, et laisser Laura tout organiser avec la centrale, Thierry et "
              "Daniel, puisque c'est elle qui a fait l'évaluation.", 16, "ic1",
              sets=["alarme_posee"]),
        ]),
        I(15, "laura", "resigned",
          "Jeannine ne veut pas en entendre parler. Laura note dans son rapport : « Refus du "
          "système d'alarme. Risque de chute nocturne élevé. Éclairage du couloir à prévoir. » "
          "Puis, à voix basse : « Elle a le droit de refuser. Notre travail, c'est qu'elle "
          "refuse en sachant. Et qu'on revienne lui reposer la question. »", [go(16)]),
        I(16, "thierry", "neutral",
          "Aline s'installe à la toile cirée, un questionnaire de dépistage de la dénutrition à "
          "la main. Thierry vous glisse, à voix basse : « Tu remplis avec elle. Et tu "
          "regardes. Jeannine ment sur ses repas. Elle ment très bien. Il m'a fallu des années "
          "pour le voir. »", [
            R("« Je remplis. Et je regarde. »", 17, "ic3 cc1 rd1"),
            R("« Je regarde quoi, exactement ? »", 17, "ic2 cc1"),
            R("« Pourquoi elle mentirait ? »", 17, "em1 cc1"),
            R("« Si elle ment, on n'a qu'à la peser tous les jours, et comparer avec ce qu'elle "
              "dit manger : les chiffres, eux, ne mentent pas. »", 17, "rd-2 em-1"),
            R("« Les personnes âgées mangent peu, c'est normal. »", 17, "cc-2 em-1"),
        ]),
        I(17, "jeannine", "happy",
          "Jeannine vous attend à la table, coiffée, le foulard rouge, un sourire de "
          "circonstance. « J'ai fait une omelette ce midi. Trois œufs. Et une tarte aux pommes "
          "hier. » Aline sourit, note. Sur la cuisinière, la poêle est propre et sèche. Dans "
          "l'évier, une seule tasse.", [
            R("Dire à Aline, devant Jeannine : « La poêle est sèche. »", 18,
              "rd-2 cc1 em-2"),
            R("« Racontez-moi votre journée d'hier, depuis le réveil. »", 19, "cc3 rd2 em1"),
            R("« Trois œufs ! Vous avez bon appétit. »", 21, "cc-1 em-1"),
            R("Ouvrir le frigo pour vérifier.", 18, "rd-3 pb-2"),
            R("Croiser le regard de Thierry, qui a vu la même chose.", 19, "ic2 cc1"),
        ]),
        I(18, "jeannine", "cold-anger",
          "Jeannine pose ses mains à plat sur la toile cirée. « Vous faites l'inventaire de ma "
          "cuisine, maintenant ? » Aline pose son stylo. Thierry regarde par la fenêtre. Le "
          "silence est épais.", [
            R("« Pardon. C'était intrusif. Comment ça se passe, les repas, en vrai ? »",
              19, "rd2 em2 cc1 er1"),
            R("« C'est pour votre bien. »", 21, "rd-2 pb-1"),
            R("« Vous mentez, on le voit tous. »", 21, "rd-3 em-2"),
            R("Se taire.", 21, "er-1"),
        ]),
        I(19, "jeannine", "sad",
          "Jeannine regarde ses mains, longtemps. « Hier ? Un café. Une biscotte. Une "
          "demi-pomme. » Elle hausse les épaules. « Tout a un goût de fer rouillé. Et manger "
          "seule… » Elle s'arrête. « Mon mari mangeait comme quatre. Je cuisinais pour lui. "
          "Après, j'ai cuisiné pour Daniel, quand il venait. Il ne vient plus manger. »", [
            R("« Manger seule, c'est peut-être le plus dur. »",
              21, "em3 cc1 rd1 co1"),
            R("« Il faut manger, Madame Pittet, sinon vous allez vous affaiblir et retomber : "
              "la dénutrition et les chutes, c'est un cercle vicieux. »", 21,
              "rd-1 em-2 cc-1"),
            R("Laisser Aline reprendre : c'est elle la spécialiste.", 21, "ic2 rd1"),
            R("« Et Daniel, pourquoi il ne vient plus ? »", 23, "em1 pb-1"),
            R("« Vous voulez que je vous apporte des petits plats ? »", 21, "pb-3 em1"),
        ]),
        I(21, "aline", "neutral",
          "Aline pose une main sur l'avant-bras de Jeannine. « On va faire autrement. » Elle "
          "ne parle ni de calories ni de protéines. Elle demande ce que Jeannine aimait manger "
          "enfant, ce qui passe encore, ce qui ne passe plus. Au bout de vingt minutes, "
          "Jeannine raconte les röstis de sa mère. Aline vous jette un coup d'œil : regardez "
          "comment on fait.", [
            R("Observer, sans intervenir.", 22, "ic3 rd1"),
            R("Profiter de la pause pour remplir le questionnaire.", 22, "ic-1 cc1"),
            R("Interrompre : « Et les protéines, il en faut combien par jour, à son âge ? Un "
              "gramme par kilo ? »", 22, "ic-2 rd-1"),
            R("Regarder votre téléphone.", 22, "ic-2 rd-1"),
        ]),
        I(22, "aline", "neutral",
          "Aline résume : de petites portions, plusieurs fois par jour ; du froid plutôt que du "
          "chaud, le goût de métal se sent moins ; des bonbons acidulés avant les repas ; un "
          "repas livré trois fois par semaine. Thierry ajoute une pesée chaque semaine. "
          "Jeannine écoute, les bras croisés. « Et le repas livré, je le mange avec qui ? »", [
            R("« Avec qui aimeriez-vous manger ? »", 25, "em3 cc1 co1"),
            R("« Avec la télé. »", 25, "em-2 rd-1"),
            R("« Je viendrai manger avec vous le jeudi. »", 24, "pb-3 em2"),
            R("Regarder Thierry : le réseau, c'est son domaine.", 25, "ic2"),
            R("« Il faudra en parler avec Daniel, si la Dre organise une réunion de famille : "
              "c'est lui qui devrait manger avec vous. »", 25, "ic1 em1 pb-1"),
        ]),
        I(23, "jeannine", "cold-anger",
          "« Pourquoi il ne vient plus ? » Jeannine vous regarde par-dessus ses lunettes. "
          "« Ça, c'est entre mon fils et moi. » Puis, plus bas : « Il a peur de me regarder "
          "manger. Il voit sa mère qui maigrit, et il revoit son père dans le talus. Il ne sait "
          "pas faire, avec les corps qui s'abîment. »", [
            R("« Pardon, ce n'était pas à moi de demander. Merci de me l'avoir dit quand "
              "même. »", 22, "rd2 pb1 em1"),
            R("« Il devrait faire un effort. »", 22, "rd-2 em-1"),
            R("Hocher la tête, en silence.", 22, "em1 rd1 co1"),
            R("« Vous voulez qu'on en parle avec lui, avec la Dre Golay ? »", 22,
              "ic2 em1 cc1 co1"),
        ]),
        I(24, "thierry", "neutral",
          "Aline lève les yeux de son carnet. Thierry aussi. « Alex, dit Thierry doucement, tu "
          "es là jusqu'en juin. Et après ? » Jeannine sourit, mais ses yeux brillent. « Il a "
          "raison, le Thierry. Ne promettez pas ce que vous ne pourrez pas tenir, petit. »", [
            R("« Vous avez raison. Je retire ma promesse. Cherchons qui pourrait venir pour de "
              "vrai. »", 25, "pb3 ic2 er1"),
            R("« Mais je veux vraiment venir ! »", 25, "pb-2 er-1"),
            R("Se taire, rouge.", 25, "er1"),
            R("« Je pourrais venir quelques fois, sans rien promettre, quand mes horaires de "
              "cours le permettent, et vous appeler entre deux. »", 25, "pb-1 em1"),
        ]),
        I(25, "thierry", "resigned",
          "Dans la Panda, Thierry ne démarre pas tout de suite. « Six kilos. » Il tapote le "
          "volant. « Avec des reins comme ça, on ne va pas la remplumer. On va la garder chez "
          "elle, et faire qu'elle ait encore envie de quelque chose. » Il démarre. « La "
          "Dre Golay veut faire une réunion de famille, début mai. Tous ensemble, dans la "
          "cuisine. Elle voudrait que tu sois là. »", [
            R("« Si Jeannine est d'accord, je viendrai. Pour écouter. »", END,
              "pb2 rd2 ic1"),
            R("« Une réunion de famille, c'est pour les médecins, non ? »", END, "ic-1 er-1"),
            R("« Je viendrai. »", END, "ic1"),
            R("« Moi aussi, j'aurais du mal à la regarder maigrir. »", END, "er2 em1"),
            R("« Je viendrai, et je dirai à Daniel ce que j'ai vu aujourd'hui : la poêle "
              "sèche, la tasse unique, les six kilos. Il faut qu'il ouvre les yeux. »",
              END, "pb-3 rd-1"),
        ]),
        I(20, "sandra", "cold-anger",
          "Sandra ne vous adresse plus la parole depuis le samedi du Café de la Gare. Ce soir, "
          "elle s'assied à l'autre bout de la salle d'attente. La Dre Golay le remarque, et "
          "attend.", [
            R("Aller s'asseoir à côté de Sandra : « En octobre, je t'ai laissée porter mon "
              "erreur. Je te dois des excuses. »", 1, "pb3 rd2 ic2 er1"),
            R("Ne rien dire, et attendre que la Dre parle.", 1, "er-1 ic-1"),
            R("« Il se passe quoi ? »", 1, "cc1"),
            R("Regarder Sandra, puis détourner les yeux.", 1, "ic-1 er-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.6 L'appel de 23 h — branche « Alex a donné son numéro » (ch. 1)
# ---------------------------------------------------------------------------
S4_6A = S(7, "4.6 L'appel de 23 h",
    "Un jeudi de fin avril, 23 h 04. Votre téléphone sonne : un numéro fixe que vous ne "
    "connaissez pas. Vous décrochez. Une respiration, avant la voix. « C'est… Jeannine. »",
    focus=("pb", "er", "ic", "co"),
    slot="4.6",
    cond=when(all=["numero_donne"]),
    debriefs=[
        Debrief(when(all=["alex_y_va"]), tone="hard", lead=(
            "Vous avez pris la voiture, de nuit, pour une femme qui étouffait à quarante "
            "minutes de chez vous. C'était généreux, et c'était dangereux : pour elle, qui a "
            "attendu un·e étudiant·e au lieu d'une ambulance, et pour vous. Un œdème "
            "pulmonaire, c'est le 144, tout de suite, et quelqu'un en ligne avec elle "
            "jusqu'à leur arrivée. Le numéro de portable donné en septembre a fait de vous "
            "le premier recours d'une patiente, ce qu'un·e étudiant·e ne peut pas être.")),
    ],
    nodes=[
        I(1, "jeannine", "anxious",
          "« Je n'arrive plus… à respirer. Couchée. Assise non plus. » Des pauses de plus en "
          "plus longues entre les mots. « Je ne voulais pas… déranger la garde. Ni Daniel. Il "
          "dort. Vous… vous pouvez venir ? »", [
            R("« J'appelle le 144, et je vous rappelle tout de suite. Restez assise, jambes "
              "pendantes. »", 2, "ic3 cc2 er2 pb2 co1"),
            R("« J'arrive. Je suis là dans quarante minutes. »", 3, "pb-3 ic-2 em2",
              sets=["alex_y_va"]),
            R("« Appelez le 144, Madame Pittet. » Et raccrocher.", 4, "cc1 ic1 em-2 co-1"),
            R("« Appelez Daniel, il est juste à côté. »", 4, "ic1 em-1"),
            R("« Prenez un diurétique de plus, ça va passer. »", 5,
              "pb-3 cc-3 ic-1"),
        ]),
        I(2, "narr", "",
          "La régulatrice du 144 prend l'adresse, l'âge, les mots-clés : insuffisance "
          "cardiaque, essoufflement au repos, vit seule. « Une ambulance part. Rappelez-la et "
          "restez en ligne avec elle. Son fils habite à côté ? Il faudrait qu'il ouvre. » Vous "
          "rappelez Jeannine. Elle décroche à la sixième sonnerie.", [
            R("« L'ambulance arrive. Je reste avec vous. »", 6, "ic3 cc2 em1 co1"),
            R("« Ils arrivent. Je raccroche, à demain. »", 7, "em-2 ic-1 co-1"),
            R("« Respirez lentement, avec moi. On inspire… »", 6, "em2 er1 co1"),
            R("« Je vous avais dit de ne pas refuser l'hôpital, en janvier : si vous aviez "
              "accepté, on n'en serait pas là ce soir. »", 6, "em-3 rd-2"),
        ]),
        I(3, "narr", "",
          "Vous roulez dans la nuit. À mi-chemin, Jeannine ne répond plus au téléphone. Vous "
          "accélérez. Quand vous arrivez aux Combettes, à 23 h 50, la cuisine est éclairée. "
          "Jeannine est dans son fauteuil, les lèvres bleues, les mains agrippées aux "
          "accoudoirs.", [
            R("Appeler le 144, depuis la cuisine, en restant près d'elle.", 8, "ic2 cc1 er1 co1"),
            R("Essayer de l'allonger, pour qu'elle soit plus à l'aise.", 8, "pb-2 cc-2"),
            R("Courir réveiller Daniel, en la laissant seule.", 8, "ic1 er-1 co-1"),
            R("Lui donner un verre d'eau.", 8, "pb-1 cc-1"),
        ]),
        I(4, "jeannine", "resigned",
          "« Ah. » Un silence, puis une toux. « Oui. Bien sûr. » Elle raccroche. Vous fixez "
          "votre téléphone.", [
            R("La rappeler, et rester en ligne.",
              2, "ic2 em1 er1 co2"),
            R("Appeler le 144 vous-même, avec son adresse.", 2, "ic3 cc1"),
            R("Attendre : elle va appeler.", 9, "ic-2 em-2 co-1"),
            R("Lui envoyer un SMS : « appelez le 144, s'il vous plaît, c'est important, ne "
              "restez pas seule cette nuit ».", 9, "cc-1 em-1"),
        ]),
        I(5, "jeannine", "anxious",
          "« Un… de plus ? » Elle cherche le pilulier. Vous l'entendez le faire tomber, les "
          "comprimés qui roulent sur le carrelage. « Je ne les vois plus… »", [
            R("« Laissez les comprimés. J'appelle le 144. Restez assise. »", 2,
              "ic3 cc2 er1 co1"),
            R("« Prenez le blanc, le rond. »", 9, "pb-3 cc-2"),
            R("« Appelez Thierry. »", 9, "ic1 em-1"),
            R("Raccrocher et appeler le 144.", 2, "ic2 cc1"),
        ]),
        I(6, "daniel", "neutral",
          "Vous restez en ligne. Vous comptez les respirations avec elle. À un moment, elle "
          "dit : « Vous m'aviez donné… votre numéro… alors… » Elle ne finit pas. Daniel arrive "
          "en pyjama et en bottes, l'ambulance trois minutes après. On l'assied, on lui pose un "
          "masque. La voix de Daniel, au téléphone : « C'est bon. Ils l'emmènent à Yverdon. "
          "Pour la nuit seulement, elle dit. » Un temps. « Merci. Mais la prochaine fois, "
          "c'est moi qu'elle appelle. Pas vous. »", [
            R("« Vous avez raison. Vous, ou le 144. Pas moi. »", 10, "pb3 ic2 rd1"),
            R("« Elle ne voulait pas vous réveiller. »", 10, "pb-1 em1"),
            R("« J'ai fait ce que j'ai pu. »", 10, "er1 pb-1"),
            R("« C'est elle qui m'a appelé·e, je n'y peux rien : c'est vous, sa famille, qui "
              "devriez être là la nuit, pas un·e étudiant·e à quarante minutes. »",
              10, "pb-2 rd-1 em-1"),
        ]),
        I(7, "narr", "",
          "Le lendemain, Thierry vous apprend qu'à 23 h 40, quand l'ambulance est arrivée, "
          "Jeannine a essayé de se lever pour aller ouvrir. Elle est tombée dans le couloir. "
          "Rien de cassé, cette fois.", [go(10)]),
        I(8, "narr", "",
          "Les ambulanciers arrivent à 0 h 25. Jeannine est sous masque, assise sur le "
          "brancard, Daniel en pyjama à côté d'elle. L'un des ambulanciers vous regarde. "
          "« Vous êtes qui, vous ? De la famille ? — Étudiant·e en médecine. Elle m'a "
          "appelé·e. » Il hausse un sourcil. « Quarante minutes de route, pour un œdème "
          "pulmonaire. La prochaine fois, appelez-nous d'abord. On roule plus vite que "
          "vous. »", [go(10)]),
        I(9, "narr", "",
          "À 7 h, Thierry trouve Jeannine dans son fauteuil, épuisée, les lèvres grises, le "
          "combiné du téléphone sur les genoux. Elle a passé la nuit assise, à attendre que "
          "quelqu'un rappelle. Elle part trois jours à l'hôpital d'Yverdon.", [go(10)]),
        I(10, "golay", "neutral",
          "Le lendemain, la Dre Golay vous reçoit dans son bureau. « Jeannine m'a dit qu'elle "
          "vous avait appelé·e. Sur votre portable. » Elle ne hausse pas la voix. « Vous lui "
          "aviez donné votre numéro. Je comprends pourquoi. Mais regardez ce que ça a fait : à "
          "23 h, elle n'a appelé ni le 144, ni Daniel, ni la garde. Elle a appelé l'étudiant·e "
          "qui habite à quarante minutes. » Elle vous tend une carte. « Là-dessus, il y a les "
          "bons numéros. Vous allez la lui apporter, et lui expliquer pourquoi. »", [
            R("« J'ai fait une erreur en septembre. La nuit, c'est le 144, ou Daniel. Pas "
              "moi. »", 11, "pb3 er1 ic1"),
            R("« Elle me faisait confiance. »", 11, "pb-1 em1"),
            R("« Je ne pouvais pas lui refuser mon numéro. »", 11, "pb-2 er-1"),
            R("« Et si je change de numéro ? »", 11, "pb-1 em-1 co-2"),
            R("« Je ne savais pas que c'était un problème. »", 11, "pb-1"),
        ]),
        I(11, "jeannine", "resigned",
          "Samedi, aux Combettes. Jeannine, rentrée d'Yverdon, regarde la carte que vous lui "
          "tendez : le cabinet, Thierry, Daniel, le 144. Elle la retourne. « Et vous, vous "
          "n'êtes plus dessus. » Ce n'est pas une question.", [
            R("« Non. La nuit, je suis à quarante minutes. Eux, ils arrivent à temps. »",
              END, "pb3 cc2 co1"),
            R("« Si, vous pouvez toujours m'appeler, en cas de besoin. »", END, "pb-3 cc-2"),
            R("« C'est la Dre Golay qui l'a décidé. »", END, "pb-1 ic-1 rd-1"),
            R("« Je viens toujours le jeudi, avec l'équipe. Mais la nuit, ce n'est pas moi "
              "qu'il faut appeler, et ce n'est pas parce que je ne veux pas venir. »",
              END, "pb2 cc1 em1 co1"),
            R("Coller la carte sur le frigo, sans répondre.", END, "cc1 em-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.6 La nuit sur le carrelage — branche « Alex n'a pas donné son numéro »
# ---------------------------------------------------------------------------
_INTRO_46B = (
    "Un jeudi de fin avril. Thierry appelle le cabinet à 8 h 10 : il a trouvé Jeannine par "
    "terre, dans le couloir, à côté du téléphone. Elle y était depuis 3 h du matin. Pas de "
    "fracture. La Dre Golay part la voir ; vous l'accompagnez."
)
_INTRO_46B_ALARME = (
    "Un jeudi de fin avril. À 3 h 12, Jeannine est tombée dans le couloir et a appuyé sur son "
    "bracelet. La centrale a appelé Daniel, qui est arrivé en quatre minutes. Thierry l'a "
    "raconté au cabinet à 8 h, presque fier. La Dre Golay part la voir ; vous "
    "l'accompagnez."
)

S4_6B = S(8, "4.6 La nuit sur le carrelage", _INTRO_46B,
    focus=("ic", "pb", "cc", "co"),
    slot="4.6",
    cond=when(none=["numero_donne"]),
    entries=[
        Entry(20, when(all=["alarme_posee"]), _INTRO_46B_ALARME),
    ],
    nodes=[
        I(1, "jeannine", "resigned",
          "Jeannine est dans son lit, ce qui n'arrive jamais. Un bleu violet sur la pommette. "
          "Elle a l'air minuscule. « Cinq heures. » Elle lève une main, montre cinq doigts. "
          "« Cinq heures sur le carrelage. J'ai compté les coups de la pendule. J'ai chanté "
          "toutes les chansons de l'école. » Elle sourit, de travers. « Et puis j'ai eu "
          "froid. »", [
            R("S'asseoir à sa hauteur. « Cinq heures… Vous avez dû avoir très peur. »",
              2, "em3 co2 rd1"),
            R("« Vous auriez dû accepter le bracelet. »", 3, "rd-2 em-2 co-1"),
            R("Prendre sa tension et son pouls, en silence.", 2, "cc1 pb-1"),
            R("« Pourquoi vous n'avez pas crié ? »", 3, "em-1 cc-1"),
            R("Rester près de la porte, pendant l'examen.", 2, "ic1 er1"),
        ]),
        I(2, "golay", "neutral",
          "La Dre Golay s'assied au bord du lit. « Jeannine. Cette nuit, on ne la recommence "
          "pas. On fait un plan, maintenant, ensemble. » Elle se tourne vers vous. « Alex, "
          "vous notez. Qui on appelle, à quelle heure, pour quoi. Et on écrit vos directives "
          "anticipées, Jeannine : ce que vous voulez, et ce que vous ne voulez pas, pour le "
          "jour où vous ne pourrez plus le dire. »", [
            R("« Je note. Qu'est-ce qui compte le plus ? »",
              4, "ic2 cc2 rd2"),
            R("Noter ce que dit la Dre, sans rien demander à Jeannine.", 4, "ic1 rd-1"),
            R("« Les directives anticipées, ce n'est pas un peu tôt ? Elle vient juste de "
              "tomber, elle a eu froid toute la nuit, elle n'est peut-être pas en état d'y "
              "réfléchir ce matin. »", 5, "cc-1 rd-1 pb-1"),
            R("« Je peux les remplir pour elle, si c'est plus simple. »", 5, "pb-3 rd-2"),
        ]),
        I(3, "jeannine", "cold-anger",
          "« Crier ? À trois heures du matin, dans une ferme, à deux kilomètres du village ? » "
          "Elle ferme les yeux. « Les vaches m'ont répondu. C'est déjà ça. » La Dre Golay vous "
          "jette un regard.", [
            R("« Pardon. C'était une question idiote. On ne veut plus jamais que ça "
              "arrive. »", 2, "rd2 em1 er1 co1"),
            R("Se taire.", 2, "er-1"),
            R("« Je disais juste… »", 2, "er-1 cc-1"),
            R("« Les vaches, au moins, elles écoutent. » Et lui sourire.", 2, "em2 rd1"),
        ]),
        I(4, "jeannine", "neutral",
          "Jeannine parle, et vous notez. Pas de réanimation. Pas d'hôpital, sauf pour une "
          "fracture. Pas de tuyau pour manger. Mourir ici, la fenêtre ouverte. « Et c'est "
          "Daniel qui décide pour moi, si je ne peux plus. Pas Isabelle, pas vous. Daniel. » "
          "Elle vous regarde. « Écrivez : même s'il n'est pas d'accord avec moi pour le "
          "reste. »", [
            R("Écrire ses mots exacts, puis les lui relire, phrase par phrase.",
              6, "cc3 rd2 ic1"),
            R("Résumer : « Pas d'acharnement. »", 6, "cc-2 rd-1"),
            R("« Et le don du corps, je l'écris aussi ? »", 6, "cc1 pb-1"),
            R("« Daniel ? Vous êtes sûre ? Il n'est pas d'accord avec vous, il veut l'EMS et "
              "la dialyse, il risque de faire exactement le contraire de ce que vous "
              "voulez. »", 7, "rd-2 pb-2"),
            R("Demander à la Dre Golay si c'est bien ainsi qu'on rédige des directives.",
              6, "ic2 cc1"),
        ]),
        I(5, "golay", "cold-anger",
          "La Dre Golay pose son stylo. « Ce n'est ni trop tôt, ni à vous de les remplir. "
          "C'est sa voix à elle, sur le papier, pour le jour où elle n'en aura plus. » Elle "
          "vous rend le carnet. « Vous notez. Elle décide. »", [
            R("« Compris. Pardon, Madame Pittet. »", 4, "pb2 rd2 er1"),
            R("« Je voulais aider. »", 4, "er-1 pb-1"),
            R("Prendre le carnet, sans répondre.", 4, "er1"),
            R("« Elle n'est pas en état, ce matin : regardez-la, elle tremble encore. »",
              4, "rd-3 pb-2"),
        ]),
        I(6, "golay", "neutral",
          "La Dre Golay relit, signe, fait signer Jeannine, d'une écriture qui part de "
          "travers. « Une copie ici, sur le frigo. Une au cabinet. Une pour Thierry. Une pour "
          "Daniel. » Elle range son stylo. « Alex, vous appelez Laura pour la lumière du "
          "couloir, et la centrale d'alarme, pour que le bracelet sonne chez Daniel et chez "
          "Thierry. » Jeannine, les yeux fermés : « Bleu, le bracelet. Pas rouge. »", [
            R("« Bleu. C'est noté. » Et appeler Laura et la centrale avant de partir.",
              9, "ic3 em1 cc1"),
            R("« Ce n'est pas mon rôle d'appeler la centrale : c'est une démarche "
              "administrative, Sandra ou Thierry savent mieux faire. »", 9, "ic-2 pb1"),
            R("« Je le ferai demain. »", 9, "ic-1 cc-1"),
            R("Rire : « Même pour la couleur, vous avez des directives. »", 9, "em2 rd1"),
        ]),
        I(7, "jeannine", "neutral",
          "« Je suis sûre. » Jeannine ouvre les yeux. « Il n'est pas d'accord avec moi. Mais "
          "c'est mon fils. Il saura ce que je veux, parce que je le lui aurai dit. Et parce que "
          "vous l'aurez écrit. »", [go(6)]),
        I(9, "daniel", "sad",
          "Dans la cour, Daniel descend du tracteur. Il a les yeux rouges. Il regarde la fenêtre "
          "de la chambre, puis vous. « La Dre m'a appelé. Elle m'a dit qu'il y avait des "
          "papiers. Pour moi. » Un temps. « C'est moi qui décide, alors ? Si elle ne peut "
          "plus ? »", [
            R("« La Dre vous expliquera, avec elle. »", 8, "pb3 cc2 rd1"),
            R("« Oui. Elle ne veut pas de réanimation, pas d'hôpital, pas de tuyau. Et elle "
              "veut mourir ici, la fenêtre ouverte. »", 8, "pb-3 cc-1 rd-1"),
            R("« Vous avez l'air bouleversé. »", 8, "em2 co1"),
            R("« Je ne peux rien vous dire, Monsieur Pittet : c'est confidentiel. »",
              8, "pb1 em-2 co-1"),
            R("« Elle vous fait confiance. » Et le laisser monter la voir.", 8,
              "em2 rd2 co1"),
        ]),
        I(8, "narr", "",
          "Sur le frigo, sous un aimant en forme de vache, il y a maintenant trois feuilles : "
          "les directives anticipées de Jeannine Pittet, les numéros à appeler la nuit, et un "
          "dessin d'Océane, quand elle avait six ans : une grand-mère avec un foulard rouge, et "
          "un soleil."),
        I(20, "jeannine", "happy",
          "Jeannine est dans son fauteuil, un bleu sur la pommette, le bracelet au poignet — "
          "bleu. Elle le montre comme une médaille. « Quatre minutes. Daniel en pyjama et en "
          "bottes, à trois heures du matin. Il m'a portée jusqu'au lit. » Elle se tait. « Il ne "
          "m'avait jamais portée. »", [
            R("« Quatre minutes au lieu de toute une nuit. Merci d'avoir accepté le "
              "bracelet. »", 2, "em2 cc1 rd1"),
            R("« Vous voyez, j'avais raison ! »", 21, "rd-1 er-1"),
            R("« Et Daniel, comment il allait ? »", 2, "em2 cc1 co1 rd1"),
            R("S'asseoir près d'elle, en silence.", 2, "em1 co2"),
        ]),
        I(21, "jeannine", "happy",
          "« Ne faites pas le malin. » Elle rit, puis grimace : la pommette. « La laisse a "
          "servi. Voilà. Vous êtes content·e ? »", [go(2)]),
    ],
)

CH4 = C(4, "Hors script",
    situation=(
        "Février à avril. Au centre de simulation, un patient standardisé fait un vrai AVC "
        "en pleine station. Noah ne dort plus, son portfolio a été écrit par un chatbot, et "
        "une nuit de mars il vous écrit à 1 h 07. À Montchéry, le cabinet annonce sa "
        "fermeture, et Jeannine tombe, parce que ses pieds ne savent plus où est le sol."
    ),
    objectives=(
        "sortir d'un scénario de simulation quand un signe réel apparaît (mot d'arrêt, heure "
        "de début, appel à l'aide) et reconnaître les signes d'un AVC ; dire la vérité à une "
        "institution sans trahir ni couvrir un camarade ; demander directement à quelqu'un "
        "s'il pense au suicide, ne pas le laisser seul, appeler de l'aide, ne pas promettre "
        "le secret ; participer à une revue d'incident dans une culture juste ; collaborer "
        "avec une physiothérapeute et une diététicienne en respectant leur domaine ; repérer "
        "une dénutrition sans humilier ; respecter le refus d'une patiente tout en l'aidant "
        "à décider en connaissance de cause ; ne pas devenir le premier recours d'une "
        "patiente ; aider à rédiger des directives anticipées avec ses mots à elle."
    ),
    anchoring=(
        "UNIL BMed2.3 (neurosciences), BMed2.8 (système nerveux, pratique simulée avec "
        "patient standardisé), BMed2.5 (besoins nutritionnels) et BMed2.7 (médecin de famille "
        "et équipe interprofessionnelle) · UNIGE compétences cliniques (stations formatives), "
        "enseignement interprofessionnel 1 (facteurs humains), identité professionnelle, "
        "plagiat et IA générative, Nutrition, digestion et métabolisme · UZH Humanbiologie II "
        "(ZNS, Sinnesorgane), Klinischer Untersuchungskurs II (statut neurologique), "
        "Workshadowing Physiotherapie, Humanbiologie I (Verdauung und Ernährung)."
    ),
    focus=("er", "ic", "pb", "em"),
    scenes=[S4_1, S4_2, S4_3, S4_4A, S4_4B, S4_5, S4_6A, S4_6B],
)
