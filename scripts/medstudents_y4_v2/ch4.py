"""Chapitre 4 — Ceux qui restent (semaine 5)."""
from __future__ import annotations

from .dsl import END, C, Entry, I, R, S, when

# ---------------------------------------------------------------------------
# 4.1 Chambre 312
# ---------------------------------------------------------------------------
S4_1 = S(1, "4.1 Chambre 312",
    "Cinquième semaine, lundi, 8 h. M. Ferreira a été réhospitalisé cette nuit, dix jours "
    "après son premier cycle de chimio-immunothérapie : essoufflement, épanchement "
    "pleural, peau jaune. Il est seul dans la chambre 312, sous oxygène. Il a demandé "
    "« l'étudiant·e de la première semaine ».",
    focus=("rd", "em", "pb", "ic"),
    nodes=[
        I(1, "ferreira", "neutral",
          "Il a encore maigri. Ses mains, posées sur le drap, sont jaunes. « Ah. C'est "
          "vous. » Un sourire fatigué. « Asseyez-vous. Je voudrais vous demander quelque "
          "chose, et je ne veux pas que vous répondiez en docteur. »", [
            R("S'asseoir. « Je vous écoute. »", 2, "rd2 em2 co1"),
            R("« Je dois finir le tour d'abord, je repasse tout à l'heure. »", 3, "rd-1 em-1 co-1"),
            R("« Je ne peux répondre qu'en étudiant·e en médecine, vous savez. »", 2, "pb1 em-1"),
            R("Tirer la chaise près du lit, s'asseoir à sa hauteur, et attendre.", 2, "rd2 em2 co1"),
            R("« Vous avez meilleure mine que je pensais ! »", 3, "cc-2 em-2"),
        ]),
        I(2, "ferreira", "melancholic",
          "« Je veux arrêter. La chimio. » Il reprend son souffle. « Dix jours à vomir dans "
          "un seau pour revenir ici plus jaune qu'avant. Je veux rentrer. Voir mes filles, et "
          "la petite. » Il vous regarde. « Vous m'aidez à le dire au docteur ? Carla ne va "
          "pas vouloir. »", [
            R("« C'est une décision importante, et c'est la vôtre. Avant qu'on la porte "
              "ensemble à l'équipe, j'aimerais comprendre ce qui vous fait dire ça "
              "aujourd'hui. »", 4, "rd3 em2 pb2 cc1 ic1"),
            R("« Vous ne pouvez pas arrêter après un seul cycle, c'est trop tôt. »", 5, "rd-2 pb-2 em-1"),
            R("« D'accord. Je le dis au Dr Moreau tout de suite, c'est réglé. »", 6, "pb-2 ic-1 cc-1"),
            R("« Vous voulez rentrer. Qu'est-ce qui compte le plus, à la maison ? »", 4, "em3 rd2"),
            R("« On ne décide pas ça comme ça. Parlez-en d'abord à votre fille. »", 5, "rd-3 pb-2"),
        ]),
        I(3, "ferreira", "resigned",
          "« Bien sûr. Le tour. » Il tourne la tête vers la fenêtre. Dans le couloir, Neuhaus "
          "vous attend déjà devant le 314.", [
            R("Revenir s'asseoir. « Le tour peut attendre cinq minutes. Je vous écoute. »",
              2, "rd2 em2 co1"),
            R("Rejoindre Neuhaus et repasser à midi.", 7, "em-2 co-1"),
            R("« Je préviens le Dr Neuhaus que je suis là, et je reviens tout de suite. »", 2, "ic2 rd1"),
            R("« Vous savez, on a beaucoup de patients ce matin. »", 7, "rd-2 em-2"),
        ]),
        I(4, "ferreira", "sad",
          "« Je ne peux plus monter l'escalier. Je ne peux plus porter la petite. Je pèse "
          "cinquante-deux kilos. » Un silence. « Et je ne veux pas que Joana se marie avec son "
          "père qui vomit dans un seau. » Puis, plus bas : « Est-ce que c'est pareil que se "
          "tuer ? Le curé dirait quoi ? »", [
            R("« Non. Arrêter un traitement qui ne vous apporte plus ce que vous en attendez, "
              "ce n'est pas se tuer. Et arrêter la chimio, ce n'est pas arrêter les soins : on "
              "continuera à vous soigner, autrement. »", 8, "cc3 co2 rd2 em2"),
            R("« Ça, c'est une question pour l'aumônier. »", 8, "em-1 co-1 ic1"),
            R("« C'est la fatigue et la déprime qui parlent. Ça va passer. »", 9, "rd-2 em-2 cc-1"),
            R("« Qu'est-ce que vous voulez vivre, dans le temps qui reste ? »", 8, "em2 rd2 co1"),
            R("« Il faut en parler au Dr Moreau, je ne peux pas répondre à ça. »", 8, "pb1 em-2"),
        ]),
        I(5, "ferreira", "angry",
          "« Trop tôt ? » Il se redresse avec peine. « Trop tôt pour qui ? »", [
            R("« Pardon. Ce n'est pas à moi de le dire. Mon rôle, c'est que vous décidiez en "
              "sachant tout ce qu'il y a à savoir. Dites-moi pourquoi. »", 4, "rd2 pb2 er1"),
            R("« La Dre Keller pense qu'il faut continuer. »", 9, "rd-1 pb-1"),
            R("Se taire, puis : « Vous avez raison. Dites-moi pourquoi. »", 4, "rd2 er2"),
            R("« Pour la médecine. Les études montrent qu'on arrête rarement si tôt. »", 9, "rd-3 cc-1 pb-1"),
        ]),
        I(6, "moreau", "cold-anger",
          "Dans le couloir, Dr Moreau vous écoute jusqu'au bout. « Réglé ? Un patient vous dit "
          "qu'il veut arrêter son traitement, et vous venez m'annoncer que c'est réglé ? » Un "
          "temps. « Qu'est-ce que vous avez vérifié ? »", [
            R("« Rien. Je retourne l'écouter : pourquoi, ce qu'il a compris de la suite "
              "possible, s'il a mal, s'il a peur d'être un poids. »", 4, "pb2 er2 cc2"),
            R("« Il a le droit de refuser un traitement. »", 10, "pb0 cc0 er-1"),
            R("« Vous avez raison. Je n'ai même pas demandé s'il avait mal. »", 4, "pb2 er2"),
            R("« C'est lui qui l'a demandé, je ne vois pas le problème. »", 10, "pb-2 er-1 ic-1"),
        ]),
        I(7, "ines", "neutral",
          "Midi. Inès Rey vous arrête devant le 312. « Il vous a attendu·e toute la matinée. "
          "Il a refusé son plateau. » Elle ne dit rien d'autre.", [
            R("Entrer tout de suite. « Pardon de vous avoir fait attendre, M. Ferreira. Je "
              "vous écoute maintenant. »", 2, "rd2 em1 er1"),
            R("« J'y vais après ma pause. »", 2, "em-2 co-1 ic-1"),
            R("« Merci de me le dire. » Puis entrer, et s'asseoir.", 2, "ic2 co1 rd1"),
            R("« Il n'avait qu'à manger. »", 2, "rd-3 co-2 ic-1"),
        ]),
        I(8, "ferreira", "anxious",
          "« Autrement. » Il répète le mot. « Ça veut dire quoi ? Je vais étouffer ? Ma femme, "
          "à la fin, elle cherchait l'air. »", [
            R("« On a des moyens de soulager l'essoufflement et l'angoisse, et une équipe dont "
              "c'est le métier. Je peux demander qu'elle passe vous voir aujourd'hui. »",
              11, "cc2 co2 ic3"),
            R("« Mais non, vous n'étoufferez pas. »", 11, "cc-2 pb-1"),
            R("« C'est possible, oui. »", 11, "co-2 cc0 em-1"),
            R("« Votre femme cherchait l'air. Vous avez peur que ce soit pareil pour vous ? »", 11, "em3 cc1"),
            R("« On verra le moment venu. »", 11, "cc-2 co-1"),
        ]),
        I(9, "ferreira", "cold-anger",
          "« La déprime. » Il a un rire qui finit en toux. « Je suis en train de mourir, et on "
          "me dit que c'est la déprime. »", [
            R("« Vous avez raison d'être triste, ce n'est pas une maladie. Je voulais surtout "
              "m'assurer que vous ne décidez pas sous le poids d'une douleur ou d'une peur "
              "qu'on pourrait soulager. »", 8, "em2 cc2 pb1 rd1"),
            R("« C'est une question que je dois poser. »", 8, "cc0 em-1"),
            R("« Pardon. Je retire le mot. Dites-moi ce qui vous pèse le plus. »", 8, "er2 em2"),
            R("« C'est pourtant fréquent, dans votre situation. »", 8, "em-2 rd-1"),
        ]),
        I(10, "moreau", "neutral",
          "« Bien sûr qu'il a le droit. Mais un droit, ça se prépare. Qu'est-ce qu'il a compris "
          "de ce que la Dre Keller peut encore lui proposer ? Et qu'est-ce qu'il craint ? »", [
            R("« Je ne sais pas. Je retourne le lui demander. »", 4, "pb2 er1 cc1"),
            R("« Il a dit qu'il en avait marre. »", 4, "cc-1"),
            R("« Vous avez raison. Je retourne le voir, et je vous fais un compte-rendu. »", 4, "pb2 ic1"),
            R("« Il n'a pas besoin de préparer, il sait ce qu'il veut. »", 4, "pb-2 ic-1"),
        ]),
        I(11, "neuhaus", "neutral",
          "Dans le couloir, Neuhaus, les yeux cernés. « T'as parlé au 312 ? Keller veut lui "
          "proposer une deuxième ligne. On ne va pas arrêter après un cycle, il a cinquante-huit "
          "ans. »", [
            R("« Il m'a dit clairement qu'il veut arrêter, et pourquoi. Je pense qu'il doit "
              "pouvoir le dire lui-même à Keller et Moreau, et qu'on appelle l'équipe mobile de "
              "soins palliatifs. »", 12, "ic3 pb2 rd2 cc1 er1"),
            R("« T'as raison, il va sûrement changer d'avis. »", 13, "rd-2 ic-1 pb-2"),
            R("« C'est sa vie, pas la tienne. »", 13, "er-2 ic-2"),
            R("« Je comprends que tu veuilles lui donner une chance. Mais la décision est la sienne. On peut en parler à Keller avec lui ? »", 12, "ic3 pb2 er1"),
            R("« Tu as raison, je vais lui dire de réfléchir encore. »", 13, "rd-3 pb-2 ic-1"),
        ]),
        I(12, "neuhaus", "neutral",
          "Il se frotte les yeux. « OK. Keller passe à 15 h. Tu organises. » Puis : « Et la "
          "famille ? La fille aînée va hurler. »", [
            R("« C'est à lui de dire qui il veut autour de la table, et quand. Je lui "
              "demande. »", 13, "rd3 pb2"),
            R("« On appelle Carla tout de suite pour la prévenir. »", 13, "rd-2 pb-2"),
            R("« Je lui propose d'inviter qui il veut, et je préviens Mathilde pour la réunion. »", 13, "rd2 ic2"),
            R("« Elle hurlera, on n'y peut rien. »", 13, "em-2 ic-1"),
        ]),
        I(13, "mathilde", "neutral",
          "Une femme en blouse blanche, badge vert, vous rejoint au desk. « Mathilde Favre, "
          "équipe mobile de soins palliatifs. Inès m'a appelée. On m'a dit que M. Ferreira "
          "voulait parler de la suite. Vous en êtes où ? »", [
            R("Lui transmettre ses mots à lui : ce qu'il veut, pourquoi, ce qu'il craint "
              "(étouffer comme sa femme), et qu'il veut en parler lui-même à 15 h.",
              14, "ic3 cc3 rd1"),
            R("« On n'a pas encore décidé, le Dr Neuhaus veut continuer. »", 14, "ic-1 cc-1"),
            R("« Il est un peu déprimé, je crois. »", 14, "cc-2 rd-1"),
            R("« Il veut arrêter. Est-ce que vous pouvez être là à 15 h ? »", 14, "ic2 cc1"),
            R("« Rien de spécial, on attend l'avis de l'oncologue. »", 14, "ic-2 cc-2"),
        ]),
        I(14, "ferreira", "neutral",
          "17 h. La réunion a eu lieu : Keller, Moreau, Mathilde, lui. M. Ferreira a l'air "
          "plus léger. « C'est décidé. On arrête. La doctoresse a dit que c'était raisonnable. "
          "Et elle m'a demandé si je voulais qu'on me réanime, si le cœur s'arrête. J'ai dit "
          "non. » Il vous regarde. « Samedi, mes filles viennent. Il faut qu'on leur dise. "
          "Vous serez là ? »", [
            R("« Si vous le voulez, oui. Et Mathilde aussi : ces réunions, c'est son métier. »",
              END, "ic2 co2 rd1"),
            R("« Le Dr Moreau sera plus indiqué·e que moi. »", END, "ic0 em-1"),
            R("« Vous devriez le leur dire seul, c'est plus intime. »", END, "em-2 co-1 ic-1"),
            R("« Je serai là. Voulez-vous qu'on prépare ensemble ce que vous leur direz ? »", -1, "co2 rd2 ic1"),
            R("« Ce n'est plus vraiment mon rôle. »", -1, "co-2 ic-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.2 Les deux sœurs
# ---------------------------------------------------------------------------
S4_2 = S(2, "4.2 Les deux sœurs",
    "Samedi, 10 h. Salle des familles. M. Ferreira, en fauteuil roulant, sous oxygène. "
    "Carla, un classeur sur les genoux. Joana, les yeux déjà rouges. Mathilde Favre et Dr "
    "Moreau. Tiago, le fiancé de Joana, attend dans le couloir.",
    focus=("ic", "em", "er", "cc"),
    nodes=[
        I(1, "carla", "cold-anger",
          "Carla ouvre son classeur avant que quiconque ait parlé. « Je veux qu'on m'explique "
          "pourquoi on arrête la chimio. Il y a des essais cliniques, j'ai lu, à Zurich. On va "
          "se battre. » Elle se tourne vers vous, qu'elle connaît depuis la première semaine.", [
            R("« Avant qu'on réponde, je crois que votre père a quelque chose à vous dire "
              "lui-même. » Regarder M. Ferreira.", 2, "rd3 pb2 ic1"),
            R("Expliquer : « La chimio l'a beaucoup affaibli et la maladie a progressé dans le "
              "foie… »", 3, "cc2 rd-1 pb-1"),
            R("« C'est une décision médicale. »", 4, "rd-3 pb-2 cc-2"),
            R("« Je comprends que vous vouliez tout essayer. On peut d'abord écouter votre père ? »", 2, "em2 rd2"),
            R("« Zurich, c'est pour les patients qui ont encore une chance. »", 4, "co-3 cc-2 rd-2"),
        ]),
        I(2, "ferreira", "neutral",
          "« C'est moi qui ai demandé, Carla. » Il lui prend la main. « Je ne veux plus. » "
          "Carla se dégage. « Tu dis ça parce que tu es fatigué. Papa, tu ne peux pas "
          "abandonner. » Joana, doucement : « Carla, laisse-le parler. »", [
            R("À Carla : « Vous avez peur de le perdre, et votre père l'entend. Il a aussi "
              "besoin que vous entendiez ce qu'il veut, lui. »", 5, "em3 er2 rd2 co2"),
            R("Se taire, et laisser le silence faire son travail.", 5, "er2 rd1"),
            R("À Joana : « Merci, Joana. »", 6, "ic-1 er-1 em-1"),
            R("Poser la main sur la table, entre eux, sans rien dire.", 5, "co2 er1"),
            R("« Carla, votre père est adulte. »", 6, "rd1 em-2 er-1"),
        ]),
        I(3, "carla", "suspicious",
          "« Vous êtes l'étudiant·e, c'est ça ? » Elle vous toise. « Vous répétez ce qu'on "
          "vous a dit de répéter. »", [
            R("« Vous avez raison, ce n'est pas à moi d'expliquer. Monsieur Ferreira ? »",
              2, "rd2 er2 pb1"),
            R("« Je connais le dossier mieux que vous, madame. »", 4, "rd-2 er-2 pb-1"),
            R("« Je répète ce que votre père m'a dit, à moi. Vous voulez l'entendre de lui ? »", 2, "rd2 cc2"),
            R("« Je suis là pour apprendre, pas pour vous répondre. »", 4, "pb-1 em-2"),
        ]),
        I(4, "moreau", "cold-anger",
          "Dr Moreau pose la main à plat sur la table. « Permettez. Ce n'est pas une décision "
          "médicale imposée. C'est la décision de votre père, et nous la soutenons. » Puis, "
          "vers vous : « Alex ? »", [
            R("« Pardon, je me suis mal exprimé·e. Monsieur Ferreira, vous voulez leur "
              "dire ? »", 2, "rd2 er1 pb1"),
            R("« C'est ce que je voulais dire. »", 2, "pb-1"),
            R("« Oui. Ce n'est pas nous qui décidons : c'est lui. »", 2, "rd2 cc1"),
            R("Se taire, et regarder ses mains.", 2, "er-1 pb-1"),
        ]),
        I(5, "carla", "angry",
          "Carla se tourne vers Mathilde, vers Moreau, vers vous. « Et Zurich ? Les essais ? "
          "Vous ne lui avez même pas proposé ! »", [
            R("« C'est une vraie question. La Dre Keller l'a regardée avec votre père : il n'y "
              "a pas d'essai auquel il puisse participer dans son état. Elle peut vous montrer "
              "ce qui a été vérifié. »", 7, "cc3 pb1 ic2 em1 rd1"),
            R("« Les essais, c'est pour les patients en meilleur état. »", 7, "cc1 em-1 co-1"),
            R("« Je vais me renseigner. On pourrait peut-être l'envoyer à Zurich. »", 8, "pb-3 cc-2 ic-1 rd-1"),
            R("« Vous voulez qu'on appelle la Dre Keller maintenant, pour qu'elle vous explique elle-même ? »", 7, "ic3 cc1"),
            R("« Il est trop tard pour ça. »", 7, "cc-2 co-2"),
        ]),
        I(6, "carla", "angry",
          "« Merci Joana. » Carla a un rire amer. « Évidemment. Joana la gentille, et moi la "
          "méchante qui veut garder son père. »", [
            R("« Ce n'est pas ce que je voulais dire. Personne n'est méchant ici. Vous voulez "
              "toutes les deux la même chose : lui. »", 5, "er2 em2 co1"),
            R("« Je n'ai pas dit ça. »", 5, "er-1 em-1"),
            R("« Vous l'aimez. C'est pour ça que c'est si dur. »", 5, "em3 co1"),
            R("« Ce n'est pas une compétition entre sœurs. »", 5, "em-2 er-1"),
        ]),
        I(7, "joana", "sad",
          "Joana a les yeux pleins de larmes. « Et le mariage ? C'est le 13 septembre. » Elle "
          "regarde son père, puis vous. « Papa, tu seras là ? »", [
            R("« Je ne peux pas vous promettre septembre. Personne ne le peut. Si ce jour "
              "compte pour vous deux, je ne l'attendrais pas. »", 9, "cc3 co2 rd1 em2 pb1"),
            R("« Il faut rester optimiste. »", 9, "cc-2 co-1"),
            R("« Honnêtement ? Non. »", 10, "co-3 em-2 cc0"),
            R("Regarder M. Ferreira : « Qu'est-ce que vous souhaitez, vous, pour ce mariage ? »", 9, "rd3 em1"),
            R("« Bien sûr qu'il sera là. »", 9, "cc-3 pb-3 co-1"),
        ]),
        I(8, "mathilde", "neutral",
          "Mathilde intervient sans hausser la voix. « Alex, on ne peut pas proposer quelque "
          "chose qui n'existe pas. » Carla vous fixe, suspendue à ce que vous allez dire.", [
            R("« Vous avez raison. Carla, je ne veux pas vous faire espérer quelque chose qui "
              "n'existe pas. La Dre Keller vous montrera ce qui a été vérifié. »", 7, "pb2 cc2 er1"),
            R("« Je voulais juste la rassurer. »", 7, "pb-1 er-1"),
            R("« Pardon. J'ai voulu vous donner de l'espoir, et c'était faux. »", 7, "pb2 er1 cc1"),
            R("« On ne sait jamais, avec les nouveaux traitements. »", 7, "pb-3 cc-2"),
        ]),
        I(9, "ferreira", "melancholic",
          "M. Ferreira regarde sa cadette. « Joana. Fais-le avant. Fais-le ici, s'il faut. » "
          "Joana éclate en sanglots. Carla se lève, renverse sa chaise, et sort.", [
            R("Laisser la réunion à Mathilde et rejoindre Carla dans le couloir.", 11, "em2 ic2 co1"),
            R("Rester, et laisser Carla seule un moment.", 12, "er1"),
            R("« Carla, rasseyez-vous, on n'a pas fini. »", 12, "rd-2 em-2"),
            R("Demander du regard à M. Ferreira s'il veut qu'on aille chercher Carla.", 11, "rd2 ic1"),
            R("« Elle reviendra quand elle sera calmée. »", 12, "em-2 co-1"),
        ]),
        I(10, "joana", "angry",
          "« Non ? » Joana se lève. « Comme ça ? « Non » ? »", [
            R("« Pardon. Je voulais dire : je ne peux pas vous promettre septembre, et si ce "
              "jour compte, il ne faut pas l'attendre. »", 9, "cc2 er1 co1"),
            R("« Vous m'avez demandé d'être honnête. »", 9, "er-2 co-2"),
            R("Se taire, et attendre qu'elle se rassoie.", 9, "er2"),
            R("« Il fallait bien que quelqu'un le dise. »", 9, "co-3 er-2"),
        ]),
        I(11, "carla", "sad",
          "Elle est à la fenêtre du couloir, les bras croisés. « Quand maman est morte, j'ai "
          "tout organisé. Les papiers, l'enterrement, la vente de la voiture. Je n'ai jamais "
          "pleuré. » Sa voix se casse. « Si j'arrête d'organiser, je fais quoi ? »", [
            R("« Peut-être être sa fille. Il y a des gens ici dont c'est le métier "
              "d'organiser. Vous, vous êtes la seule à pouvoir être Carla. »", 13, "em3 co3 rd2"),
            R("« Il faut laisser les choses se faire. »", 13, "co-1 em-1"),
            R("« Vous pourriez vous occuper des démarches de l'AI, ça l'aiderait. »", 13, "em-1 ic1"),
            R("Se mettre à côté d'elle, face à la fenêtre, sans parler.", 13, "co2 em1"),
            R("« Vous devriez retourner dans la salle, votre père a besoin de vous. »", 13, "em-2 rd-1"),
        ]),
        I(12, "mathilde", "neutral",
          "Mathilde termine avec Joana et M. Ferreira : ce qui se passe maintenant, qui "
          "appeler, les médicaments de confort. Puis elle vous glisse : « Tu veux aller voir "
          "Carla ? Elle ne doit pas rester seule avec ça. »", [
            R("« J'y vais. »", 11, "em2 ic2"),
            R("« Je crois qu'elle a besoin d'être seule. »", 13, "em-1 ic-1"),
            R("« Oui. Tu peux continuer sans moi ? »", 11, "ic2"),
            R("« Elle est adulte, elle reviendra. »", 13, "em-2 ic-1"),
        ]),
        I(13, "carla", "neutral",
          "Elle s'essuie les yeux d'un geste sec. « Et Lina ? Elle me demande tous les soirs "
          "si Vovô va guérir. Je lui dis qu'il est fatigué. » Elle vous regarde. « Je lui dis "
          "quoi ? »", [
            R("« On peut préparer ça ensemble. Les enfants de son âge comprennent plus qu'on ne "
              "croit, et ils souffrent surtout de ce qu'on ne leur dit pas. »", 14, "em2 cc2 co1 ic1"),
            R("« C'est votre choix de mère. »", 14, "pb1 em-1"),
            R("« Il faut lui dire la vérité ce soir. »", 14, "rd-2 pb-1 em-1"),
            R("« Qu'est-ce qu'elle a déjà compris, à votre avis ? »", 14, "em2 cc1"),
            R("« Dites-lui qu'il est en voyage. »", 14, "rd-3 cc-3"),
        ]),
        I(14, "moreau", "neutral",
          "Après la réunion, Dr Moreau vous retient. « Qu'est-ce qu'on transmet à l'équipe, "
          "de ce qui s'est passé ce matin ? »", [
            R("« Que M. Ferreira a exprimé lui-même sa décision, que Carla n'est pas d'accord "
              "et a besoin d'être accompagnée, que Joana envisage d'avancer la cérémonie, et "
              "que la question de Lina est ouverte. Je l'écris. »", END, "cc3 ic3"),
            R("« Que la famille est divisée. »", END, "cc0 ic0 rd-1"),
            R("« Que Carla est difficile. »", END, "rd-2 ic-1 cc-1"),
            R("« Que la décision vient du patient, et que la famille a besoin qu'on reste avec elle. »", -1, "cc2 ic1 rd1"),
            R("« Rien, tout le monde était là. »", -1, "ic-2 cc-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.3 Lina
# ---------------------------------------------------------------------------
S4_3 = S(3, "4.3 Lina",
    "Dimanche, 15 h. Salle des familles. Lina, neuf ans, dessine au feutre sur une feuille "
    "de soins retournée. Carla téléphone dans le couloir, dos tourné. Lina vous voit "
    "passer.",
    focus=("em", "rd", "cc", "co"),
    nodes=[
        I(1, "lina", "neutral",
          "« T'es le docteur de Vovô ? » Elle ne lève pas les yeux de son dessin. « Est-ce "
          "qu'il va mourir ? »", [
            R("« Qu'est-ce qui te fait penser ça ? »", 5, "em2 cc1 rd1"),
            R("« C'est une question très importante. Je veux bien y répondre, mais avec ta "
              "maman. Tu veux qu'on aille la chercher ensemble ? »", 2, "rd2 pb2 em1 ic1"),
            R("« Mais non, il est juste très fatigué. »", 3, "rd-2 cc-3"),
            R("« Oui. Il va mourir. »", 4, "pb-3 co-2 em-2"),
            R("S'asseoir à côté d'elle. « C'est un joli dessin. Tu me le racontes ? »", 5, "em2 co1"),
            R("« Ce sont des questions pour les grands. »", 3, "rd-3 em-2"),
        ]),
        I(2, "carla", "anxious",
          "Carla raccroche. « Lina, qu'est-ce que tu fais ? » — « Je demande si Vovô va "
          "mourir. » Carla pâlit et vous regarde. « On avait dit qu'on lui dirait qu'il "
          "était fatigué. »", [
            R("À Carla, à l'écart : « Elle pose la question. Si on ne lui répond pas, elle va "
              "imaginer pire, toute seule. Je peux vous aider — c'est vous qui choisissez les "
              "mots. »", 6, "pb2 em2 cc2 rd1"),
            R("« Je ne lui ai rien dit. C'est vous qui voyez. »", 7, "pb1 ic-1 em-1"),
            R("« Madame, votre fille a le droit de savoir. »", 7, "rd-1 em-2 er-1"),
            R("« Je peux rester, ou vous laisser toutes les deux. Qu'est-ce qui vous aiderait ? »", 6, "rd2 em1 ic1"),
            R("« Vous lui mentez depuis des jours, elle le sent. »", 7, "em-3 rd-2 er-1"),
        ]),
        I(3, "lina", "suspicious",
          "Elle lève enfin les yeux. « Tu mens. Maman aussi, elle dit ça. Mais Vovô, il a une "
          "bouteille d'air maintenant. Et Tia Joana pleure dans les toilettes. »", [
            R("« Tu as raison, ce n'est pas juste de la fatigue. Je veux bien t'expliquer, avec "
              "ta maman. »", 2, "cc2 rd2 er1"),
            R("« Je ne mens pas. »", 8, "cc-2 rd-2"),
            R("« Tu as bien observé. Tu veux qu'on en parle avec ta maman ? »", 2, "rd2 cc1"),
            R("« Tu es trop petite pour comprendre. »", 8, "rd-3 em-2"),
        ]),
        I(4, "carla", "angry",
          "Carla est dans l'embrasure. Elle a entendu. Lina s'est figée, le feutre en l'air. "
          "« Vous avez dit quoi à ma fille ? »", [
            R("« Pardon. J'ai répondu trop vite, sans vous. Je reste, si vous voulez, et c'est "
              "vous qui décidez de la suite. »", 6, "pb2 er2 rd1"),
            R("« Elle m'a posé la question. »", 7, "er-1 pb-1"),
            R("Se mettre à genoux près de Lina et dire à Carla : « Je suis désolé·e. On peut en parler toutes les trois ? »", 6, "pb1 er1 co1"),
            R("« De toute façon, elle allait le savoir. »", 7, "pb-3 rd-2"),
        ]),
        I(5, "lina", "neutral",
          "Elle hausse les épaules. « Parce que tout le monde chuchote. » Elle colorie un "
          "carreau en bleu, très fort. Puis, sans vous regarder : « Et parce que j'ai crié sur "
          "lui. »", [
            R("« Tu as crié sur lui ? »", 9, "em3 rd1"),
            R("« Les adultes chuchotent souvent, ça ne veut rien dire. »", 3, "cc-2 em-1"),
            R("« Tu entends qu'on chuchote. Ça doit faire peur. »", 9, "em3"),
            R("« Tu n'as rien fait de mal, ne t'inquiète pas. »", 3, "cc-1 em1"),
        ]),
        I(6, "carla", "sad",
          "Carla s'assoit. Elle a l'air d'avoir dix ans elle aussi. « Je ne sais pas comment "
          "on dit ça à une enfant. » Un temps. « Aidez-moi. »", [
            R("« On peut commencer par lui demander ce qu'elle a compris. Et utiliser les vrais "
              "mots — malade, mourir — avec des phrases simples. Vous commencez, et je "
              "complète ? »", 10, "cc3 ic2 em1 rd1"),
            R("« Je peux le faire à votre place. »", 10, "pb-1 rd-1"),
            R("« On pourrait lui dire que Vovô va partir en voyage. »", 11, "cc-3 rd-2"),
            R("« On peut lui dire ensemble, et vous la gardez contre vous. »", 10, "co2 ic2 em1"),
            R("« Je ne sais pas non plus. »", 10, "cc-1 er-1"),
        ]),
        I(7, "carla", "cold-anger",
          "« Lina, mets ton manteau. On rentre. » Lina proteste. « Mais je veux savoir ! » "
          "Carla la tire par la manche.", [
            R("« Attendez. Lina a posé une vraie question, et elle attend une réponse. Est-ce "
              "qu'on peut la lui donner ensemble, avec vos mots ? »", 6, "em2 pb2 er1 rd1"),
            R("Les laisser partir.", 12, "em-2 co-1"),
            R("« Je comprends. Vous voulez qu'on en reparle demain, avec Mathilde ? »", 12, "ic2 em1"),
            R("« Faites comme vous voulez. »", 12, "em-2 co-1"),
        ]),
        I(8, "lina", "sad",
          "Elle retourne à son dessin et ne dit plus rien. Le feutre bleu déborde des "
          "carreaux.", [
            R("S'asseoir à côté d'elle. « Je peux regarder ton dessin ? »", 5, "em2 co2"),
            R("Partir sans insister.", 12, "em-2"),
            R("Prendre un feutre et colorier un carreau à côté du sien, en silence.", 5, "em2 co2"),
            R("« Bon, je te laisse. »", 12, "em-2 co-1"),
        ]),
        I(9, "lina", "ashamed",
          "« La semaine passée. Il ne voulait pas jouer aux cartes. J'ai dit qu'il était nul. » "
          "Elle serre le feutre. « Et après, il est retourné à l'hôpital. »", [
            R("« Ce n'est pas du tout à cause de toi. La maladie de Vovô est dans son poumon "
              "depuis longtemps, bien avant les cartes. Rien de ce que tu dis ou fais ne peut "
              "la rendre plus grave. »", 2, "em3 cc3 co2 rd1"),
            R("« Mais non, ça n'a rien à voir. »", 2, "cc1 em0"),
            R("« Il ne faut pas dire des choses méchantes aux malades. »", 8, "em-3 co-3 rd-1"),
            R("« Moi aussi, parfois, je dis des choses fâchées aux gens que j'aime. Ça ne rend personne malade. »", 2, "em3 co2"),
            R("« Tu devrais t'excuser auprès de lui. »", 8, "em-3 co-2"),
        ]),
        I(10, "carla", "sad",
          "Carla prend Lina sur ses genoux. « Vovô est très malade. Les médecins ne peuvent "
          "pas le guérir. » Lina ne pleure pas. Elle vous regarde, vous. « Il va mourir quand ? "
          "Avant mon anniversaire ? C'est en août. »", [
            R("« On ne sait pas exactement. Peut-être bientôt. Ce qu'on sait, c'est qu'on fait "
              "tout pour qu'il n'ait pas mal, et que tu peux venir le voir. »", 13, "cc3 co2 em1 rd2"),
            R("« Ça, personne ne peut le savoir. »", 13, "cc1 em-1"),
            R("« Pas avant ton anniversaire, promis. »", 14, "cc-2 pb-2"),
            R("« Ce qu'on sait, c'est qu'il t'aime, et que tu peux venir le voir quand tu veux. »", 13, "co3 em1"),
            R("« Bientôt. Peut-être cette semaine. »", 13, "cc0 co-2"),
        ]),
        I(11, "lina", "confused",
          "« En voyage ? » Lina fronce les sourcils. « Où ? Il revient quand ? Il a même plus "
          "de valise. » Carla vous regarde, perdue.", [
            R("« Lina, en fait, ce n'est pas un voyage. Vovô est très malade, et les médecins "
              "ne peuvent pas le guérir. »", 10, "cc2 er1 rd1"),
            R("« Très loin. Il ne reviendra pas. »", 14, "cc-2 em-2"),
            R("« Pardon, Lina, ce n'était pas le bon mot. Ta maman va t'expliquer. »", 10, "cc2 rd1"),
            R("« Tu comprendras plus tard. »", 14, "cc-3 rd-2"),
        ]),
        I(12, "ines", "neutral",
          "20 h. Inès Rey vous appelle au desk. « Carla vient d'appeler. Lina a fait une crise "
          "au coucher : elle veut savoir si c'est sa faute que Vovô soit malade. » Un "
          "silence. « Vous étiez avec elle cet après-midi, non ? »", [
            R("« Oui, et je l'ai laissée repartir sans réponse. Je peux proposer à Carla qu'on "
              "revoie Lina demain, avec Mathilde. »", 15, "pb2 ic2 er1"),
            R("« Je n'y peux rien, c'est la mère qui a décidé. »", 15, "pb-1 ic-1 em-1"),
            R("« Je peux l'appeler, moi, avec votre accord, pour lui dire que ce n'est pas sa faute ? »", 15, "co2 ic1"),
            R("« Les enfants font souvent des crises, ça passera. »", 15, "em-3 ic-1"),
        ]),
        I(13, "lina", "sad",
          "Lina retourne son dessin. Un bonhomme à moustache pose des carreaux bleus dans une "
          "chambre. « C'est Vovô qui fait le carrelage de ma chambre. » Elle hésite. « Est-ce "
          "qu'il m'entendra encore, quand il sera très, très malade ? »", [
            R("« Oui. Même quand il sera très fatigué, il entendra ta voix. Tu pourras lui "
              "parler, et lui donner ton dessin. »", 15, "co3 em2 cc1"),
            R("« Peut-être. »", 15, "co-1 cc-1"),
            R("« Oui. Et tu pourras le mettre au mur de sa chambre. »", 15, "co2 em1"),
            R("« Non, à la fin, on n'entend plus rien. »", 15, "co-3 cc-1"),
        ]),
        I(14, "carla", "cold-anger",
          "Plus tard, dans le couloir, Carla vous arrête. « Vous lui avez promis. Et si c'est "
          "avant ? Qui va lui expliquer que le docteur avait menti ? »", [
            R("« Vous avez raison. Je n'aurais pas dû. Je retourne le lui dire, avec vous. »",
              13, "pb2 er2 cc1"),
            R("« C'était pour la consoler. »", 15, "pb-2 cc-1"),
            R("« Vous avez raison. Je lui dirai que je ne sais pas, et que je me suis trompé·e. »", 13, "pb2 cc1"),
            R("« Les enfants oublient vite. »", 15, "pb-2 em-3"),
        ]),
        I(15, "mathilde", "neutral",
          "Mathilde Favre passe en fin de journée. « Lina revient demain voir son grand-père. "
          "Qu'est-ce qu'on transmet à l'équipe, pour elle ? »", [
            R("« Les mots exacts qu'on a employés avec elle, ce qu'elle a cru — que c'était sa "
              "faute — et ce qu'on lui a répondu, et qu'elle peut venir quand elle veut. »",
              END, "cc3 ic2 em1"),
            R("« Que l'enfant est informée. »", END, "cc0 ic0"),
            R("« Rien. Moins on en parle, mieux c'est pour elle. »", END, "ic-2 cc-2 em-1"),
            R("« Qu'elle a le droit de poser toutes ses questions, et qu'on lui répond avec les vrais mots. »", -1, "cc2 ic1 rd1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.4 Le mariage
# ---------------------------------------------------------------------------
_MARIAGE_INTRO = (
    "Mardi, 9 h. Joana a pris sa décision cette nuit : la cérémonie religieuse aura lieu "
    "demain, dans la chambre 312. Le prêtre de la paroisse portugaise peut venir à 16 h. "
    "Le mariage civil suivra samedi, à la mairie, sans son père."
)
S4_4 = S(4, "4.4 Le mariage",
    _MARIAGE_INTRO,
    focus=("co", "ic", "rd"),
    entries=[
        Entry(2, when(all=["mariage_rassure"]), _MARIAGE_INTRO),
        Entry(6, when(all=["mariage_anticipe"]), _MARIAGE_INTRO),
    ],
    nodes=[
        I(1, "joana", "anxious",
          "Joana vous attrape au desk, les mots se bousculent. « Demain, 16 h. Ici. Le prêtre "
          "peut venir, Tiago a trouvé un costume. Il faut que papa soit là, même couché. » Elle "
          "vous serre le bras. « Vous m'aidez à convaincre le médecin ? »", [
            R("« On va voir ce qui est possible, et vite. Je parle à l'équipe maintenant : "
              "Inès, le Dr Neuhaus. »", 4, "ic3 co2"),
            R("« Je ne peux rien promettre, ce n'est pas moi qui décide. »", 4, "ic0 co-1"),
            R("« Un hôpital, ce n'est pas vraiment le lieu pour un mariage. »", 5, "co-2 rd-1 em-1"),
            R("« Oui. Dites-moi ce dont vous avez besoin, et je fais le lien avec l'équipe. »", 4, "ic2 co2 cc1"),
            R("« Vous ne pouvez pas attendre septembre ? »", 5, "co-3 cc-2 em-2"),
        ]),
        I(2, "ferreira", "melancholic",
          "M. Ferreira vous fait signe d'approcher. Sa voix n'est plus qu'un souffle. « Vous "
          "vous souvenez ? La première fois. Vous m'aviez dit que septembre, ça devrait "
          "aller. » Ce n'est pas un reproche, et c'est pire. « Joana voulait avancer. Je lui "
          "ai dit que le médecin avait dit que ça irait. »", [
            R("« Je m'en souviens. Je n'aurais pas dû vous dire ça : je ne le savais pas. Je "
              "suis désolé·e. »", 3, "pb3 cc2 er2 rd2"),
            R("« Personne ne pouvait savoir. »", 3, "pb-2 er-1"),
            R("« Je ne me souviens pas d'avoir dit ça. »", 3, "pb-3 cc-3 rd-1"),
            R("Lui prendre la main. « Je me suis trompé·e. Et je suis là, aujourd'hui. »", 3, "pb2 co2 er1"),
            R("« Vous savez, les pronostics, c'est toujours approximatif. »", 3, "pb-2 cc-1"),
        ]),
        I(3, "joana", "anxious",
          "Joana, à la porte, a tout entendu. Elle s'avance. « Alors on le fait demain. Ici. "
          "Le prêtre peut venir à 16 h. » Elle vous regarde. « Vous m'aidez à convaincre le "
          "médecin ? »", [
            R("« Oui. Je parle à l'équipe maintenant : Inès, le Dr Neuhaus. »", 4, "ic3 co2"),
            R("« Je ne peux rien promettre, ce n'est pas moi qui décide. »", 4, "ic0 co-1"),
            R("« Un hôpital, ce n'est pas vraiment le lieu pour un mariage. »", 5, "co-2 rd-1 em-1"),
            R("« Oui. Dites-moi ce dont vous avez besoin, et je fais le lien avec l'équipe. »", 4, "ic2 co2 cc1"),
            R("« Vous ne pouvez pas attendre un peu ? »", 5, "co-3 cc-2 em-2"),
        ]),
        I(4, "neuhaus", "neutral",
          "Neuhaus lève à peine les yeux de son écran. « Un mariage. Au 312. » Il soupire. "
          "« On n'est pas une salle des fêtes, Alex. J'ai vingt-quatre patients, le 310 est en "
          "isolement, et lui ne tient pas assis plus de dix minutes. »", [
            R("« Je comprends. Je te propose un cadre : quinze minutes, six personnes, Inès et "
              "Fatou d'accord, les réserves prêtes s'il s'essouffle. C'est peut-être la "
              "dernière chose qu'il peut faire pour sa fille. »", 7, "ic3 co2 cc2 pb1 er1"),
            R("« Ce serait inhumain de refuser. »", 8, "er-2 ic-2"),
            R("« D'accord, je leur dis que ce n'est pas possible. »", 9, "co-2 ic-1"),
            R("« Je comprends que c'est lourd. Tu veux que je demande d'abord à Inès si c'est faisable ? »", 7, "ic3 er1"),
            R("« Il va mourir, Samuel. Un peu d'humanité. »", 8, "er-3 ic-2 rd-1"),
        ]),
        I(5, "joana", "sad",
          "« Pas le lieu. » Joana a un petit rire mouillé. « Il n'y aura pas d'autre lieu. Il "
          "n'y aura pas de septembre. »", [
            R("« Vous avez raison. Pardon. Je vais voir avec l'équipe comment le rendre "
              "possible. »", 4, "co2 er1 ic1"),
            R("« Je dis juste qu'il y a des règles. »", 4, "co-2 em-1"),
            R("Se taire, et lui tendre un mouchoir. Puis : « Je vais voir ce qu'on peut faire. »", 4, "co2 ic1"),
            R("« Il faudra demander l'autorisation à la direction. »", 4, "co-2 ic-1"),
        ]),
        I(6, "ferreira", "grateful",
          "M. Ferreira vous fait signe d'approcher. « Vous m'aviez dit de ne pas attendre. La "
          "première fois. » Un sourire. « On a avancé à juin. » Il reprend son souffle. « Même "
          "juin, c'était trop loin. Alors on le fait ici. »", [
            R("« Alors faisons-le ici. Je vais voir avec l'équipe. »", 3, "co2 ic2"),
            R("« Je suis désolé·e que même juin soit trop loin. »", 3, "co2 em1"),
            R("« Vous voyez, j'avais raison. »", 3, "co-2 rd-1"),
            R("Lui serrer la main. « On va le faire ici, et ce sera beau. »", 3, "co3"),
        ]),
        I(7, "neuhaus", "neutral",
          "Il vous regarde un long moment, puis hausse les épaules. « Quinze minutes. Et c'est "
          "toi qui gères. Si le 310 sonne, tu y vas. » Il retourne à son écran. « Et demande à "
          "Inès, pas à moi. C'est elle qui sait si c'est faisable. »", [
            R("« Merci. Je vais voir Inès. »", 10, "ic2 co1"),
            R("« Merci, je savais que tu dirais oui. »", 10, "ic-1 er-1"),
            R("« Merci. Je m'occupe du 310 si besoin, promis. »", 10, "ic2 pb1"),
            R("« Tu vois, ce n'était pas si compliqué. »", 10, "ic-2 er-1"),
        ]),
        I(8, "neuhaus", "cold-anger",
          "« Inhumain. » Il pose son stylo. « J'ai quatre entrées prévues cette nuit et j'ai "
          "dormi trois heures. Tu veux parler d'humanité ? »", [
            R("« Pardon. Ce n'était pas juste. Laisse-moi te dire ce qui le rendrait faisable. »",
              4, "er2 ic2"),
            R("Aller voir directement le Dr Moreau.", 11, "ic-2 pb-1"),
            R("« Tu as raison, tu es épuisé. Je te propose une solution qui ne te coûte rien. »", 4, "er2 ic2 em1"),
            R("« Ce n'est pas mon problème. »", 11, "ic-3 er-2"),
        ]),
        I(9, "fatou", "neutral",
          "Fatou vous a entendu·e depuis le chariot. « Vous leur avez dit non ? » Elle secoue "
          "la tête. « Chez moi, on ne refuse pas un mariage à quelqu'un qui s'en va. On pousse "
          "les murs. »", [
            R("« Vous avez raison. Aidez-moi à trouver comment le rendre possible. »", 4, "ic3 co1"),
            R("« Ce n'est pas moi qui décide. »", 12, "ic-1 co-1"),
            R("« Merci, Fatou. Vous voulez bien m'aider à convaincre le Dr Neuhaus ? »", 4, "ic3 rd1"),
            R("« Chez nous, c'est un hôpital. »", 12, "rd-3 ic-2"),
        ]),
        I(10, "ines", "neutral",
          "Inès sourit, pour la première fois depuis des jours. « Faisable. Fatou a déjà des "
          "nappes blanches, ne me demandez pas d'où. Mathilde passe pour la dyspnée. » Puis : "
          "« Et vous, Alex, vous faites quoi pendant la cérémonie ? »", [
            R("« Je reste près de la porte, j'observe sa respiration, et je gère les réserves "
              "avec vous. Ce n'est pas ma fête. »", 12, "pb3 ic2 co1"),
            R("« Je m'assois avec la famille. »", 12, "pb-1 co1"),
            R("« Je pourrais dire quelques mots ? »", 12, "pb-2 rd-1"),
            R("« Je fais ce que vous me direz. C'est votre service. »", 12, "ic3 rd1"),
            R("« Je vais filmer, pour la famille. »", 12, "pb-3 rd-2"),
        ]),
        I(11, "moreau", "cold-anger",
          "Dr Moreau vous écoute, puis secoue la tête. « Vous me demandez de désavouer mon "
          "assistant devant l'équipe. Non. Revenez avec lui, et avec une proposition. »", [
            R("« D'accord. Je retourne le voir avec un plan concret. »", 4, "ic2 er1"),
            R("« Mais c'est urgent ! »", 12, "er-2 ic-1"),
            R("« Vous avez raison. Je retourne voir le Dr Neuhaus et je vous tiens au courant. »", 4, "ic2 er1"),
            R("« Tant pis, alors. »", 12, "co-2 ic-1"),
        ]),
        I(12, "narr", "",
          "Mercredi, 16 h. Des nappes blanches sur la table roulante. Le dessin de Lina scotché "
          "au mur, au-dessus du lit. Joana dans une robe simple, Tiago qui tremble, Carla qui "
          "tient Lina par les épaules. Le prêtre parle portugais, doucement. M. Ferreira, assis "
          "au bord du lit, sous oxygène, tient dix minutes. Quand le prêtre bénit les anneaux, "
          "il pose sa main sur celles de sa fille. À la fin, il vous cherche des yeux et vous "
          "fait signe d'approcher.", [
            R("S'approcher.", 13, "co2 rd1"),
            R("Rester près de la porte.", 13, "er1 pb1"),
            R("Chercher Joana du regard, et lui sourire.", 13, "co2"),
            R("Sortir votre téléphone pour photographier la cérémonie.", 13, "pb-3 rd-2"),
        ]),
        I(13, "ferreira", "grateful",
          "Il vous prend la main. Sa peau est très chaude, très fine. « Vous étiez là le jour "
          "du mot. Vous êtes là aujourd'hui. » Il cherche son souffle. « C'est bien. »", [
            R("« Merci de m'avoir laissé être là. »", END, "co3 er1 rd1"),
            R("« C'est l'équipe qu'il faut remercier. »", END, "ic2 co1"),
            R("« Ce n'est rien, c'est mon travail. »", END, "co-2 er-1"),
            R("Serrer sa main, sans rien dire.", -1, "co3 er1"),
            R("« Vous verrez, vous serez encore là en septembre. »", -1, "cc-3 pb-2 co-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.5 La dernière nuit
# ---------------------------------------------------------------------------
S4_5 = S(5, "4.5 La dernière nuit",
    "Jeudi, 23 h 30. Vous êtes resté·e après votre service : Carla vous a demandé de "
    "passer. L'infirmier de nuit, Kevin Da Silva, vous croise dans le couloir, une "
    "seringue sous-cutanée préparée dans le haricot.",
    focus=("co", "er", "ic", "cc"),
    nodes=[
        I(1, "kevin", "neutral",
          "« T'es encore là, toi ? » Il parle bas. « Le 312 respire mal depuis une heure. Il "
          "est agité. Sa fille est là. Il a des réserves prescrites, morphine et midazolam "
          "sous-cutané. J'appelle Neuhaus pour qu'il passe ? »", [
            R("« Oui, appelle-le. Je vais voir M. Ferreira et sa fille en attendant. »",
              2, "ic3 co2"),
            R("« Donne-les tout de suite, c'est prescrit. »", 3, "pb-2 ic-2"),
            R("« Je rentre, je suis de jour demain. »", 4, "co-2 ic-1"),
            R("« Appelle-le. Je te dis ce que je vois dans la chambre dès que j'y suis. »", 2, "ic3 cc1"),
            R("« Il est en fin de vie, on ne va pas déranger le médecin pour ça. »", 4, "ic-2 co-2 pb-1"),
        ]),
        I(2, "carla", "anxious",
          "La chambre sent l'oxygène et la sueur. M. Ferreira tire sur son masque, les yeux "
          "grands ouverts, chaque inspiration fait un bruit de crécelle. Carla est debout, "
          "affolée. « Il étouffe ! Faites quelque chose ! Appelez la réanimation ! »", [
            R("« Je reste avec vous. Kevin appelle le médecin et prépare les médicaments qui "
              "soulagent l'essoufflement. Votre père a demandé qu'on ne le réanime pas — on va "
              "le soulager, maintenant. »", 5, "cc3 co2 er2 rd1 ic1"),
            R("« Calmez-vous, madame. »", 6, "er-1 em-2"),
            R("Déclencher l'appel de réanimation.", 7, "rd-3 pb-3 ic-1"),
            R("Prendre la main de Carla. « Regardez-moi. On va le soulager. Kevin arrive. »", 5, "co2 er2 cc1"),
            R("« Je ne peux rien faire, je ne suis pas médecin. »", 6, "er-2 co-2 ic-1"),
        ]),
        I(3, "kevin", "cold-anger",
          "Kevin s'arrête net. « Tu me donnes des ordres, là ? Je sais lire une prescription de "
          "réserve. » Un temps. « Ce que je te demande, c'est de venir avec moi dans la "
          "chambre, parce que sa fille est en train de paniquer. »", [
            R("« Pardon. J'arrive. »", 2, "ic2 er1"),
            R("« Je disais ça pour aller plus vite. »", 2, "ic-2 er-1"),
            R("« Tu as raison. Je te suis. »", 2, "ic2 rd1"),
            R("« C'est toi l'infirmier, débrouille-toi. »", 2, "ic-3 rd-2"),
        ]),
        I(4, "carla", "anxious",
          "Vous êtes déjà à l'ascenseur quand Carla sort de la chambre. « Vous partez ? » Sa "
          "voix se casse. « Il a demandé après vous. »", [
            R("Revenir. « Je suis là. »", 2, "co3 er1"),
            R("« Je suis désolé·e, je dois y aller. Kevin est là. »", 13, "co-2 em-2"),
            R("« Je reviens. Dites-moi ce qui se passe. »", 2, "co2 em1"),
            R("« Il n'a pas besoin de moi, il a sa famille. »", 13, "co-3 em-2"),
        ]),
        I(5, "neuhaus", "neutral",
          "Neuhaus arrive en courant, le téléphone de garde à la main. Il confirme la "
          "réserve, Kevin injecte. Neuhaus dit quelques mots à Carla, puis vous prend à part. "
          "« La non-réanimation est au dossier, signée lundi. La fille réclame la réa. Tu peux "
          "rester avec elle ? J'ai deux entrées aux urgences. »", [
            R("« Oui. Je reste. »", 8, "co2 ic2"),
            R("« Je ne suis pas sûr·e d'être à la hauteur. »", 9, "er1 ic1"),
            R("« C'est à toi de lui parler, tu es le médecin. »", 9, "ic-2 co-1"),
            R("« Je reste. Qu'est-ce que je peux lui dire, à propos de la réanimation ? »", 8, "ic2 co1 cc1"),
            R("« Je ne veux pas être seul·e avec ça. »", 9, "er0 ic1"),
        ]),
        I(6, "carla", "angry",
          "« Me calmer ? » Elle vous fait face. « Mon père étouffe, et vous me dites de me "
          "calmer ? »", [
            R("« Pardon. Vous avez raison d'avoir peur. Kevin prépare les médicaments qui "
              "soulagent, le médecin arrive. Je reste avec vous. »", 5, "co2 er2 cc2"),
            R("« Crier ne va pas l'aider. »", 5, "er-2 em-2 co-1"),
            R("Se taire, rester à côté d'elle, et regarder avec elle son père.", 5, "co2 er2"),
            R("« Si vous criez, je sors. »", 5, "er-3 co-2"),
        ]),
        I(7, "kevin", "cold-anger",
          "Kevin vous attrape le poignet avant que vous n'appuyiez. « Attends ! Il est en "
          "non-réanimation, c'est signé depuis lundi. C'est lui qui l'a demandé. »", [
            R("« Tu as raison. Pardon. » Puis, à Carla : « Votre père a demandé qu'on ne le "
              "réanime pas. On va le soulager, maintenant. »", 5, "rd2 er1 cc2"),
            R("« Mais sa fille le demande ! »", 5, "rd-2 er-2"),
            R("Retirer la main de l'appel, et prendre celle de Carla.", 5, "rd2 co2"),
            R("« Tant pis, j'appelle quand même, par sécurité. »", 5, "rd-3 pb-3 ic-1"),
        ]),
        I(8, "carla", "sad",
          "Dix minutes plus tard, M. Ferreira ne tire plus sur son masque. Sa respiration est "
          "plus lente, plus calme, avec de longues pauses. Carla lui tient la main. « Il "
          "respire mieux. » Elle vous regarde. « Est-ce que… c'est maintenant ? »", [
            R("« Je crois que oui, que c'est proche. Vous pouvez lui parler, lui tenir la main. "
              "On pense que l'ouïe reste jusqu'au bout. »", 10, "cc3 co3 em2 rd1"),
            R("« On ne peut pas savoir. »", 10, "cc-1 co-1"),
            R("« Non, ne vous inquiétez pas. Il peut tenir encore des jours. »", 11, "cc-3 co-1 pb-1"),
            R("Lui laisser la chaise la plus proche du lit, et se mettre en retrait.", 10, "co2 rd2"),
            R("« Il faudrait appeler le médecin pour qu'il confirme. »", 10, "cc-1 co-1"),
        ]),
        I(9, "neuhaus", "neutral",
          "Neuhaus s'arrête dans l'embrasure. « Personne n'est à la hauteur. » Il a l'air "
          "très jeune, tout à coup. « Tu n'as rien à faire. Être là. C'est tout. »", [
            R("« D'accord. Je reste. »", 8, "co2 er2"),
            R("« Je reste, mais appelle-moi si tu as besoin. »", 8, "co1 ic1"),
            R("« Merci. Ça m'aide de l'entendre. »", 8, "er2 ic1"),
            R("« Facile à dire, tu t'en vas. »", 8, "er-2 ic-2"),
        ]),
        I(10, "carla", "sad",
          "« Joana doit venir. » Elle cherche son téléphone. « Et Lina ? Je la réveille ? Elle "
          "est chez la voisine. »", [
            R("« Appelez Joana. Pour Lina, c'est vous qui savez — certains enfants veulent dire "
              "au revoir, d'autres non. Il n'y a pas de mauvais choix. »", 12, "rd2 em2 cc2"),
            R("« Laissez dormir la petite. »", 12, "pb-1 rd-1"),
            R("« Vous voulez que j'appelle Joana pour vous, pendant que vous restez avec lui ? »", 12, "ic1 co2"),
            R("« Il vaut mieux que la petite voie ça, pour faire son deuil. »", 12, "rd-2 pb-2"),
        ]),
        I(11, "kevin", "cold-anger",
          "Dans le couloir, Kevin vous rattrape. « Tu ne peux pas lui dire ça. » Il parle très "
          "bas. « Il est en train de mourir. Elle a besoin de le savoir pour appeler sa "
          "sœur. »", [
            R("Retourner dans la chambre. « Carla, je me suis trompé·e. Je crois que c'est "
              "proche. Si vous voulez appeler votre sœur, c'est le moment. »", 10, "cc2 pb2 co1"),
            R("« Je ne voulais pas lui faire peur. »", 10, "pb-1 cc-1"),
            R("« Tu as raison. Merci de me l'avoir dit. »", 10, "pb2 ic1"),
            R("« Je ne vais pas lui enlever son dernier espoir. »", 10, "pb-3 cc-2"),
        ]),
        I(12, "narr", "",
          "Joana arrive à 1 h 15, en pyjama sous son manteau. Les deux sœurs s'assoient de "
          "chaque côté du lit. Kevin a baissé la lumière. Les pauses entre les respirations "
          "s'allongent. À 1 h 40, la suivante ne vient pas. Carla vous regarde : « C'est "
          "fini ? »", [
            R("« Oui. Il est mort. Il est parti calmement, avec vous deux. »", 14, "cc3 co3 rd1 em1"),
            R("« Il est parti. »", 14, "cc0 co1"),
            R("« Il faut attendre que le médecin constate le décès. »", 14, "cc-1 co-2"),
            R("Poser doucement la main sur l'épaule de Carla, sans rien dire.", 14, "co3 er1"),
            R("« C'est mieux comme ça, il ne souffre plus. »", 14, "co-2 cc-1 rd-1"),
        ]),
        I(13, "narr", "",
          "Vous rentrez à vélo, sous la pluie. À 6 h 30, un message d'Inès : « M. Ferreira est "
          "décédé cette nuit à 1 h 40. Ses deux filles étaient là. Il a demandé après vous "
          "vers minuit. »", []),
        I(14, "carla", "sad",
          "Joana pleure contre l'épaule de sa sœur. Carla, elle, ne pleure pas encore. Kevin "
          "entrouvre la fenêtre, sans un mot. Carla vous regarde. « Vous… vous restez un "
          "peu ? »", [
            R("« Je reste un moment, oui. Prenez le temps qu'il vous faut, rien ne presse. »",
              15, "co3 er1"),
            R("« Je dois rentrer, il est tard. »", 15, "co-2"),
            R("« Je reste. Voulez-vous que je vous laisse un moment seules avec lui, d'abord ? »", 15, "co2 rd2"),
            R("« Il faut que Kevin fasse les soins, vous devriez sortir. »", 15, "rd-3 co-2"),
        ]),
        I(15, "kevin", "neutral",
          "2 h 30, dans le couloir. Kevin vous tend un gobelet d'eau. « Ton premier ? » Vous "
          "hochez la tête. « Rentre en taxi, pas à vélo. Et demain, tu en parles à "
          "quelqu'un. »", [
            R("« Merci, Kevin. Et toi, tu tiens comment, avec toutes ces nuits ? »", END, "ic2 em2 er1"),
            R("« Ça va, je gère. »", END, "er-2"),
            R("« Je reste jusqu'au matin, de toute façon je ne dormirai pas. »", END, "er-2 pb-1"),
            R("« Je vais prendre un taxi. Merci d'être resté avec moi. »", -1, "er2 ic1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4.6 Le matin d'après
# ---------------------------------------------------------------------------
S4_6 = S(6, "4.6 Le matin d'après",
    "Vendredi, 8 h. Vous avez dormi deux heures. Chambre 312, la porte est fermée, un "
    "petit panneau accroché à la poignée. Fatou Diallo est à l'intérieur avec une bassine "
    "d'eau tiède.",
    focus=("er", "ic", "co", "pb"),
    nodes=[
        I(1, "fatou", "sad",
          "« Vous êtes venu·e ? Après cette nuit ? » Elle trempe un gant dans l'eau. « Je fais "
          "sa toilette. Chez moi, on ne laisse partir personne sale. » Un temps. « Vous voulez "
          "m'aider ? Les étudiants ne le font jamais. »", [
            R("« Oui, si la famille est d'accord. Montrez-moi. »", 2, "co3 rd2 ic2 er1"),
            R("« Je ne suis pas sûr·e d'en être capable. »", 3, "er1"),
            R("« Ce n'est pas vraiment mon travail. »", 4, "rd-2 ic-2 co-1"),
            R("« Je peux commencer par vous regarder faire ? »", 3, "rd2 ic1"),
            R("« Les pompes funèbres ne s'en occupent pas ? »", 4, "rd-2 co-2 ic-1"),
        ]),
        I(2, "fatou", "neutral",
          "Elle lui parle comme s'il dormait. « On va vous mettre votre veste, M. Ferreira. "
          "Celle du premier jour, celle que vous mettiez sur le pyjama. » Elle vous tend la "
          "veste. « Vous lui parlez, vous aussi ? »", [
            R("« Au revoir, M. Ferreira. Merci. »", 5, "co3 rd2"),
            R("L'aider en silence.", 5, "rd1 co1"),
            R("« Il ne peut plus entendre. »", 5, "rd-2 co-2"),
            R("Lui mettre la veste avec soin, en fermant les boutons un à un.", 5, "rd3 co1"),
        ]),
        I(3, "fatou", "neutral",
          "« Personne n'est capable la première fois. » Elle vous regarde par-dessus ses "
          "lunettes. « Vous pouvez juste lui tenir la main pendant que je fais. »", [
            R("S'approcher, et prendre sa main.", 2, "co2 er2"),
            R("« Je préfère attendre dehors. »", 6, "er0 co-1"),
            R("« D'accord. Je veux bien apprendre. »", 2, "ic2 er1"),
            R("« Non, vraiment, je n'y arrive pas. »", 6, "er-1"),
        ]),
        I(4, "fatou", "cold-anger",
          "« Pas votre travail. » Elle essore le gant. « C'était le mien pendant trente ans, "
          "et personne ne me l'a jamais appris non plus. »", [
            R("« Pardon. Je peux rester ? »", 2, "rd2 ic2"),
            R("Sortir.", 6, "ic-1 co-1"),
            R("« Vous avez raison. Montrez-moi. »", 2, "rd2 ic2"),
            R("« C'est pour ça qu'il y a des aides-soignantes. »", 6, "rd-3 ic-3"),
        ]),
        I(5, "carla", "sad",
          "La porte s'ouvre. Carla, et Lina, un rouleau de papier à la main. Lina s'approche de "
          "vous, pas du lit. « C'est pour toi. » Le dessin des carreaux bleus. « Maman dit que "
          "t'étais là. »", [
            R("S'accroupir à sa hauteur. « Merci, Lina. Il est très beau. Ton Vovô parlait "
              "souvent de toi. »", 7, "co3 em2"),
            R("« Merci. »", 7, "co1"),
            R("« Tu devrais le garder pour toi. »", 7, "em-2 co-1"),
            R("« Je vais le garder toute ma vie. »", 7, "co3"),
        ]),
        I(6, "ines", "neutral",
          "Dans le couloir, Inès Rey vous tend un café. « Vous avez dormi ? »", [
            R("« Deux heures. Et je n'arrête pas de revoir la dernière respiration. »", 8, "er3 ic1"),
            R("« Oui, ça va. »", 8, "er-2"),
            R("« Pas vraiment. Et vous, cette nuit, ça a été ? »", 8, "er2 ic2"),
            R("« Qu'est-ce que ça peut vous faire ? »", 8, "ic-3 er-2"),
        ]),
        I(7, "carla", "neutral",
          "Carla regarde son père, habillé de sa veste. « La première semaine, vous m'aviez dit "
          "que c'était lui qui décidait. Ça m'avait énervée. » Elle sourit à peine. « Il a "
          "décidé jusqu'au bout. »", [
            R("« Et vous l'avez laissé faire. Ce n'était pas facile. »", 8, "em2 co2 rd1"),
            R("« Je suis content·e que ça se soit bien passé. »", 8, "co0 em-1"),
            R("« Et vous l'avez accompagné. Il était fier de vous, vous savez. »", 8, "co2 em2"),
            R("« C'est la loi, de toute façon. »", 8, "em-2 rd-1"),
        ]),
        I(8, "moreau", "neutral",
          "Dr Moreau vous fait signe. Son bureau, porte fermée. « Premier décès. » Ce n'est "
          "pas une question. « Comment ça va, vraiment ? »", [
            R("« Je n'arrive pas à savoir si je suis triste ou soulagé·e pour lui. Et je n'ai "
              "presque pas dormi. »", 9, "er3 ic1"),
            R("« Bien. C'était attendu. »", 10, "er-2"),
            R("« Vide. Et en même temps je voudrais revenir ce soir. »", 9, "er2"),
            R("« Il faut que je vous parle de ma nuit du 14, j'en ai deux d'affilée. »", 9, "pb2 er1 ic1"),
        ]),
        I(9, "moreau", "neutral",
          "« Les deux à la fois. C'est normal, et ça ne passe pas en un jour. » Dr Moreau "
          "griffonne un numéro. « La psychologue du personnel. Pas parce que vous allez mal : "
          "parce que vous allez recommencer. Et cet après-midi, vous êtes en congé. C'est un "
          "ordre. »", [
            R("« Merci. Je l'appellerai. »", 11, "er2 ic2"),
            R("« Je n'en ai pas besoin, mais merci. »", 11, "er-1"),
            R("« Merci. Et je voudrais vous parler de ma garde de la semaine prochaine. »", 11, "er2 pb1"),
            R("« Les psys, c'est pour ceux qui n'y arrivent pas. »", 11, "er-3 ic-1"),
        ]),
        I(10, "moreau", "neutral",
          "« Attendu, oui. Et c'est quand même quelqu'un qui est mort dans vos bras. » Dr "
          "Moreau vous regarde longuement. « Cet après-midi, vous êtes en congé. C'est un "
          "ordre. »", [
            R("« D'accord. Merci. »", 11, "er1 ic1"),
            R("« Je préfère travailler. »", 11, "er-2 pb-1"),
            R("« Vous avez raison. Je n'ai pas dormi. »", 11, "er2"),
            R("« Merci. Est-ce que je peux quand même vous parler de ma semaine prochaine ? »", 11, "pb2 er1"),
        ]),
        I(11, "jonas", "anxious",
          "Au vestiaire, Jonas vous attend. « J'ai appris pour le 312. Désolé. » Il se gratte "
          "la nuque. « Écoute, c'est nul de demander maintenant, mais… tu pourrais prendre ma "
          "nuit du 13 ? Mercredi. C'est l'anniversaire de ma copine. Tu as déjà celle du 14, "
          "t'enchaînes, tu récupères le week-end. »", [
            R("« Je ne peux pas, Jonas. Deux nuits d'affilée après cette semaine, ce n'est pas "
              "raisonnable — ni pour moi, ni pour les patients. Demande à quelqu'un d'autre, ou "
              "on voit avec le planning. »", 12, "pb3 er2 cc1"),
            R("« OK, pas de souci. »", 13, sets=["nuits_enchainees"], scores="pb-2 er-2"),
            R("« Je prends. Mais tu me dois une fière chandelle. »", 13,
              sets=["nuits_enchainees"], scores="pb-2 er-1"),
            R("« Demande au planning, ils trouveront. Et toi, ça va ? »", 12, "pb2 er1 em1"),
            R("« Je ne sais pas… Laisse-moi voir si je tiens le coup d'ici mercredi. »", 13, "pb-1 er-1", sets=["nuits_enchainees"]),
            R("« Carrément. De toute façon, je ne dors plus. »", 13, "pb-3 er-3", sets=["nuits_enchainees"]),
        ]),
        I(12, "jonas", "sad",
          "« Ouais. T'as raison. Je demande à Léo. » Il reste planté là. « Et toi, ça va ? Le "
          "312, c'était ton patient. »", [
            R("« Pas vraiment. Je vais au débriefing d'Inès ce soir. Viens. »", END, "er2 ic2 em1"),
            R("« Ça va. »", END, "er-1"),
            R("« Non. Tu viens au débriefing avec moi ? »", -1, "er2 ic2"),
            R("« T'occupe. »", -1, "er-2 ic-1"),
        ]),
        I(13, "narr", "",
          "Dans votre agenda, deux croix rouges : nuit du mercredi 13, nuit du jeudi 14. Entre "
          "les deux, sept heures de récupération — en théorie.", []),
    ],
)

CH4 = C(4, "Ceux qui restent",
    situation=(
        "Cinquième semaine. M. Ferreira revient, très affaibli, et demande à Alex de l'aider "
        "à dire qu'il veut arrêter. Autour de lui : deux filles qui ne veulent pas la même "
        "chose, une petite-fille qui pose les questions que personne n'ose poser, un mariage "
        "qui ne peut plus attendre, et une équipe qui pousse les murs."
    ),
    objectives=(
        "accompagner un patient qui décide d'arrêter un traitement sans décider à sa place "
        "ni seul·e, distinguer arrêt des traitements et arrêt des soins, conduire une "
        "réunion de famille en rendant la parole au patient, parler de la mort à une enfant "
        "avec le parent et sans mentir, négocier avec l'équipe un projet qui a du sens pour "
        "le patient, accompagner une agonie et les proches dans le respect d'une décision de "
        "non-réanimation, et reconnaître ses propres limites de fatigue."
    ),
    anchoring=(
        "UNIL M1.6 cours-blocs (communication) et M1.7 éthique de la décision · UNIGE M1 AMC "
        "Médecine interne et médecine palliative, AMC Pédiatrie (communication avec "
        "l'enfant), enseignement interprofessionnel."
    ),
    focus=("co", "ic", "cc", "rd"),
    scenes=[S4_1, S4_2, S4_3, S4_4, S4_5, S4_6],
)
