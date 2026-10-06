"""Chapitre 5 — Une seule ligne (semaine 6, la nuit du 14).

Trois scènes communes (5.1-5.3), puis deux voies selon ce qui s'est passé à 2 h 10 :
  - erreur : M. Jaquier reçoit une pénicilline malgré son allergie (5.4-5.6 « E ») ;
  - évitée : l'erreur est interceptée (5.4-5.6 « N »).
Voir docs/MedStudents_Y4_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, when

# ---------------------------------------------------------------------------
# 5.1 L'entrée de 19 h
# ---------------------------------------------------------------------------
S5_1 = S(1, "5.1 L'entrée de 19 h",
    "Jeudi 14, 19 h. Début de votre nuit de garde avec le Dr Neuhaus. Une entrée arrive des "
    "urgences au 304 : M. Roland Jaquier, 71 ans, fièvre et toux depuis trois jours, un "
    "peu confus. Les urgences pensent à une infection virale. Sa femme est avec lui.",
    focus=("cc", "rd", "pb"),
    entries=[
        Entry(2, when(all=["nuits_enchainees"]),
              "Jeudi 14, 19 h. Deuxième nuit de garde d'affilée : vous avez dormi quatre "
              "heures cet après-midi. Une entrée arrive des urgences au 304 : M. Roland "
              "Jaquier, 71 ans, fièvre et toux depuis trois jours, un peu confus. Les urgences "
              "pensent à une infection virale. Sa femme est avec lui."),
    ],
    nodes=[
        I(1, "neuhaus", "neutral",
          "« Alex. Entrée au 304. » Neuhaus vous tend la lettre des urgences sans lever les "
          "yeux de son téléphone. « Tu fais l'anamnèse et le status, tu remplis l'entrée dans "
          "le dossier, je signe en passant. J'ai deux autres entrées et le 318 qui "
          "décompense. »", [
            R("« D'accord. Je fais une anamnèse complète — traitements, allergies — et je te "
              "présente le patient avant que tu signes. »", 3, "pb2 cc2 ic2"),
            R("« OK, je m'en occupe. »", 3, "ic1"),
            R("« Je peux reprendre la lettre des urgences ? Ça ira plus vite. »", 4, "pb-2 cc-1"),
            R("« D'accord. Tu passes relire avant de signer, ou je t'appelle ? »", 3, "pb2 ic2"),
            R("« Tu signes sans relire ? Parfait, ça ira plus vite. »", 3, "pb-3 ic-1"),
        ]),
        I(2, "neuhaus", "neutral",
          "Neuhaus vous regarde deux secondes de trop. « T'étais pas déjà là hier soir ? T'as "
          "une tête de déterré. » Il vous tend la lettre des urgences. « Bon. Entrée au 304. "
          "Anamnèse, status, tu remplis le dossier, je signe en passant. J'ai deux entrées et "
          "le 318 qui décompense. »", [
            R("« Deuxième nuit d'affilée, oui. Je te le dis pour que tu relises mes entrées "
              "de près cette nuit. »", 3, "pb2 er2 cc1 ic1"),
            R("« Ça va, je suis en forme. »", 3, "er-1 pb-1"),
            R("« Je peux reprendre la lettre des urgences ? Ça ira plus vite. »", 4, "pb-2 cc-1"),
            R("« Oui. Je vais être lent·e, mais je ferai tout. »", 3, "pb1 er1"),
            R("« Une nuit de plus ou de moins… Envoie. »", 3, "er-2 pb-2"),
        ]),
        I(3, "monique", "anxious",
          "Chambre 304. M. Jaquier est calé contre ses oreillers, des lunettes à oxygène sous "
          "le nez, les joues rouges de fièvre. Sa femme est assise sur la chaise, un sac de "
          "pharmacie en plastique sur les genoux. « Bonsoir. Vous êtes le médecin ? »", [
            R("« Bonsoir. Alex, étudiant·e en médecine, je travaille avec le Dr Neuhaus. Je "
              "vais vous poser des questions pour son dossier. Monsieur Jaquier, vous êtes "
              "d'accord que votre épouse reste ? »", 5, "rd3 cc2 pb1"),
            R("« Oui, enfin, presque. Je vais vous poser quelques questions. »", 5, "cc-1 pb-2"),
            R("S'adresser à l'épouse : « Madame, il prend quoi, comme médicaments ? »", 6, "rd-2"),
            R("« Bonsoir, madame, bonsoir monsieur. Je suis étudiant·e. On va prendre le temps. »", 5, "rd2 cc1 em1"),
            R("« Oui, c'est moi qui m'occupe de vous cette nuit. »", 5, "pb-3 cc-2"),
        ]),
        I(4, "neuhaus", "cold-anger",
          "Neuhaus lève enfin les yeux. « La lettre des urgences, c'est leur anamnèse, pas la "
          "tienne. Ils l'ont faite en quatre minutes dans un couloir. » Il retourne à son "
          "écran. « Va le voir. »", [
            R("« Tu as raison. J'y vais. »", 3, "pb1 ic1"),
            R("« Je la recopie quand même, et je complète au lit. »", 3, "pb-2 cc-1"),
            R("« D'accord. Je reprends tout avec eux. »", 3, "pb2 cc1"),
            R("« Ils ont quand même des infos, eux. »", 3, "pb-2 ic-1"),
        ]),
        I(5, "roland", "neutral",
          "« C'est rien, une grippe. » Sa voix est rauque. « C'est elle qui a voulu "
          "venir. » Sa femme ne dit rien. Il tousse longtemps.", [
            R("« Je vais quand même vous poser toutes les questions, même celles qui paraissent "
              "bêtes. Depuis quand avez-vous de la fièvre ? »", 7, "cc2 rd1 pb1"),
            R("« On va faire vite, alors. »", 7, "cc-1 pb-1"),
            R("« Une grippe, peut-être. Racontez-moi quand même, depuis le début. »", 7, "cc2 rd2"),
            R("« Si c'est rien, on va faire court. »", 7, "cc-2 pb-2"),
        ]),
        I(6, "roland", "cold-anger",
          "« Je suis là, vous savez. » Il se redresse, vexé. « Je ne suis pas encore "
          "gâteux. »", [
            R("« Pardon, M. Jaquier. C'est à vous que je dois poser les questions. »", 5, "rd2 er1"),
            R("« Votre femme connaît sûrement mieux vos médicaments. »", 7, "rd-2"),
            R("« Vous avez raison. Et votre épouse complétera si vous le voulez. »", 5, "rd2 cc1"),
            R("« Bon, bon. »", 7, "rd-2 er-1"),
        ]),
        I(7, "monique", "neutral",
          "Mme Jaquier pose le sac sur la table et aligne les boîtes : bisoprolol « pour le "
          "cœur », un anticoagulant, des gouttes pour les yeux. Vous notez. Il reste une ligne "
          "du formulaire d'entrée : « Allergies ». La lettre des urgences dit : « aucune "
          "allergie connue (selon lettre du médecin traitant, 2019) ».", [
            R("« Est-ce que vous avez déjà eu une réaction à un médicament ? Une éruption, un "
              "gonflement, un malaise ? »", 8, "cc3 pb2"),
            R("« Des allergies ? »", 9, "cc0"),
            R("« Les urgences ont noté « aucune allergie connue », je passe à l'examen. »",
              10, "pb-3 cc-2"),
            R("« Est-ce qu'un médecin vous a déjà dit de ne jamais prendre un médicament ? »", 8, "cc3 pb1"),
            R("Cocher « aucune allergie » en recopiant la lettre, sans poser la question.", 10, "pb-3 cc-3 rd-1"),
        ]),
        I(8, "monique", "anxious",
          "« La pénicilline », dit-elle aussitôt. M. Jaquier lève les yeux au ciel. « Oh, "
          "arrête. C'était il y a trente ans. » — « Tu avais gonflé comme un ballon. Ils "
          "t'avaient gardé la nuit. » — « Une piqûre de guêpe, sûrement. »", [
            R("« Racontez-moi exactement ce qui s'est passé ce jour-là. »", 11, "cc3 rd1 pb2"),
            R("« D'accord, je note « pénicilline ? ». »", 12, "cc0 pb0"),
            R("« Si c'était il y a trente ans, ce n'est probablement plus d'actualité. »",
              13, "pb-3 cc-3 rd-1"),
            R("« Madame, qu'est-ce qui vous fait dire ça ? »", 11, "em2 cc2"),
            R("« Une guêpe ou la pénicilline, on ne saura jamais. Je ne note rien. »", 13, "pb-3 cc-3 rd-1"),
        ]),
        I(9, "roland", "neutral",
          "« Non. Rien. » M. Jaquier répond avant même la fin de la question. Sa femme ouvre la "
          "bouche, le regarde, et la referme.", [
            R("« Madame, vous vouliez dire quelque chose ? »", 8, "em2 cc2 ic1"),
            R("« Et une réaction à un médicament, un jour ? Un gonflement, un malaise ? »",
              8, "cc2 pb2"),
            R("« Parfait. Aucune allergie. »", 10, "cc-1 pb-1"),
            R("« Pas de médicament qui vous aurait fait gonfler, ou gêné pour respirer ? »", 8, "cc3 pb1"),
            R("Voir Mme Jaquier hésiter, et passer quand même à la suite.", 10, "em-2 pb-2"),
        ]),
        I(10, "narr", "",
          "Vous cochez « aucune allergie connue » et passez à l'examen. Mme Jaquier fixe le sac "
          "de pharmacie. Elle a l'air de chercher ses mots.", [
            R("« Madame, vous avez l'air de vouloir ajouter quelque chose ? »", 8, "em2 cc2"),
            R("Passer à l'examen clinique.", 14, "pb-1"),
            R("S'arrêter, reposer le stylo : « Prenez votre temps. »", 8, "em2 rd2"),
            R("« Vous me direz ça demain, madame, on a peu de temps. »", 14, "rd-2 pb-2 em-1"),
        ]),
        I(11, "monique", "anxious",
          "« C'était pour une angine. Une piqûre chez le médecin. Dix minutes après, il avait "
          "la bouche toute gonflée, il respirait mal, il est devenu gris. L'ambulance. Ils "
          "l'ont gardé la nuit. Le médecin a dit : plus jamais de pénicilline. » M. Jaquier "
          "grommelle : « On en fait tout un plat. »", [
            R("« Ce que vous décrivez, c'est une réaction grave. Je l'inscris maintenant dans le "
              "champ « allergies » du dossier, avec la description, pour que tout le monde la "
              "voie. Merci de me l'avoir dit. »", 15,
              sets=["allergie_dossier"], scores="cc3 pb3 ic2 rd1"),
            R("« Je le note dans mon carnet, je le reporterai proprement dans le dossier "
              "après. »", 15, sets=["allergie_carnet"], scores="pb-1 cc0"),
            R("« M. Jaquier a raison, on ne va pas en faire un plat. »", 13, "rd-2 pb-3 cc-2"),
            R("« Je vous crois. Je l'écris au champ allergies du dossier, et je le dirai au médecin. »", 15, "cc3 pb2 ic2", sets=["allergie_dossier"]),
            R("« On verra ça avec son médecin traitant. »", 15, "pb-2 cc-2", sets=["allergie_carnet"]),
        ]),
        I(12, "monique", "anxious",
          "Elle regarde votre carnet par-dessus vos mains. « Pénicilline point "
          "d'interrogation ? » Elle secoue la tête. « Ce n'est pas un point d'interrogation. "
          "Il a failli mourir. »", [
            R("« Pardon. Racontez-moi exactement. »", 11, "em2 cc1"),
            R("« Je vérifierai avec son médecin traitant demain. »", 14,
              sets=["allergie_carnet"], scores="pb-1 em-1"),
            R("Rayer le point d'interrogation et écrire « anaphylaxie probable » devant elle.", 11, "pb2 rd1 cc1"),
            R("« Je ne suis pas là pour écrire des romans. »", 14, "rd-3 em-2", sets=["allergie_carnet"]),
        ]),
        I(13, "monique", "resigned",
          "« Plus d'actualité. » Elle répète vos mots, doucement. Puis elle regarde votre "
          "badge, et elle se tait. Vous êtes le médecin.", [
            R("« Pardon, je me suis avancé·e. Racontez-moi ce qui s'est passé. »", 11, "pb2 er1 rd1"),
            R("« Je le note quand même, par précaution. »", 14,
              sets=["allergie_carnet"], scores="pb0"),
            R("Passer à l'examen clinique.", 14, "pb-2 rd-1"),
            R("« Madame, vous le connaissez mieux que moi. Dites-moi ce qui s'est passé. »", 11, "rd2 em2"),
            R("« Voilà, on est d'accord. »", 14, "rd-3 pb-3 em-1"),
        ]),
        I(14, "neuhaus", "neutral",
          "Examen : 39,2 °C, saturation 91 % sous deux litres, crépitants à la base droite, "
          "légère confusion. Neuhaus passe la tête par la porte. « T'as fini ? Topo en deux "
          "phrases, j'ai le 318. »", [
            R("« M. Jaquier, 71 ans, fibrillation auriculaire sous bêtabloquant et "
              "anticoagulant, fièvre et toux depuis trois jours, crépitants à droite, "
              "légèrement confus. Pas d'allergie connue selon les urgences. »", 16, "cc2 ic1"),
            R("« Pneumonie probable, stable, rien de particulier. »", 16, "cc-1 ic-1"),
            R("« Pneumonie probable, légèrement confus. Je n'ai pas pu vérifier les allergies avec sa femme. »", 16, "cc2 pb1"),
            R("« Rien à signaler. »", 16, "cc-3 ic-2"),
        ]),
        I(15, "neuhaus", "neutral",
          "Examen : 39,2 °C, saturation 91 % sous deux litres, crépitants à la base droite, "
          "légère confusion. Neuhaus passe la tête par la porte. « T'as fini ? Topo en deux "
          "phrases, j'ai le 318. »", [
            R("« M. Jaquier, 71 ans, fibrillation auriculaire sous bêtabloquant et "
              "anticoagulant, fièvre et toux depuis trois jours, crépitants à droite. Et une "
              "réaction grave à la pénicilline il y a trente ans : œdème, détresse "
              "respiratoire, une nuit d'hôpital. »", 17,
              sets=["allergie_transmise"], scores="cc3 ic3 pb2"),
            R("« Pneumonie probable. Il y a peut-être une allergie à la pénicilline, mais le "
              "patient dit que ce n'était rien. »", 17,
              sets=["allergie_transmise"], scores="cc1 ic1 pb-1"),
            R("« Pneumonie probable, stable, rien de particulier. »", 17, "cc-2 ic-2"),
            R("« Réaction grave à la pénicilline il y a trente ans. Je l'écris dans le dossier maintenant, avant que tu signes. »", 17, "cc3 ic2 pb2", sets=["allergie_transmise", "allergie_dossier"]),
            R("« Rien de spécial. Sa femme s'inquiète pour tout. »", 17, "rd-2 ic-3 cc-2"),
        ]),
        I(16, "neuhaus", "neutral",
          "« OK. Pas d'antibiotique pour l'instant, les urgences pensent virus. J'attends la "
          "radio relue et la CRP. » Il est déjà reparti. « Tu finis l'entrée, on se voit à la "
          "relève de 21 h. »", [
            R("Finir l'entrée dans le dossier tout de suite, pendant que c'est frais.", END, "pb2 cc1"),
            R("« Je la finirai après la relève. »", END, "pb-2"),
            R("Finir l'entrée, et relire la lettre des urgences ligne par ligne.", -1, "pb2 cc1"),
            R("Copier-coller la lettre des urgences dans l'entrée.", -1, "pb-3 cc-2"),
        ]),
        I(17, "neuhaus", "neutral",
          "« OK. Pas d'antibiotique pour l'instant, les urgences pensent virus. J'attends la "
          "radio relue et la CRP. » Il est déjà reparti. « Tu finis l'entrée, on se voit à la "
          "relève de 21 h. »", [
            R("Remplir le champ « allergies » du dossier tout de suite, avant la relève.", END,
              sets=["allergie_dossier"], scores="pb3 cc2 ic1"),
            R("« Je mettrai le reste au propre après la relève. »", END, "pb-1"),
            R("Écrire l'allergie dans le champ dédié et dans l'observation, avec les mots de Mme Jaquier.", -1, "pb3 cc3", sets=["allergie_dossier"]),
            R("« Je le ferai demain matin, ce n'est pas urgent. »", -1, "pb-3 cc-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.2 La relève de 21 h
# ---------------------------------------------------------------------------
S5_2 = S(2, "5.2 La relève",
    "21 h. Salle de soins. Relève médico-infirmière : Kevin Da Silva prend la nuit, "
    "Neuhaus est de garde, Jonas termine sa journée. Fatou Diallo finit son service. Vous "
    "présentez l'entrée du 304.",
    focus=("ic", "cc", "er"),
    entries=[
        Entry(3, when(all=["allergie_dossier"])),
        Entry(2, when(all=["allergie_carnet"])),
    ],
    nodes=[
        I(1, "kevin", "neutral",
          "Kevin décapuchonne son stylo. « Le 304, l'entrée de ce soir. Qu'est-ce que je dois "
          "savoir pour la nuit ? »", [
            R("Transmission structurée : situation, antécédents et traitements, examen, et ce "
              "qu'il faut surveiller — saturation, tension, confusion, avec des seuils pour "
              "appeler. « Allergies : aucune connue selon les urgences. »", 4, "cc3 ic2"),
            R("« Pneumonie probable, rien de spécial. »", 4, "cc-2 ic-2"),
            R("« Tout est dans le dossier. »", 5, "ic-3 cc-2"),
            R("Transmission structurée, puis : « Je n'ai pas pu vérifier les allergies moi-même. À contrôler avant toute première dose. »", 4, "cc3 ic2 pb1"),
            R("« Il dort, il n'y aura rien cette nuit. »", 4, "cc-3 ic-2 pb-1"),
        ]),
        I(2, "kevin", "neutral",
          "Kevin décapuchonne son stylo. « Le 304, l'entrée de ce soir. Qu'est-ce que je dois "
          "savoir pour la nuit ? » Dans votre poche, le carnet où vous avez noté ce que Mme "
          "Jaquier a dit.", [
            R("Transmission structurée, puis : « Et attention : sa femme décrit une réaction "
              "grave à la pénicilline il y a trente ans. Ce n'est pas encore dans le dossier — "
              "je le mets maintenant, devant toi. »", 4,
              sets=["allergie_dossier", "allergie_transmise"], scores="cc3 ic3 pb2"),
            R("« Pneumonie probable. Il y a peut-être une allergie à la pénicilline, à "
              "vérifier. »", 4, sets=["allergie_transmise"], scores="cc1 ic1"),
            R("Transmission structurée. « Allergies : aucune dans le dossier. »", 4, "pb-3 ic-1"),
            R("« Allergie probable à la pénicilline, décrite par sa femme. Je te l'écris sur ta feuille. »", 4, "cc2 ic2", sets=["allergie_transmise"]),
            R("« Rien de spécial. »", 4, "pb-3 ic-3 cc-1"),
        ]),
        I(3, "kevin", "neutral",
          "Kevin a déjà le dossier ouvert. « Le 304. Il y a une pastille rouge : allergie "
          "grave à la pénicilline. C'est toi qui l'as mise ? Raconte. »", [
            R("« Oui. Sa femme décrit un œdème de la bouche et une détresse respiratoire après "
              "une injection, il y a trente ans. Lui minimise. » Puis la suite de la "
              "transmission.", 4, sets=["allergie_transmise"], scores="cc3 ic2 pb1"),
            R("« Oui, c'est dans le dossier. »", 4, "cc1"),
            R("« Oui. Tu peux lui mettre un bracelet rouge ? »", 4, "ic3 pb1", sets=["allergie_transmise"]),
            R("« Oui. Mais lui dit que ce n'est rien, alors… »", 4, "pb-2 cc-2"),
        ]),
        I(4, "narr", "",
          "Le bip de Neuhaus sonne. « On accélère, le 318 désature. » Jonas passe la tête : "
          "« Bonne nuit, les zombies ! » Derrière lui, Fatou, déjà en manteau, hésite dans "
          "l'embrasure. Elle vous regarde.", [
            R("« Fatou ? Vous vouliez dire quelque chose ? »", 6, "ic3 em1 rd1"),
            R("« Bonne nuit ! »", 12, "ic-1"),
            R("Faire signe à Fatou d'approcher, pendant que Neuhaus répond au bip.", 6, "ic3 rd1"),
            R("« Fatou, on est en pleine relève, ça peut attendre ? »", 12, "ic-3 rd-2"),
        ]),
        I(5, "kevin", "cold-anger",
          "« Le dossier, je le lirai. » Kevin pose son stylo. « C'est toi que j'écoute, là. "
          "Qu'est-ce que je surveille cette nuit, et quand est-ce que j'appelle ? »", [
            R("Reprendre : situation, antécédents, examen, surveillance, seuils d'appel. "
              "« Allergies : aucune connue selon les urgences. »", 4, "cc2 ic2"),
            R("« La saturation et la fièvre. »", 4, "cc0 ic-1"),
            R("« Pardon. Je te fais une vraie transmission. »", 4, "ic2 cc2"),
            R("« C'est ton travail de lire le dossier. »", 4, "ic-3 rd-1"),
        ]),
        I(6, "fatou", "neutral",
          "« La dame du 304. » Elle parle bas, comme toujours. « En partant, elle m'a dit pour "
          "la pénicilline. Qu'il avait fait une grosse réaction, une fois. Elle avait peur "
          "qu'on oublie. » Un temps. « C'est noté ? »", [
            R("« Merci, Fatou. Qu'est-ce qu'elle vous a dit exactement ? Je vérifie que c'est "
              "dans le champ allergies, et je le complète maintenant. »", 7,
              sets=["allergie_dossier", "allergie_transmise"], scores="ic3 pb3 cc2 rd1"),
            R("« Les urgences ont écrit « aucune allergie », et le patient m'a dit que "
              "non. »", 8, "ic-3 pb-2 rd-2"),
            R("« Je vérifierai demain avec son médecin traitant. »", 8,
              sets=["allergie_carnet"], scores="pb-1 ic-1"),
            R("« Non, ce n'est pas noté. Merci. Je le fais tout de suite, et je le dis à Kevin. »", 7, "ic3 pb3 cc1", sets=["allergie_dossier", "allergie_transmise"]),
            R("« Merci, Fatou, on gère. »", 8, "ic-2 pb-2"),
        ]),
        I(7, "kevin", "neutral",
          "Fatou répète les mots de Mme Jaquier : la piqûre, la bouche gonflée, l'ambulance. "
          "Kevin écrit en majuscules sur sa feuille : « ALLERGIE PÉNICILLINE — "
          "ANAPHYLAXIE », et va chercher un bracelet rouge. « Bien vu, Fatou. »", [
            R("« Merci à vous deux. »", 9, "ic2 rd1"),
            R("« C'était déjà plus ou moins noté. »", 9, "ic-2 rd-1"),
            R("« Fatou, merci. Vous avez peut-être évité quelque chose de grave. »", 9, "ic3 rd2"),
            R("Hocher la tête, déjà ailleurs.", 9, "ic-1"),
        ]),
        I(8, "fatou", "resigned",
          "« D'accord. » Fatou remonte la fermeture de son manteau. « Bonne nuit. » Elle s'en "
          "va. Kevin vous regarde une seconde, puis retourne à sa feuille.", [
            R("La rattraper dans le couloir. « Fatou, attendez. Redites-moi. »", 10, "ic2 em1"),
            R("Laisser partir.", 11, "ic-2 em-1"),
            R("Rappeler Fatou et lui demander de le redire devant Kevin.", 10, "ic3 cc1"),
            R("« Elle en fait toujours trop. »", 11, "ic-3 rd-3"),
        ]),
        I(9, "neuhaus", "neutral",
          "Neuhaus récapitule en enfilant sa veste. « Le 304 : pas d'antibiotique pour "
          "l'instant, j'attends la radio relue. Kevin, tu m'appelles s'il chauffe. Alex, tu "
          "dors dans la chambre de garde, je te bippe si besoin. »", [
            R("« D'accord. Mon bip est allumé. »", END, "ic1 cc1"),
            R("« Je vais relire les entrées de la soirée avant de m'allonger. »", END, "pb2"),
            R("« Je vais dormir. Bippez-moi seulement si c'est vraiment grave. »", END, "ic-2 pb-1"),
            R("« Kevin, n'hésite pas à m'appeler, même pour une simple question. »", -1, "ic3"),
        ]),
        I(10, "fatou", "neutral",
          "Fatou s'arrête devant l'ascenseur. « Il avait gonflé, il ne respirait plus bien, ils "
          "l'ont gardé une nuit. Il y a trente ans. » Elle hausse les épaules. « Lui dit que "
          "c'est rien. Elle, elle avait peur. »", [
            R("« Merci. Je le mets dans le dossier maintenant, et je le dis à Kevin. »", 9,
              sets=["allergie_dossier", "allergie_transmise"], scores="ic3 pb2 cc1"),
            R("« Je le note dans mon carnet. »", 11, sets=["allergie_carnet"], scores="pb-1"),
            R("« Merci. Je le dis à Kevin, et je l'écris au dossier. »", 9, "ic2 pb2 cc1", sets=["allergie_dossier", "allergie_transmise"]),
            R("« Lui dit que c'est rien. On verra. »", 11, "pb-3 rd-2 ic-1"),
        ]),
        I(11, "narr", "",
          "Fatou est partie. Kevin coche sa feuille de transmission. Neuhaus éteint l'écran. "
          "Dans votre poche, votre carnet.", [
            R("Suivre Neuhaus pour la fin de la relève.", 9, ""),
        ]),
        I(12, "narr", "",
          "Fatou hésite encore une seconde, puis remonte la fermeture de son manteau et s'en "
          "va. Personne ne l'a vue partir.", [
            R("Suivre Neuhaus pour la fin de la relève.", 9, ""),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.3 Deux heures dix
# ---------------------------------------------------------------------------
_INTRO_53 = (
    "2 h 10. Le bip vous tire de la chambre de garde. Kevin : le 304 chauffe — 39,8 °C, "
    "tension 95/55, saturation 88 %, plus confus. La radio relue à minuit montre une "
    "pneumonie lobaire droite. Neuhaus est aux urgences avec un infarctus ; il vous "
    "appelle sur le téléphone du service. Kevin est à côté de vous."
)
S5_3 = S(3, "5.3 Deux heures dix",
    _INTRO_53,
    focus=("ic", "pb", "cc"),
    entries=[
        Entry(30, when(all=["allergie_dossier"])),
        Entry(20, when(all=["allergie_transmise"])),
        Entry(10, when(all=["allergie_carnet"])),
    ],
    debriefs=[
        Debrief(when(all=["erreur"]), tone="hard", lead=(
            "À 2 h 25, la perfusion a été branchée. L'information existait depuis 19 h : "
            "dans la mémoire de Mme Jaquier, dans ce qu'avait entendu Fatou, parfois dans "
            "votre carnet. Elle n'a jamais atteint la personne qui prescrivait. La scène "
            "suivante raconte ce que ça coûte.")),
        Debrief(when(all=["evite"]), tone="good", lead=(
            "L'erreur n'a pas eu lieu. Pas par chance : parce qu'à un moment de la soirée, "
            "quelqu'un a demandé, écrit, transmis ou insisté. Regardez à quel moment "
            "c'était vous — et combien de fois ça aurait pu ne pas l'être.")),
    ],
    nodes=[
        # --- Voie par défaut : l'allergie n'a été ni notée ni transmise ----------
        I(1, "neuhaus", "neutral",
          "Au téléphone, la voix de Neuhaus est rapide, couverte par un moniteur. « Alex. "
          "Pneumonie lobaire, il se dégrade. On démarre amoxicilline-clavulanate IV, "
          "2,2 grammes, maintenant, et un bolus de 500 de NaCl. Je l'entre dans le système, tu "
          "dis à Kevin. Il a des allergies ? Regarde le dossier, vite. »", [
            R("« Le dossier dit « aucune allergie connue ». C'est repris de la lettre des "
              "urgences. »", 2, "cc1 pb-1"),
            R("« Aucune. »", 90, sets=["erreur"], scores="pb-2 cc-1"),
            R("« Le dossier dit aucune, mais c'est une info des urgences. Je la vérifie avec "
              "le patient avant la première dose. »", 3, "pb3 ic2 cc2"),
            R("« Attends, avant de signer : ses allergies viennent d'une lettre de 2019. Je vérifie. »", 3, "pb3 ic2"),
            R("« Aucune. Vas-y. »", 90, "pb-3 cc-1 ic-1", sets=["erreur"]),
        ]),
        I(2, "neuhaus", "neutral",
          "« Repris des urgences. OK. Donc aucune. » Un bip, derrière lui, quelqu'un crie un "
          "chiffre de tension. « Tu dis à Kevin, je signe. »", [
            R("« Attends. Je préfère vérifier avec le patient ou sa femme. Deux minutes. »",
              3, "pb3 ic2 er1"),
            R("« OK. »", 90, sets=["erreur"], scores="pb-2 ic-1"),
            R("« Le dossier dit aucune, mais personne n'a vérifié avec la famille. Donne-moi deux minutes. »", 3, "pb3 cc2"),
            R("« D'accord, je dis à Kevin de brancher. »", 90, "pb-2 ic-1", sets=["erreur"]),
        ]),
        I(3, "roland", "confused",
          "Au lit, M. Jaquier est brûlant, les yeux mi-clos. « Allergique ? » Il cherche. "
          "« Non… non. C'est Monique qui s'occupe de ça. »", [
            R("« Je vais appeler votre épouse. »", 4, "pb3 cc1 rd1"),
            R("À Kevin : « Il dit non. C'est bon. »", 90, sets=["erreur"], scores="pb-2 cc-1"),
            R("« Monsieur Jaquier, vous avez déjà gonflé après une piqûre ? Un médicament ? »", 4, "cc3 pb2"),
            R("« Il est confus, on ne tirera rien de lui. On y va. »", 90, "pb-3 rd-2", sets=["erreur"]),
        ]),
        I(4, "kevin", "neutral",
          "Kevin, la poche déjà montée sur la tubulure : « Appeler sa femme à 2 h 20 ? Elle va "
          "paniquer. Neuhaus attend, et lui, il est à 88 %. »", [
            R("« Je sais. Je l'appelle quand même : c'est la première dose. Trente "
              "secondes. »", 5, "pb3 er2 ic1"),
            R("« T'as raison. On y va. »", 90, sets=["erreur"], scores="pb-2 ic-1"),
            R("« Trente secondes. Si elle ne répond pas, on demande un autre antibiotique à Neuhaus. »", 5, "pb3 ic2 er1"),
            R("« Branche. J'en prends la responsabilité. »", 90, "pb-3 er-2 ic-1", sets=["erreur"]),
        ]),
        I(5, "monique", "anxious",
          "Trois sonneries. « Allô ? » La voix de quelqu'un qui dormait avec le téléphone "
          "sur la table de nuit. « Il est arrivé quelque chose ? »", [
            R("« Il est suivi de près, on s'occupe de lui. J'ai une question importante : "
              "est-ce qu'il a déjà réagi à un médicament ? »", 6, "cc3 em2 rd1"),
            R("« Madame, il a une allergie ? »", 6, "cc1 em-1"),
            R("« Madame Jaquier, pardon de vous réveiller. Il est suivi, il va bien pour l'instant. Une question sur ses allergies. »", 6, "cc3 em2 rd1"),
            R("« Rien de grave, c'est pour le dossier. Il est allergique à quelque chose ? »", 6, "cc-1 pb-1"),
        ]),
        I(6, "monique", "angry",
          "« La pénicilline ! » Elle crie presque. « Je l'ai dit ce soir ! Il avait failli "
          "mourir ! Vous n'allez pas lui donner de la pénicilline ? »", [
            R("« Non. Merci de me l'avoir redit. » Puis, sur l'autre ligne : « Neuhaus, stop : "
              "anaphylaxie à la pénicilline il y a trente ans, confirmée par son épouse. Il "
              "faut autre chose que l'amox-clav. »", 91,
              sets=["evite"], scores="cc3 ic3 pb2 er1"),
            R("« On s'en occupe, madame, rendormez-vous. » Puis prévenir Neuhaus.", 91,
              sets=["evite"], scores="cc1 ic1 em-1"),
            R("« Non, madame. On va lui donner autre chose. Merci. »", 91, "cc2 rd1 ic1", sets=["evite"]),
            R("« D'accord, je transmettrai. » Puis raccrocher, et envoyer un message à Neuhaus.", 91, "ic-1 cc-1", sets=["evite"]),
        ]),

        # --- Voie « carnet » : l'allergie est dans la poche d'Alex ---------------
        I(10, "neuhaus", "neutral",
          "Au téléphone, la voix de Neuhaus est rapide, couverte par un moniteur. « Alex. "
          "Pneumonie lobaire, il se dégrade. On démarre amoxicilline-clavulanate IV, "
          "2,2 grammes, et un bolus. Je l'entre dans le système. Il a des allergies ? Le "
          "dossier dit quoi ? » Le dossier dit « aucune allergie connue ». Votre carnet est "
          "dans votre poche.", [
            R("« Le dossier dit aucune — mais sa femme m'a décrit une réaction grave à la "
              "pénicilline, je l'ai notée dans mon carnet et je ne l'ai pas reportée. Pas "
              "d'amox-clav. »", 91, sets=["evite"], scores="pb3 cc3 ic2 er1"),
            R("« Rien dans le dossier. »", 90, sets=["erreur"], scores="pb-3 cc-3 ic-1"),
            R("« Je crois qu'il y avait quelque chose… Attends, je ne suis pas sûr·e. »",
              11, "cc-1 er-1"),
            R("« Attends : j'ai une note sur lui. Pénicilline. Je te lis ce que sa femme a dit. »", 91, "pb3 cc2 ic2", sets=["evite"]),
            R("« Le dossier dit aucune, c'est ce qui compte. »", 90, "pb-3 cc-2 ic-1", sets=["erreur"]),
        ]),
        I(11, "neuhaus", "neutral",
          "« T'es pas sûr·e de quoi ? » Il souffle. « Le dossier dit rien. J'ai un infarctus "
          "sur la table. Oui ou non ? »", [
            R("« Oui. Réaction grave à la pénicilline, décrite par sa femme à 19 h. Je l'ai "
              "dans mon carnet. »", 91, sets=["evite"], scores="pb3 er2 cc2"),
            R("« Non. Laisse tomber. »", 90, sets=["erreur"], scores="pb-3 er-1 cc-2 ic-1"),
            R("« Je ne suis pas sûr·e, donc on ne prend pas le risque. Donne autre chose. »", 91, "pb3 er2", sets=["evite"]),
            R("« Je ne sais pas. Fais comme tu penses. »", 90, "pb-3 er-2", sets=["erreur"]),
        ]),

        # --- Voie « transmise » : quelqu'un de l'équipe de nuit a entendu -------
        I(20, "neuhaus", "neutral",
          "Au téléphone, la voix de Neuhaus est rapide, couverte par un moniteur. « Alex. On "
          "démarre amoxicilline-clavulanate IV, 2,2 grammes, et un bolus. Il a des "
          "allergies ? » Un silence. « Attends. T'avais pas dit un truc sur la pénicilline, "
          "ce soir ? Le dossier dit rien. »", [
            R("« Si. Sa femme décrit une réaction grave il y a trente ans : gonflement, "
              "détresse respiratoire, une nuit à l'hôpital. Pas d'amox-clav. »", 91,
              sets=["evite"], scores="pb3 cc3 ic2 er1"),
            R("« Sa femme a évoqué une réaction, mais lui dit que ce n'était rien… Je ne sais "
              "pas. »", 21, "cc-1 pb-1"),
            R("« Non, je ne crois pas. Le dossier dit aucune. »", 90,
              sets=["erreur"], scores="pb-3 cc-3 ic-1"),
            R("« Oui. Pénicilline, réaction grave. Choisis autre chose, et je l'écris maintenant au dossier. »", 91, "pb3 cc2 ic2", sets=["evite"]),
            R("« C'était rien, sa femme exagère. »", 90, "pb-3 rd-2 cc-1", sets=["erreur"]),
        ]),
        I(21, "neuhaus", "neutral",
          "« Tu ne sais pas. Moi non plus. » On l'entend marcher vite. « Je ne peux pas laisser "
          "une pneumonie lobaire sans antibiotique. Décide : on y va ou pas ? »", [
            R("« On n'y va pas avec une pénicilline. Donne autre chose ; je confirme avec sa "
              "femme. »", 91, sets=["evite"], scores="pb3 er2 cc2"),
            R("« Je l'appelle maintenant. Deux minutes. »", 5, "pb3 ic1"),
            R("« On y va. Lui dit que c'était rien. »", 90, sets=["erreur"], scores="pb-3 er-1 cc-1 rd-2"),
            R("« Pas de pénicilline. Donne de la lévofloxacine, je vérifie demain matin avec elle. »", 91, "pb3 cc2", sets=["evite"]),
            R("« Je ne sais pas, c'est toi le médecin. »", 90, "pb-3 er-1 ic-1", sets=["erreur"]),
        ]),

        # --- Voie « dossier » : l'alerte fonctionne --------------------------------
        I(30, "neuhaus", "neutral",
          "Au téléphone, la voix de Neuhaus est rapide. « Alex. On démarre amoxicilline-"
          "clavulanate IV, je l'entre dans le système… » Un silence. « Merde. Alerte allergie. "
          "Pénicilline, réaction grave. C'est toi qui l'as mise ? »", [
            R("« Oui. Sa femme m'a décrit une anaphylaxie il y a trente ans. Il faut autre "
              "chose. »", 31, sets=["evite"], scores="cc3 ic2 pb2"),
            R("« Oui, mais lui dit que ce n'était rien. Tu peux passer outre si tu penses que "
              "c'est mieux. »", 32, sets=["evite"], scores="pb-3 cc-1"),
            R("« Oui. Réaction grave décrite par sa femme, et confirmée par une ASSC. »", 31, "cc3 ic2", sets=["evite"]),
            R("« Je ne sais plus, c'est peut-être une erreur de saisie. »", 32, "pb-3 cc-2", sets=["evite"]),
        ]),
        I(31, "neuhaus", "neutral",
          "« Bien joué. Lévofloxacine, alors. Et le bolus. » Il raccroche presque. « Tu restes "
          "avec Kevin et tu me rappelles dans trente minutes avec la tension et la "
          "saturation. »", [
            R("« Je te rappelle à 2 h 45 avec les paramètres, plus tôt si la systolique passe "
              "sous 90. »", 33, "cc3 ic3"),
            R("« OK. »", 33, "cc0"),
            R("« D'accord. Je reste au lit du patient avec Kevin. »", 33, "ic2 co1"),
            R("« Je retourne dormir, Kevin t'appellera. »", 33, "ic-2 co-1"),
        ]),
        I(32, "neuhaus", "cold-anger",
          "« Passer outre une anaphylaxie ? T'es pas bien ? » Il tape sur son clavier. "
          "« Lévofloxacine. Et la prochaine fois, tu ne proposes jamais ça. »", [
            R("« Pardon. Tu as raison. »", 33, "pb1 er1"),
            R("« C'était idiot. Merci d'avoir refusé. »", 33, "pb2 er1"),
            R("« C'était juste une suggestion. »", 33, "pb-2 er-1"),
            R("« Je voulais juste t'aider à aller plus vite. »", 33, "pb-2 er-1 cc-1"),
        ]),
        I(33, "kevin", "neutral",
          "Au 304, M. Jaquier tire sur ses lunettes à oxygène et essaie de se lever. « Où est "
          "Monique ? Je veux rentrer. » Kevin le retient d'une main. « Il arrache tout. On "
          "l'attache ? »", [
            R("« Non. On reste avec lui, on lui explique, on remet les lunettes. Je reste à "
              "côté un moment. »", 34, "rd3 co2 pb1"),
            R("« Oui, sinon il va désaturer. »", 34, "rd-3 pb-2"),
            R("« Fais comme tu veux. »", 34, "ic-2 rd-1"),
            R("« On lui dit où il est, on remet les lunettes, et j'appelle sa femme pour qu'elle lui parle. »", 34, "rd3 co2 ic1"),
            R("« Donne-lui un calmant, qu'il dorme. »", 34, "rd-2 pb-2"),
        ]),
        I(34, "narr", "",
          "À 2 h 40, la lévofloxacine coule. À 3 h, la tension remonte à 105. M. Jaquier dort. "
          "Vous restez assis·e au pied du lit jusqu'à 3 h 30.", []),

        # --- Issues ---------------------------------------------------------------
        I(90, "narr", "",
          "À 2 h 25, Kevin branche la poche d'amoxicilline-clavulanate au bras de M. Jaquier "
          "et règle le débit. Vous retournez dans la chambre de garde. Vous n'avez pas le "
          "temps de vous allonger.", []),
        I(91, "narr", "",
          "Neuhaus change la prescription : lévofloxacine. À 2 h 35, la perfusion coule. Kevin "
          "revient de la pharmacie du service avec la poche d'amoxicilline-clavulanate qu'il "
          "avait déjà préparée, et la pose sur le comptoir sans un mot.", []),
    ],
)

# ===========================================================================
# Voie ERREUR
# ===========================================================================

# ---------------------------------------------------------------------------
# 5.4 Le choc
# ---------------------------------------------------------------------------
S5_4E = S(4, "5.4 Le choc",
    "2 h 38. Treize minutes après le début de la perfusion. La sonnette du 304. Kevin est "
    "au 318 avec Neuhaus, qui vient de remonter des urgences. Vous êtes le plus près.",
    focus=("er", "ic", "pb", "cc"),
    slot="5.4",
    cond=when(all=["erreur"]),
    debriefs=[
        Debrief(when(all=["deces"]), tone="hard", lead=(
            "M. Jaquier est mort à 3 h 52 d'un choc anaphylactique provoqué par un "
            "antibiotique auquel il était allergique — une allergie que sa femme avait "
            "signalée à 19 h. Ses signes étaient ceux d'un manuel : chaleur, prurit, voix "
            "rauque, lèvres qui gonflent. Face à une anaphylaxie, le premier geste n'est pas "
            "de comprendre : c'est d'arrêter le produit et d'appeler.")),
        Debrief(when(all=["survie"]), tone="mixed", lead=(
            "M. Jaquier est vivant, aux soins intensifs. Il le doit aux minutes qui n'ont pas "
            "été perdues — ou qu'on a rattrapées. Il n'aurait jamais dû recevoir ce "
            "médicament.")),
    ],
    nodes=[
        I(1, "roland", "anxious",
          "M. Jaquier est assis au bord du lit, il se gratte le cou à s'en arracher la peau. "
          "« J'ai chaud… ça gratte partout… » Sa voix est rauque, étranglée. « Ma gorge. » Ses "
          "lèvres ont gonflé. Des plaques rouges montent sur son thorax. La perfusion coule.", [
            R("Fermer la perfusion immédiatement, appuyer sur l'appel d'urgence, crier "
              "« Kevin ! Le 304 ! ».", 2, "pb3 ic3 er2 cc1"),
            R("Courir au 318 chercher Kevin et Neuhaus.", 3, "ic1 er-1 pb-1"),
            R("Appeler Neuhaus sur son téléphone pour lui décrire les symptômes.", 4, "ic1 cc1 pb-1"),
            R("« C'est la fièvre, M. Jaquier. Je vais vous chercher un linge frais. »",
              5, "pb-3 cc-2 er-1 ic-1"),
            R("Crier « À l'aide ! » dans le couloir sans lâcher le patient, puis fermer la perfusion.", 2, "pb2 ic2 er1"),
        ]),
        I(2, "kevin", "anxious",
          "Kevin arrive en courant, Neuhaus sur ses talons. Tension 72/40. Un sifflement aigu "
          "à chaque inspiration. Saturation 84 %. Kevin : « Anaphylaxie ? »", [
            R("« Oui. Perfusion fermée. Adrénaline IM 0,5 mg selon le protocole, appel de "
              "l'équipe de réanimation, jambes surélevées, oxygène au masque. »",
              6, "cc3 ic3 pb2 er1"),
            R("« Je ne sais pas, il fait une réaction bizarre. »", 7, "cc-2 er-1"),
            R("« Neuhaus, qu'est-ce qu'on fait ? »", 7, "cc0 ic1 er-1"),
            R("« Anaphylaxie. Adrénaline maintenant, j'appelle la réa. »", 6, "cc2 ic2 er1"),
            R("« On lui donne un antihistaminique et on attend ? »", 7, "cc-2 pb-2"),
        ]),
        I(3, "narr", "",
          "Le 318 est au bout du couloir. Quarante secondes pour y aller, quarante pour "
          "revenir avec Kevin. Quand vous rentrez dans le 304, la perfusion coule toujours. "
          "Kevin la ferme d'un geste. M. Jaquier siffle en respirant, sa peau est grise. "
          "Tension 65/35. Kevin : « Appelle la réa ! Le chariot ! »", [
            R("Déclencher l'appel de réanimation et amener le chariot d'urgence.", 8, "ic2 er1"),
            R("Rester figé·e au pied du lit.", 9, "er-3 ic-2"),
            R("Allonger le patient jambes surélevées pendant que Kevin prépare l'adrénaline, puis appeler.", 8, "ic2 pb1 er1"),
            R("« Je vais chercher le Dr Neuhaus. »", 9, "ic-2 er-2"),
        ]),
        I(4, "neuhaus", "anxious",
          "Neuhaus décroche à la quatrième sonnerie. Vous décrivez. Il vous coupe : « Il "
          "gonfle ? Ferme la perfusion ! Ferme-la ! Appelle la réa, j'arrive ! » Une minute "
          "a passé. La perfusion coule toujours.", [
            R("Fermer la perfusion et déclencher l'appel de réanimation.", 8, "pb1 ic2"),
            R("« Je fais quoi en premier ? »", 9, "er-3 pb-2"),
            R("Raccrocher, fermer la perfusion, appuyer sur l'alarme, et crier pour Kevin.", 8, "pb2 ic2"),
            R("« Tu es sûr ? Il a juste l'air d'avoir chaud. »", 9, "pb-3 er-2"),
        ]),
        I(5, "narr", "",
          "Vous revenez avec un linge humide. Deux minutes. M. Jaquier ne parle plus. Il fait "
          "un bruit aigu à chaque respiration, ses lèvres ont doublé de volume, sa peau est "
          "grise. La perfusion coule toujours.", [
            R("Fermer la perfusion, déclencher l'appel de réanimation, crier.", 9, "pb1 ic2 er1"),
            R("Courir chercher Kevin.", 9, "ic0 er-2"),
            R("Appuyer sur l'appel d'urgence et fermer la perfusion en même temps.", 9, "pb2 ic2"),
            R("Lui poser le linge sur le front et attendre qu'il se calme.", 9, "pb-3 er-2 cc-1"),
        ]),
        I(6, "imhof", "anxious",
          "2 h 41. L'équipe de réanimation entre avec le chariot. Kevin a injecté "
          "l'adrénaline à 2 h 40. Dre Imhof prend la tête du lit : « Qui a vu le début ? "
          "Quand est-ce que ça a commencé, et avec quoi ? »", [
            R("« Perfusion d'amoxicilline-clavulanate commencée à 2 h 25, symptômes à 2 h 38, "
              "perfusion fermée à 2 h 38, adrénaline IM à 2 h 40. Il est sous "
              "bisoprolol. »", 10, "cc3 ic3"),
            R("« Il y a quelques minutes, je crois. Un antibiotique. »", 10, "cc-1 ic0"),
            R("Tendre la feuille où vous avez noté les heures.", 10, "cc2 ic2"),
            R("« Je ne sais pas, je suis arrivé·e après. »", 10, "cc-3 pb-2"),
        ]),
        I(7, "kevin", "cold-anger",
          "« Une réaction bizarre ? Il est en choc ! » Kevin a déjà la seringue d'adrénaline "
          "dans la main, il la plante dans la cuisse de M. Jaquier à travers le pyjama. "
          "« Appelle la réa, maintenant ! »", [
            R("Déclencher l'appel de réanimation, amener le chariot.", 8, "ic2 er1"),
            R("Rester à côté de Kevin sans rien faire, le temps qu'il finisse.", 8, "ic-2 er-2"),
            R("« Je l'allonge et je mets l'oxygène au masque. »", 8, "ic2 pb1"),
            R("« Tu es sûr qu'on peut lui faire de l'adrénaline sans médecin ? »", 8, "ic-2 er-1"),
        ]),
        I(8, "imhof", "anxious",
          "2 h 44. L'équipe de réanimation arrive. La tension ne remonte pas malgré "
          "l'adrénaline. Dre Imhof : « Sous bêtabloquant ? Glucagon. Préparez l'intubation, "
          "ça va être difficile. » Puis, sans vous regarder : « Qui a vu le début ? "
          "Quand ? »", [
            R("« Perfusion commencée à 2 h 25, symptômes à 2 h 38, fermée à 2 h 39 ou 2 h 40. "
              "Il est sous bisoprolol. »", 11, "cc3 ic2"),
            R("« Je ne sais plus exactement. »", 11, "cc-2 er-1"),
            R("« Je vous écris la chronologie, vous l'avez dans une minute. »", 11, "cc2 ic1"),
            R("« C'est l'infirmier qui a branché, demandez-lui. »", 11, "ic-3 pb-2"),
        ]),
        I(9, "narr", "",
          "Quand l'équipe de réanimation arrive, à 2 h 47, M. Jaquier ne respire plus. Dre "
          "Imhof commence le massage cardiaque. Quelqu'un vous met une feuille dans les "
          "mains : « Tu notes les heures. Tout. »", [
            R("Noter les heures, les doses, les gestes, sans lever les yeux.", 12, "ic2 er2 cc1"),
            R("Sortir de la chambre. Vous n'y arrivez pas.", 12, "er-2 ic-1"),
            R("Prendre le relais du massage quand on vous le demande.", 12, "ic2 er1"),
            R("Filmer avec votre téléphone, pour pouvoir expliquer après.", 12, "pb-3 rd-3"),
        ]),
        I(10, "narr", "",
          "Intubé à 2 h 52 malgré l'œdème, sous adrénaline en continu et glucagon, M. Jaquier "
          "est transféré aux soins intensifs à 3 h 30. Vivant. Dre Imhof retire ses gants : "
          "« Sans la perfusion fermée tout de suite et l'adrénaline dans les deux minutes, on "
          "n'en parlerait pas au présent. » Puis elle regarde la poche vide sur la potence, et "
          "ne dit plus rien.", [
            R("Continuer.", END, sets=["survie"], scores=""),
        ]),
        I(11, "narr", "",
          "À 2 h 50, son cœur s'arrête. Neuf minutes de massage, trois injections "
          "d'adrénaline. À 2 h 59, le pouls revient. À 3 h 40, M. Jaquier part aux soins "
          "intensifs, intubé, les pupilles encore lentes. Vivant — pour l'instant. Dre Imhof "
          "retire ses gants sans un mot.", [
            R("Continuer.", END, sets=["survie"], scores=""),
        ]),
        I(12, "narr", "",
          "Quarante-cinq minutes de réanimation. À 3 h 52, Dre Imhof regarde l'horloge et dit "
          "l'heure à voix haute. Kevin retire la poche vide de la potence. Personne ne "
          "parle.", [
            R("Continuer.", END, sets=["deces"], scores=""),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.5 Quatre heures
# ---------------------------------------------------------------------------
S5_5E = S(5, "5.5 Quatre heures",
    "4 h 15. Dr Moreau est arrivé·e, appelé·e par Neuhaus. L'hôpital a téléphoné à Mme "
    "Jaquier pour lui dire que son mari allait mal. Elle est en bas, avec un taxi qui "
    "attend. Son fils Olivier est en route. Moreau vous attend devant le petit salon des "
    "familles.",
    focus=("rd", "co", "pb", "er"),
    slot="5.5",
    cond=when(all=["erreur"]),
    entries=[
        Entry(2, when(all=["deces"]),
              "4 h 15. Dr Moreau est arrivé·e, appelé·e par Neuhaus. L'hôpital a téléphoné à "
              "Mme Jaquier pour lui dire que son mari allait mal. Elle ne sait pas encore "
              "qu'il est mort. Son fils Olivier est en route. Moreau vous attend devant le "
              "petit salon des familles."),
    ],
    debriefs=[
        Debrief(when(all=["esquive"]), tone="hard", lead=(
            "Cette nuit, Mme Jaquier a entendu une esquive avant d'entendre la vérité. Elle "
            "l'a entendue de la bouche de quelqu'un qui savait. Elle s'en souviendra — le "
            "jour où elle choisira un avocat, et le jour où elle décidera de le croire ou "
            "non.")),
        Debrief(when(all=["aveu"]), tone="mixed", lead=(
            "Mme Jaquier a entendu la vérité la nuit même : l'allergie était connue, "
            "l'information s'est perdue, c'est une erreur. Ça ne répare rien. Mais c'est ce "
            "qui rend la suite possible.")),
    ],
    nodes=[
        I(1, "moreau", "neutral",
          "Dr Moreau a le visage fermé, la voix calme. « Je vais lui parler. Vous venez. Vous "
          "ne dites rien que vous ne sachiez, et vous ne mentez pas. » Un temps. « Qu'est-ce "
          "qu'on sait, exactement ? »", [
            R("« Qu'il a reçu de l'amoxicilline-clavulanate à 2 h 25, qu'il a fait un choc "
              "anaphylactique, que son allergie n'était pas dans le dossier — et que sa femme "
              "l'avait signalée hier soir. »", 3, "cc3 pb3 er1"),
            R("« Qu'il a fait une réaction grave à l'antibiotique. »", 3, "cc1"),
            R("« Qu'on ne pouvait pas savoir : le dossier disait « aucune allergie ». »",
              5, "pb-3 cc-2"),
            R("« Qu'il a reçu une pénicilline malgré une allergie. Le reste, je ne le sais pas encore. »", 3, "cc2 pb2"),
            R("« Qu'il a fait un malaise pendant la nuit. »", 5, "pb-3 cc-3"),
        ]),
        I(2, "moreau", "neutral",
          "Dr Moreau a le visage fermé, la voix calme. « Elle ne sait pas qu'il est mort. Je "
          "vais le lui dire. Vous venez. Vous ne dites rien que vous ne sachiez, et vous ne "
          "mentez pas. » Un temps. « Qu'est-ce qu'on sait, exactement ? »", [
            R("« Qu'il a reçu de l'amoxicilline-clavulanate à 2 h 25, qu'il a fait un choc "
              "anaphylactique, que son allergie n'était pas dans le dossier — et que sa femme "
              "l'avait signalée hier soir. »", 4, "cc3 pb3 er1"),
            R("« Qu'il a fait une réaction grave à l'antibiotique. »", 4, "cc1"),
            R("« Qu'on ne pouvait pas savoir : le dossier disait « aucune allergie ». »",
              15, "pb-3 cc-2"),
            R("« Qu'il a reçu une pénicilline malgré une allergie. Le reste, je ne le sais pas encore. »", 4, "cc2 pb2"),
            R("« Qu'il a fait un malaise pendant la nuit. »", 15, "pb-3 cc-3"),
        ]),
        I(3, "monique", "anxious",
          "Petit salon. Mme Jaquier a gardé son manteau. Dr Moreau s'assoit en face d'elle. "
          "« Votre mari a fait une réaction allergique très grave à un antibiotique, cette "
          "nuit. Il est aux soins intensifs, intubé. Son état est critique. » Mme Jaquier ne "
          "bouge pas. « Un antibiotique ? » Elle vous regarde. « Lequel ? »", [
            R("« De l'amoxicilline. C'est une pénicilline. »", 6, "cc3 pb2"),
            R("« Un antibiotique habituel pour les pneumonies. »", 7, "cc-2 pb-2"),
            R("« Une pénicilline. Et nous devons vous dire pourquoi c'est grave. »", 6, "cc3 pb2"),
            R("« Je ne peux pas vous le dire pour l'instant. »", 7, "cc-2 pb-2"),
        ]),
        I(4, "monique", "sad",
          "Petit salon. Mme Jaquier a gardé son manteau. Dr Moreau s'assoit en face d'elle. "
          "« Madame Jaquier, votre mari a fait une réaction allergique très grave cette nuit. "
          "Son cœur s'est arrêté. On a essayé pendant quarante-cinq minutes. Il est mort à "
          "3 h 52. » Un long silence. Puis, à vous, parce que vous étiez là à 19 h : « Est-ce "
          "qu'il a souffert ? »", [
            R("« Il a eu peur au début, et du mal à respirer. Ensuite il a perdu connaissance, "
              "très vite, et nous pensons qu'il n'a plus rien senti. »", 17, "cc3 co2 rd1"),
            R("« Non, pas du tout. »", 17, "cc-2 pb-1"),
            R("« Je ne sais pas. »", 17, "cc-1 co-1"),
            R("S'asseoir près d'elle : « J'étais là. Il n'était pas seul. »", 17, "co3 rd1"),
            R("« Il est mort très vite, c'est une bonne chose. »", 17, "co-3 cc-1"),
        ]),
        I(5, "moreau", "cold-anger",
          "Dr Moreau s'arrête, la main sur la poignée. « « On ne pouvait pas savoir. » Vous en "
          "êtes sûr·e ? Vous allez répéter ça devant elle ? »", [
            R("« Non. Elle a signalé une allergie hier soir. Elle n'a pas été écrite, ou pas "
              "transmise. »", 3, "pb3 er2"),
            R("« C'est ce que dit le dossier. »", 3, "pb-2"),
            R("« Non. Pardon. Je dirai ce que je sais, pas ce qui m'arrange. »", 3, "pb3 er1"),
            R("« Ce n'est pas faux. »", 3, "pb-3 er-1"),
        ]),
        I(6, "monique", "angry",
          "« De la pénicilline ? » Elle se lève. « Je l'avais dit ! Je l'ai dit hier soir, en "
          "arrivant ! Pourquoi personne ne m'a écoutée ? » Elle vous regarde, vous.", [
            R("« Vous l'aviez dit. Et l'information n'est pas arrivée jusqu'à la personne qui a "
              "prescrit. C'est une erreur de notre part. Je suis désolé·e. »", 8,
              sets=["aveu"], scores="pb3 rd3 cc2 co1"),
            R("« Madame, nous allons analyser ce qui s'est passé. »", 9, "cc0 pb0"),
            R("« Le dossier des urgences disait « aucune allergie ». »", 10,
              sets=["esquive"], scores="pb-3 rd-2 cc-2"),
            R("Se taire, et regarder Dr Moreau.", 9, "er-1 pb-1"),
            R("« C'est vrai, vous l'aviez dit. Je suis désolé·e. Je ne vous demande pas de comprendre. »", 8, "pb2 rd2 co1", sets=["aveu"]),
        ]),
        I(7, "monique", "suspicious",
          "« Habituel. » Elle vous fixe. « Mais lequel ? » Dr Moreau ne vient pas à votre "
          "secours. « Alex. »", [
            R("« De l'amoxicilline. Une pénicilline. »", 6, "cc2 pb2"),
            R("« Je ne sais pas exactement. »", 10, sets=["esquive"], scores="pb-3 cc-3 rd-1"),
            R("« Pardon. Une pénicilline. »", 6, "cc2 pb1"),
            R("« Ce n'est pas le plus important, maintenant. »", 10, "pb-3 rd-2", sets=["esquive"]),
        ]),
        I(8, "monique", "sad",
          "Elle se rassoit d'un coup, comme si ses jambes lâchaient. « Quarante-six ans. » "
          "Elle serre son sac. « Il ne voulait pas venir. C'est moi qui l'ai forcé. »", [
            R("« Vous avez bien fait de l'amener : il avait une pneumonie. Ce qui est arrivé "
              "ne vient pas de vous. »", 11, "co3 em2 rd1"),
            R("S'asseoir près d'elle, en silence.", 11, "co2 er1"),
            R("« Il ne faut pas penser comme ça. »", 11, "em-2 co-1"),
            R("Lui tendre la main, sans parler.", 11, "co3"),
            R("« C'est vrai, s'il était resté chez lui… »", 11, "co-3 em-2 rd-1"),
        ]),
        I(9, "monique", "cold-anger",
          "« Analyser ? » Sa voix monte. « Je vous demande ce qu'on lui a donné ! » Dr Moreau "
          "se penche : « Madame Jaquier, il a reçu une pénicilline, alors que vous nous aviez "
          "signalé son allergie. C'est une erreur. Nous vous devons la vérité et des "
          "excuses. » Puis Moreau vous regarde.", [
            R("« Je suis désolé·e. C'est moi qui ai fait son entrée, hier soir. »", 8,
              sets=["aveu"], scores="pb3 rd2 er1 co1"),
            R("« Oui. »", 8, "pb0 cc0"),
            R("« C'est vrai. C'est moi qui ai fait son entrée, et je ne suis pas allé·e au bout de la question. »", 8, "pb3 rd2", sets=["aveu"]),
            R("« Je ne peux rien dire de plus. »", 8, "pb-2 em-1"),
        ]),
        I(10, "moreau", "cold-anger",
          "Dr Moreau intervient, sans hausser la voix. « Ce n'est pas exact. Madame, vous nous "
          "aviez signalé son allergie, et l'information n'a pas été transmise. C'est une "
          "erreur de notre part. » Mme Jaquier ne regarde plus Moreau. Elle vous regarde, "
          "vous.", [
            R("« Dr Moreau a raison. Je suis désolé·e. »", 8, "pb2 rd1"),
            R("Baisser les yeux.", 8, "pb-1 er-1"),
            R("« Madame, je me suis réfugié·e derrière le dossier. C'était lâche. Pardon. »", 8, "pb3 er1 rd1"),
            R("« C'est pourtant ce qui était écrit. »", 8, "pb-3 er-1"),
        ]),
        I(11, "olivier", "angry",
          "4 h 40. La porte s'ouvre sur un homme de quarante ans en veste de pluie, les "
          "cheveux mouillés. « Maman ? » Il voit son visage, puis vous. « Qu'est-ce qui s'est "
          "passé ? Qui était là ? » Il lit votre badge. « C'est qui, le responsable ? »", [
            R("« J'étais là. C'est moi qui ai fait l'entrée de votre père hier soir. Dr Moreau "
              "va vous expliquer tout ce que nous savons. »", 12, "pb3 er2 cc1"),
            R("« Je ne suis qu'étudiant·e. Voyez avec le Dr Moreau. »", 13, "pb-2 er-1"),
            R("« C'est l'infirmier qui a posé la perfusion. »", 14,
              sets=["esquive"], scores="ic-3 pb-3 rd-1"),
            R("« J'ai fait l'entrée de votre père. Je reste là, et je répondrai à vos questions. »", 12, "pb2 er2"),
            R("« Il faudrait voir avec l'hôpital, pas avec moi. »", 13, "pb-2 er-1 ic-1"),
        ]),
        I(12, "olivier", "cold-anger",
          "« Un·e étudiant·e. » Il répète le mot, lentement. « Mon père a été admis par un·e "
          "étudiant·e. » Il pose la main sur l'épaule de sa mère. « Vous allez entendre parler "
          "de nous. »", [
            R("« Je comprends votre colère. Vous avez le droit de tout savoir, et vous le "
              "saurez. »", 16, "er3 pb2 rd1"),
            R("« J'étais supervisé·e, c'est la règle. »", 16, "er-1 pb-1"),
            R("Se taire.", 16, "er1"),
            R("« Oui. Et vous saurez tout. »", 16, "pb2 er1"),
        ]),
        I(13, "olivier", "angry",
          "« Voir avec le chef. » Il a un rire sans joie. « Évidemment. Personne n'est jamais "
          "là quand ça compte. »", [
            R("« Vous avez raison. J'étais là. Je reste. »", 16, "pb2 er1"),
            R("Sortir.", 16, "er-1 co-1"),
            R("Revenir s'asseoir à côté de sa mère.", 16, "co2 pb1"),
            R("« Je n'ai pas à me justifier auprès de vous. »", 16, "er-3 rd-2"),
        ]),
        I(14, "moreau", "cold-anger",
          "« Alex. Dehors. » Dans le couloir, Dr Moreau parle très bas. « Vous venez de "
          "désigner un collègue à une famille en deuil, avant toute analyse. Kevin a exécuté "
          "une prescription avec les informations qu'on lui a données. »", [
            R("« Vous avez raison. C'était lâche. »", 16, "pb2 er1 ic2"),
            R("« C'est pourtant ce qui s'est passé. »", 16, "ic-2 pb-1"),
            R("« Je vais leur dire que je me suis trompé·e. »", 16, "pb2 ic2"),
            R("« Kevin aurait dû vérifier. »", 16, "ic-3 pb-2"),
        ]),
        I(15, "moreau", "cold-anger",
          "Dr Moreau s'arrête, la main sur la poignée. « « On ne pouvait pas savoir. » Vous en "
          "êtes sûr·e ? Vous allez répéter ça devant une femme dont le mari vient de "
          "mourir ? »", [
            R("« Non. Elle a signalé une allergie hier soir. Elle n'a pas été écrite, ou pas "
              "transmise. »", 4, "pb3 er2"),
            R("« C'est ce que dit le dossier. »", 4, "pb-2"),
            R("« Non. Pardon. Je dirai ce que je sais, pas ce qui m'arrange. »", 4, "pb3 er1"),
            R("« Ce n'est pas faux. »", 4, "pb-3 er-1"),
        ]),
        I(16, "moreau", "neutral",
          "5 h 10. Mme Jaquier veut voir son mari. Dr Moreau l'accompagne. Avant de partir, "
          "Moreau se retourne. « Vous, vous allez écrire ce qui s'est passé, heure par heure, "
          "pendant que c'est frais. Les faits. Rien que les faits. »", [
            R("« D'accord. »", END, "pb2 cc1"),
            R("« Je peux l'accompagner ? »", END, "co2 pb-1"),
            R("« Je ne suis pas sûr·e de pouvoir écrire maintenant. »", END, "er1"),
            R("« Qu'est-ce que je dois écrire, exactement ? Je ne veux pas me mettre en "
              "difficulté. »", END, "pb-2 cc-1"),
            R("« Je vais d'abord voir Kevin. Il est seul dans la salle de repos. »", -1, "ic2 em1"),
        ]),
        I(17, "monique", "sad",
          "Elle hoche la tête, lentement. Elle regarde ses mains. Puis, d'une voix blanche : "
          "« Qu'est-ce qu'il a eu ? Une réaction à quoi ? Lequel, de vos médicaments ? »", [
            R("« De l'amoxicilline. C'est une pénicilline. »", 6, "cc3 pb2"),
            R("« Un antibiotique habituel pour les pneumonies. »", 7, "cc-2 pb-2"),
            R("« Une pénicilline. Je vais vous dire pourquoi c'est si grave. »", 6, "cc3 pb2"),
            R("« On ne sait pas encore. »", 7, "pb-3 cc-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.6 La ligne
# ---------------------------------------------------------------------------
S5_6E = S(6, "5.6 La ligne",
    "7 h. La relève de jour arrive. M. Jaquier est aux soins intensifs depuis trois "
    "heures. Dans la salle de repos : Neuhaus, Kevin, et vous. Personne n'a dormi. "
    "L'ordinateur est ouvert sur le dossier du 304.",
    focus=("pb", "er", "ic"),
    slot="5.6",
    cond=when(all=["erreur"]),
    entries=[
        Entry(1, when(all=["deces"]),
              "7 h. La relève de jour arrive. M. Jaquier est mort il y a trois heures. Dans la "
              "salle de repos : Neuhaus, Kevin, et vous. Personne n'a dormi. L'ordinateur est "
              "ouvert sur le dossier du 304."),
    ],
    debriefs=[
        Debrief(when(all=["dossier_modifie"]), tone="hard", lead=(
            "À 6 h 47, vous avez réécrit une ligne du dossier. Le système a gardé "
            "l'ancienne version, l'heure et votre identifiant. Dans quelques jours, quelqu'un "
            "d'autre le lira — et ce ne sera plus seulement l'histoire d'une information "
            "perdue.")),
    ],
    nodes=[
        I(1, "neuhaus", "anxious",
          "Neuhaus a les yeux rouges. « Écoute. Il va y avoir une analyse. Il faut qu'on soit "
          "cohérents. » Il tourne l'écran vers vous : votre entrée de 19 h 40. « Allergies : "
          "aucune connue. » « Tu as écrit quoi, exactement ? »", [
            R("« « Aucune allergie connue. » C'est ce qui est écrit, et ça restera écrit. "
              "J'ajoute une note datée de maintenant, avec ce que je sais et comment je l'ai "
              "su. »", 3, "pb3 cc3 er2"),
            R("« Je peux corriger la ligne. Le système le permet. »", 2, "pb-3 cc-2"),
            R("« Qu'est-ce que tu veux que je dise ? »", 4, "pb-1 er-1"),
            R("« Je ne change rien. Je dirai à l'analyse ce que j'ai demandé, et ce que je n'ai pas demandé. »", 3, "pb3 er2"),
            R("« On pourrait écrire qu'on n'a pas eu le temps de faire l'anamnèse complète. »", 4, "pb-3 cc-2"),
        ]),
        I(2, "neuhaus", "neutral",
          "Neuhaus hésite. « Le système garde l'historique, tu sais. » Il ne vous arrête pas "
          "pour autant. Kevin, qui n'a rien dit depuis une heure, lève la tête : « Ne fais "
          "pas ça. »", [
            R("« Tu as raison, Kevin. Je ne touche à rien. J'ajoute une note datée. »",
              3, "pb3 er1 ic1"),
            R("Modifier la ligne : « Allergie pénicilline signalée par l'épouse, à "
              "vérifier ». Enregistrer.", 5, sets=["dossier_modifie"], scores="pb-3 cc-3 rd-1"),
            R("Fermer le dossier. « Non. On ne touche pas à ce qui est écrit. »", 3, "pb3 er2"),
            R("Ajouter une ligne à 19 h 40, comme si elle avait toujours été là : « pénicilline ? ».", 5, "pb-3 cc-3 rd-1", sets=["dossier_modifie"]),
        ]),
        I(3, "kevin", "sad",
          "Kevin fixe ses mains. « Moi, j'ai branché la poche. » Sa voix est très calme. « J'ai "
          "demandé s'il avait des allergies. On m'a dit non. J'ai branché. »", [
            R("« Tu as fait ce qu'on t'a dit, avec les informations qu'on t'a données. Ce qui "
              "a manqué est arrivé avant toi. »", 6, "ic3 em2 co1"),
            R("« Ce n'est la faute de personne. »", 6, "cc-1 pb-1"),
            R("Se taire.", 6, "er0 ic-1"),
            R("S'asseoir à côté de lui, sans rien dire.", 6, "em2 co1 ic1"),
            R("« Tu aurais pu vérifier le bracelet. »", 6, "ic-3 pb-1 rd-1"),
        ]),
        I(4, "neuhaus", "anxious",
          "« Je veux dire : l'allergie n'était pas dans le dossier. Donc techniquement, "
          "personne ne pouvait savoir. » Il se frotte le visage. « C'est ça qu'on dit. »", [
            R("« Non. Sa femme l'avait dite. Je ne dirai pas qu'on ne pouvait pas savoir. »",
              3, "pb3 er2"),
            R("« OK. Personne ne pouvait savoir. »", 7, "pb-3 ic-1"),
            R("« On dit ce qui s'est passé, Samuel. Toi, moi, Kevin. Chacun sa part. »", 3, "pb3 ic2"),
            R("« D'accord, mais toi tu diras que tu n'as pas relu. »", 7, "pb-2 ic-2"),
        ]),
        I(5, "narr", "",
          "Vous enregistrez. En bas de l'écran, en petits caractères gris : « Modifié par "
          "[votre identifiant] — 06:47 ». Kevin se lève et sort sans un mot.", [
            R("Continuer.", 6, ""),
        ]),
        I(6, "ines", "neutral",
          "Inès Rey arrive pour la relève de jour. Elle sait déjà. « Moreau m'a appelée. » "
          "Elle vous regarde longuement. « Vous avez fait la déclaration d'incident ? Si vous "
          "ne savez pas comment, je vous montre. »", [
            R("« Je veux la faire moi-même, maintenant, avec vous. Les faits, dans "
              "l'ordre. »", 8, "pb3 ic3 cc1"),
            R("« Je ne sais pas si c'est à moi de la faire. »", 8, "pb-1 ic-1"),
            R("« À quoi ça sert, maintenant ? »", 9, "pb-2 er-1"),
            R("« Oui. Et je veux y citer Fatou comme source, avec son accord. »", 8, "ic2 pb1 rd1"),
            R("« Je préfère attendre de savoir ce que je risque. »", 9, "pb-2 er-1"),
        ]),
        I(7, "kevin", "cold-anger",
          "Kevin se lève. « Personne ne pouvait savoir ? » Il enfile son blouson. « Sa femme "
          "l'a dit à Fatou en partant. Fatou me l'a dit ce matin, en arrivant pour le "
          "petit-déjeuner. » Il s'arrête à la porte. « Moi, je vais le dire. »", [
            R("« Kevin, attends. Tu as raison. On le dit ensemble. »", 6, "pb2 ic2"),
            R("Le laisser partir.", 6, "ic-2"),
            R("« Attends, Kevin. Tu as raison, et je viens avec toi. »", 6, "pb2 ic2 er1"),
            R("« Si tu fais ça, tu vas tous nous couler. »", 6, "pb-3 ic-3"),
        ]),
        I(8, "fatou", "sad",
          "7 h 15. Fatou entre, en blouse, les yeux gonflés. « C'est le monsieur du 304 ? » "
          "Elle s'assoit sans qu'on l'y invite. « La dame me l'avait dit. En partant. J'aurais "
          "dû le dire plus fort. »", [
            R("« Ce n'était pas à vous de crier, Fatou. C'était à nous d'écouter. »",
              10, "ic3 em2 co2 rd2"),
            R("« Il faudra le dire à l'analyse. »", 10, "ic1"),
            R("« Oui, il aurait fallu. »", 10, "ic-2 em-2"),
            R("Poser une main sur son épaule. « Merci d'être venue ce matin. »", 10, "co2 ic1"),
        ]),
        I(9, "ines", "cold-anger",
          "« À quoi ça sert ? » Inès ferme la porte. « À ce que la prochaine fois, ce soit "
          "écrit avant. À ça que ça sert. »", [
            R("« D'accord. On la fait. »", 8, "pb2 ic1"),
            R("« Faites-la, vous. »", 8, "pb-2 ic-1"),
            R("« Vous avez raison. Montrez-moi comment on la remplit. »", 8, "ic2 pb2"),
            R("« Ça ne ramènera personne. »", 8, "pb-2 er-2"),
        ]),
        I(10, "moreau", "neutral",
          "7 h 40. Dr Moreau entre. « Alex. Vous rentrez chez vous. Maintenant. » Un temps. "
          "« Vous ne conduisez pas, vous ne restez pas seul·e ce matin. Qui peut être avec "
          "vous ? »", [
            R("« Mon/ma colocataire. Je l'appelle. »", 11, "er3 ic1"),
            R("« Personne. Ça ira. »", 12, "er-2"),
            R("« Je préfère rester, je veux savoir ce qui se passe. »", 12, "er-2 pb-1"),
            R("« Ma sœur habite à côté. Je l'appelle maintenant, devant vous. »", 11, "er3 ic1"),
            R("« Je peux dormir ici, dans la chambre de garde ? »", 12, "er-1"),
        ]),
        I(11, "moreau", "neutral",
          "« Bien. Demain à 11 h, vous venez me voir. Pas pour une sanction : pour parler. » "
          "Moreau pose la main sur votre épaule, brièvement. « Il y aura une analyse, une "
          "rencontre avec la famille, peut-être pire. Vous ne serez pas seul·e. »", [
            R("« Est-ce que je suis responsable ? »", 13, "er1 pb1"),
            R("« Merci. »", END, "er1"),
            R("« Et Kevin ? Quelqu'un s'occupe de lui ? »", -1, "ic2 em2"),
            R("« Je peux aller voir Mme Jaquier avant de partir ? »", -1, "co2 pb-1"),
        ]),
        I(12, "moreau", "cold-anger",
          "« Ce n'était pas une proposition. » La voix est douce et ne se discute pas. « Qui "
          "puis-je appeler pour vous ? »", [
            R("Donner un nom et un numéro.", 11, "er1 ic1"),
            R("« Mon/ma colocataire. Je l'appelle maintenant. »", 11, "er2 ic1"),
            R("« Je vous dis que ça ira. »", 11, "er-2"),
            R("« Je rentre à pied, ça me fera du bien. »", 11, "er-2 pb-1"),
        ]),
        I(13, "moreau", "neutral",
          "Dr Moreau prend le temps de répondre. « Vous faites partie de ce qui s'est passé. "
          "Pas tout. L'analyse dira quoi. » Un temps. « En attendant, ce qui dépend de vous, "
          "c'est la vérité. Le reste, on le portera ensemble. »", [
            R("« D'accord. »", END, "er1"),
            R("« Merci de ne pas me mentir. »", -1, "er1 rd1"),
            R("« Donc c'est ma faute. »", -1, "er-2"),
            R("« Est-ce que je peux écrire à Mme Jaquier ? »", -1, "co2 pb-1"),
        ]),
    ],
)

# ===========================================================================
# Voie ÉVITÉE
# ===========================================================================

# ---------------------------------------------------------------------------
# 5.4 La poche
# ---------------------------------------------------------------------------
S5_4N = S(7, "5.4 La poche",
    "2 h 45. La lévofloxacine coule au 304. Salle de soins : Kevin se lave les mains "
    "longtemps, plus longtemps que nécessaire. Sur le comptoir, une poche "
    "d'amoxicilline-clavulanate, déjà montée sur sa tubulure.",
    focus=("ic", "er", "rd", "pb"),
    slot="5.4",
    cond=when(all=["evite"]),
    entries=[
        Entry(2, when(all=["allergie_dossier"]),
              "2 h 45. La lévofloxacine coule au 304. Salle de soins : Kevin remplit sa "
              "feuille de surveillance. Sur l'écran, la pastille rouge du dossier Jaquier : "
              "« Allergie grave — pénicilline »."),
    ],
    nodes=[
        I(1, "kevin", "anxious",
          "Kevin s'essuie les mains et montre la poche du menton. « Tu sais que je l'avais "
          "déjà montée ? Dix minutes de plus, et je la branchais. » Il la jette dans le bac "
          "des médicaments à retourner. « Dix minutes. »", [
            R("« Moi aussi, j'ai failli ne pas vérifier. On a eu de la chance, et je ne veux "
              "pas qu'on compte sur la chance. »", 3, "er2 ic2 pb1"),
            R("« Heureusement que j'étais là, hein. »", 4, "ic-2 er-1"),
            R("« Bah, il ne s'est rien passé. »", 3, "pb-2 er-1"),
            R("« Dix minutes. On va écrire ce qui s'est passé. »", 3, "pb2 ic1"),
            R("Rire nerveusement. « Imagine la tête de Neuhaus. »", 3, "er-2 rd-1"),
        ]),
        I(2, "kevin", "neutral",
          "« L'alerte a sauté quand Neuhaus a prescrit. » Kevin tapote l'écran. « Tu sais "
          "combien de fois j'ai vu une allergie arriver dans le dossier le soir même de "
          "l'entrée ? Presque jamais. D'habitude, on la découvre le lendemain, par la "
          "famille. »", [
            R("« C'est sa femme qui l'a dite. Je n'ai fait que l'écrire. »", 3, "ic3 rd1"),
            R("« C'est mon travail. »", 3, "ic0 pb1"),
            R("« Les urgences auraient dû la voir. »", 3, "ic-2"),
            R("« Et Fatou, qui l'avait entendue aussi. »", 3, "ic3 rd1"),
        ]),
        I(3, "kevin", "neutral",
          "La sonnette du 304. M. Jaquier tire sur ses lunettes à oxygène et essaie de se "
          "lever, désorienté. « Où est Monique ? Je veux rentrer. » Kevin le retient. « Il "
          "arrache tout. Il va désaturer. On l'attache ? »", [
            R("« Non. On reste avec lui, on lui explique, et j'appelle sa femme pour qu'elle "
              "lui parle au téléphone. »", 5, "rd3 co2 ic1"),
            R("« Oui, sinon il va désaturer. »", 6, "rd-3 pb-2"),
            R("« Fais comme tu veux. »", 6, "ic-2 rd-1"),
            R("« Je reste avec lui dix minutes. Monsieur Jaquier, vous êtes à l'hôpital, on s'occupe de vous. »", 5, "rd3 co2"),
            R("« Donne-lui quelque chose pour dormir. »", 6, "rd-2 pb-2"),
        ]),
        I(4, "kevin", "cold-anger",
          "Kevin se retourne. « Grâce à toi ? » Il parle calmement. « Neuhaus a prescrit sans "
          "demander. J'ai monté la poche. Et toi, tu as failli dire « aucune ». On a tous "
          "failli, Alex. Tous. »", [
            R("« Tu as raison. Moi compris. »", 3, "er2 ic2"),
            R("« Je dis juste que j'ai vérifié. »", 3, "ic-1 er-1"),
            R("Se taire, et hocher la tête.", 3, "er1 ic1"),
            R("« Au moins, moi, je n'ai rien branché. »", 3, "ic-3 er-2"),
        ]),
        I(5, "monique", "anxious",
          "Mme Jaquier décroche à la première sonnerie. Vous tendez le téléphone à son mari : "
          "« Roland ? C'est moi. Tu es à l'hôpital, tu te souviens ? » Il se calme, les yeux "
          "fermés. Puis elle vous demande : « Et pour la pénicilline… c'est bien noté, "
          "maintenant ? »", [
            R("« Oui. Et je vous dois une information : cette nuit, une pénicilline avait été "
              "préparée pour lui. On l'a arrêtée avant qu'elle soit donnée, grâce à ce que "
              "vous aviez dit. »", 7, sets=["quasi_dit"], scores="rd2 cc2 pb2"),
            R("« Oui. C'est dans le dossier, avec la description, et il a un bracelet. »",
              7, "cc2 rd1"),
            R("« Oui, oui. Ne vous inquiétez pas. »", 7, "cc-1 em-1 pb-1"),
            R("« C'est noté. Et je voudrais vous raconter la nuit en détail demain, quand vous viendrez. »", 7, "cc2 pb1 rd1"),
            R("« Il n'y a jamais eu de problème, madame. »", 7, "pb-3 cc-3"),
        ]),
        I(6, "narr", "",
          "Kevin attache le poignet droit de M. Jaquier au montant du lit. Il se débat, puis "
          "s'épuise. À 3 h 20, la saturation descend à 85 % : il a arraché ses lunettes de la "
          "main gauche. Il pleure sans bruit.", [
            R("Détacher son poignet, rester avec lui, appeler sa femme.", 5, "rd2 co2"),
            R("Remettre les lunettes et retourner à la chambre de garde.", 8, "rd-1 co-1"),
            R("Détacher le poignet, remettre les lunettes, et rester assis·e à côté de lui.", 5, "rd2 co2"),
            R("Laisser la contention, c'est plus sûr.", 8, "rd-3 co-2"),
        ]),
        I(7, "neuhaus", "neutral",
          "3 h 30. Neuhaus remonte des urgences, un café à la main, les yeux rouges. Il vous "
          "prend à part. « Bon. On n'en parle pas, OK ? Il ne s'est rien passé. Pas besoin de "
          "déclaration, ça va juste me retomber dessus. »", [
            R("« Je comprends que tu sois épuisé. Mais c'est justement parce qu'il ne s'est "
              "rien passé qu'il faut le déclarer : la prochaine fois, il n'y aura peut-être "
              "personne pour vérifier. »", 9, "pb3 ic2 cc2"),
            R("« OK, pas de souci. »", 10, "pb-3 ic-1"),
            R("« Je ne sais pas. »", 10, "pb-1 er-1"),
            R("« On en parle demain, reposés. Mais je ne vais pas faire comme si rien ne s'était passé. »", 9, "pb2 er2"),
            R("« Tu me dois un café, alors. »", 10, "pb-3 er-1"),
        ]),
        I(8, "narr", "",
          "Chambre de garde. Vous ne dormez pas. Vous repensez à la poche sur le comptoir, à "
          "la main de Kevin, aux dix minutes. À 3 h 30, on frappe : Neuhaus.", [
            R("Ouvrir.", 7, ""),
        ]),
        I(9, "neuhaus", "cold-anger",
          "« Tu vas me balancer ? » Il pose son café. « Moi, qui ai fait trois gardes cette "
          "semaine pour que vous ayez une supervision ? »", [
            R("« Ce n'est pas une dénonciation. C'est anonyme, et c'est fait pour ça. Si tu "
              "veux, on l'écrit ensemble demain matin. »", END, "pb2 ic3 er2"),
            R("« Laisse tomber, on n'en parle plus. »", END, "pb-3 ic-1"),
            R("« Je ne te balance pas. Je veux que ça n'arrive pas au prochain assistant épuisé. »", -1, "pb2 ic2 em1"),
            R("« Tu as eu de la chance que je sois là. »", -1, "ic-3 er-2"),
        ]),
        I(10, "kevin", "neutral",
          "Kevin, qui passait avec un chariot, s'arrête. Il a entendu. « Moi, je déclare. » Il "
          "regarde Neuhaus, puis vous. « C'était ma poche. »", [
            R("« Tu as raison. Je le fais avec toi. »", END, "pb2 ic2"),
            R("« Fais comme tu veux. »", END, "ic-1 pb-1"),
            R("« Je témoigne avec toi. C'est ma part aussi. »", -1, "pb2 ic2"),
            R("« Tu vas te griller pour rien. »", -1, "pb-3 ic-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.5 Sept heures
# ---------------------------------------------------------------------------
S5_5N = S(8, "5.5 Sept heures",
    "7 h. Relève de jour. Inès Rey arrive, Neuhaus termine sa garde, Kevin rend sa nuit. "
    "Vous n'avez pas dormi. M. Jaquier va mieux : 37,9 °C, saturation 94 %.",
    focus=("pb", "ic", "er"),
    slot="5.5",
    cond=when(all=["evite"]),
    nodes=[
        I(1, "ines", "neutral",
          "Kevin raconte la poche à Inès, en trois phrases. Inès pose son café. « Une "
          "pénicilline préparée pour un patient allergique. Et c'est déclaré ? » Neuhaus "
          "regarde ailleurs. Inès vous regarde, vous.", [
            R("« Pas encore. Je veux le faire maintenant, avec Kevin. »", 3,
              sets=["cirs_declare"], scores="pb3 ic2"),
            R("« Il ne s'est rien passé, finalement. »", 2, "pb-2 ic-1"),
            R("Regarder Neuhaus, sans rien dire.", 2, "pb-1 er-1"),
            R("« Pas encore. On le fait tous les trois, avec Samuel ? »", 3, "pb2 ic3", sets=["cirs_declare"]),
            R("« Non, et ce n'est pas nécessaire : personne n'a été blessé. »", 2, "pb-3 ic-2"),
        ]),
        I(2, "ines", "cold-anger",
          "« Il ne s'est rien passé parce que quelqu'un a vérifié. » Inès ne hausse pas la "
          "voix. « La prochaine fois, ce ne sera peut-être pas le cas. C'est pour ça que ça "
          "existe. »", [
            R("« Vous avez raison. Je le fais. »", 3, sets=["cirs_declare"], scores="pb2 ic2"),
            R("« C'est au Dr Neuhaus de décider. »", 4, "pb-2 ic-1"),
            R("« Montrez-moi comment on fait. »", 3, "ic2 pb2", sets=["cirs_declare"]),
            R("« C'est anonyme ? Alors ça ne sert à rien. »", 4, "pb-2 cc-1"),
        ]),
        I(3, "kevin", "neutral",
          "Le formulaire de déclaration est ouvert. Trois cases : « Que s'est-il passé ? », "
          "« Pourquoi ? », « Qu'est-ce qui aurait pu l'éviter ? ». Kevin tape la première. "
          "« Tu écris quoi, pour « pourquoi » ? »", [
            R("« L'allergie des urgences a été recopiée d'une vieille lettre, l'entrée a été "
              "faite par un·e étudiant·e sans relecture, et ce que la famille a dit à une ASSC "
              "n'avait aucun chemin jusqu'au prescripteur. »", 5, "cc3 pb2 ic2"),
            R("« Erreur humaine. »", 5, "cc-2 ic-1"),
            R("« Le médecin a prescrit sans vérifier. »", 6, "ic-3 pb-1"),
            R("« Les faits, sans les noms : ce qui a manqué, à chaque étape. »", 5, "cc2 pb2"),
        ]),
        I(4, "kevin", "neutral",
          "Kevin hausse les épaules. « Alors je le fais seul. C'était ma poche. » Il s'assoit "
          "devant l'écran.", [
            R("« Attends. Je le fais avec toi. »", 3, sets=["cirs_declare"], scores="pb2 ic2"),
            R("Le laisser faire.", 7, "ic-1 pb-1"),
            R("« Je témoigne dans ta déclaration, alors. »", 3, "ic2 pb1", sets=["cirs_declare"]),
            R("« Ne mets pas mon nom, surtout. »", 7, "pb-3 ic-2"),
        ]),
        I(5, "neuhaus", "resigned",
          "Neuhaus lit par-dessus votre épaule. « « Sans relecture. » » Il soupire. « C'est "
          "moi, ça. J'aurais dû relire ton entrée avant de signer. » Un temps. « Mets-le. »", [
            R("« Ce n'est pas contre toi. C'est trente patients pour un assistant, la "
              "nuit. »", 7, "ic2 em2"),
            R("« Oui, tu aurais dû. »", 7, "ic-2 em-1"),
            R("« On l'a tous raté quelque part. Moi le premier. »", 7, "ic2 er1 pb1"),
            R("« Je ne voulais pas t'accuser, mais c'est vrai. »", 7, "ic-2"),
        ]),
        I(6, "kevin", "cold-anger",
          "Kevin arrête de taper. « Le médecin a prescrit sans vérifier ? » Il se tourne. « Et "
          "nous, à 21 h, on avait vérifié quoi ? »", [
            R("« Pardon. Tu as raison. Je réécris. »", 3, "ic2 pb1"),
            R("« C'est lui qui prescrit. »", 7, "ic-2"),
            R("« Rien. Tu as raison. »", 3, "pb2 er1"),
            R("« Moi, j'ai vérifié à 2 h. »", 7, "ic-2 pb-1"),
        ]),
        I(7, "moreau", "neutral",
          "7 h 45. Dr Moreau vous croise dans le couloir. « Kevin m'a raconté. » Un regard. "
          "« Vous rentrez dormir. Et demain, on en reparle. » Puis : « Comment ça va ? »", [
            R("« Je n'arrête pas de penser à ce qui se serait passé si personne n'avait "
              "vérifié. »", END, "er3 ic1"),
            R("« Bien. Il ne s'est rien passé. »", END, "er-1 pb-1"),
            R("« Crevé·e, mais content·e d'avoir eu raison. »", END, "er0 pb-1"),
            R("« Épuisé·e. Et reconnaissant·e envers Kevin et Fatou. »", -1, "er2 ic2"),
            R("« J'ai sauvé un patient cette nuit. »", -1, "ic-2 pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5.6 La visite
# ---------------------------------------------------------------------------
S5_6N = S(9, "5.6 La visite",
    "Vendredi, 15 h. Vous avez dormi six heures. M. Jaquier est assis dans son fauteuil, "
    "sans oxygène, un bracelet rouge au poignet. Mme Jaquier lui coupe une pomme en "
    "quartiers.",
    focus=("rd", "cc", "co"),
    slot="5.6",
    cond=when(all=["evite"]),
    entries=[
        Entry(2, when(all=["quasi_dit"])),
    ],
    nodes=[
        I(1, "monique", "grateful",
          "« C'est vous ! » Mme Jaquier pose son couteau. « Il va mieux. Le docteur dit que "
          "l'antibiotique fait effet. » Puis, plus bas : « L'infirmier de nuit m'a dit qu'il "
          "y avait eu un souci avec un médicament. Il n'a pas voulu en dire plus. »", [
            R("« Oui. Cette nuit, un antibiotique de la famille des pénicillines avait été "
              "préparé pour votre mari. L'allergie n'était pas encore là où le prescripteur la "
              "voyait. On l'a arrêté avant qu'il soit donné, grâce à ce que vous aviez dit. Je "
              "vous devais cette information. »", 3,
              sets=["quasi_dit"], scores="rd3 cc3 pb2 em1"),
            R("« Rien de grave, un petit souci d'organisation. »", 4, "pb-2 cc-2"),
            R("« Il faudra demander au médecin. »", 5, "pb-1 cc-1"),
            R("« Oui. Je vais vous raconter exactement ce qui s'est passé cette nuit. »", 3, "pb3 cc2", sets=["quasi_dit"]),
            R("« L'infirmier a dû se tromper. »", 4, "pb-3 ic-2 cc-1"),
        ]),
        I(2, "monique", "grateful",
          "Mme Jaquier vous prend la main. « Vous m'aviez dit, au téléphone, cette nuit. Pour "
          "la pénicilline qu'ils avaient préparée. » Elle serre. « J'y ai pensé jusqu'au "
          "matin. »", [
            R("« Je suis désolé·e de vous avoir laissé ça pour la nuit. Vous voulez qu'on en "
              "reparle, avec le Dr Neuhaus ? »", 3, "co2 em2 ic1"),
            R("« Tout va bien, maintenant. »", 3, "em-1 co-1"),
            R("« Vous avez eu raison de nous le dire, hier soir. »", 3, "rd2 co1"),
            R("« Il ne fallait pas vous inquiéter. »", 3, "em-2 cc-1"),
        ]),
        I(3, "roland", "neutral",
          "M. Jaquier repose son quartier de pomme. « Monique m'a dit. Pour la pénicilline. » "
          "Il grommelle : « J'avais dit que c'était rien. » Puis, plus sérieux : « Vous voulez "
          "dire que si ma femme n'avait pas été là… »", [
            R("« Si votre femme n'avait rien dit, et si personne ne l'avait écoutée, oui, ça "
              "aurait pu être très grave. Ce n'était pas rien, M. Jaquier. C'était une "
              "anaphylaxie. »", 6, "cc3 rd2 pb1"),
            R("« N'y pensez pas. Tout va bien. »", 6, "cc-2"),
            R("« Vous auriez dû le dire vous-même. »", 7, "rd-2 em-2"),
            R("« Votre femme a bien fait d'insister. Et maintenant, vous savez, vous aussi. »", 6, "rd2 cc2"),
        ]),
        I(4, "monique", "suspicious",
          "« Un souci d'organisation. » Elle regarde le bracelet rouge au poignet de son mari. "
          "« Alors pourquoi il a ça depuis cette nuit ? »", [
            R("« Vous avez raison, je vous dois la vérité. Cette nuit, une pénicilline avait "
              "été préparée pour lui. On l'a arrêtée avant qu'elle soit donnée, grâce à ce que "
              "vous aviez dit. »", 3, sets=["quasi_dit"], scores="pb3 cc2 rd1"),
            R("« C'est la procédure. »", 8, "pb-2 cc-1"),
            R("« C'est une précaution. Et je vous dois une explication. » Puis la lui donner.", 3, "pb2 cc2", sets=["quasi_dit"]),
            R("« C'est pour tous les patients. »", 8, "pb-3 cc-2"),
        ]),
        I(5, "monique", "neutral",
          "« Au médecin ? » Elle vous regarde. « Mais vous êtes là, vous. »", [
            R("« Vous avez raison. Cette nuit, une pénicilline avait été préparée pour lui. On "
              "l'a arrêtée avant qu'elle soit donnée, grâce à ce que vous aviez dit. »", 3,
              sets=["quasi_dit"], scores="pb2 cc2 rd1"),
            R("« Je vais chercher le Dr Neuhaus. »", 9, "ic1 pb-1"),
            R("« Vous avez raison, je vous dois la vérité. » Et la lui dire.", 3, "pb2 cc2", sets=["quasi_dit"]),
            R("« Je ne suis pas autorisé·e à vous en parler. »", 9, "pb-2 cc-1"),
        ]),
        I(6, "roland", "neutral",
          "« Anaphylaxie. » Il essaie le mot, le trouve trop long. « Faudrait que je l'écrive "
          "quelque part, alors. »", [
            R("« Oui. Je vous prépare une carte d'allergie à garder dans votre portefeuille, "
              "et je l'écris dans la lettre pour votre médecin traitant, pour que ça ne se "
              "perde plus. »", 10, "cc3 ic2 pb1"),
            R("« C'est dans le dossier, maintenant. »", 10, "cc1"),
            R("« Oui. Et dites-le à chaque médecin, même s'il ne vous le demande pas. »", 10, "cc2 rd1"),
            R("« Pas besoin, maintenant c'est réglé. »", 10, "cc-3 pb-1"),
        ]),
        I(7, "roland", "cold-anger",
          "« Moi ? » Il se redresse. « C'est vous, les docteurs. » Mme Jaquier pose la main sur "
          "son bras : « Roland. »", [
            R("« Pardon. C'était à nous de l'écrire et de le transmettre. »", 6, "pb2 er1"),
            R("« On ne peut pas deviner ce que les patients ne disent pas. »", 10, "pb-2 rd-1"),
            R("« Vous avez raison. C'était notre travail. »", 6, "pb2 rd1"),
            R("« Vous avez quand même failli nous faire faire une bêtise. »", 10, "rd-3 pb-2"),
        ]),
        I(8, "monique", "cold-anger",
          "« La procédure. » Elle reprend son couteau, et ne vous regarde plus. « Je "
          "demanderai au médecin. »", [
            R("« Attendez. Je vous dois la vérité. » Et la lui dire.", 3,
              sets=["quasi_dit"], scores="pb2 cc2 er1"),
            R("Sortir.", 10, "pb-2 rd-1"),
            R("« Madame, je me suis mal exprimé·e. Voici ce qui s'est passé. »", 3, "pb2 cc2", sets=["quasi_dit"]),
            R("« Comme vous voulez. »", 10, "pb-2 em-1"),
        ]),
        I(9, "neuhaus", "neutral",
          "Neuhaus entre, s'assoit sur le bord du lit et explique tout, simplement : la "
          "poche, l'allergie qui n'était pas dans le dossier, l'arrêt à temps. Il s'excuse. "
          "En sortant, il vous glisse : « Tu aurais pu lui dire, tu sais. »", [
            R("« Oui. J'ai eu peur de mal faire. »", 10, "er2 pb1"),
            R("« Ce n'était pas mon rôle. »", 10, "pb-2 ic-1"),
            R("« Tu as raison. Je le ferai, la prochaine fois. »", 10, "pb2 er1"),
            R("« Tu as bien fait de le faire, c'est ton rôle. »", 10, "pb-1 ic1"),
        ]),
        I(10, "monique", "grateful",
          "Mme Jaquier range la pomme dans une boîte. « Vous savez, ça fait trente ans que je "
          "lui dis d'en parler, de cette piqûre. » Elle secoue la tête. « Personne ne l'avait "
          "jamais écrit. »", [
            R("« Maintenant, c'est écrit. Et c'est grâce à vous. »", END, "co2 rd2"),
            R("« Voilà. »", END, "co0"),
            R("« Il aurait pu le dire lui-même. »", END, "rd-2 co-1"),
            R("Lui sourire. « Et c'est vous qui l'avez sauvé. »", -1, "co2 rd2"),
        ]),
    ],
)

CH5 = C(5, "Une seule ligne",
    situation=(
        "Sixième semaine, la nuit du 14. Une entrée banale à 19 h : un homme de 71 ans avec "
        "une pneumonie, sa femme, un sac de médicaments, une lettre des urgences. Une "
        "ligne à remplir : « Allergies ». À 2 h 10, un antibiotique à prescrire vite."
    ),
    objectives=(
        "mener une anamnèse médicamenteuse et allergique active plutôt que recopier, "
        "reconnaître l'entourage comme source d'information, transmettre une information de "
        "sécurité (relève structurée), solliciter et écouter les soignant·e·s de "
        "proximité, oser vérifier et contredire sous pression hiérarchique et temporelle ; "
        "en cas d'incident, reconnaître une anaphylaxie et appeler sans délai, dire la vérité "
        "à la famille la nuit même, ne jamais modifier le dossier a posteriori, déclarer "
        "l'incident ou le quasi-incident ; reconnaître la fatigue comme facteur de risque."
    ),
    anchoring=(
        "UNIL M1.6 cours-blocs (anamnèse, pharmacologie clinique) et M1.7 droit médical, "
        "assécurologie · UNIGE M1 AMC Médecine interne, pharmacologie clinique, "
        "enseignement interprofessionnel (sécurité des patients, communication "
        "interprofessionnelle)."
    ),
    focus=("pb", "cc", "ic", "er"),
    scenes=[S5_1, S5_2, S5_3, S5_4E, S5_5E, S5_6E, S5_4N, S5_5N, S5_6N],
)
