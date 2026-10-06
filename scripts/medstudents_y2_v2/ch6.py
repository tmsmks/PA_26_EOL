"""Chapitre 6 — Le corps donné (mai-juin, puis septembre).

Six scènes jouées, sept écrites :
  6.1 L'examen · 6.2 La dernière visite
  6.3 branche parallèle : « Le fourgon » (la famille s'est apaisée)
      ou « Vous ne l'emmènerez pas »
  6.4 La lettre · 6.5 La cérémonie · 6.6 Septembre
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, StartChoice, go, when

# ---------------------------------------------------------------------------
# 6.1 L'examen
# ---------------------------------------------------------------------------
_INTRO_61 = (
    "Juin. Session d'examens. La grande salle de l'université transformée en salle "
    "d'examen : trois cents tables, trois cents têtes penchées. Examen de fin d'année, quatre "
    "heures. À la pause de 10 h 30, votre téléphone, rallumé dans le couloir, affiche trois "
    "appels manqués : Sandra, Sandra, Sandra."
)

S6_1 = S(1, "6.1 L'examen", _INTRO_61,
    focus=("er", "pb", "co"),
    entries=[
        Entry(20, when(all=["noah_seul"]), _INTRO_61),
        Entry(10, when(all=["noah_aide", "mensonge_portfolio"]), _INTRO_61),
        Entry(12, when(all=["noah_aide", "verite_portfolio"]), _INTRO_61),
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
        I(1, "narr", "",
          "Dans le couloir, entre deux colonnes de casiers, vous rappelez.", [go(2)]),
        I(2, "sandra", "anxious",
          "Sandra décroche à la première sonnerie. « Alex. Jeannine est très faible depuis "
          "cette nuit. Elle ne mange plus, elle dort presque tout le temps. La Dre Golay est "
          "là-bas, avec l'équipe de soins palliatifs. » Un temps. « Elle a demandé après toi. "
          "Deux fois. »", [
            R("« Merci de m'appeler. Qu'est-ce qu'en pense la Dre Golay : c'est une question "
              "d'heures, ou de jours ? »", 3, "cc3 ic2 er1"),
            R("« J'arrive. » Et partir sans repasser par la salle d'examen.", 4,
              "er-2 pb-1 em1", sets=["examen_quitte"]),
            R("« Je ne peux pas, je suis en examen. » Et raccrocher.", 5, "em-2 cc-1"),
            R("« Dis-lui que je viens ce soir. »", 3, "em1 cc1"),
            R("Fondre en larmes, au milieu du couloir.", 7, "er-2"),
        ]),
        I(3, "sandra", "sad",
          "« La Dre dit : des jours, peut-être une semaine. Pas des heures. » Sandra hésite. "
          "« Et Jeannine a dit un truc, ce matin, quand la Dre lui a dit que tu avais ton "
          "examen. » Elle imite la voix de Jeannine, mal, en riant à moitié : « Dites-lui de "
          "finir son examen, sinon je lui botte les fesses. »", [
            R("« Dis-lui que je le finis, et que je viens ce soir. Merci, Sandra. »",
              8, "er2 cc2 rd1", sets=["examen_fini"]),
            R("« Je viens quand même, maintenant. »", 4, "er-1 rd-1",
              sets=["examen_quitte"]),
            R("Aller demander au surveillant ce qui est possible.", 9, "cc1 pb1"),
            R("« D'accord. » Raccrocher, et retourner en salle, la tête ailleurs.",
              8, "er-1", sets=["examen_fini"]),
        ]),
        I(4, "golay", "neutral",
          "Vous laissez votre copie à moitié remplie sur la table 214, votre veste sur la "
          "chaise. Dans le train, puis dans le bus de Montchéry, vous pensez à Jeannine. À la "
          "ferme, à 13 h 30, la Dre Golay vous ouvre la porte. Elle ne dit rien. Elle vous "
          "laisse entrer."),
        I(5, "narr", "",
          "Vous retournez en salle. Vous ne voyez plus les questions. À 11 h 15, vous posez "
          "votre stylo. Vous n'arrivez plus à écrire.", [
            R("Se forcer à continuer, une question après l'autre, en respirant.", 8,
              "er3 pb1", sets=["examen_fini"]),
            R("Rendre la copie, sortir, et rappeler Sandra : « Dis-lui que je viens ce "
              "soir. »", 8, "er1 em1", sets=["examen_fini"]),
            R("Partir en courant.", 4, "er-2", sets=["examen_quitte"]),
            R("Demander au surveillant la permission de sortir téléphoner.", 3, "er1 cc1 ic1"),
        ]),
        I(7, "narr", "",
          "Une étudiante que vous ne connaissez pas vous tend un mouchoir sans rien dire, et "
          "retourne dans la salle. Le téléphone vibre encore : Sandra.", [
            R("Rappeler Sandra, et lui demander ce que dit la Dre Golay.", 3, "er2 cc2"),
            R("Éteindre le téléphone, et retourner en salle.", 8, "er-1 em-1",
              sets=["examen_fini"]),
            R("Partir en courant.", 4, "er-2", sets=["examen_quitte"]),
            R("Appeler Yasmine, pour ne pas rester seul·e avec ça une minute.", 3, "er2 ic1"),
        ]),
        I(8, "narr", "",
          "Vous retournez à la table 214. Pendant deux heures, vous répondez à des questions "
          "sur les reins, les hormones, la reproduction — la filtration glomérulaire, la "
          "créatinine, tout ce que Jeannine vous a appris sans le savoir. À 14 h 30, vous "
          "rendez la copie. Le bus de Montchéry part à 14 h 52."),
        I(9, "narr", "",
          "Le surveillant vous écoute, poliment. « Une patiente ? Pas de la famille ? » Il "
          "hausse les épaules, désolé. « Si vous sortez, vous ne pourrez pas revenir. Vous "
          "serez inscrit·e à la session de rattrapage, en août. C'est votre choix. »", [
            R("Retourner à votre table : Jeannine a dit de finir. Vous irez ce soir.", 8,
              "er2 pb1 rd1", sets=["examen_fini"]),
            R("Sortir : vous passerez le rattrapage en août.", 4, "er1 em1",
              sets=["examen_quitte"]),
            R("« Juste une heure, et je reviens ? » Il refuse. Vous retournez à votre "
              "table.", 8, "pb-1", sets=["examen_fini"]),
            R("« Il est inhumain, votre règlement. »", 8, "er-2 rd-1", sets=["examen_fini"]),
        ]),
        I(10, "noah", "ashamed",
          "Dans le couloir, Noah vous attend, deux cafés à la main. Il vous en tend un. « Tu "
          "as pris un avertissement à cause de moi, en février. Je ne t'avais jamais dit "
          "merci. Ni pardon. » Votre téléphone vibre dans votre poche : Sandra, encore.", [
            R("« Les deux sont acceptés. Et j'ai appris quelque chose, moi aussi : je ne "
              "mentirai plus jamais pour quelqu'un. » Puis rappeler Sandra.", 2,
              "em2 pb2 er1"),
            R("« Tu m'en dois une. » Puis rappeler Sandra.", 2, "em-1 pb-1"),
            R("Prendre le café, et rappeler Sandra sans répondre.", 2, "em-1"),
            R("« C'est ma faute, pas la tienne. J'ai menti tout seul. » Puis rappeler "
              "Sandra.", 2, "pb2 em1"),
        ]),
        I(12, "noah", "happy",
          "Dans le couloir, Noah vous attend, deux cafés à la main. Il vous en tend un. « En "
          "février, tu n'as pas menti pour moi. J'ai mis du temps à comprendre que c'était ça, "
          "être un ami. » Votre téléphone vibre dans votre poche : Sandra, encore.", [
            R("« Et toi, tu as dit la vérité. C'était le plus dur. » Puis rappeler Sandra.",
              2, "em2 rd2"),
            R("« Tu as eu chaud, quand même. » Puis rappeler Sandra.", 2, "em-1"),
            R("Le serrer dans vos bras, et rappeler Sandra.", 2, "em2 co1"),
            R("« Je n'avais pas envie d'avoir des ennuis, surtout. » Puis rappeler Sandra.",
              2, "em-1 rd-1"),
        ]),
        I(20, "narr", "",
          "Sur la porte de la salle, la liste des candidats. Une ligne barrée : « Berthoud "
          "Noah — retrait ». Votre téléphone vibre dans votre poche : Sandra, encore.", [go(2)]),
    ],
)

# ---------------------------------------------------------------------------
# 6.2 La dernière visite
# ---------------------------------------------------------------------------
_INTRO_62 = (
    "Juin, en fin d'après-midi. Les Combettes. À la demande de Jeannine, on a installé le lit "
    "médicalisé dans la cuisine, face à la cour, et la fenêtre est ouverte. Thierry est là, "
    "avec Véronique Bühler, l'infirmière de l'équipe mobile de soins palliatifs. La Dre Golay "
    "vous attend sur le seuil."
)

S6_2 = S(2, "6.2 La dernière visite", _INTRO_62,
    focus=("co", "rd", "er", "ic"),
    entries=[
        Entry(10, when(all=["famille_apaisee", "examen_quitte"]), _INTRO_62),
        Entry(1, when(all=["famille_apaisee"]), _INTRO_62),
        Entry(30, when(all=["examen_quitte"]), _INTRO_62),
    ],
    nodes=[
        I(20, "jeannine", "neutral",
          "Daniel est dans la cour, assis sur le marchepied de son tracteur, moteur éteint. Il "
          "ne rentre pas. Il ne part pas non plus. Dans la cuisine, Jeannine ouvre les yeux "
          "quand vous entrez. « Ah. La fac. » Un souffle. « Vous avez fini… votre "
          "examen ? »", [
            R("« Fini. Pour vous. » Et s'asseoir près du lit.", 2, "em2 rd1 cc1"),
            R("« Oui. » Et regarder par la fenêtre, vers Daniel.", 2, "cc1"),
            R("« Daniel ne rentre pas ? »", 2, "pb-1 em1"),
            R("Aller d'abord parler à Daniel, dans la cour.", 21, "pb-2 em1"),
            R("« Votre fils pourrait faire un effort, aujourd'hui. »", 2, "rd-2 em-1"),
        ]),
        I(1, "daniel", "sad",
          "Daniel est assis à côté du lit, sur une chaise de cuisine trop petite pour lui. Il "
          "tient la main de sa mère. Il vous fait un signe de tête, le premier depuis des "
          "mois. « Elle vous attendait. Elle a demandé si vous aviez fini votre examen. »", [
            R("« Je l'ai fini. Merci de m'avoir fait passer le message. » Et s'approcher du "
              "lit.", 2, "rd2 em1 cc1"),
            R("Saluer Daniel d'un signe de tête, et rester en retrait.", 2, "rd2 pb1"),
            R("« Comment va-t-elle ? »", 2, "cc1 em1"),
            R("Aller droit au lit, sans un mot pour Daniel.", 2, "rd-2 ic-1"),
        ]),
        I(10, "daniel", "sad",
          "Daniel est assis à côté du lit, sur une chaise de cuisine trop petite pour lui. Il "
          "tient la main de sa mère. « Vous n'êtes pas à votre examen ? » Il secoue la tête, "
          "presque amusé. « Elle va vous engueuler. »", [
            R("« Je sais. Je l'ai mérité. » Et s'approcher du lit.", 2, "er1 rd2 em1"),
            R("« Je ne pouvais pas rester là-bas. »", 2, "er1 em1"),
            R("Saluer Daniel, et rester en retrait.", 2, "rd2 pb1"),
            R("« L'examen, ce n'est pas important. »", 2, "er-1 pb-1"),
        ]),
        I(21, "daniel", "resigned",
          "« Retournez à l'intérieur. » Daniel ne lève pas les yeux. « Je rentrerai quand je "
          "pourrai. » Un temps. « Dites-lui… non. Rien. »", [
            R("« D'accord. » Et retourner dans la cuisine.", 2, "pb2 rd2"),
            R("« Elle vous attend. »", 2, "pb-1 em1"),
            R("« Vous allez le regretter. »", 2, "pb-3 rd-2"),
            R("S'asseoir un instant à côté de lui, en silence, puis rentrer.", 2, "em2 pb-1"),
        ]),
        I(30, "jeannine", "neutral",
          "Daniel est dans la cour, sur le marchepied de son tracteur, moteur éteint. Il ne "
          "rentre pas. Dans la cuisine, Jeannine ouvre les yeux quand vous entrez. « Ah. La "
          "fac. » Elle fronce les sourcils. « Il est… quelle heure ? Vous n'êtes pas… à votre "
          "examen ? »", [
            R("« Je suis parti·e. Je voulais être là. »", 31, "er1 em2 cc1"),
            R("« Ils l'ont annulé. »", 31, "cc-3 pb-1"),
            R("« Vous me botterez les fesses plus tard. »", 31, "em2 er1"),
            R("S'asseoir près du lit, sans répondre.", 31, "em1 rd1"),
        ]),
        I(31, "jeannine", "happy",
          "Jeannine soupire, et ça lui coûte. « Petit… » Elle cherche son souffle. « J'ai mis… "
          "six cents enfants au monde. Pas un seul… n'est arrivé à l'heure que j'avais "
          "prévue. » Un sourire. « Vous passerez le rattrapage. Et vous me raconterez. »",
          [go(2)]),
        I(2, "jeannine", "melancholic",
          "Jeannine respire lentement, avec de longues pauses. Véronique ajuste l'oxygène et "
          "vous fait signe : vous pouvez approcher. Océane est assise au pied du lit. Jeannine "
          "tend la main, la pose à plat sur le ventre de sa petite-fille, et la laisse là. "
          "Océane devient toute rouge, puis pleure. Jeannine sourit. « Je l'ai su… avant "
          "elle. Six cents fois. » Puis elle vous regarde. « Approchez. »", [
            R("S'approcher, et s'agenouiller à la hauteur de son visage.", 3, "rd2 em2 co1"),
            R("Rester debout au pied du lit.", 3, "er-1 em-1"),
            R("« Ne vous fatiguez pas à parler, Madame Pittet. »", 3, "rd-2 cc-1"),
            R("Prendre sa main.", 3, "em2 co2"),
        ]),
        I(3, "jeannine", "neutral",
          "Jeannine fait un geste vers la table de nuit. L'enveloppe beige : « À ouvrir "
          "après. » « C'est pour vous. Pas avant. » Elle referme les doigts sur votre main. « Et "
          "à la cérémonie… les étudiants parlent, n'est-ce pas ? » Un souffle. « Dites quelque "
          "chose de bien. Pour tous. Pas pour moi. »", [
            R("« Je vous le promets. Pour tous. » Et prendre l'enveloppe.", 4, "rd2 co2 pb1"),
            R("« Je dirai votre nom. Tout le monde saura ce que vous avez fait. »",
              5, "pb-3 rd-2"),
            R("Prendre l'enveloppe, incapable de répondre.", 4, "co1 er-1"),
            R("« Je ne suis pas sûr·e d'être choisi·e pour parler. »", 4, "cc1 er-1"),
            R("L'ouvrir tout de suite, devant elle.", 5, "rd-3 pb-2"),
        ]),
        I(4, "buhler", "neutral",
          "Véronique Bühler vous fait signe de la suivre sur le seuil. « Elle dort, maintenant. "
          "Ça peut être ce soir, ou dans trois jours. Ses réserves sont prêtes : morphine pour "
          "le souffle, midazolam si elle s'agite. Thierry et moi, on se relaie. » Elle vous "
          "regarde. « Vous voulez rester ? Vous pouvez. Mais vous pouvez aussi rentrer : vous "
          "lui avez dit au revoir, je l'ai vu. »", [
            R("« J'aimerais rester un peu, si la famille est d'accord. Je ne veux prendre la "
              "place de personne. »", 6, "rd2 pb2 em1"),
            R("« Je reste jusqu'au bout. »", 6, "pb-2 em1"),
            R("« Je rentre. Appelez-moi si… »", 7, "er1 pb1"),
            R("« Je peux faire quelque chose ? Une injection ? »", 6, "pb-3 ic-1"),
            R("« Comment vous faites, vous, pour faire ça tous les jours ? »", 8, "ic1 er1"),
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
        I(6, "narr", "",
          "Vous restez jusqu'à la nuit. Océane s'est endormie sur le canapé, la main sur son "
          "ventre. Thierry fait du café que personne ne boit. Jeannine respire, de longues "
          "pauses, puis encore. À 22 h, Véronique vous dit doucement : « Rentrez. Vous "
          "reviendrez demain. Elle sait que vous êtes venu·e. »"),
        I(7, "narr", "",
          "Dans le bus du soir, vous tenez l'enveloppe sur vos genoux, sans l'ouvrir. « À "
          "ouvrir après. » L'écriture est penchée, appliquée : celle d'une femme qui a rempli "
          "des carnets de naissance pendant quarante ans."),
        I(8, "buhler", "neutral",
          "Véronique sourit. « On ne fait pas ça tous les jours. On le fait un jour après "
          "l'autre. » Elle regarde la cuisine, le lit, la fenêtre ouverte. « Et on n'est "
          "jamais seule : Thierry, la Dre Golay, la famille. Vous. » Elle vous rend votre sac. "
          "« Alors, vous restez, ou vous rentrez ? »", [
            R("« Je reste un peu, si la famille est d'accord. »", 6, "rd2 pb2"),
            R("« Je rentre. Merci. »", 7, "er1"),
            R("« Je reste toute la nuit, avec elle. »", 6, "pb-2"),
            R("« Je ne sais pas. »", 7, "er-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.3 Le fourgon — branche « la famille s'est apaisée »
# ---------------------------------------------------------------------------
S6_3A = S(3, "6.3 Le fourgon",
    "Trois jours plus tard, 5 h 40. Thierry vous appelle : Jeannine est morte à 4 h 50, la "
    "fenêtre ouverte, Daniel à côté d'elle. Le fourgon de l'institut d'anatomie viendra à "
    "9 h. « Tu peux venir, si tu veux. Daniel a dit oui. »",
    focus=("co", "ic", "rd"),
    slot="6.3",
    cond=when(all=["famille_apaisee"]),
    nodes=[
        I(1, "narr", "",
          "Quand vous arrivez, la cuisine est calme. Jeannine est dans le lit, les mains "
          "croisées sur le drap, le foulard rouge noué. Véronique et Thierry ont fait la "
          "toilette. Océane a peint les ongles de sa grand-mère : rouge. Daniel est assis ; il "
          "ne pleure pas. Il vous fait signe d'entrer.", [
            R("S'approcher du lit, et regarder Jeannine un long moment, en silence.",
              2, "rd3 co2 er1"),
            R("Présenter vos condoléances à Daniel, puis à Océane, simplement.",
              2, "rd2 em2 co1"),
            R("« Elle a l'air paisible. »", 2, "em1 cc-1"),
            R("Chercher son pouls, comme on vous l'a appris, pour constater le décès.",
              3, "pb-3 rd-2"),
            R("Fondre en larmes.", 2, "er-1 co1"),
        ]),
        I(2, "oceane", "sad",
          "Océane vous montre les mains de sa grand-mère. « Elle m'a dit, la semaine passée : "
          "« Tu me feras les ongles, pour partir. En rouge. Les étudiants doivent voir que "
          "quelqu'un a pris soin de moi. » » Elle renifle. « Je ne savais pas que ça voulait "
          "dire quelque chose. »", [
            R("« Elle voulait qu'on sache que quelqu'un l'avait aimée. C'est vrai. Et ils le "
              "verront. »", 4, "co3 em2 rd1"),
            R("« Ça veut dire beaucoup. En septembre, sur la table, la première chose que j'ai "
              "remarquée, c'étaient des ongles vernis. »", 4, "co3 rd1 pb-1"),
            R("« C'est un peu morbide, non ? »", 4, "rd-3 em-2"),
            R("Hocher la tête, la gorge serrée.", 4, "em1 co1"),
            R("« Les étudiants ne sauront pas que c'est elle : c'est anonyme. »",
              4, "cc1 em-1"),
        ]),
        I(3, "golay", "neutral",
          "La Dre Golay pose une main sur votre poignet. « C'est fait, Alex. À 5 h 10, par "
          "moi. » Elle ne lâche pas votre poignet tout de suite. « Aujourd'hui, vous n'êtes pas "
          "là pour faire. Vous êtes là pour être là. »", [
            R("« Pardon. » Et reculer d'un pas.", 2, "rd2 er1 pb1"),
            R("« C'est le réflexe. »", 2, "er-1"),
            R("Se taire, et rester près d'elle.", 2, "er1 rd1"),
            R("« Je voulais juste être sûr·e. »", 2, "pb-1 er-1"),
        ]),
        I(4, "narr", "",
          "À 9 h, le fourgon de l'institut d'anatomie se gare dans la cour. Deux hommes en "
          "costume sombre, un brancard, une housse. Ils parlent bas ; ils demandent la "
          "permission pour tout. Daniel se lève. Il ouvre en grand la porte de la cuisine, et "
          "il la tient. Il ne dit rien. Il tient la porte.", [
            R("Se placer en retrait, à côté d'Océane, et laisser la famille accompagner "
              "Jeannine jusqu'au fourgon.", 5, "rd3 pb2"),
            R("Aider les deux hommes à porter le brancard.", 5, "pb-2 ic1"),
            R("Poser la main sur l'épaule d'Océane.", 5, "em2 co1"),
            R("Prendre une photo du fourgon.", 5, "rd-3 pb-3"),
            R("Sortir avant, pour ne pas voir.", 5, "er-1 co-1"),
        ]),
        I(5, "daniel", "resigned",
          "Le fourgon démarre lentement, dans le gravier. Daniel le regarde jusqu'au virage. "
          "Puis il se tourne vers vous. « Elle disait que vous l'écoutiez. » Il remet sa "
          "casquette. « Faites-en quelque chose. »", [
            R("« Je vous le promets. »", END, "co2 rd2"),
            R("Lui serrer la main.", END, "rd2 em1"),
            R("« Elle va beaucoup nous apprendre. »", END, "pb-1 em-1"),
            R("Se taire, et regarder le virage, à côté de lui.", END, "em2 co1"),
            R("« Vous avez été courageux. »", END, "em1 pb-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.3 « Vous ne l'emmènerez pas » — branche « la famille s'est déchirée »
# ---------------------------------------------------------------------------
S6_3B = S(4, "6.3 Vous ne l'emmènerez pas",
    "Trois jours plus tard, 6 h. Thierry vous appelle : Jeannine est morte à 4 h 50, la "
    "fenêtre ouverte. Daniel était dans la cour ; il est entré à 5 h, quand Thierry l'a "
    "appelé. Le fourgon de l'institut d'anatomie doit venir à 9 h. « Daniel dit qu'il ne la "
    "laissera pas partir. La Dre Golay est là. Viens, si tu peux. »",
    focus=("rd", "pb", "ic", "er"),
    slot="6.3",
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
            R("Rester en retrait, près d'Océane, et laisser la Dre Golay mener.",
              2, "pb2 ic2 em1"),
            R("« Monsieur Pittet, c'était sa volonté : c'est écrit. »", 3, "pb-2 rd-1 em-2"),
            R("S'asseoir à côté d'Océane.", 2, "em2 co1"),
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
            R("« C'est injuste pour l'institut. »", 5, "rd-2 em-2"),
        ]),
        I(3, "daniel", "cold-anger",
          "Daniel se tourne vers vous. « Vous. » Sa voix tremble. « Vous voulez la découper "
          "vous-même ? » Thierry fait un pas, et se place entre vous deux, sans un mot.", [
            R("« Non. Pardon. Ce n'est pas à moi de parler. » Et reculer près d'Océane.",
              2, "pb3 rd2 er1"),
            R("« Ce ne sera pas moi qui la découperai. »", 5, "cc-2 rd-1"),
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
            R("Sortir, pour leur laisser ce moment.", 7, "rd2 pb2"),
        ]),
        I(5, "golay", "cold-anger",
          "La Dre Golay vous regarde par-dessus ses lunettes. « Alex. Dehors. » Ce n'est pas "
          "une punition : c'est une évidence. Dans la cour, le soleil se lève sur le gravier. "
          "Par la fenêtre ouverte, vous entendez Océane parler à son père, sans comprendre les "
          "mots.", [
            R("Attendre dans la cour, en silence, sans chercher à entendre.", 7, "rd2 pb2 er1"),
            R("Revenir près de la porte, pour écouter.", 7, "pb-2 rd-1"),
            R("Écrire à Yasmine : « je viens de tout gâcher ».", 7, "er1 ic1"),
            R("Partir.", 8, "er-1"),
        ]),
        I(7, "narr", "",
          "À 9 h, le fourgon de l'institut se gare dans la cour. Daniel sort. Il parle "
          "longtemps avec les deux hommes en costume sombre. Puis il revient vers la cuisine. "
          "Il ne dit rien. Il ouvre la porte en grand, et il la tient. Il ne pleure pas. Il "
          "tient la porte.", [
            R("Rester en retrait, à côté d'Océane.", 9, "rd3 pb1"),
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
            R("« Je vous le promets. »", END, "co2 rd2"),
            R("Lui serrer la main, en silence.", END, "rd2 em1"),
            R("« Vous avez fait le bon choix. »", END, "pb-2 em-1"),
            R("S'asseoir à côté de lui, un moment, sans rien dire.", END, "em2 co1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.4 La lettre
# ---------------------------------------------------------------------------
_LETTRE = (
    "Le soir, chez vous, vous ouvrez l'enveloppe beige. Une feuille de cahier, l'écriture "
    "penchée de Jeannine, datée de septembre, avec des ajouts à l'encre bleue. « Petit, ou "
    "petite — je n'ai jamais su, avec vous, et ça m'est égal. Si vous lisez ceci, c'est que "
    "je suis partie, et que mon corps est chez vous, à la fac. Vous ne le verrez pas : c'est "
    "la règle, et c'est bien. Je voulais vous dire une chose que j'ai apprise en quarante ans "
    "de naissances : on ne soigne jamais un corps. On soigne quelqu'un qui habite dedans, et "
    "ceux qui l'attendent dehors. »"
)
_SIGNATURE = " « Faites-le avec les autres. J. P. »"

S6_4 = S(5, "6.4 La lettre",
    _LETTRE + " « Vous l'avez fait, avec moi. »" + _SIGNATURE,
    focus=("co", "er", "rd"),
    entries=[
        Entry(1, when(all=["revele_a_daniel"]), _LETTRE + " (À l'encre bleue : « Vous "
              "avez dit à Daniel ce que je voulais lui dire moi-même. J'ai été très en colère. "
              "Et puis, ça nous a obligés à parler, lui et moi, plus tôt que je ne l'aurais "
              "fait. Je ne vous remercie pas. Mais je vous pardonne. »)" + _SIGNATURE),
        Entry(1, when(all=["erreur_homonyme"]), _LETTRE + " (À l'encre bleue : « Le cousin "
              "Jean-Paul a su avant mon fils. Ça, je ne l'oublierai pas. Vous non plus, "
              "j'espère : c'est comme ça qu'on apprend. »)" + _SIGNATURE),
        Entry(1, when(all=["oceane_trahie"]), _LETTRE + " (À l'encre bleue : « Océane m'a "
              "raconté, pour la grange. Vous avez cru bien faire. Une grossesse, c'est à la "
              "femme de l'annoncer, à qui elle veut, quand elle veut. Considérez que c'est "
              "mon dernier cours. »)" + _SIGNATURE),
        Entry(1, when(all=["promesse_jeannine"]), _LETTRE + " (À l'encre bleue : « Vous "
              "m'aviez promis que personne ne saurait jamais. Je savais que c'était "
              "impossible, et vous aussi. Ne promettez plus jamais l'impossible à un malade : "
              "il vous croit. »)" + _SIGNATURE),
        Entry(1, when(all=["numero_donne"]), _LETTRE + " (À l'encre bleue : « Votre numéro, "
              "je l'ai gardé sur le frigo jusqu'à ce que la Dre le remplace par les bons. Vous "
              "étiez gentil·le de me le donner, et c'était une bêtise. Les deux à la "
              "fois. »)" + _SIGNATURE),
        Entry(1, when(all=["oceane_orientee"]), _LETTRE + " (À l'encre bleue : « Merci pour "
              "la grange. Océane m'a tout raconté. Elle a dit : « Il ne m'a pas dit quoi "
              "faire », ou « elle », je ne sais plus. C'est le plus beau compliment qu'on "
              "puisse faire à un soignant. »)" + _SIGNATURE),
    ],
    nodes=[
        I(1, "narr", "",
          "Vous relisez la lettre trois fois. Puis vous la repliez, et vous la rangez dans "
          "votre carnet de stage, entre la page de septembre et celle de juin.", [
            R("La relire une quatrième fois, à voix haute, pour vous seul·e.", 2, "er2 co1"),
            R("Pleurer, enfin.", 2, "er2 co1"),
            R("La photographier pour la poster en story, avec « RIP ».", 3, "rd-3 pb-3"),
            R("Appeler Yasmine, ou Léo, pour ne pas rester seul·e ce soir.", 2, "er2 ic2"),
            R("La ranger, sans la relire.", 2, "er-1"),
        ]),
        I(2, "vautier", "neutral",
          "Le lendemain, la Pre Vautier vous fait venir dans son bureau. « La cérémonie "
          "d'hommage a lieu dans dix jours. Chaque année, un étudiant ou une étudiante de "
          "deuxième année prend la parole au nom de sa volée. La table 14 vous a "
          "désigné·e. » Elle croise les mains. « La Dre Golay m'a dit que vous aviez accompagné "
          "une donneuse cette année, en stage. Je ne veux pas savoir qui. Vous ne direz pas "
          "qui. Mais je crois que vous avez quelque chose à dire. Vous acceptez ? »", [
            R("« J'accepte. Et je ne dirai le nom de personne. »", 4, "rd2 pb2 er1"),
            R("« Je ne suis pas sûr·e d'en être capable. »", 5, "er1"),
            R("« J'accepte. Je parlerai de celle que j'ai connue : sa famille sera dans la "
              "salle, ce sera beau. »", 6, "pb-3 rd-2"),
            R("« Pourquoi moi ? Maëlle parle beaucoup mieux que moi. »", 5, "er-1 ic1"),
            R("« Non. »", 7, "er-1 ic-1"),
        ]),
        I(3, "narr", "",
          "Vous ouvrez Instagram. Votre pouce reste au-dessus du bouton « Partager ». Sur "
          "l'écran : l'écriture penchée de Jeannine, et votre propre reflet. Vous pensez à une "
          "hirondelle sur un drap blanc.", [
            R("Supprimer le brouillon. Ranger le téléphone.", 2, "rd3 pb2 er1"),
            R("Publier, en « amis proches » seulement.", 9, "rd-3 pb-3"),
            R("La garder en brouillon, « pour plus tard ».", 2, "pb-1 rd-1"),
            R("L'envoyer à Maëlle, pour avoir son avis.", 2, "pb-2 rd-2"),
        ]),
        I(4, "vautier", "neutral",
          "La Pre Vautier hoche la tête. « Bien. Trois minutes. Pas de nom, aucun détail qui "
          "permette de reconnaître quelqu'un — ni un donneur, ni un patient. Vous parlez à des "
          "familles qui ne savent pas ce qu'on a fait de leurs morts. Dites-leur ce qu'on en a "
          "fait. » Elle sourit, une seconde. « Et ne citez pas l'atlas. »", [
            R("« Je dirai ce qu'ils nous ont appris. Que derrière chaque corps, il y avait "
              "quelqu'un qui en avait pris soin. »", END, "rd2 co2 cc1"),
            R("« Je dirai aussi qu'on a ri, parfois, et que ce n'était pas toujours bien. »",
              END, "rd2 pb2 cc2"),
            R("« Je ferai court. »", END, "cc1"),
            R("« Je peux parler de ma patiente, sans son nom ? »", END, "pb-1 cc1"),
            R("« Je raconterai l'histoire de la story Instagram : ça fera rire. »",
              END, "rd-3 pb-2"),
        ]),
        I(5, "vautier", "neutral",
          "« C'est exactement pour ça que je vous le demande. » La Pre Vautier pousse vers vous "
          "le livre des donneurs, ouvert à la page de la table 14. « Ceux qui sont sûrs d'en "
          "être capables parlent d'eux-mêmes. Vous, vous parlerez d'eux. »", [
            R("« D'accord. J'essaierai. Sans nom. »", 4, "rd2 er2 pb1"),
            R("« Je vais y réfléchir. »", 4, "er1"),
            R("« Vous me forcez la main. »", 4, "er-2 rd-1"),
            R("Feuilleter le livre, et accepter d'un signe de tête.", 4, "rd2 er1"),
        ]),
        I(6, "vautier", "cold-anger",
          "La Pre Vautier pose son stylo. « Non. » Un seul mot. Puis : « Cette personne a "
          "donné son corps sans son nom. Comme tous les autres. Sa famille sera peut-être dans "
          "la salle, et elle a le droit de pleurer sans que deux cents personnes se "
          "retournent. Si vous dites son nom, vous lui reprenez ce qu'elle a donné. » Elle "
          "attend. « Alors ? »", [
            R("« Vous avez raison. Pas de nom. Pour tous. D'ailleurs, elle me l'avait "
              "demandé. »", 4, "rd3 pb3 er1"),
            R("« Mais c'était une personne extraordinaire. »", 4, "pb-2 rd-1"),
            R("« D'accord. » Sans conviction.", 4, "pb1 er-1"),
            R("« Alors je ne parlerai pas. »", 7, "er-2 ic-1"),
        ]),
        I(7, "leo", "anxious",
          "La Pre Vautier ne dit rien. En sortant, vous croisez Léo dans le couloir ; il tient "
          "trois feuilles, en français et en allemand, et il a l'air terrifié. « Ils m'ont "
          "demandé de parler, si tu refuses. Je n'y arriverai pas en français. » Il vous "
          "regarde. « On le fait à deux ? Moi en allemand, toi en français ? »", [
            R("« À deux. Et sans nom. »", 4, "ic3 rd1 er1"),
            R("« D'accord. Mais c'est toi qui commences. »", 4, "ic1 er1"),
            R("« Débrouille-toi, Léo. »", 4, "ic-3 em-2"),
            R("« Je ne sais pas… Bon. D'accord. »", 4, "er-1"),
        ]),
        I(9, "oceane", "angry",
          "Une heure plus tard, un message d'Océane, sur Instagram : « Supprime ça. Tout de "
          "suite. C'est la lettre de mamie. » Vous supprimez. Trop tard pour Océane : elle ne vous écrira "
          "plus.", [go(2)]),
    ],
)

# ---------------------------------------------------------------------------
# 6.5 La cérémonie
# ---------------------------------------------------------------------------
_INTRO_65 = (
    "Fin juin, 17 h. L'aula de l'institut d'anatomie, des fleurs blanches, un quatuor "
    "d'étudiants. Au premier rang, les familles des donneuses et des donneurs de l'année. "
    "Derrière, toute la volée de deuxième année. La Pre Vautier ouvre la cérémonie. Dans "
    "cinq minutes, ce sera à vous."
)

S6_5 = S(6, "6.5 La cérémonie", _INTRO_65,
    focus=("rd", "co", "pb", "er"),
    entries=[
        Entry(20, when(all=["rencontre_rapin"]), _INTRO_65),
        Entry(30, when(all=["photo_virale"]), _INTRO_65),
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
          "Au troisième rang, une vieille dame porte une broche en forme d'hirondelle au revers "
          "de son manteau gris. Vous ne la connaissez pas. Vous comprenez quand même.", [
            R("Ne rien faire de ce que vous croyez savoir, et monter sur l'estrade.",
              1, "pb3 rd2"),
            R("Aller lui parler avant la cérémonie : « Je crois que j'ai connu votre "
              "mère. »", 1, "pb-3 rd-2 em1"),
            R("Fixer la broche, incapable de penser à autre chose.", 1, "er-2"),
            R("Chercher Maëlle des yeux.", 1, "ic1"),
        ]),
        I(20, "rapin", "neutral",
          "Au troisième rang, une femme en manteau gris, une broche en forme d'hirondelle au "
          "revers : Mme Rapin. Elle vous a reconnu·e. Elle vous fait un petit signe de tête, "
          "comme on encourage quelqu'un avant de monter sur scène.", [
            R("Lui rendre son signe de tête, et monter sur l'estrade.", 1, "rd2 er1 co1"),
            R("Détourner les yeux.", 1, "er-1 rd-1"),
            R("Aller lui parler avant de monter.", 1, "pb-1 em1"),
            R("Lui sourire, et respirer.", 1, "er2 rd1"),
        ]),
        I(30, "narr", "",
          "Au troisième rang, une femme en manteau gris porte une broche en forme d'hirondelle. "
          "Vous ne l'avez jamais vue. Vous savez qui elle est.", [
            R("Ne rien faire de ce que vous savez, et monter sur l'estrade.", 1, "pb3 rd2"),
            R("Aller lui présenter des excuses, avant la cérémonie.", 1, "pb-2 em1"),
            R("Fixer la broche, incapable de penser à autre chose.", 1, "er-2"),
            R("Chercher Maëlle des yeux.", 1, "ic1"),
        ]),
        I(1, "narr", "",
          "Vous montez sur l'estrade. Deux cents visages. Au premier rang, Océane, une main "
          "posée sur son ventre arrondi, vous regarde. Vous dépliez votre feuille. Vos mains "
          "tremblent comme en septembre, devant le premier drap blanc.", [
            R("Commencer par les mots du texte des donneurs, lus en septembre : « … nos "
              "premiers maîtres, sans jamais nous entendre les remercier. » Puis : "
              "« Aujourd'hui, nous vous remercions. »", 2, "rd3 cc2 er1"),
            R("Commencer par une blague, pour détendre la salle.", 3, "rd-2 er-1"),
            R("Lire la feuille d'une traite, sans lever les yeux.", 2, "cc-1 er1"),
            R("Commencer par l'histoire de Jeannine, sans son nom : le village, la ferme, les "
              "six cents enfants.", 4, "pb-3 rd-2 cc1"),
            R("Commencer par « Pardon », au nom de la table 14, pour ce qui n'a pas toujours "
              "été digne.", 2, "rd2 pb2 cc1"),
        ]),
        I(2, "narr", "",
          "Vous parlez des mains, des cœurs qui ont tenu, de ce qu'on apprend d'un corps qu'on "
          "ne verra jamais vivant. Vous parlez de ceux qui en avaient pris soin jusqu'au bout. "
          "La salle est silencieuse. Au moment de conclure, la phrase que vous n'aviez pas "
          "écrite vient toute seule : le nom de Jeannine, ses six cents enfants, la ferme des "
          "Combettes. Elle est là, sur vos lèvres.", [
            R("La garder pour vous. Conclure : « Nous ne connaîtrons jamais vos noms. Nous "
              "n'oublierons jamais ce que vous nous avez appris. Merci. »", 5,
              "rd3 pb3 co2 cc1"),
            R("La dire : « Elle s'appelait Jeannine. »", 6, "pb-3 rd-3 co-1",
              sets=["nom_prononce"]),
            R("Dire, sans aucun nom : « Cette année, j'ai aussi connu une donneuse vivante. "
              "Elle m'a appris à soigner quelqu'un, pas un corps. »", 5, "pb1 co2 cc1"),
            R("Se taire, longtemps, puis : « Merci. »", 5, "rd2 er1"),
        ]),
        I(3, "narr", "",
          "Personne ne rit. Au premier rang, une dame âgée baisse la tête. La Pre Vautier ne "
          "bouge pas. Vous avez trois minutes, et vous venez d'en perdre une.", [
            R("S'arrêter. « Pardon. Je recommence. » Et reprendre avec les mots du texte des "
              "donneurs.", 2, "rd2 er2 cc1"),
            R("Continuer, comme si de rien n'était.", 2, "er-1"),
            R("Faire une deuxième blague, pour rattraper la première.", 2, "rd-2 er-2"),
            R("Lire la suite très vite.", 2, "cc-1 er-1"),
        ]),
        I(4, "narr", "",
          "Au premier rang, Océane se raidit. Dans la salle, deux ou trois personnes de "
          "Montchéry échangent un regard : une sage-femme, une ferme, six cents enfants. La "
          "Pre Vautier se soulève à moitié de sa chaise.", [
            R("S'interrompre : « Pardon. Je n'aurais pas dû entrer dans les détails. Ce "
              "qu'elle m'a appris, c'est pour vous tous. » Puis revenir à tous les "
              "donneurs.", 2, "pb2 rd2 er1"),
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
              "rd2 pb1 er1"),
            R("Descendre, et quitter la salle.", 8, "er-2 rd-1"),
            R("Ajouter, au micro : « Je voulais juste lui rendre hommage. »", 8, "pb-2 er-1"),
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
            R("La serrer dans vos bras.", 9, "em2 co1"),
            R("« Tu en as parlé à ton père ? »", 9, "pb-2 em-1"),
        ]),
        I(8, "oceane", "cold-anger",
          "Océane vous attend devant la porte. Elle ne crie pas. « Mamie l'a donné sans son "
          "nom. Comme les autres. Toute sa vie, elle a laissé les autres sur le devant de la "
          "scène. » Elle tient son ventre. « Tu lui as repris ça. »", [
            R("« Tu as raison. Je n'avais pas le droit. Je suis désolé·e. »", 9, "rd2 pb2 er1"),
            R("« Je voulais lui rendre hommage. »", 9, "pb-2 em-1"),
            R("Baisser les yeux.", 9, "er-1"),
            R("« Personne ne fera le lien. »", 9, "pb-3 cc-2"),
        ]),
        I(9, "vautier", "neutral",
          "La salle se vide. La Pre Vautier range le livre des donneurs dans sa housse. « Vous "
          "savez ce que j'aime, dans cette cérémonie ? Elle ne sert à rien. Les morts "
          "n'entendent pas. » Elle referme la housse. « Elle sert aux vivants. Aux familles, à "
          "vous, à moi. On y apprend à remercier quelqu'un qu'on ne connaîtra jamais. C'est "
          "peut-être la chose la plus médicale que je vous aie apprise. »"),
    ],
)

# ---------------------------------------------------------------------------
# 6.6 Septembre
# ---------------------------------------------------------------------------
_INTRO_66 = (
    "Fin septembre. Le dernier jour du cabinet de Montchéry. Des cartons partout ; la plaque "
    "déjà dévissée, posée contre le mur. Vous êtes en troisième année, maintenant. Vous avez "
    "demandé à venir aider."
)

S6_6 = S(7, "6.6 Septembre", _INTRO_66,
    focus=("er", "pb", "co"),
    entries=[
        Entry(10, when(all=["oceane_orientee"]), _INTRO_66),
        Entry(20, when(all=["oceane_trahie"]), _INTRO_66),
    ],
    nodes=[
        I(30, "sandra", "neutral",
          "Sandra emballe le tensiomètre. « Océane est passée hier, pour dire au revoir à la "
          "Dre. Elle a un joli ventre, maintenant. » Elle ferme le carton. « Elle a demandé de "
          "tes nouvelles. Elle a dit : « Dis-lui que je me suis débrouillée. Toute "
          "seule. » »", [
            R("« Dis-lui que j'en suis heureux·se. Et que j'aurais dû lui donner un numéro, ce "
              "soir-là, pas seulement mon silence. »", 1, "em2 pb1 er1"),
            R("« Tant mieux. »", 1, "em-1"),
            R("« Elle aurait pu m'appeler. »", 1, "pb-1 em-2"),
            R("Sourire, sans répondre.", 1, "em1"),
        ]),
        I(10, "oceane", "happy",
          "En fin de matinée, la Twingo cabossée se gare devant le cabinet. Océane, les "
          "cheveux redevenus châtains, une échographie à la main. « C'est une fille. » Elle "
          "rit. « Jeanne. Papa trouve que c'est un prénom de vieille. Il a pleuré quand "
          "même. » Elle vous regarde. « Merci pour la grange. »", [
            R("« Merci à toi. Jeanne, c'est parfait. »", 1, "em2 co1 rd1"),
            R("« Ton père est au courant, alors ! »", 1, "pb-1 em1"),
            R("« Je peux voir l'échographie ? »", 1, "em1"),
            R("« Tu vas t'en sortir, seule, avec un bébé ? »", 1, "rd-2 em-1"),
        ]),
        I(20, "sandra", "sad",
          "Sandra emballe le tensiomètre. « Océane est passée hier, pour dire au revoir à la "
          "Dre. Elle a demandé si tu serais là aujourd'hui. » Elle ferme le carton. « Quand "
          "j'ai dit oui, elle a dit qu'elle repasserait une autre fois. » Elle vous regarde. "
          "« Ça lui passera, peut-être. Ou pas. »", [
            R("« Elle a raison de m'en vouloir. Si un jour elle veut me parler, je serai là. "
              "Sinon, c'est son droit. »", 1, "rd2 er2 pb1"),
            R("« Je pourrais lui écrire. »", 1, "pb-1 em1"),
            R("« Elle exagère. »", 1, "rd-2 em-2"),
            R("Se taire, et continuer d'emballer.", 1, "er1"),
        ]),
        I(1, "golay", "melancholic",
          "La Dre Golay décroche le dernier cadre : un dessin d'enfant, une maison, un soleil, "
          "une femme en blouse. « Mon fils, à cinq ans. Jeannine l'a mis au monde. » Elle le "
          "range dans un carton marqué « Maison ». « Vingt-cinq ans. Tout tient dans onze "
          "cartons. » Elle vous regarde. « Et vous, qu'est-ce que vous emportez de cette "
          "année ? »", [
            R("« Que soigner, ce n'est pas soigner des corps. C'est soigner ceux qui les "
              "habitent, et ceux qui les attendent dehors. »", 2, "er2 co2 rd2 cc2 ic1"),
            R("« Une date de naissance avant chaque phrase au téléphone. « Pause réelle » au "
              "fond de la gorge. Et une lettre, dans mon carnet. »", 2, "er2 cc2 rd1"),
            R("« De bons souvenirs. »", 2, "cc-1"),
            R("« Je ne sais pas encore. »", 2, "er1"),
            R("« Surtout que je ne veux plus jamais faire la moindre erreur. »",
              2, "er-2 cc-1"),
        ]),
        I(2, "sandra", "happy",
          "Sandra vous tend un post-it jaune, à moitié décollé, le bord gondolé : « PITTET J. = "
          "2 ! DATE DE NAISSANCE ! » « Il était collé sur mon écran depuis octobre. Prends-le. "
          "Colle-le partout où tu iras. »", [
            R("« Partout. Promis. » Et le ranger dans le carnet, à côté de la lettre.",
              3, "ic2 em2"),
            R("« Je n'en ai plus besoin, j'ai compris. »", 3, "ic-1 er-1"),
            R("Rire, et serrer Sandra dans vos bras.", 3, "em2 ic1"),
            R("« C'est un peu ridicule, non ? »", 3, "ic-2 rd-1"),
        ]),
        I(3, "golay", "neutral",
          "La Dre Golay ferme la porte du cabinet à clé, pour la dernière fois. Elle tend la "
          "clé à Sandra, qui la rendra à la commune. Puis elle se tourne vers vous, sur le "
          "trottoir. Elle ne dit pas « Tu reviendras ? ». Elle dit : « Allez apprendre. Et le "
          "jour où vous ne saurez plus pourquoi vous faites ce métier, relisez votre "
          "lettre. »", [
            R("La serrer dans vos bras.", 4, "em2 co1 rd1"),
            R("« Merci, Docteure. Pour tout. »", 4, "rd2 er1"),
            R("« Et vous, vous allez faire quoi, maintenant ? »", 5, "em2 cc1"),
            R("Partir sans vous retourner : c'est trop dur.", 4, "er-1 rd-1"),
        ]),
        I(4, "narr", "",
          "Vous prenez le bus de Montchéry une dernière fois. Au premier virage, on voit les "
          "Combettes : la cour, la grange, la fenêtre de la cuisine. Quelqu'un l'a laissée "
          "ouverte. Dans votre carnet, entre la page de septembre et celle de juin, il y a une "
          "lettre, un post-it jaune, et le dessin de trois pontages, avec, au crayon, "
          "dessous : « Elle a tenu. »"),
        I(5, "golay", "happy",
          "« Moi ? » Elle rit. « Je vais apprendre à ne rien faire. Ça va être très difficile. » "
          "Elle regarde la rue. « Et le jeudi, j'irai donner un coup de main au centre de santé "
          "d'Orbe. Une demi-journée. On ne se refait pas. »", [go(4)]),
    ],
)

CH6 = C(6, "Le corps donné",
    situation=(
        "Juin, puis septembre. L'examen de fin d'année, et un téléphone qui sonne pendant la "
        "pause. La dernière visite aux Combettes, une enveloppe « à ouvrir après », un "
        "fourgon dans la cour. Et la cérémonie d'hommage aux donneurs, où c'est vous qui "
        "parlez."
    ),
    objectives=(
        "décider sous la pression émotionnelle en vérifiant d'abord la réalité de l'urgence "
        "et la volonté de la personne ; accompagner une fin de vie à domicile sans prendre la "
        "place de la famille ni de l'équipe de soins palliatifs ; respecter la volonté d'une "
        "donneuse et la place de sa famille au moment du départ du corps ; recevoir une "
        "critique et un pardon ; parler en public au nom de sa volée en respectant "
        "l'anonymat des donneuses et des donneurs ; dire ce qu'on emporte d'une année de "
        "formation."
    ),
    anchoring=(
        "UNIL BMed2.6 (urogénital et homéostasie, hormones de la reproduction) et BMed2.10 "
        "(fin des travaux pratiques d'anatomie) · UNIGE Reproduction, identité "
        "professionnelle · UZH Humanbiologie II (Reproduktion), Praktikum klinische "
        "Anatomie II · dans les trois facultés : cérémonie d'hommage aux donneuses et aux "
        "donneurs du corps."
    ),
    focus=("co", "rd", "er", "pb"),
    start_choice=StartChoice(
        unless_any=["famille_apaisee", "famille_dechiree"],
        question=(
            "Ce chapitre fait suite à la réunion de famille d'avril aux Combettes (chapitre 5), "
            "que vous n'avez pas jouée sur cet appareil. Comment s'est-elle terminée ?"
        ),
        options=[
            ("Daniel a pris la main de sa mère : il ne s'opposera pas au don. Océane, "
             "enceinte, a trouvé de l'aide.", ["famille_apaisee", "oceane_orientee"]),
            ("Daniel est sorti en claquant la porte : il refuse le don. Océane se débrouille "
             "seule.", ["famille_dechiree", "oceane_seule"]),
        ],
    ),
    scenes=[S6_1, S6_2, S6_3A, S6_3B, S6_4, S6_5, S6_6],
)
