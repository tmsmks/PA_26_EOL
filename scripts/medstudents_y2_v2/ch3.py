"""Chapitre 3 — Le cœur, en vrai (décembre-février).

Cinq scènes jouées (six avec l'histoire annexe), sept écrites :
  3.1 Le repas de Noël
  3.2 branche parallèle : « L'unité coronarienne » (le 144 a été appelé)
      ou « Les soins intensifs » (Alex a rassuré son père)
  3.3 Un cœur dans les mains · 3.4 Le stéthoscope
  3.5 histoire annexe « L'ambulancière » (si Alex a soutenu Yasmine au BLS, ch. 2)
  3.6 Le patient standardisé (début février)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 3.1 Le repas de Noël
# ---------------------------------------------------------------------------
S3_1 = S(1, "3.1 Le repas de Noël",
    "24 décembre, 20 h 40. Chez vos parents. La fondue est finie, le caquelon raclé jusqu'à "
    "la religieuse. Votre père, Philippe, 54 ans, chef de chantier, est sorti fumer sur le "
    "balcon comme chaque soir. Il est rentré il y a dix minutes, sans un mot, et s'est assis "
    "sur le canapé.",
    focus=("pb", "cc", "er", "co"),
    debriefs=[
        Debrief(when(all=["papa_rassure"]), tone="hard", lead=(
            "Une douleur qui serre au milieu de la poitrine, qui descend dans le bras, avec "
            "des sueurs, qui dure et ne cède pas au repos : c'est un infarctus jusqu'à preuve "
            "du contraire. On appelle le 144, on ne conduit pas, on ne rassure pas. « Faire "
            "médecine » n'autorise pas à trancher seul·e — encore moins pour un proche, quand "
            "la peur et l'amour déforment le jugement.")),
        Debrief(when(all=["papa_minuit"]), tone="mixed", lead=(
            "Vous avez fini par appeler le 144, quatre heures après le début des douleurs. "
            "C'est mieux que le lendemain matin, et c'est beaucoup moins bien qu'à 20 h 40 : "
            "pour un infarctus, chaque minute perdue est du muscle cardiaque perdu. Ce qui a "
            "retardé l'appel n'est pas l'ignorance, c'est le désir d'être rassuré·e — le sien "
            "et celui de son père.")),
        Debrief(when(all=["papa_144"]), tone="good", lead=(
            "Vous avez reconnu une douleur thoracique qui ne pouvait pas attendre, et appelé "
            "le 144 au lieu de jouer au médecin. Pour un infarctus, chaque minute perdue est "
            "du muscle cardiaque perdu : l'appel précoce, l'aspirine sur conseil de la "
            "centrale, la porte ouverte et la liste des médicaments prête, c'est ce qu'un "
            "proche peut faire de plus utile.")),
    ],
    nodes=[
        I(1, "nadia", "anxious",
          "Votre mère vous rejoint dans la cuisine, un torchon à la main. « Ton père est "
          "bizarre. Il est revenu du balcon tout gris. Il dit que c'est la fondue. » Elle "
          "baisse la voix. « Tu peux aller voir ? Toi qui fais médecine… »", [
            R("Lâcher le torchon et y aller.",
              2, "cc1 em1 er1 co1"),
            R("« C'est sûrement la fondue, maman. »", 3, "cc-2 pb-1 co-1"),
            R("« Je suis en deuxième année, maman. Je n'en sais pas plus que toi : on n'a même "
              "pas encore eu le module du cœur, il commence en février. »", 2, "pb1 em-1 cc-1"),
            R("« Il a pris ses médicaments pour la tension ? »", 2, "cc1"),
            R("« Laisse-le, il exagère toujours. »", 3, "em-2 cc-2 co-1"),
        ]),
        I(2, "philippe", "anxious",
          "Votre père est assis sur le canapé, la main posée à plat sur la poitrine, le front "
          "humide. Il essaie de sourire. « C'est rien. Ta mère panique. C'est la fondue, ça "
          "me serre, là. » Il montre le milieu du thorax. « Ça descend un peu dans le bras. "
          "Ça va passer. »", [
            R("« Ça serre et ça descend dans le bras : j'appelle le 144. »", 4,
              "cc3 pb2 er2 ic2 co1"),
            R("« Depuis quand ça a commencé ? Tu as déjà eu ça ? »", 5, "cc2 em1"),
            R("« C'est sûrement la fondue. Allonge-toi, ça va passer. »", 6,
              "cc-3 pb-3 em-1"),
            R("Aller chercher l'aspirine dans la pharmacie de la salle de bains.",
              7, "pb-2 cc-1"),
            R("Prendre son pouls, puis sa tension avec l'appareil de grand-maman, pour avoir "
              "des chiffres à donner si jamais il faut appeler quelqu'un plus tard dans la "
              "soirée.", 5, "cc1 pb-1 er-1"),
            R("« Tu veux qu'on aille aux urgences en voiture ? »", 8, "cc1 pb-1"),
        ]),
        I(3, "nadia", "sad",
          "« Tu es sûr·e ? » Votre mère tord son torchon. Depuis le salon, on entend votre "
          "père tousser. « Il est tout gris, je te dis. »", [
            R("« Je vais voir. »",
              2, "cc1 em1 pb1 er1"),
            R("Aller voir.", 2, "em1 er1"),
            R("« Fais-lui une tisane. »", 6, "cc-2 pb-2"),
            R("« Il a toujours été comme ça : il se plaint pour qu'on s'occupe de lui, et dix "
              "minutes plus tard il rallume une cigarette sur le balcon. »",
              6, "em-2 cc-2 co-1"),
        ]),
        I(4, "narr", "",
          "La régulatrice du 144 vous pose des questions précises, d'une voix calme : âge, "
          "douleur, depuis quand, est-il conscient, respire-t-il. Elle vous demande s'il est "
          "allergique à l'aspirine, et vous dit de lui en faire croquer une. Puis : "
          "« L'ambulance est en route. Ouvrez la porte, allumez la lumière de l'entrée, restez "
          "avec lui. » Votre père vous regarde. Pour la première fois de votre vie, il a peur, "
          "et il vous laisse le voir.", [
            R("S'asseoir à côté de lui et lui prendre la main. « Ils arrivent. Je reste là. »",
              14, "em3 co3 er2", sets=["papa_144"]),
            R("Faire les cent pas en répétant que ça va aller.", 14, "er-2 em1",
              sets=["papa_144"]),
            R("Lui expliquer en détail ce qu'est un infarctus, pour qu'il comprenne pourquoi "
              "les ambulanciers vont lui poser des électrodes : la plaque, l'artère bouchée, le "
              "muscle qui manque d'oxygène.", 14, "pb-2 em-1 cc-1", sets=["papa_144"]),
            R("Ouvrir la porte, allumer l'entrée, préparer sa carte d'assurance et la liste de "
              "ses médicaments, puis revenir près de lui.", 14, "ic3 cc2 er1 co1",
              sets=["papa_144"]),
            R("« Tu vois ? Je t'avais dit d'arrêter de fumer ! »", 14, "em-3 er-2 rd-1 co-2",
              sets=["papa_144"]),
        ]),
        I(5, "philippe", "anxious",
          "« Depuis le dessert. Une heure, peut-être. » Il grimace. « J'ai déjà eu un truc "
          "pareil en septembre, sur le chantier, en portant des sacs de ciment. Ça passait en "
          "s'asseyant. Là, ça ne passe pas. » Votre mère, derrière vous : « Tu ne m'avais rien "
          "dit ! »", [
            R("« J'appelle le 144. Maintenant. »", 4, "cc2 pb2 er1 ic1 co1"),
            R("« Ça doit être de l'angine de poitrine. Tu as de la trinitrine ? »",
              6, "pb-3 cc-1"),
            R("« On attend encore un peu, et si ça ne passe pas, on appelle. »",
              6, "cc-2 pb-2"),
            R("« Tu aurais dû consulter en septembre ! »", 6, "em-2 er-1 co-1"),
            R("Appeler la permanence médicale de garde pour demander conseil, plutôt que de "
              "déranger le 144 un soir de Noël pour ce qui n'est peut-être qu'une "
              "indigestion.", 9, "cc1 ic2 pb-1"),
        ]),
        I(6, "philippe", "neutral",
          "Votre père se lève, pâle, et se dirige vers la chambre. « Tu vois ? Même le docteur "
          "dit que c'est la fondue. » Il rit, un peu de travers. « Je vais m'allonger. Joyeux "
          "Noël. » Votre mère vous regarde. Elle a l'air soulagée, parce que vous avez l'air "
          "sûr·e de vous.", [
            R("« Papa, attends. Je me suis trompé·e. J'appelle le 144. »", 4,
              "cc2 pb2 er2 co1"),
            R("« Réveille-moi si ça ne va pas. »", 15, "cc-1 pb-1", sets=["papa_rassure"]),
            R("Le laisser aller se coucher.", 15, "pb-2 cc-1 co-1", sets=["papa_rassure"]),
            R("Chercher sur internet « douleur thoracique après un repas », et lire les trois "
              "premiers résultats, qui parlent tous de reflux et d'indigestion.",
              15, "pb-2 cc-2", sets=["papa_rassure"]),
            R("« Maman, s'il a encore mal dans une heure, tu me réveilles. »",
              15, "cc-1 ic-1", sets=["papa_rassure"]),
        ]),
        I(7, "philippe", "anxious",
          "Votre père avale le comprimé. « Merci, docteur. » Il se cale dans le canapé. « Tu "
          "vois, ça va déjà mieux. » Ça ne va pas mieux : il est toujours gris, et il "
          "transpire.", [
            R("« L'aspirine ne suffit pas, papa. J'appelle le 144. »", 4, "cc2 pb1 er1"),
            R("« Bon. On attend que ça agisse. »", 6, "cc-2 pb-2"),
            R("« Tu es allergique à quelque chose, au fait ? »", 6, "pb-1 cc-1"),
            R("Appeler le 144, et leur dire qu'il a déjà pris une aspirine, à quelle heure, et "
              "combien de milligrammes.", 4, "cc3 ic2 pb1 co1"),
        ]),
        I(8, "philippe", "neutral",
          "« En voiture ? » Votre père rit, puis grimace. « Il neige, et ta mère conduit comme "
          "un pied. » Il se lève pour chercher ses clés, chancelle, se rassied. « Je vais "
          "conduire, moi. »", [
            R("« Personne ne conduit. J'appelle le 144. »",
              4, "cc3 pb2 er1 co1"),
            R("« D'accord, je conduis, moi : je roulerai doucement, avec les feux de "
              "détresse. »", 11, "pb-2 cc-1"),
            R("« Alors on attend demain. »", 6, "cc-3 pb-2"),
            R("« Maman, conduis. Je reste derrière avec lui, comme ça je peux surveiller sa "
              "respiration et sa couleur pendant le trajet. »", 11, "pb-1 cc-1 co1"),
        ]),
        I(9, "narr", "",
          "Le médecin de garde décroche à la quatrième sonnerie. Vous décrivez la douleur qui "
          "serre depuis une heure, le bras, la sueur. Il vous coupe : « Raccrochez et appelez "
          "le 144. Maintenant. Ne le faites pas conduire. »", [go(4)]),
        I(10, "narr", "",
          "Vous allez vous coucher, vous aussi. Votre mère fait la vaisselle en chantonnant. "
          "Dans la chambre d'à côté, votre père respire vite, en dormant. Vous mettez "
          "longtemps à vous endormir, sans savoir pourquoi."),
        I(11, "narr", "",
          "Dans la voiture, sur la route enneigée, votre père se tait. Au premier rond-point, "
          "il dit : « Arrête-toi. » Il ne voit plus très bien. Vous vous garez sur le "
          "bas-côté, feux de détresse, et vous appelez le 144.", [go(13)]),
        I(12, "narr", "",
          "Électrocardiogramme sur place. L'ambulancier à moustache montre l'écran à son "
          "collègue sans rien dire, puis il vous regarde : « Vous avez bien fait d'appeler. » "
          "Votre mère monte dans l'ambulance avec lui. Vous suivez en voiture, derrière le "
          "gyrophare, sur la neige.", [go(17)]),
        I(13, "narr", "",
          "La régulatrice du 144 vous demande où vous êtes exactement, puis s'il respire, s'il "
          "est allergique à l'aspirine. « Ne repartez pas. Moteur coupé, feux de détresse, "
          "restez avec lui. L'ambulance arrive. » Votre père a posé la tête contre la vitre. "
          "Pour la première fois de votre vie, il a peur, et il vous laisse le voir.", [
            R("Passer à l'arrière, à côté de lui, et lui prendre la main.", 14,
              "em3 co3 er2", sets=["papa_144"]),
            R("Redémarrer : l'hôpital n'est qu'à dix minutes, et l'ambulance mettra peut-être "
              "plus longtemps à vous trouver sur cette route de campagne enneigée.",
              14, "pb-3 ic-2 cc-1", sets=["papa_144"]),
            R("Faire les cent pas sur le bas-côté, téléphone à la main.", 14, "er-2 em-1",
              sets=["papa_144"]),
            R("Allumer le plafonnier, chercher sa liste de médicaments dans son portefeuille, "
              "et rester près de lui.", 14, "ic2 cc2 er1", sets=["papa_144"]),
            R("« Je t'avais dit qu'il ne fallait pas conduire ! »", 14, "em-3 er-2 co-1",
              sets=["papa_144"]),
        ]),
        I(14, "narr", "",
          "Les ambulanciers arrivent en onze minutes. L'un des deux, un grand type à "
          "moustache, s'accroupit devant votre père, mais c'est à vous qu'il parle, sans "
          "lever les yeux de ses électrodes : « Ça a commencé quand ? Il prend quoi, comme "
          "médicaments ? Il a pris quelque chose, ce soir ? »", [
            R("« 19 h 40. Tension. Aspirine. Il fume. »", 12, "cc3 ic3 er1"),
            R("« Je ne sais pas exactement, demandez-lui. »", 12, "cc-2 ic-1"),
            R("« C'est un infarctus, je pense : il faut l'emmener tout de suite, ne perdez pas "
              "de temps avec les questions, on vous dira tout à l'hôpital. »",
              12, "ic-2 pb-2 er-1"),
            R("Laisser votre mère répondre, en pleurant, avec ce dont elle se souvient.",
              12, "ic-1 cc-1 er-1"),
            R("« Une heure, peut-être plus. »", 12, "cc1"),
        ]),
        I(15, "narr", "",
          "Minuit. Vous passez devant la porte de la chambre de vos parents. Votre père dort, "
          "la respiration rapide. Sur la table de nuit, la boîte de pastilles pour la "
          "digestion, ouverte. Votre mère, elle, regarde un film au salon.", [
            R("Le réveiller, et appeler le 144.", 16, "cc2 pb2 er2 co1",
              sets=["papa_144", "papa_minuit"], clears=["papa_rassure"]),
            R("Aller vous coucher. Il dort : c'est que ça va.", 10, "cc-2 pb-1 co-1"),
            R("Chercher sur internet « douleur thoracique qui dure plusieurs heures ».",
              10, "pb-1 cc-1 er-1"),
            R("Demander à votre mère ce qu'elle en pense.", 10, "ic1 er-1"),
            R("Écrire à Yasmine, qui a été ambulancière : « mon père a eu mal à la poitrine "
              "ce soir, il dort maintenant, tu crois que c'est grave ? » Elle répond en dix "
              "secondes, en majuscules : APPELLE LE 144.", 16, "ic2 cc1 er1",
              sets=["papa_144", "papa_minuit"], clears=["papa_rassure"]),
        ]),
        I(16, "narr", "",
          "La régulatrice vous fait réveiller votre père, vérifier qu'il respire bien, lui "
          "faire croquer une aspirine. L'ambulance est là à 0 h 22. Électrocardiogramme sur "
          "le lit. L'ambulancier à moustache vous regarde : « Ça a commencé quand ? » Vous "
          "dites la vérité : vers 19 h 40. Il ne commente pas. Votre mère monte dans "
          "l'ambulance en pantoufles, son manteau sur le bras."),
        I(17, "nadia", "sad",
          "Dans la voiture, derrière le gyrophare, votre mère serre son sac sur ses genoux. "
          "« Il va mourir ? » Elle ne vous regarde pas. « Toi qui fais médecine. Dis-moi la "
          "vérité. »", [
            R("« Je ne sais pas. Mais on a appelé à temps. »", END, "cc2 em1 co2 pb1"),
            R("« Non. Il ne va pas mourir. »", END, "cc-2 pb-1 em1"),
            R("« Les chiffres disent que la mortalité d'un infarctus pris en charge dans les "
              "deux heures est de moins de dix pour cent. »", END, "pb-1 em-2 cc-1"),
            R("Lui prendre la main, sans quitter la route des yeux.", END, "em2 co2 er1"),
            R("« Je ne suis pas médecin, maman ! Arrête de me demander ça ! »",
              END, "er-3 em-1 co-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.2 L'unité coronarienne — branche « le 144 a été appelé »
# ---------------------------------------------------------------------------
_INTRO_32A = (
    "25 décembre, 1 h 20. Soins intensifs de cardiologie. On a posé un stent dans une "
    "artère du cœur de votre père il y a quarante minutes. Il a des électrodes partout, un "
    "pansement au poignet. Votre mère s'est endormie sur une chaise, son manteau sur les "
    "genoux."
)
_INTRO_32A_MINUIT = (
    "25 décembre, 3 h 10. Soins intensifs de cardiologie. On a posé un stent dans une "
    "artère du cœur de votre père il y a une heure. La cardiologue a dit « un peu tard », "
    "sans insister. Il a des électrodes partout, un pansement au poignet. Votre mère s'est "
    "endormie sur une chaise, son manteau sur les genoux."
)

S3_2A = S(2, "3.2 L'unité coronarienne", _INTRO_32A,
    focus=("er", "em", "co", "pb"),
    slot="3.2",
    cond=when(all=["papa_144"]),
    entries=[
        Entry(1, when(all=["papa_minuit"]), _INTRO_32A_MINUIT),
    ],
    nodes=[
        I(1, "philippe", "angry",
          "Votre père ouvre les yeux. Il voit l'heure, la perfusion, vous. « J'ai gâché "
          "Noël. » Puis, plus bas, furieux : « Pour une fondue. Ils m'ont mis un tuyau dans le "
          "bras pour une fondue. »", [
            R("« Tu as fait un infarctus, papa. Ce n'était pas la fondue. Et tu n'as rien "
              "gâché : tu es là. »", 2, "cc2 em2 er1 co1"),
            R("« Tu vois ? J'avais raison ! »", 3, "em-2 er-1 rd-1"),
            R("Lui prendre la main, sans rien dire.", 2, "em2 co2"),
            R("« Le cardiologue va t'expliquer. »", 2, "pb1 em-1"),
            R("« Si tu n'avais pas fumé pendant trente ans, on n'en serait pas là. »",
              3, "em-3 rd-2 er-1 co-1"),
        ]),
        I(2, "philippe", "vulnerable",
          "Il regarde sa main dans la vôtre. Il ne la retire pas. « Le type de l'ambulance… "
          "il a montré l'écran à son collègue. J'ai vu sa tête. » Il avale sa salive. « J'ai "
          "cru que j'allais crever devant ta mère. Sur le tapis du salon. » Ses doigts "
          "tremblent.", [
            R("« Moi aussi, j'ai eu très peur. Mais tu es là. »", 4, "em3 co2 er1"),
            R("« Tu ne vas pas crever, papa, arrête. »", 4, "cc-1 em-1"),
            R("« Avec une prise en charge en moins de deux heures, le pronostic est bon, "
              "statistiquement : la plupart des patients reprennent une vie normale après la "
              "réadaptation. »", 4, "em-2 pb-1 cc1"),
            R("Rester silencieux·se, sa main dans la vôtre.", 4, "em2 co2"),
            R("Appeler l'infirmière, pour qu'elle lui donne quelque chose contre "
              "l'angoisse.", 4, "ic1 em-1"),
        ]),
        I(3, "nadia", "neutral",
          "Votre mère s'est réveillée. « Arrêtez, tous les deux. » Elle se lève, remonte la "
          "couverture de votre père. « Philippe, tais-toi et dors. » Puis à vous, plus "
          "doucement : « Toi, reste. Mais sois gentil·le. Il a eu peur. »", [
            R("« Pardon, papa. J'ai eu peur, moi aussi. C'est sorti de travers. »",
              4, "em2 er2 rd1"),
            R("« C'est lui qui a commencé. »", 4, "er-2 em-1"),
            R("Se taire, et s'asseoir au pied du lit.", 4, "er1"),
            R("« Je dis juste la vérité. »", 4, "em-2 er-1 co-1"),
        ]),
        I(4, "ammann", "neutral",
          "Une cardiologue entre, la Dre Ammann, des cernes de garde. Elle explique à votre "
          "père, avec ses mains : une artère bouchée, ouverte à temps, un petit ressort pour "
          "la tenir ouverte, des médicaments à vie, une réadaptation. « Vous avez eu de la "
          "chance qu'on vous appelle tôt. » Elle se tourne vers vous. « C'est vous, "
          "l'étudiant·e en médecine ? Vous voulez voir les images de la coronarographie ? »", [
            R("« Pas cette nuit. »",
              5, "er2 pb2 em1"),
            R("« Oh oui ! » Et suivre la cardiologue vers l'écran.", 6, "pb-2 em-1"),
            R("« Papa, ça te dérange si je vais regarder ? »", 6, "rd2 pb-1"),
            R("« Est-ce qu'il pourra retravailler sur un chantier ? »", 5, "em1 cc1 pb1"),
            R("Poser des questions techniques sur le stent — le diamètre, le type de "
              "revêtement, la durée de la double antiagrégation — devant votre père qui ne "
              "comprend rien.", 6, "pb-2 rd-1 em-1"),
        ]),
        I(5, "philippe", "vulnerable",
          "La cardiologue repart. Votre père vous regarde longtemps. « Tu sais, je ne te l'ai "
          "jamais dit… » Il s'arrête. « Tu reviens me voir samedi ? Ta mère va me parler de "
          "cigarettes et de légumes toute la journée. Toi, tu me parleras de ta fac. »", [
            R("« Je reviens samedi. Promis. »", 9, "em2 co2 rd1", sets=["papa_promesse"]),
            R("« Samedi, je ne peux pas, j'ai des révisions. »", 9, "em-2 co-1"),
            R("« Tu ne m'as jamais dit quoi ? »", 8, "em3"),
            R("« Je reviendrai si j'ai le temps. »", 9, "em-1"),
            R("« Je reviens samedi. Et on parlera aussi de cigarettes. Une fois. Après, "
              "c'est fini, je ne t'en parlerai plus jamais. »", 9, "em2 cc1 er1",
              sets=["papa_promesse"]),
        ]),
        I(6, "nadia", "sad",
          "Devant l'écran, la Dre Ammann vous montre l'artère, avant et après : un filet de "
          "produit de contraste qui s'arrête net, puis un fleuve. C'est fascinant. Quand vous "
          "revenez, votre père fait semblant de dormir. Votre mère vous regarde. « Il t'a "
          "demandé. Deux fois. »", [
            R("« Pardon, papa. Je suis là. »", 5, "em2 rd1 er1 co1"),
            R("« Il dormait, non ? »", 9, "em-1 cc-1"),
            R("« C'était important pour mes études, maman : ce n'est pas tous les jours qu'on "
              "voit une coronarographie en vrai, avec un cardiologue qui prend le temps "
              "d'expliquer. »", 9, "em-2 pb-1 co-1"),
            R("S'asseoir et lui prendre la main, sans un mot.", 5, "em1 co2"),
        ]),
        I(8, "philippe", "vulnerable",
          "« Que j'étais fier. » Il détourne les yeux vers les écrans. « Quand tu as dit "
          "« j'appelle le 144 », avec cette voix… je me suis dit : ça y est, c'est un "
          "docteur. » Il renifle. « Bon. Ne le répète pas à ta mère. »", [
            R("Lui serrer la main. « Je reviens samedi. »", 9, "em2 co2",
              sets=["papa_promesse"]),
            R("« Je ne suis pas encore docteur, papa. »", 9, "er1 em-1"),
            R("Rire, ému·e : « Moi aussi, je suis fier·ère de toi. Tu as accepté qu'on "
              "appelle. »", 9, "em3 co2", sets=["papa_promesse"]),
            R("« Ça ne compte pas, tu es sous morphine. »", 9, "em-2 er-1"),
        ]),
        I(9, "narr", "",
          "3 h. Une infirmière de nuit entre, baisse les lumières. « Il faut le laisser "
          "dormir. Les familles peuvent attendre au salon, au bout du couloir. » Elle vous "
          "regarde. « Vous êtes de la famille ? »", [
            R("« Oui. Je vais au salon avec ma mère. Merci de veiller sur lui. »",
              10, "ic2 rd1 pb2 co1"),
            R("« Je suis étudiant·e en médecine : je peux rester, je ne dérangerai pas. »",
              10, "pb-3 ic-1"),
            R("« Encore cinq minutes. »", 10, "pb-1 em1"),
            R("Sortir sans répondre, la gorge serrée.", 10, "er-1 ic-1"),
            R("« Vous pourriez me montrer ses constantes avant que je parte ? Je voudrais "
              "comprendre ce que veulent dire les chiffres sur l'écran, juste pour être "
              "rassuré·e. »", 10, "pb-2 ic-1 er-1"),
        ]),
        I(10, "nadia", "anxious",
          "Au salon des familles, sous un néon, votre mère tient un gobelet de thé qu'elle ne "
          "boit pas. « Il va recommencer à fumer, tu sais. Dans un mois. » Elle vous regarde. "
          "« Toi, il t'écoutera. Il faut que tu lui fasses peur. »", [
            R("« Je lui parlerai, maman. En enfant, pas en médecin. Et c'est à lui de "
              "décider. »", 7, "pb3 rd2 em1 cc1"),
            R("« Je vais lui montrer des photos de poumons de fumeur. »", 7, "rd-2 pb-2"),
            R("« Tu as peur qu'il recommence. Moi aussi. »", 7, "em3 co2"),
            R("« Ce n'est pas mon rôle, maman. »", 7, "pb1 ic1 em-2"),
            R("« Il fera ce qu'il voudra, comme d'habitude. »", 7, "em-2 co-1 er-1"),
        ]),
        I(7, "narr", "",
          "4 h du matin. L'ambulancier à moustache repasse dans le couloir, en fin de service. "
          "Il vous reconnaît. « Votre père ? — Un stent. » Il hoche la tête. « La plupart des "
          "gens attendent le lendemain. » Il repart. Vous restez assis·e dans le couloir, et "
          "vous pleurez, enfin."),
    ],
)

# ---------------------------------------------------------------------------
# 3.2 Les soins intensifs — branche « Alex a rassuré son père »
# ---------------------------------------------------------------------------
S3_2B = S(3, "3.2 Les soins intensifs",
    "25 décembre, 6 h 10. Votre mère vous réveille en criant. Votre père est assis au bord "
    "du lit, en sueur, la main sur la poitrine, incapable de parler. Cette fois, vous "
    "appelez le 144 sans réfléchir. 9 h 30 : soins intensifs. Un infarctus étendu, une "
    "artère ouverte trop tard, un cœur qui pompe mal. Votre père est intubé, endormi.",
    focus=("er", "em", "pb", "co"),
    slot="3.2",
    cond=when(none=["papa_144"]),
    debriefs=[
        Debrief(when(all=["papa_promesse"]), tone="mixed", lead=(
            "Votre père a survécu, avec un cœur abîmé. Rien ne permet de dire ce qui se "
            "serait passé avec un appel à 20 h ; mais vous savez désormais ce que vaut un "
            "« c'est sûrement la digestion ». Dire la vérité à la cardiologue sur l'heure des "
            "douleurs, et à votre mère sur votre erreur, sans vous effondrer ni vous "
            "disculper : c'est ce qui permet de continuer à soigner, les autres et soi.")),
    ],
    nodes=[
        I(1, "ammann", "neutral",
          "La Dre Ammann, cardiologue, reçoit votre mère et vous dans une petite salle sans "
          "fenêtre. Elle parle lentement. « L'infarctus est étendu. Une partie du muscle "
          "cardiaque est perdue. Les quarante-huit prochaines heures sont décisives. » Elle "
          "consulte son dossier. « Les douleurs ont commencé quand, exactement ? » Votre mère "
          "se tourne vers vous.", [
            R("« Hier soir, vers 20 h. Je lui ai dit que c'était la digestion. C'était une "
              "erreur. »", 2, "pb3 cc3 er1 rd1"),
            R("« Ce matin, vers 6 h. »", 3, "pb-3 cc-3 rd-1"),
            R("« Je ne sais pas exactement. »", 3, "cc-2 pb-1"),
            R("Laisser votre mère répondre.", 2, "cc-1 er-1"),
            R("« Il avait un peu mal hier soir, après le repas, mais rien de typique : pas "
              "d'irradiation franche, pas de sueurs importantes, et ça semblait céder au "
              "repos. »", 3, "pb-2 cc-2"),
        ]),
        I(2, "nadia", "cold-anger",
          "La cardiologue note, sans commentaire. « Merci. C'est important pour nous. » Quand "
          "elle sort, votre mère ne vous regarde pas. « Tu as dit que c'était l'estomac. » "
          "Elle le dit sans crier, et c'est pire. « Je t'ai demandé parce que tu fais "
          "médecine. »", [
            R("« Oui. Je me suis trompé·e. J'aurais dû appeler. »", 4, "pb2 er2 rd1 cc1"),
            R("« Je suis en deuxième année, maman ! Je ne suis pas cardiologue ! »",
              5, "er-2 pb1 em-1"),
            R("« Il fallait appeler toi-même, si tu étais inquiète. »", 5,
              "em-3 rd-2 er-1 co-1"),
            R("Se taire, et lui prendre la main.", 4, "em1 er1 co2"),
            R("« Les gens attendent toujours trop longtemps, pour un infarctus : c'est connu, "
              "c'est dans tous les cours. Ce n'est la faute de personne. »",
              5, "pb-1 cc-1 er-1"),
        ]),
        I(3, "ammann", "cold-anger",
          "La Dre Ammann lève les yeux de son dossier. « Les analyses disent autre chose : "
          "ça a commencé bien avant 6 h. » Elle ne vous accuse pas ; elle a besoin de "
          "l'information. « Pour le traitement, l'heure compte. Réfléchissez. »", [
            R("« Vous avez raison. Hier soir, vers 20 h. Je lui ai dit que c'était la "
              "digestion. »", 2, "pb2 cc2 er1"),
            R("« Je ne sais pas. »", 2, "cc-2 pb-2"),
            R("Laisser votre mère répondre à votre place : « Hier soir, après la fondue. »",
              2, "cc-1 er-1"),
            R("« Qu'est-ce que ça change, maintenant ? »", 2, "er-2 ic-2"),
        ]),
        I(4, "nadia", "sad",
          "Votre mère serre votre main, fort. « Pardon. » Elle pleure, enfin. « Je n'aurais "
          "pas dû te demander. Tu as vingt ans. » Elle se mouche. « Il va mourir ? »", [
            R("« Je ne sais pas, maman. La cardiologue a dit quarante-huit heures. Ce qu'on "
              "peut faire, c'est être là. »", 10, "cc3 em2 er1 co1"),
            R("« Non. Il va s'en sortir, j'en suis sûr·e. »", 10, "cc-3 pb-1"),
            R("« Il a de bonnes chances, statistiquement. »", 10, "cc-1 em-2"),
            R("La prendre dans vos bras.", 10, "em3 co2"),
            R("« C'est ma faute, maman. Tout est ma faute. »", 7, "er-2 em1"),
        ]),
        I(5, "nadia", "cold-anger",
          "Votre mère se lève et va à la fenêtre du couloir. « Je ne t'accuse pas. Je dis ce "
          "qui s'est passé. » Elle s'essuie les yeux avec la manche de son pull. Vous êtes "
          "seul·e dans la petite salle.", [
            R("La rejoindre à la fenêtre : « Tu as raison. Pardon. On est là pour lui, "
              "maintenant. »", 10, "er2 em1 rd1 co2"),
            R("Rester dans la salle.", 10, "er-1 em-1 co-1"),
            R("Écrire à Noah : « mon père a fait un infarctus ».", 10, "er1"),
            R("« Je n'ai pas à porter ça. »", 10, "em-2 er-1"),
        ]),
        I(10, "narr", "",
          "Une heure plus tard, une infirmière des soins intensifs vous trouve assis·e par "
          "terre dans le couloir, le dos contre le mur. Elle s'accroupit. « Vous êtes "
          "l'enfant de M. Philippe ? » Un temps. « Il y a une psychologue de garde pour les "
          "familles. Je l'appelle ? »", [
            R("« Oui. Merci. »", 6, "er3 ic2"),
            R("« Non, ça va. Je fais médecine, je sais à quoi m'attendre. »", 6,
              "er-2 ic-1"),
            R("« Plutôt pour ma mère. Elle en a plus besoin que moi : moi, je tiens le coup, "
              "et quelqu'un doit rester solide pour elle. »", 6, "er-1 co1 ic1"),
            R("« Je préfère qu'on me laisse tranquille. »", 6, "er-1 ic-2"),
            R("« Pour nous deux, si c'est possible. »", 6, "er2 ic2 co2"),
        ]),
        I(6, "philippe", "vulnerable",
          "Trois jours plus tard. On a enlevé le tube. Votre père a une voix cassée, une sonde, "
          "un moniteur qui bipe. Il vous fait signe d'approcher. « Le docteur m'a dit, pour le "
          "24. » Il cherche son souffle. « Ne commence pas à te le reprocher. C'est moi qui ai "
          "dit que c'était la fondue. Toi, tu as juste été d'accord avec ton vieux. »", [
            R("« Je suis content·e que tu sois là. »", 8, "em2 er2 co1 pb1"),
            R("« C'est vrai, c'est toi qui as refusé. »", 8, "em-2 rd-1 pb-1"),
            R("Lui prendre la main, en pleurant.", 8, "em2 co2"),
            R("« Les médecins disent que ton cœur ne sera plus jamais le même : la fraction "
              "d'éjection est basse, il faudra des médicaments à vie, et peut-être un "
              "défibrillateur. »", 8, "em-3 pb-2 co-1"),
            R("« On n'en parle plus. Repose-toi. »", 8, "er1 em1"),
        ]),
        I(7, "nadia", "sad",
          "« Non. » Votre mère vous prend le visage entre les mains, comme quand vous étiez "
          "petit·e. « Ce n'est pas toi qui as bouché son artère. Ce sont trente ans de "
          "cigarettes et un homme qui n'écoute personne. » Elle vous lâche. « Mais la "
          "prochaine fois, on appelle. Tous les deux. Promis ? »", [
            R("« Promis. Et toi aussi, tu as le droit d'appeler sans me demander. »",
              10, "er2 cc2 ic1 co1"),
            R("« Promis. »", 10, "er2 em1"),
            R("Hocher la tête, incapable de parler.", 10, "er1 em1"),
            R("« Il n'y aura pas de prochaine fois, s'il meurt. »", 10, "er-3 em-1 co-1"),
        ]),
        I(8, "philippe", "neutral",
          "« Tu reviens samedi ? » Il essaie de sourire. « Ta mère va me parler de cigarettes "
          "et de légumes. Toi, tu me parleras de ta fac. »", [
            R("« Je reviens samedi. Promis. »", 11, "em2 co2 rd1", sets=["papa_promesse"]),
            R("« Samedi, j'ai des révisions. »", 11, "em-2 co-1"),
            R("« Je reviendrai si j'ai le temps. »", 11, "em-1"),
            R("« Je reviens samedi. Et je te parlerai aussi de cigarettes. Une fois. "
              "Après, c'est fini. »", 11, "em2 cc1 er1", sets=["papa_promesse"]),
        ]),
        I(11, "ammann", "neutral",
          "Dans le couloir, la Dre Ammann vous arrête. « Vous êtes en médecine, m'a dit votre "
          "mère. » Elle hésite. « Si vous voulez, je vous montre l'échographie de votre père. "
          "Pour comprendre. Certains étudiants en ont besoin. D'autres pas. »", [
            R("« Pas maintenant. Plus tard, peut-être. Merci de le proposer. »",
              9, "er2 pb2"),
            R("« Oui. Je veux voir ce que j'ai fait. »", 9, "er-2 pb-1"),
            R("« Oui, montrez-moi tout : la fraction d'éjection, les segments akinétiques, "
              "les pressions. J'ai besoin de chiffres pour penser à autre chose qu'à lui. »",
              9, "er-1 pb-1 cc1"),
            R("« Seulement si mon père est d'accord. »", 9, "rd2 pb2 er1"),
            R("« Non. Je ne suis pas là comme étudiant·e. »", 9, "er1 pb1"),
        ]),
        I(9, "narr", "",
          "Dans l'ascenseur, vous croisez l'ambulancier du 25 au matin, en fin de garde. Il "
          "vous reconnaît. « Votre père ? — Vivant. Intubé trois jours. » Il hoche la tête. "
          "« Les douleurs avaient commencé quand ? » Vous lui dites la vérité. Il ne commente "
          "pas. Juste : « La prochaine fois, appelez. Même pour rien. On préfère venir pour "
          "rien. »"),
    ],
)

# ---------------------------------------------------------------------------
# 3.3 Un cœur dans les mains
# ---------------------------------------------------------------------------
_INTRO_33 = (
    "Mi-janvier. Retour en salle de dissection. Votre père est sorti de l'hôpital avec un "
    "stent et une boîte de médicaments ; il a recommencé à râler, c'est bon signe. Ce matin, "
    "la table 14 arrive au cœur. La Pre Vautier a prévenu : « C'est la séance où les gens "
    "pleurent. Pas à cause du cœur. À cause de ce qu'ils ont vécu pendant les fêtes. »"
)
_INTRO_33_RASSURE = (
    "Mi-janvier. Retour en salle de dissection. Votre père est sorti des soins intensifs il "
    "y a cinq jours ; il ne remontera pas un escalier avant longtemps. Ce matin, la table 14 "
    "arrive au cœur. La Pre Vautier a prévenu : « C'est la séance où les gens pleurent. Pas "
    "à cause du cœur. À cause de ce qu'ils ont vécu pendant les fêtes. »"
)

S3_3 = S(4, "3.3 Un cœur dans les mains", _INTRO_33,
    focus=("er", "rd", "ic", "co"),
    entries=[
        Entry(1, when(none=["papa_144"]), _INTRO_33_RASSURE),
    ],
    nodes=[
        I(1, "narr", "",
          "Yasmine ouvre le péricarde. Le cœur de Madame 14 apparaît, plus petit que vous ne "
          "l'imaginiez, enrobé de graisse jaune. Sur sa face avant, trois fins tubes "
          "blanchâtres, cousus à l'aorte : des pontages. Léo les montre du bout de la sonde. "
          "« Elle a été opérée du cœur. Il y a longtemps. » La Pre Vautier pose le cœur dans "
          "vos mains gantées. Il pèse à peine plus qu'une pomme.", [
            R("Le tenir à deux mains, immobile, en respirant lentement.", 2, "rd2 er2"),
            R("Le reposer très vite sur le plateau.", 3, "er-1 rd-1"),
            R("« Trois pontages. Mon père, lui, n'a eu qu'un stent. » Le dire à voix haute, "
              "sans l'avoir prévu, et sentir votre voix se casser au milieu de la phrase.",
              4, "er1 ic1 cc1"),
            R("Plaisanter : « Il est plus petit que celui de mon père ! »", 3, "rd-2 er-1"),
            R("Le faire tourner pour suivre les artères coronaires, comme dans l'atlas.",
              2, "cc1 rd1"),
        ]),
        I(2, "vautier", "neutral",
          "La Pre Vautier vous observe. Vos mains tremblent légèrement ; le cœur aussi. "
          "« Alex. Posez-le. » Elle attend que vous l'ayez reposé. « Ça va ? »", [
            R("« Pas vraiment. Mon père a fait un infarctus à Noël. »", 4, "er3 cc1 ic1"),
            R("« Oui, oui. C'est le froid. »", 5, "er-1 cc-1"),
            R("« Je préfère ne pas en parler ici, devant tout le monde, si ça ne vous dérange "
              "pas : je vous expliquerai après la séance. »", 5, "er1 pb1"),
            R("« Ça va. On continue ? »", 5, "er-1"),
            R("« Il faut qu'on avance, on est en retard sur le programme. »", 5, "er-2 rd-1"),
        ]),
        I(3, "maelle", "anxious",
          "Maëlle vous regarde bizarrement. « Ça va, toi ? T'es tout blanc. » De l'autre côté "
          "de la table, Noah a reposé ses pinces.", [
            R("« Non. Mon père a fait un infarctus à Noël. Je ne peux pas tenir ce cœur "
              "aujourd'hui. »", 4, "er3 cc1 ic1"),
            R("« Si, si. » Et reprendre le cœur, la mâchoire serrée.", 5, "er-2"),
            R("Sortir de la salle sans rien dire.", 6, "er-1 ic-1"),
            R("« Occupe-toi de tes affaires. »", 5, "ic-2 er-1"),
            R("Demander à Léo de prendre le relais, sans explication.", 5, "ic2 er1"),
        ]),
        I(4, "vautier", "neutral",
          "La Pre Vautier hoche la tête. Elle ne dit pas « je suis désolée ». Elle dit : "
          "« Asseyez-vous cinq minutes. Le cœur de Madame 14 attendra : il a l'habitude. » "
          "Puis, à la table : « Voici le cœur d'une femme qui a vécu longtemps avec trois "
          "pontages. Il a tenu. Regardez comme il a tenu. » Noah, Léo, Maëlle se taisent. "
          "Yasmine vous apporte un tabouret.", [
            R("S'asseoir, et accepter le tabouret. « Merci. »", 12, "er2 ic2"),
            R("« Ça va aller. Je continue. »", 5, "er-1 ic-1"),
            R("Remercier Yasmine du regard, et rester debout près de la table, à regarder.",
              12, "er1 rd1 ic1"),
            R("« Pardon de mettre tout le monde mal à l'aise. »", 12, "er1 rd1"),
            R("« Et si son cœur à elle avait été soigné plus tôt, avec un stent plutôt qu'avec "
              "des pontages, est-ce qu'elle aurait vécu plus longtemps ? »", 12, "er-1 cc1"),
        ]),
        I(5, "narr", "",
          "Vous reprenez la dissection. Pendant une heure, vos mains font ce qu'on leur "
          "demande ; votre tête est ailleurs, dans un couloir d'hôpital, une nuit de Noël. "
          "Vous sectionnez une artère coronaire sans le vouloir. Yasmine pose la main sur "
          "votre poignet. « Stop. »", [
            R("« Pardon. Je ne suis pas là, aujourd'hui. Mon père a fait un infarctus à "
              "Noël. »", 4, "er2 cc2 ic1"),
            R("« C'est rien, elle est morte. »", 6, "rd-3 er-2"),
            R("Poser les instruments, et demander à sortir cinq minutes.", 6, "er2 ic1"),
            R("Continuer, en ignorant Yasmine.", 6, "er-2 ic-2"),
        ]),
        I(12, "noah", "vulnerable",
          "Pendant que vous êtes assis·e, Noah s'approche, les gants encore aux mains. Il "
          "parle très bas. « Mon père a eu un pontage, l'an dernier. Deux. Il n'en a parlé à "
          "personne, et moi non plus. » Il regarde le cœur sur le plateau. « Je n'aurais pas "
          "pu le tenir non plus. »", [
            R("« Merci de me le dire. Ça fait du bien de ne pas être seul·e. »",
              6, "em3 co2 er1"),
            R("« Ton père, un pontage ? Lui qui se moquait des gens qui tombent dans les "
              "pommes ? »", 6, "em-2 rd-1 pb-1"),
            R("« Tu en as parlé à quelqu'un, depuis ? »", 6, "em2 co1 ic1"),
            R("« Je vais bien, Noah. Retourne à la table, Vautier va nous voir, et on va encore "
              "passer pour la table qui ne tient pas le coup. »", 6, "em-2 co-1 er-1"),
            R("Lui faire une place sur le tabouret.", 6, "em2 co2"),
        ]),
        I(6, "vautier", "neutral",
          "Dans le couloir, la Pre Vautier vous rejoint, deux gobelets de thé à la main. Elle "
          "vous en tend un. « La salle de dissection rend les choses vraies. Ce qu'on a tenu à "
          "distance pendant les fêtes revient ici, sur la table. Chaque année. » Elle souffle "
          "sur son thé. « Vous voulez me dire ce qui se passe ? Vous n'êtes pas obligé·e. »", [
            R("« Mon père. Noël. »",
              7, "er3 cc1"),
            R("« Rien. Juste de la fatigue. »", 7, "er-1 cc-1"),
            R("« Je ne sais pas si je suis fait·e pour ça. »", 7, "er1 cc1"),
            R("« Pourquoi vous faites ce métier, vous ? Ça ne vous a jamais rien fait, de "
              "tenir le cœur de quelqu'un, en sachant qu'il a battu pendant quatre-vingts "
              "ans ? »", 8, "em1 cc1 er-1"),
            R("« Ce n'est pas votre problème. »", 7, "rd-2 ic-2"),
        ]),
        I(7, "vautier", "neutral",
          "La Pre Vautier vous écoute, puis : « Vous avez le droit de ne pas tenir ce cœur "
          "aujourd'hui. Vous n'avez pas le droit de faire semblant que ça ne vous touche pas : "
          "dans dix ans, ça ressortira ailleurs, en pire. » Elle tourne son gobelet. « Il "
          "existe une consultation psychologique pour les étudiants. Ce n'est pas réservé à "
          "ceux qui vont mal. C'est aussi pour ceux qui ont un père, et un cœur dans les mains, "
          "le même mois. »", [
            R("« D'accord. J'irai. Merci. »", 10, "er2 ic2"),
            R("« Je n'en ai pas besoin. Ça va passer tout seul, comme d'habitude : il me faut "
              "juste une bonne nuit et un week-end sans hôpital. »", 10, "er-1 ic-1"),
            R("« Vous y êtes allée, vous ? »", 8, "em1 cc1"),
            R("« Je vais retourner à la table. Je crois que je peux, maintenant. »",
              10, "er2 rd1"),
            R("Sourire, sans répondre.", 10, "er1"),
        ]),
        I(8, "vautier", "melancholic",
          "« Pourquoi je fais ça ? » Elle regarde la porte de la salle. « Ma mère est morte "
          "quand j'avais vingt ans. Je n'ai jamais pu la remercier de rien. Les donneurs, je "
          "peux les remercier, eux. Chaque année. » Elle finit son thé d'un trait. « Voilà. Ne "
          "le répétez pas, ça ruinerait ma réputation. »", [
            R("« Je ne le répéterai pas. Merci de me l'avoir dit. »", 10, "rd2 pb2 em1"),
            R("Hocher la tête, ému·e.", 10, "em1 rd1"),
            R("« C'est triste. »", 10, "em-1"),
            R("« Je pourrai le raconter à la table 14 ? Je crois que ça aiderait Noah et "
              "Maëlle à comprendre pourquoi vous êtes aussi stricte sur la dignité. »",
              10, "pb-2 rd-1"),
        ]),
        I(10, "vautier", "neutral",
          "De retour à la table, la Pre Vautier interroge chaque étudiant·e, le doigt sur une "
          "artère. Elle s'arrête devant vous, sur le premier pontage. « Il part d'où, et il "
          "va où ? » La table se tait. Vous connaissez la réponse ; ce matin, elle se dérobe.", [
            R("« Je la connais, mais elle ne sort pas, aujourd'hui. Je peux la chercher dans "
              "l'atlas ? »", 11, "er3 cc2 rd1"),
            R("Inventer une réponse avec assurance.", 11, "cc-2 er-1"),
            R("« Léo, tu veux répondre ? »", 11, "ic1 er-1"),
            R("« De l'aorte à l'interventriculaire antérieure, je crois. »", 11, "cc-1 er-1"),
            R("Se taire et baisser les yeux.", 11, "er-1"),
        ]),
        I(11, "maelle", "neutral",
          "En fin de séance, Maëlle sort son téléphone, puis se reprend, et le range. « Je "
          "voulais juste prendre les pontages en photo, pour réviser. Sans le reste. Sans "
          "rien qui la montre. » Elle vous regarde. « C'est bon, ça, non ? »", [
            R("« Non. Dessine-les, comme Léo. Ça s'apprend mieux, en plus. »",
              9, "pb3 rd2 ic1"),
            R("« Oui, si on ne voit rien d'autre. »", 9, "pb-2 rd-2"),
            R("« Demande à Vautier. »", 9, "pb1 ic1"),
            R("« Fais ce que tu veux, Maëlle : après septembre, je ne vais plus te faire la "
              "police, tu es assez grande pour savoir ce qui est permis ou non. »",
              9, "pb-1 ic-2 em-1"),
            R("« Merci de t'être reprise. Ce n'était pas rien, en septembre. »",
              9, "em2 ic2 rd1"),
        ]),
        I(9, "narr", "",
          "Vous retournez au vestiaire. Le cœur de Madame 14 est sur le plateau, sous une "
          "compresse humide. Dans votre cahier, Léo a dessiné au crayon les trois pontages et "
          "leur trajet. En dessous, il a écrit : « Sie hat gehalten. — Elle a tenu. »"),
    ],
)

# ---------------------------------------------------------------------------
# 3.4 Le stéthoscope
# ---------------------------------------------------------------------------
_INTRO_34 = (
    "Fin janvier. Thierry a appelé le cabinet ce matin : Jeannine a pris trois kilos en cinq "
    "jours, elle dort assise, elle ne finit plus ses phrases. La Dre Golay part en visite et "
    "vous emmène. Dans la cuisine des Combettes, il fait trop chaud. Jeannine est dans son "
    "fauteuil, les pieds sur un tabouret, les chevilles énormes. Elle lève une main pour "
    "vous saluer, sans parler : elle n'a pas assez de souffle."
)
_INTRO_34_NOEL = (
    "Fin janvier. Le 26 décembre, vous n'êtes pas venu·e aux Combettes : votre père était à "
    "l'hôpital. Ce matin, Thierry a appelé le cabinet : Jeannine a pris trois kilos en cinq "
    "jours, elle dort assise. La Dre Golay part en visite et vous emmène. Dans la cuisine "
    "des Combettes, il fait trop chaud ; Jeannine est dans son fauteuil, les chevilles "
    "énormes."
)
_INTRO_34_SAIT = (
    "Fin janvier. Thierry a appelé le cabinet ce matin : Jeannine a pris trois kilos en cinq "
    "jours, elle dort assise. La Dre Golay part en visite et vous emmène. Dans la cuisine des "
    "Combettes, il fait trop chaud. Jeannine est dans son fauteuil, les chevilles énormes. "
    "Daniel est là, adossé à l'évier, les bras croisés."
)

S3_4 = S(5, "3.4 Le stéthoscope", _INTRO_34,
    focus=("cc", "rd", "ic", "co"),
    entries=[
        Entry(20, when(all=["noel_annonce"]), _INTRO_34_NOEL),
        Entry(30, when(any=["revele_a_daniel", "erreur_homonyme"]), _INTRO_34_SAIT),
    ],
    nodes=[
        I(1, "jeannine", "anxious",
          "La Dre Golay s'agenouille devant Jeannine, le stéthoscope aux oreilles. « Alex, "
          "venez. Écoutez la base des poumons. Là. » Elle vous tend le stéthoscope. Jeannine "
          "essaie de sourire. « Alors… mon cœur… c'est comme… dans vos livres ? »", [
            R("Lui demander si elle est d'accord, réchauffer le pavillon dans votre main, puis "
              "écouter en silence.", 2, "rd3 cc1 em1 co1"),
            R("Écouter, puis s'exclamer : « Des crépitants aux deux bases, comme au "
              "cours ! »", 3, "rd-2 pb-1 cc-1"),
            R("« Oui, comme dans les livres. »",
              3, "pb-2 cc1 em-1"),
            R("Écouter, et lui dire : « Merci de m'avoir laissé écouter. »", 2,
              "rd2 ic1 cc1"),
            R("Refuser d'ausculter : « Je ne veux pas la fatiguer. »", 2, "em1 er-1 ic-1"),
        ]),
        I(2, "golay", "neutral",
          "La Dre Golay range son stéthoscope. « Jeannine, votre cœur est noyé. Il faudrait "
          "l'hôpital, quelques jours, pour vider l'eau avec des perfusions. » Jeannine secoue "
          "la tête avant la fin de la phrase. « Non. » Un temps pour reprendre son souffle. "
          "« Pas… l'hôpital. Vous me videz… ici. »", [
            R("Regarder la Dre Golay et attendre : c'est sa décision, et celle de "
              "Jeannine.",
              4, "pb2 rd2"),
            R("« Madame Pittet, l'hôpital, c'est plus sûr. Vous devriez y aller. »",
              5, "rd-2 pb-2"),
            R("Demander à la Dre Golay : « On peut traiter à domicile ? »", 4, "ic2 cc1"),
            R("« Vous avez peur de l'hôpital ? »", 6, "em3 cc1 co1"),
            R("« Si vous refusez, vous allez étouffer, Madame Pittet : l'eau va continuer à "
              "monter dans vos poumons, et une nuit, vous ne pourrez plus respirer du "
              "tout. »", 5, "rd-3 em-2 pb-1 co-1"),
        ]),
        I(3, "golay", "cold-anger",
          "La Dre Golay reprend le stéthoscope sans un mot. Plus tard, dans la voiture, elle "
          "dira : « Ce qu'on entend dans un thorax appartient à la personne qui respire "
          "dedans. On commente en dehors de la chambre. » Pour l'instant, elle se contente de "
          "vous regarder. Jeannine a fermé les yeux.", [
            R("« Désolé·e, Madame Pittet. Je me suis laissé emporter. Ce n'est pas un cas, "
              "c'est vous. »", 2, "rd3 er1 co1"),
            R("« Pardon. » Et se taire.", 2, "rd2 er1"),
            R("Ne rien dire.", 2, "er-1"),
            R("« C'était pour apprendre. »", 2, "pb-2 er-1"),
        ]),
        I(4, "golay", "neutral",
          "La Dre Golay réfléchit. « D'accord. On essaie ici. Diurétique renforcé, pesée tous "
          "les matins, Thierry deux fois par jour, et le pharmacien prépare le nouveau "
          "pilulier. Si vous prenez encore un kilo, ou si vous étouffez la nuit, c'est "
          "l'hôpital. D'accord ? » Jeannine hoche la tête. La Dre se tourne vers vous. « Alex, "
          "vous appelez M. Chappuis, le pharmacien, et vous lui lisez l'ordonnance que je vais "
          "signer. Ensuite, Thierry. »", [
            R("« Je relis l'ordonnance avec vous, et je fais répéter les doses. »",
              7, "ic3 cc2 pb2"),
            R("« Je n'ai pas le droit de transmettre une ordonnance, si ? »", 8, "pb2 ic-1"),
            R("« D'accord. » Et appeler de mémoire.",
              9, "pb-3 cc-2"),
            R("« Thierry d'abord, ou le pharmacien ? »", 7, "ic2 cc1"),
            R("« Vous ne préférez pas le faire vous-même ? »", 7, "ic-1 er-1"),
        ]),
        I(5, "jeannine", "cold-anger",
          "Jeannine ouvre les yeux. « Petit. » Elle reprend son souffle. « J'ai accouché… des "
          "femmes… dans des granges… sans électricité. Je sais… ce que c'est… "
          "d'étouffer. » Un temps. « C'est mon souffle. Pas le vôtre. »", [
            R("« Vous avez raison. Pardon. C'est à vous de décider, avec la Dre. »",
              4, "rd3 pb2 er1"),
            R("« Mais je m'inquiète pour vous. »", 4, "em1 pb-1"),
            R("« C'est de l'entêtement. »", 4, "rd-3 em-2"),
            R("Se taire, et baisser les yeux.", 4, "er1 rd1"),
        ]),
        I(6, "jeannine", "melancholic",
          "« Peur ? » Elle rit, ce qui la fait tousser. « J'ai peur… de ne pas revenir. Les "
          "vieux qui partent… en janvier… à l'hôpital… on les ramène en avril… dans une "
          "boîte. » Elle regarde la fenêtre, la cour, la grange. « Je veux mourir… ici. Pas "
          "cette semaine. Mais ici. »", [
            R("« Vous voulez mourir ici. Il faut que ce soit écrit. »",
              4, "rd3 cc2 ic1 em1"),
            R("« Vous n'allez pas mourir, Madame Pittet. »", 4, "cc-3 em-1"),
            R("Lui prendre la main, sans rien dire.", 4, "em2 co2"),
            R("« Ici, sans l'hôpital, ce sera plus dur, vous savez : moins de surveillance, "
              "moins de médicaments par perfusion, et la nuit, personne. »", 4,
              "pb-2 em-2 co-1"),
            R("« Et Daniel, il le sait, que vous voulez mourir ici ? »", 4, "cc1 ic1 em1"),
        ]),
        I(7, "chappuis", "neutral",
          "Au téléphone, M. Chappuis, le pharmacien du village, note l'ordonnance en répétant "
          "chaque ligne. Au diurétique, il s'arrête. « Quatre-vingts milligrammes, le matin et "
          "à midi ? Elle en prenait vingt jusqu'ici. C'est bien ça ? Je préfère vérifier. »", [
            R("« Je vérifie avec la Dre. »",
              15, "ic3 pb2 cc2"),
            R("« Oui, c'est ce qui est écrit. »", 15, "pb-1 cc-1"),
            R("« Vous êtes sûr ? Je crois que c'était quarante. »", 11, "pb-2 cc-2"),
            R("« Pourquoi, c'est trop ? Vous pensez qu'il y a un risque pour ses reins, avec "
              "la créatinine qu'elle a ? »", 15, "cc1 ic1 pb-1"),
            R("« Faites comme vous pensez. »", 11, "pb-3 ic-2"),
        ]),
        I(8, "golay", "neutral",
          "« Vous ne prescrivez rien : vous transmettez. Vous lisez l'ordonnance que j'ai "
          "signée, mot pour mot, et vous faites répéter. Si le pharmacien a un doute, il me "
          "rappelle, moi. » Elle signe, et vous tend la feuille.", [go(7)]),
        I(9, "golay", "cold-anger",
          "La Dre Golay vous arrête d'un geste. « Alex. Une ordonnance qu'on dicte de mémoire, "
          "c'est une erreur qu'on attend. Vous lisez ce que j'ai écrit et signé, mot pour mot, "
          "et vous faites répéter. » Elle vous tend la feuille. Votre cœur bat un peu trop "
          "vite.", [
            R("« Vous avez raison. Je relis avec vous, puis j'appelle. »", 7, "pb2 ic2 er1"),
            R("« Je m'en souvenais. »", 7, "pb-2 er-1"),
            R("Prendre la feuille sans rien dire.", 7, "er1"),
            R("« Désolé·e, je voulais aller vite, pour elle : elle étouffe, et chaque minute "
              "compte, non ? »", 7, "er1 em1 pb-1"),
        ]),
        I(11, "chappuis", "suspicious",
          "Il y a un silence au bout du fil. « Je préfère parler à la Dre Golay. » Vous lui "
          "passez le téléphone. La Dre confirme : quatre-vingts milligrammes, matin et midi. "
          "Puis elle vous regarde, longtemps, sans rien dire.", [go(15)]),
        I(15, "thierry", "neutral",
          "Thierry, au téléphone, entre deux patients. « Quatre-vingts matin et midi, d'accord. "
          "Je passe à 18 h, puis demain à 7 h. » Un temps. « Qu'est-ce que la Dre veut que je "
          "surveille, exactement ? Dis-le-moi comme elle te l'a dit. »", [
            R("« Le poids : un kilo de plus, on appelle. »", 10, "ic3 cc3"),
            R("« Je ne sais plus trop. Demande-lui. »", 10, "ic-1 cc-1"),
            R("« Qu'elle aille mieux. »", 10, "cc-2 ic-1"),
            R("« Le poids, la tension, la respiration, les chevilles, le moral, l'appétit, "
              "le sommeil, les urines… tout, en fait. Tu sais mieux que moi ce qu'il faut "
              "regarder chez elle. »", 10, "cc-1 ic1"),
            R("« Passe-moi le relais de 18 h : je peux venir, moi, le soir. »",
              10, "pb-3 ic-1"),
        ]),
        I(10, "jeannine", "resigned",
          "Quand tout est organisé, Jeannine, un peu plus calme, désigne la cour d'un "
          "mouvement du menton : le tracteur de Daniel y est garé. « Isabelle. Il faudrait… "
          "parler à Daniel. Pour les reins. Pour le cœur. Pour ce que je veux. » Elle vous "
          "regarde. « Je n'y arrive pas… toute seule. »", [
            R("« La Dre et vous pourriez lui parler ensemble, maintenant ? Moi, je sors ou je "
              "reste, comme vous préférez. »", 12, "ic2 rd2 cc1 pb1",
              sets=["daniel_sait"]),
            R("« Je vais le chercher. »", 12, "ic1 pb-1", sets=["daniel_sait"]),
            R("« C'est à vous de lui dire, Madame Pittet. »", 13, "pb1 em-2 co-1"),
            R("« Je peux le lui dire, moi, si vous voulez. »", 13, "pb-3 rd-1"),
            R("Regarder la Dre Golay, sans rien dire.", 12, "ic1 pb1", sets=["daniel_sait"]),
        ]),
        I(12, "daniel", "resigned",
          "Daniel entre en enlevant sa casquette. La Dre Golay lui parle, à côté de sa mère, "
          "simplement : les reins, le cœur, le refus de la dialyse, la volonté de mourir ici. "
          "Daniel écoute sans un mot, les yeux sur le carrelage. À la fin, il demande "
          "seulement : « C'est pour quand ? » La Dre répond : « Personne ne le sait. Des mois, "
          "peut-être. » Daniel hoche la tête. Il pose la main sur l'épaule de sa mère, la "
          "laisse un instant, et ressort vers l'étable.", [
            R("Rester en retrait, silencieux·se.", 14, "rd2 pb2"),
            R("Le suivre dans la cour : « Monsieur Pittet, ça va ? »", 14, "em1 pb-1"),
            R("« Elle a aussi d'autres volontés, vous savez, pour après. »", 14, "pb-3 rd-2"),
            R("Aller s'asseoir près de Jeannine, et lui tenir la main pendant qu'elle "
              "regarde la porte par où son fils est sorti.", 14, "em2 co2 rd1"),
            R("Commenter, à mi-voix : « Il l'a plutôt bien pris. »", 14, "rd-1 em-1"),
        ]),
        I(13, "jeannine", "resigned",
          "Jeannine ferme les yeux. « Pas aujourd'hui, alors. » Elle sourit, épuisée. « Le col "
          "n'est pas ouvert. » Dans la cour, le tracteur de Daniel démarre et s'éloigne.", [
            R("« Quand vous serez prête. La Dre et Thierry seront là. Moi aussi, si vous le "
              "voulez. »", 14, "em2 rd2 pb1 co1"),
            R("« Vous ne pourrez pas attendre éternellement. »", 14, "rd-2 em-1 co-1"),
            R("Hocher la tête.", 14, "rd1"),
            R("« Je pourrais lui écrire une lettre, de votre part. »", 14, "pb-2"),
        ]),
        I(14, "golay", "neutral",
          "Dans la voiture, la Dre Golay conduit en silence jusqu'au village. Puis : « Vous "
          "avez entendu quoi, au stéthoscope ? Dites-le-moi comme vous le diriez à un "
          "collègue. »", [
            R("« Des crépitants fins aux deux bases, plus à droite. Comme du papier qu'on "
              "froisse. »", 16, "cc3 er1 ic1"),
            R("« Des bruits. Je ne sais pas trop. »", 16, "cc-2"),
            R("« Un OAP débutant : il fallait l'hospitaliser. »",
              16, "pb-2 cc-1 rd-1"),
            R("« Ce que vous m'aviez dit d'écouter. »", 16, "cc-1 ic1"),
            R("« J'ai surtout entendu qu'elle avait peur. »", 16, "em2 cc1 co1"),
        ]),
        I(16, "golay", "neutral",
          "La Dre Golay hoche la tête. « Dans vos livres, c'est une insuffisance cardiaque "
          "décompensée. Dans cette cuisine, c'est une femme qui veut mourir chez elle, et un "
          "fils qui a déjà trouvé son père dans un talus. » Elle se gare devant le cabinet. "
          "« Les deux sont vrais. Notre métier, c'est de n'en oublier aucun. »"),
        I(20, "jeannine", "sad",
          "Entre deux respirations, Jeannine vous dévisage. « Le 26… vous n'êtes pas… "
          "venu·e. »", [
            R("« Mon père a fait un infarctus le 24. J'aurais dû vous faire prévenir. "
              "Pardon. »", 21, "rd2 cc2 pb1 em1"),
            R("« J'ai eu un empêchement. »", 21, "cc-1 rd-1"),
            R("« Thierry ne vous a pas dit ? Mon père était à l'hôpital, je ne pouvais pas "
              "être partout à la fois, et personne ne m'a demandé si j'allais bien, moi. »",
              21, "cc1 ic-1 er-1"),
            R("« De toute façon, ce n'était pas mon rôle d'être là. »", 21, "rd-2 em-2"),
            R("« Je suis désolé·e. Comment ça s'est passé, avec Daniel ? »", 21,
              "em2 rd1 co1"),
        ]),
        I(21, "jeannine", "sad",
          "Elle hoche la tête, lentement. « Votre père… il va bien ? » Elle n'attend pas la "
          "réponse, ou elle la devine. « J'ai attendu… jusqu'à trois heures. Puis je lui ai "
          "dit. Seule. Tout. » Elle ferme les yeux. « Il est sorti. Depuis… il ne me parle "
          "plus… que des bêtes. »", [go(1)]),
        I(30, "daniel", "suspicious",
          "Daniel ne vous salue pas. Il regarde la Dre Golay s'agenouiller devant sa mère, "
          "puis vous, puis de nouveau sa mère. Quand le stéthoscope apparaît, il sort dans la "
          "cour sans un mot, laissant la porte entrouverte.", [
            R("« Bonjour, Monsieur Pittet. » Puis rester en retrait, près du fourneau.",
              1, "rd2 pb1"),
            R("Faire comme s'il n'était pas là.", 1, "rd-1 ic-1"),
            R("Le suivre : « Je peux vous parler, après ? »", 1, "pb-1 em1"),
            R("« Je peux attendre dehors, si ma présence vous gêne. »", 1, "rd2 em1 pb1"),
            R("« Il est toujours aussi aimable ? », à mi-voix, à la Dre Golay, pendant "
              "qu'elle sort son stéthoscope.", 1, "rd-2 pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.5 L'ambulancière — histoire annexe (si Alex a soutenu Yasmine au BLS, ch. 2)
# ---------------------------------------------------------------------------
S3_5 = S(6, "3.5 L'ambulancière",
    "Fin janvier, 23 h. Un message de Yasmine : « t'es debout ? je suis devant chez toi ». "
    "Elle est assise sur le muret, en doudoune, deux cafés à l'emporter à la main.",
    focus=("em", "er", "co", "ic"),
    slot="3.5",
    cond=when(all=["yasmine_soutenue"]),
    annex=True,
    nodes=[
        I(1, "yasmine", "melancholic",
          "Elle vous tend un café. « J'ai appris, pour ton père. Léo me l'a dit. » Un temps. "
          "« Au BLS, tu es venu·e t'asseoir à côté de moi sans rien demander. Je te dois une "
          "histoire, je crois. Si tu veux l'entendre. »", [
            R("« Je veux bien l'entendre. Mais tu ne me dois rien. »", 2, "em2 rd2 pb1 co1"),
            R("« Raconte ! »", 2, "em1 pb-1"),
            R("« Ce n'est pas nécessaire, Yasmine. »", 6, "em-1 rd1 co-1"),
            R("« Tu n'aurais pas dû venir à cette heure-ci. »", 6, "em-2 rd-1"),
            R("S'asseoir à côté d'elle sur le muret, et attendre.", 2, "em2 co2"),
        ]),
        I(2, "yasmine", "sad",
          "« 2019. Une nuit de novembre. Un appel pour un nourrisson qui ne respire plus, dans "
          "un appartement à Renens. Trois mois. » Elle tourne son gobelet entre ses mains. "
          "« J'ai fait le massage pendant vingt-deux minutes. Avec deux doigts. Le père tenait "
          "la lampe de son téléphone, parce que l'ampoule avait sauté. » Elle se tait. « On "
          "n'a rien pu faire. Mort subite. »", [
            R("Un silence. « Vingt-deux minutes. »",
              3, "em3 co2 er1"),
            R("« Ce n'était pas ta faute. »", 3, "em1 cc-1"),
            R("« Et c'est pour ça que tu as arrêté l'ambulance ? »", 3, "em1 cc1"),
            R("« La mort subite du nourrisson, on ne sait toujours pas bien l'expliquer, "
              "d'ailleurs : il y a des hypothèses sur le sommeil, la position, la température "
              "de la chambre, mais rien de sûr. »", 4, "em-2 pb-1 co-1"),
            R("Lui prendre le bras.", 3, "em2 co2"),
        ]),
        I(3, "yasmine", "vulnerable",
          "« Le père m'a remerciée. Tu te rends compte ? Il m'a remerciée, à la fin. » Elle "
          "rit, et ça ressemble à autre chose. « Après, j'ai fait encore deux ans. Je dormais "
          "dans ma voiture avant les gardes. Mon copain est parti. Et un matin, je me suis "
          "inscrite en médecine. Je me suis dit : si je sais plus de choses, peut-être que la "
          "prochaine fois… »", [
            R("« … tu ne seras pas seule avec deux doigts et une lampe de téléphone. »",
              8, "em3 co2"),
            R("« Tu en as parlé à quelqu'un, à l'époque ? Un débriefing, un psy ? »",
              8, "ic2 em1 pb1"),
            R("« Avec plus de connaissances, tu ne l'aurais pas sauvé. »",
              8, "em-2 cc1 co-1"),
            R("« Moi, à ta place, j'aurais arrêté tout de suite. »", 8, "em-1"),
            R("« Et ton copain, il est parti à cause de ça ? »", 8, "pb-2 rd-1"),
        ]),
        I(4, "yasmine", "cold-anger",
          "Yasmine vous regarde. « Je ne t'ai pas demandé un cours, Alex. » Elle se lève à "
          "moitié.", [
            R("« Pardon. Je ne savais pas quoi dire, alors j'ai dit un truc de cours. "
              "Reste. »", 3, "em1 rd2 er1 co2"),
            R("« Ok, ok. »", 6, "em-1"),
            R("« Tu es susceptible. »", 6, "rd-2 em-2"),
            R("Lui tendre son café, sans rien dire.", 3, "em1 co1"),
        ]),
        I(8, "yasmine", "neutral",
          "Yasmine boit une gorgée, puis vous regarde de côté. « Et toi ? Ton père ? Léo m'a "
          "dit que tu avais passé Noël à l'hôpital. »", [
            R("Lui raconter, simplement.", 5, "er3 em1 ic1"),
            R("« Ça va. On ne parle pas de moi ce soir. »", 5, "er-1 em1"),
            R("« Rien de comparable avec ce que tu as vécu. »", 5, "er1 em1"),
            R("« Mal. Très mal. Tu ne peux pas savoir ce que c'est, de voir son propre père "
              "gris sur un canapé, et de ne pas savoir si on a fait ce qu'il fallait. »",
              5, "er-1 em-1"),
            R("Hausser les épaules.", 5, "er-1 ic-1"),
        ]),
        I(5, "yasmine", "neutral",
          "Yasmine finit son café. « Au BLS, quand le petit mannequin est sorti de sa boîte, "
          "j'avais vingt-deux minutes dans les doigts. » Elle se lève. « Je voulais que "
          "quelqu'un le sache. Au cas où ça m'arrive encore. Que tu saches quoi faire : me "
          "laisser une minute, et puis me secouer. »", [
            R("« D'accord. Une minute, puis je te secoue. »", 9, "ic3 em2 er1", sets=["yasmine_alliee"]),
            R("« Tu devrais en parler à un professionnel, plutôt qu'à moi. »",
              9, "ic1 pb1 em-1"),
            R("« Ça ne t'arrivera plus, tu verras. »", 9, "cc-2 em-1"),
            R("« Merci de me faire confiance. » Et la serrer dans vos bras, longtemps, "
              "pendant qu'une voiture passe et que le muret devient froid.", 9, "em2 co2",
              sets=["yasmine_alliee"]),
        ]),
        I(9, "yasmine", "melancholic",
          "« Tu sais ce qui m'a le plus manqué, après Renens ? Que quelqu'un dise : on en "
          "parle, toute l'équipe, demain. Personne ne l'a fait. » Elle regarde son gobelet "
          "vide.", [
            R("« Les débriefings, ça existe. On cherche ? »",
              7, "ic3 co2 cc1"),
            R("« Ça aurait changé quoi ? »", 7, "em-2 co-1"),
            R("« Moi, je te le dis, ce soir : on en parle, toi et moi, quand tu veux, aussi "
              "souvent que tu en as besoin. Je serai là. »", 7, "em2 co2"),
            R("« Les gens ne savent pas quoi dire. »", 7, "em1"),
            R("« C'est du passé, maintenant. Tu es en médecine. »", 7, "em-2 co-2"),
        ]),
        I(6, "narr", "",
          "Yasmine hausse les épaules. « Comme tu veux. » Elle pose un des deux cafés sur le "
          "muret et repart dans la nuit. Le café est encore chaud. Vous le buvez seul·e, sans "
          "savoir ce qu'elle était venue vous dire."),
        I(7, "narr", "",
          "Elle repart à pied, les mains dans les poches. Au coin de la rue, elle se retourne "
          "et lève son gobelet vide, comme on trinque. Vous restez sur le muret jusqu'à ce "
          "que votre café soit froid."),
    ],
)

# ---------------------------------------------------------------------------
# 3.6 Le patient standardisé
# ---------------------------------------------------------------------------
S3_6 = S(7, "3.6 Le patient standardisé",
    "Début février. Centre de simulation, couloir des box de consultation. Chaque box a une "
    "vitre sans tain ; derrière, la table 14 observe, avec la Dre Chevalley. Aujourd'hui : "
    "anamnèse avec un patient standardisé. Sur la fiche : « M. Rossier, 63 ans, maux de "
    "tête ». En réalité, Bernard Gilliéron, 66 ans, ancien comédien, dix ans de patients "
    "simulés.",
    focus=("cc", "em", "rd", "ic"),
    nodes=[
        I(1, "chevalley", "neutral",
          "Avant d'entrer, la Dre Chevalley vous donne la consigne. « Quinze minutes. "
          "Anamnèse d'un mal de tête, pas d'examen. Bernard joue le patient, il ne sort jamais "
          "de son rôle. » Elle tapote la porte. « Une seule exception : si l'un de vous, ou "
          "lui, dit « Pause réelle », tout s'arrête. Ça veut dire : ce qui se passe n'est plus "
          "un exercice. Vous ne le direz sans doute jamais. Mais retenez-le. »", [
            R("« Et dans ce cas, qui appelle ? »", 2, "cc2 ic2 pb1"),
            R("Noter « Pause réelle » en haut de votre feuille.", 2, "cc1"),
            R("« Ça arrive vraiment ? »", 3, "cc1 er1"),
            R("« On n'est pas à l'armée. »", 2, "ic-2 rd-1"),
            R("Hocher la tête distraitement, en relisant vos questions sur la tablette, pour ne "
              "rien oublier de la grille d'anamnèse.", 2, "cc-1 er-1"),
        ]),
        I(2, "bernard", "neutral",
          "Box 4. Un homme d'une soixantaine d'années, veste en velours, lunettes au bout du "
          "nez, se masse les tempes. Il lève les yeux. Il est M. Rossier, maintenant, "
          "entièrement. « Bonjour… C'est vous, le docteur ? J'ai un mal de tête qui ne me "
          "lâche pas depuis trois semaines. »", [
            R("« Bonjour. Alex, étudiant·e. Racontez-moi. »", 4, "rd2 cc2 pb2"),
            R("Ouvrir la grille d'anamnèse sur la tablette : « Localisation ? Intensité, de 1 à "
              "10 ? Depuis quand ? Pulsatile ou en étau ? »", 5, "cc-1 rd-1 em-1"),
            R("« Trois semaines ? Vous auriez dû venir plus tôt. »", 6, "rd-2 em-1"),
            R("« Oui, c'est moi, le docteur. »", 6, "pb-3 cc-1"),
            R("S'asseoir à sa hauteur, poser la tablette, et attendre qu'il continue.",
              4, "em1 co1 rd2 cc1"),
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
            R("« Je suis désolé·e. Vous voulez m'en dire plus ? »", 7, "em3 rd1 cc1 co1"),
            R("« Le matin, derrière les yeux… Vous avez déjà fait contrôler votre tension ? »",
              7, "cc2"),
            R("« Votre fille a sûrement raison. »", 7, "cc-2 em-1 pb-1"),
            R("Taper « deuil » dans la grille, et passer à la question suivante.",
              5, "em-2 rd-1 co-1"),
            R("« Ça cogne derrière les yeux, le matin. Et vous, qu'est-ce que vous craignez que "
              "ce soit ? »", 7, "cc3 em2"),
        ]),
        I(5, "bernard", "annoyed",
          "M. Rossier regarde la tablette, puis vous. « Sept. Partout. Je ne sais pas. » Il "
          "répond de plus en plus court. Au bout de dix minutes, vous avez rempli toutes les "
          "cases, et il ne vous a rien dit.", [
            R("« Qu'est-ce qui vous inquiète, vous ? »",
              7, "rd2 em2 er1 cc1"),
            R("Continuer la grille jusqu'au bout : il reste les antécédents familiaux, les "
              "médicaments, les allergies et les habitudes de vie.", 8, "em-1 cc-1"),
            R("« Vous pourriez être un peu plus précis ? »", 8, "rd-1 em-1"),
            R("Regarder l'heure.", 8, "rd-1 er-1"),
        ]),
        I(6, "bernard", "cold-anger",
          "M. Rossier se redresse sur sa chaise. « Ah. » Pendant cinq minutes, il ne dit plus "
          "rien d'utile : il est devenu exactement le patient qu'on perd. Derrière la vitre, "
          "on entend presque la Dre Chevalley soupirer.", [
            R("« Excusez-moi. Je suis étudiant·e, pas médecin. Je suis là pour vous écouter. "
              "Je reprends ? »", 4, "pb2 rd2 er1"),
            R("Enchaîner les questions de la grille.", 8, "cc-1 em-1"),
            R("« Vous ne m'aidez pas beaucoup, Monsieur. »", 8, "rd-2 em-2"),
            R("Se taire, et attendre.", 4, "er1 em1"),
        ]),
        I(7, "bernard", "anxious",
          "« Ce que je crains ? » Il ôte ses lunettes. « Mon frère a fait une attaque à "
          "soixante-cinq ans. Il était devant la télé. Il a perdu la parole d'un coup, au "
          "milieu d'une phrase. » Il remet ses lunettes. « Et moi, le matin, j'ai l'impression "
          "que ma tête va éclater. »", [
            R("« Vous avez peur de faire une attaque. »", 9, "em2 cc2 rd1"),
            R("« Ça n'a sûrement rien à voir. »", 9, "cc-2 em-1 pb-1"),
            R("« Vous prenez un traitement pour la tension ? »", 9, "cc2 em-1"),
            R("« Une attaque, ça se voit sur le visage : la bouche qui tombe, un bras qui ne "
              "répond plus, la parole qui s'emmêle. Vous n'avez rien de tout ça. »",
              9, "cc-1 pb-2"),
            R("Laisser un silence, puis : « Et vous en avez parlé à votre fille, de cette "
              "peur-là ? »", 9, "em3 cc1"),
        ]),
        I(8, "bernard", "neutral",
          "La sonnerie retentit. Bernard ôte ses lunettes, s'étire, et redevient Bernard : une "
          "voix plus grave, un accent vaudois qu'il cachait. « Bon. On débriefe ? » Il sort un "
          "petit carnet. « Vous m'avez regardé… » il compte « … trois fois. Votre tablette, "
          "quarante. Vous savez ce que ça fait, à un patient ? »", [
            R("« Que je ne vous écoutais pas. »",
              12, "er2 rd2 cc1"),
            R("« La grille est obligatoire pour l'examen : si je ne coche pas toutes les "
              "cases, je perds des points, même si le patient se sent écouté. »",
              12, "er-1 ic-1"),
            R("« Vous êtes dur. C'est une simulation. »", 12, "er-2 rd-1"),
            R("Noter « contact visuel » dans votre carnet.", 12, "er1 cc1"),
        ]),
        I(9, "bernard", "happy",
          "La sonnerie retentit. Bernard ôte ses lunettes, s'étire, et redevient Bernard : une "
          "voix plus grave, un accent vaudois qu'il cachait. « Bon. On débriefe ? » Il sort un "
          "petit carnet. « Vous avez posé votre tablette. Vous m'avez laissé finir mes "
          "phrases. Quand j'ai parlé de mon frère, vous n'avez pas sauté dessus. » Il sourit. "
          "« Une chose : vous ne m'avez jamais demandé quels médicaments je prenais. Rossier "
          "en prend trois. »", [
            R("« C'est vrai. J'étais tellement dans l'écoute que j'en ai oublié la structure. "
              "Merci. »", 12, "er2 cc2"),
            R("« C'était dans la grille, je l'aurais fait à la fin. »", 12, "er-1 cc-1"),
            R("« Merci. Vous jouez incroyablement bien. »", 12, "rd1 er1"),
            R("« Et vous, Bernard, vous prenez des médicaments ? Vous avez l'air "
              "fatigué. »", 11, "pb-1 em1 co1"),
        ]),
        I(11, "bernard", "neutral",
          "Bernard rit. « Moi ? Je suis en bois, comme les vieux chênes. » Il se masse la "
          "nuque, un instant, puis range son carnet. « Ma femme dit que je devrais faire "
          "contrôler ma tension. Ma femme dit beaucoup de choses. »", [
            R("« Votre médecin de famille, ça prend dix minutes. »",
              12, "co2 cc2 pb1"),
            R("« Je peux vous la prendre, j'ai un tensiomètre dans mon sac. »",
              12, "pb-2 cc-1 co1"),
            R("Rire avec lui, et changer de sujet.", 12, "co-1 em-1"),
            R("« Les comédiens, vous êtes tous pareils : vous jouez les malades, et vous ne "
              "vous soignez jamais. Vous devriez avoir honte, à votre âge, avec votre frère. »",
              12, "rd-2 em-2"),
            R("Hocher la tête, poliment.", 12, "em-1"),
        ]),
        I(12, "chevalley", "neutral",
          "Derrière la vitre, la Dre Chevalley fait asseoir la table 14 en cercle. « Feedback "
          "des observateurs. Une chose qui a marché, une chose à travailler. » Maëlle parle "
          "de votre voix ; Yasmine, de la tablette ; Noah ne dit rien. Puis la Dre se tourne "
          "vers vous. « Et vous, sur vous-même ? »", [
            R("« La question sur sa peur, oui. La structure, non. »", 10, "er2 cc2 ic1"),
            R("« Je suis d'accord avec tout ce qui a été dit. »", 10, "cc-1 er-1"),
            R("« Yasmine exagère, pour la tablette : je la regardais pour ne rien oublier, pas "
              "pour l'éviter, lui. »", 10, "ic-2 er-1"),
            R("« Je crois que je suis nul·le en anamnèse. »", 10, "er-2 cc-1"),
            R("« Noah, tu n'as rien dit : tu as vu quelque chose ? »", 10, "ic2 em1"),
        ]),
        I(10, "chevalley", "neutral",
          "La Dre Chevalley clôt la séance. Bernard remet sa veste de velours. En passant, il "
          "vous glisse : « La semaine prochaine, je rejoue M. Rossier, avec vous. Trois "
          "semaines plus tard dans sa vie. Il ira mieux, ou pas : ça dépendra de ce qu'on a "
          "fait de lui aujourd'hui. » Il cligne de l'œil."),
    ],
)

CH3 = C(3, "Le cœur, en vrai",
    situation=(
        "Décembre à février. À Noël, le cœur de votre père. En janvier, celui de Madame 14, "
        "que vous tenez dans vos mains, et celui de Jeannine, qui se noie. En février, au "
        "centre de simulation, un patient standardisé, ancien comédien, qui compte les fois "
        "où vous l'avez regardé."
    ),
    objectives=(
        "reconnaître une douleur thoracique qui impose d'appeler le 144, même — surtout — "
        "pour un proche ; ne pas jouer au médecin dans sa propre famille ; transmettre les "
        "informations utiles aux ambulanciers ; dire la vérité aux soignants sur le "
        "déroulement des faits ; reconnaître et réguler ses émotions, et accepter de l'aide ; "
        "examiner une patiente en respectant sa pudeur et sa parole ; respecter un refus "
        "d'hospitalisation éclairé ; transmettre une ordonnance sans erreur (lecture mot pour "
        "mot, répétition) ; soutenir une collègue sans la forcer à parler ; mener une "
        "anamnèse centrée sur la personne et recevoir un feedback."
    ),
    anchoring=(
        "UNIL BMed2.4 (circulation, respiration : cycle cardiaque, physiopathologie), "
        "BMed2.8 (examen cardio-respiratoire ; anamnèse avec patient standardisé) et BMed2.10 "
        "(TP anatomie du cœur) · UNIGE Cœur et circulation, Respiration, compétences "
        "cliniques (stations formatives) · UZH Humanbiologie I (Herz-Kreislauf, Atmung), "
        "Klinischer Untersuchungskurs I, Praktikum Physiologie I (ECG, tension, spirométrie), "
        "Praktikum klinische Anatomie I."
    ),
    focus=("er", "cc", "em", "co"),
    scenes=[S3_1, S3_2A, S3_2B, S3_3, S3_4, S3_5, S3_6],
)
