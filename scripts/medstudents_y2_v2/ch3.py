"""Chapitre 3 — Le cœur, en vrai (décembre-janvier).

Cinq scènes jouées, six ou sept écrites :
  3.1 BLS · 3.2 Le repas de Noël
  3.3 branche parallèle : « L'unité coronarienne » (Alex a appelé le 144)
      ou « Les soins intensifs » (Alex a rassuré son père)
  3.4 Un cœur dans les mains · 3.5 Le stéthoscope
  3.6 histoire annexe « L'ambulancière » (si Alex a soutenu Yasmine au BLS)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 3.1 BLS
# ---------------------------------------------------------------------------
S3_1 = S(1, "3.1 BLS",
    "Mi-décembre. Centre de simulation, salle 3. Des mannequins alignés sur des tapis "
    "bleus, un défibrillateur d'entraînement, une odeur de désinfectant et de plastique "
    "neuf. La Dre Chevalley, responsable du centre, fait asseoir la table 14 en cercle. "
    "Aujourd'hui : réanimation de base.",
    focus=("ic", "cc", "er"),
    nodes=[
        I(1, "chevalley", "neutral",
          "« Dans un arrêt cardiaque, ce qui tue, ce n'est presque jamais l'ignorance. C'est "
          "le silence, le flou et la peur. Qui fait quoi, qui appelle, qui compte. » Elle "
          "désigne le mannequin. « Groupes de quatre. Un leader. Les autres font ce qu'il "
          "dit, et le répètent à voix haute. On appelle ça la communication en boucle "
          "fermée. Qui commence ? » Yasmine soupire : elle a fait ça mille fois.", [
            R("« Je veux bien mener. Yasmine, tu nous corriges si on se trompe ? »",
              2, "ic3 cc1 er1"),
            R("« Yasmine a l'expérience : qu'elle le fasse. »", 3, "ic-1 er-1"),
            R("« Je fais les compressions. Je préfère ne pas parler. »", 2, "cc-1 ic1"),
            R("« Pourquoi c'est si important de répéter à voix haute ? »", 4, "cc2 ic1"),
            R("Rire avec Noah, qui fait mine d'embrasser le mannequin.", 3, "rd-1 ic-2 er-1"),
        ]),
        I(2, "narr", "",
          "« Scénario : un homme de soixante ans s'effondre dans un hall de gare. » La Dre "
          "Chevalley lance le chronomètre. Le mannequin est par terre. Noah se fige, Maëlle "
          "cherche le défibrillateur des yeux, Léo vérifie la sécurité des lieux comme dans le "
          "protocole. Yasmine attend, bras croisés, de voir ce que vous allez faire.", [
            R("« Monsieur, vous m'entendez ? » Secouer ses épaules, regarder s'il respire dix "
              "secondes, puis : « Noah, tu appelles le 144 et tu mets le haut-parleur. Maëlle, "
              "le défibrillateur. Je commence les compressions. »", 5, "ic3 cc3 er2 rd1"),
            R("Se jeter sur le thorax et commencer les compressions sans rien dire.",
              6, "cc-2 ic-2"),
            R("Crier « Quelqu'un appelle les secours ! » en commençant les compressions.",
              6, "cc-1 ic1"),
            R("Chercher le pouls carotidien pendant trente secondes.", 6, "cc-1 er-1"),
            R("Regarder Yasmine, pour savoir quoi faire.", 3, "er-2 ic-1"),
        ]),
        I(3, "yasmine", "annoyed",
          "Yasmine soupire et prend la place. « Bon. » En trente secondes, elle a tout fait : "
          "appel, défibrillateur, compressions, comptage à voix haute, relève toutes les deux "
          "minutes. Pas une erreur. La Dre Chevalley arrête le chronomètre. « Parfait. Et "
          "les trois autres n'ont rien appris. » Yasmine hausse les épaules.", [
            R("« On recommence, et cette fois c'est moi qui mène. Yasmine, tu observes et tu "
              "nous débriefes ? »", 2, "ic3 er2 pb1"),
            R("« Elle le fait mieux que nous : autant qu'elle le fasse. »", 7, "ic-2 er-1"),
            R("« C'est injuste, elle a six ans d'avance. »", 7, "ic-2 er-2"),
            R("« Yasmine, tu nous montres une fois au ralenti ? »", 2, "ic2 cc1"),
        ]),
        I(4, "chevalley", "neutral",
          "« Parce que dans le bruit, la peur et l'adrénaline, on entend ce qu'on a envie "
          "d'entendre. Le leader dit : « Noah, appelle le 144. » Noah répond : « J'appelle "
          "le 144. » Et quand c'est fait : « 144 en ligne. » Sinon, trois personnes croient "
          "que quelqu'un d'autre a appelé, et personne n'a appelé. » Elle vous tend le "
          "chronomètre. « Vous menez. »", [go(2)]),
        I(5, "narr", "",
          "Deux minutes de compressions. Vous comptez à voix haute. Noah répète tout, la voix "
          "tremblante mais claire : « 144 en ligne. » Maëlle colle les électrodes. Le "
          "défibrillateur d'entraînement parle : « Choc recommandé. » « Tout le monde "
          "s'écarte ! » Le choc. Vous reprenez. La Dre Chevalley arrête le chronomètre. "
          "« Propre. » Yasmine, pour la première fois, sourit.", [go(7)]),
        I(6, "chevalley", "neutral",
          "La Dre Chevalley arrête le chronomètre au bout de deux minutes. « Qui a appelé le "
          "144 ? » Silence. Personne. « Le défibrillateur ? » Maëlle l'a cherché, sans que "
          "personne le lui demande. « Vous avez fait des compressions parfaites sur un homme "
          "pour qui personne n'a jamais appelé à l'aide. »", [
            R("« J'ai foncé sans organiser l'équipe. Je recommence, en distribuant les rôles "
              "à voix haute. »", 2, "er2 ic2 cc1"),
            R("« Dans la vraie vie, il y aurait du monde autour. »", 7, "er-1 ic-1"),
            R("« Je pensais que quelqu'un l'avait fait. »", 7, "cc1 ic-1"),
            R("« C'est le stress. »", 7, "er-1"),
            R("« Noah aurait pu appeler, il ne faisait rien. »", 7, "ic-3 rd-1"),
        ]),
        I(7, "chevalley", "neutral",
          "« Dernier scénario. » La Dre Chevalley pose sur la table un petit mannequin, de la "
          "taille d'un bébé. « Nourrisson de trois mois, retrouvé inconscient dans son lit "
          "par sa mère. Yasmine, vous menez. » Yasmine s'approche. Ses mains, au-dessus du "
          "mannequin, ne bougent pas. Cinq secondes. Dix. Elle est devenue grise.", [
            R("S'approcher d'elle et, à voix basse : « Yasmine. Tu veux que je prenne ? » En "
              "posant une main sur son épaule.", 8, "em3 ic2 er1",
              sets=["yasmine_soutenue"]),
            R("« Yasmine, on t'attend ! »", 9, "em-2 ic-1 er-1"),
            R("Prendre la place sans rien dire, et lancer le scénario.", 8, "ic1 em1",
              sets=["yasmine_soutenue"]),
            R("Rire nerveusement : « Elle a vu un fantôme. »", 9, "em-3 rd-2"),
            R("Regarder la Dre Chevalley, pour qu'elle arrête l'exercice.", 8, "ic2 em1",
              sets=["yasmine_soutenue"]),
            R("« Dre Chevalley, je crois qu'il faut une pause. » En se plaçant entre Yasmine "
              "et le groupe.", 8, "em2 ic2 rd2 er1", sets=["yasmine_soutenue"]),
        ]),
        I(8, "chevalley", "neutral",
          "La Dre Chevalley dit simplement : « Pause de dix minutes. » Yasmine sort sans un "
          "mot. Par la porte vitrée, vous la voyez dans le couloir, dos au mur, les yeux "
          "fermés. La Dre Chevalley vous regarde. « Allez-y, si vous voulez. Pas pour la faire "
          "parler. Pour qu'elle ne soit pas seule. »", [
            R("Sortir, et s'asseoir à côté de Yasmine, sans rien demander.", 10, "em3 co2 rd1",
              sets=["yasmine_soutenue"]),
            R("« Elle préférera être seule. »", 11, "em-1"),
            R("Sortir, et lui demander : « Qu'est-ce qui t'est arrivé ? Raconte. »",
              10, "em1 pb-2 rd-1"),
            R("Lui apporter un verre d'eau, et revenir dans la salle.", 11, "em2 rd1"),
            R("Glisser à Maëlle : « C'était quoi, son problème ? »", 11, "rd-2 pb-1 em-1"),
        ]),
        I(9, "yasmine", "cold-anger",
          "Yasmine se redresse d'un coup. « Rigole. » Sa voix est blanche. « Le jour où tu en "
          "auras un vrai dans les mains, tu rigoleras moins. » Elle sort. La Dre Chevalley "
          "arrête l'exercice et vous regarde longtemps.", [
            R("La suivre : « Yasmine ! Pardon. C'était minable. »", 10, "rd2 em2 er1",
              sets=["yasmine_soutenue"]),
            R("« C'était pour détendre. »", 11, "er-1 rd-1"),
            R("Ne rien dire.", 11, "er-1"),
            R("« Elle est susceptible, hein. »", 11, "rd-2 em-2"),
        ]),
        I(10, "yasmine", "melancholic",
          "Yasmine ne vous regarde pas. « Ça va. » Un long silence. « C'est le mannequin. La "
          "taille. » Elle n'en dit pas plus, et vous ne demandez rien. Au bout de dix "
          "minutes, elle se lève, se passe de l'eau sur le visage et rentre dans la salle. "
          "Elle mène le scénario du nourrisson sans une erreur, la mâchoire serrée.",
          [go(11)]),
        I(11, "chevalley", "neutral",
          "Fin de séance. La Dre Chevalley rassemble le groupe. « Ce que vous avez appris "
          "aujourd'hui, ce n'est pas le rythme des compressions. C'est que, dans une équipe, "
          "chacun porte quelque chose qu'on ne voit pas. Le leader, c'est celui qui le voit à "
          "temps. » Elle range le petit mannequin dans sa boîte, avec un soin étrange.", [
            R("« Dans un vrai arrêt, je saurais distribuer les rôles. Je crois. »",
              END, "er1 ic1 cc1"),
            R("« J'ai surtout appris que je parle trop peu. »", END, "er2 cc1"),
            R("« J'ai appris que Yasmine n'est pas en métal. »", END, "em2 ic1"),
            R("« Rien de neuf, on l'avait vu en cours. »", END, "ic-2 er-1"),
            R("« Que le plus dur, c'est le silence de la première seconde. »",
              END, "er2 cc2 ic1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.2 Le repas de Noël
# ---------------------------------------------------------------------------
S3_2 = S(2, "3.2 Le repas de Noël",
    "24 décembre, 20 h 40. Chez vos parents. La fondue est finie, le caquelon raclé jusqu'à "
    "la religieuse. Votre père, Philippe, 54 ans, chef de chantier, est sorti fumer sur le "
    "balcon comme chaque soir. Il est rentré il y a dix minutes, sans un mot, et s'est assis "
    "sur le canapé.",
    focus=("pb", "cc", "er", "ic"),
    debriefs=[
        Debrief(when(all=["papa_rassure"]), tone="hard", lead=(
            "Une douleur qui serre au milieu de la poitrine, qui descend dans le bras, avec "
            "des sueurs, qui dure et ne cède pas au repos : c'est un infarctus jusqu'à preuve "
            "du contraire. On appelle le 144, on ne conduit pas, on ne rassure pas. « Faire "
            "médecine » n'autorise pas à trancher seul·e — encore moins pour un proche, quand "
            "la peur et l'amour déforment le jugement.")),
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
            R("Lâcher le torchon et y aller : « Il a mal où ? Depuis quand ? »",
              2, "cc2 em1 er1"),
            R("« C'est sûrement la fondue, maman. »", 3, "cc-2 pb-1"),
            R("« Je suis en deuxième année, maman. Je n'en sais pas plus que toi. »",
              2, "pb1 em-1"),
            R("« Il a pris ses médicaments pour la tension ? »", 2, "cc1"),
            R("« Laisse-le, il exagère toujours. »", 3, "em-2 cc-2"),
        ]),
        I(2, "philippe", "anxious",
          "Votre père est assis sur le canapé, la main posée à plat sur la poitrine, le front "
          "humide. Il essaie de sourire. « C'est rien. Ta mère panique. C'est la fondue, ça "
          "me serre, là. » Il montre le milieu du thorax. « Ça descend un peu dans le bras. "
          "Ça va passer. »", [
            R("« Papa, une douleur qui serre dans la poitrine et qui descend dans le bras, avec "
              "la sueur, il faut appeler le 144. Tout de suite. Je les appelle. »",
              4, "cc3 pb2 er2 ic2"),
            R("« Depuis quand ça a commencé ? Tu as déjà eu ça ? »", 5, "cc2 em1"),
            R("« C'est sûrement la fondue. Allonge-toi, ça va passer. »", 6, "cc-3 pb-3 em-1"),
            R("Aller chercher l'aspirine dans la pharmacie de la salle de bains.",
              7, "pb-2 cc-1"),
            R("Prendre son pouls, puis sa tension avec l'appareil de grand-maman.",
              5, "cc1 pb-1"),
            R("« Tu veux qu'on aille aux urgences en voiture ? »", 8, "cc1 pb-1"),
        ]),
        I(3, "nadia", "sad",
          "« Tu es sûr·e ? » Votre mère tord son torchon. Depuis le salon, on entend votre "
          "père tousser. « Il est tout gris, je te dis. »", [
            R("« Je vais le voir, maman. Et si c'est ce que je crains, on appelle le 144. »",
              2, "cc2 em1 pb1"),
            R("Aller voir.", 2, "em1 er1"),
            R("« Fais-lui une tisane. »", 6, "cc-2 pb-2"),
            R("« Il a toujours été comme ça : il dramatise. »", 6, "em-2 cc-2"),
        ]),
        I(4, "narr", "",
          "La régulatrice du 144 vous pose des questions précises, d'une voix calme : âge, "
          "douleur, depuis quand, est-il conscient, respire-t-il. Elle vous demande s'il est "
          "allergique à l'aspirine, et vous dit de lui en faire croquer une. Puis : "
          "« L'ambulance est en route. Ouvrez la porte, allumez la lumière de l'entrée, restez "
          "avec lui. » Votre père vous regarde. Pour la première fois de votre vie, il a peur, "
          "et il vous laisse le voir.", [
            R("S'asseoir à côté de lui et lui prendre la main. « Ils arrivent, papa. Je reste "
              "là. »", 12, "em3 co2 er2", sets=["papa_144"]),
            R("Faire les cent pas en répétant que ça va aller.", 12, "er-2 em1",
              sets=["papa_144"]),
            R("Lui expliquer en détail ce qu'est un infarctus.", 12, "pb-2 em-1 cc-1",
              sets=["papa_144"]),
            R("Ouvrir la porte, allumer l'entrée, préparer sa carte d'assurance et la liste de "
              "ses médicaments, puis revenir près de lui.", 12, "ic3 cc2 er1",
              sets=["papa_144"]),
            R("« Tu vois ? Je t'avais dit d'arrêter de fumer ! »", 12, "em-3 er-2 rd-1",
              sets=["papa_144"]),
        ]),
        I(5, "philippe", "anxious",
          "« Depuis le dessert. Une heure, peut-être. » Il grimace. « J'ai déjà eu un truc "
          "pareil en septembre, sur le chantier, en portant des sacs de ciment. Ça passait en "
          "s'asseyant. Là, ça ne passe pas. » Votre mère, derrière vous : « Tu ne m'avais rien "
          "dit ! »", [
            R("« Une douleur depuis une heure, qui ne passe pas au repos : j'appelle le 144. "
              "Maintenant. »", 4, "cc3 pb2 er1 ic1"),
            R("« Ça doit être de l'angine de poitrine. Tu as de la trinitrine ? »",
              6, "pb-3 cc-1"),
            R("« On attend encore un peu, et si ça ne passe pas, on appelle. »",
              6, "cc-2 pb-2"),
            R("« Tu aurais dû consulter en septembre ! »", 6, "em-2 er-1"),
            R("Appeler la permanence médicale de garde pour demander conseil.",
              9, "cc1 ic2 pb1"),
        ]),
        I(6, "philippe", "neutral",
          "Votre père se lève, pâle, et se dirige vers la chambre. « Tu vois ? Même le docteur "
          "dit que c'est la fondue. » Il rit, un peu de travers. « Je vais m'allonger. Joyeux "
          "Noël. » Votre mère vous regarde. Elle a l'air soulagée, parce que vous avez l'air "
          "sûr·e de vous.", [
            R("Le rattraper dans le couloir : « Papa, attends. Je me suis trompé·e. On appelle "
              "le 144. Maintenant. »", 4, "cc2 pb2 er2"),
            R("« Réveille-moi si ça ne va pas. »", 10, "cc-1 pb-1", sets=["papa_rassure"]),
            R("Le laisser aller se coucher.", 10, "pb-2 cc-1", sets=["papa_rassure"]),
            R("Chercher sur internet « douleur thoracique après un repas ».", 10, "pb-2 cc-2",
              sets=["papa_rassure"]),
            R("« Maman, s'il a encore mal dans une heure, tu me réveilles. »",
              10, "cc-1 ic-1", sets=["papa_rassure"]),
        ]),
        I(7, "philippe", "anxious",
          "Votre père avale le comprimé. « Merci, docteur. » Il se cale dans le canapé. « Tu "
          "vois, ça va déjà mieux. » Ça ne va pas mieux : il est toujours gris, et il "
          "transpire.", [
            R("« L'aspirine ne suffit pas, papa. J'appelle le 144. »", 4, "cc2 pb1 er1"),
            R("« Bon. On attend que ça agisse. »", 6, "cc-2 pb-2"),
            R("« Tu es allergique à quelque chose, au fait ? »", 6, "pb-1 cc-1"),
            R("Appeler le 144, et leur dire qu'il a déjà pris une aspirine.",
              4, "cc3 ic2 pb1"),
        ]),
        I(8, "philippe", "neutral",
          "« En voiture ? » Votre père rit, puis grimace. « Il neige, et ta mère conduit comme "
          "un pied. » Il se lève pour chercher ses clés, chancelle, se rassied. « Je vais "
          "conduire, moi. »", [
            R("« Non. Personne ne conduit. Assieds-toi : j'appelle le 144, ils viennent te "
              "chercher. »", 4, "cc3 pb2 er1"),
            R("« D'accord, je conduis, moi. »", 11, "pb-2 cc-1"),
            R("« Alors on attend demain. »", 6, "cc-3 pb-2"),
            R("« Maman, conduis. Je reste derrière avec lui. »", 11, "pb-1 cc-1"),
        ]),
        I(9, "narr", "",
          "Le médecin de garde décroche à la quatrième sonnerie. Vous décrivez la douleur qui "
          "serre depuis une heure, le bras, la sueur. Il vous coupe : « Raccrochez et appelez "
          "le 144. Maintenant. Ne le faites pas conduire. »", [go(4)]),
        I(10, "narr", "",
          "Votre père va se coucher. Votre mère fait la vaisselle en chantonnant. Vous regardez "
          "un film sans le voir. À minuit, vous passez devant la porte de la chambre : il dort, "
          "la respiration un peu rapide. Vous allez vous coucher, vous aussi."),
        I(11, "narr", "",
          "Dans la voiture, sur la route enneigée, votre père se tait. Au premier rond-point, "
          "il dit : « Arrête-toi. » Il ne voit plus très bien. Vous vous garez sur le "
          "bas-côté, feux de détresse, et vous appelez le 144.", [go(13)]),
        I(12, "narr", "",
          "Les ambulanciers arrivent en onze minutes. Électrocardiogramme sur place. L'un des "
          "deux, un grand type à moustache, montre l'écran à son collègue sans "
          "rien dire, puis il vous regarde : « Vous avez bien fait d'appeler. » Votre mère "
          "monte dans l'ambulance. Vous suivez en voiture, derrière le gyrophare, sur la "
          "neige."),
        I(13, "narr", "",
          "La régulatrice du 144 vous demande où vous êtes exactement, puis s'il respire, s'il "
          "est allergique à l'aspirine. « Ne repartez pas. Moteur coupé, feux de détresse, "
          "restez avec lui. L'ambulance arrive. » Votre père a posé la tête contre la vitre. "
          "Pour la première fois de votre vie, il a peur, et il vous laisse le voir.", [
            R("Passer à l'arrière, à côté de lui, et lui prendre la main. « Ils arrivent, papa. "
              "Je reste là. »", 12, "em3 co2 er2", sets=["papa_144"]),
            R("Redémarrer : l'hôpital n'est qu'à dix minutes.", 12, "pb-3 ic-2 cc-1",
              sets=["papa_144"]),
            R("Faire les cent pas sur le bas-côté, téléphone à la main.", 12, "er-2 em-1",
              sets=["papa_144"]),
            R("Allumer le plafonnier, chercher sa liste de médicaments dans son portefeuille, "
              "et rester près de lui.", 12, "ic2 cc2 er1", sets=["papa_144"]),
            R("« Je t'avais dit qu'il ne fallait pas conduire ! »", 12, "em-3 er-2",
              sets=["papa_144"]),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.3 L'unité coronarienne — branche « Alex a appelé le 144 »
# ---------------------------------------------------------------------------
S3_3A = S(3, "3.3 L'unité coronarienne",
    "25 décembre, 1 h 20. Soins intensifs de cardiologie. On a posé un stent dans une "
    "artère du cœur de votre père il y a quarante minutes. Il a des électrodes partout, un "
    "pansement au poignet. Votre mère s'est endormie sur une chaise, son manteau sur les "
    "genoux.",
    focus=("er", "em", "rd"),
    slot="3.3",
    cond=when(all=["papa_144"]),
    nodes=[
        I(1, "philippe", "angry",
          "Votre père ouvre les yeux. Il voit l'heure, la perfusion, vous. « J'ai gâché "
          "Noël. » Puis, plus bas, furieux : « Pour une fondue. Ils m'ont mis un tuyau dans le "
          "bras pour une fondue. »", [
            R("« Tu as fait un infarctus, papa. Ce n'était pas la fondue. Et tu n'as rien "
              "gâché : tu es là. »", 2, "cc2 em2 er1"),
            R("« Tu vois ? J'avais raison ! »", 3, "em-2 er-1 rd-1"),
            R("Lui prendre la main, sans rien dire.", 2, "em2 co2"),
            R("« Le cardiologue va t'expliquer. »", 2, "pb1 em-1"),
            R("« Si tu n'avais pas fumé pendant trente ans, on n'en serait pas là. »",
              3, "em-3 rd-2 er-1"),
        ]),
        I(2, "philippe", "vulnerable",
          "Il regarde sa main dans la vôtre. Il ne la retire pas. « Le type de l'ambulance… "
          "il a montré l'écran à son collègue. J'ai vu sa tête. » Il avale sa salive. « J'ai "
          "cru que j'allais crever devant ta mère. Sur le tapis du salon. » Ses doigts "
          "tremblent.", [
            R("« Moi aussi, j'ai eu peur. Très peur. Mais tu es là, et ils disent que le stent "
              "a bien marché. »", 4, "em3 co2 er1"),
            R("« Tu ne vas pas crever, papa, arrête. »", 4, "cc-1 em-1"),
            R("« Avec une prise en charge en moins de deux heures, le pronostic est bon, "
              "statistiquement. »", 4, "em-2 pb-1 cc1"),
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
            R("« Je dis juste la vérité. »", 4, "em-2 er-1"),
        ]),
        I(4, "ammann", "neutral",
          "Une cardiologue entre, la Dre Ammann, des cernes de garde. Elle explique à votre "
          "père, avec ses mains : une artère bouchée, ouverte à temps, un petit ressort pour "
          "la tenir ouverte, des médicaments à vie, une réadaptation. « Vous avez eu de la "
          "chance qu'on vous appelle tôt. Une heure de plus, et c'était un autre muscle. » "
          "Elle se tourne vers vous. « C'est vous, l'étudiant·e en médecine ? Vous voulez voir "
          "les images de la coronarographie ? »", [
            R("« Merci. Pas cette nuit. Cette nuit, je suis juste son enfant. »",
              5, "er2 pb2 em1"),
            R("« Oh oui ! » Et suivre la cardiologue vers l'écran.", 6, "pb-2 em-1"),
            R("« Papa, ça te dérange si je vais regarder ? »", 6, "rd2 pb-1"),
            R("« Est-ce qu'il pourra retravailler sur un chantier ? »", 5, "em1 cc1 pb1"),
            R("Poser des questions techniques sur le stent, devant votre père qui ne comprend "
              "rien.", 6, "pb-2 rd-1 em-1"),
        ]),
        I(5, "philippe", "vulnerable",
          "La cardiologue repart. Votre père vous regarde longtemps. « Tu sais, je ne te l'ai "
          "jamais dit… » Il s'arrête. « Tu reviens me voir samedi ? Ta mère va me parler de "
          "cigarettes et de légumes toute la journée. Toi, tu me parleras de ta fac. »", [
            R("« Je reviens samedi. Promis. Et je te parlerai de la fac, pas de "
              "cigarettes. »", 7, "em2 co2 rd1", sets=["papa_promesse"]),
            R("« Samedi, je ne peux pas, j'ai des révisions. »", 7, "em-2 co-1"),
            R("« Tu ne m'as jamais dit quoi ? »", 8, "em3"),
            R("« Je reviendrai si j'ai le temps. »", 7, "em-1"),
            R("« Je reviens samedi. Et on parlera aussi de cigarettes. Une fois. Après, c'est "
              "fini. »", 7, "em2 cc2 er1", sets=["papa_promesse"]),
        ]),
        I(6, "nadia", "sad",
          "Devant l'écran, la Dre Ammann vous montre l'artère, avant et après : un filet de "
          "produit de contraste qui s'arrête net, puis un fleuve. C'est fascinant. Quand vous "
          "revenez, votre père fait semblant de dormir. Votre mère vous regarde. « Il t'a "
          "demandé. Deux fois. »", [
            R("S'asseoir près de lui. « Pardon, papa. Je suis là. »", 5, "em2 rd1 er1"),
            R("« Il dormait, non ? »", 7, "em-1 cc-1"),
            R("« C'était important pour mes études, maman. »", 7, "em-2 pb-1"),
            R("S'asseoir et lui prendre la main, sans un mot.", 5, "em2 co1"),
        ]),
        I(7, "narr", "",
          "4 h du matin. L'ambulancier à moustache repasse dans le couloir, en fin de service. "
          "Il vous reconnaît. « Votre père ? — Un stent. » Il hoche la tête. « La plupart des "
          "gens attendent le lendemain. Vous avez bien fait. » Il repart. Vous restez assis·e "
          "dans le couloir, et vous pleurez, enfin."),
        I(8, "philippe", "vulnerable",
          "« Que j'étais fier. » Il détourne les yeux vers les écrans. « Quand tu as dit "
          "« j'appelle le 144 », avec cette voix… je me suis dit : ça y est, c'est un "
          "docteur. » Il renifle. « Bon. Ne le répète pas à ta mère. »", [
            R("Lui serrer la main. « Je reviens samedi. »", 7, "em2 co2",
              sets=["papa_promesse"]),
            R("« Je ne suis pas encore docteur, papa. »", 7, "er1 em-1"),
            R("Rire, ému·e : « Moi aussi, je suis fier·ère de toi. Tu as accepté qu'on "
              "appelle. »", 7, "em3 co2", sets=["papa_promesse"]),
            R("« Ça ne compte pas, tu es sous morphine. »", 7, "em-2 er-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.3 Les soins intensifs — branche « Alex a rassuré son père »
# ---------------------------------------------------------------------------
S3_3B = S(4, "3.3 Les soins intensifs",
    "25 décembre, 6 h 10. Votre mère vous réveille en criant. Votre père est assis au bord "
    "du lit, en sueur, la main sur la poitrine, incapable de parler. Cette fois, vous "
    "appelez le 144 sans réfléchir. 9 h 30 : soins intensifs. Un infarctus étendu, une "
    "artère ouverte trop tard, un cœur qui pompe mal. Votre père est intubé, endormi.",
    focus=("er", "em", "pb"),
    slot="3.3",
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
            R("« Hier soir, vers 20 h, après le repas. Il avait mal dans la poitrine et dans le "
              "bras, il transpirait. J'ai pensé que c'était la digestion, et je lui ai dit "
              "d'aller se coucher. C'était une erreur. »", 2, "pb3 cc3 er1 rd1"),
            R("« Ce matin, vers 6 h. »", 3, "pb-3 cc-3 rd-1"),
            R("« Je ne sais pas exactement. »", 3, "cc-2 pb-1"),
            R("Laisser votre mère répondre.", 2, "cc-1 er-1"),
            R("« Il avait un peu mal hier soir, mais rien de typique. »", 3, "pb-2 cc-2"),
        ]),
        I(2, "nadia", "cold-anger",
          "La cardiologue note, sans commentaire. « Merci. C'est important pour nous. » Quand "
          "elle sort, votre mère ne vous regarde pas. « Tu as dit que c'était l'estomac. » "
          "Elle le dit sans crier, et c'est pire. « Je t'ai demandé parce que tu fais "
          "médecine. »", [
            R("« Oui. Je l'ai dit, et je me suis trompé·e. Je n'aurais jamais dû trancher. "
              "J'aurais dû appeler. »", 4, "pb2 er2 rd1 cc1"),
            R("« Je suis en deuxième année, maman ! Je ne suis pas cardiologue ! »",
              5, "er-2 pb1 em-1"),
            R("« Il fallait appeler toi-même, si tu étais inquiète. »", 5, "em-3 rd-2 er-1"),
            R("Se taire, et lui prendre la main.", 4, "em2 er1"),
            R("« Les gens attendent toujours trop longtemps, pour un infarctus. Ce n'est la "
              "faute de personne. »", 5, "pb-1 cc-1 er-1"),
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
              "peut faire, c'est être là. »", 6, "cc3 em2 er1"),
            R("« Non. Il va s'en sortir, j'en suis sûr·e. »", 6, "cc-3 pb-1"),
            R("« Il a de bonnes chances, statistiquement. »", 6, "cc-1 em-2"),
            R("La prendre dans vos bras.", 6, "em3 co2"),
            R("« C'est ma faute, maman. Tout est ma faute. »", 7, "er-2 em1"),
        ]),
        I(5, "nadia", "cold-anger",
          "Votre mère se lève et va à la fenêtre du couloir. « Je ne t'accuse pas. Je dis ce "
          "qui s'est passé. » Elle s'essuie les yeux avec la manche de son pull. Vous êtes "
          "seul·e dans la petite salle.", [
            R("La rejoindre à la fenêtre : « Tu as raison. Pardon. On est là pour lui, "
              "maintenant. »", 6, "er2 em2 rd1"),
            R("Rester dans la salle.", 6, "er-1 em-1"),
            R("Écrire à Noah : « mon père a fait un infarctus ».", 6, "er1"),
            R("« Je n'ai pas à porter ça. »", 6, "em-2 er-1"),
        ]),
        I(6, "philippe", "vulnerable",
          "Trois jours plus tard. On a enlevé le tube. Votre père a une voix cassée, une sonde, "
          "un moniteur qui bipe. Il vous fait signe d'approcher. « Le docteur m'a dit, pour le "
          "24. » Il cherche son souffle. « Ne commence pas à te le reprocher. C'est moi qui ai "
          "dit que c'était la fondue. Toi, tu as juste été d'accord avec ton vieux. »", [
            R("« Je n'aurais pas dû être d'accord. Mais je suis tellement content·e que tu "
              "sois là, papa. »", 8, "em2 er2 co1 pb1"),
            R("« C'est vrai, c'est toi qui as refusé. »", 8, "em-2 rd-1 pb-1"),
            R("Lui prendre la main, en pleurant.", 8, "em2 co2"),
            R("« Les médecins disent que ton cœur ne sera plus jamais le même. »",
              8, "em-3 pb-2"),
            R("« On n'en parle plus. Repose-toi. »", 8, "er1 em1"),
        ]),
        I(7, "nadia", "sad",
          "« Non. » Votre mère vous prend le visage entre les mains, comme quand vous étiez "
          "petit·e. « Ce n'est pas toi qui as bouché son artère. Ce sont trente ans de "
          "cigarettes et un homme qui n'écoute personne. » Elle vous lâche. « Mais la "
          "prochaine fois, on appelle. Tous les deux. Promis ? »", [
            R("« Promis. Et toi aussi, tu as le droit d'appeler sans me demander. »",
              6, "er2 cc2 ic1"),
            R("« Promis. »", 6, "er2 em1"),
            R("Hocher la tête, incapable de parler.", 6, "er1 em1"),
            R("« Il n'y aura pas de prochaine fois, s'il meurt. »", 6, "er-3 em-1"),
        ]),
        I(8, "philippe", "neutral",
          "« Tu reviens samedi ? » Il essaie de sourire. « Ta mère va me parler de cigarettes "
          "et de légumes. Toi, tu me parleras de ta fac. »", [
            R("« Je reviens samedi. Promis. »", 9, "em2 co2 rd1", sets=["papa_promesse"]),
            R("« Samedi, j'ai des révisions. »", 9, "em-2 co-1"),
            R("« Je reviendrai si j'ai le temps. »", 9, "em-1"),
            R("« Je reviens samedi. Et je te parlerai aussi de cigarettes. Une fois. Après, "
              "c'est fini. »", 9, "em2 cc2 er1", sets=["papa_promesse"]),
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
# 3.4 Un cœur dans les mains
# ---------------------------------------------------------------------------
_INTRO_34 = (
    "Mi-janvier. Retour en salle de dissection. Votre père est sorti de l'hôpital avec un "
    "stent et une boîte de médicaments ; il a recommencé à râler, c'est bon signe. Ce matin, "
    "la table 14 arrive au cœur. La Pre Vautier a prévenu : « C'est la séance où les gens "
    "pleurent. Pas à cause du cœur. À cause de ce qu'ils ont vécu pendant les fêtes. »"
)
_INTRO_34_RASSURE = (
    "Mi-janvier. Retour en salle de dissection. Votre père est sorti des soins intensifs il "
    "y a cinq jours ; il ne remontera pas un escalier avant longtemps. Ce matin, la table 14 "
    "arrive au cœur. La Pre Vautier a prévenu : « C'est la séance où les gens pleurent. Pas "
    "à cause du cœur. À cause de ce qu'ils ont vécu pendant les fêtes. »"
)

S3_4 = S(5, "3.4 Un cœur dans les mains", _INTRO_34,
    focus=("er", "rd", "ic"),
    entries=[
        Entry(1, when(none=["papa_144"]), _INTRO_34_RASSURE),
    ],
    nodes=[
        I(1, "narr", "",
          "Yasmine ouvre le péricarde. Le cœur de Madame 14 apparaît, plus petit que vous ne "
          "l'imaginiez, enrobé de graisse jaune. Sur sa face avant, trois fins tubes "
          "blanchâtres, cousus à l'aorte : des pontages. Léo les montre du bout de la sonde. "
          "« Elle a été opérée du cœur. Il y a longtemps. » La Pre Vautier pose le cœur dans "
          "vos mains gantées. Il pèse à peine plus qu'une pomme.", [
            R("Le tenir à deux mains, immobile, en respirant lentement.", 2, "rd2 er2"),
            R("Le reposer très vite sur le plateau.", 3, "er-1"),
            R("« Trois pontages. Mon père, lui, n'a eu qu'un stent. » Le dire à voix haute, "
              "sans l'avoir prévu.", 4, "er1 ic1"),
            R("Plaisanter : « Il est plus petit que celui de mon père ! »", 3, "rd-2 er-1"),
            R("Le faire tourner pour suivre les artères coronaires, comme dans l'atlas.",
              2, "cc1 rd1"),
        ]),
        I(2, "vautier", "neutral",
          "La Pre Vautier vous observe. Vos mains tremblent légèrement ; le cœur aussi. "
          "« Alex. Posez-le. » Elle attend que vous l'ayez reposé. « Ça va ? »", [
            R("« Pas vraiment. Mon père a fait un infarctus à Noël. Je ne m'attendais pas à ce "
              "que ça me fasse ça. »", 4, "er3 cc1 ic1"),
            R("« Oui, oui. C'est le froid. »", 5, "er-1 cc-1"),
            R("« Je préfère ne pas en parler ici. »", 5, "er1 pb1"),
            R("« Ça va. On continue ? »", 5, "er-1"),
            R("« Il faut qu'on avance, on est en retard sur le programme. »", 5, "er-2 rd-1"),
        ]),
        I(3, "maelle", "anxious",
          "Maëlle vous regarde bizarrement. « Ça va, toi ? T'es tout blanc. » De l'autre côté "
          "de la table, Noah a reposé ses pinces.", [
            R("« Non. Mon père a fait un infarctus à Noël. Je crois que je ne peux pas tenir "
              "ce cœur aujourd'hui. »", 4, "er3 cc1 ic1"),
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
            R("S'asseoir, et accepter le tabouret. « Merci. »", 7, "er2 ic2"),
            R("« Ça va aller. Je continue. »", 5, "er-1 ic-1"),
            R("Remercier Yasmine du regard, et rester debout près de la table, à regarder.",
              7, "er1 rd1 ic1"),
            R("« Pardon de mettre tout le monde mal à l'aise. »", 7, "er1 rd1"),
            R("« Et si son cœur à elle avait été soigné plus tôt ? »", 7, "er1 em1"),
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
        I(6, "vautier", "neutral",
          "Dans le couloir, la Pre Vautier vous rejoint, deux gobelets de thé à la main. Elle "
          "vous en tend un. « La salle de dissection rend les choses vraies. Ce qu'on a tenu à "
          "distance pendant les fêtes revient ici, sur la table. Chaque année. » Elle souffle "
          "sur son thé. « Vous voulez me dire ce qui se passe ? Vous n'êtes pas obligé·e. »", [
            R("« Mon père a fait un infarctus à Noël. J'étais là. Je n'arrive pas à séparer "
              "son cœur de celui-là. »", 7, "er3 cc2"),
            R("« Rien. Juste de la fatigue. »", 7, "er-1 cc-1"),
            R("« Je ne sais pas si je suis fait·e pour ça. »", 7, "er1 cc1"),
            R("« Pourquoi vous faites ce métier, vous ? »", 8, "em1 cc1"),
            R("« Ce n'est pas votre problème. »", 7, "rd-2 ic-2"),
        ]),
        I(7, "vautier", "neutral",
          "La Pre Vautier vous écoute, puis : « Vous avez le droit de ne pas tenir ce cœur "
          "aujourd'hui. Vous n'avez pas le droit de faire semblant que ça ne vous touche pas : "
          "dans dix ans, ça ressortira ailleurs, en pire. » Elle tourne son gobelet. « Il "
          "existe une consultation psychologique pour les étudiants. Ce n'est pas réservé à "
          "ceux qui vont mal. C'est aussi pour ceux qui ont un père, et un cœur dans les mains, "
          "le même mois. »", [
            R("« D'accord. J'irai. Merci. »", 9, "er2 ic2"),
            R("« Je n'en ai pas besoin. »", 9, "er-1 ic-1"),
            R("« Vous y êtes allée, vous ? »", 8, "em1 cc1"),
            R("« Je vais retourner à la table. Je crois que je peux, maintenant. »",
              9, "er2 rd1"),
            R("Sourire, sans répondre.", 9, "er1"),
        ]),
        I(8, "vautier", "melancholic",
          "« Pourquoi je fais ça ? » Elle regarde la porte de la salle. « Ma mère est morte "
          "quand j'avais vingt ans. Je n'ai jamais pu la remercier de rien. Les donneurs, je "
          "peux les remercier, eux. Chaque année. » Elle finit son thé d'un trait. « Voilà. Ne "
          "le répétez pas, ça ruinerait ma réputation. »", [
            R("« Je ne le répéterai pas. Merci de me l'avoir dit. »", 9, "rd2 pb2 em1"),
            R("Hocher la tête, ému·e.", 9, "em1 rd1"),
            R("« C'est triste. »", 9, "em-1"),
            R("« Je pourrai le raconter à la table 14 ? »", 9, "pb-2 rd-1"),
        ]),
        I(9, "narr", "",
          "Vous retournez à la table. Le cœur de Madame 14 est sur le plateau, sous une "
          "compresse humide. Dans votre cahier, Léo a dessiné au crayon les trois pontages et "
          "leur trajet. En dessous, il a écrit : « Sie hat gehalten. — Elle a tenu. »"),
    ],
)

# ---------------------------------------------------------------------------
# 3.5 Le stéthoscope
# ---------------------------------------------------------------------------
_INTRO_35 = (
    "Fin janvier. Thierry a appelé le cabinet ce matin : Jeannine a pris trois kilos en cinq "
    "jours, elle dort assise, elle ne finit plus ses phrases. La Dre Golay part en visite et "
    "vous emmène. Dans la cuisine des Combettes, il fait trop chaud. Jeannine est dans son "
    "fauteuil, les pieds sur un tabouret, les chevilles énormes. Elle lève une main pour "
    "vous saluer, sans parler : elle n'a pas assez de souffle."
)
_INTRO_35_NOEL = (
    "Fin janvier. Le 26 décembre, vous n'êtes pas venu·e aux Combettes : votre père était à "
    "l'hôpital. Ce matin, Thierry a appelé le cabinet : Jeannine a pris trois kilos en cinq "
    "jours, elle dort assise. La Dre Golay part en visite et vous emmène. Dans la cuisine "
    "des Combettes, il fait trop chaud ; Jeannine est dans son fauteuil, les chevilles "
    "énormes."
)
_INTRO_35_SAIT = (
    "Fin janvier. Thierry a appelé le cabinet ce matin : Jeannine a pris trois kilos en cinq "
    "jours, elle dort assise. La Dre Golay part en visite et vous emmène. Dans la cuisine des "
    "Combettes, il fait trop chaud. Jeannine est dans son fauteuil, les chevilles énormes. "
    "Daniel est là, adossé à l'évier, les bras croisés."
)

S3_5 = S(6, "3.5 Le stéthoscope", _INTRO_35,
    focus=("cc", "rd", "ic", "em"),
    entries=[
        Entry(20, when(all=["noel_annonce"]), _INTRO_35_NOEL),
        Entry(30, when(any=["revele_a_daniel", "erreur_homonyme"]), _INTRO_35_SAIT),
    ],
    nodes=[
        I(1, "jeannine", "anxious",
          "La Dre Golay s'agenouille devant Jeannine, le stéthoscope aux oreilles. « Alex, "
          "venez. Écoutez la base des poumons. Là. » Elle vous tend le stéthoscope. Jeannine "
          "essaie de sourire. « Alors… mon cœur… c'est comme… dans vos livres ? »", [
            R("Lui demander si elle est d'accord, réchauffer le pavillon du stéthoscope dans "
              "votre main, puis écouter en silence.", 2, "rd3 cc1 em1"),
            R("Écouter, puis s'exclamer : « Des crépitants aux deux bases, comme au "
              "cours ! »", 3, "rd-2 pb-1 cc-1"),
            R("« Oui, comme dans les livres : votre cœur ne pompe plus assez, alors l'eau "
              "remonte dans vos poumons. »", 3, "pb-2 cc1 em-1"),
            R("Écouter, rendre le stéthoscope à la Dre Golay, et dire à Jeannine : « Merci de "
              "m'avoir laissé écouter. »", 2, "rd2 ic1 cc1"),
            R("Refuser d'ausculter : « Je ne veux pas la fatiguer. »", 2, "em1 er-1 ic-1"),
        ]),
        I(2, "golay", "neutral",
          "La Dre Golay range son stéthoscope. « Jeannine, votre cœur est noyé. Il faudrait "
          "l'hôpital, quelques jours, pour vider l'eau avec des perfusions. » Jeannine secoue "
          "la tête avant la fin de la phrase. « Non. » Un temps pour reprendre son souffle. "
          "« Pas… l'hôpital. Vous me videz… ici. »", [
            R("Regarder la Dre Golay et attendre : c'est sa décision, et celle de Jeannine.",
              4, "pb2 rd2 ic1"),
            R("« Madame Pittet, l'hôpital, c'est plus sûr. Vous devriez y aller. »",
              5, "rd-2 pb-2"),
            R("Demander à la Dre Golay : « On peut traiter à domicile ? »", 4, "ic2 cc1"),
            R("« Vous avez peur de l'hôpital ? »", 6, "em3 cc1"),
            R("« Si vous refusez, vous allez étouffer. »", 5, "rd-3 em-2 pb-1"),
        ]),
        I(3, "golay", "cold-anger",
          "La Dre Golay reprend le stéthoscope sans un mot. Plus tard, dans la voiture, elle "
          "dira : « Ce qu'on entend dans un thorax appartient à la personne qui respire "
          "dedans. On commente en dehors de la chambre. » Pour l'instant, elle se contente de "
          "vous regarder. Jeannine a fermé les yeux.", [
            R("« Désolé·e, Madame Pittet. Je me suis laissé emporter. Ce n'est pas un cas, "
              "c'est vous. »", 2, "rd3 er1"),
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
            R("« D'accord. Je relis l'ordonnance avec vous avant d'appeler, et je fais répéter "
              "les doses au pharmacien. »", 7, "ic3 cc2 pb2"),
            R("« Je n'ai pas le droit de transmettre une ordonnance, si ? »", 8, "pb2 ic-1"),
            R("« D'accord. » Et appeler le pharmacien de mémoire, sans attendre "
              "l'ordonnance.", 9, "pb-3 cc-2"),
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
            R("« Vous voulez mourir ici. C'est important que la Dre Golay l'entende, et que ce "
              "soit écrit, pour que tout le monde le respecte. »", 4, "rd3 cc2 ic1 em1"),
            R("« Vous n'allez pas mourir, Madame Pittet. »", 4, "cc-3 em-1"),
            R("Lui prendre la main, sans rien dire.", 4, "em2 co2"),
            R("« Ici, sans l'hôpital, ce sera plus dur. »", 4, "pb-2 em-2"),
            R("« Et Daniel, il le sait, que vous voulez mourir ici ? »", 4, "cc1 ic1 em1"),
        ]),
        I(7, "chappuis", "neutral",
          "Au téléphone, M. Chappuis, le pharmacien du village, note l'ordonnance en répétant "
          "chaque ligne. Au diurétique, il s'arrête. « Quatre-vingts milligrammes, le matin et "
          "à midi ? Elle en prenait vingt jusqu'ici. C'est bien ça ? Je préfère vérifier. »", [
            R("« Je vérifie avec la Dre Golay, et je vous confirme tout de suite. » Et poser la "
              "question à la Dre, l'ordonnance à la main.", 10, "ic3 pb2 cc2"),
            R("« Oui, c'est ce qui est écrit. »", 10, "pb-1 cc-1"),
            R("« Vous êtes sûr ? Je crois que c'était quarante. »", 11, "pb-2 cc-2"),
            R("« Pourquoi, c'est trop ? »", 10, "cc1 ic1"),
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
            R("« Désolé·e, je voulais aller vite, pour elle. »", 7, "er1 em1 pb1"),
        ]),
        I(10, "jeannine", "resigned",
          "La Dre Golay confirme : quatre-vingts, matin et midi. Le pharmacien répète, "
          "raccroche. Thierry viendra à 18 h. Quand tout est organisé, Jeannine, un peu plus "
          "calme, désigne la cour d'un mouvement du menton : le tracteur de Daniel y est garé. "
          "« Isabelle. Il faudrait… parler à Daniel. Pour les reins. Pour le cœur. Pour ce que "
          "je veux. » Elle vous regarde. « Je n'y arrive pas… toute seule. »", [
            R("« La Dre Golay et vous pourriez lui parler ensemble, ici, maintenant qu'il est "
              "là ? Moi, je peux sortir, ou rester, comme vous préférez. »",
              12, "ic2 rd2 cc1 pb1", sets=["daniel_sait"]),
            R("« Je vais le chercher. »", 12, "ic1 pb-1", sets=["daniel_sait"]),
            R("« C'est à vous de lui dire, Madame Pittet. »", 13, "pb1 em-2"),
            R("« Je peux le lui dire, moi, si vous voulez. »", 13, "pb-3 rd-1"),
            R("Regarder la Dre Golay, sans rien dire.", 12, "ic1 pb1",
              sets=["daniel_sait"]),
        ]),
        I(11, "chappuis", "suspicious",
          "Il y a un silence au bout du fil. « Je préfère parler à la Dre Golay. » Vous lui "
          "passez le téléphone. La Dre confirme : quatre-vingts milligrammes, matin et midi. "
          "Puis elle vous regarde, longtemps, sans rien dire.", [go(10)]),
        I(12, "daniel", "resigned",
          "Daniel entre en enlevant sa casquette. La Dre Golay lui parle, à côté de sa mère, "
          "simplement : les reins, le cœur, le refus de la dialyse, la volonté de mourir ici. "
          "Daniel écoute sans un mot, les yeux sur le carrelage. À la fin, il demande "
          "seulement : « C'est pour quand ? » La Dre répond : « Personne ne le sait. Des mois, "
          "peut-être. » Daniel hoche la tête. Il pose la main sur l'épaule de sa mère, la "
          "laisse un instant, et ressort vers l'étable.", [
            R("Rester en retrait, silencieux·se.", 14, "rd2 pb2"),
            R("Le suivre dans la cour : « Monsieur Pittet, ça va ? »", 14, "em1 pb-1"),
            R("« Elle a aussi d'autres volontés, vous savez. »", 14, "pb-3 rd-2"),
            R("Aller s'asseoir près de Jeannine.", 14, "em2 co1"),
            R("Commenter, à mi-voix : « Il l'a plutôt bien pris. »", 14, "rd-1 em-1"),
        ]),
        I(13, "jeannine", "resigned",
          "Jeannine ferme les yeux. « Pas aujourd'hui, alors. » Elle sourit, épuisée. « Le col "
          "n'est pas ouvert. » Dans la cour, le tracteur de Daniel démarre et s'éloigne.", [
            R("« Quand vous serez prête. La Dre Golay et Thierry seront là. Et moi aussi, si "
              "vous le voulez. »", 14, "em2 rd2 pb1"),
            R("« Vous ne pourrez pas attendre éternellement. »", 14, "rd-2 em-1"),
            R("Hocher la tête.", 14, "rd1"),
            R("« Je pourrais lui écrire une lettre, de votre part. »", 14, "pb-2"),
        ]),
        I(14, "golay", "neutral",
          "Dans la voiture, la Dre Golay conduit en silence jusqu'au village. Puis : « Vous "
          "avez entendu les crépitants. Dans vos livres, c'est une insuffisance cardiaque "
          "décompensée. Dans cette cuisine, c'est une femme qui veut mourir chez elle, et un "
          "fils qui a déjà trouvé son père dans un talus. » Elle se gare devant le cabinet. "
          "« Les deux sont vrais. Notre métier, c'est de n'en oublier aucun. »"),
        I(20, "jeannine", "sad",
          "Entre deux respirations, Jeannine vous dévisage. « Le 26… vous n'êtes pas… "
          "venu·e. »", [
            R("« Mon père a fait un infarctus le soir du 24. J'étais à l'hôpital avec lui. "
              "J'aurais dû vous faire prévenir. Pardon. »", 21, "rd2 cc2 pb1 em1"),
            R("« J'ai eu un empêchement. »", 21, "cc-1 rd-1"),
            R("« Thierry ne vous a pas dit ? Mon père était aux soins intensifs. »",
              21, "cc1 ic-1"),
            R("« De toute façon, ce n'était pas mon rôle d'être là. »", 21, "rd-2 em-2"),
            R("« Je suis désolé·e. Comment ça s'est passé, avec Daniel ? »", 21, "em2 rd1"),
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
            R("« Il est toujours aussi aimable ? » à mi-voix, à la Dre Golay.",
              1, "rd-2 pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.6 L'ambulancière — histoire annexe (si Alex a soutenu Yasmine au BLS)
# ---------------------------------------------------------------------------
S3_6 = S(7, "3.6 L'ambulancière",
    "Fin janvier, 23 h. Un message de Yasmine : « t'es debout ? je suis devant chez toi ». "
    "Elle est assise sur le muret, en doudoune, deux cafés à l'emporter à la main.",
    focus=("em", "er", "ic"),
    slot="3.6",
    cond=when(all=["yasmine_soutenue"]),
    annex=True,
    nodes=[
        I(1, "yasmine", "melancholic",
          "Elle vous tend un café. « J'ai appris, pour ton père. Léo me l'a dit. » Un temps. "
          "« Au BLS, tu es venu·e t'asseoir à côté de moi sans rien demander. Je te dois une "
          "histoire, je crois. Si tu veux l'entendre. »", [
            R("« Je veux bien l'entendre. Mais tu ne me dois rien. »", 2, "em2 rd2 pb1"),
            R("« Raconte ! »", 2, "em1 pb-1"),
            R("« Ce n'est pas nécessaire, Yasmine. Je ne t'ai rien demandé. »", 6, "em-1 rd1"),
            R("« Tu n'aurais pas dû venir à cette heure-ci. »", 6, "em-2 rd-1"),
            R("S'asseoir à côté d'elle sur le muret, et attendre.", 2, "em2 co1"),
        ]),
        I(2, "yasmine", "sad",
          "« 2019. Une nuit de novembre. Un appel pour un nourrisson qui ne respire plus, dans "
          "un appartement à Renens. Trois mois. » Elle tourne son gobelet entre ses mains. "
          "« J'ai fait le massage pendant vingt-deux minutes. Avec deux doigts. Le père tenait "
          "la lampe de son téléphone, parce que l'ampoule avait sauté. » Elle se tait. « On "
          "n'a rien pu faire. Mort subite. »", [
            R("Laisser le silence durer. Puis : « Vingt-deux minutes. Avec deux doigts. »",
              3, "em3 co2 er1"),
            R("« Ce n'était pas ta faute. »", 3, "em1 cc-1"),
            R("« Et c'est pour ça que tu as arrêté l'ambulance ? »", 3, "em1 cc1"),
            R("« La mort subite du nourrisson, on ne sait toujours pas bien l'expliquer, "
              "d'ailleurs. »", 4, "em-2 pb-1"),
            R("Lui prendre le bras.", 3, "em2 co2"),
        ]),
        I(3, "yasmine", "vulnerable",
          "« Le père m'a remerciée. Tu te rends compte ? Il m'a remerciée, à la fin. » Elle "
          "rit, et ça ressemble à autre chose. « Après, j'ai fait encore deux ans. Je dormais "
          "dans ma voiture avant les gardes. Mon copain est parti. Et un matin, je me suis "
          "inscrite en médecine. Je me suis dit : si je sais plus de choses, peut-être que la "
          "prochaine fois… »", [
            R("« … tu ne seras pas seule avec deux doigts et une lampe de téléphone. »",
              5, "em3 co2"),
            R("« Tu en as parlé à quelqu'un, à l'époque ? Un débriefing, un psy ? »",
              5, "ic2 em1 pb1"),
            R("« Avec plus de connaissances, tu ne l'aurais pas sauvé. »", 5, "em-2 cc1 co-1"),
            R("« Moi, à ta place, j'aurais arrêté tout de suite. »", 5, "em-1"),
            R("« Et ton copain, il est parti à cause de ça ? »", 5, "pb-2 rd-1"),
        ]),
        I(4, "yasmine", "cold-anger",
          "Yasmine vous regarde. « Je ne t'ai pas demandé un cours, Alex. » Elle se lève à "
          "moitié.", [
            R("« Pardon. Je ne savais pas quoi dire, alors j'ai dit un truc de cours. "
              "Reste. »", 3, "em2 rd2 er1"),
            R("« Ok, ok. »", 6, "em-1"),
            R("« Tu es susceptible. »", 6, "rd-2 em-2"),
            R("Lui tendre son café, sans rien dire.", 3, "em1 co1"),
        ]),
        I(5, "yasmine", "neutral",
          "Yasmine finit son café. « Au BLS, quand le petit mannequin est sorti de sa boîte, "
          "j'avais vingt-deux minutes dans les doigts. » Elle se lève. « Je voulais que "
          "quelqu'un le sache. Au cas où ça m'arrive encore. Que tu saches quoi faire : me "
          "laisser une minute, et puis me secouer. »", [
            R("« D'accord. Une minute, puis je te secoue. Et toi, si tu me vois me figer, "
              "pareil. »", 7, "ic3 em2 er1", sets=["yasmine_alliee"]),
            R("« Tu devrais en parler à un professionnel, plutôt qu'à moi. »",
              7, "ic1 pb1 em-1"),
            R("« Ça ne t'arrivera plus, tu verras. »", 7, "cc-2 em-1"),
            R("« Merci de me faire confiance. » Et la serrer dans vos bras.", 7, "em2 co2",
              sets=["yasmine_alliee"]),
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

CH3 = C(3, "Le cœur, en vrai",
    situation=(
        "Décembre et janvier. À la fac, le module circulation et respiration, et une matinée "
        "de réanimation au centre de simulation. À Noël, le cœur de votre père. En janvier, "
        "celui de Jeannine, qui se noie, et celui de Madame 14, que vous tenez dans vos "
        "mains."
    ),
    objectives=(
        "organiser une réanimation de base avec une communication en boucle fermée ; "
        "reconnaître une douleur thoracique qui impose d'appeler le 144, même — surtout — "
        "pour un proche ; ne pas jouer au médecin dans sa propre famille ; dire la vérité aux "
        "soignants sur le déroulement des faits ; reconnaître et réguler ses émotions en "
        "salle de dissection ; examiner une patiente en respectant sa pudeur et sa parole ; "
        "respecter un refus d'hospitalisation éclairé ; transmettre une ordonnance sans "
        "erreur (lecture mot pour mot, répétition) ; soutenir une collègue sans la forcer à "
        "parler."
    ),
    anchoring=(
        "UNIL BMed2.4 (circulation, respiration) et BMed2.8 (urgences et réanimation, examen "
        "cardio-respiratoire) · UNIGE Cœur et circulation, Respiration, compétences "
        "cliniques (gestes de base) · UZH Humanbiologie I (Herz-Kreislauf, Atmung), "
        "Klinischer Untersuchungskurs I, Praktikum Physiologie I (ECG, tension, "
        "spirométrie)."
    ),
    focus=("er", "cc", "ic", "em"),
    scenes=[S3_1, S3_2, S3_3A, S3_3B, S3_4, S3_5, S3_6],
)
