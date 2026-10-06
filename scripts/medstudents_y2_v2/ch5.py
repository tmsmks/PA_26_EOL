"""Chapitre 5 — Ce que le village sait (avril).

Six scènes jouées, sept ou huit écrites :
  5.1 Six kilos · 5.2 La table de la cuisine · 5.3 La grange
  5.4 branche parallèle : « L'appel de 23 h » (Alex a donné son numéro à Jeannine)
      ou « La nuit sur le carrelage »
  5.5 L'atelier · 5.6 Le cabinet ferme
  5.7 histoire annexe « Le balcon » (si Alex a promis de revenir voir son père)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, StartChoice, go, when

# ---------------------------------------------------------------------------
# 5.1 Six kilos
# ---------------------------------------------------------------------------
S5_1 = S(1, "5.1 Six kilos",
    "Début avril. Visite de contrôle aux Combettes avec Thierry et Aline Morel, la "
    "diététicienne du CMS. Jeannine a perdu six kilos depuis février. Ses reins continuent "
    "de baisser ; la Dre Golay parle d'urémie. Elle dit que tout a un goût de métal.",
    focus=("em", "cc", "ic"),
    nodes=[
        I(1, "thierry", "neutral",
          "Dans la Panda, Thierry vous tend une feuille : un questionnaire de dépistage de la "
          "dénutrition. « Aline mène l'entretien, tu remplis le questionnaire avec elle. Et tu "
          "regardes. » Il se gare. « Jeannine ment sur ses repas. Elle ment très bien. Il m'a "
          "fallu des années pour apprendre à le voir. »", [
            R("« Je remplis le questionnaire, et je te dirai ce que je vois que le "
              "questionnaire ne dit pas. »", 2, "ic3 cc1 rd1"),
            R("« Je regarde quoi, exactement ? »", 2, "ic2 cc1"),
            R("« Pourquoi elle mentirait ? »", 2, "em1 cc1"),
            R("« Si elle ment, on n'a qu'à la peser tous les jours. »", 2, "rd-2 em-1"),
            R("« Les personnes âgées mangent peu, c'est normal. »", 2, "cc-2 em-1"),
        ]),
        I(2, "jeannine", "happy",
          "Jeannine vous attend à la table, coiffée, le foulard rouge, un sourire de "
          "circonstance. « J'ai fait une omelette ce midi. Trois œufs. Et une tarte aux pommes "
          "hier. » Aline sourit, note. Sur la cuisinière, la poêle est propre et sèche. Dans "
          "l'évier, une seule tasse.", [
            R("Dire à Aline, devant Jeannine : « La poêle est sèche. »", 3, "rd-2 cc1 em-2"),
            R("Ne rien dire, et poser une question ouverte : « Racontez-moi votre journée "
              "d'hier, depuis le réveil. »", 4, "cc3 rd2 em1"),
            R("« Trois œufs ! Vous avez bon appétit. »", 5, "cc-1 em-1"),
            R("Ouvrir le frigo pour vérifier.", 3, "rd-3 pb-2"),
            R("Croiser le regard de Thierry, qui a vu la même chose.", 4, "ic2 cc1"),
        ]),
        I(3, "jeannine", "cold-anger",
          "Jeannine pose ses mains à plat sur la toile cirée. « Vous faites l'inventaire de ma "
          "cuisine, maintenant ? » Aline pose son stylo. Thierry regarde par la fenêtre. Le "
          "silence est épais.", [
            R("« Pardon, Madame Pittet. C'était intrusif. Ce qui m'inquiète, c'est vous, pas "
              "votre frigo. Comment ça se passe, les repas, en vrai ? »", 4, "rd2 em2 cc1 er1"),
            R("« C'est pour votre bien. »", 5, "rd-2 pb-1"),
            R("« Vous mentez, on le voit tous. »", 5, "rd-3 em-2"),
            R("Se taire.", 5, "er-1"),
        ]),
        I(4, "jeannine", "sad",
          "Jeannine regarde ses mains, longtemps. « Hier ? Un café. Une biscotte. Une "
          "demi-pomme. » Elle hausse les épaules. « Tout a un goût de fer rouillé. Et manger "
          "seule… » Elle s'arrête. « Mon mari mangeait comme quatre. Je cuisinais pour lui. "
          "Après, j'ai cuisiné pour Daniel, quand il venait. Il ne vient plus manger. »", [
            R("« Merci de nous le dire. Le goût de métal, la Dre Golay en avait parlé : Aline "
              "pourra peut-être vous aider à le rendre moins pénible. Et manger seule… c'est "
              "peut-être le plus dur. »", 6, "em3 cc2 rd1"),
            R("« Il faut manger, Madame Pittet, sinon vous allez vous affaiblir. »",
              5, "rd-1 em-2 cc-1"),
            R("Laisser Aline reprendre : c'est elle la spécialiste.", 6, "ic2 rd1"),
            R("« Et Daniel, pourquoi il ne vient plus ? »", 7, "em1 pb-1"),
            R("« Vous voulez que je vous apporte des petits plats ? »", 6, "pb-3 em1"),
        ]),
        I(5, "aline", "neutral",
          "Aline pose une main sur l'avant-bras de Jeannine. « On va faire autrement. » Elle "
          "ne parle ni de calories ni de protéines. Elle demande ce que Jeannine aimait manger "
          "enfant, ce qui passe encore, ce qui ne passe plus. Au bout de vingt minutes, "
          "Jeannine raconte les röstis de sa mère. Aline vous jette un coup d'œil : regardez "
          "comment on fait.", [
            R("Observer, sans intervenir, et noter ce qu'elle fait.", 6, "ic3 rd1"),
            R("Profiter de la pause pour remplir le questionnaire.", 6, "ic-1 cc1"),
            R("Interrompre : « Et les protéines, il en faut combien ? »", 6, "ic-2 rd-1"),
            R("Regarder votre téléphone.", 6, "ic-2 rd-1"),
        ]),
        I(6, "aline", "neutral",
          "Aline résume : de petites portions, plusieurs fois par jour ; du froid plutôt que du "
          "chaud, le goût de métal se sent moins ; des bonbons acidulés avant les repas ; un "
          "repas livré trois fois par semaine. Thierry ajoute une pesée chaque semaine. "
          "Jeannine écoute, les bras croisés. « Et le repas livré, je le mange avec qui ? »", [
            R("« C'est une vraie question. Est-ce qu'il y a quelqu'un — Océane, une voisine — "
              "avec qui vous aimeriez manger, certains jours ? »", 8, "em3 cc1 ic1"),
            R("« Avec la télé. »", 8, "em-2 rd-1"),
            R("« Je viendrai manger avec vous le jeudi. »", 9, "pb-3 em2"),
            R("Regarder Thierry : le réseau, c'est son domaine.", 8, "ic2"),
            R("« Il faudra en parler avec Daniel. »", 8, "ic1 em1"),
        ]),
        I(7, "jeannine", "cold-anger",
          "« Pourquoi il ne vient plus ? » Jeannine vous regarde par-dessus ses lunettes. "
          "« Ça, c'est entre mon fils et moi. » Puis, plus bas : « Il a peur de me regarder "
          "manger. Il voit sa mère qui maigrit, et il revoit son père dans le talus. Il ne sait "
          "pas faire, avec les corps qui s'abîment. »", [
            R("« Pardon, ce n'était pas à moi de demander. Merci de me l'avoir dit quand "
              "même. »", 6, "rd2 pb1 em1"),
            R("« Il devrait faire un effort. »", 6, "rd-2 em-1"),
            R("Hocher la tête, en silence.", 6, "em1 rd1"),
            R("« Vous voulez qu'on en parle avec lui, avec la Dre Golay ? »", 6, "ic2 em1 cc1"),
        ]),
        I(8, "thierry", "resigned",
          "Dans la Panda, Thierry ne démarre pas tout de suite. « Six kilos. » Il tapote le "
          "volant. « Avec des reins comme ça, on ne va pas la remplumer. On va la garder chez "
          "elle, et faire qu'elle ait encore envie de quelque chose. » Il démarre. « La "
          "Dre Golay veut faire une réunion de famille, la semaine prochaine. Tous ensemble, "
          "dans la cuisine. Elle voudrait que tu sois là. »", [
            R("« Si Jeannine est d'accord, je viendrai. Pour écouter. »", END, "pb2 rd2 ic1"),
            R("« Une réunion de famille, c'est pour les médecins, non ? »", END, "ic-1 er-1"),
            R("« Je viendrai. »", END, "ic1"),
            R("« Moi aussi, j'aurais du mal à la regarder maigrir. »", END, "er2 em1"),
        ]),
        I(9, "thierry", "neutral",
          "Aline lève les yeux de son carnet. Thierry aussi. « Alex, dit Thierry doucement, tu "
          "es là jusqu'en juin. Et après ? » Jeannine sourit, mais ses yeux brillent. « Il a "
          "raison, le Thierry. Ne promettez pas ce que vous ne pourrez pas tenir, petit. »", [
            R("« Vous avez raison. Pardon. On cherche avec Thierry qui pourrait venir, pour de "
              "vrai, et longtemps. »", 8, "pb3 ic2 er1"),
            R("« Mais je veux vraiment venir ! »", 8, "pb-2 er-1"),
            R("Se taire, rouge.", 8, "er1"),
            R("« Je pourrais venir quelques fois, sans rien promettre. »", 8, "pb1 em1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.2 La table de la cuisine
# ---------------------------------------------------------------------------
_INTRO_52 = (
    "Mardi, 18 h. La cuisine des Combettes. Autour de la toile cirée : Jeannine, dans son "
    "fauteuil ; la Dre Golay ; Thierry ; Daniel, debout près de la porte, la casquette dans "
    "les mains ; Océane, assise sur le plan de travail. Et vous, près du fourneau. Daniel ne "
    "sait presque rien. La Dre Golay ouvre la réunion."
)
_INTRO_52_MALADIE = (
    "Mardi, 18 h. La cuisine des Combettes. Autour de la toile cirée : Jeannine, dans son "
    "fauteuil ; la Dre Golay ; Thierry ; Daniel, debout près de la porte, la casquette dans "
    "les mains ; Océane, assise sur le plan de travail. Et vous, près du fourneau. Daniel "
    "sait, pour les reins et le cœur. Il ne sait pas tout. La Dre Golay ouvre la réunion."
)
_INTRO_52_DON = (
    "Mardi, 18 h. La cuisine des Combettes. Autour de la toile cirée : Jeannine, dans son "
    "fauteuil ; la Dre Golay ; Thierry ; Daniel, debout près de la porte, la casquette dans "
    "les mains ; Océane, assise sur le plan de travail. Et vous, près du fourneau. Daniel "
    "sait tout, y compris pour le don du corps. Il ne l'a jamais accepté."
)

S5_2 = S(2, "5.2 La table de la cuisine", _INTRO_52,
    focus=("ic", "rd", "pb", "cc"),
    entries=[
        Entry(30, when(any=["revele_a_daniel", "noel_annonce"]), _INTRO_52_DON),
        Entry(1, when(any=["info_lachee", "erreur_homonyme", "daniel_sait"]),
              _INTRO_52_MALADIE),
    ],
    debriefs=[
        Debrief(when(all=["famille_dechiree"]), tone="hard", lead=(
            "La réunion s'est brisée. Ce n'est pas toujours la faute de quelqu'un : une famille "
            "a le droit d'exploser devant la mort qui vient. Mais dans une réunion de famille, "
            "l'étudiant·e n'est ni l'avocat·e de la patiente ni celui ou celle qui explique au "
            "fils ce qu'il doit ressentir. Rester à sa place, rapporter fidèlement les mots de "
            "la patiente quand elle le demande, ne jamais révéler ce qu'elle a confié : c'est "
            "ce qui laisse la porte ouverte pour la suite.")),
        Debrief(when(all=["famille_apaisee"]), tone="good", lead=(
            "Daniel a pris la main de sa mère. Il n'a pas changé d'avis sur le don, mais il ne "
            "s'y opposera pas. C'est souvent ainsi que se terminent les bonnes réunions de "
            "famille : pas d'accord parfait, mais une volonté entendue, et un fils qui reste. "
            "Votre rôle était petit, et c'était le bon : laisser la parole à ceux à qui elle "
            "appartient.")),
    ],
    nodes=[
        I(1, "golay", "neutral",
          "La Dre Golay parle simplement : les reins qui s'arrêtent, le cœur qui se noie, les "
          "six kilos, les chutes. « Votre mère a décidé de ne pas faire de dialyse. Elle veut "
          "rester ici, jusqu'au bout. Nous sommes là pour en parler ensemble. » Daniel ne "
          "s'assied pas. « Jusqu'au bout. » Il regarde sa mère. « Il y a un EMS à Orbe avec une "
          "place en mai. Et la dialyse, à Yverdon, il y a un transport. On peut "
          "s'organiser. »", [
            R("Rester en retrait, silencieux·se : ce n'est pas votre réunion.",
              2, "pb2 rd1 ic1"),
            R("« Votre mère a le droit de refuser la dialyse, Monsieur Pittet. »",
              3, "rd1 pb-2 em-2"),
            R("Regarder Jeannine, pour voir si elle veut répondre elle-même.", 2, "rd2 em1"),
            R("« Une place en EMS en mai, c'est une chance. »", 3, "rd-2 pb-2"),
            R("Noter ce que dit chacun, pour le compte rendu de la Dre Golay.", 2, "ic1 cc1"),
        ]),
        I(2, "jeannine", "neutral",
          "Jeannine laisse Daniel finir. Puis : « Daniel. Assieds-toi. » Il ne s'assied pas. "
          "« Pas d'EMS. Pas de machine. Je veux mourir ici, dans ma cuisine, avec la fenêtre "
          "ouverte. » Elle reprend son souffle. « Et il y a autre chose. Après. Mon corps, je "
          "l'ai donné à la faculté de médecine. Pour les étudiants. » Daniel blêmit. Océane "
          "retient son souffle. Jeannine se tourne vers vous. « Dites-leur, vous. Ce que je "
          "vous ai dit en septembre. Pourquoi. »", [
            R("« Ce n'est pas à moi de parler à votre place, Madame Pittet. Mais si vous le "
              "voulez, je peux répéter ce que vous m'avez dit, avec vos mots, et vous me "
              "corrigez. »", 4, "pb2 rd2 cc2"),
            R("« Votre mère m'a dit qu'elle avait mis au monde six cents enfants, et qu'il "
              "fallait bien que quelqu'un nous apprenne à recevoir le reste. Ceux qui "
              "partent. »", 4, "cc2 rd2 co1 pb-1"),
            R("« Je ne peux rien dire : c'est le secret médical. »", 5, "pb1 em-2 rd-1"),
            R("« C'est un très beau geste, Monsieur Pittet. Vous devriez être fier. »",
              6, "pb-2 em-2 rd-1"),
            R("Regarder la Dre Golay, pour qu'elle réponde.", 5, "ic1 er-1"),
        ]),
        I(3, "daniel", "cold-anger",
          "La Dre Golay lève une main, sans vous regarder. Daniel se tourne vers vous, "
          "lentement. « Et vous, vous êtes qui, pour me dire ce qui est bien pour ma mère ? "
          "Vous êtes là depuis septembre. Moi, depuis cinquante-quatre ans. »", [
            R("« Vous avez raison. Ce n'était pas à moi de parler. Pardon. »",
              2, "rd2 pb2 er1"),
            R("« Je suis là pour votre mère. »", 6, "pb-1 rd-1 ic-1"),
            R("Se taire, rouge.", 2, "er1"),
            R("« Je connais le droit, monsieur. »", 6, "rd-3 pb-2"),
        ]),
        I(4, "daniel", "cold-anger",
          "Daniel regarde sa mère. Sa voix est très basse. « En morceaux. Dans une cave, en "
          "ville. Avec des gamins comme lui qui rigolent. » Il vous désigne du menton. « Je "
          "sais comment ils sont. J'ai vu des trucs. Des photos, sur internet. » Océane "
          "descend du plan de travail.", [
            R("« Vous avez raison d'avoir peur de ça. Il y a des étudiant·e·s qui font des "
              "erreurs — j'en ai vu, et j'en ai fait. Mais la salle n'est pas une cave, et les "
              "donneurs ne sont jamais seuls : il y a des règles, et chaque année une "
              "cérémonie pour les remercier. »", 7, "cc3 rd2 er1 pb1"),
            R("« Personne ne rigole, en dissection. »", 6, "cc-2 pb-1"),
            R("Se taire.", 7, "er-1"),
            R("« C'est la décision de votre mère, pas la vôtre. »", 6, "rd1 em-3 pb-1"),
            R("Laisser la Dre Golay répondre, et ne parler que si elle vous le demande.",
              7, "ic2 pb2"),
        ]),
        I(5, "jeannine", "sad",
          "Jeannine soupire. « Bon. Je vais le dire moi-même, alors. » Elle parle de ses six "
          "cents enfants, des accouchements dans les granges sans électricité, de l'idée qui "
          "lui est venue un soir, en regardant un reportage : apprendre aux jeunes à recevoir "
          "ceux qui partent. Elle le dit mieux que vous ne l'auriez fait. Daniel l'écoute sans "
          "la regarder.", [go(4)]),
        I(6, "daniel", "angry",
          "Daniel frappe la table du plat de la main. Les tasses sautent. « Personne ne va "
          "découper ma mère ! » Il sort. La porte claque. Dans la cour, le tracteur démarre. "
          "Jeannine ferme les yeux. Océane pleure.", [
            R("Ne pas le suivre. Rester près de Jeannine et d'Océane, et laisser la Dre Golay "
              "décider de la suite.", 9, "pb2 ic2 em1", sets=["famille_dechiree"]),
            R("Courir après lui dans la cour.", 10, "pb-2 em1"),
            R("« Il va revenir. Il a besoin de temps. »", 9, "cc-1 em1",
              sets=["famille_dechiree"]),
            R("« C'est ma faute, je n'aurais pas dû parler. »", 9, "er-2",
              sets=["famille_dechiree"]),
            R("« Il est toujours comme ça, votre fils ? »", 9, "rd-2 em-2",
              sets=["famille_dechiree"]),
        ]),
        I(7, "daniel", "sad",
          "Daniel s'assied enfin, sur la chaise la plus proche de la porte. Long silence. "
          "Puis, à sa mère, sans vous regarder : « Pourquoi ? Pourquoi tu veux qu'ils "
          "t'emmènent, là-bas ? » Jeannine ouvre la bouche. Rien ne sort. Elle vous regarde. "
          "La Dre Golay aussi.", [
            R("« Je crois que c'est à votre mère de répondre. Prenez votre temps, Madame "
              "Pittet. »", 8, "pb2 rd2 em1"),
            R("« Elle avait peur de votre réaction, à cause de votre père. »",
              6, "pb-3 rd-3 em-1"),
            R("« Elle voulait vous protéger. »", 8, "pb-1 em1"),
            R("Se lever pour sortir, et laisser la famille entre elle.", 8, "rd2 pb2"),
            R("Fixer la table.", 8, "er-1"),
        ]),
        I(8, "jeannine", "melancholic",
          "Jeannine tend la main vers son fils, par-dessus la toile cirée. « Parce que j'ai "
          "passé ma vie à aider les gens à arriver. Je veux aider ceux qui soigneront les gens "
          "qui partent. » Un temps. « Et parce que tu as tenu ton père une heure dans le talus. "
          "Je ne voulais pas que tu aies à t'occuper de mon corps, à moi. » Daniel baisse la "
          "tête. Ses épaules tremblent. Au bout d'un long moment, il prend la main de sa mère. "
          "« Je ne viendrai pas à la cérémonie. » Un temps. « Mais je ne t'empêcherai pas. »", [
            R("Rester immobile, en silence, et laisser ce moment leur appartenir.",
              11, "rd3 co2 er1", sets=["famille_apaisee"]),
            R("Sortir sans bruit dans la cour.", 11, "rd2 pb2", sets=["famille_apaisee"]),
            R("« Vous voyez, ce n'était pas si difficile. »", 11, "rd-3 em-2",
              sets=["famille_apaisee"]),
            R("Prendre en photo les deux mains, pour Océane.", 11, "rd-3 pb-3",
              sets=["famille_apaisee"]),
            R("Pleurer, et devoir sortir.", 11, "er-1 co1", sets=["famille_apaisee"]),
        ]),
        I(9, "golay", "resigned",
          "La Dre Golay attend que le bruit du tracteur se soit éteint. « Ça ne s'arrête pas "
          "ce soir, Jeannine. Il reviendra demain matin, pour les bêtes. Et on "
          "recommencera. » Jeannine ne répond pas. Océane s'assied par terre, la tête contre "
          "le genou de sa grand-mère."),
        I(10, "daniel", "cold-anger",
          "Daniel est dans la cour, la main sur le capot du tracteur. Il ne se retourne pas. "
          "« Retournez à l'intérieur. » Sa voix se casse. « Vous n'êtes pas de la famille. »", [
            R("« Vous avez raison. Je retourne à l'intérieur. » Et y retourner.",
              9, "pb3 rd1", sets=["famille_dechiree"]),
            R("« Votre mère a besoin de vous, maintenant. »", 9, "pb-2 em1",
              sets=["famille_dechiree"]),
            R("Poser une main sur son épaule.", 9, "pb-3 em1", sets=["famille_dechiree"]),
            R("« Je comprends ce que vous ressentez. »", 9, "pb-2 em-1",
              sets=["famille_dechiree"]),
        ]),
        I(11, "narr", "",
          "La Dre Golay range ses papiers sans bruit. Thierry fait du café. Océane s'est "
          "assise par terre, la tête contre le genou de sa grand-mère. Daniel n'a pas lâché la "
          "main de sa mère. Dehors, il fait nuit. Personne ne parle plus de l'EMS d'Orbe."),
        I(30, "daniel", "cold-anger",
          "Daniel ne s'assied pas. Avant même que la Dre Golay ait ouvert la bouche : « Si on "
          "est là pour parler de la cave, je m'en vais. » Jeannine soupire. La Dre Golay, "
          "calmement : « On est là pour parler de votre mère. De tout. »", [
            R("Rester en retrait, et laisser la Dre Golay mener.", 31, "pb2 rd1 ic1"),
            R("« Ce n'est pas une cave, monsieur. »", 32, "pb-2 rd-1"),
            R("Regarder Jeannine.", 31, "rd2 em1"),
            R("« J'étais en salle de dissection lundi. Je peux vous raconter comment ça se "
              "passe, si vous voulez. »", 32, "pb-2 cc1 er-1"),
        ]),
        I(31, "golay", "neutral",
          "La Dre Golay déroule la situation : les reins, le cœur, les six kilos, les chutes, "
          "le refus de la dialyse, la volonté de mourir ici. Daniel écoute, debout. À la fin : "
          "« Il y a un EMS à Orbe avec une place en mai. » Jeannine : « Non. » Daniel se "
          "tourne vers vous. « Et vous ? Vous allez la découper, vous aussi, un jour ? »", [
            R("« Non. Les étudiant·e·s qui dissèquent ne savent jamais qui est la personne "
              "devant eux. C'est la règle : l'anonymat. Personne ne saura que c'est elle. »",
              7, "cc3 rd2 pb1"),
            R("« Peut-être. Je ne sais pas. »", 6, "cc-2 em-1"),
            R("« Ce n'est pas une boucherie, monsieur. »", 6, "rd-1 em-2"),
            R("Laisser la Dre Golay répondre.", 7, "ic2 pb1"),
            R("« Ça, il faudrait le demander à la Pre Vautier, à l'institut. Je peux vous donner "
              "son contact. »", 7, "ic2 cc1 pb1"),
        ]),
        I(32, "daniel", "cold-anger",
          "La Dre Golay lève une main, sans vous regarder. Daniel se tourne vers vous, "
          "lentement. « Vous, vous allez m'expliquer ce que c'est ? Vous êtes là depuis "
          "septembre. Moi, depuis cinquante-quatre ans. »", [
            R("« Vous avez raison. Ce n'était pas à moi de parler. Pardon. »",
              31, "rd2 pb2 er1"),
            R("« Je suis là pour votre mère. »", 6, "pb-1 rd-1 ic-1"),
            R("Se taire, rouge.", 31, "er1"),
            R("« Je sais de quoi je parle, monsieur. »", 6, "rd-3 pb-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.3 La grange
# ---------------------------------------------------------------------------
_INTRO_53 = (
    "Après la réunion. Il fait nuit. Océane vous attend dans la grange, assise sur une botte "
    "de paille, l'écran de son téléphone allumé comme une lampe."
)

S5_3 = S(3, "5.3 La grange", _INTRO_53,
    focus=("em", "rd", "pb", "co"),
    entries=[
        Entry(1, when(all=["oceane_confiance"]), _INTRO_53),
        Entry(10, when(none=["oceane_confiance"]), _INTRO_53),
    ],
    debriefs=[
        Debrief(when(all=["oceane_trahie"]), tone="hard", lead=(
            "Océane a dix-sept ans et elle est capable de discernement : c'est elle qui "
            "décide qui apprend sa grossesse, et quand — son père, sa grand-mère, sa "
            "médecin. Le secret qu'elle vous a confié n'était pas à vous. On peut s'inquiéter "
            "pour une mineure sans la trahir : l'écouter, l'orienter vers des professionnels "
            "tenus au secret, et rester disponible.")),
        Debrief(when(all=["oceane_seule"]), tone="mixed", lead=(
            "Vous avez gardé le secret d'Océane, et c'était juste. Mais elle est repartie "
            "seule, sans savoir vers qui se tourner. Garder un secret ne suffit pas : on peut "
            "donner, sans rien décider à sa place, le nom des personnes dont c'est le métier "
            "d'aider — un centre de santé sexuelle, sa médecin, tenue au secret même envers "
            "son père.")),
        Debrief(when(all=["oceane_orientee"]), tone="good", lead=(
            "Vous n'avez rien décidé pour Océane, rien dit à son père, et vous ne l'avez pas "
            "laissée seule : un numéro, des horaires, le droit de changer d'avis. C'est "
            "exactement ce qu'on peut faire, et pas davantage, quand une adolescente confie "
            "une grossesse.")),
    ],
    nodes=[
        I(1, "oceane", "vulnerable",
          "« Je peux te dire un truc ? Un vrai secret. » Elle éteint son téléphone. Dans le "
          "noir, sa voix. « Je suis enceinte. Dix semaines. Personne ne sait. Ni mon copain, ni "
          "papa. Juste mamie, peut-être : elle me regarde bizarrement depuis Pâques. » Un "
          "temps. « Elle ne peut pas mourir maintenant. Tu comprends ? Pas maintenant. »", [
            R("Laisser un silence. Puis : « Merci de me le dire. Ça fait beaucoup, en même "
              "temps : ta grand-mère, et ça. Comment tu te sens, toi ? »", 2, "em3 co2 rd1"),
            R("« Tu vas le garder ? »", 3, "pb-2 rd-2"),
            R("« Il faut le dire à ton père. »", 4, "pb-3 rd-2"),
            R("« Félicitations ! »", 3, "em-1 cc-1"),
            R("« Tu as vu un médecin ? »", 5, "cc2 pb1"),
        ]),
        I(2, "oceane", "sad",
          "« Mal. » Elle rit et pleure à la fois. « Je ne sais pas si je le veux. Je ne sais "
          "rien. J'ai dix-sept ans, je suis en deuxième année d'apprentissage, et mon père ne "
          "parle à personne. » Elle s'essuie le nez sur sa manche. « Toi, tu sais des trucs. "
          "Dis-moi quoi faire. »", [
            R("« Je ne peux pas décider pour toi, et personne ne devrait. Mais tu n'as pas à "
              "décider seule : il y a des gens dont c'est le métier de t'aider à réfléchir, "
              "sans te juger. Le centre de santé sexuelle, ou la Dre Golay. Tu veux qu'on "
              "regarde ensemble comment les contacter ? »", 6, "pb3 cc2 em2 ic1 rd1",
              sets=["oceane_orientee"]),
            R("« À ta place, je le garderais. Ta grand-mère serait si heureuse. »",
              7, "pb-3 rd-2"),
            R("« À ta place, je ne le garderais pas. Tu as dix-sept ans. »", 7, "pb-3 rd-2"),
            R("« Parles-en à ta grand-mère : elle a été sage-femme. »", 6, "pb1 ic1 em1",
              sets=["oceane_orientee"]),
            R("« Je ne sais pas quoi te dire. »", 7, "em1 cc-1"),
        ]),
        I(3, "oceane", "cold-anger",
          "Océane se raidit. « Je t'ai dit que j'étais enceinte, pas que je voulais ton "
          "avis. » Elle ramène ses genoux contre elle.", [
            R("« Tu as raison. Pardon. Je t'écoute, c'est tout. »", 2, "rd2 em2 er1"),
            R("« Je voulais juste savoir. »", 7, "pb-1 em-1"),
            R("« Ok, ok. »", 7, "em-1"),
            R("« Il faut quand même que tu réfléchisses vite, à dix semaines. »",
              7, "pb-2 em-2"),
        ]),
        I(4, "oceane", "angry",
          "« Mon père ? » Océane se lève d'un bond. « Mon père ne sait même pas regarder sa "
          "mère maigrir ! Tu veux que je lui annonce ça ce soir, après ça ? » Elle vous fixe. "
          "« Si tu lui dis, je ne te parle plus jamais. »", [
            R("« Je ne lui dirai rien. Ni à lui, ni à personne. C'est à toi de décider qui sait, "
              "et quand. Pardon. »", 2, "pb3 rd2 er1"),
            R("« Il a le droit de savoir : tu es mineure. »", 12, "pb-3 rd-2"),
            R("« D'accord, je ne dirai rien. »", 7, "pb1"),
            R("Se taire.", 7, "er-1"),
        ]),
        I(5, "oceane", "suspicious",
          "« Un médecin ? Pour qu'il le dise à papa ? » Elle secoue la tête. « On est dans un "
          "village. La Dre Golay a soigné toute ma famille. »", [
            R("« La Dre Golay est tenue au secret, même envers ton père : à dix-sept ans, c'est "
              "toi qui décides qui sait. Et si tu préfères quelqu'un d'extérieur, il y a le "
              "centre de santé sexuelle, à Yverdon. Personne ne le saura. »", 6,
              "cc3 pb2 em1", sets=["oceane_orientee"]),
            R("« Ton père le saura de toute façon. »", 7, "pb-2 em-2"),
            R("« Je ne sais pas comment ça marche, pour les mineures. »", 7, "cc-1"),
            R("« Si tu veux, je demande à la Dre Golay comment ça se passe, sans dire ton "
              "nom. »", 6, "pb-1 em1 ic1", sets=["oceane_orientee"]),
        ]),
        I(6, "oceane", "grateful",
          "Océane rallume son téléphone. Vous cherchez ensemble le numéro du centre de santé "
          "sexuelle, et les horaires. Elle l'enregistre sous « Fleuriste Yverdon ». Elle rit, "
          "pour la première fois de la soirée. « Mamie, je lui dirai. Avant… avant. » Elle se "
          "lève, s'époussette. « Merci de ne pas m'avoir dit quoi faire. »", [
            R("« Tu as le droit de changer d'avis, sur tout, à tout moment. Et si tu veux que "
              "quelqu'un t'accompagne au rendez-vous, demande à quelqu'un en qui tu as "
              "confiance. »", END, "em2 pb2 cc1", sets=["oceane_orientee"]),
            R("« Tiens-moi au courant. »", END, "pb-1 em1", sets=["oceane_orientee"]),
            R("« Je peux venir avec toi, si tu veux. »", END, "pb-3 em1",
              sets=["oceane_orientee"]),
            R("La laisser partir, et rester un moment dans la grange.", END, "er1 rd1",
              sets=["oceane_orientee"]),
        ]),
        I(7, "oceane", "hurt",
          "Océane hausse les épaules. « Laisse tomber. » Elle se lève. « T'es comme les "
          "autres. » Elle sort de la grange. Dans la cour, vous l'entendez ouvrir la portière "
          "de sa Twingo.", [
            R("La rattraper : « Océane, attends. Je me suis mal exprimé·e. Tu peux trouver de "
              "l'aide sans que ton père le sache. Je te donne le numéro du centre de santé "
              "sexuelle ? »", 6, "pb2 em2 cc2", sets=["oceane_orientee"]),
            R("La laisser partir.", END, "em-1", sets=["oceane_seule"]),
            R("Lui envoyer un message plus tard : « désolé·e ».", END, "em1",
              sets=["oceane_seule"]),
            R("Aller le dire à la Dre Golay, sans son accord, « pour son bien ».", 9,
              "pb-3 rd-2", sets=["oceane_trahie"]),
        ]),
        I(8, "daniel", "angry",
          "Daniel est assis sur le marchepied du tracteur. Vous vous entendez lui dire : "
          "« Il faut que vous parliez à Océane. Elle a besoin de vous. Elle est enceinte. » "
          "Daniel vous regarde comme si vous lui aviez tiré dessus. Derrière vous, sur le seuil "
          "de la grange, Océane a tout entendu.", [
            R("« Océane, pardon. Je n'avais pas le droit. »", END, "pb2 rd2",
              sets=["oceane_trahie"]),
            R("« C'était pour ton bien. »", END, "pb-3 rd-2", sets=["oceane_trahie"]),
            R("Partir, sans un mot.", END, "er-2 rd-1", sets=["oceane_trahie"]),
            R("« Monsieur Pittet, soyez doux avec elle. »", END, "pb-2 em1",
              sets=["oceane_trahie"]),
        ]),
        I(9, "golay", "resigned",
          "La Dre Golay vous écoute, dans sa voiture, les phares allumés. Puis : « Vous avez "
          "bien fait de vous inquiéter. Mais elle a dix-sept ans, elle est capable de "
          "discernement : c'était à elle de décider si elle voulait m'en parler. Maintenant, "
          "elle saura que ce qu'elle dit dans une grange finit dans ma voiture. » Elle soupire. "
          "« Je l'appellerai. Et je lui dirai que vous m'avez parlé. Je ne mentirai pas pour "
          "vous. »"),
        I(10, "oceane", "angry",
          "Océane est assise dans le noir. Quand vous entrez, elle ne lève pas les yeux. "
          "« Qu'est-ce que tu veux ? Raconter à tout le monde ce qui se passe chez nous ? » "
          "Puis, d'un coup, elle se penche et vomit dans la paille. Elle reste pliée en deux, "
          "les mains sur les genoux.", [
            R("S'accroupir à côté d'elle, lui tendre un mouchoir, et attendre. « Je ne raconte "
              "rien. Ça va ? »", 11, "em3 rd1 pb1"),
            R("« C'est le stress de la réunion. »", 11, "cc-1"),
            R("« Tu es enceinte ? »", 3, "pb-2 rd-2"),
            R("Aller chercher Thierry.", 11, "ic1 pb-1 em-1"),
            R("Ressortir, gêné·e.", 7, "em-2"),
        ]),
        I(11, "oceane", "suspicious",
          "Océane s'essuie la bouche. Elle rit, sans joie. « Ça fait trois semaines que je "
          "vomis tous les matins. Je suis enceinte. Voilà. » Elle vous regarde, défiante. "
          "« Content·e ? Maintenant tu sais un truc que mon père ne sait pas. »", [
            R("« Je ne dirai rien à personne. C'est à toi de décider qui sait. Et toi, comment "
              "tu te sens ? »", 2, "pb3 em2 rd1"),
            R("« Il faut le dire à ton père. »", 4, "pb-3 rd-2"),
            R("« Tu vas le garder ? »", 3, "pb-2 rd-2"),
            R("« Tu as vu un médecin ? »", 5, "cc2 pb1"),
        ]),
        I(12, "oceane", "angry",
          "« Si tu lui dis, je te jure… » Océane a les poings serrés. Par la porte de la "
          "grange, on voit Daniel dans la cour, assis sur le marchepied du tracteur, la tête "
          "dans les mains.", [
            R("« Je ne lui dirai pas. Je me suis trompé·e : c'est toi qui décides. »",
              2, "pb3 rd2 er1"),
            R("Sortir rejoindre Daniel dans la cour.", 8, "pb-3 rd-3 em-1"),
            R("« Alors dis-le-lui toi-même. Ce soir. »", 7, "pb-2 rd-1"),
            R("Se taire, et regarder Daniel par la porte.", 7, "er-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.4 L'appel de 23 h — branche « Alex a donné son numéro »
# ---------------------------------------------------------------------------
S5_4A = S(4, "5.4 L'appel de 23 h",
    "Un jeudi d'avril, 23 h 04. Votre téléphone sonne : un numéro fixe que vous ne "
    "connaissez pas. Vous décrochez. Une respiration, avant la voix. « C'est… Jeannine. »",
    focus=("pb", "er", "ic"),
    slot="5.4",
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
            R("« Jeannine, j'appelle le 144 pour vous, maintenant, et je vous rappelle tout de "
              "suite après. Restez assise, les jambes pendantes. Vous avez votre bracelet ? "
              "Appuyez dessus aussi. »", 2, "ic3 cc2 er2 pb2"),
            R("« J'arrive. Je suis là dans quarante minutes. »", 3, "pb-3 ic-2 em2",
              sets=["alex_y_va"]),
            R("« Appelez le 144, Madame Pittet. » Et raccrocher.", 4, "cc1 ic1 em-2"),
            R("« Appelez Daniel, il est juste à côté. »", 4, "ic1 em-1"),
            R("« Prenez un diurétique de plus, ça va passer. »", 5, "pb-3 cc-3 ic-1"),
        ]),
        I(2, "narr", "",
          "La régulatrice du 144 prend l'adresse, l'âge, les mots-clés : insuffisance "
          "cardiaque, essoufflement au repos, vit seule. « Une ambulance part. Rappelez-la et "
          "restez en ligne avec elle. Son fils habite à côté ? Il faudrait qu'il ouvre. » Vous "
          "rappelez Jeannine. Elle décroche à la sixième sonnerie.", [
            R("« Jeannine, l'ambulance arrive. Je reste avec vous au téléphone. J'appelle aussi "
              "Daniel, pour qu'il vienne ouvrir. D'accord ? »", 6, "ic3 cc2 em1"),
            R("« Ils arrivent. Je raccroche, à demain. »", 7, "em-2 ic-1"),
            R("« Respirez lentement, avec moi. On inspire… »", 6, "em2 er1"),
            R("« Je vous avais dit de ne pas refuser l'hôpital. »", 6, "em-3 rd-2"),
        ]),
        I(3, "narr", "",
          "Vous roulez dans la nuit. À mi-chemin, Jeannine ne répond plus au téléphone. Vous "
          "accélérez. Quand vous arrivez aux Combettes, à 23 h 50, la cuisine est éclairée. "
          "Jeannine est dans son fauteuil, les lèvres bleues, les mains agrippées aux "
          "accoudoirs.", [
            R("Appeler le 144 tout de suite, depuis la cuisine, en restant près d'elle.",
              8, "ic2 cc1 er1"),
            R("Essayer de l'allonger, pour qu'elle soit plus à l'aise.", 8, "pb-2 cc-2"),
            R("Courir réveiller Daniel.", 8, "ic1 er-1"),
            R("Lui donner un verre d'eau.", 8, "pb-1 cc-1"),
        ]),
        I(4, "jeannine", "resigned",
          "« Ah. » Un silence, puis une toux. « Oui. Bien sûr. » Elle raccroche. Vous fixez "
          "votre téléphone.", [
            R("La rappeler tout de suite, et lui proposer d'appeler le 144 à sa place, en "
              "restant en ligne avec elle.", 2, "ic2 em2 er1"),
            R("Appeler le 144 vous-même, avec son adresse.", 2, "ic3 cc1"),
            R("Attendre : elle va appeler.", 9, "ic-2 em-2"),
            R("Lui envoyer un SMS : « appelez le 144 ».", 9, "cc-1 em-2"),
        ]),
        I(5, "jeannine", "anxious",
          "« Un… de plus ? » Elle cherche le pilulier. Vous l'entendez le faire tomber, les "
          "comprimés qui roulent sur le carrelage. « Je ne les vois plus… »", [
            R("« Laissez les comprimés. J'appelle le 144 pour vous, tout de suite. Restez "
              "assise. »", 2, "ic3 cc2 er1"),
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
            R("« Vous avez raison. C'est vous, ou le 144. Pas moi. J'en parle à la Dre Golay, "
              "pour qu'on l'organise avec elle. »", 10, "pb3 ic2 rd1"),
            R("« Elle ne voulait pas vous réveiller. »", 10, "pb-1 em1"),
            R("« J'ai fait ce que j'ai pu. »", 10, "er1 pb-1"),
            R("« C'est elle qui m'a appelé·e, je n'y peux rien. »", 10, "pb-2 rd-1"),
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
            R("« J'ai fait une erreur en septembre. Je vais la lui apporter, et le lui "
              "expliquer : la nuit, c'est le 144, ou Daniel. Pas moi. »", END, "pb3 er1 ic1"),
            R("« Elle me faisait confiance. »", END, "pb-1 em1"),
            R("« Je ne pouvais pas lui refuser mon numéro. »", END, "pb-2 er-1"),
            R("« Et si je change de numéro ? »", END, "pb-1 em-1 er1"),
            R("« Je ne savais pas que c'était un problème. »", END, "pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.4 La nuit sur le carrelage — branche « Alex n'a pas donné son numéro »
# ---------------------------------------------------------------------------
_INTRO_54B = (
    "Un jeudi d'avril. Thierry appelle le cabinet à 8 h 10 : il a trouvé Jeannine par terre, "
    "dans le couloir, à côté du téléphone. Elle y était depuis 3 h du matin. Pas de "
    "fracture. La Dre Golay part la voir ; vous l'accompagnez."
)
_INTRO_54B_ALARME = (
    "Un jeudi d'avril. À 3 h 12, Jeannine est tombée dans le couloir et a appuyé sur son "
    "bracelet. La centrale a appelé Daniel, qui est arrivé en quatre minutes. Thierry l'a "
    "raconté au cabinet à 8 h, presque fier. La Dre Golay part la voir ; vous "
    "l'accompagnez."
)

S5_4B = S(5, "5.4 La nuit sur le carrelage", _INTRO_54B,
    focus=("ic", "pb", "cc"),
    slot="5.4",
    cond=when(none=["numero_donne"]),
    entries=[
        Entry(20, when(all=["alarme_posee"]), _INTRO_54B_ALARME),
    ],
    nodes=[
        I(1, "jeannine", "resigned",
          "Jeannine est dans son lit, ce qui n'arrive jamais. Un bleu violet sur la pommette. "
          "Elle a l'air minuscule. « Cinq heures. » Elle lève une main, montre cinq doigts. "
          "« Cinq heures sur le carrelage. J'ai compté les coups de la pendule. J'ai chanté "
          "toutes les chansons de l'école. » Elle sourit, de travers. « Et puis j'ai eu "
          "froid. »", [
            R("S'asseoir à côté du lit, à sa hauteur. « Cinq heures… Vous avez dû avoir très "
              "peur. »", 2, "em3 co2 rd1"),
            R("« Vous auriez dû accepter le bracelet. »", 3, "rd-2 em-2"),
            R("Prendre sa tension et son pouls, en silence.", 2, "cc1 pb-1"),
            R("« Pourquoi vous n'avez pas crié ? »", 3, "em-1 cc-1"),
            R("Rester près de la porte, pendant que la Dre Golay l'examine.", 2, "ic1 er1"),
        ]),
        I(2, "golay", "neutral",
          "La Dre Golay s'assied au bord du lit. « Jeannine. Cette nuit, on ne la recommence "
          "pas. On fait un plan, maintenant, ensemble. » Elle se tourne vers vous. « Alex, "
          "vous notez. Qui on appelle, à quelle heure, pour quoi. Et on écrit vos directives "
          "anticipées, Jeannine : ce que vous voulez, et ce que vous ne voulez pas, pour le "
          "jour où vous ne pourrez plus le dire. »", [
            R("« Je note. Madame Pittet, on commence par ce qui compte le plus pour vous ? »",
              4, "ic2 cc2 rd2"),
            R("Noter ce que dit la Dre, sans rien demander à Jeannine.", 4, "ic1 rd-1"),
            R("« Les directives anticipées, ce n'est pas un peu tôt ? »", 5, "cc-1 rd-1 pb-1"),
            R("« Je peux les remplir pour elle, si c'est plus simple. »", 5, "pb-3 rd-2"),
        ]),
        I(3, "jeannine", "cold-anger",
          "« Crier ? À trois heures du matin, dans une ferme, à deux kilomètres du village ? » "
          "Elle ferme les yeux. « Les vaches m'ont répondu. C'est déjà ça. » La Dre Golay vous "
          "jette un regard.", [
            R("« Pardon. C'était une question idiote. Ce que je voulais dire : on ne veut plus "
              "jamais que ça arrive. »", 2, "rd2 em1 er1"),
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
            R("Écrire ses mots exacts, puis les lui relire, phrase par phrase, pour qu'elle les "
              "corrige.", 6, "cc3 rd2 ic1"),
            R("Résumer : « Pas d'acharnement. »", 6, "cc-2 rd-1"),
            R("« Et le don du corps, je l'écris aussi ? »", 6, "cc1 pb-1"),
            R("« Daniel ? Vous êtes sûre ? Il n'est pas d'accord avec vous. »", 7, "rd-2 pb-2"),
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
            R("« Elle n'est pas en état. »", 4, "rd-3 pb-2"),
        ]),
        I(6, "golay", "neutral",
          "La Dre Golay relit, signe, fait signer Jeannine, d'une écriture qui part de "
          "travers. « Une copie ici, sur le frigo. Une au cabinet. Une pour Thierry. Une pour "
          "Daniel. » Elle range son stylo. « Alex, vous appelez Laura pour la lumière du "
          "couloir, et la centrale d'alarme, pour que le bracelet sonne chez Daniel et chez "
          "Thierry. » Jeannine, les yeux fermés : « Bleu, le bracelet. Pas rouge. »", [
            R("« Bleu. C'est noté. » Et appeler Laura et la centrale avant de partir.",
              8, "ic3 em1 cc1"),
            R("« Ce n'est pas mon rôle d'appeler la centrale. »", 8, "ic-2 pb1"),
            R("« Je le ferai demain. »", 8, "ic-1 cc-1"),
            R("Rire : « Même pour la couleur, vous avez des directives. »", 8, "em2 rd1"),
        ]),
        I(7, "jeannine", "neutral",
          "« Je suis sûre. » Jeannine ouvre les yeux. « Il n'est pas d'accord avec moi. Mais "
          "c'est mon fils. Il saura ce que je veux, parce que je le lui aurai dit. Et parce que "
          "vous l'aurez écrit. »", [go(6)]),
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
            R("« Et Daniel, comment il allait ? »", 2, "em2 cc1"),
            R("S'asseoir près d'elle, en silence.", 2, "em2 co1"),
        ]),
        I(21, "jeannine", "happy",
          "« Ne faites pas le malin. » Elle rit, puis grimace : la pommette. « La laisse a "
          "servi. Voilà. Vous êtes content·e ? »", [go(2)]),
    ],
)

# ---------------------------------------------------------------------------
# 5.5 L'atelier
# ---------------------------------------------------------------------------
_INTRO_55 = (
    "Mi-avril. Atelier de design de recherche, salle de séminaire. Par groupes, il faut "
    "construire un protocole d'étude en trois semaines. Le Dr Ibarra anime. Maëlle a déjà "
    "une idée, et elle est enthousiaste."
)

S5_5 = S(6, "5.5 L'atelier", _INTRO_55,
    focus=("ic", "pb", "em"),
    entries=[
        Entry(20, when(all=["noah_seul"]), _INTRO_55),
    ],
    nodes=[
        I(1, "noah", "neutral",
          "Noah est revenu lundi. Il a maigri, il a les cheveux plus courts, et il ne regarde "
          "plus son téléphone. Il s'assied à côté de vous. « Salut. » Maëlle fait comme si de "
          "rien n'était, trop fort. Yasmine lui pousse un café. Léo lui a gardé des fiches.", [
            R("« Content·e que tu sois là. » Et laisser Noah décider de ce qu'il veut dire, ou "
              "pas.", 2, "em2 rd2 pb1"),
            R("« Alors, c'était comment, l'hôpital psychiatrique ? »", 3, "pb-3 rd-3"),
            R("« Tu as l'air mieux ! »", 2, "em1 cc-1"),
            R("Lui faire de la place, et lui montrer où on en est du protocole.",
              2, "ic2 em1"),
            R("L'ignorer, pour ne pas le mettre mal à l'aise.", 2, "em-2 ic-1"),
        ]),
        I(2, "maelle", "happy",
          "Maëlle se lève. « Mon idée : une enquête sur ce que les gens pensent du don du "
          "corps. Pourquoi ils donnent, pourquoi ils refusent. On fait des entretiens avec des "
          "donneurs vivants, et avec leurs familles. » Elle vous regarde. « Toi, tu vas dans un "
          "cabinet de village. Tu dois bien en connaître, des vieux qui ont signé ? »", [
            R("« Ce que je vois au cabinet est couvert par le secret : je ne peux donner aucun "
              "nom, ni même dire si j'en connais. Mais l'idée est bonne : on peut recruter par "
              "l'institut d'anatomie, avec un consentement en bonne et due forme. »",
              4, "pb3 cc2 ic2 rd2"),
            R("« Il y a une patiente qui… Non, je ne peux pas. »", 5, "pb-2 cc-1"),
            R("« Oui, j'en connais une. Elle serait parfaite. »", 5, "pb-3 rd-2"),
            R("« Je ne veux pas en parler. »", 4, "pb1 ic-1 cc-1"),
            R("« Les familles de donneurs, c'est délicat. Il faudrait passer par une "
              "commission d'éthique. »", 4, "cc2 ic1 pb1"),
        ]),
        I(3, "noah", "cold-anger",
          "Noah vous regarde. Toute la table s'est tue. « Fermé. Ça s'appelle un service "
          "fermé. » Il se lève, prend son sac. Le Dr Ibarra se lève aussi, et le suit dans le "
          "couloir.", [
            R("Le suivre, et s'excuser : « C'était nul, et déplacé. Pardon. »",
              2, "rd2 em2 er1"),
            R("« Je demandais juste… »", 2, "er-1 rd-1"),
            R("Rester assis·e, rouge.", 2, "er-1"),
            R("« Il est susceptible, depuis. »", 2, "rd-3 em-2"),
        ]),
        I(4, "ibarra", "neutral",
          "Le Dr Ibarra, qui écoutait depuis le fond de la salle, s'approche. « Bonne "
          "question, ça. Au cabinet, vous êtes soignant·e. Ici, vous êtes chercheur·euse. Ce "
          "sont deux rôles, et les gens qui vous ont parlé en tant que soignant·e ne vous ont "
          "pas donné leur accord pour devenir des sujets d'étude. » Il tapote le protocole. "
          "« Écrivez-le dans la section éthique. Mot pour mot. »", [
            R("Écrire la phrase dans le protocole, et proposer d'ajouter un formulaire de "
              "consentement.", 6, "ic2 pb2 cc1"),
            R("« C'est évident. »", 6, "ic-1 er-1"),
            R("« Et si la personne est d'accord ? »", 6, "cc2 pb1"),
            R("Laisser Maëlle l'écrire.", 6, "ic1"),
        ]),
        I(5, "ibarra", "cold-anger",
          "Le Dr Ibarra a entendu. Il s'approche. « Alex. Ce que vous voyez au cabinet ne sort "
          "pas du cabinet. Ni les noms, ni les détails, ni même l'existence d'« une patiente "
          "qui… ». Dans un village, une demi-phrase suffit à reconnaître quelqu'un. » Maëlle "
          "rougit. « Pardon, c'est moi qui ai demandé. »", [
            R("« C'est moi qui ai parlé. Vous avez raison. Je n'ajouterai rien. »",
              4, "pb3 er1 ic1"),
            R("« Je n'ai donné aucun nom. »", 4, "pb-2 er-1"),
            R("« C'est Maëlle qui insistait. »", 4, "ic-2 pb-1"),
            R("Se taire.", 4, "er1"),
        ]),
        I(6, "noah", "vulnerable",
          "À la pause, Noah reste à côté de vous, à la fenêtre. « Tu sais ce qui est bizarre ? "
          "À l'hôpital, la psy m'a demandé qui j'avais appelé, cette nuit-là. J'ai dit ton nom. "
          "Elle a dit : « Gardez cette personne. » » Il hausse les épaules. « Alors je te "
          "garde. Mais je ne veux pas que tu sois mon infirmier. J'ai une psy, maintenant. Le "
          "jeudi. »", [
            R("« Ça me va. Moi, je suis juste ton ami·e. La psy, c'est son métier. »",
              7, "pb3 em2"),
            R("« Tu peux m'appeler n'importe quand, jour et nuit. »", 7, "pb-2 em1"),
            R("« Et ton père ? »", 8, "em1 cc1"),
            R("« Tant mieux, parce que moi, je n'en peux plus de tout porter. »",
              7, "er-1 em-2"),
            R("Lui serrer l'épaule, sans rien dire.", 7, "em2 co1"),
        ]),
        I(7, "ibarra", "neutral",
          "Fin de l'atelier. Le protocole tient en quatre pages. Dans la section éthique, une "
          "phrase écrite en gras. Le Dr Ibarra relit, et rend la feuille. « Bon travail. » En "
          "sortant, il s'arrête près de la table. « La meilleure étude que vous ferez cette "
          "année, c'est celle-là : comment on prend soin les uns des autres sans se prendre "
          "pour le médecin des autres. »"),
        I(8, "noah", "neutral",
          "« Mon père est venu à l'hôpital. Il s'est assis, il n'a rien dit pendant une heure. "
          "Puis il a dit : « Moi aussi, en deuxième année, j'ai failli arrêter. » » Noah rit. "
          "« Vingt ans qu'il me raconte son sandwich au jambon à côté du cadavre. Il ne m'avait "
          "jamais dit ça. »", [
            R("« Peut-être qu'il avait besoin que tu t'arrêtes, pour pouvoir le dire. »",
              7, "em2 co1 cc1"),
            R("« Il aurait pu le dire plus tôt. »", 7, "em-1 rd-1"),
            R("Sourire.", 7, "em1"),
            R("« Les pères, hein. »", 7, "em1 er1"),
        ]),
        I(20, "narr", "",
          "La chaise de Noah est vide. La semaine dernière, il a écrit au groupe : « j'arrête "
          "médecine. je pars bosser chez mon oncle à Neuchâtel, dans une menuiserie. ça va "
          "mieux. merci pour tout ». Maëlle a mis un cœur. Yasmine n'a rien répondu. Léo a "
          "écrit trois paragraphes. Le Dr Ibarra a laissé la chaise à sa place.", [
            R("Proposer au groupe d'écrire à Noah ensemble, après l'atelier, puis se mettre au "
              "travail.", 21, "ic2 em2"),
            R("Glisser à Yasmine, à voix basse : « C'est ma faute. Cette nuit-là, je me suis "
              "rendormi·e. »", 22, "er1 cc1"),
            R("Retirer la chaise.", 21, "er-1 rd-1"),
            R("« Au moins, il va mieux. »", 21, "er1 em1"),
            R("Écrire à Noah pendant l'atelier : « tu nous manques ».", 21, "em2 ic-1"),
        ]),
        I(21, "maelle", "neutral",
          "Maëlle se lève, moins enthousiaste qu'elle ne voudrait. « Mon idée : une enquête "
          "sur ce que les gens pensent du don du corps. Pourquoi ils donnent, pourquoi ils "
          "refusent. Des entretiens avec des donneurs vivants, et avec leurs familles. » Elle "
          "vous regarde. « Toi, tu vas dans un cabinet de village. Tu dois bien en connaître, "
          "des vieux qui ont signé ? »", [
            R("« Ce que je vois au cabinet est couvert par le secret : je ne peux donner aucun "
              "nom, ni même dire si j'en connais. Mais l'idée est bonne : on peut recruter par "
              "l'institut d'anatomie, avec un consentement en bonne et due forme. »",
              24, "pb3 cc2 ic2 rd2"),
            R("« Il y a une patiente qui… Non, je ne peux pas. »", 25, "pb-2 cc-1"),
            R("« Oui, j'en connais une. Elle serait parfaite. »", 25, "pb-3 rd-2"),
            R("« Je ne veux pas en parler. »", 24, "pb1 ic-1 cc-1"),
            R("« Les familles de donneurs, c'est délicat. Il faudrait passer par une "
              "commission d'éthique. »", 24, "cc2 ic1 pb1"),
        ]),
        I(22, "yasmine", "neutral",
          "Yasmine ne vous regarde pas : elle regarde la chaise. « Cette nuit-là, c'est à toi "
          "qu'il a écrit. Ça veut dire que tu comptais. Et tu as appris quelque chose que tu "
          "n'oublieras jamais. » Elle vous pousse un café. « C'est ça, le métier. On porte, et "
          "on apprend. Tu ne t'endormiras plus jamais sur un message comme celui-là. »", [
            R("« Non. Plus jamais. » Et se mettre au travail.", 21, "er2 ic1 pb1"),
            R("« Facile à dire. »", 21, "er-1 ic-1"),
            R("Hocher la tête, la gorge serrée.", 21, "er1"),
            R("« Je vais aller voir quelqu'un. Un psy. Pour moi. »", 21, "er3 ic1"),
        ]),
        I(23, "leo", "happy",
          "À la pause, Léo vous montre son téléphone : les trois paragraphes qu'il a écrits à "
          "Noah, en français, sans une faute. « Il m'a répondu. Il dit que la menuiserie, c'est "
          "comme l'anatomie, sauf que les morceaux ne te regardent pas. » Léo sourit, un peu. "
          "« Je crois qu'il va bien. Vraiment. »", [
            R("« Merci de lui avoir écrit. Tu peux lui dire que je pense à lui ? Ou je le lui "
              "dirai moi-même. »", 7, "em2 ic2"),
            R("« Il aurait pu rester. »", 7, "em-2"),
            R("Sourire.", 7, "em1"),
            R("« Tu es devenu bon en français. »", 7, "rd1 em1"),
        ]),
        I(24, "ibarra", "neutral",
          "Le Dr Ibarra, qui écoutait depuis le fond de la salle, s'approche. « Au cabinet, "
          "vous êtes soignant·e. Ici, vous êtes chercheur·euse. Deux rôles. Les gens qui vous "
          "ont parlé en tant que soignant·e ne vous ont pas donné leur accord pour devenir des "
          "sujets d'étude. » Il tapote le protocole. « Écrivez-le dans la section éthique. Mot "
          "pour mot. »", [
            R("Écrire la phrase dans le protocole, et proposer d'ajouter un formulaire de "
              "consentement.", 23, "ic2 pb2 cc1"),
            R("« C'est évident. »", 23, "ic-1 er-1"),
            R("« Et si la personne est d'accord ? »", 23, "cc2 pb1"),
            R("Laisser Maëlle l'écrire.", 23, "ic1"),
        ]),
        I(25, "ibarra", "cold-anger",
          "Le Dr Ibarra a entendu. « Alex. Ce que vous voyez au cabinet ne sort pas du "
          "cabinet. Ni les noms, ni les détails, ni même l'existence d'« une patiente qui… ». "
          "Dans un village, une demi-phrase suffit à reconnaître quelqu'un. » Maëlle rougit. "
          "« Pardon, c'est moi qui ai demandé. »", [
            R("« C'est moi qui ai parlé. Vous avez raison. Je n'ajouterai rien. »",
              24, "pb3 er1 ic1"),
            R("« Je n'ai donné aucun nom. »", 24, "pb-2 er-1"),
            R("« C'est Maëlle qui insistait. »", 24, "ic-2 pb-1"),
            R("Se taire.", 24, "er1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.6 Le cabinet ferme
# ---------------------------------------------------------------------------
_INTRO_56 = (
    "Fin avril. Jeudi, 18 h 30. Le dernier patient est parti. La Dre Golay ferme elle-même "
    "les volets, comme toujours. Puis elle demande à Sandra et à vous de vous asseoir dans la "
    "salle d'attente vide."
)

S5_6 = S(7, "5.6 Le cabinet ferme", _INTRO_56,
    focus=("er", "pb", "ic"),
    entries=[
        Entry(20, when(all=["esquive_homonyme"]), _INTRO_56),
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
            R("« Et Sandra, qu'est-ce qu'elle va faire ? »", 4, "ic2 em2"),
            R("« Vous avez essayé de passer une annonce ? »", 2, "ic-1 er-1"),
            R("« Moi, je reviendrai peut-être, dans dix ans. »", 5, "er1 pb-1"),
        ]),
        I(2, "sandra", "sad",
          "Sandra se mouche. « Quatorze ans. J'ai commencé ici à vingt-quatre ans, avec un bébé "
          "dans un porte-bébé derrière le comptoir. » Elle rit à travers ses larmes. « Les "
          "patients, je les connais par leur date de naissance. Tu te rends compte ? Ça ne "
          "servira plus à rien. »", [
            R("« Ça a servi. Moi, c'est ici que j'ai appris l'importance d'une date de "
              "naissance. Grâce à toi. »", 6, "ic3 em2"),
            R("« Tu retrouveras facilement un poste. »", 6, "em-1 cc-1"),
            R("La prendre dans vos bras.", 6, "em2 co2"),
            R("« C'est la vie. »", 6, "em-2 co-1"),
            R("Se taire, et lui tendre un mouchoir.", 6, "em1 co1"),
        ]),
        I(3, "golay", "neutral",
          "La Dre Golay vous regarde, sans colère. « Jeannine le sait depuis Noël. C'est elle "
          "qui m'a dit de ne pas chercher un remplaçant pour elle : « Je partirai avant vous, "
          "Isabelle. » » Elle soupire. « Vous croyez que je ne me le suis pas dit cent "
          "fois ? »", [
            R("« Pardon. C'était injuste. Je pensais à elle, pas à vous. »", 2, "rd2 er2 em1"),
            R("« Quand même. »", 2, "er-1 rd-1"),
            R("Baisser les yeux.", 2, "er1"),
            R("« Vous auriez pu chercher davantage. »", 2, "rd-3 er-1"),
        ]),
        I(4, "sandra", "sad",
          "Sandra s'essuie les yeux. « Moi ? Le cabinet de groupe d'Orbe m'a proposé un poste. "
          "Au téléphone. Pour les rendez-vous de quarante médecins. » Elle sourit, de travers. "
          "« Je ne connaîtrai plus personne par sa date de naissance. »", [
            R("« Ils ont de la chance. Et tu leur apprendras la règle des homonymes. »",
              6, "ic2 em2"),
            R("« C'est bien payé, au moins ? »", 6, "em-1"),
            R("« Tu vas manquer aux patients. »", 6, "em2"),
            R("« Au moins, tu auras moins de travail. »", 6, "em-2 rd-1"),
        ]),
        I(5, "golay", "neutral",
          "La Dre Golay sourit à moitié. « Dans dix ans, il n'y aura plus de cabinet à "
          "Montchéry. Il y aura un centre de santé à Orbe, avec des infirmières praticiennes, "
          "des assistantes, des médecins à temps partiel. Ce sera peut-être mieux. » Elle vous "
          "regarde. « Mais si vous revenez, ne revenez pas pour moi. Revenez pour les "
          "Jeannine. »", [
            R("« Les Jeannine… J'en ai rencontré une. Ça suffit pour savoir que ce métier "
              "existe. »", 6, "er2 rd1 ic1"),
            R("« Je ne sais pas encore ce que je ferai. Mais je saurai pourquoi. »",
              6, "er2 pb1"),
            R("« Promis. »", 6, "pb-1 er1"),
            R("« La médecine de famille, ce n'est pas pour moi, je crois. »", 6, "er1 cc1"),
            R("« Les infirmières praticiennes, ce n'est pas vraiment de la médecine. »",
              6, "ic-3 rd-2"),
        ]),
        I(6, "golay", "melancholic",
          "La Dre Golay se lève, prend ses clés. Sur le pas de la porte, elle se retourne. "
          "« J'accueille des étudiants depuis vingt ans. Vous êtes le dernier, ou la "
          "dernière. » Un temps. « Tu reviendras, toi ? » C'est la première fois qu'elle vous "
          "tutoie.", [
            R("« Je ne sais pas. Mais je n'oublierai jamais ce cabinet. Ni ce que vous m'avez "
              "appris, qui n'est pas dans les livres. »", END, "er2 rd2 cc1"),
            R("« Oui ! Promis. »", END, "pb-2 er1"),
            R("« Je veux faire de la chirurgie. »", END, "cc1"),
            R("Lui serrer la main, longtemps, sans répondre.", END, "rd2 em1"),
            R("« Sûrement pas. C'est trop dur, la campagne. »", END, "rd-2 em-1"),
        ]),
        I(20, "sandra", "cold-anger",
          "Sandra ne vous adresse plus la parole depuis le samedi du Café de la Gare. Ce soir, "
          "elle s'assied à l'autre bout de la salle d'attente. La Dre Golay le remarque, et "
          "attend.", [
            R("Aller s'asseoir à côté de Sandra : « Avant que la Dre commence : en octobre, je "
              "t'ai laissée porter mon erreur. Je te dois des excuses depuis six mois. »",
              1, "pb3 rd2 ic2 er1"),
            R("Ne rien dire, et attendre que la Dre parle.", 1, "er-1 ic-1"),
            R("« Il se passe quoi ? »", 1, "cc1"),
            R("Regarder Sandra, puis détourner les yeux.", 1, "ic-1 er-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.7 Le balcon — histoire annexe (si Alex a promis de revenir voir son père)
# ---------------------------------------------------------------------------
S5_7 = S(8, "5.7 Le balcon",
    "Fin avril, un samedi. Chez vos parents. Votre père a terminé sa réadaptation "
    "cardiaque : sept kilos de moins, une heure de marche par jour. Depuis la cuisine, votre "
    "mère vous fait signe de regarder le balcon.",
    focus=("em", "pb", "rd"),
    slot="5.7",
    cond=when(all=["papa_promesse"]),
    annex=True,
    nodes=[
        I(1, "philippe", "ashamed",
          "Sur le balcon, votre père, en pantoufles, une cigarette entre les doigts. Il la "
          "cache derrière son dos en vous voyant, comme un ado. « C'est la première. Depuis "
          "Noël. » Elle est à moitié fumée. Il y a trois mégots dans le pot de géraniums.", [
            R("« Papa. » Et s'accouder à côté de lui sur la balustrade, sans rien ajouter, pour "
              "l'instant.", 2, "em2 rd2"),
            R("« Tu veux mourir, c'est ça ? »", 3, "em-3 rd-2"),
            R("Lui prendre la cigarette des doigts, et l'écraser.", 3, "rd-2 pb-1"),
            R("« Trois mégots, papa. Pas une. »", 3, "cc2 em-1"),
            R("« Je ne dirai rien à maman. »", 4, "pb-2 cc-1"),
        ]),
        I(2, "philippe", "neutral",
          "Il regarde la ville. « Ta mère me parle de cigarettes, la cardiologue me parle de "
          "cigarettes, la physio me parle de cigarettes. » Il tire une bouffée. « Toi, tu vas "
          "me parler de quoi ? »", [
            R("« De la fac, comme promis. Et une fois, une seule, de cigarettes. Puis plus "
              "jamais. »", 5, "em2 cc2 pb1"),
            R("« Du fait que tu vas mourir, si tu continues. »", 3, "em-2 cc1 rd-1"),
            R("« De rien. Je ne suis pas ton médecin. »", 5, "pb2 em-1"),
            R("« Tu as peur, papa ? »", 6, "em3"),
        ]),
        I(3, "philippe", "angry",
          "Votre père écrase sa cigarette avec rage. « Arrête de me parler comme un médecin. "
          "Tu n'es pas mon médecin. Tu es mon gamin. » Il rentre et claque la porte-fenêtre. "
          "Votre mère vous regarde à travers la vitre, les bras croisés.", [
            R("Le rejoindre au salon : « Tu as raison. Je ne suis pas ton médecin. Je suis ton "
              "enfant, et j'ai eu peur de te perdre à Noël. C'est tout. »", 6, "em3 er2 rd1"),
            R("Rester sur le balcon.", END, "er-1 em-1"),
            R("« Fais ce que tu veux, c'est ta vie. »", END, "em-3 co-2"),
            R("Aller dire à votre mère de lui confisquer ses cigarettes.", END, "pb-1 rd-2"),
        ]),
        I(4, "philippe", "happy",
          "« Merci. » Il sourit, soulagé, et en allume une autre. « T'es le seul qui me "
          "comprend. » Derrière la vitre, votre mère vous regarde. Elle a vu la deuxième "
          "cigarette.", [
            R("« Non, papa. Je ne vais pas te couvrir. Je ne le dirai pas à maman à ta place, "
              "mais je te demande de le lui dire toi-même. Et d'en parler à ta "
              "cardiologue. »", 5, "pb3 cc2 em1"),
            R("Hausser les épaules.", END, "pb-1 em-1"),
            R("« Juste celle-là, hein. »", END, "pb-2 cc-1"),
            R("Rentrer, et faire comme si de rien n'était devant votre mère.", END, "pb-2 ic-1"),
        ]),
        I(5, "philippe", "vulnerable",
          "Il vous écoute parler de la fac : la salle de dissection, Madame 14, le cœur aux "
          "trois pontages. Il ne dit rien. À la fin, il regarde la cigarette éteinte dans sa "
          "main. « Trois pontages. Et elle a tenu combien de temps, ta dame ? — Longtemps, je "
          "crois. » Il hoche la tête. Il jette le paquet dans le pot de géraniums. « Ne le dis "
          "pas à ta mère. Je veux lui faire la surprise. »", [
            R("« Promis. Et si tu reprends, tu as le droit de me le dire. Je ne ferai pas le "
              "médecin. »", END, "em2 rd2 pb1"),
            R("« Tu vas tenir, cette fois ? »", END, "cc1 em-1"),
            R("Le serrer dans vos bras.", END, "em2 co2"),
            R("« Je vérifierai le pot de géraniums. »", END, "rd-2 em-1"),
        ]),
        I(6, "philippe", "vulnerable",
          "« Peur ? » Il rit, puis non. « Tous les soirs. Je me couche, et je me demande si je "
          "vais me réveiller. La cigarette, c'est le seul moment où je n'y pense pas. » Il la "
          "regarde se consumer. « C'est con, hein ? »", [
            R("« Non. C'est humain. Et cette peur-là, tu peux en parler à ta cardiologue, ou à "
              "la psychologue de la réadaptation : ils ont l'habitude. Tu n'es pas obligé de la "
              "fumer. »", 5, "em3 cc2 ic1"),
            R("« Oui, c'est con. »", 3, "em-3 rd-1"),
            R("Lui prendre la main.", 5, "em2 co2"),
            R("« Tout le monde a peur. »", 5, "em-1 cc-1"),
        ]),
    ],
)

CH5 = C(5, "Ce que le village sait",
    situation=(
        "Avril. À la fac, la digestion, le métabolisme et le rein, et un atelier de "
        "recherche. Aux Combettes, Jeannine a perdu six kilos, et la Dre Golay réunit la "
        "famille autour de la toile cirée. Dans la grange, Océane a un secret. Et le cabinet "
        "de Montchéry va fermer."
    ),
    objectives=(
        "repérer une dénutrition sans humilier ni infantiliser ; rester à sa place dans une "
        "réunion de famille, et rapporter fidèlement les mots d'une patiente quand elle le "
        "demande ; respecter le secret confié par une mineure capable de discernement et "
        "l'orienter sans décider à sa place ; ne pas devenir le premier recours d'une "
        "patiente (numéro personnel, déplacements de nuit) ; aider à rédiger des directives "
        "anticipées avec les mots de la patiente ; séparer le rôle de soignant·e et celui de "
        "chercheur·euse ; accueillir le retour d'un camarade sans devenir son soignant ; "
        "reconnaître le travail de l'assistante médicale."
    ),
    anchoring=(
        "UNIL BMed2.5 (besoins nutritionnels), BMed2.6 (filtration glomérulaire, "
        "physiopathologie), BMed2.7 (médecin de famille, équipe interprofessionnelle) et "
        "BMed2.9 (ateliers de design de recherche) · UNIGE Nutrition, digestion et "
        "métabolisme, Excrétion et homéostasie, dimensions communautaires (éthique), stage "
        "IMFE · UZH Humanbiologie I (Verdauung und Ernährung), Humanbiologie II (Niere, "
        "Methodik medizinischer Forschung)."
    ),
    focus=("ic", "rd", "pb", "em"),
    start_choice=StartChoice(
        unless_any=["noah_aide", "noah_seul"],
        question=(
            "Ce chapitre fait suite à la nuit de mars où Noah a écrit à Alex (chapitre 4), "
            "que vous n'avez pas jouée sur cet appareil. Que s'est-il passé cette nuit-là ?"
        ),
        options=[
            ("Alex ne l'a pas laissé seul : Noah a passé quelques jours à l'hôpital, et il "
             "revient à la fac.", ["noah_aide"]),
            ("Alex s'est rendormi·e : Noah a été retrouvé au matin, et il a quitté la "
             "médecine.", ["noah_seul"]),
        ],
    ),
    scenes=[S5_1, S5_2, S5_3, S5_4A, S5_4B, S5_5, S5_6, S5_7],
)
