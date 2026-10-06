"""Chapitre 1 — Les mots qu'on n'a pas appris (semaine 1)."""
from __future__ import annotations

from .dsl import END, C, I, R, S

# ---------------------------------------------------------------------------
# 1.1 Premier matin — nouvelle scène
# ---------------------------------------------------------------------------
S1_1 = S(1, "1.1 Premier matin",
    "Lundi, 7 h 30, 3ᵉ étage, médecine interne. Premier jour de stage. Le Dr Neuhaus, "
    "médecin assistant, a deux cafés à la main et vingt-quatre patients sur sa liste. "
    "Le tour commence dans dix minutes.",
    focus=("ic", "rd", "pb"),
    nodes=[
        I(1, "neuhaus", "happy",
          "« Alex ? Samuel Neuhaus, assistant. Bienvenue au 3ᵉ. Ici tout le monde se tutoie, "
          "sauf le chef. » Il vous tend un des cafés. « Tu prends les chambres 308 à 312 avec "
          "moi. Tour dans dix minutes. Des questions ? »", [
            R("« Une seule : qui est l'infirmière référente de ces chambres ? J'aimerais me "
              "présenter avant le tour. »", 2, "ic3 rd1 pb1 cc1"),
            R("« Aucune, je te suis. »", 3, "er1"),
            R("« Je peux avoir les patients les plus intéressants ? Il me manque des gestes "
              "pour mon carnet de stage. »", 4, "rd-2 pb-1 ic-1"),
            R("« Juste une : qu'est-ce que tu attends de moi, concrètement, pendant le tour ? »", 3, "cc2 ic1 pb1"),
            R("Hocher la tête sans rien dire et partir chercher une blouse.", 3, "ic-1 cc-1"),
            R("« Dix minutes ? Je descends prendre un vrai café, je vous rejoins. »", 3, "ic-2 pb-2 rd-1"),
        ]),
        I(2, "ines", "neutral",
          "L'infirmière lève les yeux de son chariot. « Inès Rey. Référente du 308 au 316. » "
          "Un temps. « Les étudiants se présentent rarement avant de débarquer dans mes "
          "chambres. Vous savez ce qu'on attend de vous au tour ? »", [
            R("« Pas vraiment. Qu'est-ce qui vous aiderait, vous ? »", 5, "ic3 rd1 em1 pb1"),
            R("« Présenter mes patients et proposer une conduite à tenir. »", 5, "cc1 pb1"),
            R("« Le Dr Neuhaus m'a briefé·e, ça devrait aller. »", 6, "ic-2 rd-1"),
            R("« J'allais justement vous demander ce que vous savez des patients avant le tour. »", 5, "ic3 rd1"),
            R("« Je suis là pour apprendre la médecine, pas le fonctionnement infirmier. »", 6, "ic-3 rd-3 pb-1"),
        ]),
        I(3, "jonas", "happy",
          "Jonas, votre co-stagiaire, surgit en enfilant sa blouse. « Salut ! T'as vu la "
          "liste ? Le carreleur du 312, masse pulmonaire. J'espère que c'est un cancer, j'ai "
          "jamais vu d'annonce. » Le rideau du 312 est à trois mètres.", [
            R("« Il s'appelle M. Ferreira. Et il est à trois mètres, derrière un rideau. »",
              7, "rd3 pb2 er1"),
            R("Rire à moitié. « T'es terrible. »", 7, "rd-2 pb-2"),
            R("Ne rien dire, et changer de sujet.", 7, "rd-1"),
            R("Baisser la voix : « Pas ici. On en parle au vestiaire si tu veux. »", 7, "rd2 pb1 ic1"),
            R("« Moi aussi. Paraît que c'est formateur, les annonces. »", 7, "rd-3 pb-2 em-2"),
        ]),
        I(4, "neuhaus", "neutral",
          "Il sourit sans que ce soit une approbation. « Les plus intéressants. Ici, tous les "
          "patients sont intéressants — pour eux-mêmes. » Il boit une gorgée. « Mais "
          "d'accord, tu veux des gestes. Qui te les apprend, à ton avis ? »", [
            R("« Les infirmières, pour beaucoup. Je vais me présenter à la référente. »",
              2, "ic3 rd1 pb1"),
            R("« Toi, j'imagine. »", 3, "ic-1"),
            R("« Je me débrouillerai, j'ai fait des stages. »", 3, "ic-2 pb-1 er-1"),
            R("« Les patients, d'abord. Ils nous apprennent ce qu'on ne sait pas encore. »", 3, "rd2 pb1"),
            R("« Peu importe, du moment que je coche mes cases. »", 3, "rd-2 pb-2 ic-1"),
        ]),
        I(5, "ines", "neutral",
          "« Ce qui m'aiderait ? Que vous lisiez les transmissions infirmières avant le tour, "
          "pas après. Et que vous ne disiez jamais à un patient « on verra avec "
          "l'infirmière » sans m'en parler. » Elle vous tend une feuille. « Le 312 n'a pas "
          "dormi. »", [
            R("« Je les lis maintenant. Qu'est-ce qui l'a empêché de dormir ? »", 6, "ic2 em2 cc1"),
            R("« D'accord, merci. »", 6, "ic1"),
            R("« Je n'aurai pas le temps avant le tour, je les lirai après. »", 6, "ic-2 pb-1"),
            R("« Promis. Et si un patient me demande quelque chose qui vous concerne, je vous le dis. »", 6, "ic3 cc1 rd1"),
            R("« Les transmissions infirmières, je les lis rarement : c'est surtout pour vous. »", 6, "ic-3 rd-2"),
        ]),
        I(6, "fatou", "neutral",
          "Dans le couloir, une ASSC vous arrête à voix basse. « Vous êtes le nouvel "
          "étudiant·e ? Fatou. » Elle désigne le 312 du menton. « Le monsieur ne mange plus "
          "depuis deux jours. Il dit que c'est la nourriture. Moi je crois qu'il a peur. »", [
            R("« Merci de me le dire. Qu'est-ce qui vous fait penser ça ? »", 8, "ic3 em2 rd1"),
            R("« Je le noterai. »", 8, "ic0 cc1"),
            R("« Vous pouvez le mettre dans les transmissions, s'il vous plaît ? »", 8, "ic-2 rd-1"),
            R("« Peur de quoi, à votre avis ? Il vous a dit quelque chose ? »", 8, "em2 ic2"),
            R("« Il est peut-être juste difficile avec la nourriture. »", 8, "em-2 ic-1 rd-1"),
        ]),
        I(7, "neuhaus", "neutral",
          "Neuhaus claque des doigts. « Le tour, les enfants. » Au passage, une ASSC glisse "
          "quelque chose à Jonas, qui hausse les épaules. « Elle dit que le 312 ne mange "
          "plus. Bof. »", [
            R("Rattraper l'ASSC. « Pardon — vous pouvez me redire ce que vous avez remarqué ? »",
              8, "ic3 em1 rd1"),
            R("« Ça vaut peut-être la peine de le signaler au tour. »", 9, "ic1 cc1"),
            R("Suivre Neuhaus sans s'arrêter.", 9, "ic-2 em-1"),
            R("« Jonas, c'est elle qui le voit manger trois fois par jour. On l'écoute. »", 8, "ic3 rd1 pb1"),
        ]),
        I(8, "fatou", "neutral",
          "« Il pose sa fourchette dès que quelqu'un parle de ses examens. Et cette nuit il a "
          "demandé à ma collègue si on mourait vite, d'une tache au poumon. » Elle hausse les "
          "épaules. « Les gens me disent des choses. Personne ne me les demande. »", [
            R("« Moi, je vous les demande. Je le dirai au tour, en citant vos mots. »",
              9, "ic3 rd2 cc1"),
            R("« C'est important, merci. »", 9, "ic1"),
            R("Noter ses mots exacts dans votre carnet, devant elle.", 9, "ic2 cc2 rd1"),
            R("« Vous savez, les patients disent beaucoup de choses la nuit. »", 9, "ic-2 em-2 rd-1"),
        ]),
        I(9, "narr", "",
          "Chambre 312, chambre double. Le voisin de M. Ferreira a baissé le son de sa "
          "télévision. Neuhaus parcourt l'écran de l'ordinateur mobile. « Alors, M. Ferreira, "
          "le scanner montre une masse assez importante au poumon droit, on attend encore des "
          "éléments. » M. Ferreira se redresse. « Une masse. C'est un cancer, docteur ? » "
          "Neuhaus se tourne vers vous : « Alex, tu veux répondre ? »", [
            R("« Monsieur Ferreira, c'est une vraie question, et elle mérite mieux qu'une "
              "chambre à deux lits. On revient vous voir aujourd'hui, dans un endroit calme, "
              "avec des éléments complets. »", 10, "rd3 pb2 cc2 em2"),
            R("« On ne sait pas encore, il faut attendre les résultats. »", 11, "cc-1 rd0"),
            R("« C'est probable, oui, mais le médecin vous expliquera. »", 12, "rd-3 pb-3 cc-2"),
            R("Regarder Neuhaus : « Je crois que c'est au Dr Neuhaus de vous répondre. »", 11, "pb1 cc-1"),
            R("« Non, ne vous inquiétez pas, c'est sûrement une infection. »", 11, "cc-3 pb-2 rd-2"),
        ]),
        I(10, "ferreira", "anxious",
          "Il regarde son voisin, puis vous. « Aujourd'hui. » Il pose la main sur la "
          "couverture. « Vous promettez ? »", [
            R("« Je vais tout faire pour, et si ce n'est pas possible, je reviens vous dire "
              "pourquoi avant midi. »", 13, "cc3 rd2 pb2"),
            R("« Promis. »", 13, "cc0 pb-1"),
            R("Regarder Neuhaus sans répondre.", 13, "rd-1 cc-1 ic-1"),
            R("« Je ne peux pas promettre à la place du médecin. Mais je vous promets de revenir vous dire où on en est. »", 13, "cc3 pb2 rd1"),
            R("« On verra, ça dépend du planning. »", 13, "cc-2 rd-1 em-1"),
        ]),
        I(11, "ferreira", "suspicious",
          "Il hoche la tête lentement, comme quelqu'un qui a entendu cette phrase trop "
          "souvent. « Attendre. » Il se rallonge et tourne la tête vers la fenêtre.", [
            R("« Je vois que la réponse ne vous suffit pas. On reviendra vous en parler "
              "aujourd'hui, pas entre deux lits. »", 13, "rd2 em2 cc1"),
            R("Passer au patient suivant.", 13, "em-1 rd-1"),
            R("Rester un instant près du lit : « Je repasse vous voir avant midi. »", 13, "em2 rd1 cc1"),
            R("« Vous savez, attendre, c'est aussi ça, l'hôpital. »", 13, "em-2 rd-2"),
        ]),
        I(12, "neuhaus", "cold-anger",
          "Dans le couloir, Neuhaus vous attrape par la manche. « Tu viens d'annoncer un "
          "probable cancer à un patient, sans résultat, devant son voisin de chambre. » Il "
          "baisse la voix. « Il va passer la journée avec ça. »", [
            R("« Tu as raison. Qu'est-ce que je peux faire pour réparer, maintenant ? »",
              13, "pb2 er2 ic2"),
            R("« Il a posé la question, je n'allais pas lui mentir. »", 13, "pb-1 er-1"),
            R("« C'est toi qui m'as demandé de répondre. »", 13, "ic-2 er-2 pb-1"),
            R("« Je vais lui dire que je me suis avancé·e, et qu'on reviendra avec de vraies réponses. »", 13, "pb2 cc2 er1"),
            R("« Il fallait bien que quelqu'un le lui dise. »", 13, "pb-2 er-1 rd-1"),
        ]),
        I(13, "ines", "neutral",
          "Inès Rey vous attend au bout du couloir, bras croisés. « Il paraît que le 312 aura "
          "une réponse aujourd'hui. » Ce n'est pas un reproche, pas encore. « Qui la donne, "
          "quand, et est-ce que je suis dedans ? C'est moi qui serai là quand vous serez "
          "parti·e. »", [
            R("« Je ne sais pas encore qui la donne. Mais je veux que vous soyez dans la "
              "pièce, et je vous tiens au courant dès que c'est décidé. »", 14, "ic3 cc2 pb1"),
            R("« Je demande au Dr Neuhaus et je reviens vers vous. »", 14, "ic1 cc1"),
            R("« C'est une décision médicale, on vous dira. »", 14, "ic-3 rd-2 pb-1 cc-1"),
            R("« Vous le connaissez mieux que nous. Vous voulez être là quand on lui parle ? »", 14, "ic3 rd2"),
        ]),
        I(14, "moreau", "neutral",
          "Une voix derrière vous. « C'est vous, Alex ? » Dr Moreau, le médecin-chef. « Le "
          "bilan de M. Ferreira vient d'être validé. Je voulais vous en parler après le "
          "colloque — mais j'entends qu'il y a déjà eu des engagements pris au tour. » Un "
          "sourire bref. « Racontez-moi. »", [
            R("Résumer honnêtement : la question du patient, la réponse donnée, ce que Fatou "
              "et Inès ont signalé.", END, "cc3 ic2 pb2"),
            R("« Rien de spécial, le patient voulait savoir. »", END, "cc-1 ic-1"),
            R("« Le Dr Neuhaus vous expliquera mieux que moi. »", END, "ic-1 pb-1 cc-1"),
            R("« J'ai répondu trop vite au tour. Je préfère vous le dire avant que vous l'appreniez par quelqu'un d'autre. »", -1, "pb3 er1 cc1"),
            R("« Tout va bien, c'est sous contrôle. »", -1, "cc-2 pb-2"),
        ]),
    ],
)

# Reprise de la v1 : scène 1.1 Avant d'entrer
S1_2 = S(2, "1.2 Avant d'entrer",
    "Le bilan de M. Ferreira est validé : adénocarcinome pulmonaire avec lésions hépatiques. Dr Moreau propose à Alex de mener l'annonce. Tout se joue avant d'ouvrir la porte — ce qu'on sait, ce que le patient sait, qui doit être là, et où l'on parle.",
    focus=("cc", "ic", "er"),
    nodes=[
        I(1, "moreau", "neutral", "« Le bilan de M. Ferreira est revenu. Adénocarcinome pulmonaire, avec des lésions hépatiques. Je vous propose de mener l'annonce cet après-midi — je serai dans la pièce, je n'interviendrai que si vous me le demandez. »", [
            R("« D'accord. Est-ce que je peux relire le dossier et préparer avec vous avant d'y aller ? »", 2, "rd1 er1 cc2 pb2 ic1"),
            R("« Oui bien sûr, j'y vais tout de suite, autant ne pas le faire attendre. »", 3, "er-1 cc-1 pb-1"),
            R("« Je préfère que vous le fassiez. Je ne me sens pas prêt·e pour ça. »", 4, "er-1 pb1"),
            R("« Oui. Est-ce qu'Inès Rey peut être là, elle aussi ? »", 2, "ic3 rd1 cc1"),
            R("« Pourquoi moi ? C'est vous le médecin-chef. »", 4, "er-1 ic-1 pb-1"),
        ]),
        I(2, "moreau", "neutral", "« Bon réflexe. Alors dites-moi : avant d'entrer dans une chambre pour annoncer ça, qu'est-ce que vous devez savoir ? »", [
            R("« Ce qui lui a déjà été dit, ce qu'il en a compris, et ce qu'on peut lui proposer comme suite concrète. »", 5, "em1 cc3 pb2"),
            R("« Le stade exact, le protocole et les chiffres de survie. Il va me les demander. »", 5, "em-1 cc1 pb1"),
            R("« Honnêtement ? Surtout qu'il ne s'effondre pas devant moi. »", 5, "em1 er-1"),
            R("« S'il veut savoir, et jusqu'où. Certains patients ne veulent pas tout entendre d'un coup. »", 5, "rd2 cc2"),
            R("« Rien de spécial, j'improviserai selon sa réaction. »", 5, "cc-2 pb-2"),
        ]),
        I(3, "moreau", "cold-anger", "Dr Moreau vous retient. « Attendez. Une annonce qu'on improvise, le patient s'en souvient toute sa vie. Asseyez-vous deux minutes. »", [
            R("« Vous avez raison. Je reprends le dossier depuis le début. »", 2, "er1 cc1 pb1 ic1"),
            R("« Je connais le dossier, j'étais au colloque ce matin. »", 5, "er-1 cc-1 pb-2 ic-1"),
            R("« D'accord. Qu'est-ce que je dois regarder en premier ? »", 2, "ic2 er1 pb1"),
            R("« Il attend depuis ce matin, c'est cruel de le faire attendre encore. »", 5, "em1 pb-2 cc-1"),
        ]),
        I(4, "moreau", "neutral", "« Je peux la faire, évidemment. Mais vous serez médecin dans deux ans, et personne ne se sent prêt la première fois. Qu'est-ce qui vous arrête exactement ? »", [
            R("« La peur de dire une bêtise irrattrapable. J'aimerais qu'on prépare ensemble, et que vous repreniez la main si je bloque. »", 2, "er2 cc2 pb2 ic2"),
            R("« Rien. Laissez tomber, j'y vais. »", 3, "er-2 cc-1"),
            R("« Je n'ai jamais vu quelqu'un mourir. Je ne sais pas de quoi je parle. »", 2, "em1 er1 pb1"),
            R("« Qu'il me pose une question à laquelle je ne sais pas répondre. »", 2, "er2 cc1"),
        ]),
        I(5, "moreau", "neutral", "Vous ouvrez le dossier. Bilan d'extension complet, avis oncologique en attente, consultation prévue demain. « Qu'est-ce que vous en retenez pour cet après-midi ? »", [
            R("« Que je peux nommer la maladie et son extension, mais pas encore le traitement. Je dirai ce que je sais et j'assumerai ce que je ne sais pas. »", 6, "er2 cc3 pb3"),
            R("« Qu'on peut déjà lui parler de chimiothérapie, c'est ce qui se fait dans ces cas-là. »", 6, "cc-2 pb-3"),
            R("« Qu'il vaut mieux attendre demain et l'avis de l'oncologue pour tout dire d'un coup. »", 6, "rd-2 em-1 cc-1 pb-1"),
            R("« Que je ne sais pas encore ce qu'on lui proposera, et que je dois le lui dire franchement. »", 6, "cc2 pb2"),
            R("« Que c'est trop tôt pour moi, je préfère laisser l'oncologue faire. »", 6, "er-1 pb-1 ic-1"),
        ]),
        I(6, "ines", "neutral", "L'infirmière référente vous croise dans le couloir. « Vous allez voir M. Ferreira ? Sa fille aînée arrive à 16 h. Et il a très mal dormi cette nuit, il m'a parlé à 3 h du matin. »", [
            R("« Ah, ça change des choses. Qu'est-ce qu'il vous a dit cette nuit ? »", 7, "rd1 em2 cc2 ic3"),
            R("« Merci, je note pour 16 h. On y va maintenant, c'est calé avec le Dr Moreau. »", 8, "cc1 pb1"),
            R("« C'est une décision médicale, on gère. »", 9, "rd-2 pb-2 ic-3"),
            R("« Il vous a dit quelque chose d'important cette nuit ? Je vous écoute. »", 7, "ic3 em1"),
            R("« Sa fille à 16 h ? On attendra qu'elle soit là pour tout dire d'un coup. »", 8, "rd-2 pb-2"),
        ]),
        I(7, "ines", "neutral", "« Il m'a demandé si ça pouvait être une tumeur. Textuellement. Et il m'a dit qu'il n'osait pas poser la question au médecin pour ne pas déranger. »", [
            R("« Donc la question est déjà là. Je vais partir de ça plutôt que de lui tomber dessus. Vous pouvez être présente à l'entretien ? »", 10, "rd2 em2 cc3 ic3"),
            R("« Parfait, ce sera plus facile alors, il s'y attend déjà. »", 10, "em-1 ic1"),
            R("« Il aurait dû nous le dire directement plutôt que de vous réveiller la nuit. »", 10, "rd-1 em-2 ic-2"),
            R("« Merci. Je lui demanderai d'abord ce qu'il pense, avant de dire quoi que ce soit. »", 10, "cc2 em1 ic1"),
            R("« Tant mieux, ça m'évitera de trop expliquer. »", 10, "em-2 cc-1"),
        ]),
        I(8, "ines", "resigned", "Elle hausse les épaules. « Comme vous voulez. » Elle hésite, puis ajoute : « Il m'a quand même parlé de ses craintes cette nuit, mais bon, ce n'est pas mon rôle. »", [
            R("« Non, attendez, c'est exactement votre rôle et ça m'intéresse. Qu'est-ce qu'il a dit ? »", 7, "rd2 em2 er2 cc2 ic3"),
            R("« On fera le point après l'entretien. »", 10, "em-1 ic-1"),
            R("« Pardon, je vous ai coupée. Ses craintes, c'était quoi ? »", 7, "ic2 er1 em1"),
            R("« Vous me direz ça aux transmissions. »", 10, "ic-2 em-1"),
        ]),
        I(9, "ines", "angry", "Elle se fige. « Très bien. Mais c'est moi qui resterai dans la chambre ce soir, quand vous serez rentré·e chez vous. »", [
            R("« Vous avez raison et je me suis mal exprimé·e. Je ne peux pas annoncer ça sans l'équipe qui va porter la suite. Qu'est-ce qu'il vous a dit cette nuit ? »", 7, "rd3 em2 er3 ic3"),
            R("« Je ne voulais pas vous vexer. »", 7, ""),
            R("« Pardon. Vous avez raison. Qu'est-ce qu'il vous a dit ? »", 7, "ic2 er1"),
            R("« Justement, vous aurez tout le temps de le consoler. »", 7, "ic-3 rd-2 em-2"),
        ]),
        I(10, "moreau", "neutral", "« Un point encore. M. Ferreira parle très bien français, mais c'est sa deuxième langue. Vous en tenez compte comment ? »", [
            R("« Phrases courtes, pas de jargon, et je lui demande régulièrement de me redire ce qu'il a compris. S'il décroche, je propose un interprète, même s'il dit que ce n'est pas nécessaire. »", 11, "rd3 em2 cc3 pb2"),
            R("« Il parle français depuis quarante ans, il n'y aura pas de problème. »", 11, "rd-1 em-1 cc-1"),
            R("« Sa fille traduira quand elle arrivera à 16 h. »", 11, "rd-3 em-1 cc-2 pb-3"),
            R("« Je lui demande dans quelle langue il préfère qu'on parle de choses graves. »", 11, "rd3 cc2"),
            R("« Je parlerai plus lentement, ça suffira. »", 11, "cc0 rd-1"),
        ]),
        I(11, "moreau", "neutral", "« Qui est dans la pièce ? »", [
            R("« Lui, moi, vous en retrait, et Madame Rey s'il l'accepte. Je lui demande avant d'entrer s'il veut quelqu'un avec lui. »", 12, "rd3 cc2 pb2 ic3"),
            R("« Lui et moi, c'est plus intime. »", 12, "ic-2"),
            R("« Toute l'équipe, comme ça tout le monde a la même information. »", 12, "rd-3 em-2 pb-2"),
            R("« Ça dépend de lui. Je lui pose la question avant d'entrer. »", 12, "rd3 pb1"),
            R("« Sa fille aînée, pour le soutenir. »", 12, "rd-3 pb-2"),
        ]),
        I(12, "moreau", "neutral", "« Dernier point pratique. Il est en chambre double, son voisin est réveillé, et le tour de 15 h commence dans dix minutes. »", [
            R("« On décale le tour et on trouve un endroit fermé. Je ne peux pas lui annoncer ça avec un rideau pour seule intimité. »", 13, "rd3 er1 cc2 pb2"),
            R("« On tire le rideau et on parle doucement, ça ira. »", 14, "rd-2 cc-1 pb-1"),
            R("« On attend 16 h que sa fille soit là, comme ça on le dit une seule fois. »", 14, "rd-1 em-1 cc-1 pb-2"),
            R("« On lui propose la salle d'entretien, et on lui laisse choisir l'heure. »", 13, "rd3 cc1 pb1"),
            R("« On peut le faire pendant le tour, ça ira plus vite. »", 14, "rd-3 pb-3 em-1"),
        ]),
        I(13, "moreau", "neutral", "« Bien. Alors formulez-moi votre objectif. Pas le mien, le vôtre : à la fin de cet entretien, qu'est-ce que vous voulez qu'il se soit passé ? »", [
            R("« Qu'il sache ce qu'il a, avec ses mots à lui ; qu'il ait pu réagir ; et qu'il sache précisément ce qui se passe demain et qui il peut appeler ce soir. »", 15, "rd3 em2 co2 cc3 pb2"),
            R("« Qu'il ait compris le diagnostic et accepté le traitement. »", 15, "rd-1 cc1 pb-2"),
            R("« Qu'il le prenne le mieux possible. »", 15, "em1 cc-1"),
            R("« Qu'il reparte en sachant qu'on ne le laissera pas seul. »", 15, "co2 em2"),
            R("« Que ça dure moins de dix minutes. »", 15, "rd-2 er-1"),
        ]),
        I(14, "moreau", "cold-anger", "« Réfléchissez deux secondes. L'information est la sienne, pas celle de sa fille. Et un rideau n'est pas un mur : son voisin entendra tout, et lui le sait. »", [
            R("« Vous avez raison. Salle d'entretien, et je lui demande d'abord s'il veut quelqu'un avec lui. C'est lui qui décidera de répéter devant sa fille. »", 13, "rd3 er2 cc2 pb3"),
            R("« On fait comme vous voulez, vous avez l'habitude. »", 13, "cc-1 pb-1"),
            R("« D'accord. Et je lui demanderai s'il veut que sa fille soit là, ou pas. »", 13, "rd2 pb2"),
            R("« Il n'y a pas d'autre salle libre de toute façon. »", 13, "rd-2 pb-1"),
        ]),
        I(15, "moreau", "neutral", "« Il va vous demander combien de temps il lui reste. C'est quasi systématique. Vous répondez quoi ? »", [
            R("« Que je ne peux pas lui donner un chiffre honnête, que je ne veux pas en inventer un, et que l'oncologue pourra en parler plus précisément demain. »", 16, "rd2 em2 cc3 pb3"),
            R("« Les médianes de survie dans ce stade, pour qu'il ait une idée réaliste. »", 16, "em-2 co-2"),
            R("« Qu'il ne faut pas penser à ça maintenant. »", 16, "rd-2 em-2 cc-2"),
            R("« Je lui demanderai ce qu'il veut savoir, et ce que ce chiffre changerait pour lui. »", 16, "rd2 em2 cc2"),
            R("« Six mois, pour qu'il ait un repère. »", 16, "cc-3 pb-3"),
        ]),
        I(16, "moreau", "neutral", "« On y est. Vous ouvrez la porte dans trente secondes. Votre première phrase, c'est quoi ? »", [
            R("« Je lui dis que les résultats sont arrivés, et je lui demande d'abord ce qu'il a compris de sa situation jusqu'ici. »", -1, "rd2 em2 cc3 pb2"),
            R("« Monsieur Ferreira, vous avez un cancer du poumon avec des métastases au foie. »", -1, "rd-1 em-2 cc-2"),
            R("« Comment allez-vous aujourd'hui ? Il fait beau dehors, non ? »", -1, "em-1 cc-2 pb-2"),
            R("« Je m'assois, je le regarde, et je lui demande comment il va depuis ce matin. »", -1, "rd2 em2"),
            R("« Je lui dis que j'ai une mauvaise nouvelle et que je suis désolé·e. »", -1, "cc1 em1 pb-1"),
        ]),
    ],
)

# Reprise de la v1 : scène 1.2 L'annonce
S1_3 = S(3, "1.3 L'annonce",
    "Salle d'entretien, porte fermée. M. Ferreira est assis, il a enfilé sa veste par-dessus le pyjama. Inès Rey est là. Dr Moreau reste en retrait. C'est à Alex.",
    focus=("cc", "em", "er", "rd"),
    nodes=[
        I(1, "ferreira", "anxious", "« Vous vouliez me parler ? » Il se redresse. « Ma femme est décédée ici il y a quatre ans. On m'avait fait venir dans cette pièce aussi. »", [
            R("« Oui. Avant que je vous dise où nous en sommes, j'aimerais savoir : vous, de votre côté, qu'est-ce que vous vous êtes dit depuis votre entrée ? »", 2, "rd2 em3 cc3"),
            R("« Ne vous inquiétez pas, ce n'est pas pareil. »", 3, "em-2 cc-2"),
            R("« Les résultats de vos examens sont arrivés. »", 4, "cc1 pb1"),
            R("Lui laisser un instant, puis : « Ça doit être dur de revenir dans cette pièce. »", 2, "em3 co2"),
            R("« On ne va pas parler de votre femme aujourd'hui. »", 4, "em-3 rd-2"),
        ]),
        I(2, "ferreira", "anxious", "« Franchement ? » Il regarde ses mains. « J'ai maigri de huit kilos. Je tousse du sang. Je ne suis pas idiot. J'ai demandé à l'infirmière cette nuit si ça pouvait être une tumeur. »", [
            R("« Vous avez eu raison d'y penser. Est-ce que vous voulez que je vous dise précisément ce que montrent les examens ? »", 5, "rd3 em3 cc3 pb2"),
            R("« Effectivement, c'est une tumeur. Un adénocarcinome pulmonaire de stade IV. »", 6, "em-1 cc1"),
            R("« On ne peut encore rien affirmer, il faut attendre d'autres examens. »", 3, "em-1 cc-3"),
            R("« Vous avez déjà beaucoup compris. Qu'est-ce qui vous inquiète le plus ? »", 5, "em3 cc1"),
            R("« Ne vous faites pas de films, on va tout vous expliquer. »", 3, "rd-2 em-2 cc-1"),
        ]),
        I(3, "ferreira", "cold-anger", "Il vous regarde longuement. « Vous savez, quand on me ment, je le vois. Ma femme aussi, on lui a dit qu'on ne savait pas encore, pendant trois semaines. »", [
            R("« Vous avez raison, et je m'en excuse. Les résultats sont arrivés, ils ne sont pas bons, et je vais vous les dire maintenant. »", 5, "rd3 er2 cc3"),
            R("« Je ne vous mens pas, je suis prudent·e. »", 6, "rd-1 cc-2"),
            R("« Vous avez raison de le dire. Je vais être franc·he avec vous. »", 5, "rd2 er1 cc2"),
            R("« Personne ne vous ment, Monsieur Ferreira. Calmez-vous. »", 6, "rd-2 er-2 em-2"),
        ]),
        I(4, "ferreira", "anxious", "« Et alors ? » Son regard se fige. Il a compris à votre visage, mais vous ne lui avez rien laissé le temps d'amortir.", [
            R("« Excusez-moi, je reprends. Ce que je dois vous annoncer est grave, et je préfère vous le dire calmement. »", 5, "rd2 em2 er2 cc2"),
            R("« C'est un cancer. Métastasé. »", 6, "rd-1 em-2"),
            R("Se taire, s'asseoir plus près, et attendre qu'il reprenne.", 5, "em2 er2 co1"),
            R("« Je vais être direct·e : les nouvelles sont mauvaises. »", 6, "cc1 em-1"),
        ]),
        I(5, "ferreira", "neutral", "« Allez-y. » Il pose les mains à plat sur la table. « Dites-moi tout. Je préfère savoir. »", [
            R("« Très bien. Je vais aller par étapes, et vous m'arrêtez dès que vous voulez. »", 7, "rd3 em2 cc3 pb2"),
            R("« Tout, c'est beaucoup. Je vais commencer par l'essentiel. »", 7, "rd2 em1 cc2"),
            R("« Je vais tout vous détailler pour que vous ayez une vision complète. »", 6, "em-1"),
            R("« Avant, voulez-vous qu'Inès reste avec nous ? »", 7, "rd2 ic2"),
            R("« Accrochez-vous, ce n'est pas facile à entendre. »", 7, "em-1 cc-1"),
        ]),
        I(6, "ferreira", "confused", "Il lève la main. « Attendez. Attendez. Je n'ai rien compris après le mot poumon. »", [
            R("« Pardon. Je reprends simplement : vous avez un cancer du poumon, et il s'est étendu au foie. Le reste peut attendre. »", 10, "rd2 em2 er2 cc3"),
            R("« Je vous mettrai tout par écrit, ne vous en faites pas. »", 10, ""),
            R("« Pardon, je suis allé·e trop vite. Qu'est-ce que vous avez entendu ? »", 10, "cc3 em2"),
            R("« C'est technique. Le principal, c'est que ce n'est pas bon. »", 10, "cc-2 em-2"),
        ]),
        I(7, "ferreira", "neutral", "Il hoche la tête. « J'écoute. »", [
            R("« Ce que montrent les examens n'est pas bon. » — marquer un temps — « Il s'agit d'une tumeur au poumon. »", 8, "rd3 em3 er3 cc3"),
            R("« Les examens montrent un adénocarcinome pulmonaire avec des lésions hépatiques secondaires multiples. »", 6, "rd-1 em-2 cc-3"),
            R("« Ce n'est pas la meilleure nouvelle, mais il y a des choses à faire. »", 9, "cc-2"),
            R("« Je vais vous dire ce que montrent les examens, et après vous posez toutes les questions que vous voulez. »", 8, "cc2 rd2"),
            R("« Bon, je vais être honnête : c'est un cancer métastatique. »", 6, "cc-1 em-2 pb-1"),
        ]),
        I(8, "ferreira", "neutral", "Il ne bouge pas. « Une tumeur. » Il répète le mot lentement. « Et elle est où, exactement ? »", [
            R("« Dans le poumon droit. Et malheureusement, elle s'est déjà étendue au foie. C'est un cancer avancé. »", 10, "rd3 em2 er3 cc3"),
            R("« Dans le poumon. On regardera le reste avec l'oncologue. »", 9, "cc-2"),
            R("« Dans le poumon, et il a touché le foie. Vous voulez que je vous montre sur l'image ? »", 10, "cc3 rd1"),
            R("« Un peu partout, malheureusement. »", 9, "cc-2 em-1"),
        ]),
        I(9, "ferreira", "suspicious", "« Il y a autre chose. » Ce n'est pas une question. « Sinon vous ne feriez pas cette tête. »", [
            R("« Oui. La maladie s'est déjà étendue au foie. Je ne voulais pas tout dire d'un coup, mais je ne veux pas non plus vous le cacher. »", 10, "rd3 er2 cc3"),
            R("« Non, c'est tout pour aujourd'hui. »", 10, "rd-2 cc-3"),
            R("« Vous avez raison. Il y a autre chose, et je vais vous le dire maintenant. »", 10, "cc2 rd2 pb1"),
            R("« Rien d'autre qui doive vous inquiéter aujourd'hui. »", 10, "cc-3 pb-2 rd-1"),
        ]),
        I(10, "ferreira", "sad", "Il ne dit plus rien. Il fixe un point sur la table. Vingt secondes passent. Inès Rey ne bouge pas. Dr Moreau ne bouge pas.", [
            R("Ne rien dire. Rester présent·e, le regarder, attendre qu'il reprenne la parole.", 11, "rd3 em3 co3 er3 cc2"),
            R("« Je sais que c'est beaucoup d'un coup. Prenez le temps qu'il vous faut. »", 11, "em2 co2 er2 cc1"),
            R("« Je comprends tout à fait ce que vous ressentez. »", 12, "em-2 co-1"),
            R("Poser doucement la boîte de mouchoirs sur la table, sans parler.", 11, "co3 er1"),
            R("« Vous voulez un verre d'eau ? Je peux continuer ? »", 12, "em-1 cc-1"),
        ]),
        I(11, "ferreira", "sad", "« Excusez-moi. » Il s'essuie les yeux d'un revers de manche, gêné. « Je ne pleure jamais, d'habitude. »", [
            R("« Vous n'avez pas à vous excuser. On vient de vous annoncer quelque chose de très dur. »", 13, "rd3 em3 co3 er2"),
            R("Lui tendre la boîte de mouchoirs sans rien dire.", 13, "rd3 em3 co3 er3 cc1"),
            R("« Allons, il ne faut pas se laisser abattre. »", 12, "rd-2 em-3 co-2"),
            R("« Pleurer, c'est ce qu'il y a de plus normal, ici. »", 13, "em2 co2"),
            R("« Ça va passer. »", 12, "em-2 co-1"),
        ]),
        I(12, "ferreira", "cold-anger", "Il se referme d'un coup. « Vous ne pouvez pas comprendre. Vous avez quoi, vingt-cinq ans ? »", [
            R("« Vous avez raison, je ne peux pas savoir ce que ça fait. Je peux seulement rester là et vous écouter. »", 13, "rd3 em3 co2 er3"),
            R("« J'ai vu beaucoup de patients dans votre situation. »", 13, "rd-2 em-2"),
            R("« Non, je ne peux pas comprendre. Mais je peux rester. »", 13, "em3 er2"),
            R("« L'âge n'a rien à voir avec la compétence. »", 13, "er-2 em-2"),
        ]),
        I(13, "ferreira", "neutral", "« C'est grave, alors. » Il vous regarde. « Dites-le avec vos mots. »", [
            R("« Oui, c'est grave. C'est une maladie qu'on ne sait pas guérir à ce stade, mais qu'on sait souvent ralentir et accompagner. »", 14, "rd3 co2 cc3"),
            R("« C'est sérieux, mais il ne faut pas perdre espoir, la médecine fait des progrès. »", 14, "em-1 cc-2"),
            R("« C'est un stade IV, donc oui, le pronostic est mauvais. »", 14, "em-2 co-2 cc1"),
            R("« C'est grave, oui. Et vous ne serez pas seul pour la suite. »", 14, "cc2 co2 rd1"),
            R("« Tout dépendra de la réponse aux traitements. »", 14, "cc-1"),
        ]),
        I(14, "ferreira", "neutral", "« Il me reste combien de temps ? » Sa voix est nette. Il vous regarde droit dans les yeux.", [
            R("« Je ne peux pas vous donner un chiffre honnêtement, et je ne veux pas vous en inventer un. C'est une maladie sérieuse pour laquelle il existe des traitements. L'oncologue pourra être plus précise demain. »", 15, "rd3 em2 co2 cc3 pb2"),
            R("« Difficile à dire… peut-être un an, peut-être plus. Ça dépend beaucoup des gens. »", 15, "cc-2"),
            R("« Ne pensez pas à ça maintenant, concentrons-nous sur le traitement. »", 15, "rd-2 em-2 cc-1"),
            R("« Qu'est-ce qui vous aiderait à savoir, pour les semaines qui viennent ? »", 15, "em2 rd2 cc1"),
            R("« Six mois, peut-être moins. »", 15, "cc-2 pb-3 co-2"),
        ]),
        I(15, "ferreira", "anxious", "« Ce n'est pas une réponse. » Il se penche. « J'ai une fille qui se marie en septembre. J'ai besoin de savoir si je dois lui dire d'avancer la date. »", [
            R("« Là je peux vous répondre autrement : si cette date compte pour vous, n'attendez pas pour en parler avec elle. Et je poserai votre question à l'oncologue demain, avec vous. »", 16, sets=["mariage_anticipe"], scores="rd3 em3 co3 cc3"),
            R("« Septembre, c'est dans cinq mois. Ça devrait aller. »", 16, sets=["mariage_rassure"], scores="cc-2 pb-2"),
            R("« Je ne peux vraiment pas me prononcer. »", 16, "em-2 co-2"),
            R("« Qu'est-ce que cette date représente pour vous ? »", 16, "em3 rd1"),
            R("« Dites-lui de ne rien changer, on ne sait jamais. »", 16, "cc-2 pb-2", sets=["mariage_rassure"]),
        ]),
        I(16, "ferreira", "anxious", "« Et je vais devenir quoi ? » Il montre ses mains. « Je pose du carrelage. Je travaille encore trois jours par semaine. »", [
            R("« On ne va pas décider ça aujourd'hui. Mais c'est une vraie question et on va s'en occuper : il y a un service social ici dont c'est exactement le métier. »", 17, "rd3 co2 cc3 pb3 ic2"),
            R("« Il va falloir arrêter de travailler, évidemment. »", 17, "rd-2 em-2"),
            R("« Ce n'est pas le plus important pour l'instant. »", 17, "rd-2 em-2 cc-1"),
            R("« Qu'est-ce qui compte le plus pour vous, dans votre travail ? »", 17, "em2 rd2"),
            R("« On verra ça avec l'assistante sociale, ce n'est pas mon rôle. »", 17, "em-2 pb-1"),
        ]),
        I(17, "ferreira", "anxious", "« Et l'assurance ? Si j'arrête, on me paie combien ? Je n'ai pas fini de payer l'appartement. »", [
            R("« Je ne connais pas assez bien les règles de l'assurance-invalidité pour vous répondre sans risque de me tromper. Je demande à l'assistante sociale de passer demain — c'est elle qui saura. »", 18, "rd2 cc3 pb3 ic3"),
            R("« L'AI prend le relais après six mois, en général autour de 60 % du salaire. »", 18, "cc-1 pb-3"),
            R("« Ce sont des questions administratives, ce n'est pas mon domaine. »", 18, "em-2 co-2 pb1 ic-1"),
            R("« C'est une vraie inquiétude. On ne vous laissera pas seul avec ces papiers. »", 18, "em2 co2 ic1"),
            R("« Ne pensez pas à l'argent maintenant. »", 18, "em-2 rd-1"),
        ]),
        I(18, "ferreira", "ashamed", "« J'ai fumé jusqu'à quarante-cinq ans. » Il baisse les yeux. « C'est de ma faute, c'est ça ? »", [
            R("« Le tabac augmente le risque, c'est vrai. Mais des gens qui n'ont jamais fumé développent ce cancer, et beaucoup de fumeurs ne l'auront jamais. Chercher un coupable ne vous aidera pas, et sûrement pas vous-même. »", 19, "rd3 em3 co3 cc3"),
            R("« Le tabac est le principal facteur de risque du cancer du poumon, oui. »", 19, "rd-2 em-3 co-3 cc1"),
            R("« Mais non, ça n'a rien à voir. »", 19, "em1 cc-3"),
            R("« Ce qui compte maintenant, c'est ce qu'on fait à partir d'aujourd'hui. »", 19, "co2 rd1"),
            R("« C'est un peu tard pour les regrets. »", 19, "rd-3 co-3 em-2"),
        ]),
        I(19, "ferreira", "sad", "Il souffle longuement. « Comment je dis ça à mes filles ? L'aînée arrive dans une heure. »", [
            R("« On peut le faire ensemble si vous le souhaitez. C'est vous qui décidez de ce qu'elles savent et quand — c'est votre information, pas la mienne. »", 20, "rd3 em3 co2 pb3"),
            R("« Voulez-vous que je m'en charge ? Ce sera plus simple pour vous. »", 21, "rd-1 co1 pb-2"),
            R("« C'est une question personnelle, je préfère ne pas m'en mêler. »", 21, "em-2 co-2 pb-1"),
            R("« Vous voulez qu'on prépare ensemble ce que vous allez leur dire ? »", 20, "rd2 em2 ic1"),
            R("« Dites-lui simplement que c'est un cancer, elle comprendra. »", 21, "em-2 cc-1"),
        ]),
        I(20, "ferreira", "melancholic", "« Carla va vouloir tout organiser. Elle fait ça depuis la mort de sa mère. » Il esquisse un sourire fatigué. « Et la petite va pleurer. »", [
            R("« Alors on peut prévoir ça : leur dire ensemble, ou que vous leur disiez d'abord seul et que je réponde aux questions après. Qu'est-ce qui vous irait le mieux ? »", 22, "rd3 em3 co3 cc3 pb3"),
            R("« Vous les connaissez mieux que moi, faites comme vous le sentez. »", 22, "rd1 em1"),
            R("« Qu'est-ce que vous voulez qu'elles gardent de cette journée ? »", 22, "em3 co2 rd1"),
            R("« Ne vous inquiétez pas, vos filles sont solides. »", 22, "em-2 cc-1"),
        ]),
        I(21, "ferreira", "vulnerable", "« Vous ne voulez pas m'aider pour ça ? » Il paraît soudain très seul. « Je ne sais pas comment on dit ce genre de chose. »", [
            R("« Si, bien sûr. Excusez-moi. On va préparer ça ensemble — c'est vous qui décidez, mais vous n'êtes pas obligé de le faire seul. »", 20, "rd3 em3 co3 er2"),
            R("« Beaucoup de gens trouvent leurs mots au moment venu. »", 22, "em-1 co-1 cc-1"),
            R("« Si, je vais vous aider. On peut le préparer ensemble. »", 20, "em2 co2"),
            R("« Je suis étudiant·e, je n'ai pas le droit de parler à votre famille. »", 22, "pb-1 em-2 cc-1"),
        ]),
        I(22, "ferreira", "neutral", "« Bon. » Il se redresse. « Et maintenant, qu'est-ce qui se passe ? »", [
            R("« Demain matin, l'oncologue passe vous voir avec les options de traitement. D'ici là, rien ne vous est demandé. Je note vos questions au fur et à mesure si vous voulez. »", 23, "rd2 co2 cc3 ic2"),
            R("« On va lancer la chimiothérapie dès que possible, il ne faut pas perdre de temps. »", 23, "rd-1 cc-1 pb-2"),
            R("« On verra tout ça demain, reposez-vous. »", 23, "cc-1"),
            R("« Maintenant, vous pouvez vous reposer. Je repasse ce soir, avec vos questions si vous en avez. »", 23, "co2 cc2"),
            R("« Maintenant, il faut être fort. »", 23, "em-2 cc-1"),
        ]),
        I(23, "moreau", "neutral", "Dr Moreau vous adresse un regard discret. Vous n'avez pas encore vérifié ce que M. Ferreira a réellement retenu.", [
            R("« Monsieur Ferreira, pour être sûr·e de ne pas vous avoir embrouillé : si votre fille vous demande tout à l'heure ce que le médecin a dit, vous lui répondez quoi ? »", 24, "rd3 em2 cc3 pb2"),
            R("« Vous avez bien tout compris ? »", 24, "cc-1"),
            R("Conclure sans vérifier.", 25, "rd-1 cc-2 pb-1"),
            R("« Est-ce que je peux vous demander ce que vous avez retenu, pour être sûr·e d'avoir été clair·e ? »", 24, "cc3 rd1"),
            R("« Je vous laisse, vous avez sûrement besoin d'être seul. »", 25, "cc-2 em-1"),
        ]),
        I(24, "ferreira", "neutral", "« Que j'ai un cancer du poumon. Qu'il est parti dans le foie. Qu'on ne peut pas le guérir mais qu'on peut le freiner. Et que je vois la spécialiste demain. » Il marque un temps. « C'est ça ? »", [
            R("« C'est exactement ça. Vous avez tout retenu. »", 25, "rd3 co2 cc3"),
            R("« Presque. On dit plutôt métastases hépatiques. »", 25, "rd-2 em-2 cc-1"),
            R("« Oui. Et vous l'avez dit mieux que moi. »", 25, "rd2 co1"),
            R("« À peu près. On reverra les détails avec l'oncologue. »", 25, "cc-1 rd-1"),
        ]),
        I(25, "ines", "neutral", "Inès Rey intervient doucement. « Monsieur Ferreira, je suis là jusqu'à 20 h, et ma collègue prend le relais après. Vous pouvez sonner. »", [
            R("« Et je repasse en fin d'après-midi avant de partir. Vous n'êtes pas seul avec ça. »", 26, "rd2 em3 co3 ic3"),
            R("« Voilà, l'équipe infirmière est là. »", 26, "ic1"),
            R("« Merci, Inès. » Puis, à M. Ferreira : « Je repasse avant 18 h. »", 26, "ic2 co1 cc1"),
            R("Se lever et partir sans rien ajouter.", 26, "co-2 ic-1"),
        ]),
        I(26, "moreau", "neutral", "Dans le couloir, une fois la porte refermée. « Avant de passer à autre chose : qu'est-ce qu'on trace, et pour qui ? »", [
            R("« Une note avec les mots exacts que j'ai employés, ce qu'il a reformulé, ses questions en suspens, et le fait qu'il décide lui-même quand informer ses filles. Je la lis aux transmissions de ce soir. »", -1, "rd3 cc3 pb3 ic3"),
            R("« Que l'annonce a été faite ce jour, avec l'accord du patient pour la suite. »", -1, "pb1"),
            R("« C'est dans l'observation médicale, ça suffira. »", -1, "cc-2 pb-1 ic-2"),
            R("« Les mots employés, ce qu'il a compris, et ce qu'il veut qu'on dise ou non à ses filles. Je vous montre la note avant de la signer. »", -1, "cc3 ic2 pb1"),
            R("« Pas grand-chose. Par écrit, il vaut mieux rester vague. »", -1, "cc-3 ic-2 pb-2"),
        ]),
    ],
)

# Reprise de la v1 : scène 1.3 Le lendemain
S1_4 = S(4, "1.4 Le lendemain",
    "Huit heures du matin. M. Ferreira a passé une mauvaise nuit. Et il a dit à sa fille, hier soir au téléphone, qu'il avait « une infection au poumon ».",
    focus=("rd", "em", "ic"),
    nodes=[
        I(1, "ines", "neutral", "« Il n'a pas dormi. Et il a appelé sa fille hier soir devant moi : il lui a dit qu'il avait une infection au poumon. Elle arrive à 9 h. »", [
            R("« Merci de me le dire. Avant de juger, j'aimerais comprendre pourquoi il a dit ça. Je vais le voir. »", 2, "rd2 em3 er3 cc2 ic3"),
            R("« Il a menti à sa fille alors qu'on a passé une heure à tout lui expliquer. »", 3, "rd-2 em-2 er-2"),
            R("« Ce n'est pas notre problème, c'est sa famille. »", 3, "em-2 co-2 pb-2 ic-2"),
            R("« Vous avez parlé avec lui cette nuit ? Il vous a dit pourquoi ? »", 2, "ic2 em1"),
            R("« Super. Donc tout est à refaire. »", 3, "er-2 em-2"),
        ]),
        I(2, "ferreira", "ashamed", "Il est assis au bord du lit, habillé. « Vous êtes déjà là ? » Il évite votre regard.", [
            R("« Bonjour Monsieur Ferreira. Comment s'est passée la nuit ? »", 4, "rd3 em3 cc2"),
            R("« Votre fille arrive à 9 h. Il faut qu'on parle de ce que vous lui avez dit. »", 5, "rd-2 em-2 er-2 cc1"),
            R("S'asseoir à côté de lui. « Vous avez pu dormir un peu ? »", 4, "em2 rd1"),
            R("« Il paraît que vous avez parlé à votre fille hier soir ? »", 5, "pb-1 em-1"),
        ]),
        I(3, "ines", "neutral", "Elle vous regarde. « Vous savez, quand mon père a eu son AVC, j'ai dit à mes enfants pendant deux jours que c'était un malaise. On n'est pas toujours prêt à dire les choses à voix haute. »", [
            R("« Vous avez raison, j'ai réagi trop vite. Je vais aller lui demander ce qui s'est passé, sans lui faire la leçon. »", 2, "rd2 em3 er3 ic3"),
            R("« Ce n'est pas comparable, on lui a expliqué en détail hier. »", 2, "em-2 er-2 ic-2"),
            R("« Ça m'aide de l'entendre. Merci. »", 2, "ic2 er1"),
            R("« Je ne vois pas le rapport. »", 2, "ic-2 em-2"),
        ]),
        I(4, "ferreira", "melancholic", "« J'ai regardé le plafond. » Il hausse les épaules. « À un moment j'ai cru que j'avais rêvé la conversation d'hier. »", [
            R("« C'est une réaction fréquente — on entend, et en même temps quelque chose refuse. Est-ce que vous voulez qu'on reprenne ensemble ce qui a été dit ? »", 6, "rd3 em3 co3 cc3"),
            R("« Vous n'avez pas rêvé, malheureusement. »", 6, "em-1 co-1 cc1"),
            R("« Je vais vous prescrire quelque chose pour dormir. »", 6, "em-1 cc-1 pb-1"),
            R("« Ça arrive souvent, après une nouvelle pareille. Vous voulez en parler ? »", 6, "em2 cc1"),
            R("« Il faut accepter, maintenant. »", 6, "em-2 rd-1"),
        ]),
        I(5, "ferreira", "angry", "Il se raidit. « Vous m'espionnez, maintenant ? »", [
            R("« Non, et je m'y suis mal pris·e. Je voulais dire que je suis là pour vous aider avec elle, pas pour vous reprocher quoi que ce soit. »", 4, "rd3 em3 er3"),
            R("« L'infirmière était présente, elle m'a rapporté la conversation. »", 6, "rd-2 em-2 er-1"),
            R("« Pardon. Je voulais vous proposer mon aide, pas vous faire un reproche. »", 4, "er2 rd1"),
            R("« Pas du tout. Mais votre fille a le droit de savoir. »", 6, "rd-2 pb-2"),
        ]),
        I(6, "ferreira", "neutral", "« Allez-y. Redites-moi. » Il s'assoit dans le fauteuil.", [
            R("« Plutôt que je redise, dites-moi d'abord ce qui vous est resté. Je compléterai. »", 7, "rd3 em2 cc3 pb2"),
            R("« Vous avez un adénocarcinome pulmonaire métastatique au foie. »", 8, "rd-1 em-2 cc-1"),
            R("« Qu'est-ce qui vous a le plus marqué, hier ? »", 7, "em2 cc2"),
            R("« Je vous ai déjà tout dit hier, vous ne vous souvenez pas ? »", 8, "em-3 rd-2"),
        ]),
        I(7, "ferreira", "confused", "« Une tumeur au poumon. Et… » Il hésite. « Vous aviez dit que c'était dans le foie aussi, mais que le foie, ça se soigne bien. Non ? »", [
            R("« Là je dois vous corriger, et je préfère le faire maintenant. Je n'ai pas dit ça. L'atteinte du foie vient du cancer du poumon — c'est ce qui rend la maladie avancée. »", 9, "rd3 co2 er2 cc3"),
            R("« Oui, enfin, disons que c'est plus compliqué que ça. »", 8, "rd-1 cc-3"),
            R("« Non, ce n'est pas du tout ce que j'ai dit. »", 8, "rd-2 em-2 cc1"),
            R("« Je comprends que ce soit ce que vous avez entendu. Reprenons ce que j'ai voulu dire sur le foie. »", 9, "cc3 em1"),
            R("« Oui, le foie, ça se soigne bien. »", 9, "cc-3 pb-3 rd-1"),
        ]),
        I(8, "ferreira", "ashamed", "Il se ferme. « Alors j'ai encore tout compris de travers. »", [
            R("« Non. C'est normal de ne pas tout retenir quand on reçoit une nouvelle pareille — c'est pour ça qu'on reprend aujourd'hui. Personne ne retient tout. »", 9, "rd3 em3 co3 er2 cc2"),
            R("« Ce n'est pas grave, on recommencera autant de fois qu'il faudra. »", 9, "em1 co1"),
            R("« Vous avez très bien compris l'essentiel : c'est grave. Le reste, on le reprend ensemble. »", 9, "em2 cc2 rd1"),
            R("« Oui, c'est dommage. »", 9, "em-3 rd-2"),
        ]),
        I(9, "ferreira", "ashamed", "Il finit par lâcher : « J'ai dit à Carla que c'était une infection. » Un silence. « Je n'ai pas réussi à dire le mot au téléphone. »", [
            R("« Je comprends. Ce n'est pas un mensonge, c'est un mot qui ne sort pas. Qu'est-ce que vous voulez qu'elle sache, quand elle arrivera ? »", 10, "rd3 em3 co3 cc3 pb3"),
            R("« Il va falloir lui dire la vérité maintenant. »", 10, "rd-1 em-1 cc1 pb-1"),
            R("« Ce n'est pas très prudent, elle risque de l'apprendre autrement. »", 10, "rd-2 em-2 co-2"),
            R("« Qu'est-ce qui vous a empêché de le dire ? »", 10, "em3 rd1"),
            R("« Vous lui avez menti, donc. »", 10, "rd-3 em-3"),
        ]),
        I(10, "ferreira", "vulnerable", "« Qu'elle sache. Mais je ne veux pas le dire moi-même. » Il vous regarde. « Vous pouvez le faire, vous ? Avec moi dans la pièce. »", [
            R("« Oui. C'est vous qui me le demandez, donc je peux. On se met d'accord sur ce que je dis et ce que je ne dis pas. »", 11, "rd3 em2 co3 cc3 pb3"),
            R("« C'est à vous de le faire, c'est votre famille. »", 11, "rd-1 em-2 co-3 pb-1"),
            R("« Bien sûr, je m'en occupe, ne vous inquiétez pas. »", 11, "co2 cc-1 pb-2"),
            R("« D'accord. On le fait ensemble, et vous m'arrêtez si je vais trop loin. »", 11, "rd3 pb1 ic1"),
            R("« Je vais demander au Dr Moreau de le faire, c'est plus sûr. »", 11, "em-1 ic1"),
        ]),
        I(11, "carla", "neutral", "Elle entre sans frapper, manteau sur le bras. « Bonjour. Alors, cette infection ? Il faut combien de jours d'antibiotiques ? »", [
            R("Regarder M. Ferreira, attendre son signe de tête, puis : « Madame Ferreira, asseyez-vous. Ce n'est pas une infection. Votre père m'a demandé de vous expliquer. »", 13, "rd3 em2 co2 cc3 pb3"),
            R("« Ce n'est pas une infection, c'est un cancer du poumon métastasé. »", 12, "rd-2 em-2 cc1 pb-2"),
            R("« Je préfère que votre père vous en parle lui-même. »", 12, "rd-1 em-1 co-2 pb-1"),
            R("« Bonjour. Asseyez-vous : votre père voulait qu'on parle tous les trois. »", 13, "rd2 cc2"),
            R("« Il faudra voir ça avec lui, je ne peux rien vous dire. »", 12, "cc-2 em-1"),
        ]),
        I(12, "ferreira", "ashamed", "M. Ferreira se recroqueville dans son fauteuil. Carla le regarde, puis vous, puis lui. « Papa ? »", [
            R("« Excusez-moi. J'aurais dû laisser votre père mener ce moment. Monsieur Ferreira, est-ce que vous voulez que je continue, ou préférez-vous parler ? »", 13, "rd3 em2 er3 pb3"),
            R("Poursuivre l'explication médicale.", 14, "rd-2 em-2 pb-2"),
            R("Se taire, et regarder M. Ferreira pour lui rendre la parole.", 13, "rd3 er1"),
            R("« Bon, puisque c'est dit… »", 14, "em-2 rd-2"),
        ]),
        I(13, "carla", "anxious", "Elle s'assoit lentement. « Un cancer. » Elle sort son téléphone, le repose. « Depuis quand vous le savez ? »", [
            R("« Depuis hier après-midi. Votre père a été informé en premier — c'est la règle, l'information lui appartient. Il a souhaité que vous le sachiez aujourd'hui. »", 14, "rd3 em2 cc3 pb3"),
            R("« Hier. On vous aurait appelée, mais on ne peut rien dire sans l'accord du patient. »", 14, "rd2 cc2 pb2"),
            R("« C'est votre père qui a choisi de ne rien vous dire hier soir. »", 14, "rd-2 em-2 cc1 pb-1"),
            R("« Hier. Il a voulu choisir lui-même le moment de vous le dire. »", 14, "rd2 cc2"),
            R("« Vous auriez dû venir hier. »", 14, "em-3 rd-2"),
        ]),
        I(14, "carla", "angry", "Elle se tourne vers son père. « Tu m'as menti hier au téléphone. » Sa voix tremble. « Comme maman. Vous m'avez tous menti jusqu'au bout. »", [
            R("« Votre père n'a pas réussi à prononcer le mot au téléphone. Ce n'est pas la même chose que vous mentir — et il m'a demandé ce matin de vous dire les choses. »", 15, "rd3 em3 co3 er3 cc3"),
            R("« Je comprends votre colère, mais ce n'est pas le moment. »", 15, "rd-2 em-2 co-2 er-1"),
            R("Laisser le silence s'installer entre eux sans intervenir.", 15, "rd2 em2 co1 er3"),
            R("« Vous avez le droit d'être en colère. Ce n'est pas la même chose que ce qui s'est passé avec votre mère. »", 15, "em2 er1 cc1"),
            R("« Il n'avait pas le choix, il fallait vous protéger. »", 15, "cc-2 rd-2"),
        ]),
        I(15, "carla", "sad", "Elle finit par demander, plus bas : « Il va mourir quand ? »", [
            R("« Je ne peux pas répondre à ça, et votre père a posé la même question hier. L'oncologue passe ce matin — vous pourrez la lui poser ensemble. »", 16, "rd3 em3 co2 cc3 pb3"),
            R("« Personne ne peut le dire. Il faut vivre au jour le jour. »", 16, "em-1 cc-1"),
            R("« Dans ce genre de situation, on parle généralement de quelques mois à un an. »", 16, "rd-2 pb-3"),
            R("« Personne ne peut le dire aujourd'hui. Ce qu'on peut faire, c'est ne pas perdre le temps qu'il y a. »", 16, "cc2 co2"),
            R("« Il faut vous préparer au pire. »", 16, "co-2 cc-1"),
        ]),
        I(16, "carla", "anxious", "Elle a déjà repris son téléphone. « Bon. Je m'occupe de tout. Je prends un congé, je vends sa voiture, je résilie son abonnement de chantier… »", [
            R("« Attendez une seconde. » — se tourner vers M. Ferreira — « Monsieur Ferreira, est-ce que c'est ce que vous voulez ? »", 17, "rd3 em2 cc3 pb3 ic1"),
            R("« C'est une bonne chose que vous puissiez l'aider. »", 17, "rd-2 pb-2"),
            R("« Carla, est-ce qu'on peut d'abord demander à votre père ce qu'il veut ? »", 17, "rd3 cc1"),
            R("« Oui, organisez-vous, ça vous occupera l'esprit. »", 17, "rd-2 em-2"),
        ]),
        I(17, "ferreira", "angry", "« Je ne vends pas la voiture. » C'est la première fois qu'il hausse la voix. « Je suis malade, je ne suis pas mort. »", [
            R("« Vous avez entièrement raison, et c'est important de le dire. Carla, votre père décide de ce qui le concerne aussi longtemps qu'il le peut. Ce que vous pouvez faire, c'est l'accompagner aux rendez-vous s'il le souhaite. »", 18, "rd3 em3 co2 cc3 pb3"),
            R("« Ne vous énervez pas, votre fille veut bien faire. »", 18, "rd-2 em-1 pb-2"),
            R("« Vous êtes vivant, et c'est vous qui décidez. On le note. »", 18, "rd3 cc1"),
            R("« Monsieur Ferreira, votre fille essaie de vous aider. Soyez raisonnable. »", 18, "rd-3 pb-2"),
        ]),
        I(18, "ines", "neutral", "Dans le couloir. « J'ai entendu depuis la porte. Qu'est-ce que je note pour l'équipe ? »", [
            R("« Que la fille aînée est informée depuis ce matin avec l'accord du patient, que le patient garde la décision sur ses affaires personnelles, et que l'assistante sociale doit passer pour l'AI. Je rédige, vous relisez ? »", -1, "rd3 cc3 pb3 ic3"),
            R("« Que la famille est au courant. »", -1, "cc-1"),
            R("« Rien de particulier, tout s'est bien passé. »", -1, "cc-2 pb-1 ic-2"),
            R("« Que la famille est informée, et ce que le patient veut garder pour lui. »", -1, "cc2 ic1 rd1"),
            R("« Que la fille est difficile. »", -1, "rd-2 ic-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 1.5 Le vestiaire — nouvelle scène
# ---------------------------------------------------------------------------
S1_5 = S(5, "1.5 Le vestiaire",
    "Vendredi, 18 h 10. Fin de la première semaine. Vestiaire des étudiants, sous-sol. "
    "Jonas range sa blouse en sifflotant. Dans votre poche, la note que vous n'avez pas "
    "encore relue : « Mots exacts employés avec M. Ferreira ».",
    focus=("er", "rd", "ic"),
    nodes=[
        I(1, "jonas", "happy",
          "« Alors, la star du 312 ! » Il vous lance une barre de céréales. « Il paraît que "
          "le carreleur a pleuré. T'as fait fondre le carrelage ? »", [
            R("« Il a pleuré parce qu'on venait de lui dire qu'il allait mourir, Jonas. Je n'ai "
              "pas envie d'en rire. »", 2, "rd3 pb1 er1 cc1"),
            R("Rire. « Même pas. Plutôt du ciment, le type. »", 3, "rd-3 pb-3 er-1"),
            R("« Laisse tomber. »", 4, "ic-1 er0"),
            R("Poser la barre de céréales. « Il a eu le courage de pleurer devant nous. Moi, je ne sais pas si j'y arriverais. »", 2, "rd2 em2 er1"),
            R("« Tu parles comme ça de tous les patients ? »", 4, "rd1 pb1 er-1"),
        ]),
        I(2, "jonas", "ashamed",
          "Il perd son sourire. « Ouais. Pardon. » Il s'assoit sur le banc. « Mon premier "
          "patient en fin de vie, c'était la semaine passée, en chir. Il est mort pendant que "
          "je remplissais son ordonnance de sortie. Personne ne m'a demandé comment ça "
          "allait. »", [
            R("« Et alors, comment ça allait ? »", 5, "em3 co2 ic1"),
            R("« Tu devrais en parler à quelqu'un. »", 5, "em1 ic1"),
            R("« C'est le métier, non ? »", 6, "em-2 co-1 er-1"),
            R("S'asseoir à côté de lui, sans rien dire.", 5, "em2 co1"),
            R("« T'aurais dû prendre un jour de congé. »", 6, "em-1 pb-1"),
        ]),
        I(3, "ines", "cold-anger",
          "La porte du vestiaire est restée entrouverte. Inès Rey, qui passait chercher son "
          "manteau, s'arrête. « Le « ciment », c'est le monsieur à qui vous avez annoncé un "
          "cancer mardi ? » Un temps. « Il m'a demandé ce matin si vous alliez repasser le "
          "voir. »", [
            R("« Oui. C'était déplacé, et ce n'est pas ce que je pense de lui. Je repasse le "
              "voir lundi matin. »", 7, "rd2 pb2 er1 ic1"),
            R("« C'était une blague entre étudiants, il ne l'a pas entendue. »", 7, "rd-2 pb-2 ic-1"),
            R("Se taire, rouge de honte.", 7, "er-1"),
            R("« Vous avez raison. Et merci de me le dire en face. »", 7, "rd1 ic2 er2"),
            R("« C'est Jonas qui a commencé. »", 7, "ic-2 pb-2 er-1"),
        ]),
        I(4, "jonas", "neutral",
          "Il hausse les épaules. « OK, t'es tendu·e. » Il ferme son casier. « Tu sais ce "
          "qu'on dit : si tu ramènes les patients à la maison, t'as fini dans cinq ans. »", [
            R("« Et si je ne les ramène nulle part, je suis fini·e dans combien de temps ? »",
              5, "er2 em1 ic1"),
            R("« T'as sûrement raison. »", 6, "er-1"),
            R("« Moi, je préfère les ramener un peu, et en parler. »", 5, "er2 ic2"),
            R("« Ou alors on arrête d'en parler et on va boire un verre. »", 6, "er-1 ic-1"),
        ]),
        I(5, "jonas", "sad",
          "Jonas regarde ses chaussures. « Bizarrement, ça allait. Et puis le soir, j'ai "
          "mangé un kebab et je me suis mis à chialer dans le bus. Pour un mec dont je ne "
          "connaissais même pas le prénom. » Il rit, un peu faux.", [
            R("« C'est peut-être justement pour ça. Il n'y avait personne pour le connaître. "
              "Moi aussi, mardi soir, j'ai tourné en rond. »", 7, "em3 er2 co2"),
            R("« Ça arrive à tout le monde. »", 7, "em-1 co-1"),
            R("« Tu devrais voir le psy de l'uni. »", 7, "em-1 ic1"),
            R("« Tu veux qu'on en parle à Inès, vendredi ? »", 7, "ic2 em1"),
        ]),
        I(6, "jonas", "neutral",
          "« Voilà. » Il attrape son sac. « On encaisse, on avance. » Au moment de sortir, il "
          "se retourne. « Au fait, Rey organise un truc en salle de pause le vendredi à "
          "18 h 30. Un débriefing. Les étudiants n'y vont jamais. »", [
            R("« On y va. Tous les deux. »", 8, "ic3 er2 em1"),
            R("« Vas-y si tu veux, moi je rentre. »", 9, "ic-1 er-1"),
            R("« Justement. Allons-y, pour une fois. »", 8, "ic2 er1"),
            R("« Les débriefings, c'est pour les infirmières. »", 9, "ic-3 rd-2"),
        ]),
        I(7, "ines", "neutral",
          "Inès Rey réapparaît dans l'encadrement de la porte, manteau sur le bras. « On fait "
          "un débriefing d'équipe en salle de pause, le vendredi à 18 h 30. Un quart d'heure. "
          "Les étudiants ne viennent jamais. » Elle regarde Jonas, puis vous.", [
            R("« On vient. Tous les deux. »", 8, "ic3 er2 rd1"),
            R("« Je suis épuisé·e. Une autre fois. »", 9, "ic-1"),
            R("« C'est obligatoire ? »", 9, "ic-2 rd-1"),
            R("« Qu'est-ce qu'on y dit, d'habitude ? »", 8, "ic2 cc1"),
        ]),
        I(8, "fatou", "happy",
          "Salle de pause. Inès, Fatou, deux infirmières, et Neuhaus debout près de la "
          "machine à café. Fatou se tourne vers vous. « Le monsieur du 312 a mangé ce midi. "
          "Pour la première fois depuis mardi. Il m'a dit que l'étudiant·e lui avait parlé "
          "« comme à un homme, pas comme à un dossier ». »", [
            R("« Merci de me le dire. C'est grâce à vous et à Inès, aussi : vous m'aviez dit "
              "qu'il avait peur. »", 10, "ic3 rd2 em1"),
            R("« Ah. Ça fait du bien. »", 10, "er1"),
            R("« C'est surtout que la nourriture s'est améliorée. »", 10, "er-1 ic-1 rd-1"),
            R("Sourire, et ne rien dire : laisser à Fatou son moment.", 10, "rd2 ic1"),
        ]),
        I(9, "moreau", "neutral",
          "Dans l'ascenseur, Dr Moreau entre au deuxième. « Alex. Vous partez ? » Les portes "
          "se referment. « Première semaine. Vous avez fait votre première annonce. Qu'est-ce "
          "que vous en faites, ce soir ? »", [
            R("« Je ne sais pas encore. Je crois que j'aurais dû aller au débriefing d'Inès. »",
              11, "er2 ic2"),
            R("« Rien de spécial. C'était une semaine normale. »", 11, "er-2 ic-1"),
            R("« Je vais y repenser tout le week-end, je le sens. »", 11, "er1"),
            R("« Honnêtement ? J'ai un nœud dans le ventre depuis mardi. »", 11, "er3 ic1"),
        ]),
        I(10, "neuhaus", "neutral",
          "Neuhaus pose son gobelet. « Et toi, ça va ? Vraiment ? Pas la version couloir. »", [
            R("« Je n'arrête pas de repenser aux vingt secondes de silence. Je ne savais pas si "
              "je devais parler. »", 12, "er3 ic2 cc1"),
            R("« Ça va, c'est le métier. »", 12, "er-2"),
            R("« Mieux que toi, vu tes cernes. »", 12, "er0 ic-1"),
            R("« Pas terrible. Et toi, comment tu fais, avec toutes tes gardes ? »", 12, "er2 ic2"),
        ]),
        I(11, "moreau", "neutral",
          "Les portes s'ouvrent au rez-de-chaussée. Dr Moreau ne sort pas tout de suite. « On "
          "ne s'habitue pas, Alex. On apprend à porter. Ceux qui confondent les deux tiennent "
          "dix ans, pas trente. » Un signe de tête vers le couloir. « Le débriefing d'Inès, "
          "c'est tous les vendredis. »", [
            R("« J'y serai vendredi prochain. »", END, "er2 ic2"),
            R("« Je note. »", END, "er-1 ic-1"),
            R("« Et vous, qui vous aide à porter ? »", -1, "em2 ic1"),
            R("« Moi, je ne ramène rien à la maison. »", -1, "er-2"),
        ]),
        I(12, "ines", "neutral",
          "Inès vous regarde un moment. « Le silence, c'était juste. Il me l'a dit. » Puis, "
          "plus bas : « La semaine prochaine, vous aurez une famille qui vous demandera de "
          "mentir. Ça arrive toujours la deuxième semaine. »", [
            R("« Alors je viendrai vous voir avant de répondre quoi que ce soit. »", END, "ic3 pb2"),
            R("« Je dirai non, c'est tout. »", END, "pb1 em-1"),
            R("« On verra bien. »", END, "ic-2 er-1"),
            R("« Qu'est-ce que je réponds, ce jour-là ? »", -1, "ic2 pb1"),
        ]),
    ],
)

CH1 = C(1, "Les mots qu'on n'a pas appris",
    situation=(
        "Première semaine de stage au 3ᵉ étage de médecine interne. Alex rencontre "
        "l'équipe — un assistant débordé, une infirmière exigeante, une ASSC qui voit "
        "tout, un co-stagiaire qui plaisante trop — et mène sa première annonce de "
        "diagnostic grave."
    ),
    objectives=(
        "s'intégrer dans une équipe en reconnaissant le savoir des soignant·e·s ; "
        "préparer une annonce (cadre, information disponible, équipe, langue), explorer "
        "ce que le patient sait déjà, délivrer par paliers avec un coup de semonce, "
        "supporter le silence, répondre au pronostic sans mentir, vérifier ce qui a été "
        "compris, reprendre le lendemain ce que la sidération a effacé et accompagner "
        "l'annonce à la famille sans déposséder le patient ; enfin, reconnaître ce que "
        "l'annonce fait à celui ou celle qui la porte."
    ),
    anchoring=(
        "UNIL M1.6 cours-blocs (communication, anamnèse, résolution de cas) et M1.7 droit "
        "médical, éthique de la décision · UNIGE M1 UIDC et AMC Médecine interne, "
        "médecine palliative, enseignement interprofessionnel."
    ),
    focus=("cc", "rd", "em", "ic"),
    scenes=[S1_1, S1_2, S1_3, S1_4, S1_5],
)
