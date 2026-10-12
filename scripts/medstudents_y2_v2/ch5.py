"""Chapitre 5 — Le corps donné (mai-juin, puis septembre).

Six scènes jouées, sept écrites :
  5.1 La table de la cuisine · 5.2 La grange
  5.3 La dernière visite (la veille de l'examen, puis l'examen et l'appel de Sandra)
  5.4 branche parallèle : « Le fourgon » (la famille s'est apaisée)
      ou « Vous ne l'emmènerez pas »
  5.5 La lettre (et Noah, selon la nuit de mars)
  5.6 La cérémonie (puis le dernier jour du cabinet, en septembre)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, StartChoice, go, when

# ---------------------------------------------------------------------------
# 5.1 La table de la cuisine
# ---------------------------------------------------------------------------
_INTRO_51 = (
    "Début mai, mardi, 18 h. La cuisine des Combettes. Autour de la toile cirée : Jeannine, "
    "dans son fauteuil ; la Dre Golay ; Thierry ; Daniel, debout près de la porte, la "
    "casquette dans les mains ; Océane, assise sur le plan de travail. Et vous, près du "
    "fourneau. Daniel ne sait presque rien. La Dre Golay ouvre la réunion."
)
_INTRO_51_MALADIE = (
    "Début mai, mardi, 18 h. La cuisine des Combettes. Autour de la toile cirée : Jeannine, "
    "dans son fauteuil ; la Dre Golay ; Thierry ; Daniel, debout près de la porte, la "
    "casquette dans les mains ; Océane, assise sur le plan de travail. Et vous, près du "
    "fourneau. Daniel sait, pour les reins et le cœur. Il ne sait pas tout. La Dre Golay "
    "ouvre la réunion."
)
_INTRO_51_DON = (
    "Début mai, mardi, 18 h. La cuisine des Combettes. Autour de la toile cirée : Jeannine, "
    "dans son fauteuil ; la Dre Golay ; Thierry ; Daniel, debout près de la porte, la "
    "casquette dans les mains ; Océane, assise sur le plan de travail. Et vous, près du "
    "fourneau. Daniel sait tout, y compris pour le don du corps. Il ne l'a jamais accepté."
)

S5_1 = S(1, "5.1 La table de la cuisine", _INTRO_51,
    focus=("ic", "rd", "pb", "co"),
    entries=[
        Entry(30, when(any=["revele_a_daniel", "noel_annonce"]), _INTRO_51_DON),
        Entry(1, when(any=["info_lachee", "erreur_homonyme", "daniel_sait"]),
              _INTRO_51_MALADIE),
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
          "place en juin. Et la dialyse, à Yverdon, il y a un transport. On peut "
          "s'organiser. »", [
            R("Se taire : ce n'est pas votre réunion.",
              2, "pb2 rd1 ic1 er1"),
            R("« Votre mère a le droit de refuser la dialyse, Monsieur Pittet : c'est la loi, "
              "une personne capable de discernement décide seule de ses traitements. »",
              3, "rd1 pb-2 em-2"),
            R("Regarder Jeannine.", 2, "rd2 em1 co1"),
            R("« Une place en EMS en juin, c'est une chance. »", 3, "rd-2 pb-2"),
            R("Noter ce que dit chacun, pour le compte rendu de la Dre Golay.", 2, "ic1 cc1"),
        ]),
        I(2, "jeannine", "neutral",
          "Jeannine laisse Daniel finir. Puis : « Daniel. Assieds-toi. » Il ne s'assied pas. "
          "« Pas d'EMS. Pas de machine. Je veux mourir ici, dans ma cuisine, avec la fenêtre "
          "ouverte. » Elle reprend son souffle. « Et il y a autre chose. Après. Mon corps, je "
          "l'ai donné à la faculté de médecine. Pour les étudiants. » Daniel blêmit. Océane "
          "retient son souffle. Jeannine se tourne vers vous. « Dites-leur, vous. Ce que je "
          "vous ai dit en septembre. Pourquoi. »", [
            R("« Ce n'est pas à moi de parler à votre place. Mais si vous voulez, je répète vos "
              "mots, et vous me corrigez. »", 4, "pb2 rd2 cc2"),
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
            R("« Vous avez raison. Pardon. »", 2, "rd2 pb2 er1"),
            R("« Je suis là pour votre mère. »", 6, "pb-1 rd-1 ic-1"),
            R("Se taire, rouge.", 2, "er1"),
            R("« Je connais le droit, monsieur : votre mère est capable de discernement, et "
              "personne ne peut l'obliger à aller en EMS ou à faire une dialyse. »",
              6, "rd-3 pb-2"),
        ]),
        I(4, "daniel", "cold-anger",
          "Daniel regarde sa mère. Sa voix est très basse. « En morceaux. Dans une cave, en "
          "ville. Avec des gamins comme lui qui rigolent. » Il vous désigne du menton. « Je "
          "sais comment ils sont. J'ai vu des trucs. Des photos, sur internet. » Océane "
          "descend du plan de travail.", [
            R("« Vous avez raison d'avoir peur de ça. Il y a des étudiant·e·s qui font des "
              "erreurs — j'en ai vu, j'en ai fait. Mais les donneurs ne sont jamais seuls : il "
              "y a des règles, et une cérémonie pour les remercier. »", 7, "cc3 rd2 er1 pb1"),
            R("« Personne ne rigole, en dissection. »", 6, "cc-2 pb-1"),
            R("Se taire.", 7, "er-1"),
            R("« C'est la décision de votre mère, pas la vôtre. »", 6, "rd1 em-3 pb-1"),
            R("Laisser la Dre Golay répondre.", 7, "ic2 pb2"),
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
            R("Rester près de Jeannine et d'Océane.",
              9, "pb2 em2 co2", sets=["famille_dechiree"]),
            R("Courir après lui dans la cour.", 10, "pb-2 em1"),
            R("« Il va revenir. Il a besoin de temps. »", 9, "cc-1 em1",
              sets=["famille_dechiree"]),
            R("« C'est ma faute, je n'aurais pas dû parler. »", 9, "er-2",
              sets=["famille_dechiree"]),
            R("« Il est toujours comme ça, votre fils ? Il ne peut pas écouter sa mère cinq "
              "minutes sans claquer une porte ? »", 9, "rd-2 em-2 co-1",
              sets=["famille_dechiree"]),
        ]),
        I(7, "daniel", "sad",
          "Daniel s'assied enfin, sur la chaise la plus proche de la porte. Long silence. "
          "Puis, à sa mère, sans vous regarder : « Pourquoi ? Pourquoi tu veux qu'ils "
          "t'emmènent, là-bas ? » Jeannine ouvre la bouche. Rien ne sort. Elle vous regarde. "
          "La Dre Golay aussi.", [
            R("« Prenez votre temps, Madame Pittet. »",
              8, "pb2 rd2 em1 co1"),
            R("« Elle avait peur de votre réaction, à cause de votre père, et de l'heure que "
              "vous avez passée dans le talus. »", 6, "pb-3 rd-3 em-1"),
            R("« Elle voulait vous protéger. »", 8, "pb-1 em1"),
            R("Se lever pour sortir, et laisser la famille entre elle.", 8, "rd1 pb2"),
            R("Fixer la table.", 8, "er-1"),
        ]),
        I(8, "jeannine", "melancholic",
          "Jeannine tend la main vers son fils, par-dessus la toile cirée. « Parce que j'ai "
          "passé ma vie à aider les gens à arriver. Je veux aider ceux qui soigneront les gens "
          "qui partent. » Un temps. « Et parce que tu as tenu ton père une heure dans le talus. "
          "Je ne voulais pas que tu aies à t'occuper de mon corps, à moi. » Daniel baisse la "
          "tête. Ses épaules tremblent. Au bout d'un long moment, il prend la main de sa mère. "
          "« Je ne viendrai pas à la cérémonie. » Un temps. « Mais je ne t'empêcherai pas. »", [
            R("Rester immobile, en silence.", 11, "rd3 co2 er1", sets=["famille_apaisee"]),
            R("Sortir sans bruit dans la cour.", 11, "rd2 pb2", sets=["famille_apaisee"]),
            R("« Vous voyez, ce n'était pas si difficile. »", 11, "rd-3 em-2",
              sets=["famille_apaisee"]),
            R("Prendre en photo les deux mains sur la toile cirée, discrètement, pour "
              "l'envoyer à Océane plus tard : elle voudra s'en souvenir.", 11,
              "rd-3 pb-3", sets=["famille_apaisee"]),
            R("Pleurer, et devoir sortir.", 11, "er-1 co1", sets=["famille_apaisee"]),
        ]),
        I(9, "golay", "resigned",
          "La Dre Golay attend que le bruit du tracteur se soit éteint. « Ça ne s'arrête pas "
          "ce soir, Jeannine. Il reviendra demain matin, pour les bêtes. Et on "
          "recommencera. » Jeannine ne répond pas. Océane s'assied par terre, la tête contre "
          "le genou de sa grand-mère.", [go(12)]),
        I(10, "daniel", "cold-anger",
          "Daniel est dans la cour, la main sur le capot du tracteur. Il ne se retourne pas. "
          "« Retournez à l'intérieur. » Sa voix se casse. « Vous n'êtes pas de la famille. »", [
            R("« Vous avez raison. » Et y retourner.", 9, "pb3 rd1",
              sets=["famille_dechiree"]),
            R("« Votre mère a besoin de vous, maintenant. »", 9, "pb-2 em1",
              sets=["famille_dechiree"]),
            R("Poser une main sur son épaule.", 9, "pb-3 em1", sets=["famille_dechiree"]),
            R("« Je comprends ce que vous ressentez : moi aussi, à Noël, j'ai cru perdre mon "
              "père, et je n'ai pas su quoi faire. »", 9, "pb-2 em-1",
              sets=["famille_dechiree"]),
        ]),
        I(11, "narr", "",
          "La Dre Golay range ses papiers sans bruit. Thierry fait du café. Océane s'est "
          "assise par terre, la tête contre le genou de sa grand-mère. Daniel n'a pas lâché la "
          "main de sa mère. Dehors, il fait nuit. Personne ne parle plus de l'EMS d'Orbe.",
          [go(12)]),
        I(12, "golay", "neutral",
          "Dans la cour, la Dre Golay ouvre sa portière, puis se ravise. « Vous étiez à votre "
          "place, ce soir ? » Elle ne vous laisse pas le temps de répondre. « Qu'est-ce qui a "
          "été le plus dur, pour vous ? »", [
            R("« Me taire quand Jeannine m'a demandé de parler à sa place. »",
              END, "er2 pb2 cc1"),
            R("« Rien. C'était leur réunion. »", END, "er-1 cc-1"),
            R("« Daniel. J'avais envie de lui expliquer qu'il avait tort, qu'il allait le "
              "regretter, et qu'il devait écouter sa mère au lieu de penser à lui. »",
              END, "er1 pb-2 rd-1"),
            R("« Je ne sais pas. »", END, "er-1"),
            R("« Océane. Elle ne disait rien, et je voyais bien qu'elle avait quelque chose à "
              "dire. »", END, "em2 co1 er1"),
        ]),
        I(30, "daniel", "cold-anger",
          "Daniel ne s'assied pas. Avant même que la Dre Golay ait ouvert la bouche : « Si on "
          "est là pour parler de la cave, je m'en vais. » Jeannine soupire. La Dre Golay, "
          "calmement : « On est là pour parler de votre mère. De tout. »", [
            R("Rester en retrait, et laisser la Dre Golay mener.", 31, "pb2 rd1 ic1"),
            R("« Ce n'est pas une cave, monsieur. C'est un institut, avec des règles. »", 32, "pb-2 rd-1"),
            R("Regarder Jeannine.", 31, "rd2 em1"),
            R("« J'étais en salle de dissection lundi. Je peux vous raconter comment ça se "
              "passe, concrètement, si vous voulez : les tables, les draps, les règles. »",
              32, "pb-2 cc1 er-1"),
        ]),
        I(31, "golay", "neutral",
          "La Dre Golay déroule la situation : les reins, le cœur, les six kilos, les chutes, "
          "le refus de la dialyse, la volonté de mourir ici. Daniel écoute, debout. À la fin : "
          "« Il y a un EMS à Orbe avec une place en juin. » Jeannine : « Non. » Daniel se "
          "tourne vers vous. « Et vous ? Vous allez la découper, vous aussi, un jour ? »", [
            R("« Non. Ceux qui dissèquent ne savent jamais qui est devant eux. Personne ne "
              "saura que c'est elle. »", 7, "cc3 rd2 pb1"),
            R("« Peut-être. Je ne sais pas. »", 6, "cc-2 em-1"),
            R("« Ce n'est pas une boucherie, monsieur. »", 6, "rd-1 em-2"),
            R("Laisser la Dre Golay répondre.", 7, "ic2 pb1"),
            R("« Ça, il faudrait le demander à la Pre Vautier, à l'institut. Je peux vous "
              "donner son contact. »", 7, "ic2 cc1 pb1"),
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
# 5.2 La grange
# ---------------------------------------------------------------------------
_INTRO_52 = (
    "Après la réunion. Il fait nuit. Océane vous attend dans la grange, assise sur une botte "
    "de paille, l'écran de son téléphone allumé comme une lampe."
)
_INTRO_52_SEULE = (
    "Après la réunion. Il fait nuit. En traversant la cour pour repartir, vous entendez "
    "quelqu'un tousser dans la grange, dont la porte est restée entrouverte."
)

S5_2 = S(2, "5.2 La grange", _INTRO_52,
    focus=("em", "rd", "pb", "co"),
    entries=[
        Entry(1, when(all=["oceane_confiance"]), _INTRO_52),
        Entry(10, when(none=["oceane_confiance"]), _INTRO_52_SEULE),
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
            "Vous n'avez rien décidé pour Océane, rien dit à son père ni à sa grand-mère, et "
            "vous ne l'avez pas laissée seule : un numéro, des horaires, le droit de changer "
            "d'avis. C'est exactement ce qu'on peut faire, et pas davantage, quand une "
            "adolescente confie une grossesse.")),
    ],
    nodes=[
        I(1, "oceane", "vulnerable",
          "« Je peux te dire un truc ? Un vrai secret. » Elle éteint son téléphone. Dans le "
          "noir, sa voix. « Je suis enceinte. Dix semaines. Personne ne sait. Ni mon copain, ni "
          "papa. Juste mamie, peut-être : elle me regarde bizarrement depuis Pâques. » Un "
          "temps. « Elle ne peut pas mourir maintenant. Tu comprends ? Pas maintenant. »", [
            R("Laisser un silence. « Merci de me le dire. Comment tu te sens, toi ? »",
              2, "em3 co2 rd1"),
            R("« Tu vas le garder ? »", 3, "pb-2 rd-2"),
            R("« Il faut le dire à ton père, ce soir. »",
              4, "pb-3 rd-2"),
            R("« Félicitations ! »", 3, "em-1 cc-1"),
            R("« Tu as vu un médecin ? »", 5, "cc2 pb1"),
        ]),
        I(2, "oceane", "sad",
          "« Mal. » Elle rit et pleure à la fois. « Je ne sais pas si je le veux. Je ne sais "
          "rien. J'ai dix-sept ans, je suis en deuxième année d'apprentissage, et mon père ne "
          "parle à personne. » Elle s'essuie le nez sur sa manche. « Toi, tu sais des trucs. "
          "Dis-moi quoi faire. »", [
            R("« Je ne décide pas pour toi. Mais des gens peuvent t'aider à réfléchir, sans te "
              "juger : le centre de santé sexuelle, ou la Dre Golay. On regarde comment les "
              "joindre ? »", 6, "pb3 cc2 em1 co1 ic1 rd1", sets=["oceane_orientee"]),
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
            R("« Pardon. Je t'écoute, c'est tout. »", 2, "rd2 em2 er1 co1"),
            R("« Je voulais juste savoir. »", 7, "pb-1 em-1"),
            R("« Ok, ok. »", 7, "em-1"),
            R("« Il faut quand même que tu réfléchisses vite, à dix semaines : en Suisse, après "
              "douze semaines, ce n'est plus toi seule qui décides. »", 7, "pb-2 em-2"),
        ]),
        I(4, "oceane", "angry",
          "« Mon père ? » Océane se lève d'un bond. « Mon père ne sait même pas regarder sa "
          "mère maigrir ! Tu veux que je lui annonce ça ce soir, après ça ? » Elle vous fixe. "
          "« Si tu lui dis, je ne te parle plus jamais. »", [
            R("« Je ne lui dirai rien. À personne. C'est toi qui décides qui sait, et quand. "
              "Pardon. »", 2, "pb3 rd2 er1"),
            R("« Il a le droit de savoir : tu es mineure. »", 12, "pb-3 rd-2"),
            R("« D'accord, je ne dirai rien. »", 7, "pb1"),
            R("Se taire.", 7, "er-1"),
        ]),
        I(5, "oceane", "suspicious",
          "« Un médecin ? Pour qu'il le dise à papa ? » Elle secoue la tête. « On est dans un "
          "village. La Dre Golay a soigné toute ma famille. »", [
            R("« La Dre Golay est tenue au secret, même envers ton père : à dix-sept ans, c'est "
              "toi qui décides. Et il y a le centre de santé sexuelle, à Yverdon. »",
              6, "cc3 pb2 em1", sets=["oceane_orientee"]),
            R("« Ton père le saura de toute façon. »", 7, "pb-2 em-2"),
            R("« Je ne sais pas comment ça marche, pour les mineures. »", 7, "cc-1"),
            R("« Si tu veux, je demande à la Dre Golay comment ça se passe, sans dire ton nom : "
              "elle ne saura pas que c'est toi, je dirai que c'est pour une amie. »",
              6, "pb-1 em1 ic1", sets=["oceane_orientee"]),
        ]),
        I(6, "oceane", "grateful",
          "Océane rallume son téléphone. Vous cherchez ensemble le numéro du centre de santé "
          "sexuelle, et les horaires. Elle l'enregistre sous « Fleuriste Yverdon ». Elle rit, "
          "pour la première fois de la soirée. « Mamie, je lui dirai. Avant… avant. » Elle se "
          "lève, s'époussette. « Merci de ne pas m'avoir dit quoi faire. »", [
            R("« Tu as le droit de changer d'avis, sur tout. »", 13, "em2 pb2 cc1",
              sets=["oceane_orientee"]),
            R("« Tiens-moi au courant. »", 13, "pb-1 em1", sets=["oceane_orientee"]),
            R("« Je peux venir avec toi au rendez-vous, si tu veux : comme ça, tu ne seras pas "
              "seule, et je pourrai t'expliquer ce que te dit la conseillère. »",
              13, "pb-3 em1", sets=["oceane_orientee"]),
            R("La laisser partir, et rester un moment dans la grange.", 13, "er1 rd1",
              sets=["oceane_orientee"]),
        ]),
        I(7, "oceane", "hurt",
          "Océane hausse les épaules. « Laisse tomber. » Elle se lève. « T'es comme les "
          "autres. » Elle sort de la grange. Dans la cour, vous l'entendez ouvrir la portière "
          "de sa Twingo.", [
            R("La rattraper : « Océane, attends. Tu peux trouver de l'aide sans que ton père "
              "le sache. Je te donne le numéro du centre de santé sexuelle ? »", 6,
              "pb2 em1 cc2 co2", sets=["oceane_orientee"]),
            R("La laisser partir.", 13, "em-1 co-1", sets=["oceane_seule"]),
            R("Lui envoyer un message plus tard : « désolé·e ».", 13, "em1",
              sets=["oceane_seule"]),
            R("Aller le dire à la Dre Golay, sans son accord, « pour son bien ».", 9,
              "pb-3 rd-2", sets=["oceane_trahie"]),
        ]),
        I(8, "daniel", "angry",
          "Daniel est assis sur le marchepied du tracteur. Vous vous entendez lui dire : "
          "« Il faut que vous parliez à Océane. Elle a besoin de vous. Elle est enceinte. » "
          "Daniel vous regarde comme si vous lui aviez tiré dessus. Derrière vous, sur le seuil "
          "de la grange, Océane a tout entendu.", [
            R("« Océane. Pardon. »", END, "pb2 rd2 er1",
              sets=["oceane_trahie"]),
            R("« C'était pour ton bien. »", END, "pb-3 rd-2", sets=["oceane_trahie"]),
            R("Partir, sans un mot.", END, "er-2 rd-1", sets=["oceane_trahie"]),
            R("« Monsieur Pittet, soyez doux avec elle, s'il vous plaît : elle a peur, et elle "
              "a peur de vous décevoir, surtout ce soir. »", END, "pb-2 em1",
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
            R("S'accroupir à côté d'elle, lui tendre un mouchoir, et attendre.", 11,
              "em3 rd1 pb1 co2"),
            R("« C'est le stress de la réunion. »", 11, "cc-1"),
            R("« Tu es enceinte ? »", 3, "pb-2 rd-2"),
            R("Aller chercher Thierry, l'infirmier.", 11, "ic1 pb-1 em-1"),
            R("Ressortir, gêné·e.", 7, "em-2 co-1"),
        ]),
        I(11, "oceane", "suspicious",
          "Océane s'essuie la bouche. Elle rit, sans joie. « Ça fait trois semaines que je "
          "vomis tous les matins. Je suis enceinte. Voilà. » Elle vous regarde, défiante. "
          "« Content·e ? Maintenant tu sais un truc que mon père ne sait pas. »", [
            R("« Je ne dirai rien à personne. Et toi, comment tu te sens ? »", 2,
              "pb3 em2 rd1"),
            R("« Il faut le dire à ton père. Il a le droit de savoir, tu es mineure. »", 4, "pb-3 rd-2"),
            R("« Tu vas le garder ? Avec ton apprentissage, ce ne sera pas simple. »", 3, "pb-2 rd-2 em-1"),
            R("« Tu as vu un médecin ? Dix semaines, il faudrait une échographie, et faire les "
              "prises de sang du premier trimestre, au moins pour vérifier que tout va "
              "bien. »", 5, "cc1 pb-1"),
        ]),
        I(12, "oceane", "angry",
          "« Si tu lui dis, je te jure… » Océane a les poings serrés. Par la porte de la "
          "grange, on voit Daniel dans la cour, assis sur le marchepied du tracteur, la tête "
          "dans les mains.", [
            R("« Je ne lui dirai pas. C'est toi qui décides. »", 2, "pb3 rd2 er1"),
            R("Sortir rejoindre Daniel dans la cour.", 8, "pb-3 rd-3 em-1"),
            R("« Alors dis-le-lui toi-même. Ce soir. Moi, je ne peux pas garder ça. »", 7, "pb-2 rd-1"),
            R("Se taire, et regarder Daniel par la porte, en vous demandant combien de temps "
              "un père peut rester assis comme ça, sans bouger.", 7, "er-1"),
        ]),
        I(13, "jeannine", "neutral",
          "En repassant par la cuisine, vous croisez le regard de Jeannine, dans son fauteuil. "
          "Elle vous arrête d'un geste. « Elle vous a parlé, la petite. Je le vois à votre "
          "tête. » Un temps. « Elle est enceinte, n'est-ce pas ? »", [
            R("« Je ne peux pas vous dire ce qu'Océane m'a dit, ni même si elle m'a dit quelque "
              "chose. »", END, "pb3 cc2 rd1"),
            R("« Oui. Dix semaines. »", END, "pb-3 rd-2"),
            R("« Je ne sais pas de quoi vous parlez. »", END, "cc-2 pb1 rd-1"),
            R("« Vous l'avez su avant elle, je crois. »", END, "pb-3 rd-1 em1"),
            R("« Si elle a quelque chose à vous dire, elle viendra. Elle vous aime. »",
              END, "pb1 em2 co1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.3 La dernière visite — la veille de l'examen, puis l'examen et l'appel de Sandra
# ---------------------------------------------------------------------------
_INTRO_53 = (
    "Juin, la veille de l'examen de fin d'année. Les Combettes. À la demande de Jeannine, on "
    "a installé le lit médicalisé dans la cuisine, face à la cour, et la fenêtre est "
    "ouverte. Thierry est là, avec Véronique Bühler, l'infirmière de l'équipe mobile de "
    "soins palliatifs. La Dre Golay vous attend sur le seuil."
)

S5_3 = S(3, "5.3 La dernière visite", _INTRO_53,
    focus=("co", "er", "rd", "pb"),
    entries=[
        Entry(1, when(all=["famille_apaisee"]), _INTRO_53),
        Entry(20, when(none=["famille_apaisee"]), _INTRO_53),
    ],
    debriefs=[
        Debrief(when(all=["examen_quitte"]), tone="mixed", lead=(
            "Vous avez quitté l'examen pour Jeannine. Personne ne peut dire que c'était une "
            "faute ; mais regardez comment la décision s'est prise. Dans une urgence qui "
            "touche un·e patient·e qu'on aime, on vérifie d'abord ce qui se passe vraiment "
            "(des heures ou des jours ?), on écoute ce que la personne a elle-même demandé, "
            "et on ne sacrifie pas sa formation par culpabilité. Le rattrapage d'août, lui, "
            "existe.")),
        Debrief(when(all=["examen_fini"]), tone="good", lead=(
            "Vous avez fini votre examen, comme Jeannine l'avait demandé, après avoir vérifié "
            "qu'il s'agissait de jours et non d'heures. Rester n'est pas abandonner : c'est "
            "parfois la manière la plus fidèle de répondre à quelqu'un qui vous a appris à "
            "recevoir le reste.")),
    ],
    nodes=[
        I(20, "jeannine", "neutral",
          "Daniel est dans la cour, assis sur le marchepied de son tracteur, moteur éteint. Il "
          "ne rentre pas. Il ne part pas non plus. Dans la cuisine, Jeannine ouvre les yeux "
          "quand vous entrez. « Ah. La fac. » Un souffle. « C'est demain… votre examen ? »", [
            R("« Demain. » Et s'asseoir près du lit.", 2, "em1 rd1 co2"),
            R("« Oui. » Et regarder par la fenêtre, vers Daniel.", 2, "cc1"),
            R("« Daniel ne rentre pas ? »", 2, "pb-1 em1"),
            R("Aller d'abord parler à Daniel, dans la cour, pour lui dire que sa mère le "
              "réclame, même si elle ne l'a pas dit.", 21, "pb-2 em1"),
            R("« Votre fils pourrait faire un effort, aujourd'hui. »", 2, "rd-2 em-1 co-1"),
        ]),
        I(21, "daniel", "resigned",
          "« Retournez à l'intérieur. » Daniel ne lève pas les yeux. « Je rentrerai quand je "
          "pourrai. » Un temps. « Dites-lui… non. Rien. »", [
            R("« D'accord. » Et retourner dans la cuisine.", 2, "pb2 rd2"),
            R("« Elle vous attend. »", 2, "pb-1 em1"),
            R("« Vous allez le regretter. »", 2, "pb-3 rd-2"),
            R("S'asseoir un instant à côté de lui, en silence, puis rentrer.", 2,
              "em1 co2 pb-1"),
        ]),
        I(1, "daniel", "sad",
          "Daniel est assis à côté du lit, sur une chaise de cuisine trop petite pour lui. Il "
          "tient la main de sa mère. Il vous fait un signe de tête, le premier depuis des "
          "mois. « Elle vous attendait. Elle a demandé si vous aviez révisé. »", [
            R("« Un peu. Merci de m'avoir laissé venir. » Et s'approcher du lit.",
              2, "rd2 em1 cc1"),
            R("Saluer Daniel d'un signe de tête, et rester en retrait.", 2, "rd2 pb1"),
            R("« Comment va-t-elle ? »", 2, "cc1 em1"),
            R("Aller droit au lit, sans un mot pour Daniel.", 2, "rd-2 ic-1"),
        ]),
        I(2, "jeannine", "melancholic",
          "Jeannine respire lentement, avec de longues pauses. Véronique ajuste l'oxygène et "
          "vous fait signe : vous pouvez approcher. Océane est assise au pied du lit. Jeannine "
          "tend la main, la pose à plat sur le ventre de sa petite-fille, et la laisse là. "
          "Océane devient toute rouge, puis pleure. Jeannine sourit. « Je l'ai su… avant "
          "elle. Six cents fois. » Puis elle vous regarde. « Approchez. »", [
            R("S'agenouiller à la hauteur de son visage.", 3, "rd2 em2 co1"),
            R("Rester debout au pied du lit.", 3, "er-1 em-1"),
            R("« Ne vous fatiguez pas à parler, Madame Pittet : on est tous là, vous n'avez "
              "rien à dire, reposez-vous. »", 3, "rd-2 cc-1"),
            R("Prendre sa main.", 3, "em2 co2"),
        ]),
        I(3, "jeannine", "neutral",
          "Jeannine fait un geste vers la table de nuit. L'enveloppe beige : « À ouvrir "
          "après. » « C'est pour vous. Pas avant. » Elle referme les doigts sur votre main. « Et "
          "à la cérémonie… les étudiants parlent, n'est-ce pas ? » Un souffle. « Dites quelque "
          "chose de bien. Pour tous. Pas pour moi. »", [
            R("« Je vous le promets. Pour tous. » Et prendre l'enveloppe.", 4,
              "rd2 co2 pb1"),
            R("« Je dirai votre nom. Tout le monde saura ce que vous avez fait. »",
              5, "pb-3 rd-2"),
            R("Prendre l'enveloppe, incapable de répondre.", 4, "co1 er-1"),
            R("« Je ne suis pas sûr·e d'être choisi·e pour parler. »", 4, "cc1 er-1"),
            R("L'ouvrir tout de suite, devant elle, pour qu'elle sache que vous l'avez lue "
              "et qu'elle puisse vous dire si vous avez bien compris.", 5, "rd-3 pb-2"),
        ]),
        I(5, "jeannine", "cold-anger",
          "Jeannine retire sa main. Elle a encore la force de froncer les sourcils. « Non. » Un "
          "souffle. « Je l'ai donné… sans mon nom. Comme les autres. » Elle ferme les yeux. "
          "« Ne me faites pas… regretter… la fac. »", [
            R("« Pardon. Sans votre nom. Pour tous. »", 4, "rd3 pb2"),
            R("« Mais vous méritez qu'on le sache ! »", 4, "pb-2 rd-1"),
            R("Se taire, honteux·se.", 4, "er-1"),
            R("Reposer l'enveloppe sur la table de nuit.", 4, "rd1"),
        ]),
        I(4, "buhler", "neutral",
          "Véronique Bühler vous fait signe de la suivre sur le seuil. « Elle dort, maintenant. "
          "Ça peut être ce soir, ou dans trois jours. Ses réserves sont prêtes : morphine pour "
          "le souffle, midazolam si elle s'agite. Thierry et moi, on se relaie. » Elle vous "
          "regarde. « Vous voulez rester ? Vous pouvez. Mais vous avez un examen demain. »", [
            R("« Un peu, si la famille est d'accord. Je ne veux prendre la place de "
              "personne. »", 6, "rd2 pb2 em1"),
            R("« Je reste jusqu'au bout. Mon examen, je le repasserai. »", 6, "pb-2 em1"),
            R("« Je rentre. Appelez-moi si… »", 7, "er1 pb1"),
            R("« Je peux faire quelque chose ? Une injection ? »", 6, "pb-3 ic-1"),
            R("« Comment vous faites, vous, pour faire ça tous les jours, sans craquer, et "
              "rentrer chez vous le soir comme si de rien n'était ? »", 8, "ic1 er1"),
        ]),
        I(8, "buhler", "neutral",
          "Véronique sourit. « On ne fait pas ça tous les jours. On le fait un jour après "
          "l'autre. » Elle regarde la cuisine, le lit, la fenêtre ouverte. « Et on n'est "
          "jamais seule : Thierry, la Dre Golay, la famille. Vous. » Elle vous rend votre sac. "
          "« Alors, vous restez, ou vous rentrez ? »", [
            R("« Je reste un peu, si la famille est d'accord. »", 6, "rd2 pb2 co1"),
            R("« Je rentre. Merci. »", 7, "er1"),
            R("« Je reste toute la nuit, avec elle. »", 6, "pb-2"),
            R("« Je ne sais pas. »", 7, "er-1"),
        ]),
        I(6, "narr", "",
          "Vous restez jusqu'à la nuit. Océane s'est endormie sur le canapé, la main sur son "
          "ventre. Thierry fait du café que personne ne boit. Au moment où vous partez, "
          "Jeannine ouvre les yeux. « Finissez… votre examen. » Un souffle. « Sinon… je vous "
          "botte les fesses. »", [go(9)]),
        I(7, "narr", "",
          "Dans le bus du soir, vous tenez l'enveloppe sur vos genoux, sans l'ouvrir. « À "
          "ouvrir après. » L'écriture est penchée, appliquée : celle d'une femme qui a rempli "
          "des carnets de naissance pendant quarante ans.", [go(9)]),
        I(9, "narr", "",
          "Le lendemain. La grande salle de l'université, trois cents tables, trois cents têtes "
          "penchées. Examen de fin d'année, quatre heures. À la pause de 10 h 30, votre "
          "téléphone, rallumé dans le couloir, affiche trois appels manqués : Sandra, Sandra, "
          "Sandra.", [go(10)]),
        I(10, "sandra", "anxious",
          "Sandra décroche à la première sonnerie. « Alex. Jeannine est très faible depuis "
          "cette nuit. Elle ne mange plus, elle dort presque tout le temps. La Dre Golay est "
          "là-bas, avec l'équipe de soins palliatifs. » Un temps. « Elle a demandé après toi. "
          "Deux fois. »", [
            R("« Des heures, ou des jours ? »", 11,
              "cc3 er2 ic1"),
            R("« J'arrive. » Et partir sans repasser par la salle d'examen, la copie à moitié "
              "remplie sur la table, la veste sur la chaise.", 13, "er-2 pb-1 em1",
              sets=["examen_quitte"]),
            R("« Je ne peux pas, je suis en examen. » Et raccrocher.", 14,
              "em-2 cc-1 co-1"),
            R("« Dis-lui que je viens ce soir. »", 11, "em1 cc1 co1"),
            R("Fondre en larmes, au milieu du couloir.", 15, "er-2"),
        ]),
        I(11, "sandra", "sad",
          "« La Dre dit : des jours, peut-être une semaine. Pas des heures. » Sandra hésite. "
          "« Et Jeannine a redit un truc, ce matin, quand la Dre lui a parlé de ton examen. » "
          "Elle imite la voix de Jeannine, mal, en riant à moitié : « Dites-lui de finir son "
          "examen, sinon je lui botte les fesses. »", [
            R("« Dis-lui que je le finis, et que je viens ce soir. Merci, Sandra. »",
              12, "er2 cc2 rd1 co1", sets=["examen_fini"]),
            R("« Je viens quand même, maintenant. »", 13, "er-1 rd-1",
              sets=["examen_quitte"]),
            R("Aller demander au surveillant ce qui est possible.", 16, "cc1 pb1"),
            R("« D'accord. » Raccrocher, et retourner en salle, la tête ailleurs.",
              12, "er-1", sets=["examen_fini"]),
        ]),
        I(14, "narr", "",
          "Vous retournez en salle. Vous ne voyez plus les questions. À 11 h 15, vous posez "
          "votre stylo. Vous n'arrivez plus à écrire.", [
            R("Continuer, une question après l'autre, en respirant.", 12, "er3 pb1",
              sets=["examen_fini"]),
            R("Rendre la copie, sortir, et rappeler Sandra : « Dis-lui que je viens ce "
              "soir. »", 12, "er1 em1 co1", sets=["examen_fini"]),
            R("Partir en courant.", 13, "er-2", sets=["examen_quitte"]),
            R("Lever la main pour demander au surveillant la permission de sortir "
              "téléphoner, en expliquant qu'une patiente que vous suivez est en fin de "
              "vie.", 16, "er1 cc1 ic1"),
        ]),
        I(15, "narr", "",
          "Une étudiante que vous ne connaissez pas vous tend un mouchoir sans rien dire, et "
          "retourne dans la salle. Le téléphone vibre encore : Sandra.", [
            R("Rappeler Sandra, et lui demander ce que dit la Dre Golay.", 11, "er2 cc2"),
            R("Éteindre le téléphone, et retourner en salle.", 12, "er-1 em-1 co-1",
              sets=["examen_fini"]),
            R("Partir en courant.", 13, "er-2", sets=["examen_quitte"]),
            R("Appeler Yasmine.",
              11, "er2 ic1"),
        ]),
        I(16, "narr", "",
          "Le surveillant vous écoute, poliment. « Une patiente ? Pas de la famille ? » Il "
          "hausse les épaules, désolé. « Si vous sortez, vous ne pourrez pas revenir. Vous "
          "serez inscrit·e à la session de rattrapage, en août. C'est votre choix. »", [
            R("Retourner à votre table : Jeannine a dit de finir. Vous irez ce soir.", 12,
              "er2 pb1 rd1", sets=["examen_fini"]),
            R("Sortir : vous passerez le rattrapage en août.", 13, "er1 em1",
              sets=["examen_quitte"]),
            R("« Juste une heure, et je reviens ? » Il refuse. Vous retournez à votre "
              "table.", 12, "pb-1", sets=["examen_fini"]),
            R("« Il est inhumain, votre règlement : elle va mourir, et vous me parlez de "
              "session de rattrapage. »", 12, "er-2 rd-1", sets=["examen_fini"]),
        ]),
        I(12, "narr", "",
          "Vous retournez à la table 214. Pendant deux heures, vous répondez à des questions "
          "sur les reins, les hormones, la reproduction — la filtration glomérulaire, la "
          "créatinine, tout ce que Jeannine vous a appris sans le savoir. À 14 h 30, vous "
          "rendez la copie. Le bus de Montchéry part à 14 h 52.", [go(17)]),
        I(13, "narr", "",
          "Vous laissez votre copie à moitié remplie sur la table 214, votre veste sur la "
          "chaise. Dans le train, puis dans le bus de Montchéry, vous pensez à Jeannine. À la "
          "ferme, à 13 h 30, la Dre Golay vous ouvre la porte. Elle ne dit rien. Elle vous "
          "laisse entrer.", [go(18)]),
        I(17, "jeannine", "happy",
          "16 h 10. La cuisine des Combettes. Jeannine respire lentement, avec de longues "
          "pauses. Elle ouvre les yeux quand vous vous asseyez. « Alors ? » Un souffle. "
          "« Fini ? »", [
            R("« Fini. Pour vous. »", 19, "em2 rd1 co2"),
            R("« Je crois que je l'ai raté. »", 19, "er-2 em-1"),
            R("Lui raconter les questions sur la créatinine et la filtration "
              "glomérulaire, en riant, pour qu'elle sache qu'elle était dans l'examen.", 19, "em-1 rd-2 cc-1"),
            R("« Oui. Ne vous fatiguez pas à parler. »", 19, "rd-1 cc1"),
            R("Prendre sa main, et hocher la tête.", 19, "em1 co2"),
        ]),
        I(18, "jeannine", "neutral",
          "Jeannine ouvre les yeux. Elle fronce les sourcils. « Il est… quelle heure ? Vous "
          "n'êtes pas… à votre examen ? »", [
            R("« Je suis parti·e. Je voulais être là. »", 22, "er1 em2 cc1 rd1"),
            R("« Ils l'ont annulé. »", 22, "cc-3 pb-1"),
            R("« Vous me botterez les fesses plus tard. »", 22, "em2 co1"),
            R("S'asseoir près du lit, sans répondre, et lui prendre la main, parce que vous "
              "n'avez pas envie de mentir, et pas la force d'expliquer.", 22, "em1 rd1"),
        ]),
        I(22, "jeannine", "happy",
          "Jeannine soupire, et ça lui coûte. « Petit… » Elle cherche son souffle. « J'ai mis… "
          "six cents enfants au monde. Pas un seul… n'est arrivé à l'heure que j'avais "
          "prévue. » Un sourire. « Vous passerez le rattrapage. Et vous me raconterez. »",
          [go(19)]),
        I(19, "buhler", "neutral",
          "À 22 h, Véronique vous raccompagne jusqu'à la porte. « Rentrez. Revenez quand vous "
          "voudrez. Elle sait que vous êtes venu·e. » Dans la cour, la fenêtre de la cuisine "
          "est restée ouverte. On entend la respiration de Jeannine, de longues pauses, puis "
          "encore."),
    ],
)

# ---------------------------------------------------------------------------
# 5.4 Le fourgon — branche « la famille s'est apaisée »
# ---------------------------------------------------------------------------
S5_4A = S(4, "5.4 Le fourgon",
    "Trois jours plus tard, 5 h 40. Thierry vous appelle : Jeannine est morte à 4 h 50, "
    "Daniel à côté d'elle. Le fourgon de l'institut d'anatomie viendra à 9 h. « Tu peux "
    "venir, si tu veux. Daniel a dit oui. »",
    focus=("co", "ic", "rd", "er"),
    slot="5.4",
    cond=when(all=["famille_apaisee"]),
    nodes=[
        I(1, "narr", "",
          "Quand vous arrivez, la cuisine est calme. Jeannine est dans le lit, les mains "
          "croisées sur le drap, le foulard rouge noué. Véronique et Thierry ont fait la "
          "toilette. Océane a peint les ongles de sa grand-mère : rouge. Daniel est assis ; il "
          "ne pleure pas. Il vous fait signe d'entrer.", [
            R("S'approcher du lit, et la regarder longtemps, en silence.",
              2, "rd3 co2 er1"),
            R("Présenter vos condoléances à Daniel, puis à Océane, simplement.",
              2, "rd2 em2 co1"),
            R("« Elle a l'air paisible. »", 2, "em1 cc-1"),
            R("Chercher son pouls, comme on vous l'a appris, pour constater le décès "
              "vous-même : c'est le premier geste qu'on vous a enseigné pour une personne "
              "qu'on trouve sans vie.", 3, "pb-3 rd-2"),
            R("Fondre en larmes.", 2, "er-1 co1"),
        ]),
        I(2, "oceane", "sad",
          "Océane vous montre les mains de sa grand-mère. « Elle m'a dit, la semaine passée : "
          "« Tu me feras les ongles, pour partir. En rouge. Les étudiants doivent voir que "
          "quelqu'un a pris soin de moi. » » Elle renifle. « Je ne savais pas que ça voulait "
          "dire quelque chose. »", [
            R("« Ils le verront. »", 6, "co3 em2 rd1"),
            R("« Ça veut dire beaucoup. En septembre, sur la table, la première chose que j'ai "
              "remarquée, c'étaient des ongles vernis. »", 6, "co3 rd1 pb-1"),
            R("« C'est un peu morbide, non ? »", 6, "rd-3 em-2"),
            R("Hocher la tête, la gorge serrée.", 6, "em1 co1"),
            R("« Les étudiants ne sauront pas que c'est elle : c'est anonyme. »",
              6, "cc1 em-1"),
        ]),
        I(3, "golay", "neutral",
          "La Dre Golay pose une main sur votre poignet. « C'est fait, Alex. À 5 h 10, par "
          "moi. » Elle ne lâche pas votre poignet tout de suite. « Aujourd'hui, vous n'êtes pas "
          "là pour faire. Vous êtes là pour être là. »", [
            R("« Pardon. » Et reculer d'un pas.", 2, "rd2 er1 pb1"),
            R("« C'est le réflexe. »", 2, "er-1"),
            R("Se taire, et rester près d'elle.", 2, "er1 rd1"),
            R("« Je voulais juste être sûr·e, pour la famille : c'est important qu'un "
              "professionnel le confirme, non ? »", 2, "pb-1 er-1"),
        ]),
        I(6, "thierry", "melancholic",
          "Thierry se lève et ouvre en grand la fenêtre de la cuisine, que quelqu'un avait "
          "refermée à cause de la fraîcheur de la nuit. L'air de juin entre, avec l'odeur de "
          "l'herbe coupée. « Elle me l'avait demandé, la première fois que je "
          "suis venu. « Le jour où je meurs, tu ouvres la fenêtre. Pour que je puisse "
          "sortir. » » Il reste là, les mains sur le rebord.", [
            R("Rester à côté de lui, sans rien dire.", 4, "co2 ic1 em1 er1"),
            R("« C'est une croyance de la campagne, ça ? »", 4, "rd-2 em-1"),
            R("« Tu as tenu ta promesse. »", 4, "em2 co1"),
            R("« Il faudrait la refermer avant que le fourgon arrive, non ? Avec les mouches, "
              "et la chaleur qui monte, ce n'est peut-être pas l'idéal pour le corps. »",
              4, "rd-2 co-2 pb-1"),
            R("Ouvrir aussi la porte de la cour.", 4, "co1 rd1"),
        ]),
        I(4, "narr", "",
          "À 9 h, le fourgon de l'institut d'anatomie se gare dans la cour. Deux hommes en "
          "costume sombre, un brancard, une housse. Ils parlent bas ; ils demandent la "
          "permission pour tout. Daniel se lève. Il ouvre en grand la porte de la cuisine, et "
          "il la tient. Il ne dit rien. Il tient la porte.", [
            R("Se placer en retrait, à côté d'Océane.", 5, "rd3 pb2 co1"),
            R("Aider les deux hommes à porter le brancard.", 5, "pb-2 ic1"),
            R("Poser la main sur l'épaule d'Océane.", 5, "em2 co2"),
            R("Prendre une photo du fourgon, pour vous en souvenir.", 5, "rd-3 pb-3"),
            R("Sortir avant, pour ne pas voir.", 5, "er-1 co-1"),
        ]),
        I(5, "daniel", "resigned",
          "Le fourgon démarre lentement, dans le gravier. Daniel le regarde jusqu'au virage. "
          "Puis il se tourne vers vous. « Elle disait que vous l'écoutiez. » Il remet sa "
          "casquette. « Faites-en quelque chose. »", [
            R("« Je vous le promets. »", 7, "co2 rd2"),
            R("Lui serrer la main.", 7, "rd2 em1"),
            R("« Elle va beaucoup nous apprendre. »", 7, "pb-1 em-1"),
            R("Se taire, et regarder le virage, à côté de lui.", 7, "em1 co2"),
            R("« Vous avez été courageux, Monsieur Pittet. Peu de fils auraient tenu la porte "
              "comme vous l'avez fait, après tout ce que vous avez vécu. »", 7, "em1 pb-1"),
        ]),
        I(7, "oceane", "vulnerable",
          "Avant que vous repartiez, Océane vous rattrape près de la grange. « La cérémonie, "
          "en juin… On peut venir ? Moi, et papa, s'il veut. »", [
            R("« Je crois que oui. Je demande à la Pre Vautier, et je te redis. »", END,
              "cc2 ic2 em1"),
            R("« Je ne sais pas. Demande à quelqu'un d'autre. »", END, "cc-2 em-1"),
            R("« Oui, et je dirai le nom de ta grand-mère, pour qu'on sache qui elle "
              "était. »", END, "pb-3 rd-2"),
            R("« J'aimerais beaucoup que tu sois là. »", END, "em2 co1"),
            R("« Il vaudrait peut-être mieux que vous ne veniez pas cette année, ton père et "
              "toi : ce sera très dur, si près de sa mort. »", END, "pb-2 em-1 rd-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.4 « Vous ne l'emmènerez pas » — branche « la famille s'est déchirée »
# ---------------------------------------------------------------------------
S5_4B = S(5, "5.4 Vous ne l'emmènerez pas",
    "Trois jours plus tard, 6 h. Thierry vous appelle : Jeannine est morte à 4 h 50, la "
    "fenêtre ouverte. Daniel était dans la cour ; il est entré à 5 h, quand Thierry l'a "
    "appelé. Le fourgon de l'institut d'anatomie doit venir à 9 h. « Daniel dit qu'il ne la "
    "laissera pas partir. La Dre Golay est là. Viens, si tu peux. »",
    focus=("rd", "pb", "ic", "er"),
    slot="5.4",
    cond=when(none=["famille_apaisee"]),
    debriefs=[
        Debrief(when(), tone="mixed", lead=(
            "Un don du corps est un acte de volonté de la personne, écrit et signé. Mais un "
            "institut d'anatomie n'arrache pas un corps à une famille qui s'y oppose de toutes "
            "ses forces : un don se fait en paix, ou il ne se fait pas. Dans ces heures-là, "
            "l'étudiant·e n'a rien à décider et presque rien à dire. Être là, se taire, ne pas "
            "plaider : c'est ce qui laisse à une famille la place de changer d'avis.")),
    ],
    nodes=[
        I(1, "daniel", "angry",
          "Dans la cuisine, Jeannine est dans le lit, le foulard rouge noué, les ongles peints "
          "en rouge par Océane. Daniel est debout contre la porte, les bras en croix, comme "
          "pour la boucher. « Personne ne l'emmène. Elle sera enterrée à Montchéry, à côté de "
          "mon père. » La Dre Golay est au téléphone, à voix basse. Océane pleure sur le "
          "canapé.", [
            R("Laisser la Dre Golay mener.",
              2, "pb2 ic2 rd1"),
            R("« Monsieur Pittet, c'était sa volonté : c'est écrit, et signé, et vous ne "
              "pouvez pas vous y opposer, légalement. »", 3, "pb-2 rd-1 em-2"),
            R("S'asseoir à côté d'Océane.", 2, "em2 co2"),
            R("« Vous n'avez pas le droit. »", 3, "pb-3 rd-2 em-2"),
            R("Aller voir Jeannine, en silence, un moment.", 2, "rd2 co1"),
        ]),
        I(2, "golay", "neutral",
          "La Dre Golay raccroche. « C'était la Pre Vautier. » Elle s'adresse à Daniel, "
          "calmement. « La volonté de votre mère est écrite et signée. Mais l'institut "
          "n'arrachera jamais un corps à une famille qui s'y oppose de toutes ses forces. La "
          "Pre Vautier dit : un don, ça se fait en paix, ou ça ne se fait pas. » Daniel la "
          "regarde, interdit. « Donc… c'est moi qui décide ? » — « C'est vous qui décidez si "
          "vous pouvez la laisser partir. Personne ne vous forcera. »", [
            R("Se taire. Ce n'est ni votre décision, ni votre famille.", 4, "pb3 rd2"),
            R("« Votre mère voulait aider les étudiants. Moi, elle m'a aidé·e. »",
              4, "pb-1 co2 cc1"),
            R("« Si vous refusez, vous trahissez votre mère. »", 5, "pb-3 rd-2 em-2"),
            R("Regarder Océane, qui s'est levée.", 4, "em1 rd1"),
            R("« C'est injuste pour l'institut, qui a déjà tout préparé, et pour les "
              "étudiants, qui comptaient sur elle. »", 5, "rd-2 em-2"),
        ]),
        I(3, "daniel", "cold-anger",
          "Daniel se tourne vers vous. « Vous. » Sa voix tremble. « Vous voulez la découper "
          "vous-même ? » Thierry fait un pas, et se place entre vous deux, sans un mot.", [
            R("« Non. Pardon. » Et reculer près d'Océane.", 2, "pb3 rd2 er1"),
            R("« Ce ne sera pas moi qui la découperai : les étudiants ne savent jamais qui est "
              "sur leur table. »", 5, "cc-2 rd-1"),
            R("Sortir dans la cour.", 2, "er1 pb1"),
            R("« Calmez-vous. »", 5, "rd-1 em-2"),
        ]),
        I(4, "oceane", "sad",
          "Océane s'approche de son père, lui prend le bras. « Papa. Elle m'a fait lui peindre "
          "les ongles. Pour les étudiants. Pour qu'ils voient que quelqu'un l'aimait. » Elle "
          "pleure. « Si tu la gardes ici, c'est toi que tu gardes. Pas elle. » Daniel regarde "
          "sa fille. Puis les mains de sa mère. Longtemps.", [
            R("Rester immobile, en silence.", 7, "rd2 er2"),
            R("Pleurer, sans bruit.", 7, "er-1 co1"),
            R("« Elle a raison, Monsieur Pittet. »", 7, "pb-2 rd-1"),
            R("Sortir, pour leur laisser ce moment.", 7, "rd2 pb2 co1"),
        ]),
        I(5, "golay", "cold-anger",
          "La Dre Golay vous regarde par-dessus ses lunettes. « Alex. Dehors. » Ce n'est pas "
          "une punition : c'est une évidence. Dans la cour, le soleil se lève sur le gravier. "
          "Par la fenêtre ouverte, vous entendez Océane parler à son père, sans comprendre les "
          "mots.", [
            R("Attendre dans la cour, sans chercher à entendre.", 7, "rd2 pb2 er1"),
            R("Revenir près de la porte, pour écouter.", 7, "pb-2 rd-1"),
            R("Écrire à Yasmine : « je viens de tout gâcher ».", 7, "er1 ic1"),
            R("Partir.", 8, "er-1 co-1"),
        ]),
        I(7, "narr", "",
          "À 9 h, le fourgon de l'institut se gare dans la cour. Daniel sort. Il parle "
          "longtemps avec les deux hommes en costume sombre. Puis il revient vers la cuisine. "
          "Il ne dit rien. Il ouvre la porte en grand, et il la tient. Il ne pleure pas. Il "
          "tient la porte.", [
            R("Rester en retrait, à côté d'Océane.", 9, "rd3 pb1 co1"),
            R("Aider à porter le brancard.", 9, "pb-2 ic1"),
            R("Remercier Daniel, à voix haute.", 9, "pb-1 em1"),
            R("Prendre une photo du fourgon.", 9, "rd-3 pb-3"),
        ]),
        I(8, "narr", "",
          "Vous partez avant 9 h. Le soir, Thierry vous écrit : « Le fourgon est parti à "
          "9 h 20. Daniel a tenu la porte. Océane voulait te le dire elle-même, mais elle n'a "
          "pas ton numéro. C'est mieux comme ça. »"),
        I(9, "daniel", "resigned",
          "Le fourgon disparaît au virage. Daniel s'assied sur le marchepied du tracteur. Il "
          "parle sans vous regarder. « Je ne viendrai pas à votre cérémonie. » Un temps. "
          "« Mais si elle vous a appris quelque chose… faites-en quelque chose. »", [
            R("« Je vous le promets. »", 10, "co2 rd2 er1"),
            R("Lui serrer la main, en silence.", 10, "rd2 em1"),
            R("« Vous avez fait le bon choix. »", 10, "pb-2 em-1"),
            R("S'asseoir à côté de lui, un moment, sans rien dire.", 10, "em1 co2"),
            R("« Vous devriez venir à la cérémonie, quand même : ça vous ferait du bien, et "
              "votre mère l'aurait voulu, j'en suis sûr·e. »", 10, "pb-2 em-1"),
        ]),
        I(10, "oceane", "vulnerable",
          "Océane vous attend près de votre vélo, les yeux gonflés. « Moi, je viendrai. À la "
          "cérémonie. Même si papa ne vient pas. » Elle hésite. « Tu crois qu'ils sauront, "
          "les étudiants, que c'était elle ? »", [
            R("« Non. C'est ce qu'elle voulait. »", END, "cc3 rd2"),
            R("« Je ferai en sorte qu'ils le sachent. »", END, "pb-3 rd-2"),
            R("« Peut-être. Les ongles rouges, ça se remarque, tu sais : moi, en septembre, "
              "c'est la première chose que j'ai vue sur la table. »", END, "pb-2 cc-1"),
            R("« Je ne sais pas. »", END, "cc-1"),
            R("La serrer dans vos bras.", END, "em2 co2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.5 La lettre (et Noah, selon la nuit de mars)
# ---------------------------------------------------------------------------
_LETTRE = (
    "Hier soir, vous avez ouvert l'enveloppe beige. Une feuille de cahier, l'écriture "
    "penchée de Jeannine, datée de septembre, avec des ajouts à l'encre bleue. « Petit, ou "
    "petite — je n'ai jamais su, avec vous, et ça m'est égal. Si vous lisez ceci, c'est que "
    "je suis partie, et que mon corps est chez vous, à la fac. Vous ne le verrez pas : c'est "
    "la règle, et c'est bien. Je voulais vous dire une chose que j'ai apprise en quarante ans "
    "de naissances : on ne soigne jamais un corps. On soigne quelqu'un qui habite dedans, et "
    "ceux qui l'attendent dehors. »"
)
_SIGNATURE = " « Faites-le avec les autres. J. P. »"

# Post-scriptum à l'encre bleue, selon le parcours (le premier qui correspond).
_PS: list[tuple[list[str], str]] = [
    (["revele_a_daniel"], " (À l'encre bleue : « Vous avez dit à Daniel ce que je voulais lui "
     "dire moi-même. J'ai été très en colère. Et puis, ça nous a obligés à parler, lui et moi, "
     "plus tôt que je ne l'aurais fait. Je ne vous remercie pas. Mais je vous pardonne. »)"),
    (["erreur_homonyme"], " (À l'encre bleue : « Le cousin Jean-Paul a su avant mon fils. Ça, "
     "je ne l'oublierai pas. Vous non plus, j'espère : c'est comme ça qu'on apprend. »)"),
    (["oceane_trahie"], " (À l'encre bleue : « Océane m'a raconté, pour la grange. Vous avez "
     "cru bien faire. Une grossesse, c'est à la femme de l'annoncer, à qui elle veut, quand "
     "elle veut. Considérez que c'est mon dernier cours. »)"),
    (["promesse_jeannine"], " (À l'encre bleue : « Vous m'aviez promis que personne ne "
     "saurait jamais. Je savais que c'était impossible, et vous aussi. Ne promettez plus "
     "jamais l'impossible à un malade : il vous croit. »)"),
    (["numero_donne"], " (À l'encre bleue : « Votre numéro, je l'ai gardé sur le frigo "
     "jusqu'à ce que la Dre le remplace par les bons. Vous étiez gentil·le de me le donner, "
     "et c'était une bêtise. Les deux à la fois. »)"),
    (["oceane_orientee"], " (À l'encre bleue : « Merci pour la grange. Océane m'a tout "
     "raconté. Elle a dit : « Il ne m'a pas dit quoi faire », ou « elle », je ne sais plus. "
     "C'est le plus beau compliment qu'on puisse faire à un soignant. »)"),
]
_PS_DEFAUT = " « Vous l'avez fait, avec moi. »"

# Noah, selon la nuit de mars (ch. 4) : nœud d'entrée de la scène.
_NOAH: list[tuple[list[str], int]] = [
    (["noah_seul"], 30),
    (["noah_aide", "mensonge_portfolio"], 31),
    (["noah_aide", "verite_portfolio"], 32),
]
# Noah aidé, sans souvenir du portfolio (chapitre 4 non joué sur cet appareil).
_NOAH_DEFAUT = 33


def _entrees_lettre() -> list[Entry]:
    """Toutes les combinaisons post-scriptum × Noah (le premier point d'entrée qui
    correspond gagne : d'abord le post-scriptum le plus prioritaire, puis Noah)."""
    out: list[Entry] = []
    for flags, ps in _PS:
        intro = _LETTRE + ps + _SIGNATURE
        for nflags, node in _NOAH:
            out.append(Entry(node, when(all=flags + nflags), intro))
        out.append(Entry(_NOAH_DEFAUT, when(all=flags), intro))
    for nflags, node in _NOAH:
        out.append(Entry(node, when(all=nflags), _LETTRE + _PS_DEFAUT + _SIGNATURE))
    return out


S5_5 = S(6, "5.5 La lettre", _LETTRE + _PS_DEFAUT + _SIGNATURE,
    focus=("co", "er", "rd", "pb"),
    entries=_entrees_lettre(),
    nodes=[
        I(33, "noah", "happy",
          "Le lendemain, à l'institut. Dans le couloir du bureau de la Pre Vautier, Noah vous "
          "attend, deux cafés à la main. Il a repris des couleurs. « J'ai appris, pour ta "
          "patiente. Léo me l'a dit. » Il vous tend un café. « En mars, tu ne m'as pas laissé "
          "seul. Je ne te l'ai jamais dit : merci. »", [
            R("« Merci d'être encore là. »", 2, "em2 co2 rd1"),
            R("« Ce n'est rien, n'importe qui l'aurait fait. »", 2, "er1 em-1"),
            R("Le serrer dans vos bras.", 2, "em2 co2"),
            R("« Tu prends toujours ton traitement ? Tu as revu la psychiatre ? »", 2,
              "pb-2 em-1 rd-1"),
            R("« Comment tu vas, toi, depuis mars ? »", 2, "em2 cc1"),
        ]),
        I(32, "noah", "happy",
          "Le lendemain, à l'institut. Dans le couloir du bureau de la Pre Vautier, Noah vous "
          "attend, deux cafés à la main. Il a repris des couleurs. « J'ai appris, pour ta "
          "patiente. Léo me l'a dit. » Il vous tend un café. « En février, tu n'as pas menti "
          "pour moi. J'ai mis du temps à comprendre que c'était ça, être un ami. »", [
            R("« Et toi, tu as dit la vérité. C'était le plus dur. »", 2, "em2 rd2 co1"),
            R("« Tu as eu chaud, quand même. »", 2, "em-1"),
            R("Le serrer dans vos bras.", 2, "em2 co2"),
            R("« Je n'avais pas envie d'avoir des ennuis, surtout : mentir à une commission "
              "d'intégrité, en deuxième année, c'est le meilleur moyen de ne jamais finir ses "
              "études. »", 2, "em-1 rd-1"),
            R("« Comment tu vas, toi, depuis mars ? »", 2, "em2 cc1"),
        ]),
        I(31, "noah", "ashamed",
          "Le lendemain, à l'institut. Dans le couloir du bureau de la Pre Vautier, Noah vous "
          "attend, deux cafés à la main. « J'ai appris, pour ta patiente. » Il vous tend un "
          "café. « Tu as pris un avertissement à cause de moi, en février. Je ne t'avais "
          "jamais dit merci. Ni pardon. »", [
            R("« Les deux sont acceptés. »",
              2, "em2 co2 er1"),
            R("« Tu m'en dois une. »", 2, "em-1 pb-1"),
            R("Prendre le café, sans répondre.", 2, "em-1 co-1"),
            R("« C'est ma faute, pas la tienne. J'ai menti tout seul, personne ne m'y a "
              "obligé·e. »", 2, "pb2 em1"),
            R("« Tu vas mieux ? »", 2, "em2 co1"),
        ]),
        I(30, "leo", "sad",
          "Le lendemain, à l'institut. Dans le couloir, Léo vous montre son téléphone : un "
          "message de Noah, depuis Neuchâtel, où il travaille dans la menuiserie de son "
          "oncle. « dites à alex que je pense à la dame de la ferme ». Léo range son téléphone. "
          "« Il va bien, je crois. Vraiment. »", [
            R("« Tu peux lui dire merci ? Je lui écrirai aussi. »", 2, "em2 ic2 co1"),
            R("« Il aurait pu rester. »", 2, "em-2 co-1"),
            R("« Comment il sait, pour Jeannine ? Qui lui a parlé d'elle ? »", 2,
              "pb1 em-1"),
            R("Hocher la tête, la gorge serrée, en repensant à la nuit de mars, au message de "
              "1 h 07, et à ce que vous auriez pu faire autrement.", 2, "er1 em1"),
            R("« Tant mieux. »", 2, "em1"),
        ]),
        I(2, "vautier", "neutral",
          "La Pre Vautier vous fait asseoir. « La cérémonie d'hommage a lieu dans dix jours. "
          "Chaque année, un étudiant ou une étudiante de deuxième année prend la parole au nom "
          "de sa volée. La table 14 vous a désigné·e. » Elle croise les mains. « La Dre Golay "
          "m'a dit que vous aviez accompagné une donneuse cette année, en stage. Je ne veux pas "
          "savoir qui. Vous ne direz pas qui. Mais je crois que vous avez quelque chose à "
          "dire. Vous acceptez ? »", [
            R("« J'accepte. Sans nom. »", 4, "rd2 pb2 er1"),
            R("« Je ne suis pas sûr·e d'en être capable. »", 5, "er1"),
            R("« J'accepte. Je parlerai de celle que j'ai connue : sa famille sera dans la "
              "salle, ce sera beau, et ça montrera aux autres familles ce que leurs proches "
              "nous ont donné. »", 6, "pb-3 rd-2"),
            R("« Pourquoi moi ? Maëlle parle beaucoup mieux que moi. »", 5, "er-1 ic1"),
            R("« Non. »", 7, "er-1 ic-1"),
        ]),
        I(4, "vautier", "neutral",
          "La Pre Vautier hoche la tête, comme si c'était réglé. « Trois minutes. Pas de nom, "
          "aucun détail qui permette de reconnaître quelqu'un — ni un donneur, ni un patient. Vous parlez à des "
          "familles qui ne savent pas ce qu'on a fait de leurs morts. Dites-leur ce qu'on en a "
          "fait. » Elle sourit, une seconde. « Et ne citez pas l'atlas. »", [
            R("« Ce qu'ils nous ont appris. »", 10, "rd2 co2 cc1 er1"),
            R("« Je dirai aussi qu'on a ri, parfois, et que ce n'était pas toujours bien. »",
              10, "rd1 pb1 cc-1"),
            R("« Je ferai court. »", 10, "cc1"),
            R("« Je peux parler de ma patiente, sans son nom ? Juste son métier, son village, "
              "et ce qu'elle m'a dit dans sa cuisine, en septembre ? »", 10, "pb-2 cc1"),
            R("« Je raconterai l'histoire de la story Instagram : ça fera rire. »",
              10, "rd-3 pb-2"),
        ]),
        I(5, "vautier", "neutral",
          "« C'est exactement pour ça que je vous le demande. » La Pre Vautier pousse vers vous "
          "le livre des donneurs, ouvert à la page de la table 14. « Ceux qui sont sûrs d'en "
          "être capables parlent d'eux-mêmes. Vous, vous parlerez d'eux. »", [
            R("« J'essaierai. Sans nom. »", 4, "rd2 er2 pb1"),
            R("« Je vais y réfléchir, et je vous redis demain. »", 4, "er1"),
            R("« Vous me forcez la main. »", 4, "er-2 rd-1"),
            R("Feuilleter le livre, et accepter d'un signe de tête.", 4, "rd2 er1"),
        ]),
        I(6, "vautier", "cold-anger",
          "La Pre Vautier pose son stylo. « Non. » Un seul mot. Puis : « Cette personne a "
          "donné son corps sans son nom. Comme tous les autres. Sa famille sera peut-être dans "
          "la salle, et elle a le droit de pleurer sans que deux cents personnes se "
          "retournent. Si vous dites son nom, vous lui reprenez ce qu'elle a donné. » Elle "
          "attend. « Alors ? »", [
            R("« Pas de nom. Elle me l'avait demandé. »", 4, "rd3 pb3 er1"),
            R("« Mais c'était une personne extraordinaire. »", 4, "pb-2 rd-1"),
            R("« D'accord. » Sans conviction.", 4, "pb1 er-1"),
            R("« Alors je ne parlerai pas. Je ne vois pas comment dire merci à quelqu'un sans "
              "dire qui il était. »", 7, "er-2 ic-1"),
        ]),
        I(7, "leo", "anxious",
          "En sortant, vous croisez Léo dans le couloir ; il tient trois feuilles, en français "
          "et en allemand, et il a l'air terrifié. « Ils m'ont demandé de parler, si tu "
          "refuses. Je n'y arriverai pas en français. » Il vous regarde. « On le fait à deux ? "
          "Moi en allemand, toi en français ? »", [
            R("« À deux. Et sans nom. »", 8, "ic3 rd1 er1 co1"),
            R("« D'accord. Mais c'est toi qui commences. »", 8, "ic1 er1"),
            R("« Débrouille-toi, Léo. »", 12, "ic-3 em-2"),
            R("« Je ne sais pas… Bon. D'accord. »", 8, "er-1"),
        ]),
        I(8, "vautier", "neutral",
          "Vous retournez ensemble frapper à la porte du bureau 112. La Pre Vautier lève les "
          "yeux, voit Léo et ses trois feuilles, et ne pose aucune question. « À deux, alors. "
          "Vous en français, lui en allemand. »", [go(4)]),
        I(12, "narr", "",
          "Léo vous regarde, puis baisse les yeux. « D'accord. » Il s'en va sans se retourner, "
          "ses trois feuilles à la main. Le soir, vous ne dormez pas. À 7 h, vous écrivez à la "
          "Pre Vautier, Léo en copie : « Si l'offre tient toujours, je parlerai. Avec Léo, s'il "
          "veut encore de moi. » Léo répond le premier : « ok. merci. » À 8 h, vous êtes tous "
          "les deux devant le bureau 112.", [go(4)]),
        I(10, "narr", "",
          "Le soir, chez vous, vous relisez la lettre. Puis vous ouvrez Instagram. Votre pouce "
          "reste au-dessus du bouton « Partager ». Sur l'écran : l'écriture penchée de "
          "Jeannine, et votre propre reflet. Vous pensez à une hirondelle sur un drap blanc.", [
            R("Supprimer le brouillon.", 11, "rd3 pb2 er1"),
            R("Publier, en « amis proches » seulement : c'est une belle lettre, et ceux qui "
              "vous connaissent comprendront ce que cette année a été.", 9, "rd-3 pb-3"),
            R("La garder en brouillon, « pour plus tard ».", 11, "pb-1 rd-1"),
            R("L'envoyer à Maëlle, pour avoir son avis.", 11, "pb-2 rd-2"),
            R("Appeler Yasmine, ou Léo, pour ne pas rester seul·e ce soir.", 11, "er2 ic2"),
        ]),
        I(9, "oceane", "angry",
          "Une heure plus tard, un message d'Océane, avec la capture d'écran qu'on lui a "
          "envoyée du village : « Supprime ça. Tout de suite. C'est la lettre de mamie. »", [
            R("Supprimer. « Pardon. »", 11, "rd2 pb1 er1 em1"),
            R("« C'est ma lettre, c'est elle qui me l'a écrite. »", 11, "rd-2 em-2"),
            R("Supprimer, sans répondre.", 11, "pb1 em-1"),
            R("« Je voulais lui rendre hommage, Océane : tout le monde a trouvé ça beau, il "
              "y a déjà quarante cœurs. »", 11, "pb-2 em-1"),
        ]),
        I(11, "narr", "",
          "Vous rangez la lettre dans votre carnet de stage, entre la page de septembre et "
          "celle de juin."),
    ],
)

# ---------------------------------------------------------------------------
# 5.6 La cérémonie (puis le dernier jour du cabinet, en septembre)
# ---------------------------------------------------------------------------
_INTRO_56 = (
    "Fin juin, 17 h. L'aula de l'institut d'anatomie, des fleurs blanches, un quatuor "
    "d'étudiants. Au premier rang, les familles des donneuses et des donneurs de l'année. "
    "Derrière, toute la volée de deuxième année. La Pre Vautier ouvre la cérémonie. Dans "
    "cinq minutes, ce sera à vous."
)

S5_6 = S(7, "5.6 La cérémonie", _INTRO_56,
    focus=("rd", "co", "pb", "er"),
    entries=[
        Entry(20, when(all=["rencontre_rapin"]), _INTRO_56),
        Entry(30, when(all=["photo_virale"]), _INTRO_56),
    ],
    debriefs=[
        Debrief(when(all=["nom_prononce"]), tone="hard", lead=(
            "Vous avez dit le nom de Jeannine, devant sa petite-fille et devant le village. "
            "Elle avait donné son corps sans son nom, comme tous les autres, et elle vous "
            "l'avait demandé : « Pour tous. Pas pour moi. » L'anonymat des donneurs n'est pas "
            "une froideur administrative : c'est ce qui permet à chaque famille de pleurer "
            "sans être regardée, et à chaque don d'être égal aux autres.")),
        Debrief(when(none=["nom_prononce"]), tone="good", lead=(
            "Vous avez parlé pour tous, sans un nom, sans un détail qui permette de "
            "reconnaître quelqu'un — et pourtant, chacun dans la salle a pu y reconnaître les "
            "siens. C'est la forme la plus difficile de la gratitude : remercier des gens "
            "qu'on ne connaîtra jamais, et qui ne l'entendront pas.")),
    ],
    nodes=[
        I(40, "narr", "",
          "Au troisième rang, une femme d'une cinquantaine d'années porte une broche en forme "
          "d'hirondelle au revers de son manteau gris. Vous ne la connaissez pas. Vous comprenez quand même.", [
            R("Ne rien faire de ce que vous croyez savoir, et monter sur l'estrade.",
              1, "pb3 rd2"),
            R("Aller lui parler avant la cérémonie : « Je crois que j'ai connu votre "
              "mère. »", 1, "pb-3 rd-2 em1"),
            R("Fixer la broche, incapable de penser à autre chose.", 1, "er-2"),
            R("Chercher Maëlle des yeux, pour savoir si elle a vu la broche, elle aussi, et "
              "si elle a compris la même chose que vous.", 1, "ic1 er-1"),
        ]),
        I(20, "rapin", "neutral",
          "Au troisième rang, une femme en manteau gris, une broche en forme d'hirondelle au "
          "revers : Mme Rapin. Elle vous a reconnu·e. Elle vous fait un petit signe de tête, "
          "comme on encourage quelqu'un avant de monter sur scène.", [
            R("Hocher la tête.", 1, "rd2 er1 co1"),
            R("Détourner les yeux.", 1, "er-1 rd-1"),
            R("Aller lui parler avant de monter, pour lui dire ce que vous allez dire, et lui "
              "demander si elle est d'accord.", 1, "pb-1 em1"),
            R("Lui sourire, et respirer.", 1, "er2 rd1"),
        ]),
        I(30, "narr", "",
          "Au troisième rang, une femme en manteau gris porte une broche en forme d'hirondelle. "
          "Vous ne l'avez jamais vue. Vous savez qui elle est.", [
            R("Ne rien faire de ce que vous savez, et monter sur l'estrade.", 1, "pb3 rd2"),
            R("Aller lui présenter des excuses, avant la cérémonie, au nom de la table 14, "
              "pour la story de septembre.", 1, "pb-2 em1"),
            R("Fixer la broche, incapable de penser à autre chose.", 1, "er-2"),
            R("Chercher Maëlle des yeux.", 1, "ic1"),
        ]),
        I(1, "narr", "",
          "Vous montez sur l'estrade. Deux cents visages. Au premier rang, Océane, une main "
          "posée sur son ventre arrondi, vous regarde. Vous dépliez votre feuille. Vos mains "
          "tremblent comme en septembre, devant le premier drap blanc.", [
            R("Commencer par les mots lus en septembre : « … nos premiers maîtres, sans jamais "
              "nous entendre les remercier. » Puis : « Aujourd'hui, nous vous remercions. »",
              2, "rd3 cc2 er1"),
            R("Commencer par une blague, pour détendre la salle.", 3, "rd-2 er-1"),
            R("Lire la feuille d'une traite, sans lever les yeux.", 2, "cc-1 er1"),
            R("Commencer par l'histoire de Jeannine, sans son nom : le village, la ferme, les "
              "six cents enfants.", 4, "pb-3 rd-2 cc1"),
            R("Commencer par « Pardon », au nom de la table 14.", 2, "rd2 pb2 cc1"),
        ]),
        I(2, "narr", "",
          "Vous parlez des mains, des cœurs qui ont tenu, de ce qu'on apprend d'un corps qu'on "
          "ne verra jamais vivant. Vous parlez de ceux qui en avaient pris soin jusqu'au bout. "
          "La salle est silencieuse. Au moment de conclure, la phrase que vous n'aviez pas "
          "écrite vient toute seule : le nom de Jeannine, ses six cents enfants, la ferme des "
          "Combettes. Elle est là, sur vos lèvres.", [
            R("La garder pour vous. « Nous ne connaîtrons jamais vos noms. Nous n'oublierons "
              "jamais ce que vous nous avez appris. Merci. »", 5, "rd3 pb3 co2 cc1"),
            R("La dire : « Elle s'appelait Jeannine. »", 6, "pb-3 rd-3 co-1",
              sets=["nom_prononce"]),
            R("Dire, sans aucun nom : « Cette année, j'ai aussi connu une donneuse vivante. "
              "Elle m'a appris à soigner quelqu'un, pas un corps. »", 5, "pb1 co2 cc1"),
            R("Se taire, longtemps, puis : « Merci. »", 5, "rd2 er1"),
        ]),
        I(3, "narr", "",
          "Personne ne rit. Au premier rang, une dame âgée baisse la tête. La Pre Vautier ne "
          "bouge pas. Vous avez trois minutes, et vous venez d'en perdre une.", [
            R("S'arrêter. « Pardon. Je recommence. »", 2, "rd2 er2 cc1"),
            R("Continuer, comme si de rien n'était.", 2, "er-1"),
            R("Faire une deuxième blague, pour rattraper la première, en vous moquant de "
              "vous-même cette fois, pour que la salle comprenne que c'était involontaire.",
              2, "rd-2 er-2"),
            R("Lire la suite très vite.", 2, "cc-1 er-1"),
        ]),
        I(4, "narr", "",
          "Au premier rang, Océane se raidit. Dans la salle, deux ou trois personnes de "
          "Montchéry échangent un regard : une sage-femme, une ferme, six cents enfants. La "
          "Pre Vautier se soulève à moitié de sa chaise.", [
            R("S'interrompre : « Pardon. Ce qu'elle m'a appris, c'est pour vous tous. » Puis "
              "revenir à tous les donneurs.", 2, "pb2 rd2 er1"),
            R("Continuer, en ajoutant son prénom.", 6, "pb-3 rd-3", sets=["nom_prononce"]),
            R("Accélérer, pour finir vite.", 2, "er-1 cc-1"),
            R("Regarder Océane, et ne plus savoir quoi dire.", 2, "er-1"),
        ]),
        I(5, "narr", "",
          "Un silence. Pas d'applaudissements : c'est la règle, ici. Quelqu'un, au premier "
          "rang, se lève ; puis tout le monde. Une minute de silence, que Léo annonce en trois "
          "langues, comme il l'avait proposé en septembre : « Danke. Merci. Grazie. » Vous "
          "redescendez de l'estrade.", [go(7)]),
        I(6, "narr", "",
          "Le nom tombe dans le silence. Au premier rang, Océane porte les mains à sa bouche. "
          "Des têtes se tournent vers elle. Quelqu'un chuchote « la sage-femme de "
          "Montchéry ». La Pre Vautier se lève, vient jusqu'à l'estrade et dit doucement, au "
          "micro : « Merci, Alex. » Elle termine à votre place.", [
            R("Descendre, et aller s'excuser auprès d'Océane, à voix basse.", 8,
              "rd2 pb1 er1 co1"),
            R("Descendre, et quitter la salle.", 8, "er-2 rd-1"),
            R("Ajouter, au micro : « Elle le méritait. »", 8, "pb-2 er-1"),
            R("Rester sur l'estrade, figé·e.", 8, "er-2"),
        ]),
        I(7, "oceane", "happy",
          "Après la cérémonie, les familles déposent des fleurs blanches devant le livre des "
          "donneurs. Océane vient vers vous. Elle sourit, les yeux rouges. « C'était bien. "
          "Elle aurait dit : « Pas mal, pour la fac. » » Puis, plus bas : « Si c'est une fille, "
          "je l'appellerai Jeanne. »", [
            R("« Elle aurait aimé. » Et ne rien ajouter.", 9, "em2 co2 rd1"),
            R("« Et si c'est un garçon ? » En souriant.", 9, "em2"),
            R("« Tu as décidé de le garder, alors ? »", 9, "pb-2 rd-1"),
            R("La serrer dans vos bras.", 9, "em1 co2"),
            R("« Tu en as parlé à ton père ? Il faudrait, maintenant que tu as décidé : il "
              "va bientôt le voir, de toute façon. »", 9, "pb-2 em-1"),
        ]),
        I(8, "oceane", "cold-anger",
          "Océane vous attend devant la porte. Elle ne crie pas. « Mamie l'a donné sans son "
          "nom. Comme les autres. Toute sa vie, elle a laissé les autres sur le devant de la "
          "scène. » Elle tient son ventre. « Tu lui as repris ça. »", [
            R("« Tu as raison. »", 9, "rd2 pb2 er1"),
            R("« Je voulais lui rendre hommage. »", 9, "pb-2 em-1"),
            R("Baisser les yeux.", 9, "er-1"),
            R("« Personne ne fera le lien : il y avait deux cents personnes, et la plupart ne "
              "connaissent pas Montchéry. »", 9, "pb-3 cc-2"),
        ]),
        I(9, "vautier", "neutral",
          "La salle se vide. La Pre Vautier range le livre des donneurs dans sa housse. « Vous "
          "savez ce que j'aime, dans cette cérémonie ? Elle ne sert à rien. Les morts "
          "n'entendent pas. » Elle referme la housse. « Elle sert aux vivants. Aux familles, à "
          "vous, à moi. On y apprend à remercier quelqu'un qu'on ne connaîtra jamais. C'est "
          "peut-être la chose la plus médicale que je vous aie apprise. »", [go(50)]),
        I(50, "golay", "melancholic",
          "Fin septembre. Le dernier jour du cabinet de Montchéry. Des cartons partout ; la "
          "plaque déjà dévissée, posée contre le mur. Vous êtes en troisième année, "
          "maintenant ; vous avez demandé à venir aider. La Dre Golay décroche le dernier "
          "cadre : un dessin d'enfant, une maison, un soleil, une femme en blouse. « Mon fils, "
          "à cinq ans. Jeannine l'a mis au monde. » Elle le range. « Vingt-cinq ans. Tout tient "
          "dans onze cartons. » Elle vous regarde. « Et vous, qu'est-ce que vous emportez de "
          "cette année ? »", [
            R("« Qu'on soigne quelqu'un qui habite un corps, et ceux qui l'attendent "
              "dehors. »", 51, "er2 co2 rd2 cc1"),
            R("« Une date de naissance avant chaque phrase au téléphone. « Pause réelle » au "
              "fond de la gorge. Et une lettre, dans mon carnet. »", 51, "er2 cc2 rd1"),
            R("« De bons souvenirs. »", 51, "cc-1"),
            R("« Je ne sais pas encore. »", 51, "er1"),
            R("« Surtout que je ne veux plus jamais faire la moindre erreur. »",
              51, "er-2 cc-1"),
        ]),
        I(51, "sandra", "happy",
          "Sandra vous tend un post-it jaune, à moitié décollé, le bord gondolé : « PITTET J. = "
          "2 ! DATE DE NAISSANCE ! » « Il était collé sur mon écran depuis octobre. Prends-le. "
          "Colle-le partout où tu iras. »", [
            R("« Partout. » Et le ranger dans le carnet, à côté de la lettre.", 52,
              "ic2 em2 er1"),
            R("« Je n'en ai plus besoin, j'ai compris. »", 52, "ic-1 er-1"),
            R("Rire, et serrer Sandra dans vos bras.", 52, "em2 ic1 co1"),
            R("« C'est un peu ridicule, non ? »", 52, "ic-2 rd-1"),
            R("« Garde-le, toi. Tu en auras besoin à Orbe. »",
              52, "ic1 em1"),
        ]),
        I(52, "golay", "melancholic",
          "La Dre Golay ferme la porte du cabinet à clé, pour la dernière fois. Elle tend la "
          "clé à Sandra, qui la rendra à la commune. Puis elle se tourne vers vous, sur le "
          "trottoir. « J'accueille des étudiants depuis vingt ans. Vous êtes le dernier, ou la "
          "dernière. » Un temps. « Tu reviendras, toi ? » C'est la première fois qu'elle vous "
          "tutoie.", [
            R("« Je ne sais pas. Mais je n'oublierai jamais ce cabinet. »", 54,
              "er2 rd2 cc1"),
            R("« Oui ! Promis. »", 54, "pb-2 er1"),
            R("« Et vous, vous allez faire quoi, maintenant ? »", 53, "em2 cc1"),
            R("Lui serrer la main, longtemps, sans répondre.", 54, "rd2 em1"),
            R("« Sûrement pas. C'est trop dur, la campagne : les gardes, la solitude, et "
              "personne pour reprendre le cabinet quand on veut partir. »", 54, "rd-2 em-1"),
        ]),
        I(53, "golay", "happy",
          "« Moi ? » Elle rit. « Je vais apprendre à ne rien faire. Ça va être très difficile. » "
          "Elle regarde la rue. « Et le jeudi, j'irai donner un coup de main au centre de santé "
          "d'Orbe. Une demi-journée. On ne se refait pas. »", [go(54)]),
        I(54, "narr", "",
          "Vous prenez le bus de Montchéry une dernière fois. Au premier virage, on voit les "
          "Combettes : la cour, la grange, la fenêtre de la cuisine. Quelqu'un l'a laissée "
          "ouverte. Dans votre carnet, entre la page de septembre et celle de juin, il y a une "
          "lettre, un post-it jaune, et le dessin de trois pontages, avec, au crayon, "
          "dessous : « Elle a tenu. »"),
    ],
)

CH5 = C(5, "Le corps donné",
    situation=(
        "Mai et juin, puis septembre. Une réunion de famille autour de la toile cirée, un "
        "secret dans la grange, l'examen de fin d'année et un téléphone qui sonne pendant la "
        "pause. La dernière visite aux Combettes, une enveloppe « à ouvrir après », un "
        "fourgon dans la cour. Et la cérémonie d'hommage aux donneurs, où c'est vous qui "
        "parlez."
    ),
    objectives=(
        "rester à sa place dans une réunion de famille, et rapporter fidèlement les mots d'une "
        "patiente quand elle le demande ; respecter le secret confié par une mineure capable "
        "de discernement et l'orienter sans décider à sa place ; décider sous la pression "
        "émotionnelle en vérifiant d'abord la réalité de l'urgence et la volonté de la "
        "personne ; accompagner une fin de vie à domicile sans prendre la place de la famille "
        "ni de l'équipe de soins palliatifs ; respecter la volonté d'une donneuse et la place "
        "de sa famille au moment du départ du corps ; recevoir une critique et un pardon ; "
        "parler en public au nom de sa volée en respectant l'anonymat des donneuses et des "
        "donneurs ; dire ce qu'on emporte d'une année de formation."
    ),
    anchoring=(
        "UNIL BMed2.6 (urogénital et homéostasie : filtration glomérulaire, hormones de la "
        "reproduction), BMed2.10 (fin des travaux pratiques d'anatomie) et BMed2.7 · UNIGE "
        "Excrétion et homéostasie, Reproduction, dimensions communautaires (éthique), "
        "identité professionnelle · UZH Humanbiologie II (Niere, Reproduktion), Praktikum "
        "klinische Anatomie II · dans les trois facultés : cérémonie d'hommage aux "
        "donneuses et aux donneurs du corps."
    ),
    focus=("co", "rd", "pb", "er"),
    start_choice=StartChoice(
        unless_any=["noah_aide", "noah_seul"],
        question=(
            "Ce chapitre fait suite à la nuit de mars où Noah a écrit à Alex (chapitre 4), "
            "que vous n'avez pas jouée sur cet appareil. Que s'est-il passé cette nuit-là ?"
        ),
        options=[
            ("Alex ne l'a pas laissé seul : Noah a passé quelques jours à l'hôpital, et il "
             "est revenu à la fac.", ["noah_aide"]),
            ("Alex s'est rendormi·e : Noah a été retrouvé au matin, et il a quitté la "
             "médecine.", ["noah_seul"]),
        ],
    ),
    scenes=[S5_1, S5_2, S5_3, S5_4A, S5_4B, S5_5, S5_6],
)
