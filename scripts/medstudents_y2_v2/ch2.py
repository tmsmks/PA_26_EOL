"""Chapitre 2 — Deux Pittet (octobre-novembre).

Cinq scènes jouées, six ou sept écrites :
  2.1 Le jour des vaccins · 2.2 Le téléphone · 2.3 L'APP du jeudi
  2.4 branche parallèle : « Le Café de la Gare » (Alex a appelé le mauvais Pittet)
      ou « La créatinine »
  2.5 Le dimanche aux Combettes
  2.6 histoire annexe « Léo » (si Alex a inclus Léo au tutorat)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 2.1 Le jour des vaccins
# ---------------------------------------------------------------------------
S2_1 = S(1, "2.1 Le jour des vaccins",
    "Jeudi, fin octobre. Journée de vaccination contre la grippe au cabinet de Montchéry : "
    "quarante rendez-vous, une file jusque sur le trottoir, Sandra au bord de l'implosion. "
    "La Dre Golay vaccine à la chaîne dans la salle 1. Dans la salle 2 attendent une jeune "
    "mère et son bébé de deux mois, pour le contrôle et les premiers vaccins.",
    focus=("cc", "rd", "em"),
    nodes=[
        I(1, "golay", "neutral",
          "La Dre Golay vous attrape au passage, une seringue dans chaque main. « Alex, vous "
          "commencez avec Mme Duc, en salle 2 ? Comment va le bébé, l'alimentation, le "
          "sommeil. Elle a des questions sur les vaccins : écoutez, ne promettez rien. Je "
          "reviens dans dix minutes. » Elle repart vers la salle 1.", [
            R("« D'accord. J'écoute ses questions, je les note, et je ne réponds pas à votre "
              "place sur les vaccins. »", 2, "pb3 ic2 cc1"),
            R("« Je peux lui expliquer moi-même, on a eu le cours d'immunologie. »",
              2, "pb-2 ic-1"),
            R("« Je préférerais attendre que vous soyez là. »", 2, "pb1 ic-1 em-1"),
            R("« Qu'est-ce qu'elle a comme questions, à peu près ? »", 2, "ic2 cc1"),
            R("Hocher la tête sans rien dire.", 2, "ic-1"),
        ]),
        I(2, "duc", "anxious",
          "Salle 2. Une jeune femme, un bébé endormi contre elle, un sac à langer qui "
          "déborde. Elle parle vite. « Bonjour. Coralie. Lui, c'est Elio, il a deux mois. » "
          "Elle sort son téléphone. « J'ai lu des trucs. L'aluminium, les vaccins à six "
          "maladies d'un coup, l'autisme. Six maladies à deux mois, ça fait beaucoup, "
          "non ? »", [
            R("« Vous avez beaucoup lu, et ça vous inquiète. Qu'est-ce qui vous fait le plus "
              "peur, dans tout ça ? »", 3, "em3 cc2 rd1"),
            R("« L'histoire de l'autisme, c'est une fraude. Ça a été démontré. »",
              4, "cc1 rd-2 em-2 pb-1"),
            R("« Les gens qui écrivent ça sur internet ne sont pas médecins. »",
              4, "rd-2 em-2 cc-1"),
            R("« Moi, je suis étudiant·e, je ne peux pas vous conseiller. Attendez la "
              "Dre. »", 5, "pb2 em-2 cc-1"),
            R("« Ce sont de vraies questions. Je vais noter tout ce qui vous inquiète, pour "
              "que la Dre puisse vous répondre point par point. »", 3, "cc2 pb2 em2 ic1"),
            R("Lui montrer sur votre téléphone les chiffres de couverture vaccinale de "
              "l'OFSP.", 4, "cc-1 em-1 pb-1"),
        ]),
        I(3, "duc", "vulnerable",
          "Elle caresse la tête du bébé. « Ma sœur a un garçon autiste. Il avait quinze mois "
          "quand il a arrêté de parler. Juste après un vaccin. » Un temps. « Tout le monde me "
          "dit que ça n'a rien à voir. Personne ne nous a jamais dit pourquoi il avait "
          "arrêté de parler, alors. »", [
            R("Laisser un silence. « Personne ne vous a jamais expliqué ce qui est arrivé à "
              "votre neveu. Et vous avez peur que ça arrive à Elio. »", 6, "em3 co2 cc1"),
            R("« C'est une coïncidence de calendrier : l'autisme se manifeste souvent à cet "
              "âge-là. »", 6, "cc2 em-1 pb-1"),
            R("« Je comprends. Moi aussi, je serais méfiant·e. »", 6, "pb-2 cc-2 em1"),
            R("« Ça doit être dur, pour votre sœur. Et pour vous. »", 6, "em2 co2"),
            R("« Vous voulez que je demande à la Dre Golay de vous expliquer ce qu'on sait, "
              "justement, sur ce lien ? »", 6, "cc2 ic2 em1 pb1"),
        ]),
        I(4, "duc", "angry",
          "Coralie se raidit. Elio se réveille et se met à pleurer. « Super. Encore quelqu'un "
          "qui me prend pour une idiote. » Elle range son téléphone. « Je vais attendre la "
          "Dre, merci. »", [
            R("« Vous avez raison, j'ai répondu trop vite, et à côté. Pardon. Qu'est-ce qui "
              "vous inquiète le plus ? »", 3, "rd2 em2 er1 cc1"),
            R("« Je vous donnais juste les faits. »", 7, "er-1 em-1"),
            R("Se taire, et regarder le bébé qui pleure.", 7, "er1"),
            R("« Si vous ne le faites pas vacciner, c'est lui qui en paiera le prix. »",
              7, "rd-3 em-3 pb-2"),
            R("Lui proposer un verre d'eau : « Je vous laisse tranquille. Je dis à la Dre "
              "que vous avez des questions. »", 7, "rd1 ic1 cc1"),
        ]),
        I(5, "duc", "sad",
          "« Ah. » Elle baisse les yeux sur le bébé. « Tout le monde me renvoie à quelqu'un "
          "d'autre. » Un silence s'installe. Elio tète son poing.", [
            R("« Pardon, je me suis mal exprimé·e. Je ne peux pas décider à la place de la "
              "Dre, mais je peux vous écouter. Racontez-moi. »", 3, "em2 rd2 pb1 cc1"),
            R("Remplir le formulaire de prévention, en silence.", 7, "em-2"),
            R("« Elle ne va pas tarder. »", 7, "em-1"),
            R("« Il a l'air en pleine forme, Elio. Il dort bien ? »", 3, "em1 cc1 rd1"),
            R("« Ce n'est pas moi qui ai fait les vaccins, je n'y peux rien. »",
              7, "em-2 rd-1 cc-1"),
        ]),
        I(6, "golay", "neutral",
          "La Dre Golay revient, essoufflée, et s'assied. « Alors ? » Coralie vous regarde. "
          "La Dre aussi : c'est à vous de résumer.", [
            R("« Mme Duc a des questions sur les vaccins d'Elio : l'aluminium, le nombre de "
              "vaccins, et surtout l'autisme — son neveu a cessé de parler à quinze mois, "
              "juste après un vaccin, et personne ne lui a jamais expliqué pourquoi. »",
              8, "cc3 ic2 rd2 em2"),
            R("« Elle est contre les vaccins. »", 9, "rd-3 cc-2 em-1"),
            R("« Elle a des questions. Je lui ai dit que tout ça, c'étaient des fake "
              "news. »", 9, "cc-1 rd-2 pb-1"),
            R("« Je préfère qu'elle vous le dise elle-même. »", 8, "rd1 ic-1"),
            R("« Elle a peur, je crois. Pour Elio. »", 8, "em2 cc1"),
        ]),
        I(7, "golay", "neutral",
          "La Dre Golay revient. Elle regarde Coralie, les yeux rouges, le bébé qui pleure, "
          "puis vous. « Alex, vous pouvez aller aider Sandra au comptoir ? Je prends la "
          "suite. »", [
            R("Avant de sortir : « Mme Duc a des questions importantes. Je crois que je l'ai "
              "brusquée, et je m'en excuse. »", 10, "pb2 rd2 ic2 er1"),
            R("Sortir sans un mot.", 10, "ic-1 er-1"),
            R("« Elle refuse les vaccins. »", 10, "rd-3 cc-2"),
            R("« Je lui ai juste donné les faits. »", 10, "er-1 ic-1 pb-1"),
            R("« D'accord. » Et se promettre de demander plus tard à la Dre comment elle s'y "
              "prend.", 10, "er1 ic1"),
        ]),
        I(8, "golay", "happy",
          "La Dre Golay se tourne vers Coralie. Elle ne sort ni brochure ni statistique. "
          "« Votre neveu, il a quel âge, maintenant ? » Pendant vingt minutes, elle parle de "
          "l'autisme, des premiers signes, de ce qu'on sait et de ce qu'on ne sait pas. Puis "
          "de la coqueluche, qu'Elio pourrait attraper dans la file de la Migros. Coralie "
          "pose ses questions une par une. À la fin : « Je peux réfléchir une semaine ? — "
          "Bien sûr. Revenez quand vous voulez, sans rendez-vous. » Quand la porte se "
          "referme, la Dre vous regarde. « Qu'est-ce que vous avez vu ? »", [
            R("« Vous ne l'avez jamais contredite. Vous avez répondu à sa peur, pas à "
              "internet. »", 11, "cc2 rd2 er1"),
            R("« Qu'elle ne l'a pas fait vacciner. C'est un échec, non ? »", 11, "rd-1 er-1"),
            R("« Vous êtes restée vingt minutes, alors que la file va jusqu'à la Migros. »",
              11, "ic2 cc1"),
            R("« Qu'elle a le droit de réfléchir, et que vous le lui avez dit. »",
              11, "rd3 pb1 cc1"),
            R("« Que ça prend trop de temps, pour un cabinet comme le vôtre. »",
              11, "rd-1 ic-1"),
        ]),
        I(9, "golay", "cold-anger",
          "La Dre Golay ne vous répond pas. Elle se tourne vers Coralie, qui a entendu. « Je "
          "ne vous mets dans aucune case, Madame Duc. Racontez-moi. » Plus tard, dans le "
          "couloir : « Alex. Un mot, et une maman ne revient plus jamais. Les étiquettes, on "
          "les laisse aux pots de confiture. »", [
            R("« Vous avez raison. J'ai résumé sa peur en un mot. C'était injuste. »",
              11, "rd2 er2 pb1"),
            R("« Mais elle était vraiment contre. »", 11, "rd-2 er-1"),
            R("« Je voulais vous faire gagner du temps. »", 11, "ic1 rd-1"),
            R("Hocher la tête, rouge jusqu'aux oreilles.", 11, "er1"),
            R("« Je m'excuserai auprès d'elle, si elle revient. »", 11, "rd2 pb1 em1"),
        ]),
        I(10, "sandra", "neutral",
          "Au comptoir, Sandra vous tend une pile de dossiers. « Tu tombes bien, le téléphone "
          "ne s'arrête pas. » Elle vous regarde par-dessus ses lunettes. « T'inquiète. La "
          "Dre rattrape toujours. Toujours. »", [go(11)]),
        I(11, "golay", "neutral",
          "18 h. Quarante vaccins, deux malaises, un chien qui a mordu le facteur. La Dre "
          "Golay se masse la nuque. « La moitié de la médecine de famille, c'est ça : des gens "
          "qui ont peur et qui ont lu des choses. On ne gagne jamais contre internet. On gagne "
          "contre la peur, un patient à la fois. » Elle éteint l'ordinateur. « Coralie "
          "reviendra. Ou pas. Ce sera son choix, et on l'aura respecté. »", [
            R("« Et si elle ne revient pas, et qu'Elio attrape la coqueluche ? »",
              END, "em1 cc1 er1"),
            R("« J'ai appris plus aujourd'hui qu'en trois semaines d'immunologie. »",
              END, "er1 rd1 cc1"),
            R("« Moi, je l'aurais obligée. »", END, "rd-3 pb-2"),
            R("« Comment vous faites pour ne jamais vous énerver ? »", END, "er2 ic1"),
            R("« Merci de m'avoir laissé·e seul·e avec elle. J'ai vu ce que je ne savais pas "
              "encore faire. »", END, "er2 pb2 ic1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 2.2 Le téléphone
# ---------------------------------------------------------------------------
S2_2 = S(2, "2.2 Le téléphone",
    "Deux semaines plus tard. Jeudi, 16 h 20. Les résultats de laboratoire de la semaine "
    "sont arrivés d'un coup. La Dre Golay est en visite à domicile ; Sandra a six personnes "
    "au comptoir et le téléphone qui sonne sans arrêt.",
    focus=("pb", "cc", "ic"),
    debriefs=[
        Debrief(when(all=["info_lachee"]), tone="hard", lead=(
            "Vous avez appelé le mauvais Pittet, puis vous lui avez parlé de la santé de "
            "Jeannine. Au téléphone, la règle tient en une ligne : vérifier l'identité — "
            "nom, prénom, date de naissance — avant de dire quoi que ce soit, et ne donner "
            "aucun résultat. Le secret médical vaut pour les voisins, les cousins et les "
            "fils, et il vaut aussi pour les étudiant·e·s (art. 321 du Code pénal).")),
        Debrief(when(all=["erreur_homonyme"]), tone="hard", lead=(
            "Vous avez appelé le mauvais Pittet et confirmé que l'appel concernait Jeannine. "
            "Même sans détail, dire à un tiers qu'une patiente a des résultats à discuter, "
            "c'est déjà révéler quelque chose. Deux homonymes dans un logiciel : la seule "
            "protection, c'est la date de naissance, vérifiée avant de parler.")),
        Debrief(when(all=["appel_rattrape"]), tone="mixed", lead=(
            "Vous avez composé le mauvais numéro, et vous vous êtes arrêté·e à temps. C'est "
            "un quasi-incident : il ne s'est presque rien passé, et c'est justement pour ça "
            "qu'il faut le dire. Ce qui l'a rendu possible — deux « Pittet J. », un post-it "
            "sans date de naissance, une file de six personnes — recommencera demain.")),
        Debrief(when(all=["bon_pittet"]), tone="good", lead=(
            "Vous avez appelé la bonne Pittet. Au téléphone : vérifier l'identité avant de "
            "parler, ne donner aucun résultat, transmettre fidèlement ce que la patiente "
            "demande de transmettre — ici, son refus de la dialyse, qui appartient à "
            "l'entretien avec la Dre Golay.")),
    ],
    nodes=[
        I(1, "sandra", "anxious",
          "Sandra vous tend un post-it sans lever les yeux de son écran. « Rappelle Pittet, "
          "s'il te plaît. La Dre veut la voir lundi pour ses résultats. Le numéro est dans le "
          "dossier. » Le post-it dit : « Pittet — résultats — RDV lundi Dre ». Rien "
          "d'autre.", [
            R("« Quel Pittet ? Il y en a plusieurs au village, non ? Tu as une date de "
              "naissance ? »", 2, "pb3 cc2 ic2"),
            R("« D'accord. » Ouvrir le logiciel et taper « Pittet ».", 3, "pb-1"),
            R("« Je n'ai pas le droit de téléphoner aux patients, si ? »", 4, "pb1 ic-1"),
            R("« Qu'est-ce que je dis, si on me demande les résultats ? »", 5, "pb2 cc2 ic1"),
            R("« Je fais ça après ma pause. »", 3, "ic-2 rd-1"),
        ]),
        I(2, "sandra", "grateful",
          "Sandra fouille la pile de fax du laboratoire. « Pittet J., 81 ans. Créatinine en "
          "hausse, la Dre veut la voir lundi. » Elle souffle. « Jeannine. Pas Jean-Paul. "
          "J'allais te faire appeler le mauvais. Des Pittet, ici, il y en a onze. » Elle "
          "vous tend le fax. « Le rendez-vous, et rien d'autre au téléphone. C'est la Dre qui "
          "explique. »", [go(6)]),
        I(3, "narr", "",
          "Vous tapez « Pittet ». Onze résultats. Deux « Pittet J. » ont eu une prise de sang "
          "cette semaine : Pittet Jean-Paul, né en 1967, et Pittet Jeannine, née en 1944. Le "
          "fax du laboratoire, sur le comptoir, dit seulement « Pittet J. — créatinine en "
          "hausse — convoquer ». Le premier de la liste est Jean-Paul.", [
            R("Comparer avec le fax : l'âge est noté en petit, 81 ans. Ouvrir le dossier de "
              "Jeannine.", 6, "pb3 cc2"),
            R("Ouvrir le premier de la liste et composer le numéro.", 7, "pb-2 cc-1"),
            R("Demander à Sandra : « Pittet J., c'est Jean-Paul ou Jeannine ? »",
              2, "pb2 ic2 cc1"),
            R("Appeler les deux : on verra bien qui a fait une prise de sang.",
              7, "pb-3 cc-2"),
            R("Rendre le post-it à Sandra : vous ne savez pas qui appeler.", 2, "pb1 ic1 cc-1"),
        ]),
        I(4, "sandra", "annoyed",
          "« Prendre un rendez-vous, oui. Donner des résultats, non. » Elle vous tend le "
          "combiné. « Tu dis : la Dre aimerait vous voir lundi pour discuter de vos résultats. "
          "Et rien d'autre. Tu t'en sors ? »", [
            R("« Oui. Et je vérifie l'identité avant de dire quoi que ce soit. C'est quel "
              "Pittet, au fait ? »", 2, "pb3 cc1 ic2"),
            R("« Oui, oui. »", 3, "cc-1"),
            R("« Et si c'est un proche qui répond ? »", 5, "pb2 cc1"),
            R("« Franchement, le secrétariat, ce n'est pas mon rôle. »", 3, "ic-3 rd-2"),
            R("Prendre le combiné et chercher le numéro.", 3, "pb-1"),
        ]),
        I(5, "sandra", "neutral",
          "« Rien. » Sandra cale le combiné contre son épaule. « Tu ne donnes aucun résultat "
          "au téléphone. Tu vérifies que tu parles à la bonne personne — nom, prénom, date de "
          "naissance — et tu dis que la Dre veut la voir. Si quelqu'un d'autre répond, même le "
          "mari, même le fils : tu demandes qu'elle rappelle le cabinet. Point. » Un temps. "
          "« Et c'est Pittet Jeannine. Pas Jean-Paul. »", [go(6)]),
        I(6, "jeannine", "neutral",
          "Trois sonneries. « Pittet. » Une voix de femme, un peu essoufflée. Derrière, un "
          "chien qui aboie.", [
            R("« Bonjour, ici Alex, du cabinet de la Dre Golay. Est-ce que je parle bien à "
              "Mme Jeannine Pittet ? Pouvez-vous me donner votre date de naissance ? »",
              8, "pb3 cc2 rd2 ic1"),
            R("« Madame Pittet ? C'est pour vos résultats : votre créatinine a "
              "augmenté. »", 9, "pb-2 cc-1"),
            R("« Madame Pittet, la Dre aimerait vous voir lundi pour vos résultats. »",
              8, "pb-1 cc1"),
            R("« Bonjour Madame Pittet ! Comment vont vos chevilles ? »", 8, "rd1 em1 pb-1"),
            R("« C'est le petit de la fac. La Dre veut vous voir, c'est pour vos reins. »",
              9, "pb-2 cc-1 rd-1"),
        ]),
        I(7, "jeanpaul", "neutral",
          "« Pittet ! » Une voix d'homme, une télé derrière. Vous lancez : « Bonjour, ici le "
          "cabinet de la Dre Golay, c'est pour vos résultats de prise de sang… » — « Mes "
          "résultats ? J'ai fait que le cholestérol, moi. » Un temps. « C'est pas plutôt pour "
          "la Jeannine, ça ? Elle était au cabinet jeudi. Qu'est-ce qu'elle a, la "
          "Jeannine ? »", [
            R("« Excusez-moi, je dois vérifier quelque chose. Le cabinet vous rappellera. "
              "Bonne journée. » Et raccrocher, sans un mot de plus.", 12, "pb3 cc2 er1",
              sets=["appel_rattrape"]),
            R("« Ah, pardon ! Oui, c'est pour Mme Jeannine Pittet. Vous la connaissez ? Vous "
              "pourriez lui dire de rappeler ? »", 14, "pb-2 cc-1",
              sets=["erreur_homonyme"]),
            R("« Rien de grave : ses reins fatiguent un peu. Dites-lui de rappeler la "
              "Dre. »", 13, "pb-3 cc-2 rd-2", sets=["erreur_homonyme", "info_lachee"]),
            R("« Je ne peux rien vous dire. » Puis : « Vous savez si elle est chez "
              "elle ? »", 14, "pb-1 cc-1", sets=["erreur_homonyme"]),
            R("Raccrocher brusquement, sans rien dire.", 12, "pb1 rd-2 cc-2",
              sets=["appel_rattrape"]),
        ]),
        I(8, "jeannine", "happy",
          "« C'est moi. 4 mai 1944, si vous voulez tout savoir. » Elle rit. « Lundi ? Ça doit "
          "être les reins, hein. La Dre m'avait prévenue. C'est mauvais ? Vous pouvez me le "
          "dire, à moi, je ne vais pas m'évanouir. »", [
            R("« Je n'ai pas les résultats sous les yeux, et ce n'est pas à moi de les "
              "interpréter. La Dre vous expliquera tout lundi, et vous pourrez lui poser toutes "
              "vos questions. »", 10, "pb3 cc2 rd1"),
            R("« Votre créatinine est à 212. C'est assez haut. »", 9, "pb-3 cc-1"),
            R("« Je crois que c'est sérieux, oui. »", 9, "pb-2 cc-2 em-1"),
            R("« Vous avez l'air inquiète. Vous voulez qu'on avance le rendez-vous ? »",
              10, "em2 pb1 ic1"),
            R("« Ne vous inquiétez pas, ce n'est sûrement rien. »", 10, "cc-3 pb-2"),
        ]),
        I(9, "jeannine", "resigned",
          "Un silence. « Ah. » Puis, plus bas : « Bon. Dites à la Dre que je sais ce que ça "
          "veut dire, et que je ne ferai pas de dialyse. Je ne vais pas passer trois "
          "après-midi par semaine branchée à une machine à Yverdon. » Elle raccroche avant "
          "que vous ayez répondu.", [
            R("Aller trouver Sandra tout de suite : « J'ai donné des résultats au téléphone, "
              "et elle l'a mal pris. Il faut prévenir la Dre. »", 11, "pb2 ic3 er1 cc1",
              sets=["bon_pittet"]),
            R("Noter « RDV lundi », et passer à la suite.", 11, "pb-1 ic-1",
              sets=["bon_pittet"]),
            R("La rappeler pour s'excuser, et lui donner les chiffres exacts.", 11, "pb-3 cc-1",
              sets=["bon_pittet"]),
            R("Ne rien dire à personne.", 11, "pb-2 ic-2", sets=["bon_pittet"]),
        ]),
        I(10, "jeannine", "neutral",
          "« Hm. Vous êtes bien dressé·e. » Elle rit. « Lundi, alors. Dites à la Dre que je "
          "sais ce que ça veut dire, les reins, à mon âge. Et que je ne ferai pas de "
          "dialyse. Elle comprendra. »", [
            R("« Je le lui dirai mot pour mot. Et lundi, vous pourrez lui dire vous-même tout "
              "ce que vous voulez qu'elle sache. »", 11, "cc2 rd2 ic1 pb1",
              sets=["bon_pittet"]),
            R("« Il ne faut pas dire ça, Madame Pittet. La dialyse, ça peut vous sauver. »",
              11, "rd-2 pb-2", sets=["bon_pittet"]),
            R("« D'accord. » Et raccrocher.", 11, "cc-1 ic-1", sets=["bon_pittet"]),
            R("« Vous voulez que quelqu'un vous accompagne lundi ? »", 11, "em2 cc1",
              sets=["bon_pittet"]),
            R("« Vous avez le droit de refuser. Mais parlez-en avec la Dre avant de décider : "
              "elle vous dira ce que ça implique. »", 11, "rd2 cc2 pb1",
              sets=["bon_pittet"]),
        ]),
        I(11, "sandra", "neutral",
          "Sandra raccroche son propre téléphone au même moment. « Alors ? » Vous lui "
          "transmettez le rendez-vous. Elle note, puis, sans lever les yeux : « Elle t'a dit, "
          "pour la dialyse ? » Vous hochez la tête. « À moi aussi, il y a deux ans. La Dre "
          "l'avait écoutée. » Elle colle un post-it jaune sur son écran, en gros : « PITTET J. "
          "= 2 ! DATE DE NAISSANCE ! »"),
        I(12, "sandra", "anxious",
          "Vous raccrochez, le cœur battant. Sandra a entendu, entre deux patients. « C'était "
          "Jean-Paul ? » Vous hochez la tête. « Il a su quelque chose ? » — « Qu'on appelait "
          "pour des résultats. Il a deviné que c'était pour Jeannine. »", [
            R("« Je n'ai pas vérifié l'identité avant de parler. Je le note, et je le dis à la "
              "Dre ce soir. »", 17, "pb3 ic2 cc1"),
            R("« Il n'a rien su, c'est l'essentiel. »", 17, "pb-1 er1"),
            R("« C'est ton post-it qui n'était pas clair. »", 17, "ic-2 pb-1"),
            R("« On pourrait faire quelque chose pour les homonymes ? Une alerte dans le "
              "logiciel ? »", 17, "ic3 cc1 pb1"),
            R("Se taire, et passer au patient suivant.", 17, "pb-1 ic-1"),
        ]),
        I(13, "jeanpaul", "suspicious",
          "« Les reins ? » Jean-Paul baisse le son de la télé. « Elle va devoir aller à la "
          "dialyse, alors. Comme le père Bovay. Il a pas tenu six mois. » Il a l'air presque "
          "content d'avoir une nouvelle. « Elle le sait, au moins ? Et Daniel ? »", [
            R("« Je n'aurais jamais dû vous dire ça. C'est une erreur de ma part, et je vous "
              "demande de n'en parler à personne. Je dois prévenir la Dre. »",
              15, "pb2 cc2 er1"),
            R("« Elle refuse la dialyse, de toute façon. »", 15, "pb-3 rd-2 cc-1"),
            R("« Je ne sais pas. » Et raccrocher.", 15, "pb-1 er-1"),
            R("« Vous pourriez prévenir Daniel ? »", 15, "pb-3 ic-1"),
            R("« Je ne peux rien dire de plus. Au revoir. »", 15, "pb1 cc1"),
        ]),
        I(14, "jeanpaul", "suspicious",
          "« Ah, la Jeannine. » Jean-Paul baisse le son de la télé. « Elle va pas fort, hein ? "
          "On la voit plus au culte. C'est quoi, son problème ? Le cœur ? »", [
            R("« Je ne peux rien vous dire, je suis désolé·e. Je me suis trompé·e de numéro. » "
              "Et prévenir Sandra immédiatement.", 15, "pb3 cc1 ic1"),
            R("« Non, c'est plutôt les reins. »", 13, "pb-3 cc-1", sets=["info_lachee"]),
            R("« Vous êtes de la famille ? »", 15, "pb-2 cc-1"),
            R("Raccrocher.", 15, "pb1 rd-1 cc-1"),
            R("« Je ne sais pas. Vous la voyez souvent ? »", 15, "pb-2 em1"),
        ]),
        I(15, "sandra", "anxious",
          "Vous raccrochez. Sandra a tout entendu, entre deux patients. Elle vous regarde. "
          "« C'était Jean-Paul ? » Elle ferme les yeux une seconde. « Jean-Paul, c'est la "
          "radio du village. Ce soir, tout le Café de la Gare saura. »", [
            R("« Oui. Je n'ai pas vérifié la date de naissance. C'est ma faute. Il faut "
              "prévenir la Dre, et Jeannine, avant qu'elle l'apprenne par quelqu'un "
              "d'autre. »", 16, "pb3 ic2 er1 cc1 rd1"),
            R("« Tu ne m'avais pas dit lequel. »", 16, "ic-2 pb-2 er-1"),
            R("« Il ne dira rien, il avait l'air gentil. »", 16, "pb-2 cc-1"),
            R("« On pourrait ne rien dire. Ça va peut-être passer. »", 16, "pb-3 ic-2 rd-1"),
            R("« Qu'est-ce que je dois faire ? »", 16, "ic2 er1"),
        ]),
        I(16, "narr", "",
          "Sandra appelle la Dre Golay sur son portable. Vous l'entendez dire : « Non, c'est "
          "l'étudiant·e. Oui. Jean-Paul. » Puis plus rien. Elle raccroche et vous tend, sans "
          "un mot, le formulaire de déclaration d'incident du cabinet."),
        I(17, "sandra", "neutral",
          "Sandra colle un post-it jaune sur son écran, en gros : « PITTET J. = 2 ! DATE DE "
          "NAISSANCE ! » « Voilà notre système d'alerte. » Elle rit, nerveusement. « La Dre "
          "appellera Jeannine elle-même. Et Jean-Paul, je m'en occupe : il me doit une tarte "
          "aux pruneaux. »"),
    ],
)

# ---------------------------------------------------------------------------
# 2.3 L'APP du jeudi
# ---------------------------------------------------------------------------
S2_3 = S(3, "2.3 L'APP du jeudi",
    "Jeudi suivant, 10 h 15. Salle de tutorat B. Apprentissage par problèmes : huit "
    "étudiant·e·s autour d'une table, un tableau blanc, un cas en trois pages. Le tuteur, "
    "le Dr Ibarra, médecin assistant en pédiatrie, s'assied dans un coin et n'ouvrira "
    "presque pas la bouche. Le cas du jour : « Mme R., 34 ans, fatigue, pâleur, "
    "essoufflement à l'effort. »",
    focus=("ic", "cc", "pb"),
    nodes=[
        I(1, "ibarra", "neutral",
          "« Qui anime aujourd'hui ? Qui écrit au tableau ? » Silence. Noah a son ordinateur "
          "ouvert, Maëlle son téléphone, Yasmine les bras croisés. Léo a imprimé le cas et "
          "l'a annoté au crayon, en allemand et en français.", [
            R("« J'écris au tableau. Léo, tu veux animer ? Tu as déjà annoté tout le cas. »",
              2, "ic3 rd1 cc1", sets=["leo_inclus"]),
            R("« J'anime. » Et prendre aussi le feutre.", 2, "ic-1 cc1"),
            R("« Noah, t'as l'air prêt, vas-y. »", 2, "ic1"),
            R("Attendre que quelqu'un se dévoue.", 2, "ic-1"),
            R("« On tourne : chaque séance, quelqu'un de différent. Aujourd'hui j'écris, "
              "Yasmine anime ? »", 2, "ic3 cc2"),
            R("« Franchement, l'APP, c'est du temps perdu. On lit le cours, et c'est "
              "réglé. »", 2, "ic-3 rd-1"),
        ]),
        I(2, "noah", "happy",
          "Noah démarre avant tout le monde. « Anémie microcytaire, ferriprive, "
          "probablement des règles abondantes. Bilan martial, ferritine, et on cherche une "
          "cause digestive si elle a plus de cinquante ans, ce qui n'est pas le cas. » Il "
          "tourne son écran : un chatbot vient de lui écrire une réponse impeccable, "
          "références comprises. « Voilà. On a fini ? » Maëlle rit. Yasmine non.", [
            R("« C'est peut-être juste. Mais l'APP, c'est qu'on y arrive ensemble, en "
              "raisonnant. Qu'est-ce qu'on sait, nous, sans l'écran ? »", 3, "ic3 cc2 pb1"),
            R("« Génial, on gagne une heure. »", 4, "ic-2 pb-1"),
            R("Recopier la réponse du chatbot au tableau.", 4, "ic-1 pb-1 cc-1"),
            R("« Léo, tu avais souligné quelque chose dans le cas, non ? »", 5, "ic3 rd2",
              sets=["leo_inclus"]),
            R("Regarder le Dr Ibarra, pour qu'il intervienne.", 3, "ic-1 er-1"),
        ]),
        I(3, "yasmine", "angry",
          "Yasmine décroise les bras. « Le chatbot ne sait pas que Mme R. a trois enfants, un "
          "mari qui travaille de nuit, et qu'elle ne mange presque plus de viande depuis "
          "qu'elle a perdu son travail. C'est page deux. » Elle regarde Noah. « Toi non plus, "
          "d'ailleurs. T'as pas lu la page deux. » Noah rougit. Le silence devient lourd.", [
            R("« On a tous nos façons de travailler. Yasmine a raison pour la page deux, et "
              "Noah a le bon point de départ. On met les deux au tableau ? »",
              5, "ic3 cc2 em2 er1 rd1"),
            R("« Yasmine, calme-toi. »", 5, "ic-1 rd-1"),
            R("Rire, pour détendre l'atmosphère.", 5, "er-1 ic-1"),
            R("« Elle a raison, Noah. Tu triches. »", 5, "ic-2 em-2 rd-1"),
            R("« Page deux, justement : qu'est-ce qu'on en tire ? Léo, tu l'as annotée. »",
              5, "ic3 cc1 rd1", sets=["leo_inclus"]),
        ]),
        I(4, "ibarra", "neutral",
          "Le Dr Ibarra lève enfin les yeux de son café. « Intéressant. Vous avez la "
          "réponse. » Il se lève, efface le tableau, et écrit une seule question : « Pourquoi "
          "Mme R. ne va-t-elle plus chez le médecin depuis six mois ? » Il se rassied. « Je "
          "vous écoute. »", [
            R("« Page deux : elle a perdu son travail. Elle a peur de ce que ça coûte, avec la "
              "franchise de sa caisse maladie. »", 5, "cc2 ic1 em1"),
            R("« Parce qu'elle ne savait pas qu'elle était malade ? »", 5, "cc1"),
            R("« Ce n'est pas médical, comme question. »", 5, "rd-2 ic-1"),
            R("Se tourner vers Léo, qui a levé la main sans oser parler : « Léo ? »",
              5, "ic3 rd2", sets=["leo_inclus"]),
            R("Poser la question au chatbot de Noah.", 5, "pb-2 ic-1"),
        ]),
        I(5, "leo", "vulnerable",
          "Léo s'éclaircit la gorge. « Page deux. Elle donne sa viande aux enfants. Elle a dit "
          "à la pharmacienne : « Moi, je mange ce qui reste. » » Il cherche ses mots. « Bei "
          "uns… à Zurich, on appelait ça… les déterminants… sociaux ? La cause, ce n'est pas "
          "seulement les règles. C'est l'argent. » Personne ne dit rien. Puis Maëlle : "
          "« Ouah. »", [
            R("Écrire au tableau, en gros : « Carence d'apport — précarité », et dessous : "
              "« Léo ». « C'est exactement ça. »", 6, "ic3 rd2 cc1", sets=["leo_inclus"]),
            R("« Bien vu. » Et passer à la suite.", 6, "ic1"),
            R("« On dit « déterminants sociaux », oui. Et « bei uns », ici, on dit « chez "
              "nous ». »", 6, "rd-2 ic-1 em-1"),
            R("« Noah, ton chatbot avait vu ça ? »", 6, "ic-1 em-1"),
            R("« Alors une ordonnance de fer ne suffira pas. Qui, dans le réseau de soins, "
              "peut l'aider pour l'argent ? »", 6, "ic3 cc2"),
        ]),
        I(6, "ibarra", "neutral",
          "Midi. Le Dr Ibarra se lève. « Pour jeudi prochain : chacun écrit sa réflexion de "
          "portfolio sur la séance. Ce que vous avez appris, et comment. Pas ce que vous avez "
          "lu. » Il regarde Noah. « Avec vos mots. » Il sort.", [go(7)]),
        I(7, "noah", "anxious",
          "Dans le couloir, Noah vous rattrape. Il a les yeux cernés. « T'as fait ta "
          "réflexion de portfolio sur l'APP de la dernière fois ? Tu peux me l'envoyer ? Juste "
          "pour voir comment tu tournes ça. Je reformulerai, promis. Je n'ai pas le temps "
          "cette semaine, j'ai trois révisions en retard. »", [
            R("« Non, Noah. Ce texte, c'est le mien, et le tien doit être le tien. Mais je "
              "peux t'aider à écrire le tien : on se pose une heure ce soir ? »",
              8, "pb3 em2 ic1"),
            R("« Ok, je te l'envoie. Mais tu changes tout, hein. »", 9, "pb-3 ic-1",
              sets=["texte_partage"]),
            R("« Demande à ton chatbot. »", 10, "em-2 ic-1 pb1"),
            R("« T'as l'air crevé. Ça va, toi, en ce moment ? »", 11, "em3 co1"),
            R("« Si je te l'envoie et que ça se voit, on aura des problèmes tous les deux. "
              "Non. »", 8, "pb2 cc1 em-1"),
            R("Le lui envoyer sans rien dire : c'est un pote.", 9, "pb-3 cc-1",
              sets=["texte_partage"]),
        ]),
        I(8, "noah", "sad",
          "Noah hoche la tête trop vite. « Ouais. T'as raison. » Son téléphone vibre : un "
          "message de son père, qu'il ne lit pas. « Laisse tomber, je vais me "
          "débrouiller. »", [
            R("« Ce soir, 20 h, à la bibli. Je t'aide à trouver tes mots, pas les miens. »",
              12, "em2 ic2 pb1"),
            R("« Ok. Bon courage. »", 12, "em-1"),
            R("« C'est ton père ? Tu veux en parler ? »", 11, "em3"),
            R("« Tu sais qu'il y a un logiciel anti-plagiat, hein. »", 12, "pb1 em-2"),
            R("« Arrête de te plaindre, on est tous crevés. »", 12, "em-3 co-2"),
        ]),
        I(9, "noah", "happy",
          "« T'es le ou la meilleur·e. » Noah vous serre l'épaule. Le soir, il vous envoie un "
          "pouce levé. Puis : « j'ai fait passer ton texte dans le chatbot pour le "
          "reformuler, ça déchire ». Vous relisez son message deux fois.", [
            R("« Noah. Ne rends pas ça. Le logiciel va trouver mes phrases, et l'IA, ça se "
              "voit. Écris le tien : je t'aide, si tu veux. »", 12, "pb3 em1 cc2"),
            R("« Cool. »", 12, "pb-2"),
            R("Ne pas répondre.", 12, "pb-1 ic-1"),
            R("« Ok, mais si ça se voit, je dirai que tu me l'as volé. »", 12, "pb-1 em-2 ic-2"),
            R("« Supprime-le de ton ordi, s'il te plaît. Je te le demande vraiment. »",
              12, "pb2 cc1"),
        ]),
        I(10, "noah", "hurt",
          "Noah vous regarde comme si vous l'aviez giflé. « Merci. Vraiment. » Il s'en va. "
          "De loin, vous le voyez s'asseoir sur un banc, la tête dans les mains.", [
            R("Le rejoindre sur le banc. « Pardon. C'était nul. Qu'est-ce qui se passe ? »",
              11, "em3 er1 rd1"),
            R("Le laisser. Il a besoin d'apprendre à se débrouiller.", 12, "em-2 co-1"),
            R("Lui envoyer un message : « désolé·e, mal dormi ».", 12, "em1"),
            R("En parler à Maëlle : « Noah pète un câble. »", 12, "pb-2 rd-1"),
        ]),
        I(11, "noah", "vulnerable",
          "Noah s'assied sur la première marche de l'escalier. « Mon père m'appelle tous les "
          "soirs. Il veut mes notes, mon rang, ce que les profs disent de moi. Il connaît la "
          "moitié des profs. » Il rit. « Je dors quatre heures par nuit. J'ai l'impression "
          "d'avoir déjà raté ma vie, à vingt ans. »", [
            R("« Quatre heures par nuit, depuis combien de temps ? Ça m'inquiète, Noah. Il y a "
              "un service de consultation pour les étudiants. Tu veux qu'on regarde "
              "ensemble ? »", 12, "em2 ic2 pb2 cc1"),
            R("« Tu n'as rien raté. Tu es en deuxième année, et tu es là. »", 12, "em2 co2"),
            R("« Coupe ton téléphone le soir. »", 12, "cc1 em-1"),
            R("« Mon pauvre. Bon, je dois y aller. »", 12, "em-2 co-2"),
            R("« Tu veux que je t'aide pour ton portfolio, ce soir ? Pas en te donnant le "
              "mien : en t'aidant à écrire le tien. »", 12, "em2 pb2 ic1"),
        ]),
        I(12, "narr", "",
          "Le soir, vous relisez votre propre réflexion de portfolio. Vous avez écrit : "
          "« J'ai appris qu'une anémie peut être une question d'argent. » Vous pensez à "
          "Mme R., qui mange ce qui reste, et à Noah, qui ne dort plus."),
    ],
)

# ---------------------------------------------------------------------------
# 2.4 Le Café de la Gare — branche « Alex a appelé le mauvais Pittet »
# ---------------------------------------------------------------------------
_INTRO_24 = (
    "Samedi matin. Vous passez au cabinet chercher un livre oublié. Sandra est là, malgré "
    "la fermeture ; elle a la tête de quelqu'un qui n'a pas dormi. « Assieds-toi. Hier "
    "soir, au Café de la Gare, Jean-Paul a raconté que le cabinet l'avait appelé pour les "
    "résultats de la Jeannine. Que ça devait être grave. Daniel était au bar. Il arrive. "
    "La Dre est en route. »"
)
_INTRO_24_INFO = (
    "Samedi matin. Vous passez au cabinet chercher un livre oublié. Sandra est là, malgré "
    "la fermeture ; elle a la tête de quelqu'un qui n'a pas dormi. « Assieds-toi. Hier "
    "soir, au Café de la Gare, Jean-Paul a raconté à tout le monde que la Jeannine avait "
    "les reins foutus et qu'elle allait finir à la dialyse. Daniel était au bar. Il "
    "arrive. La Dre est en route. »"
)

S2_4A = S(4, "2.4 Le Café de la Gare", _INTRO_24,
    focus=("pb", "rd", "er", "cc"),
    slot="2.4",
    cond=when(all=["erreur_homonyme"]),
    entries=[
        Entry(1, when(all=["info_lachee"]), _INTRO_24_INFO),
    ],
    debriefs=[
        Debrief(when(all=["esquive_homonyme"]), tone="hard", lead=(
            "Vous avez laissé Sandra porter une erreur qui était la vôtre. Après un "
            "incident, la personne qui l'a commis ne doit pas se cacher derrière « le "
            "cabinet » : reconnaître sa part, tout de suite, protège les collègues, la "
            "confiance du patient, et soi-même. La responsabilité de l'institution — ici, la "
            "Dre Golay — n'efface pas la vôtre.")),
        Debrief(when(all=["aveu_homonyme"]), tone="mixed", lead=(
            "Rien ne rendra à Daniel la façon dont il a appris la maladie de sa mère. Mais "
            "vous avez dit « c'est moi », sans vous défausser sur Sandra ni sur le logiciel, "
            "et sans spéculer sur la santé de Jeannine. C'est ce qu'on attend après un "
            "incident : reconnaître, s'excuser, laisser parler la personne responsable, et "
            "changer ce qui l'a rendu possible.")),
    ],
    nodes=[
        I(1, "daniel", "angry",
          "La porte vitrée claque. Daniel Pittet, en bottes, la casquette à la main. Il ne "
          "s'assied pas. « C'est qui, qui a téléphoné à Jean-Paul ? » Sandra ouvre la bouche. "
          "Vous êtes debout à côté d'elle.", [
            R("« C'est moi. J'ai appelé le mauvais Pittet, sans vérifier à qui je parlais. "
              "C'est mon erreur, pas celle de Sandra. »", 2, "pb3 rd2 er2 ic2",
              sets=["aveu_homonyme"]),
            R("Regarder Sandra.", 3, "pb-2 ic-3 er-1"),
            R("« Il y a eu une erreur au cabinet. »", 3, "pb-1 cc-1"),
            R("« Calmez-vous, Monsieur Pittet. »", 3, "rd-1 er-1 em-2"),
            R("« C'est le post-it de Sandra qui n'était pas clair. »", 3, "ic-3 pb-3 rd-1"),
        ]),
        I(2, "daniel", "cold-anger",
          "Daniel vous regarde longtemps. Il a les yeux rouges, de fatigue ou d'autre chose. "
          "« Vous. » Il fait un pas. « Ma mère est malade, elle ne m'a rien dit, et c'est "
          "Jean-Paul Pittet qui me l'apprend au café, devant le père Cuendet et la moitié du "
          "village. Vous savez ce que ça fait ? »", [
            R("« Non. Je ne peux pas le savoir. Je suis désolé·e. Ce que j'ai fait n'aurait "
              "jamais dû arriver. »", 4, "rd2 em2 er1 pb1"),
            R("« Votre mère allait vous le dire. »", 5, "pb-3 cc-2"),
            R("Se taire, et soutenir son regard.", 4, "er2 rd1"),
            R("« Vous devriez en parler avec elle. »", 5, "pb-1 em-1"),
            R("« C'est surtout Jean-Paul qui n'aurait pas dû le raconter. »",
              5, "pb-2 er-1 rd-1"),
        ]),
        I(3, "daniel", "angry",
          "Daniel tape du plat de la main sur le comptoir. Un pot de stylos se renverse. « Je "
          "vous ai posé une question. Qui ? » Sandra baisse les yeux. Elle ne dira rien. Elle "
          "attend que vous parliez.", [
            R("« C'est moi. Sandra n'y est pour rien. Je n'ai pas vérifié à qui je "
              "parlais. »", 2, "pb3 rd2 ic3 er1", sets=["aveu_homonyme"]),
            R("Laisser le silence durer jusqu'à l'arrivée de la Dre.", 6, "pb-2 ic-3",
              sets=["esquive_homonyme"]),
            R("« Le cabinet va vous répondre. La Dre arrive. »", 6, "pb-1 ic-1 cc-1",
              sets=["esquive_homonyme"]),
            R("« Quelqu'un du secrétariat s'est trompé de numéro. »", 6, "pb-3 ic-3 cc-1",
              sets=["esquive_homonyme"]),
            R("Ramasser les stylos, sans répondre.", 6, "er-1 pb-1",
              sets=["esquive_homonyme"]),
        ]),
        I(4, "golay", "neutral",
          "La Dre Golay entre, en manteau, essoufflée. Elle prend la mesure de la scène. "
          "« Daniel. Asseyez-vous, s'il vous plaît. » Il ne s'assied pas. Elle reste debout "
          "aussi. « Le cabinet a fait une erreur, et j'en suis responsable. Alex a appelé le "
          "mauvais Pittet. Je vous présente nos excuses. Ce que je ne peux pas faire, c'est "
          "vous parler de la santé de votre mère : ça, c'est à elle. » Daniel se tourne vers "
          "vous.", [
            R("« Monsieur Pittet, je vous présente mes excuses, à vous et à votre mère. Je "
              "les lui présenterai aussi, si elle l'accepte. »", 7, "rd3 pb2 er1 co1"),
            R("« Je ne referai plus jamais cette erreur. »", 7, "pb1 er1"),
            R("Rester silencieux·se, et laisser la Dre parler.", 7, "ic1 er1"),
            R("« Votre mère va bien, ne vous inquiétez pas. »", 7, "cc-3 pb-3"),
            R("« Vous pouvez lui demander vous-même. Elle vous répondra. »", 7, "pb1 em-1"),
        ]),
        I(5, "daniel", "resigned",
          "Daniel rit, d'un rire sans joie. « Elle allait me le dire. Bien sûr. Comme pour le "
          "reste. » Il remet sa casquette, l'enlève de nouveau. « Le reste ? », demande "
          "Sandra. Il ne répond pas. Une voiture se gare devant le cabinet.", [go(4)]),
        I(6, "golay", "cold-anger",
          "La Dre Golay entre, en manteau. Elle regarde Daniel, Sandra, vous. « Daniel, "
          "asseyez-vous. » Puis, d'une voix égale : « Sandra m'a expliqué. Ce n'est pas elle "
          "qui a téléphoné à Jean-Paul. » Elle vous regarde. Le silence dure. Daniel aussi "
          "vous regarde, maintenant.", [
            R("« C'est moi. J'aurais dû le dire tout de suite. Pardon, Sandra. Pardon, "
              "Monsieur Pittet. »", 7, "pb3 rd2 er1 ic2",
              sets=["aveu_homonyme"], clears=["esquive_homonyme"]),
            R("« Je pensais que c'était au cabinet de répondre. »", 9, "pb-2 er-1"),
            R("« Je ne savais pas qu'il fallait vérifier la date de naissance. »",
              9, "pb-2 cc-1 ic-1"),
            R("Baisser les yeux.", 9, "er-1"),
            R("« Il y avait deux Pittet J. dans le logiciel. N'importe qui se serait "
              "trompé. »", 9, "pb-3 ic-1"),
        ]),
        I(7, "golay", "neutral",
          "La Dre Golay parle longtemps, calmement, à Daniel. Elle reconnaît l'erreur du "
          "cabinet, explique ce qui va changer — une alerte sur les homonymes, une règle pour "
          "les appels —, et refuse, doucement mais fermement, de parler de la santé de "
          "Jeannine. « Ça, c'est à elle de vous le dire. Allez la voir. Pas pour la gronder : "
          "pour l'écouter. » Daniel se lève. À la porte, il se retourne vers vous. « Vous, au "
          "moins, vous l'avez dit. » Il met sa casquette. « Ça ne change rien. Mais vous "
          "l'avez dit. »", [
            R("« Je comprendrais que vous ne vouliez plus me voir chez votre mère. C'est à "
              "elle et à vous de décider. »", 10, "rd2 pb2 em1"),
            R("« Merci. »", 10, "er1"),
            R("« Vous devriez parler à votre mère aujourd'hui. »", 10, "pb-1 em1"),
            R("« Je passerai la voir jeudi, comme d'habitude. »", 10, "pb-2 rd-1"),
            R("Hocher la tête, sans rien dire.", 10, "rd1 er1"),
        ]),
        I(9, "golay", "neutral",
          "La Dre Golay parle longtemps, calmement, à Daniel. Elle reconnaît l'erreur du "
          "cabinet, explique ce qui va changer, et refuse, doucement mais fermement, de parler "
          "de la santé de Jeannine. « Ça, c'est à elle de vous le dire. » Daniel se lève. À la "
          "porte, il se retourne vers vous. « Vous, je ne veux plus vous voir chez ma mère. » "
          "La porte vitrée tremble longtemps.", [
            R("Courir après lui : « Monsieur Pittet ! C'était moi. Pardon. »",
              10, "pb2 rd1 er1"),
            R("Le laisser partir.", 10, "er-1"),
            R("« C'est lui qui exagère. »", 10, "rd-2 er-1 em-1"),
            R("Se tourner vers Sandra : « Pardon. Pour tout à l'heure. »", 10, "ic2 rd1"),
            R("« De toute façon, je n'ai rien à faire chez sa mère. »", 10, "em-2 rd-1"),
        ]),
        I(10, "golay", "neutral",
          "La Dre Golay remplit avec vous la déclaration d'incident du cabinet. Ligne par "
          "ligne : ce qui s'est passé, ce qui l'a rendu possible — deux « Pittet J. », un "
          "post-it sans date de naissance, une file de six personnes —, et ce qui va changer. "
          "Elle ne hausse jamais la voix. « On ne fait pas ça pour trouver un coupable. On le "
          "fait pour que la prochaine Sandra et le prochain Alex ne se retrouvent pas là. » "
          "Puis : « Jeannine, je l'appelle tout à l'heure. Elle voudra peut-être vous voir. "
          "Ou pas. »"),
    ],
)

# ---------------------------------------------------------------------------
# 2.4 La créatinine — branche « personne n'a parlé au village »
# ---------------------------------------------------------------------------
_INTRO_24B = (
    "Lundi, 14 h. Jeannine est assise dans le cabinet de la Dre Golay, son sac à main sur "
    "les genoux, son foulard rouge noué serré. Les résultats sont à l'écran. La Dre vous a "
    "demandé d'être là, et Jeannine aussi."
)
_INTRO_24B_RATTRAPE = (
    "Lundi, 14 h. Samedi, Jean-Paul est passé au cabinet demander « ce qu'avait la "
    "Jeannine » ; Sandra l'a renvoyé avec un sourire et pas un mot. Jeannine est assise dans "
    "le cabinet de la Dre Golay, son sac à main sur les genoux. Les résultats sont à "
    "l'écran. La Dre vous a demandé d'être là, et Jeannine aussi."
)
_INTRO_24B_REVELE = (
    "Lundi, 14 h. Depuis septembre, Daniel ne rentre plus dans la cuisine de sa mère : il "
    "nourrit les bêtes, et il repart. Jeannine ne vous a plus adressé la parole. Elle est "
    "assise dans le cabinet de la Dre Golay, son sac à main sur les genoux. La Dre vous a "
    "demandé d'être là. Jeannine n'a pas dit non."
)

S2_4B = S(5, "2.4 La créatinine", _INTRO_24B,
    focus=("rd", "cc", "co"),
    slot="2.4",
    cond=when(none=["erreur_homonyme"]),
    entries=[
        Entry(20, when(all=["revele_a_daniel"]), _INTRO_24B_REVELE),
        Entry(1, when(all=["appel_rattrape"]), _INTRO_24B_RATTRAPE),
    ],
    nodes=[
        I(1, "golay", "neutral",
          "« Jeannine, vos reins travaillent moins bien. Beaucoup moins bien qu'au "
          "printemps. » La Dre tourne l'écran vers elle. « Si ça continue à ce rythme, dans "
          "quelques mois, il faudra parler de dialyse. » Jeannine ne regarde pas l'écran. "
          "Elle vous regarde, vous.", [
            R("Soutenir son regard, sans rien dire : ce n'est pas à vous de parler.",
              2, "rd2 pb2 er1"),
            R("« La dialyse, ça se passe très bien, maintenant, Madame Pittet. »",
              3, "pb-3 cc-2"),
            R("Regarder ailleurs.", 2, "em-1 er-1"),
            R("Lui tendre un mouchoir, au cas où.", 2, "em1 rd-1"),
            R("Rapprocher un peu votre chaise de la sienne.", 2, "em2 co1"),
        ]),
        I(2, "jeannine", "neutral",
          "Jeannine pose son sac sur le bureau. « Isabelle, j'ai mis au monde votre fils, "
          "alors je vais vous parler franchement. » Elle croise les mains. « Pas de dialyse. "
          "Pas de machine trois après-midi par semaine à Yverdon, avec Daniel qui perd une "
          "journée de foin pour m'y conduire. J'ai huitante et un ans. J'ai eu une belle vie, "
          "un mari que j'ai aimé, et j'ai vu naître six cents enfants. » Elle se tourne vers "
          "vous. « Vous, la fac, vous trouvez que je suis folle ? »", [
            R("« Non. Je trouve que vous savez ce que vous voulez. Et que la Dre Golay est la "
              "bonne personne pour vous dire tout ce que ça implique, avant que vous "
              "décidiez. »", 4, "rd3 pb2 cc2 em1"),
            R("« Un peu, oui. La dialyse pourrait vous donner des années. »", 3, "rd-3 pb-3"),
            R("« Ce n'est pas à moi de juger. »", 4, "pb2 em-1"),
            R("« Vous avez peur de la dialyse, ou d'être un poids pour Daniel ? »",
              5, "em3 cc1"),
            R("« Moi, à votre place, je ferais pareil. »", 4, "pb-2 em1"),
            R("Regarder la Dre Golay, pour qu'elle réponde.", 4, "pb1 ic1 em-1"),
        ]),
        I(3, "golay", "cold-anger",
          "La Dre Golay lève la main, sans vous regarder. « Alex. » Un seul mot. Puis, à "
          "Jeannine : « On n'est pas là pour vous convaincre, Jeannine. On est là pour que "
          "vous décidiez en sachant tout. »", [
            R("« Pardon, Madame Pittet. Ce n'était pas à moi de dire ça. »", 4, "pb2 rd2 er1"),
            R("Se taire, rouge.", 4, "er1"),
            R("« Je voulais juste l'aider. »", 4, "pb-1 er-1"),
            R("« Mais c'est vrai, non, que la dialyse… »", 4, "pb-3 er-2"),
        ]),
        I(4, "golay", "neutral",
          "La Dre Golay explique : ce qui se passera si les reins continuent à baisser — la "
          "fatigue, les jambes, le goût de métal dans la bouche ; ce qu'on peut faire sans "
          "dialyse pour que ce soit le plus confortable possible ; les directives "
          "anticipées, pour que sa volonté soit écrite. « Et Daniel ? » Jeannine soupire. "
          "« À Noël. Je lui dirai à Noël. Tout. » Elle se tourne vers vous. « Le 26, vous "
          "viendrez ? J'aimerais qu'il y ait quelqu'un de la médecine. Pas Isabelle : elle me "
          "connaît trop. »", [
            R("« Si la Dre Golay est d'accord, je viendrai. Pour écouter, pas pour parler à "
              "votre place. »", 6, "pb3 rd2 ic1", sets=["noel_annonce"]),
            R("« Promis, je serai là. »", 6, "pb-1 em1", sets=["noel_annonce"]),
            R("« Ce n'est pas le rôle d'un·e étudiant·e. »", 6, "pb1 em-2"),
            R("« Pourquoi attendre Noël ? Il faudrait le lui dire maintenant. »",
              6, "rd-2 pb-1"),
            R("Regarder la Dre Golay : « C'est possible ? »", 7, "ic2 pb2"),
        ]),
        I(5, "jeannine", "sad",
          "Jeannine met du temps à répondre. « Des deux. » Elle lisse son foulard. « Daniel a "
          "déjà porté son père. Je ne veux pas qu'il me porte, moi, trois fois par semaine, "
          "jusqu'à ce que je ne sois plus qu'un tuyau. » La Dre Golay ne dit rien. Elle vous "
          "laisse la question.", [
            R("« Est-ce que Daniel sait, pour vos reins ? Et pour ce que vous voulez ? »",
              4, "cc2 em1 ic1"),
            R("« Ce serait peut-être à lui de dire s'il veut vous porter. »",
              4, "rd1 em1 pb-1"),
            R("« Je comprends. »", 4, "em1"),
            R("« Mais vous n'êtes pas un poids ! »", 4, "cc-2 em1"),
            R("« Si vous refusez la dialyse, il faudra au moins le dire à Daniel. Sinon, "
              "c'est lâche. »", 4, "rd-3 em-2"),
        ]),
        I(6, "jeannine", "happy",
          "Jeannine se lève, remet son foulard. « Bien. » Sur le pas de la porte, elle se "
          "retourne. « Vous savez ce qu'on dit, chez les sages-femmes ? On ne pousse pas "
          "avant que le col soit ouvert. Daniel, c'est pareil. » Elle sort. La Dre Golay "
          "range ses lunettes. « Elle a raison. Elle a presque toujours raison. C'est "
          "épuisant. »"),
        I(7, "golay", "neutral",
          "La Dre Golay réfléchit. « Si vous le souhaitez toutes les deux. Vous serez témoin, "
          "Alex, pas médiateur·rice : si Daniel pose des questions médicales, vous lui dites "
          "de m'appeler. Et vous m'appelez après. »", [
            R("« D'accord. Témoin, pas médiateur·rice. Je vous appellerai le 26 au soir. »",
              6, "pb3 ic2 cc1", sets=["noel_annonce"]),
            R("« Et si ça se passe mal ? »", 6, "er1 cc1", sets=["noel_annonce"]),
            R("« Finalement, je préfère ne pas être mêlé·e à ça. »", 6, "em-2 pb1"),
            R("« Je pourrais aussi lui expliquer la dialyse, à Daniel. »", 6, "pb-3 ic-1",
              sets=["noel_annonce"]),
        ]),
        I(20, "jeannine", "cold-anger",
          "Jeannine vous voit, et pince les lèvres. « Ah. Vous. »", [
            R("« Madame Pittet, je vous ai trahie en septembre. Je n'avais pas le droit de "
              "dire ça à Daniel. Je ne vous demande pas de me pardonner. Si vous préférez que "
              "je sorte, je sors. »", 21, "pb3 rd3 er1 co1"),
            R("« Bonjour, Madame Pittet. » Comme si de rien n'était.", 21, "rd-2 er-1"),
            R("« Daniel aurait fini par le savoir, de toute façon. »", 21, "pb-3 rd-3 em-1"),
            R("Proposer de sortir, sans un mot d'explication.", 21, "pb1 er-1"),
            R("« Je suis désolé·e. Je pensais bien faire. »", 21, "rd1 er1 pb-1"),
        ]),
        I(21, "jeannine", "resigned",
          "Jeannine vous regarde longtemps. « Restez. Ce que j'ai à dire aujourd'hui, autant "
          "que vous l'entendiez. » Elle se tourne vers la Dre Golay. « Alors, ces "
          "reins ? »", [go(1)]),
    ],
)

# ---------------------------------------------------------------------------
# 2.5 Le dimanche aux Combettes
# ---------------------------------------------------------------------------
_INTRO_25 = (
    "Dimanche de novembre. Thierry vous a proposé sa tournée du dimanche, avec l'accord de "
    "la Dre Golay. Aux Combettes, une Twingo cabossée est garée dans la cour : une jeune "
    "fille aux cheveux violets en décharge des seaux de chrysanthèmes. Océane, la "
    "petite-fille de Jeannine, apprentie fleuriste. Pendant que Thierry prépare le "
    "pilulier dans la cuisine, elle vous fait signe de la suivre dans la grange."
)

S2_5 = S(6, "2.5 Le dimanche aux Combettes", _INTRO_25,
    focus=("em", "rd", "pb", "cc"),
    entries=[
        Entry(20, when(all=["revele_a_daniel"]), _INTRO_25),
        Entry(10, when(all=["erreur_homonyme"]), _INTRO_25),
    ],
    nodes=[
        I(1, "oceane", "suspicious",
          "Entre deux bottes de paille, Océane croise les bras. « C'est toi, la fac ? Mamie "
          "parle de toi tout le temps. » Elle vous dévisage. « Elle te parle à toi, et pas à "
          "nous. Elle a quoi ? »", [
            R("« Je ne peux pas te parler de sa santé, Océane. Pas parce que c'est toi : parce "
              "que c'est elle qui décide à qui elle en parle. Tu peux le lui demander, à "
              "elle. »", 3, "pb3 rd2 cc2", sets=["oceane_confiance"]),
            R("« Rien de grave, ne t'inquiète pas. »", 3, "cc-2 pb-2"),
            R("« Ses reins fatiguent un peu. »", 3, "pb-3 rd-1"),
            R("« Tu as l'air inquiète. Qu'est-ce que tu as remarqué, toi ? »", 2, "em3 cc1",
              sets=["oceane_confiance"]),
            R("« Demande à ton père. »", 3, "pb-1 em-2"),
        ]),
        I(2, "oceane", "sad",
          "Océane donne un coup de pied dans la paille. « Elle dort assise dans son fauteuil. "
          "Elle ne monte plus voir les veaux. Et elle a rangé tous ses papiers dans une boîte "
          "à biscuits, avec des étiquettes. Mamie ne range jamais rien. » Sa voix se casse. "
          "« Les vieux qui rangent leurs papiers, c'est qu'ils vont mourir. Tout le monde "
          "sait ça. »", [
            R("« Tu as vu beaucoup de choses, et tu as peur. C'est à elle qu'il faut le dire, "
              "ça. Tu veux que je lui dise que tu aimerais lui parler ? »",
              3, "em3 co2 pb1 ic1"),
            R("« Mais non, ça ne veut pas dire ça. »", 3, "cc-2 em-1"),
            R("« Elle a huitante et un ans, Océane. Un jour ou l'autre… »",
              3, "em-2 rd-1 pb-1"),
            R("« Tu en as parlé à ton père ? »", 3, "ic1 em1"),
            R("S'asseoir sur une botte de paille, à côté d'elle, et attendre.", 3, "em2 co2"),
        ]),
        I(3, "jeannine", "happy",
          "« Océane ! Lâche la fac, elle est là pour le travail. » Jeannine est sur le seuil "
          "de la grange, appuyée sur sa canne, Thierry derrière elle. Elle a tout entendu, ou "
          "presque. « Viens m'aider à mettre la table, ma grande. Et toi, la fac, tu restes "
          "manger la tresse ? » Océane vous regarde. Thierry aussi.", [
            R("« Merci, mais le repas, c'est en famille. Je repars avec Thierry. »",
              4, "pb3 rd1"),
            R("« Avec plaisir ! »", 5, "pb-2 em1"),
            R("« Océane a des questions, Madame Pittet. Je crois qu'elle aimerait vous "
              "parler. »", 6, "ic2 em2 pb1"),
            R("« Non merci, je ne mange pas chez les patients. »", 4, "rd-2 em-1 pb1"),
            R("« Océane me demandait ce que vous aviez. Je n'ai rien dit, bien sûr. »",
              6, "pb-2 rd-2"),
        ]),
        I(4, "thierry", "neutral",
          "Dans la Panda, Thierry vous regarde de côté. « Pour le repas, t'as bien fait. Ma "
          "première année, j'ai dit oui à tout le monde : tresse, raclette, baptême. Au bout "
          "de six mois, je ne savais plus si j'étais leur infirmier ou leur cousin. » Il "
          "démarre. « Et la petite, elle t'a demandé quoi ? »", [
            R("« Ce qu'avait sa grand-mère. Je ne lui ai rien dit de médical, et je lui ai "
              "proposé d'en parler avec Jeannine. Tu pourrais l'aider, toi aussi ? »",
              7, "ic3 pb2 cc1"),
            R("« Rien d'important. »", 7, "ic-1 cc-1"),
            R("« Ce qu'avait Jeannine. Je ne savais pas ce que j'avais le droit de dire à une "
              "mineure. »", 7, "pb1 cc1 ic1"),
            R("« Elle est un peu perdue, je crois. »", 7, "em2 pb-1"),
            R("« Rien. Et franchement, la famille, ce n'est pas mon problème. »",
              7, "em-2 ic-2 rd-1"),
        ]),
        I(5, "jeannine", "happy",
          "La table est mise pour quatre : elle avait prévu. Thierry, lui, est reparti. "
          "Jeannine coupe la tresse. Au deuxième café, elle vous demande votre avis sur ses "
          "jambes ; Océane, sur un bouton qu'elle a dans le dos. Daniel, qui passait chercher "
          "une clé, vous regarde depuis la porte sans entrer.", [
            R("« Pour vos jambes et pour le bouton, il faut demander à la Dre Golay. "
              "Aujourd'hui, je suis juste invité·e, et je n'aurais sans doute pas dû l'être. "
              "Merci pour la tresse. »", 7, "pb3 cc1 rd1"),
            R("Regarder les jambes, puis le bouton.", 7, "pb-3 rd-1"),
            R("« Ça a l'air de rien, ne vous inquiétez pas. »", 7, "pb-2 cc-2"),
            R("« Je ne peux pas, désolé·e. » Et changer de sujet.", 7, "pb2 em-1"),
            R("Se lever pour saluer Daniel, et lui expliquer pourquoi vous êtes là.",
              7, "rd1 pb1 cc1"),
        ]),
        I(6, "jeannine", "neutral",
          "Jeannine regarde sa petite-fille. Puis elle tapote la chaise à côté d'elle. « Viens "
          "là. » Océane s'assied. « Mes reins ne marchent plus très bien, ma grande. Je ne "
          "veux pas de machine. Et je ne veux pas qu'on en parle à ton père : c'est à moi de "
          "le faire. Tu peux garder ça ? » Océane hoche la tête, les yeux pleins de larmes. "
          "Jeannine vous regarde par-dessus son épaule. « Vous voyez. On n'a pas besoin de "
          "vous pour tout. »", [
            R("Sortir de la grange pour les laisser seules.", 4, "rd3 pb2"),
            R("« Océane, tu peux venir me parler quand tu veux. »", 4, "pb-2 ic-1"),
            R("Rester, et prendre la main d'Océane.", 4, "pb-1 em2"),
            R("« Il faudra bien le dire à Daniel, aussi. »", 4, "rd-2 pb-1"),
            R("Hocher la tête vers Jeannine, et rejoindre Thierry dans la cour.",
              4, "rd2 ic1 pb1"),
        ]),
        I(7, "narr", "",
          "Le soir, dans votre chambre, vous relisez le cours d'immunologie sans en retenir "
          "une ligne. Vous pensez à une boîte à biscuits pleine de papiers étiquetés, et à "
          "une fille aux cheveux violets qui a dix-sept ans, pas sept."),
        I(10, "oceane", "angry",
          "Océane vous reconnaît avant que vous ayez ouvert la bouche. « C'est toi. Le ou la "
          "stagiaire qui a appelé Jean-Paul. » Elle pose son seau, lentement. « Mon père a "
          "appris au café que mamie était malade. Devant tout le monde. Il a pleuré dans la "
          "voiture. Mon père, il ne pleure jamais. »", [
            R("« Oui, c'est moi. C'était une faute grave, et je suis désolé·e — pour ton "
              "père, et pour ta grand-mère. »", 11, "pb3 rd2 er1 co1"),
            R("« C'était une erreur du cabinet. »", 11, "pb-2 cc-1"),
            R("« Jean-Paul n'aurait jamais dû le raconter. »", 11, "pb-2 er-1"),
            R("« Comment va ton père ? »", 11, "em2"),
            R("« C'est ta grand-mère qui aurait dû le lui dire avant. »", 11, "rd-3 pb-2 em-1"),
        ]),
        I(11, "oceane", "sad",
          "Océane s'essuie les yeux d'un revers de manche, furieuse d'avoir pleuré. « Elle a "
          "quoi, mamie ? Pour de vrai ? Personne ne me dit rien, à moi. J'ai dix-sept ans, pas "
          "sept. »", [
            R("« Je ne peux pas te le dire, et cette fois je ne ferai pas d'erreur. Mais tu as "
              "le droit de le lui demander, à elle. Je crois qu'elle te le dira. »",
              12, "pb3 rd2 cc1 em1", sets=["oceane_confiance"]),
            R("« Les reins. Elle refuse la dialyse. »", 12, "pb-3 rd-2"),
            R("« Demande à la Dre Golay. »", 12, "pb1 em-1"),
            R("« Tu as raison, tu as le droit de savoir. Je vais en parler à ta "
              "grand-mère. »", 12, "pb-1 em1"),
            R("S'asseoir sur le muret à côté d'elle. « Tu as l'air seule, avec tout ça. »",
              12, "em3 co1", sets=["oceane_confiance"]),
        ]),
        I(12, "jeannine", "neutral",
          "« Océane ! Lâche la fac, elle est là pour le travail. » Jeannine est sur le seuil "
          "de la grange, appuyée sur sa canne, Thierry derrière elle. « Viens m'aider à mettre "
          "la table, ma grande. Et toi, la fac, tu restes manger la tresse ? »", [
            R("« Merci, mais le repas, c'est en famille. Je repars avec Thierry. »",
              4, "pb3 rd1"),
            R("« Avec plaisir ! »", 5, "pb-2 em1"),
            R("« Je reste, si Océane est d'accord. »", 5, "pb-1 rd1"),
            R("« Non merci, je ne mange pas chez les patients. »", 4, "rd-2 em-1 pb1"),
            R("« Merci. Océane, tes questions, c'est à ta grand-mère qu'il faut les "
              "poser. »", 4, "pb2 em-1 rd-1"),
        ]),
        I(20, "oceane", "cold-anger",
          "Océane vous dévisage. « C'est toi, la fac ? C'est toi qui as dit à papa, pour le "
          "corps de mamie ? » Elle pose ses seaux. « Depuis, il ne rentre plus dans la "
          "cuisine. Il nourrit les bêtes et il repart. Mamie mange seule. »", [
            R("« Oui. C'est moi. Je n'avais pas le droit. Je m'en veux tous les jours. »",
              21, "pb3 rd2 er1 co1"),
            R("« Il aurait fini par l'apprendre. »", 21, "rd-3 pb-3 em-1"),
            R("« Ton père a besoin de temps. »", 21, "pb-1 em1"),
            R("« Tu le savais, toi, pour le don ? »", 21, "pb-2 rd-1"),
            R("Baisser les yeux. « Je suis désolé·e. »", 21, "rd1 er1"),
        ]),
        I(21, "oceane", "sad",
          "« Moi, je trouve ça beau, le don. » Océane le dit très vite, comme une chose "
          "interdite. « Mamie dit qu'elle a passé sa vie à aider les gens à arriver, et "
          "qu'elle veut aider ceux qui soigneront les gens qui partent. » Elle hausse les "
          "épaules. « Papa dit que c'est de la boucherie. C'est vrai qu'ils vont la "
          "découper ? »", [
            R("« Ils vont l'étudier, avec beaucoup de respect. Elle restera anonyme, et à la "
              "fin, il y a une cérémonie pour remercier les donneurs. Ce respect, je suis en "
              "train de l'apprendre. Pas toujours bien. »", 12, "cc3 rd2 em1 pb1",
              sets=["oceane_confiance"]),
            R("« Oui. C'est comme ça qu'on apprend. »", 12, "rd-2 cc-1 em-2"),
            R("« Je ne peux pas parler de ta grand-mère. »", 12, "pb1 em-2"),
            R("« Pose la question à ta grand-mère. Elle te répondra mieux que moi. »",
              12, "pb2 cc1 em1", sets=["oceane_confiance"]),
            R("« Si tu veux, je peux te montrer des photos de la salle. »", 12, "rd-3 pb-3"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 2.6 Léo — histoire annexe (si Alex a inclus Léo au tutorat)
# ---------------------------------------------------------------------------
S2_6 = S(7, "2.6 Léo",
    "Samedi, 15 h. Bibliothèque universitaire, troisième étage, la table du fond. Léo vous a "
    "écrit hier : « Tu veux réviser le sang ? J'ai fait des fiches. » Il est là depuis 9 h. "
    "Ses fiches sont en deux langues.",
    focus=("em", "ic", "rd"),
    slot="2.6",
    cond=when(all=["leo_inclus"]),
    annex=True,
    nodes=[
        I(1, "leo", "vulnerable",
          "Léo pousse ses fiches vers vous. Elles sont parfaites : la cascade de la "
          "coagulation en couleurs, les globules dessinés à la règle. Dans la marge, au "
          "crayon, des mots allemands barrés et remplacés par des mots français. « Je ne "
          "comprends pas les QCM. Je connais la matière. Mais les phrases… « Laquelle des "
          "propositions suivantes n'est pas fausse ? » » Il rit, mal. « En allemand, on ne "
          "parle pas comme ça. »", [
            R("« Tes fiches sont meilleures que les miennes. Les QCM, on peut les décortiquer "
              "ensemble : je te traduis les pièges, tu m'expliques la coagulation. Deal ? »",
              2, "ic3 rd2 em2 cc1"),
            R("« Faut que tu bosses ton français, Léo. »", 3, "rd-2 em-2"),
            R("« Moi non plus, je ne comprends pas ces phrases. Personne ne les "
              "comprend. »", 2, "em2 er1"),
            R("« Il existe un soutien pour les étudiant·e·s allophones. Tu devrais "
              "demander. »", 2, "ic1 cc1 em-1"),
            R("Prendre ses fiches en photo, pour vous.", 3, "rd-2 ic-1 pb-1"),
        ]),
        I(2, "leo", "happy",
          "Pendant deux heures, ça marche. Vous traduisez les pièges des QCM ; il vous "
          "explique pourquoi le facteur VIII et le facteur IX ne se trompent jamais de rôle. "
          "À 17 h, il range ses fiches, puis s'arrête. « Je peux te dire un truc ? Je n'ai "
          "parlé à personne, en dehors des cours, depuis septembre. Personne. Le week-end, je "
          "rentre à Bienne, et je ne dis pas à ma mère que je suis seul ici. »", [
            R("« Merci de me le dire. Ce n'est pas rien, d'arriver seul dans une volée qui se "
              "connaît déjà. Tu viens vendredi, à la soirée de la table 14 ? Je te présente, "
              "vraiment. »", 4, "em3 ic2 co1", sets=["leo_allie"]),
            R("« Ça va s'arranger, tu verras. »", 6, "em-1 cc-1"),
            R("« Tu devrais en parler au service de consultation psychologique. »",
              6, "ic1 em-1"),
            R("Rester silencieux·se, et attendre qu'il continue.", 5, "em2 co1"),
            R("« Ah ouais, c'est dur. Bon, j'y vais, je retrouve des potes. »",
              6, "em-3 co-2"),
        ]),
        I(3, "leo", "ashamed",
          "Léo ramasse ses fiches, lentement. « Oui. Bien sûr. » Il ne dit plus rien pendant "
          "une heure. À 16 h, il s'en va en murmurant un « merci » qui n'en est pas un.", [
            R("Le rattraper dans l'escalier : « Léo, attends. C'était nul, ce que j'ai dit. "
              "Tes fiches sont géniales. On recommence ? »", 2, "rd2 em2 er1 ic1"),
            R("Le laisser partir.", END, "em-1 ic-1"),
            R("Lui envoyer un message : « merci pour les fiches ! »", END, "ic1 rd-1"),
            R("Raconter à Maëlle que Léo est « un peu bizarre ».", END, "rd-3 pb-2"),
        ]),
        I(4, "narr", "",
          "En sortant de la bibliothèque, il fait déjà nuit. Léo vous serre la main, trop "
          "formellement, puis rit de lui-même. « Merci. » Dans le bus, vous recevez une "
          "photo : la fiche de la cascade de la coagulation, avec, au crayon, dans un coin : "
          "« für Alex — pour Alex »."),
        I(5, "leo", "vulnerable",
          "« À Zurich, j'avais un groupe. On faisait du POL, les tutorats par problèmes, tous "
          "les jeudis. On finissait toujours à la même pizzeria. » Il fait tourner son "
          "crayon. « Ici, au tutorat, j'ai les réponses. Je ne les dis pas, parce que j'ai peur "
          "de mal dire. Alors on croit que je ne sais rien. »", [
            R("« Jeudi, au tutorat, tu as vu ce que personne n'avait vu, page deux. Tout le "
              "monde l'a entendu. Recommence. Et si tu bloques sur un mot, dis-le en "
              "allemand : je t'aiderai à le traduire. »", 4, "ic3 em2 rd2",
              sets=["leo_allie"]),
            R("« Faut juste oser. »", 6, "cc1 em-1"),
            R("« Tu devrais peut-être retourner à Zurich. »", 6, "em-2 ic-2 rd-1"),
            R("« On pourrait se faire une pizzeria du jeudi, nous aussi. »", 4, "ic2 em2",
              sets=["leo_allie"]),
        ]),
        I(6, "narr", "",
          "Vous sortez ensemble de la bibliothèque. Léo vous serre la main, trop "
          "formellement. « Merci pour les QCM. » Il part vers la gare. Le samedi suivant, il "
          "révise seul, à la même table du fond."),
    ],
)

CH2 = C(2, "Deux Pittet",
    situation=(
        "Octobre et novembre. À la fac, le module sang, immunité, microbes, et un tutorat du "
        "jeudi où Noah répond à tout avec un chatbot. Au cabinet de Montchéry, c'est la "
        "saison des vaccins et des prises de sang. Et dans le logiciel, il y a deux "
        "« Pittet J. »."
    ),
    objectives=(
        "informer un parent hésitant sans pression ni leçon, dans les limites de son rôle ; "
        "vérifier l'identité avant toute information au téléphone et ne donner aucun "
        "résultat (secret médical, art. 321 CP) ; reconnaître une erreur et s'excuser sans "
        "se défausser sur un·e collègue ; contribuer à un travail de groupe sans prendre le "
        "pouvoir ni se taire ; refuser de partager un travail personnel qui servira à "
        "plagier ; respecter le refus de traitement éclairé d'une patiente ; parler à une "
        "adolescente sans trahir sa grand-mère ; inclure un pair isolé."
    ),
    anchoring=(
        "UNIL BMed2.2 (sang, immunité, microbes ; épidémiologie), BMed2.8 (anamnèse et "
        "communication) et BMed2.7 (équipe interprofessionnelle) · UNIGE dimensions "
        "communautaires (médecine ambulatoire, éthique, santé publique), APP/CBCL, plagiat "
        "et IA générative, stage IMFE · UZH Humanbiologie I (Blut und Immunsystem), "
        "POL-Tutorat I."
    ),
    focus=("pb", "cc", "ic", "rd"),
    scenes=[S2_1, S2_2, S2_3, S2_4A, S2_4B, S2_5, S2_6],
)
