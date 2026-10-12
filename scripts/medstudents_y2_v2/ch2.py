"""Chapitre 2 — Deux Pittet (octobre-décembre).

Cinq scènes jouées (six avec l'histoire annexe), sept écrites :
  2.1 Le jour des vaccins (la mère qui hésite, puis le téléphone et les deux « Pittet J. »)
  2.2 L'APP du jeudi
  2.3 branche parallèle : « Le Café de la Gare » (Alex a appelé le mauvais Pittet)
      ou « La créatinine »
  2.4 Le dimanche aux Combettes
  2.5 histoire annexe « Léo » (si Alex a inclus Léo au tutorat)
  2.6 BLS (mi-décembre, au centre de simulation)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 2.1 Le jour des vaccins — le matin, une mère qui hésite ; l'après-midi, le téléphone
# ---------------------------------------------------------------------------
S2_1 = S(1, "2.1 Le jour des vaccins",
    "Jeudi, fin octobre. Journée de vaccination contre la grippe au cabinet de Montchéry : "
    "quarante rendez-vous, une file jusque sur le trottoir, Sandra au bord de l'implosion. "
    "La Dre Golay vaccine à la chaîne dans la salle 1. Dans la salle 2 attendent une jeune "
    "mère et son bébé de deux mois, pour le contrôle et les premiers vaccins.",
    focus=("cc", "pb", "em", "ic"),
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
            "Le matin, vous avez écouté une mère inquiète sans la juger ni décider pour elle ; "
            "l'après-midi, vous avez appelé la bonne Pittet. Au téléphone : vérifier "
            "l'identité avant de parler, ne donner aucun résultat, transmettre fidèlement ce "
            "que la patiente demande de transmettre — ici, son refus de la dialyse, qui "
            "appartient à l'entretien avec la Dre Golay.")),
    ],
    nodes=[
        I(1, "golay", "neutral",
          "La Dre Golay vous attrape au passage, une seringue dans chaque main. « Alex, vous "
          "commencez avec Mme Duc, en salle 2 ? Comment va le bébé, l'alimentation, le "
          "sommeil. Elle a des questions sur les vaccins : écoutez, ne promettez rien. Je "
          "reviens dans dix minutes. » Elle repart vers la salle 1.", [
            R("« D'accord : j'écoute ses questions, je les note, et je vous les transmets. »",
              2, "pb3 ic2 cc1"),
            R("« Je peux lui expliquer moi-même : on a eu le cours d'immunologie la semaine "
              "passée, je connais les adjuvants et le calendrier vaccinal suisse. »",
              2, "pb-2 ic-1 cc-1"),
            R("« Je préférerais attendre que vous soyez là. »", 2, "pb1 ic-1 em-1"),
            R("« Qu'est-ce qu'elle a comme questions, à peu près ? Je préfère savoir à quoi "
              "m'attendre avant d'entrer. »", 2, "ic2 cc1 er1"),
            R("Hocher la tête sans rien dire.", 2, "ic-1"),
        ]),
        I(2, "duc", "anxious",
          "Salle 2. Une jeune femme, un bébé endormi contre elle, un sac à langer qui "
          "déborde. Elle parle vite. « Bonjour. Coralie. Lui, c'est Elio, il a deux mois. » "
          "Elle sort son téléphone. « J'ai lu des trucs. L'aluminium, les vaccins à six "
          "maladies d'un coup, l'autisme. Six maladies à deux mois, ça fait beaucoup, "
          "non ? »", [
            R("« Vous avez beaucoup lu. Qu'est-ce qui vous fait le plus peur ? »",
              3, "em3 cc2 rd1 co1"),
            R("« L'histoire de l'autisme, c'est une fraude, ça a été démontré : l'étude a été "
              "retirée, et son auteur a perdu son droit d'exercer. »", 4, "cc1 rd-2 em-2 pb-1"),
            R("« Les gens qui écrivent ça sur internet ne sont pas médecins. »",
              4, "rd-2 em-2 cc-1"),
            R("« Je suis étudiant·e, je ne peux pas vous conseiller. Attendez la Dre. »",
              5, "pb2 em-2 cc-1"),
            R("« Ce sont de vraies questions. Je les note toutes pour la Dre, une par une, et "
              "vous me dites si j'en oublie. »", 3, "cc2 pb2 em1 ic1"),
            R("Lui montrer sur votre téléphone les chiffres de couverture vaccinale de "
              "l'OFSP.", 4, "cc-1 em-1 pb-1"),
        ]),
        I(3, "duc", "vulnerable",
          "Elle caresse la tête du bébé. « Ma sœur a un garçon autiste. Il avait quinze mois "
          "quand il a arrêté de parler. Juste après un vaccin. » Un temps. « Tout le monde me "
          "dit que ça n'a rien à voir. Personne ne nous a jamais dit pourquoi il avait "
          "arrêté de parler, alors. »", [
            R("Laisser un silence. « Personne ne vous a jamais expliqué ce qui est arrivé à "
              "votre neveu. Et vous avez peur que ça arrive à Elio. »", 12, "em3 co2 cc1"),
            R("« C'est une coïncidence de calendrier : l'autisme se manifeste souvent à "
              "cet âge-là. »", 12, "cc2 em-1 pb-1 co-1"),
            R("« Je comprends. Moi aussi, je serais méfiant·e. »", 12, "pb-2 cc-2 em1"),
            R("« Ça doit être dur, pour votre sœur. Et pour vous. »", 12, "em2 co2"),
            R("« Vous voulez que la Dre vous explique ce qu'on sait sur ce lien ? »",
              12, "cc2 ic1 em1 pb1"),
        ]),
        I(4, "duc", "angry",
          "Coralie se raidit. Elio se réveille et se met à pleurer. « Super. Encore quelqu'un "
          "qui me prend pour une idiote. » Elle range son téléphone. « Je vais attendre la "
          "Dre, merci. »", [
            R("« Pardon. J'ai répondu à côté. »", 3, "rd2 em2 er1"),
            R("« Je vous donnais juste les faits. »", 7, "er-1 em-1"),
            R("Se taire, et regarder le bébé qui pleure.", 7, "er1 em-1 co-1"),
            R("« Si vous ne le faites pas vacciner, c'est lui qui en paiera le prix, pas vous : "
              "la coqueluche, à deux mois, ça peut tuer. »", 7, "rd-3 em-3 pb-2 co-1"),
            R("Lui proposer un verre d'eau, et aller prévenir la Dre qu'elle a des "
              "questions.", 7, "rd1 ic1 cc1"),
        ]),
        I(5, "duc", "sad",
          "« Ah. » Elle baisse les yeux sur le bébé. « Tout le monde me renvoie à quelqu'un "
          "d'autre. » Un silence s'installe. Elio tète son poing.", [
            R("« Pardon. Je ne décide pas, mais je peux vous écouter. »", 3,
              "em2 rd2 pb1 cc1 co1"),
            R("Remplir le formulaire de prévention, en silence, pour avoir quelque chose à "
              "faire avec les mains en attendant que la Dre revienne.", 7, "em-2 co-1"),
            R("« Elle ne va pas tarder. »", 7, "em-1 co-1"),
            R("« Il a l'air en pleine forme, Elio. Il dort bien ? Il mange bien ? Il vous "
              "laisse dormir un peu, la nuit ? »", 3, "em1 cc1 rd1"),
            R("« Ce n'est pas moi qui ai fait les vaccins, je n'y peux rien. »",
              7, "em-2 rd-1 cc-1"),
        ]),
        I(12, "duc", "vulnerable",
          "Coralie berce Elio, qui s'est rendormi. Puis, sans vous regarder : « Et vous ? Si "
          "c'était votre bébé, vous le feriez ? »", [
            R("« Moi, oui. Mais c'est vous qui décidez. »", 6, "cc2 em2 pb1 rd1"),
            R("« Bien sûr, tout le monde le fait. »", 6, "rd-1 em-1 cc-1"),
            R("« Je ne peux pas répondre à ça. »", 6, "pb1 em-2 cc-1"),
            R("« Oui, sans hésiter. Ne pas vacciner un bébé aujourd'hui, avec tout ce qu'on "
              "sait sur la coqueluche et la rougeole, c'est prendre un risque énorme pour lui "
              "et pour les autres bébés. »", 6, "pb-2 em-2 cc1 rd-1"),
            R("« Je vous dirai ce que j'en pense, mais pas maintenant : la Dre arrive. »",
              6, "pb-1 cc-1"),
        ]),
        I(6, "golay", "neutral",
          "La Dre Golay revient, essoufflée, et s'assied. « Alors ? » Coralie vous regarde. "
          "La Dre aussi : c'est à vous de résumer.", [
            R("« Mme Duc a des questions sur l'aluminium, le nombre de vaccins, et surtout "
              "l'autisme : son neveu a cessé de parler à quinze mois, juste après un vaccin, "
              "et personne ne lui a jamais expliqué pourquoi. »", 8, "cc3 ic2 rd2 em2"),
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
            R("Avant de sortir : « Elle a des questions importantes. Je crois que je l'ai "
              "brusquée. Pardon. »", 10, "pb2 rd2 ic2 er1"),
            R("Sortir sans un mot.", 10, "ic-1 er-1"),
            R("« Elle refuse les vaccins. »", 10, "rd-3 cc-2"),
            R("« Je lui ai juste donné les faits : l'étude sur l'autisme est une fraude, "
              "l'aluminium est en quantité infime, et les vaccins combinés sont testés "
              "ensemble. »", 10, "er-1 ic-1 pb-1"),
            R("« D'accord. » Et se promettre de demander plus tard à la Dre comment elle s'y "
              "prend avec les parents inquiets.", 10, "er1 ic1"),
        ]),
        I(8, "golay", "happy",
          "La Dre Golay se tourne vers Coralie. Elle ne sort ni brochure ni statistique. "
          "« Votre neveu, il a quel âge, maintenant ? » Pendant vingt minutes, elle parle de "
          "l'autisme, des premiers signes, de ce qu'on sait et de ce qu'on ne sait pas. Puis "
          "de la coqueluche, qu'Elio pourrait attraper dans la file de la Migros. Coralie "
          "pose ses questions une par une. À la fin : « Je peux réfléchir une semaine ? — "
          "Bien sûr. Revenez quand vous voulez, sans rendez-vous. » Quand la porte se "
          "referme, la Dre vous regarde. « Qu'est-ce que vous avez vu ? »", [
            R("« Vous avez répondu à sa peur, pas à internet. »", 11, "cc2 rd2 em2"),
            R("« Qu'elle ne l'a pas fait vacciner. C'est un échec, non ? Avec la coqueluche "
              "qui circule, une semaine de réflexion, c'est une semaine de risque. »",
              11, "rd-1 er-1 cc-1"),
            R("« Vous êtes restée vingt minutes, alors que la file va jusqu'à la Migros. »",
              11, "ic2 cc1"),
            R("« Qu'elle a le droit de réfléchir, et que vous le lui avez dit. »",
              11, "rd3 pb1"),
            R("« Que ça prend trop de temps, pour un cabinet comme le vôtre. »",
              11, "rd-1 ic-1"),
        ]),
        I(9, "golay", "cold-anger",
          "La Dre Golay ne vous répond pas. Elle se tourne vers Coralie, qui a entendu. « Je "
          "ne vous mets dans aucune case, Madame Duc. Racontez-moi. » Plus tard, dans le "
          "couloir : « Alex. Un mot, et une maman ne revient plus jamais. Les étiquettes, on "
          "les laisse aux pots de confiture. »", [
            R("« Vous avez raison. C'était injuste. »", 11, "rd2 er2 pb1 em1"),
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
          "12 h 30. La Dre Golay mange une pomme debout, entre deux patients. « La moitié de "
          "la médecine de famille, c'est ça : des gens qui ont peur et qui ont lu des choses. "
          "On ne gagne jamais contre internet. On gagne contre la peur, un patient à la "
          "fois. » Elle jette le trognon. « Coralie reviendra. Ou pas. Ce sera son choix, et "
          "on l'aura respecté. »", [
            R("« Et si elle ne revient pas, et qu'Elio attrape la coqueluche ? »",
              21, "em1 cc1 er1"),
            R("« J'ai appris plus ce matin qu'en trois semaines d'immunologie. »",
              21, "er1 rd1 cc1"),
            R("« Moi, je l'aurais obligée. »", 21, "rd-3 pb-2"),
            R("« Comment vous faites pour ne jamais vous énerver ? »",
              21, "er1 ic1 rd-1"),
            R("« Merci de m'avoir laissé·e seul·e avec elle. J'ai vu ce que je ne sais pas "
              "encore faire. »", 21, "er2 pb2 ic1"),
        ]),
        I(21, "sandra", "anxious",
          "16 h 20. Les résultats du laboratoire arrivent d'un coup, par fax. La Dre Golay est "
          "partie en visite à domicile ; Sandra a six personnes au comptoir et le téléphone "
          "qui sonne sans arrêt. Elle vous tend un post-it sans lever les yeux de son écran. "
          "« Rappelle Pittet, s'il te plaît. La Dre veut la voir lundi pour ses résultats. Le "
          "numéro est dans le dossier. » Le post-it dit : « Pittet — résultats — RDV lundi "
          "Dre ». Rien d'autre.", [
            R("« Quel Pittet ? Il y en a plusieurs au village. Tu as une date de "
              "naissance ? »", 22, "pb3 cc2 ic2"),
            R("« D'accord. » Ouvrir le logiciel et taper « Pittet ».", 23, "pb-1"),
            R("« Je n'ai pas le droit de téléphoner aux patients, si ? »", 24, "pb1 ic-1"),
            R("« Qu'est-ce que je dis, si on me demande les résultats au téléphone ? Je "
              "préfère savoir avant d'appeler, pour ne pas improviser devant le patient. »",
              25, "pb2 cc2 ic1"),
            R("« Je fais ça après ma pause. »", 23, "ic-2 rd-1"),
        ]),
        I(22, "sandra", "grateful",
          "Sandra fouille la pile de fax du laboratoire. « Pittet J., 81 ans. Créatinine en "
          "hausse, la Dre veut la voir lundi. » Elle souffle. « Jeannine. Pas Jean-Paul. "
          "J'allais te faire appeler le mauvais. Des Pittet, ici, il y en a onze. » Elle "
          "vous tend le fax. « Le rendez-vous, et rien d'autre au téléphone. C'est la Dre qui "
          "explique. »", [go(26)]),
        I(23, "narr", "",
          "Vous tapez « Pittet ». Onze résultats. Deux « Pittet J. » ont eu une prise de sang "
          "cette semaine : Pittet Jean-Paul, né en 1967, et Pittet Jeannine, née en 1944. Le "
          "fax du laboratoire, sur le comptoir, dit seulement « Pittet J. — 81 ans — "
          "créatinine en hausse — convoquer ». Le premier de la liste est Jean-Paul.", [
            R("Vérifier l'âge sur le fax : 81 ans. C'est Jeannine.", 26, "pb3 cc2 er1"),
            R("Ouvrir le premier de la liste et composer le numéro.", 27, "pb-2 cc-1"),
            R("Demander à Sandra : « Pittet J., c'est Jean-Paul ou Jeannine ? »",
              22, "pb2 ic2 cc1"),
            R("Appeler les deux, l'un après l'autre : celui qui a fait une prise de sang cette "
              "semaine le dira bien, et on gagnera du temps sur la file du comptoir.",
              27, "pb-3 cc-2"),
            R("Rendre le post-it à Sandra : vous ne savez pas qui appeler.", 22,
              "pb1 ic1 cc-1"),
        ]),
        I(24, "sandra", "annoyed",
          "« Prendre un rendez-vous, oui. Donner des résultats, non. » Elle vous tend le "
          "combiné. « Tu dis : la Dre aimerait vous voir lundi pour discuter de vos résultats. "
          "Et rien d'autre. Tu t'en sors ? »", [
            R("« Oui. Identité d'abord. »", 22, "pb3 cc1 ic2"),
            R("« Oui, oui. »", 23, "cc-1"),
            R("« Et si c'est un proche qui répond ? »", 25, "pb2 cc1"),
            R("« Franchement, le secrétariat, ce n'est pas mon rôle. »", 23, "ic-3 rd-2"),
            R("Prendre le combiné et chercher le numéro.", 23, "pb-1"),
        ]),
        I(25, "sandra", "neutral",
          "« Rien. » Sandra cale le combiné contre son épaule. « Tu ne donnes aucun résultat "
          "au téléphone. Tu vérifies que tu parles à la bonne personne — nom, prénom, date de "
          "naissance — et tu dis que la Dre veut la voir. Si quelqu'un d'autre répond, même le "
          "mari, même le fils : tu demandes qu'elle rappelle le cabinet. Point. » Un temps. "
          "« Et c'est Pittet Jeannine. Pas Jean-Paul. »", [go(26)]),
        I(26, "jeannine", "neutral",
          "Trois sonneries. « Pittet. » Une voix de femme, un peu essoufflée. Derrière, un "
          "chien qui aboie.", [
            R("« Ici Alex, du cabinet. Mme Jeannine Pittet ? Votre date de naissance ? »",
              28, "pb3 cc2 rd2 ic1"),
            R("« Madame Pittet ? C'est pour vos résultats : votre créatinine a augmenté, la Dre "
              "aimerait vous voir lundi pour en parler, et peut-être adapter votre "
              "traitement. »", 29, "pb-2 cc-1"),
            R("« Madame Pittet, la Dre aimerait vous voir lundi pour vos résultats. »",
              28, "pb-1 cc1"),
            R("« Bonjour Madame Pittet ! Comment vont vos chevilles, depuis la dernière fois ? "
              "Et le chat ? »", 28, "rd1 em1 pb-1"),
            R("« C'est le petit de la fac. La Dre veut vous voir, c'est pour vos reins. »",
              29, "pb-2 cc-1 rd-1"),
        ]),
        I(27, "jeanpaul", "neutral",
          "« Pittet ! » Une voix d'homme, une télé derrière. Vous lancez : « Bonjour, ici le "
          "cabinet de la Dre Golay, c'est pour vos résultats de prise de sang… » — « Mes "
          "résultats ? J'ai fait que le cholestérol, moi. » Un temps. « C'est pas plutôt pour "
          "la Jeannine, ça ? Elle était au cabinet jeudi. Qu'est-ce qu'elle a, la "
          "Jeannine ? »", [
            R("« Erreur de ma part, pardon. Au revoir. » Et raccrocher.", 32, "pb3 cc2 er1",
              sets=["appel_rattrape"]),
            R("« Ah, pardon ! Oui, c'est pour Mme Jeannine Pittet. Vous la connaissez ? Vous "
              "pourriez lui dire de rappeler le cabinet, s'il vous plaît, si vous la voyez au "
              "village ? »", 34, "pb-2 cc-1", sets=["erreur_homonyme"]),
            R("« Rien de grave : ses reins fatiguent un peu. Dites-lui de rappeler la Dre. »",
              33, "pb-3 cc-2 rd-2", sets=["erreur_homonyme", "info_lachee"]),
            R("« Je ne peux rien vous dire. » Puis : « Vous savez si elle est chez elle ? »",
              34, "pb-1 cc-1", sets=["erreur_homonyme"]),
            R("Raccrocher brusquement, sans rien dire.", 32, "pb1 rd-2 cc-2",
              sets=["appel_rattrape"]),
        ]),
        I(28, "jeannine", "happy",
          "« C'est moi. 4 mai 1944, si vous voulez tout savoir. » Elle rit. « Lundi ? Ça doit "
          "être les reins, hein. La Dre m'avait prévenue. C'est mauvais ? Vous pouvez me le "
          "dire, à moi, je ne vais pas m'évanouir. »", [
            R("« Ce n'est pas à moi de les lire. La Dre vous expliquera lundi. »", 30, "pb3 cc2 rd1"),
            R("« Votre créatinine est à 212. C'est assez haut. »", 29, "pb-3 cc-1"),
            R("« Je crois que c'est sérieux, oui. »", 29, "pb-2 cc-2 em-1 co-1"),
            R("« Vous avez l'air inquiète. Vous voulez qu'on avance le rendez-vous ? »",
              30, "em2 pb1 ic1 co1"),
            R("« Ne vous inquiétez pas, ce n'est sûrement rien. »", 30, "cc-3 pb-2"),
        ]),
        I(29, "jeannine", "resigned",
          "Un silence. « Ah. » Puis, plus bas : « Bon. Dites à la Dre que je sais ce que ça "
          "veut dire, et que je ne ferai pas de dialyse. Je ne vais pas passer trois "
          "après-midi par semaine branchée à une machine à Yverdon. » Elle raccroche avant "
          "que vous ayez répondu.", [
            R("Prévenir Sandra : « J'ai trop parlé. Il faut le dire à la Dre. »",
              31, "pb2 ic3 er1 cc1", sets=["bon_pittet"]),
            R("Noter « RDV lundi », et passer à la suite.", 31, "pb-1 ic-1",
              sets=["bon_pittet"]),
            R("La rappeler pour s'excuser, et lui donner les chiffres exacts, puisqu'elle a "
              "de toute façon compris.", 31, "pb-3 cc-1", sets=["bon_pittet"]),
            R("Ne rien dire à personne.", 31, "pb-2 ic-2", sets=["bon_pittet"]),
            R("Écrire dans le dossier, en majuscules : « REFUSE LA DIALYSE », pour que la Dre "
              "le voie.", 31, "pb-1 cc1 ic1 rd-1", sets=["bon_pittet"]),
        ]),
        I(30, "jeannine", "neutral",
          "« Hm. Vous êtes bien dressé·e. » Elle rit. « Lundi, alors. Dites à la Dre que je "
          "sais ce que ça veut dire, les reins, à mon âge. Et que je ne ferai pas de "
          "dialyse. Elle comprendra. »", [
            R("« Je le lui dirai mot pour mot. Et lundi, vous pourrez le lui dire vous-"
              "même. »", 31, "cc2 rd2 ic1 pb1", sets=["bon_pittet"]),
            R("« Il ne faut pas dire ça, Madame Pittet. La dialyse, ça peut vous sauver : il y "
              "a des gens qui vivent dix ans avec, et qui continuent à voyager. »",
              31, "rd-2 pb-2", sets=["bon_pittet"]),
            R("« D'accord. » Et raccrocher.", 31, "cc-1 ic-1", sets=["bon_pittet"]),
            R("« Vous voulez que quelqu'un vous accompagne lundi ? »", 31, "em1 cc1 co2",
              sets=["bon_pittet"]),
            R("« Vous avez le droit de refuser. Mais parlez-en d'abord avec la Dre : elle vous "
              "dira ce que ça implique. »", 31, "rd2 cc2 pb1", sets=["bon_pittet"]),
        ]),
        I(31, "sandra", "neutral",
          "Sandra raccroche son propre téléphone au même moment. « Alors ? » Vous lui "
          "transmettez le rendez-vous. Elle note, puis, sans lever les yeux : « Elle t'a dit, "
          "pour la dialyse ? » Vous hochez la tête. « À moi aussi, il y a deux ans. La Dre "
          "l'avait écoutée. » Elle colle un post-it jaune sur son écran, en gros : « PITTET J. "
          "= 2 ! DATE DE NAISSANCE ! »"),
        I(32, "sandra", "anxious",
          "Vous raccrochez, le cœur battant. Sandra a entendu, entre deux patients. « C'était "
          "Jean-Paul ? » Vous hochez la tête. « Il a su quelque chose ? » — « Qu'on appelait "
          "pour des résultats. Il a deviné que c'était pour Jeannine. »", [
            R("« Je n'ai pas vérifié l'identité avant de parler. Je le note, et je le dis à la "
              "Dre ce soir. »", 37, "pb3 ic2 cc1"),
            R("« Il n'a rien su, c'est l'essentiel. »", 37, "pb-1 er1"),
            R("« C'est ton post-it qui n'était pas clair. »", 37, "ic-2 pb-1"),
            R("« On pourrait faire quelque chose pour les homonymes, non ? Une alerte dans le "
              "logiciel, une couleur différente, la date de naissance affichée en gros à côté "
              "du nom ? »", 37, "ic3 cc1 pb1"),
            R("Se taire, et passer au patient suivant.", 37, "pb-1 ic-1"),
        ]),
        I(33, "jeanpaul", "suspicious",
          "« Les reins ? » Jean-Paul baisse le son de la télé. « Elle va devoir aller à la "
          "dialyse, alors. Comme le père Bovay. Il a pas tenu six mois. » Il a l'air presque "
          "content d'avoir une nouvelle. « Elle le sait, au moins ? Et Daniel ? »", [
            R("« Je n'aurais jamais dû vous dire ça. Je vous demande de n'en parler à "
              "personne. Je dois prévenir la Dre. »", 35, "pb2 cc2 er1"),
            R("« Elle refuse la dialyse, de toute façon. Elle l'a dit à la Dre il y a deux "
              "ans, alors… »", 35, "pb-3 rd-2 cc-1"),
            R("« Je ne sais pas. » Et raccrocher.", 35, "pb-1 er-1"),
            R("« Vous pourriez prévenir Daniel ? »",
              35, "pb-3 ic-1"),
            R("« Je ne peux rien dire de plus. Au revoir. »", 35, "pb1 cc1"),
        ]),
        I(34, "jeanpaul", "suspicious",
          "« Ah, la Jeannine. » Jean-Paul baisse le son de la télé. « Elle va pas fort, hein ? "
          "On la voit plus au culte. C'est quoi, son problème ? Le cœur ? »", [
            R("« Erreur de numéro. »", 35,
              "pb3 cc1"),
            R("« Non, c'est plutôt les reins. »", 33, "pb-3 cc-1", sets=["info_lachee"]),
            R("« Vous êtes de la famille ? »", 35, "pb-2 cc-1"),
            R("Raccrocher.", 35, "pb1 rd-1 cc-1"),
            R("« Je ne sais pas. Vous la voyez souvent ? »", 35, "pb-2 em1"),
        ]),
        I(35, "sandra", "anxious",
          "Vous raccrochez. Sandra a tout entendu, entre deux patients. Elle vous regarde. "
          "« C'était Jean-Paul ? » Elle ferme les yeux une seconde. « Jean-Paul, c'est la "
          "radio du village. Ce soir, tout le Café de la Gare saura. »", [
            R("« Oui. C'est ma faute. Il faut prévenir la Dre, et Jeannine. »",
              36, "pb3 ic2 er1 cc1 rd1"),
            R("« Tu ne m'avais pas dit lequel. »", 36, "ic-2 pb-2 er-1"),
            R("« Il ne dira rien, il avait l'air gentil, et puis il n'a rien appris de "
              "précis : il a juste deviné qu'on appelait pour quelqu'un de sa famille. »",
              36, "pb-2 cc-1"),
            R("« On pourrait ne rien dire. Ça va peut-être passer, il oubliera d'ici ce "
              "soir. »", 36, "pb-3 ic-2 rd-1"),
            R("« Qu'est-ce que je dois faire ? »", 36, "ic2 er1"),
        ]),
        I(36, "narr", "",
          "Sandra appelle la Dre Golay sur son portable. Vous l'entendez dire : « Non, c'est "
          "l'étudiant·e. Oui. Jean-Paul. » Puis plus rien. Elle raccroche et vous tend, sans "
          "un mot, le formulaire de déclaration d'incident du cabinet."),
        I(37, "sandra", "neutral",
          "Sandra colle un post-it jaune sur son écran, en gros : « PITTET J. = 2 ! DATE DE "
          "NAISSANCE ! » « Voilà notre système d'alerte. » Elle rit, nerveusement. « La Dre "
          "appellera Jeannine elle-même. Et Jean-Paul, je m'en occupe : il me doit une tarte "
          "aux pruneaux. »"),
    ],
)

# ---------------------------------------------------------------------------
# 2.2 L'APP du jeudi
# ---------------------------------------------------------------------------
S2_2 = S(2, "2.2 L'APP du jeudi",
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
              2, "ic3 rd2 cc1", sets=["leo_inclus"]),
            R("« J'anime. » Et prendre aussi le feutre.", 2, "ic-1 cc1"),
            R("« Noah, t'as l'air prêt, vas-y. »", 2, "ic1"),
            R("Attendre que quelqu'un se dévoue.", 2, "ic-1"),
            R("« On tourne : chaque séance, quelqu'un de différent. Aujourd'hui j'écris, "
              "Yasmine anime, et la semaine prochaine on change. »", 2, "ic2 cc2 er1"),
            R("« Franchement, l'APP, c'est du temps perdu. On lit le cours, et c'est "
              "réglé. »", 2, "ic-3 rd-1 er-1"),
        ]),
        I(2, "noah", "happy",
          "Noah démarre avant tout le monde. « Anémie microcytaire, ferriprive, "
          "probablement des règles abondantes. Bilan martial, ferritine, et on cherche une "
          "cause digestive si elle a plus de cinquante ans, ce qui n'est pas le cas. » Il "
          "tourne son écran : un chatbot vient de lui écrire une réponse impeccable, "
          "références comprises. « Voilà. On a fini ? » Maëlle rit. Yasmine non.", [
            R("« Peut-être. Mais qu'est-ce qu'on sait, nous, sans l'écran ? »",
              3, "ic3 cc2 pb1"),
            R("« Génial, on gagne une heure. On peut aller boire un café et revenir à midi "
              "pour signer la feuille de présence. »", 4, "ic-2 pb-2"),
            R("Recopier la réponse du chatbot au tableau.", 4, "ic-1 pb-1 cc-1"),
            R("« Léo, tu avais souligné quelque chose dans le cas, non ? »", 5, "ic3 rd1",
              sets=["leo_inclus"]),
            R("Regarder le Dr Ibarra, pour qu'il intervienne et remette un peu d'ordre dans "
              "la séance.", 3, "ic-1 er-1"),
        ]),
        I(3, "yasmine", "angry",
          "Yasmine décroise les bras. « Le chatbot ne sait pas que Mme R. a trois enfants, un "
          "mari qui travaille de nuit, et qu'elle ne mange presque plus de viande depuis "
          "qu'elle a perdu son travail. C'est page deux. » Elle regarde Noah. « Toi non plus, "
          "d'ailleurs. T'as pas lu la page deux. » Noah rougit. Le silence devient lourd.", [
            R("« Les deux au tableau : la page deux, et le départ de Noah ? »",
              5, "ic3 cc2 em2 er1"),
            R("« Yasmine, calme-toi. »", 5, "ic-1 rd-1 er-1"),
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
            R("« Elle a perdu son travail. Elle a peur de ce que ça coûte. »",
              5, "cc2 ic1 em2"),
            R("« Parce qu'elle ne savait pas qu'elle était malade ? »", 5, "cc1"),
            R("« Ce n'est pas médical, comme question. »", 5, "rd-2 ic-1"),
            R("Se tourner vers Léo, qui a levé la main sans oser parler : « Léo ? »",
              5, "ic3 rd2 em1", sets=["leo_inclus"]),
            R("Poser la question au chatbot de Noah.", 5, "pb-2 ic-1"),
        ]),
        I(5, "leo", "vulnerable",
          "Léo s'éclaircit la gorge. « Page deux. Elle donne sa viande aux enfants. Elle a dit "
          "à la pharmacienne : « Moi, je mange ce qui reste. » » Il cherche ses mots. « Bei "
          "uns… à Zurich, on appelait ça… les déterminants… sociaux ? La cause, ce n'est pas "
          "seulement les règles. C'est l'argent. » Personne ne dit rien. Puis Maëlle : "
          "« Ouah. »", [
            R("Écrire au tableau : « Précarité ». Et dessous : « Léo ».", 13, "ic3 rd2 cc1", sets=["leo_inclus"]),
            R("« Bien vu. » Et passer à la suite.", 13, "ic1"),
            R("« On dit « déterminants sociaux », oui. Et « bei uns », ici, on dit « chez "
              "nous ». »", 13, "rd-2 ic-1 em-1"),
            R("« Noah, ton chatbot avait vu ça ? »", 13, "ic-1 em-1"),
            R("« Alors une ordonnance de fer ne suffira pas. Qui, dans le réseau de soins, "
              "peut l'aider pour l'argent ? L'assistante sociale de la commune ? »",
              13, "ic3 cc2"),
        ]),
        I(13, "maelle", "happy",
          "Maëlle se frotte les mains. « Bon. Objectifs d'apprentissage : on en a cinq. On se "
          "les répartit, chacun demande un résumé à l'IA, on colle tout dans un document, et "
          "jeudi c'est plié. » Noah hoche la tête. Yasmine lève les yeux au ciel.", [
            R("« Chacun écrit le sien. Et on dit si on a utilisé une IA. »",
              14, "ic2 pb3 cc1"),
            R("« Super idée. » Et ouvrir le chatbot.", 14, "pb-2 ic-1"),
            R("« Fais ce que tu veux. Moi, je travaille seul·e, comme ça au moins je sais ce "
              "que je rends. »", 14, "ic-3 em-1"),
            R("« Et Léo et Yasmine, ils en pensent quoi ? Ils n'ont rien dit depuis le début "
              "de la discussion. »", 14, "ic3 rd1"),
            R("« L'IA se trompe sur les références, j'ai lu un article là-dessus : elle invente "
              "des études qui n'existent pas. »", 14, "cc1 pb1"),
        ]),
        I(14, "ibarra", "neutral",
          "Midi moins le quart. Le Dr Ibarra se lève enfin. « Avant de partir : un tour de "
          "table. Qu'est-ce qui a aidé le groupe, aujourd'hui ? Et qu'est-ce qui l'a "
          "freiné ? » Il commence par vous.", [
            R("« La page deux, et Léo. Et on est allés trop vite. »", 6, "ic2 cc2 er1 rd1"),
            R("« Le chatbot de Noah nous a freinés : il a donné la réponse, et personne n'a "
              "plus réfléchi. »", 6, "ic-2 rd-2 cc1"),
            R("« Tout s'est bien passé. »", 6, "cc-2 ic-1"),
            R("« Je ne sais pas trop. »", 6, "cc-1"),
            R("« Ce qui a aidé, c'est quand Yasmine nous a obligés à relire. Ce qui a freiné, "
              "je crois que c'est la peur de dire une bêtise devant les autres. »",
              6, "ic2 cc2 em1"),
        ]),
        I(6, "ibarra", "neutral",
          "Midi. Le Dr Ibarra range son gobelet. « Pour jeudi prochain : chacun écrit sa "
          "réflexion de portfolio sur la séance. Ce que vous avez appris, et comment. Pas ce "
          "que vous avez lu. » Il regarde Noah. « Avec vos mots. » Il sort.", [go(7)]),
        I(7, "noah", "anxious",
          "Dans le couloir, Noah vous rattrape. Il a les yeux cernés. « T'as fait ta "
          "réflexion de portfolio sur l'APP de la dernière fois ? Tu peux me l'envoyer ? Juste "
          "pour voir comment tu tournes ça. Je reformulerai, promis. Je n'ai pas le temps "
          "cette semaine, j'ai trois révisions en retard. »", [
            R("« Non, Noah. Mais je peux t'aider à écrire le tien. Ce soir ? »",
              8, "pb3 em1 co1 ic1"),
            R("« Ok, je te l'envoie. Mais tu changes tout, hein, je ne veux pas qu'on ait des "
              "problèmes. »", 9, "pb-3 ic-1", sets=["texte_partage"]),
            R("« Demande à ton chatbot. »", 10, "em-2 ic-1 pb1"),
            R("« T'as l'air crevé. Ça va, toi, en ce moment ? Tu dors combien d'heures par "
              "nuit ? »", 11, "em3 co1"),
            R("« Si je te l'envoie et que ça se voit, on aura des problèmes tous les deux : le "
              "logiciel anti-plagiat compare tous les portfolios de la volée. Non. »",
              8, "pb2 cc1 em-1"),
            R("Le lui envoyer sans rien dire : c'est un pote.", 9, "pb-3 cc-1",
              sets=["texte_partage"]),
        ]),
        I(8, "noah", "sad",
          "Noah hoche la tête trop vite. « Ouais. T'as raison. » Son téléphone vibre : un "
          "message de son père, qu'il ne lit pas. « Laisse tomber, je vais me "
          "débrouiller. »", [
            R("« Ce soir, 20 h, à la bibli ? »",
              16, "em2 ic2 pb1 co1"),
            R("« Ok. Bon courage. »", 16, "em-1 co-1"),
            R("« C'est ton père ? Tu veux en parler ? »", 11, "em3 co1"),
            R("« Tu sais qu'il y a un logiciel anti-plagiat, hein. »", 16, "pb1 em-2"),
            R("« Arrête de te plaindre, on est tous crevés. »", 16, "em-3 co-2"),
        ]),
        I(9, "noah", "happy",
          "« T'es le ou la meilleur·e. » Noah vous serre l'épaule. Le soir, il vous envoie un "
          "pouce levé. Puis : « j'ai fait passer ton texte dans le chatbot pour le "
          "reformuler, ça déchire ». Vous relisez son message deux fois.", [
            R("« Noah. Ne rends pas ça. Le logiciel trouvera mes phrases. Écris le tien, je "
              "t'aide. »", 15, "pb3 em1 cc2 co1"),
            R("« Cool. »", 15, "pb-2"),
            R("Ne pas répondre.", 15, "pb-1 ic-1"),
            R("« Ok, mais si ça se voit, je dirai que tu me l'as volé sur mon ordinateur, et "
              "je n'aurai aucun scrupule à le dire à la commission. »", 15, "pb-1 em-2 ic-2"),
            R("« Supprime-le de ton ordi, s'il te plaît. Je te le demande vraiment, comme un "
              "service. »", 15, "pb2 cc1"),
        ]),
        I(15, "noah", "happy",
          "« t'inquiète » « personne verra » « tout le monde fait ça, même les assistants "
          "pour leurs articles »", [
            R("« C'est mon texte. Ne le rends pas. »", 16, "pb3 cc2 er1"),
            R("« Bon. C'est ton problème. »", 16, "pb-2 em-1 co-1"),
            R("« Tu as peut-être raison. »", 16, "pb-2 cc-1"),
            R("Écrire au Dr Ibarra pour signaler que Noah s'apprête à rendre un texte qui n'est "
              "pas de lui, avec les captures d'écran de la conversation, pour vous couvrir en "
              "cas de problème.", 16, "pb1 ic-2 em-2"),
            R("« Appelle-moi. On en parle de vive voix. »", 16, "em2 co1 pb1"),
        ]),
        I(10, "noah", "hurt",
          "Noah vous regarde comme si vous l'aviez giflé. « Merci. Vraiment. » Il s'en va. "
          "De loin, vous le voyez s'asseoir sur un banc, la tête dans les mains.", [
            R("Le rejoindre sur le banc. « Pardon. C'était nul. Qu'est-ce qui se passe ? »",
              11, "em3 er1 rd1 co1"),
            R("Le laisser. Il a besoin d'apprendre à se débrouiller seul, comme tout le monde "
              "en deuxième année, sinon il ne tiendra jamais jusqu'en sixième.",
              16, "em-2 co-2"),
            R("Lui envoyer un message : « désolé·e, mal dormi ».", 16, "em1"),
            R("En parler à Maëlle, en riant à moitié : « Noah pète un câble, il veut copier "
              "mon portfolio. »", 16, "pb-2 rd-1"),
        ]),
        I(11, "noah", "vulnerable",
          "Noah s'assied sur la première marche de l'escalier. « Mon père m'appelle tous les "
          "soirs. Il veut mes notes, mon rang, ce que les profs disent de moi. Il connaît la "
          "moitié des profs. » Il rit. « Je dors quatre heures par nuit. J'ai l'impression "
          "d'avoir déjà raté ma vie, à vingt ans. »", [
            R("« Ça m'inquiète. Tu veux qu'on appelle la consultation pour étudiants ? »",
              16, "em2 ic2 pb2 cc1 co1"),
            R("« Tu n'as rien raté. Tu es en deuxième année, et tu es là, malgré tout ça. »",
              16, "em2 co2"),
            R("« Coupe ton téléphone le soir, et mets-le dans une autre pièce : c'est ce que "
              "recommandent tous les articles sur le sommeil. »", 16, "cc1 em-1"),
            R("« Mon pauvre. Bon, je dois y aller. »", 16, "em-2 co-2"),
            R("« Tu veux que je t'aide pour ton portfolio, ce soir ? Pas en te donnant le "
              "mien. »", 16, "em1 co1 pb2 ic1"),
        ]),
        I(16, "narr", "",
          "Le soir, devant votre propre réflexion de portfolio. Le Dr Ibarra a demandé « ce "
          "que vous avez appris, et comment ». Le curseur clignote.", [
            R("Écrire ce que Léo vous a appris.",
              12, "pb2 rd2 cc1 ic1"),
            R("Écrire sur l'anémie ferriprive : bilan martial, ferritine, causes digestives.",
              12, "cc1"),
            R("Demander au chatbot un premier jet « pour voir », puis le retoucher.",
              12, "pb-3 cc-1"),
            R("Écrire que le groupe a très bien fonctionné.", 12, "cc-2 pb-1"),
            R("Écrire que Noah a triché, pour que le tuteur le sache.", 12, "pb-2 ic-2 rd-2"),
        ]),
        I(12, "narr", "",
          "Vous relisez votre réflexion. Vous avez écrit : « J'ai appris qu'une anémie peut "
          "être une question d'argent. » Vous pensez à Mme R., qui mange ce qui reste, et à "
          "Noah, qui ne dort plus."),
    ],
)

# ---------------------------------------------------------------------------
# 2.3 Le Café de la Gare — branche « Alex a appelé le mauvais Pittet »
# ---------------------------------------------------------------------------
_INTRO_23 = (
    "Samedi matin. Vous passez au cabinet chercher un livre oublié. Sandra est là, malgré "
    "la fermeture ; elle a la tête de quelqu'un qui n'a pas dormi. « Assieds-toi. Hier "
    "soir, au Café de la Gare, Jean-Paul a raconté que le cabinet l'avait appelé pour les "
    "résultats de la Jeannine. Que ça devait être grave. Daniel était au bar. Il arrive. "
    "La Dre est en route. »"
)
_INTRO_23_INFO = (
    "Samedi matin. Vous passez au cabinet chercher un livre oublié. Sandra est là, malgré "
    "la fermeture ; elle a la tête de quelqu'un qui n'a pas dormi. « Assieds-toi. Hier "
    "soir, au Café de la Gare, Jean-Paul a raconté à tout le monde que la Jeannine avait "
    "les reins foutus et qu'elle allait finir à la dialyse. Daniel était au bar. Il "
    "arrive. La Dre est en route. »"
)

S2_3A = S(3, "2.3 Le Café de la Gare", _INTRO_23,
    focus=("pb", "rd", "er", "ic"),
    slot="2.3",
    cond=when(all=["erreur_homonyme"]),
    entries=[
        Entry(1, when(all=["info_lachee"]), _INTRO_23_INFO),
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
            R("« Non. Je ne peux pas le savoir. Je suis désolé·e. »", 4,
              "rd2 em2 er1 pb1 co1"),
            R("« Votre mère allait vous le dire, à Noël, elle me l'a dit : elle attendait le "
              "bon moment pour ne pas vous faire de peine. »", 5, "pb-3 cc-2"),
            R("Se taire, et soutenir son regard.", 4, "er2 rd1"),
            R("« Vous devriez en parler avec elle. »", 5, "pb-1 em-1"),
            R("« C'est surtout Jean-Paul qui n'aurait pas dû le raconter au café, devant tout "
              "le monde. »", 5, "pb-2 er-1 rd-1"),
        ]),
        I(3, "daniel", "angry",
          "Daniel tape du plat de la main sur le comptoir. Un pot de stylos se renverse. « Je "
          "vous ai posé une question. Qui ? » Sandra baisse les yeux. Elle ne dira rien. Elle "
          "attend que vous parliez.", [
            R("« C'est moi. Sandra n'y est pour rien. »", 2, "pb3 rd2 ic3 er1",
              sets=["aveu_homonyme"]),
            R("Laisser le silence durer jusqu'à l'arrivée de la Dre.", 6, "pb-2 ic-3",
              sets=["esquive_homonyme"]),
            R("« Le cabinet va vous répondre. La Dre arrive. »", 6, "pb-1 ic-1 cc-1",
              sets=["esquive_homonyme"]),
            R("« Quelqu'un du secrétariat s'est trompé de numéro : avec deux Pittet J. dans le "
              "logiciel, c'était facile de se tromper, vous savez. »", 6, "pb-3 ic-3 cc-1",
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
            R("« Je vous présente mes excuses, à vous et à votre mère. »", 7, "rd3 pb2 er1 co1"),
            R("« Je ne referai plus jamais cette erreur. »", 7, "pb1 er1"),
            R("Rester silencieux·se, et laisser la Dre parler.", 7, "ic1 er1"),
            R("« Votre mère va bien, ne vous inquiétez pas : ce ne sont que des résultats de "
              "contrôle, la Dre la suit de près, et elle a toujours été solide. »",
              7, "cc-3 pb-3"),
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
            R("« C'est moi. J'aurais dû le dire tout de suite. Pardon, Sandra. »",
              7, "pb3 rd2 er1 ic2", sets=["aveu_homonyme"], clears=["esquive_homonyme"]),
            R("« Je pensais que c'était au cabinet de répondre, pas à moi : je ne suis qu'un·e "
              "étudiant·e, je n'ai pas de responsabilité dans ce genre de situation. »",
              9, "pb-2 er-1"),
            R("« Je ne savais pas qu'il fallait vérifier la date de naissance avant de "
              "parler. »", 9, "pb-2 cc-1 ic-1"),
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
            R("« C'est à vous deux de décider si je reviens. »", 11, "rd2 pb2 em1"),
            R("« Merci. »", 11, "er1"),
            R("« Vous devriez parler à votre mère aujourd'hui. »", 11, "pb-1 em1"),
            R("« Je passerai la voir jeudi, comme d'habitude. »", 11, "pb-2 rd-1"),
            R("Hocher la tête, sans rien dire.", 11, "rd1 er1"),
        ]),
        I(9, "golay", "neutral",
          "La Dre Golay parle longtemps, calmement, à Daniel. Elle reconnaît l'erreur du "
          "cabinet, explique ce qui va changer, et refuse, doucement mais fermement, de parler "
          "de la santé de Jeannine. « Ça, c'est à elle de vous le dire. » Daniel se lève. À la "
          "porte, il se retourne vers vous. « Vous, je ne veux plus vous voir chez ma mère. » "
          "La porte vitrée tremble longtemps.", [
            R("Courir après lui : « Monsieur Pittet ! C'était moi. Pardon. »",
              12, "pb3 rd1 er1"),
            R("Le laisser partir.", 12, "er-1"),
            R("« C'est lui qui exagère, il cherchait juste quelqu'un sur qui crier. »",
              12, "rd-2 er-1 em-1"),
            R("Se tourner vers Sandra : « Pardon. Pour tout à l'heure. »", 12, "ic2 rd1"),
            R("« De toute façon, je n'ai rien à faire chez sa mère : je ne suis là que le "
              "jeudi, et ce n'est même pas ma patiente. »", 12, "em-2 rd-1 pb-1"),
        ]),
        I(11, "sandra", "sad",
          "La porte se referme. Sandra ramasse les stylos un par un. Puis, sans vous regarder : "
          "« Merci. J'aurais pu me taire et te laisser couler, tu sais. J'y ai pensé. » Elle "
          "remet le pot sur le comptoir. « Quatorze ans que je fais ce métier. C'est la "
          "première fois qu'un stagiaire dit « c'est moi » à ma place. »", [
            R("« Mon erreur. On change le post-it ensemble ? »", 10, "ic3 pb1 cc1 er1 co1"),
            R("« Normal. »", 10, "er1"),
            R("« Tu aurais pu me prévenir qu'il y avait deux Pittet. »", 10, "ic-2 pb-1"),
            R("« Je l'ai dit parce que la Dre allait l'apprendre de toute façon, et que ça "
              "aurait été pire pour moi si elle l'avait découvert par Daniel ou par "
              "Jean-Paul. »", 10, "pb-1 er-1 rd-1"),
            R("« Ça va, toi ? Il t'a fait peur. »", 10, "em2 co2 ic1"),
        ]),
        I(12, "sandra", "cold-anger",
          "Sandra a ramassé les stylos. Elle parle sans vous regarder. « Tu m'as laissée seule "
          "devant lui. Dix secondes de silence, c'est long, quand un homme comme Daniel tape "
          "sur ton comptoir. » Elle remet le pot en place, très droit. « Je n'oublierai "
          "pas. »", [
            R("« Tu as raison. J'ai eu peur, et je t'ai laissée seule. Pardon. »",
              10, "ic3 pb2 er2 rd1"),
            R("« Je ne savais pas quoi dire. »", 10, "er-1"),
            R("« Ce n'était pas à moi de répondre, c'était au cabinet : la Dre l'a dit "
              "elle-même, c'est elle qui est responsable de ce qui se passe ici. »",
              10, "ic-2 pb-2 er-1"),
            R("« Il ne t'aurait rien fait. »", 10, "em-2 co-1"),
            R("Partir sans répondre, le livre oublié sous le bras, et ne pas revenir avant "
              "jeudi prochain.", 10, "ic-2 er-1 co-1"),
        ]),
        I(10, "golay", "neutral",
          "La Dre Golay remplit avec vous la déclaration d'incident du cabinet. Ligne par "
          "ligne : ce qui s'est passé, ce qui l'a rendu possible, ce qui va changer. Elle ne "
          "hausse jamais la voix. Elle vous tend le stylo. « Facteurs contributifs. Qu'est-ce "
          "qui a rendu l'erreur possible ? »", [
            R("« Deux « Pittet J. », un post-it sans date de naissance, une file de six "
              "personnes. Et moi, qui n'ai pas vérifié. »", 13, "ic2 cc3 pb2 er1"),
            R("« Moi. C'est tout. »", 13, "er-1 cc-2 pb1"),
            R("« Sandra, qui m'a donné un post-it incomplet. »", 13, "ic-3 rd-1"),
            R("« Le logiciel, qui ne signale pas les homonymes. »", 13, "ic1 cc1 pb-1"),
            R("« La fatigue. C'était la journée des vaccins. »", 13, "er-1 pb-2 cc-1"),
        ]),
        I(13, "golay", "neutral",
          "« On ne fait pas ça pour trouver un coupable. On le fait pour que la prochaine "
          "Sandra et le prochain Alex ne se retrouvent pas là. » Elle signe, et range le "
          "formulaire. « Jeannine, je l'appelle tout à l'heure. Elle voudra peut-être vous "
          "voir. Ou pas. »"),
    ],
)

# ---------------------------------------------------------------------------
# 2.3 La créatinine — branche « personne n'a parlé au village »
# ---------------------------------------------------------------------------
_INTRO_23B = (
    "Lundi, 14 h. Jeannine est assise dans le cabinet de la Dre Golay, son sac à main sur "
    "les genoux, son foulard rouge noué serré. Les résultats sont à l'écran. La Dre vous a "
    "demandé d'être là, et Jeannine aussi."
)
_INTRO_23B_RATTRAPE = (
    "Lundi, 14 h. Samedi, Jean-Paul est passé au cabinet demander « ce qu'avait la "
    "Jeannine » ; Sandra l'a renvoyé avec un sourire et pas un mot. Jeannine est assise dans "
    "le cabinet de la Dre Golay, son sac à main sur les genoux. Les résultats sont à "
    "l'écran. La Dre vous a demandé d'être là, et Jeannine aussi."
)
_INTRO_23B_REVELE = (
    "Lundi, 14 h. Depuis septembre, Daniel ne rentre plus dans la cuisine de sa mère : il "
    "nourrit les bêtes, et il repart. Jeannine ne vous a plus adressé la parole. Elle est "
    "assise dans le cabinet de la Dre Golay, son sac à main sur les genoux. La Dre vous a "
    "demandé d'être là. Jeannine n'a pas dit non."
)

S2_3B = S(4, "2.3 La créatinine", _INTRO_23B,
    focus=("rd", "cc", "co", "er"),
    slot="2.3",
    cond=when(none=["erreur_homonyme"]),
    entries=[
        Entry(20, when(all=["revele_a_daniel"]), _INTRO_23B_REVELE),
        Entry(1, when(all=["appel_rattrape"]), _INTRO_23B_RATTRAPE),
    ],
    nodes=[
        I(1, "golay", "neutral",
          "« Jeannine, vos reins travaillent moins bien. Beaucoup moins bien qu'au "
          "printemps. » La Dre tourne l'écran vers elle. « Si ça continue à ce rythme, dans "
          "quelques mois, il faudra parler de dialyse. » Jeannine ne regarde pas l'écran. "
          "Elle vous regarde, vous.", [
            R("Soutenir son regard, en silence.",
              2, "rd2 pb2 er1"),
            R("« La dialyse, ça se passe très bien, maintenant, Madame Pittet : trois séances "
              "par semaine, et on peut lire ou dormir pendant. »", 3, "pb-3 cc-2"),
            R("Regarder ailleurs.", 2, "em-1 er-1 co-1"),
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
            R("« Non. Vous savez ce que vous voulez. »", 4, "rd3 pb2 em1"),
            R("« Un peu, oui. La dialyse pourrait vous donner des années. »", 3, "rd-3 pb-3"),
            R("« Ce n'est pas à moi de juger. »", 4, "pb2 em-1"),
            R("« Vous avez peur de la dialyse, ou d'être un poids pour Daniel ? »",
              5, "em3 cc1 co1"),
            R("« Moi, à votre place, je ferais pareil : à huitante et un ans, trois "
              "après-midi par semaine branchée à une machine, ce n'est pas une vie, c'est une "
              "survie. »", 4, "pb-2 em1 rd-1"),
            R("Regarder la Dre Golay, pour qu'elle réponde à votre place.", 4,
              "pb1 ic1 em-1"),
        ]),
        I(3, "golay", "cold-anger",
          "La Dre Golay lève la main, sans vous regarder. « Alex. » Un seul mot. Puis, à "
          "Jeannine : « On n'est pas là pour vous convaincre, Jeannine. On est là pour que "
          "vous décidiez en sachant tout. »", [
            R("« Pardon, Madame Pittet. Ce n'était pas à moi de dire ça. C'est votre décision, "
              "et vous la prendrez en sachant tout. »", 4, "pb2 rd2 er1"),
            R("Se taire, rouge.", 4, "er1"),
            R("« Je voulais juste l'aider. »", 4, "pb-1 er-1"),
            R("« Mais c'est vrai, non, que la dialyse pourrait lui donner des années ? Je "
              "n'ai rien dit de faux. »", 4, "pb-3 er-2"),
        ]),
        I(4, "golay", "neutral",
          "La Dre Golay explique : ce qui se passera si les reins continuent à baisser — la "
          "fatigue, les jambes, le goût de métal dans la bouche ; ce qu'on peut faire sans "
          "dialyse pour que ce soit le plus confortable possible ; les directives "
          "anticipées, pour que sa volonté soit écrite. « Et Daniel ? » Jeannine soupire. "
          "« À Noël. Je lui dirai à Noël. Tout. » Elle se tourne vers vous. « Le 26, vous "
          "viendrez ? J'aimerais qu'il y ait quelqu'un de la médecine. Pas Isabelle : elle me "
          "connaît trop. »", [
            R("« Si la Dre est d'accord, je viendrai. Pour écouter. »", 6, "pb3 rd2 ic1",
              sets=["noel_annonce"]),
            R("« Promis, je serai là, quoi qu'il arrive, même si la Dre préfère que je ne "
              "vienne pas : c'est vous qui me le demandez. »", 6, "pb-3 em1",
              sets=["noel_annonce"]),
            R("« Ce n'est pas le rôle d'un·e étudiant·e. »", 6, "pb1 em-2 co-1"),
            R("« Pourquoi attendre Noël ? Il faudrait le lui dire maintenant. »",
              6, "rd-2 pb-1"),
            R("Regarder la Dre Golay : « C'est possible ? »", 7, "ic2 pb2"),
        ]),
        I(5, "jeannine", "sad",
          "Jeannine met du temps à répondre. « Des deux. » Elle lisse son foulard. « Daniel a "
          "déjà porté son père. Je ne veux pas qu'il me porte, moi, trois fois par semaine, "
          "jusqu'à ce que je ne sois plus qu'un tuyau. » La Dre Golay ne dit rien. Elle vous "
          "laisse la question.", [
            R("« Vous voulez le protéger. Et lui, vous savez ce qu'il voudrait ? »",
              4, "em3 cc1 rd1 co1"),
            R("« Est-ce que Daniel sait, pour vos reins ? Et pour ce que vous voulez ? Parce "
              "que s'il ne sait rien, il ne peut pas vous dire s'il est d'accord ou non. »",
              4, "cc2 em1 ic1"),
            R("« Je comprends. »", 4, "em1"),
            R("« Mais vous n'êtes pas un poids ! »", 4, "cc-2 em1"),
            R("« Si vous refusez la dialyse, il faudra au moins le dire à Daniel. Sinon, "
              "c'est lâche. »", 4, "rd-3 em-2 co-1"),
        ]),
        I(6, "jeannine", "happy",
          "Jeannine se lève, remet son foulard. « Bien. » Sur le pas de la porte, elle se "
          "retourne. « Vous savez ce qu'on dit, chez les sages-femmes ? On ne pousse pas "
          "avant que le col soit ouvert. Daniel, c'est pareil. » Elle sort. La Dre Golay "
          "range ses lunettes. « Elle a raison. Elle a presque toujours raison. C'est "
          "épuisant. »", [go(8)]),
        I(7, "golay", "neutral",
          "La Dre Golay réfléchit. « Si vous le souhaitez toutes les deux. Vous serez témoin, "
          "Alex, pas médiateur·rice : si Daniel pose des questions médicales, vous lui dites "
          "de m'appeler. Et vous m'appelez après. »", [
            R("« D'accord. Témoin, pas médiateur·rice. »", 6, "pb3 ic2 cc1", sets=["noel_annonce"]),
            R("« Et si ça se passe mal ? »", 6, "er1 cc1", sets=["noel_annonce"]),
            R("« Finalement, je préfère ne pas être mêlé·e à ça. »", 6, "em-2 pb1 co-1"),
            R("« Je pourrais aussi lui expliquer la dialyse, à Daniel, et pourquoi sa mère "
              "n'en veut pas : il l'entendrait peut-être mieux de quelqu'un d'extérieur. »",
              6, "pb-3 ic-1", sets=["noel_annonce"]),
        ]),
        I(8, "golay", "neutral",
          "Quand la porte s'est refermée, la Dre Golay ne range pas tout de suite le dossier. "
          "« Alors ? Qu'est-ce que ça vous a fait, quand elle a dit non ? »", [
            R("« J'ai eu envie de la convaincre. Ça m'a surpris·e. »", 9, "er3 cc1 pb1"),
            R("« Rien de spécial. C'est sa décision. »", 9, "er-1 em-1"),
            R("« De la colère, un peu. Elle pourrait vivre des années de plus avec la dialyse, "
              "et elle refuse pour ne pas déranger son fils : je trouve ça absurde, et injuste "
              "pour lui. »", 9, "er-1 rd-2 pb-1"),
            R("« J'ai pensé à ma grand-mère. »", 9, "er2"),
            R("« De la tristesse. Et du respect. Je ne sais pas encore si on a le droit de "
              "ressentir les deux en même temps, devant une patiente. »", 9, "er2 rd1 em1"),
        ]),
        I(9, "golay", "neutral",
          "La Dre Golay hoche la tête. « Vous auriez voulu qu'elle accepte ? »", [
            R("« Oui. Ça ne compte pas. »",
              10, "pb3 rd2 er1"),
            R("« Évidemment. Tout le monde voudrait ça. »", 10, "pb-1 rd-1"),
            R("« Non. Elle a raison, et je l'aurais dit à sa place. »", 10, "pb-1 cc-1"),
            R("« Je ne sais pas. »", 10, "er1"),
            R("« Oui. Je pourrais lui en reparler jeudi, quand vous ne serez pas là. »",
              10, "pb-3 ic-2"),
        ]),
        I(10, "sandra", "neutral",
          "Au comptoir, Sandra range les dossiers. « Alors, la Jeannine ? Je dois lui réserver "
          "des créneaux, ou pas ? Et le transport pour Yverdon, je l'organise ? »", [
            R("« Pas de transport : elle ne fera pas de dialyse. Pour les rendez-vous, la Dre "
              "te dira. »", 11, "ic3 cc2 pb1"),
            R("« Je ne peux rien te dire, c'est le secret médical. »", 11, "ic-2 pb-1 cc-1"),
            R("« Elle refuse la dialyse, elle veut mourir chez elle, elle a parlé de Noël et "
              "de Daniel, et la Dre a sorti les directives anticipées : je crois que c'est la "
              "fin, Sandra. »", 11, "pb-2 cc-1 rd-1"),
            R("« Demande à la Dre. »", 11, "ic-1"),
            R("« Je ne sais pas trop. Je crois qu'elle a dit non à la dialyse, mais je n'ai "
              "pas tout compris. »", 11, "cc-1 ic1"),
        ]),
        I(11, "narr", "",
          "Le soir, en rentrant, vous cherchez « directives anticipées » sur le site de la "
          "faculté. Vous tombez sur un formulaire de quatre pages. Vous pensez à une femme de "
          "huitante et un ans qui a mis au monde six cents enfants, et qui vient de décider "
          "de sa propre fin, en dix minutes, entre deux patients."),
        I(20, "jeannine", "cold-anger",
          "Jeannine vous voit, et pince les lèvres. « Ah. Vous. »", [
            R("« Madame Pittet, je vous ai trahie en septembre. Si vous préférez que je sorte, "
              "je sors. »", 21, "pb3 rd3 er1 co1"),
            R("« Bonjour, Madame Pittet. » Comme si de rien n'était.",
              21, "rd-2 er-1"),
            R("« Daniel aurait fini par le savoir, de toute façon. »", 21, "pb-3 rd-3 em-1"),
            R("Proposer de sortir, sans un mot d'explication.", 21, "pb1 er-1"),
            R("« Je suis désolé·e. Je pensais bien faire en le disant à votre fils. »",
              21, "rd1 er1 pb-1"),
        ]),
        I(21, "jeannine", "resigned",
          "Jeannine vous regarde longtemps. « Restez. Ce que j'ai à dire aujourd'hui, autant "
          "que vous l'entendiez. » Elle se tourne vers la Dre Golay. « Alors, ces "
          "reins ? »", [go(1)]),
    ],
)

# ---------------------------------------------------------------------------
# 2.4 Le dimanche aux Combettes
# ---------------------------------------------------------------------------
_INTRO_24 = (
    "Dimanche de novembre. Thierry vous a proposé sa tournée du dimanche, avec l'accord de "
    "la Dre Golay. Aux Combettes, une Twingo cabossée est garée dans la cour : une jeune "
    "fille aux cheveux violets en décharge des seaux de chrysanthèmes. Océane, la "
    "petite-fille de Jeannine, apprentie fleuriste. Pendant que Thierry prépare le "
    "pilulier dans la cuisine, elle vous fait signe de la suivre dans la grange."
)

S2_4 = S(5, "2.4 Le dimanche aux Combettes", _INTRO_24,
    focus=("em", "rd", "pb", "co"),
    entries=[
        Entry(20, when(all=["revele_a_daniel"]), _INTRO_24),
        Entry(10, when(all=["erreur_homonyme"]), _INTRO_24),
    ],
    nodes=[
        I(1, "oceane", "suspicious",
          "Entre deux bottes de paille, Océane croise les bras. « C'est toi, la fac ? Mamie "
          "parle de toi tout le temps. » Elle vous dévisage. « Elle te parle à toi, et pas à "
          "nous. Elle a quoi ? »", [
            R("« Je ne peux pas te parler de sa santé. Pas parce que c'est toi : parce que "
              "c'est elle qui décide à qui elle en parle. »", 3, "pb3 rd2 cc2",
              sets=["oceane_confiance"]),
            R("« Rien de grave, ne t'inquiète pas. »", 3, "cc-2 pb-2"),
            R("« Ses reins fatiguent un peu. »", 3, "pb-3 rd-1"),
            R("« Tu as l'air inquiète. Qu'est-ce que tu as remarqué, toi ? »", 2,
              "em3 cc1 co1", sets=["oceane_confiance"]),
            R("« Demande à ton père. »", 3, "pb-1 em-2 co-1"),
        ]),
        I(2, "oceane", "sad",
          "Océane donne un coup de pied dans la paille. « Elle dort assise dans son fauteuil. "
          "Elle ne monte plus voir les veaux. Et elle a rangé tous ses papiers dans une boîte "
          "à biscuits, avec des étiquettes. Mamie ne range jamais rien. » Sa voix se casse. "
          "« Les vieux qui rangent leurs papiers, c'est qu'ils vont mourir. Tout le monde "
          "sait ça. »", [
            R("« Tu as peur. C'est à elle qu'il faut le dire. Tu veux que je lui dise que tu "
              "aimerais lui parler ? »", 3, "em3 co2 pb1 ic1"),
            R("« Mais non, ça ne veut pas dire ça. Les personnes âgées rangent leurs papiers "
              "pour plein de raisons : les impôts, la banque, un déménagement… »",
              3, "cc-2 em-1"),
            R("« Elle a huitante et un ans, Océane. Un jour ou l'autre… »",
              3, "em-2 rd-1 pb-1 co-1"),
            R("« Tu en as parlé à ton père ? »", 3, "ic1 em1"),
            R("S'asseoir sur une botte de paille, à côté d'elle, et attendre.", 3, "em2 co2"),
        ]),
        I(3, "jeannine", "happy",
          "« Océane ! Lâche la fac, elle est là pour le travail. » Jeannine est sur le seuil "
          "de la grange, appuyée sur sa canne, Thierry derrière elle. Elle a tout entendu, ou "
          "presque. « Viens m'aider à mettre la table, ma grande. Et toi, la fac, tu restes "
          "manger la tresse ? » Océane vous regarde. Thierry aussi.", [
            R("« Merci, mais le repas, c'est en famille. Je repars avec Thierry. »",
              8, "pb3 rd1"),
            R("« Avec plaisir ! »", 5, "pb-2 em1"),
            R("« Océane a des questions, Madame Pittet. Je crois qu'elle aimerait vous "
              "parler. »", 6, "ic2 em2 pb1"),
            R("« Non merci, je ne mange pas chez les patients. »",
              8, "rd-2 em-1 pb1"),
            R("« Océane me demandait ce que vous aviez. Je n'ai rien dit, bien sûr. »",
              6, "pb-2 rd-2"),
        ]),
        I(4, "thierry", "neutral",
          "Dans la Panda, Thierry vous regarde de côté. « Pour le repas, t'as bien fait. Ma "
          "première année, j'ai dit oui à tout le monde : tresse, raclette, baptême. Au bout "
          "de six mois, je ne savais plus si j'étais leur infirmier ou leur cousin. » Il "
          "démarre. « Et la petite, elle t'a demandé quoi ? »", [
            R("« Ce qu'avait sa grand-mère. Je n'ai rien dit. Tu pourrais l'aider, toi ? "
              "»", 7, "ic3 pb2 cc1"),
            R("« Rien d'important. »", 7, "ic-1 cc-1"),
            R("« Ce qu'avait Jeannine. Je ne savais pas ce que j'avais le droit de dire à une "
              "mineure. »", 7, "pb1 cc1 ic1"),
            R("« Elle est un peu perdue, je crois. »", 7, "em2 pb-1"),
            R("« Rien. Et franchement, la famille, ce n'est pas mon problème : je suis là pour "
              "la patiente, pas pour gérer les angoisses de tout le village. »",
              7, "em-2 ic-2 rd-1 co-1"),
        ]),
        I(5, "jeannine", "happy",
          "La table est mise pour quatre : elle avait prévu. Thierry, lui, est reparti. "
          "Jeannine coupe la tresse. Au deuxième café, elle vous demande votre avis sur ses "
          "jambes ; Océane, sur un bouton qu'elle a dans le dos. Daniel, qui passait chercher "
          "une clé, vous regarde depuis la porte sans entrer.", [
            R("« Pour vos jambes et pour le bouton, il faut demander à la Dre Golay. "
              "Aujourd'hui, je suis juste invité·e. »", 8, "pb3 cc1 rd1"),
            R("Regarder les jambes, puis le bouton.", 8, "pb-3 rd-1"),
            R("« Ça a l'air de rien, ne vous inquiétez pas. »", 8, "pb-2 cc-2"),
            R("« Je ne peux pas, désolé·e. » Et changer de sujet.", 8, "pb2 em-1"),
            R("Se lever pour saluer Daniel, et lui expliquer pourquoi vous êtes là, à cette "
              "table, un dimanche.", 8, "rd1 pb1 cc1"),
        ]),
        I(6, "jeannine", "neutral",
          "Jeannine regarde sa petite-fille. Puis elle tapote la chaise à côté d'elle. « Viens "
          "là. » Océane s'assied. « Mes reins ne marchent plus très bien, ma grande. Je ne "
          "veux pas de machine. Et je ne veux pas qu'on en parle à ton père : c'est à moi de "
          "le faire. Tu peux garder ça ? » Océane hoche la tête, les yeux pleins de larmes. "
          "Jeannine vous regarde par-dessus son épaule. « Vous voyez. On n'a pas besoin de "
          "vous pour tout. »", [
            R("Sortir de la grange pour les laisser seules.", 8, "rd3 pb2"),
            R("« Océane, tu peux venir me parler quand tu veux, je te donnerai mon numéro "
              "avant de partir. »", 8, "pb-3 ic-1"),
            R("Rester, et prendre la main d'Océane.", 8, "pb-1 em1 co2"),
            R("« Il faudra bien le dire à Daniel, aussi. »", 8, "rd-2 pb-1"),
            R("Hocher la tête vers Jeannine, et rejoindre Thierry dans la cour.",
              8, "rd2 ic1 pb1"),
        ]),
        I(8, "oceane", "vulnerable",
          "Dans la cour, au moment où vous partez, Océane vous rattrape près de la Panda. Elle "
          "a son téléphone à la main. « T'as Insta ? Si mamie va mal, je pourrais t'écrire. "
          "Toi, tu me répondrais. Eux, ils ne me disent jamais rien. »", [
            R("« Si mamie va mal : le 144, ou Thierry. Et tu peux parler à la Dre, elle "
              "t'écoutera. »", 4, "pb3 cc2 ic1 em1 co1"),
            R("Lui donner votre compte Instagram : c'est juste un contact, et elle a besoin de "
              "quelqu'un à qui parler.", 4, "pb-3 em1"),
            R("« Je ne donne pas mon Insta aux familles. »", 4, "pb1 em-2 co-1"),
            R("« Ils ne te disent rien parce qu'ils ont peur, eux aussi. »", 4, "em2 co1"),
            R("« Je ne suis là que le jeudi, et je ne suis pas sûr·e de pouvoir répondre si tu "
              "m'écris : je ne sais pas ce que j'aurais le droit de te dire. »",
              4, "cc-1 pb1 em-1"),
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
            R("« Oui, c'est moi. C'était une faute grave, et je suis désolé·e — pour ton père, "
              "et pour ta grand-mère. »", 11, "pb3 rd2 er1 co1"),
            R("« C'était une erreur du cabinet. »", 11, "pb-2 cc-1"),
            R("« Jean-Paul n'aurait jamais dû le raconter. »", 11, "pb-2 er-1"),
            R("« Comment va ton père ? »", 11, "em2 co1"),
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
              12, "em3 co2", sets=["oceane_confiance"]),
        ]),
        I(12, "jeannine", "neutral",
          "« Océane ! Lâche la fac, elle est là pour le travail. » Jeannine est sur le seuil "
          "de la grange, appuyée sur sa canne, Thierry derrière elle. « Viens m'aider à mettre "
          "la table, ma grande. Et toi, la fac, tu restes manger la tresse ? »", [
            R("« Le repas, c'est en famille. Merci. »",
              8, "pb3 rd1"),
            R("« Avec plaisir ! »", 5, "pb-2 em1"),
            R("« Je reste, si Océane est d'accord. »", 5, "pb-1 rd1"),
            R("« Non merci, je ne mange pas chez les patients. »", 8, "rd-2 em-1 pb1"),
            R("« Merci. Océane, tes questions, c'est à ta grand-mère qu'il faut les poser, "
              "pas à moi : elle est là, elle peut te répondre maintenant. »",
              8, "pb2 em-1 rd-1"),
        ]),
        I(20, "oceane", "cold-anger",
          "Océane vous dévisage. « C'est toi, la fac ? C'est toi qui as dit à papa, pour le "
          "corps de mamie ? » Elle pose ses seaux. « Depuis, il ne rentre plus dans la "
          "cuisine. Il nourrit les bêtes et il repart. Mamie mange seule. »", [
            R("« Oui. C'est moi. Je n'avais pas le droit, et je le regrette tous les "
              "jours. »", 21, "pb3 rd2 er1 co1"),
            R("« Il aurait fini par l'apprendre, de toute façon. »",
              21, "rd-3 pb-3 em-1"),
            R("« Ton père a besoin de temps. »", 21, "pb-1 em1 co1"),
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
              "train de l'apprendre. Pas toujours bien. »", 12, "cc3 rd2 em1 pb1 co1",
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
# 2.5 Léo — histoire annexe (si Alex a inclus Léo au tutorat)
# ---------------------------------------------------------------------------
S2_5 = S(6, "2.5 Léo",
    "Samedi, 15 h. Bibliothèque universitaire, troisième étage, la table du fond. Léo vous a "
    "écrit hier : « Tu veux réviser le sang ? J'ai fait des fiches. » Il est là depuis 9 h. "
    "Ses fiches sont en deux langues.",
    focus=("em", "ic", "co"),
    slot="2.5",
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
            R("« Tes fiches sont meilleures que les miennes. Je te traduis les pièges, tu "
              "m'expliques la coagulation. Deal ? »", 7, "ic3 rd2 em2"),
            R("« Faut que tu bosses ton français, Léo. »", 3, "rd-2 em-2 co-1"),
            R("« Moi non plus, je ne comprends pas ces phrases. Personne ne les comprend. »",
              7, "em2 er1"),
            R("« Il existe un soutien pour les allophones, tu sais. »", 7, "ic1 cc1 em-1"),
            R("Prendre ses fiches en photo, pour vous.", 3, "rd-2 ic-1 pb-1"),
        ]),
        I(7, "leo", "neutral",
          "Pendant une heure, ça marche. Léo vous explique pourquoi le facteur VIII et le "
          "facteur IX ne se trompent jamais de rôle. Puis il pointe une question : « Un garçon "
          "de huit ans saigne longtemps après une extraction dentaire. Laquelle n'est pas "
          "fausse ? » Il vous regarde, plein d'espoir. Vous n'en avez aucune idée.", [
            R("« Je ne sais pas. On cherche ensemble ? »", 2, "cc2 er2 ic2"),
            R("Répondre au hasard, avec assurance, pour ne pas le décevoir.", 2,
              "cc-2 er-1 ic-1"),
            R("« Hémophilie, sûrement. » Et passer vite à la suivante.", 2, "cc-1 ic-1"),
            R("« C'est toi l'expert de la coagulation, je te laisse répondre et tu "
              "m'expliques : moi, je ne fais que traduire les pièges du français. »",
              2, "ic2 em1 er-1"),
            R("Chercher la réponse dans le cours, sur votre téléphone, sans rien dire.", 2,
              "er1 ic-1"),
        ]),
        I(2, "leo", "happy",
          "À 17 h, il range ses fiches, puis s'arrête. « Je peux te dire un truc ? Je n'ai "
          "parlé à personne, en dehors des cours, depuis septembre. Personne. Le week-end, je "
          "rentre à Bienne, et je ne dis pas à ma mère que je suis seul ici. »", [
            R("« Tu viens vendredi, à la soirée de la table 14 ? »", 4, "em3 ic2 co2", sets=["leo_allie"]),
            R("« Ça va s'arranger, tu verras. »", 8, "em-1 cc-1"),
            R("« Tu devrais en parler au service de consultation psychologique. »",
              8, "ic1 em-1"),
            R("Rester silencieux·se, et attendre qu'il continue.", 5, "em2 co1"),
            R("« Ah ouais, c'est dur. Bon, j'y vais, je retrouve des potes. »",
              3, "em-3 co-2"),
        ]),
        I(3, "leo", "ashamed",
          "Léo ramasse ses fiches, lentement. « Oui. Bien sûr. » Il ne dit plus rien pendant "
          "une heure. À 16 h, il s'en va en murmurant un « merci » qui n'en est pas un.", [
            R("Le rattraper dans l'escalier : « Léo, attends. C'était nul, ce que j'ai dit. "
              "Tes fiches sont géniales. On recommence ? »", 7, "rd2 em2 er1 ic1 co1"),
            R("Le laisser partir.", 6, "em-1 ic-1 co-1"),
            R("Lui envoyer un message : « merci pour les fiches ! »", 6, "ic1 rd-1"),
            R("Raconter à Maëlle que Léo est « un peu bizarre ».", 6, "rd-3 pb-2"),
        ]),
        I(5, "leo", "vulnerable",
          "« À Zurich, j'avais un groupe. On faisait du POL, les tutorats par problèmes, tous "
          "les jeudis. On finissait toujours à la même pizzeria. » Il fait tourner son "
          "crayon. « Ici, au tutorat, j'ai les réponses. Je ne les dis pas, parce que j'ai peur "
          "de mal dire. Alors on croit que je ne sais rien. »", [
            R("« Jeudi, tu as vu ce que personne n'avait vu, page deux. Recommence. Et si tu "
              "bloques sur un mot, dis-le en allemand : je t'aiderai. »", 9,
              "ic3 em2 rd2 co1", sets=["leo_allie"]),
            R("« Faut juste oser. »", 8, "cc1 em-1"),
            R("« Tu devrais peut-être retourner à Zurich. »", 8, "em-2 ic-2 rd-1"),
            R("« On pourrait se faire une pizzeria du jeudi, nous aussi. »", 9, "ic2 em2 co1",
              sets=["leo_allie"]),
        ]),
        I(4, "narr", "",
          "En sortant de la bibliothèque, il fait déjà nuit. Léo vous serre la main, trop "
          "formellement, puis rit de lui-même. Dans le bus, vous recevez une photo : la fiche "
          "de la cascade de la coagulation, avec, au crayon, dans un coin : « für Alex — pour "
          "Alex »."),
        I(9, "leo", "happy",
          "Sur le trottoir, Léo hésite. « Et… pour mon portfolio de jeudi. Tu pourrais "
          "corriger mon français ? Juste les fautes. » Il vous tend une feuille couverte de "
          "ratures.", [
            R("« Les fautes, oui. Les idées, elles sont à toi : je n'y touche pas. »",
              4, "pb3 ic2 em1"),
            R("« Je te le réécris, ce sera plus simple, et tu seras sûr que c'est bien : tu "
              "n'auras qu'à le recopier à la main avant de le rendre. »", 4, "pb-3 ic-1 em1"),
            R("« Le service des langues fait ça mieux que moi. »", 4, "ic1 em-1 co-1"),
            R("« Ton français est très bien, ne change rien. »", 4, "cc-1 em1"),
            R("Lire la feuille tout de suite, sous le réverbère, et la lui rendre avec un "
              "sourire.", 4, "em2 ic1 rd1"),
        ]),
        I(8, "narr", "",
          "Vous rentrez seul·e. Le samedi suivant, Léo révise à la même table du fond, seul "
          "lui aussi. Vous le voyez par la vitre en passant, penché sur ses fiches en deux "
          "langues."),
        I(6, "narr", "",
          "Vous sortez ensemble de la bibliothèque. Léo vous serre la main, trop "
          "formellement. « Merci pour les QCM. » Il part vers la gare. Le samedi suivant, il "
          "révise seul, à la même table du fond."),
    ],
)

# ---------------------------------------------------------------------------
# 2.6 BLS
# ---------------------------------------------------------------------------
S2_6 = S(7, "2.6 BLS",
    "Mi-décembre. Centre de simulation, salle 3. Des mannequins alignés sur des tapis "
    "bleus, un défibrillateur d'entraînement, une odeur de désinfectant et de plastique "
    "neuf. La Dre Chevalley, responsable du centre, fait asseoir la table 14 en cercle. "
    "Aujourd'hui : réanimation de base.",
    focus=("ic", "cc", "er", "co"),
    nodes=[
        I(1, "chevalley", "neutral",
          "« Dans un arrêt cardiaque, ce qui tue, ce n'est presque jamais l'ignorance. C'est "
          "le silence, le flou et la peur. Qui fait quoi, qui appelle, qui compte. » Elle "
          "désigne le mannequin. « Groupes de quatre. Un leader. Les autres font ce qu'il "
          "dit, et le répètent à voix haute. On appelle ça la communication en boucle "
          "fermée. Qui commence ? » Yasmine soupire : elle a fait ça mille fois.", [
            R("« Je mène. Yasmine, tu nous corriges ? »",
              2, "ic3 cc1 er1"),
            R("« Yasmine a l'expérience : qu'elle le fasse. »", 3, "ic-1 er-1"),
            R("« Je fais les compressions. Je préfère ne pas parler. »", 2, "cc-1 ic1"),
            R("« Pourquoi c'est si important de répéter à voix haute, si tout le monde "
              "entend déjà ce que dit le leader ? »", 4, "cc2 ic1"),
            R("Rire avec Noah, qui fait mine d'embrasser le mannequin.", 3, "rd-1 ic-2 er-1"),
        ]),
        I(2, "narr", "",
          "« Scénario : un homme de soixante ans s'effondre dans un hall de gare. » La Dre "
          "Chevalley lance le chronomètre. Le mannequin est par terre. Noah se fige, Maëlle "
          "cherche le défibrillateur des yeux, Léo vérifie la sécurité des lieux comme dans le "
          "protocole. Yasmine attend, bras croisés, de voir ce que vous allez faire.", [
            R("« Monsieur, vous m'entendez ? » Secouer ses épaules, regarder s'il respire dix "
              "secondes, puis : « Noah, tu appelles le 144 et tu mets le haut-parleur. "
              "Maëlle, le défibrillateur. Je commence les compressions. »",
              5, "ic3 cc3 er2 rd1"),
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
            R("« On recommence. Je mène. »", 2, "ic2 er2 pb1"),
            R("« Elle le fait mieux que nous : autant qu'elle le fasse. »", 7, "ic-2 er-1"),
            R("« C'est injuste, elle a six ans d'avance sur nous tous, c'est normal qu'elle "
              "aille plus vite : ce n'est pas un exercice équitable. »", 7, "ic-2 er-2"),
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
          "« Propre. » Yasmine, pour la première fois, sourit.", [go(12)]),
        I(12, "chevalley", "neutral",
          "« On tourne. Noah, vous menez. » Noah s'agenouille. Il bafouille : « Euh… "
          "Monsieur ? » Il regarde le mannequin, puis vous. Personne n'a encore appelé le 144. "
          "Le chronomètre tourne : dix secondes, quinze.", [
            R("« Noah, j'appelle le 144 ? »", 7, "ic3 cc2 er1"),
            R("Prendre sa place, pour gagner du temps.", 7, "ic-2 rd-1 co-1"),
            R("Appeler le 144 sans rien dire, pendant qu'il cherche ses mots.", 7,
              "cc-1 ic-1"),
            R("« Respire. Tu sais faire : conscience, respiration, 144. On est là. »",
              7, "em2 co1 cc1 ic1"),
            R("Rire : « Il bugge ! »", 7, "rd-2 em-2 er-1 co-1"),
        ]),
        I(6, "chevalley", "neutral",
          "La Dre Chevalley arrête le chronomètre au bout de deux minutes. « Qui a appelé le "
          "144 ? » Silence. Personne. « Le défibrillateur ? » Maëlle l'a cherché, sans que "
          "personne le lui demande. « Vous avez fait des compressions parfaites sur un homme "
          "pour qui personne n'a jamais appelé à l'aide. »", [
            R("« J'ai foncé sans organiser l'équipe. »", 2, "er2 ic2 cc1"),
            R("« Dans la vraie vie, il y aurait du monde autour : quelqu'un aurait forcément "
              "appelé les secours, dans un hall de gare. »", 7, "er-1 ic-1"),
            R("« Je pensais que quelqu'un l'avait fait. »", 7, "cc1 ic-1"),
            R("« C'est le stress. »", 7, "er-1"),
            R("« Noah aurait pu appeler, il ne faisait rien. »", 7, "ic-3 rd-1"),
        ]),
        I(7, "chevalley", "neutral",
          "« Dernier scénario. » La Dre Chevalley pose sur la table un petit mannequin, de la "
          "taille d'un bébé. « Nourrisson de trois mois, retrouvé inconscient dans son lit "
          "par sa mère. Yasmine, vous menez. » Yasmine s'approche. Ses mains, au-dessus du "
          "mannequin, ne bougent pas. Cinq secondes. Dix. Elle est devenue grise.", [
            R("À voix basse : « Yasmine, je prends ? »",
              8, "em3 ic2 er1 co2", sets=["yasmine_soutenue"]),
            R("« Yasmine, on t'attend ! »", 9, "em-2 ic-1 er-1 co-1"),
            R("Prendre la place sans rien dire, et lancer le scénario.", 8, "ic1 em1",
              sets=["yasmine_soutenue"]),
            R("Rire nerveusement : « Elle a vu un fantôme. »", 9, "em-3 rd-2 co-1"),
            R("Regarder la Dre Chevalley, pour qu'elle arrête l'exercice.", 8, "ic2 em1",
              sets=["yasmine_soutenue"]),
            R("« Dre Chevalley, je crois qu'il faut une pause. » En se plaçant entre Yasmine "
              "et le groupe, pour que personne ne la regarde.", 8, "em2 ic2 rd2 co1",
              sets=["yasmine_soutenue"]),
        ]),
        I(8, "chevalley", "neutral",
          "La Dre Chevalley dit simplement : « Pause de dix minutes. » Yasmine sort sans un "
          "mot. Par la porte vitrée, vous la voyez dans le couloir, dos au mur, les yeux "
          "fermés. La Dre Chevalley vous regarde. « Allez-y, si vous voulez. Pas pour la faire "
          "parler. Pour qu'elle ne soit pas seule. »", [
            R("S'asseoir à côté d'elle, sans rien demander.", 10,
              "em3 co3 rd1", sets=["yasmine_soutenue"]),
            R("« Elle préférera être seule. »", 11, "em-1 co-1"),
            R("Sortir, et lui demander : « Qu'est-ce qui t'est arrivé ? Raconte. »",
              10, "em1 pb-2 rd-1"),
            R("Lui apporter un verre d'eau, et revenir dans la salle.", 11, "em1 rd1 co2"),
            R("Glisser à Maëlle, pendant que la Dre range le mannequin : « C'était quoi, son "
              "problème, à Yasmine ? »", 11, "rd-2 pb-1 em-1"),
        ]),
        I(9, "yasmine", "cold-anger",
          "Yasmine se redresse d'un coup. « Rigole. » Sa voix est blanche. « Le jour où tu en "
          "auras un vrai dans les mains, tu rigoleras moins. » Elle sort. La Dre Chevalley "
          "arrête l'exercice et vous regarde longtemps.", [
            R("La suivre. « Pardon. »", 10, "rd2 em2 er1 co1",
              sets=["yasmine_soutenue"]),
            R("« C'était pour détendre. »", 11, "er-1 rd-1"),
            R("Ne rien dire.", 11, "er-1 co-1"),
            R("« Elle est susceptible, hein. Elle prend tout trop au sérieux, depuis le début "
              "de l'année. »", 11, "rd-2 em-2"),
        ]),
        I(10, "yasmine", "melancholic",
          "Yasmine ne vous regarde pas. « Ça va. » Un long silence. « C'est le mannequin. La "
          "taille. » Elle n'en dit pas plus, et vous ne demandez rien. Au bout de dix "
          "minutes, elle se lève, se passe de l'eau sur le visage et rentre dans la salle. "
          "Elle mène le scénario du nourrisson sans une erreur, la mâchoire serrée.",
          [go(13)]),
        I(13, "chevalley", "neutral",
          "Débriefing en cercle. La Dre Chevalley distribue des cartons. « Chacun écrit une "
          "chose que l'équipe a bien faite, et une chose à changer. Pas de nom. » Elle "
          "ramasse, lit à voix haute. Puis elle vous regarde. « Et vous, à l'oral : qu'est-ce "
          "que l'équipe a appris ? »", [
            R("« À répéter, même quand on a peur. »", 11, "ic2 cc2 er1 co1"),
            R("« Que Yasmine est la meilleure, et qu'on devrait la laisser mener à chaque "
              "fois : on gagnerait du temps, et le patient aussi. »", 11, "ic-2 er-1"),
            R("« Rien de plus que le cours en ligne. »", 11, "ic-2 rd-1"),
            R("« À appeler le 144 avant tout. »", 11, "cc2 ic1"),
            R("« Je ne sais pas. Je n'y ai pas encore réfléchi. »", 11, "cc-1"),
        ]),
        I(11, "chevalley", "neutral",
          "Fin de séance. La Dre Chevalley rassemble le groupe. « Ce que vous avez appris "
          "aujourd'hui, ce n'est pas le rythme des compressions. C'est que, dans une équipe, "
          "chacun porte quelque chose qu'on ne voit pas. Le leader, c'est celui qui le voit à "
          "temps. » Elle range le petit mannequin dans sa boîte, avec un soin étrange. Puis, "
          "à vous seul·e : « Et vous, comment ça va ? Vos mains tremblaient, au début. »", [
            R("« Elles tremblaient. J'avais peur. »",
              END, "er3 cc1"),
            R("« Très bien, merci. »", END, "er-1"),
            R("« C'est la caféine. »", END, "er-1 cc-1"),
            R("« Je crois que je ne serai jamais à l'aise avec l'urgence. Yasmine, elle, "
              "est née pour ça, et moi je suis juste un·e étudiant·e qui a lu des livres. »",
              END, "er-2 ic-1"),
            R("« Mieux qu'au début. J'ai compris que je n'étais pas seul·e. »",
              END, "er2 ic1"),
        ]),
    ],
)

CH2 = C(2, "Deux Pittet",
    situation=(
        "Octobre à décembre. À la fac, le module sang, immunité, microbes, un tutorat du "
        "jeudi où Noah répond à tout avec un chatbot, et une matinée de réanimation au "
        "centre de simulation. Au cabinet de Montchéry, c'est la saison des vaccins et des "
        "prises de sang. Et dans le logiciel, il y a deux « Pittet J. »."
    ),
    objectives=(
        "informer un parent hésitant sans pression ni leçon, dans les limites de son rôle ; "
        "vérifier l'identité avant toute information au téléphone et ne donner aucun "
        "résultat (secret médical, art. 321 CP) ; reconnaître une erreur et s'excuser sans "
        "se défausser sur un·e collègue, et participer à une déclaration d'incident ; "
        "contribuer à un travail de groupe sans prendre le pouvoir ni se taire ; refuser de "
        "partager un travail personnel qui servira à plagier, et déclarer l'usage d'une IA ; "
        "respecter le refus de traitement éclairé d'une patiente ; parler à une adolescente "
        "sans trahir sa grand-mère ; inclure un pair isolé ; organiser une réanimation de "
        "base avec une communication en boucle fermée, et voir le ou la collègue qui se "
        "fige."
    ),
    anchoring=(
        "UNIL BMed2.2 (sang, immunité, microbes : immunité adaptative, épidémiologie), "
        "BMed2.8 (anamnèse et communication ; urgences et réanimation) et BMed2.7 (équipe "
        "interprofessionnelle) · UNIGE dimensions communautaires (médecine ambulatoire, "
        "éthique, santé publique), APP/CBCL, plagiat et IA générative, stage IMFE (pédiatre), "
        "compétences cliniques (gestes de base) · UZH Humanbiologie I (Blut und "
        "Immunsystem), POL-Tutorat I, Mantelstudium Notfall- und Rettungsmedizin (Lucerne)."
    ),
    focus=("pb", "cc", "ic", "em"),
    scenes=[S2_1, S2_2, S2_3A, S2_3B, S2_4, S2_5, S2_6],
)
