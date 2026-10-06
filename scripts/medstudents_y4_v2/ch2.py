"""Chapitre 2 — Et si on ne disait rien ? (semaine 2)."""
from __future__ import annotations

from .dsl import END, C, Entry, I, R, S, when

# Reprise de la v1 : scène 2.1 Dans le couloir
S2_1 = S(1, "2.1 Dans le couloir",
    "Mme Haddad, 74 ans, hospitalisée pour un ictère. L'imagerie montre une masse pancréatique très probablement maligne. Sa fille Sofia intercepte Alex avant la visite du matin.",
    focus=("em", "pb", "rd"),
    nodes=[
        I(1, "sofia", "anxious", "« Vous êtes l'étudiant·e qui suit ma mère ? Je voulais vous voir avant. » Elle baisse la voix. « Ne lui dites rien. Si c'est un cancer, elle ne le supportera pas. Mon père est mort comme ça — on lui a balancé ça en trois minutes, il s'est éteint en six semaines. »", [
            R("« Je vois que ça remue quelque chose de très dur pour vous. Est-ce que vous pouvez me raconter ce qui s'est passé avec votre père ? »", 2, "rd2 em3 co3 er2 cc2"),
            R("« Je comprends, ne vous inquiétez pas, on ne lui dira rien. »", 4, sets=["promesse_sofia"], scores="rd-3 em1 cc-2 pb-3"),
            R("« Ce n'est pas vous qui décidez de ce que votre mère sait. »", 5, "rd1 em-3 co-3 cc-2 pb2"),
            R("« Je vous écoute. Qu'est-ce qui vous fait si peur ? »", 2, "em3 co1"),
            R("« D'accord. On attendra que vous soyez prête pour qu'elle le sache. »", 4, "rd-2 pb-2 cc-1", sets=["promesse_sofia"]),
        ]),
        I(2, "sofia", "sad", "« Le médecin est entré, il a dit le mot, il a donné des pourcentages, et il est reparti. Mon père n'a plus jamais reparlé de rien. Il est mort en silence. »", [
            R("« Ce que vous décrivez, ce n'est pas une annonce, c'est un abandon. Ce n'est pas ce qu'on va faire ici. Mais je ne peux pas vous promettre de mentir à votre mère. »", 6, "rd3 em3 co3 cc3 pb3"),
            R("« Je vous promets qu'on fera attention. On ne lui dira que si elle demande. »", 4, sets=["promesse_sofia"], scores="em2 co1 cc-1 pb-2"),
            R("« Chaque patient est différent, votre mère n'est pas votre père. »", 3, "rd1 em-1 cc1"),
            R("Rester silencieux·se un moment, puis : « Je suis désolé·e que votre père ait vécu ça. »", 6, "co3 em2"),
            R("« Ça ne se passera pas comme ça, je vous le promets. On ne lui dira rien. »", 4, "pb-3 cc-2 rd-2", sets=["promesse_sofia"]),
        ]),
        I(3, "sofia", "angry", "« Évidemment que ce n'est pas la même personne. » Elle serre son sac. « Mais c'est la même manière de faire, et c'est ça que je ne veux plus voir. »", [
            R("« Vous avez raison, et c'est une critique juste. La manière compte autant que le contenu. Laissez-moi vous dire comment je compte m'y prendre. »", 6, "rd3 em3 er3 cc3"),
            R("« On a des protocoles pour ça maintenant. »", 6, "em-1"),
            R("« Dites-moi ce qui vous a le plus blessée, dans la manière. »", 2, "em3 er1"),
            R("« Je ne suis pas responsable de ce qui est arrivé à votre père. »", 6, "er-2 em-2"),
        ]),
        I(4, "moreau", "cold-anger", "Dr Moreau vous a entendu·e depuis la salle de soins. « Alex, un mot. » Une fois à l'écart : « Vous venez de promettre quelque chose que vous n'avez pas le droit de tenir. »", [
            R("« Vous avez raison. Je me suis laissé·e emporter par sa détresse. Je retourne la voir pour rectifier maintenant, pas dans trois jours. »", 7, clears=["promesse_sofia"], scores="er2 cc2 pb3 ic2"),
            R("« Elle était en détresse, je n'allais pas lui faire un cours de droit. »", 7, "er-1 cc-1 pb-2 ic-1"),
            R("« De toute façon la patiente ne demandera peut-être rien. »", 7, "rd-2 er-1 cc-2 pb-3"),
            R("« Je sais. Vous pouvez venir avec moi pour que je le lui dise correctement ? »", 7, "ic2 pb2 er1", clears=["promesse_sofia"]),
            R("« Je ne lui ai rien promis de précis. »", 7, "pb-3 cc-2"),
        ]),
        I(5, "sofia", "angry", "Elle recule d'un pas, les yeux brillants. « Excusez-moi de vouloir protéger ma mère. »", [
            R("« Pardon, je me suis mal exprimé·e. Votre inquiétude est légitime. Ce que je voulais dire, c'est que l'information appartient à votre mère — mais ça ne veut pas dire qu'on va la lui jeter à la figure. »", 2, "rd3 em3 co2 er3 cc3"),
            R("« C'est le cadre légal, ce n'est pas contre vous. »", 6, "em-1 cc1"),
            R("« Vous avez raison, je me suis mal exprimé·e. Racontez-moi ce qui vous fait peur. »", 2, "em2 er2"),
            R("« Protéger, ce n'est pas mentir, madame. »", 6, "cc1 em-2 rd-1"),
        ]),
        I(6, "sofia", "anxious", "« Alors qu'est-ce que vous allez faire, concrètement ? »", [
            R("« Je vais demander à votre mère ce qu'elle souhaite savoir, et jusqu'où. Si elle me dit qu'elle ne veut pas de détails, je respecterai ça aussi. Et vous pourrez être présente si elle le souhaite. »", 8, "rd3 em3 cc3 pb3"),
            R("« On va attendre quelques jours qu'elle soit plus forte. »", 7, "rd-2 cc-2 pb-2"),
            R("« Je vais suivre la procédure du service. »", 7, "em-2 cc-1"),
            R("« Lui demander d'abord ce qu'elle sait déjà, et ce qu'elle veut savoir. »", 8, "rd3 cc2"),
            R("« Je vais tout lui expliquer, c'est son droit. »", 7, "cc1 em-2 rd-1"),
        ]),
        I(7, "sofia", "suspicious", "« Vous me récitez quelque chose. » Elle vous regarde bien en face. « Vous allez lui dire ou pas ? »", [
            R("« Je vais lui proposer de lui dire, et je suivrai sa réponse. Je ne peux pas vous promettre l'inverse, et je ne veux pas vous mentir à vous non plus. »", 8, "rd3 er2 cc3 pb3"),
            R("« Je ne peux pas vous répondre. »", 8, "rd-1 em-2 cc-2"),
            R("« Je ne vais ni lui imposer quoi que ce soit, ni lui mentir. C'est elle qui décidera. »", 8, "rd2 pb2 cc2"),
            R("« Non. Je vous le promets. »", 8, "pb-3 cc-3 rd-1", sets=["promesse_sofia"]),
        ]),
        I(8, "sofia", "sad", "Elle se tait, puis : « Et si elle décide d'arrêter les traitements ? Si elle se laisse aller, comme papa ? »", [
            R("« C'est ça qui vous fait le plus peur, en fait. Si elle prenait cette décision en sachant ce qu'elle fait, ce serait son droit — mais ce n'est pas ce qui arrive le plus souvent. Le plus souvent, savoir permet de choisir. »", 9, "rd3 em3 co3 cc3"),
            R("« On ne la laissera pas faire ça. »", 9, "rd-3 pb-3"),
            R("« Ce sera à elle de décider, on n'y peut rien. »", 9, "rd1 em-2 co-2 pb1"),
            R("« Qu'est-ce qui vous ferait le plus peur, dans cette décision ? »", 9, "em3 cc1"),
            R("« À son âge, arrêter les traitements, c'est souvent le plus raisonnable. »", 9, "rd-2 pb-2 cc-1"),
        ]),
        I(9, "sofia", "neutral", "« De toute façon je suis sur le formulaire. Personne de confiance. C'est moi qui décide si elle ne peut plus. »", [
            R("« Vous êtes sa représentante thérapeutique, oui — et c'est important. Mais ce rôle s'active seulement si votre mère perd sa capacité de discernement. Aujourd'hui, elle l'a entièrement. »", 10, "rd3 cc3 pb3"),
            R("« Exactement, donc on passera par vous pour les décisions. »", 10, "rd-3 cc-3 pb-3"),
            R("« Ce n'est pas le sujet aujourd'hui. »", 10, "rd-1 em-2 cc-1"),
            R("« Votre rôle compte. Il commencera le jour où elle ne pourra plus décider. »", 10, "cc2 em1 pb1"),
            R("« Oui, mais ça ne vous donne pas le droit de décider à sa place. »", 10, "cc2 em-2 er-1"),
        ]),
        I(10, "sofia", "sad", "« Alors je sers à quoi, moi ? »", [
            R("« À être là. Sincèrement : ce qui protège le plus votre mère dans les semaines qui viennent, ce n'est pas le silence, c'est vous, présente, dans la chambre. »", 11, "rd3 em3 co3 cc3"),
            R("« À l'accompagner aux rendez-vous et à nous aider pour l'organisation du retour. »", 11, "em1 co1 cc2 ic1"),
            R("« Vous n'avez pas de rôle médical, c'est notre travail. »", 11, "rd-2 em-3 co-3"),
            R("« À l'aider à dire ce qu'elle veut, si elle vous le demande. »", 11, "rd2 em1 cc1"),
            R("« À rien, pour l'instant. »", 11, "em-3 co-2"),
        ]),
        I(11, "ines", "neutral", "Inès Rey vous rejoint après le départ de Sofia. « Elle m'a fait la même demande hier soir. Qu'est-ce qu'on répond quand la patiente nous pose la question à nous, la nuit ? »", [
            R("« On dit tous la même chose : que les résultats sont arrivés, que le médecin va lui en parler aujourd'hui. Personne n'invente et personne n'esquive. Je le note au dossier. »", 12, "rd2 cc3 pb3 ic3"),
            R("« Renvoyez-la vers moi ou le Dr Moreau, c'est plus prudent. »", 12, "cc1 pb1 ic1"),
            R("« Dites-lui qu'on attend encore des examens. »", 12, "cc-3 pb-3 ic-2"),
            R("« On se met d'accord maintenant sur une phrase commune, et je la note. »", 12, "ic3 cc2"),
            R("« Je ne sais pas, on verra au cas par cas. »", 12, "ic-2 cc-2"),
        ]),
        I(12, "ines", "neutral", "« Je vous dis autre chose. Hier, quand sa fille est partie, Mme Haddad m'a demandé si l'aumônier passait le dimanche. Elle ne me l'avait jamais demandé. »", [
            R("« C'est une information précieuse — elle est peut-être déjà en train de se préparer à quelque chose. Je vais l'écouter avant de parler. »", 13, "rd2 em3 co2 cc2 ic3"),
            R("« Ça ne veut pas forcément dire grand-chose. »", 13, "em-2 cc-1 ic-2"),
            R("« Notez-le, on en reparlera au colloque. »", 13, "cc1 ic1"),
            R("« Qu'est-ce qu'elle vous a dit d'autre, cette nuit-là ? »", 13, "ic2 em1"),
            R("« Les patients âgés demandent souvent l'aumônier, ça ne veut rien dire. »", 13, "rd-2 em-2"),
        ]),
        I(13, "moreau", "neutral", "« Avant d'entrer. Formulez-moi la règle, simplement, comme si vous l'expliquiez à un étudiant de deuxième année. »", [
            R("« L'information médicale appartient au patient capable de discernement. Il a le droit de savoir, le droit de ne pas savoir, et le droit de décider qui d'autre est informé. »", 14, "rd3 cc3 pb3"),
            R("« On doit tout dire au patient, c'est la loi. »", 14, "cc-1"),
            R("« On adapte selon les familles. »", 14, "rd-3 cc-3 pb-3"),
            R("« Le patient décide, et on l'aide à décider. »", 14, "rd2 cc1"),
            R("« La famille et le médecin décident ensemble. »", 14, "rd-3 pb-2"),
        ]),
        I(14, "moreau", "neutral", "« Vous avez mentionné le droit de ne pas savoir. Comment vous le mettez en œuvre sans en faire un prétexte pour vous taire ? »", [
            R("« En posant la question explicitement au patient, et en traçant sa réponse. Un patient qui n'a jamais été interrogé n'a pas renoncé à savoir : il n'a simplement pas été informé. »", 15, "rd3 cc3 pb3"),
            R("« En observant s'il pose des questions ou pas. »", 15, "rd-1 cc-2 pb-2"),
            R("« En le lui proposant clairement, sans insister, et en respectant sa réponse. »", 15, "rd2 cc2"),
            R("« Si elle ne demande rien, c'est qu'elle ne veut pas savoir. »", 15, "rd-2 cc-2"),
        ]),
        I(15, "moreau", "neutral", "« Dernier point. Vous entrez dans une chambre où la patiente a peut-être déjà compris, et où sa fille vous a mis la pression. Quel est votre principal risque ? »", [
            R("« De parler trop, pour combler mon propre malaise. Je vais poser des questions courtes et la laisser mener. »", 16, "em2 er3 cc3 pb2"),
            R("« De me tromper sur le diagnostic. »", 16, ""),
            R("« De la brusquer. »", 16, "em2 er1 cc1"),
            R("« D'être influencé·e par ce que sa fille m'a dit. »", 16, "pb2 er1"),
            R("« Aucun. Je sais ce que je fais. »", 16, "er-2 pb-1"),
        ]),
        I(16, "moreau", "neutral", "« Allez-y. Je ne vous accompagne pas cette fois : elle vous parlera mieux seul·e. Madame Rey entre avec vous. »", [
            R("« D'accord. Je viens vous faire le point juste après, avant le colloque. »", -1, "er2 cc2 pb3 ic3"),
            R("« Très bien. »", -1, ""),
            R("« D'accord. Inès, vous me faites signe si je parle trop ? »", -1, "ic3 er1"),
            R("« Je préférerais que vous veniez. »", -1, "ic1"),
            R("« Seul·e ? Je risque de tout rater. »", -1, "er-2"),
        ]),
    ],
)

# Reprise de la v1 : scène 2.2 Ce que la patiente demande
S2_2 = S(2, "2.2 Ce que la patiente demande",
    "Chambre 308. Mme Haddad est assise dans le fauteuil, un mot fléché sur les genoux. Elle a vu Alex passer trois fois dans le couloir sans entrer.",
    focus=("rd", "cc", "em", "co"),
    nodes=[
        I(1, "haddad", "neutral", "« Asseyez-vous, vous me donnez le tournis. » Elle pose son stylo. « J'ai été institutrice quarante ans. Je sais reconnaître un enfant qui cache quelque chose. »", [
            R("« Vous avez raison, je ne suis pas très doué·e. Est-ce que vous voulez qu'on parle de vos résultats ? »", 3, "rd3 em2 cc3"),
            R("« Je ne cache rien, on attend encore des éléments. »", 2, "rd-2 cc-3"),
            R("« Comment vous sentez-vous aujourd'hui ? »", 2, "em1 cc-1"),
            R("Ranger le dossier et s'asseoir en face d'elle. « Vous avez raison. Je peux ? »", 3, "rd2 em1 er1"),
            R("« Je ne suis pas là pour jouer aux devinettes, madame. »", 2, "rd-2 er-2"),
        ]),
        I(2, "haddad", "neutral", "Un silence. « Vous n'êtes pas venu·e pour me demander ça. » Elle sourit sans méchanceté. « Et vous n'attendez rien du tout. »", [
            R("« Non, en effet. Je suis venu·e vous parler de vos résultats, et je m'y suis pris·e lâchement. Est-ce que c'est le bon moment ? »", 3, "rd3 er2 cc3"),
            R("« Si, si, c'est ma tournée habituelle. »", 4, "rd-2 cc-3"),
            R("« Vous avez raison. Je voulais vous parler de vos résultats. Vous le souhaitez ? »", 3, "rd2 cc2"),
            R("« Si vous le dites. »", 4, "rd-2 cc-1"),
        ]),
        I(3, "haddad", "neutral", "« Oui. » Elle croise les mains. « Mais avant, dites-moi une chose : est-ce que c'est le genre de nouvelle après laquelle on réorganise sa vie ? »", [
            R("« Oui. C'est ce genre de nouvelle. Est-ce que vous voulez que je vous dise tout, ou seulement l'essentiel pour commencer ? »", 6, "rd3 em3 er3 cc3 pb3"),
            R("« Oui, mais rien n'est certain, il faut rester positive. »", 4, "em-1 cc-2"),
            R("« Je préfère que le Dr Moreau vous réponde. »", 5, "rd-1 em-2 cc-1"),
            R("« Oui. Voulez-vous que votre fille soit là, ou préférez-vous l'entendre seule ? »", 6, "rd3 pb1 cc1"),
            R("« Non, non, ce n'est pas si grave. »", 4, "cc-3 pb-2"),
        ]),
        I(4, "haddad", "neutral", "« Jeune personne. » Son ton reste doux. « Ma fille vous a parlé, n'est-ce pas ? »", [
            R("« Oui. Elle a très peur pour vous, à cause de ce qui s'est passé avec votre mari. Mais c'est à vous que je dois répondre, pas à elle. »", 6, "rd3 em3 cc3 pb3"),
            R("« Je ne peux pas vous dire ce que votre fille m'a dit. »", 6, "em-1 cc-1 pb1"),
            R("« Non, pas du tout. »", 5, "rd-2 cc-3"),
            R("« Oui. Et je lui ai dit que c'est à vous que je répondrais. »", 6, "rd2 pb2 cc1"),
        ]),
        I(5, "haddad", "cold-anger", "Elle repose le mot fléché et vous regarde un long moment. « J'ai eu six cents élèves. Je vais vous dire ce que je leur disais : ce n'est pas la bêtise qui me fâche, c'est qu'on me prenne pour une idiote. »", [
            R("« Vous avez raison, et je vous demande pardon. Je recommence honnêtement : les résultats sont arrivés, ils ne sont pas bons, et je suis là pour en parler. »", 6, "rd3 em2 er3 cc3"),
            R("« Je ne voulais pas vous inquiéter inutilement. »", 6, "rd-2 cc-2"),
            R("« Je ne vous prends pas pour une idiote. Je ne savais pas comment commencer. »", 6, "er2 rd1 cc1"),
            R("« Ce sont les consignes du service, madame. »", 6, "rd-2 pb-2"),
        ]),
        I(6, "haddad", "neutral", "« Dites-moi l'essentiel. Je vous demanderai le reste quand je serai prête. »", [
            R("« L'examen a montré une masse sur le pancréas. Tout indique qu'elle est cancéreuse. C'est sérieux. » — puis attendre.", 9, "rd3 em2 er3 cc3"),
            R("« Il y a une lésion pancréatique de 4 cm avec envahissement vasculaire et probable carcinose péritonéale. »", 7, "rd-1 em-2 cc-3"),
            R("« Il y a quelque chose sur le pancréas, mais on va voir ce qu'on peut faire. »", 8, "cc-2"),
            R("« L'essentiel : une masse sur le pancréas, très probablement un cancer. Voulez-vous que je m'arrête là pour l'instant ? »", 9, "cc3 rd2"),
            R("« Il faut rester positive, mais c'est un cancer, oui. »", 8, "em-1 pb-1"),
        ]),
        I(7, "haddad", "neutral", "« Ce n'est pas ce que je vous ai demandé. Je vous ai demandé l'essentiel, en français. »", [
            R("« Pardon. En français : c'est très probablement un cancer du pancréas, et il est déjà étendu. »", 9, "rd3 er2 cc3"),
            R("« C'est compliqué, je préfère que l'oncologue vous l'explique. »", 8, "rd-1 em-2 cc-2 pb-1"),
            R("« Pardon. Un cancer du pancréas, déjà étendu. »", 9, "cc3"),
            R("« Je vais vous faire un schéma, ce sera plus clair. »", 8, "cc-1 em-1"),
        ]),
        I(8, "haddad", "neutral", "« Quelque chose. » Elle répète le mot. « J'ai enseigné le français. Quand on ne veut pas nommer une chose, c'est qu'elle fait peur. Elle vous fait peur à vous, ou à moi ? »", [
            R("« À moi, probablement. C'est très probablement un cancer du pancréas, et il est déjà étendu. Voilà, je l'ai dit. »", 9, "rd3 em2 er3 cc3"),
            R("« Ni l'un ni l'autre, je voulais rester prudent·e. »", 9, "rd-1 cc-2"),
            R("« Vous avez raison, je tourne autour. C'est un cancer du pancréas. »", 9, "cc3 er1"),
            R("« Ne jouons pas sur les mots. »", 9, "er-2 rd-2"),
        ]),
        I(9, "haddad", "resigned", "Elle hoche lentement la tête, plusieurs fois. Elle reprend son mot fléché, le repose. Le silence dure.", [
            R("Attendre sans rien dire, en restant présent·e.", 10, "rd3 em3 co3 er3 cc2"),
            R("« Voulez-vous que je vous laisse un moment ? »", 10, "rd3 em2 co2 er2"),
            R("« Est-ce que vous avez des questions ? »", 10, "em-1 er-1"),
            R("Lui prendre doucement la main, si elle la laisse.", 10, "co3 em1"),
            R("« C'est beaucoup, je sais. Mais on a des traitements, vous savez. »", 10, "em-1 cc-1"),
        ]),
        I(10, "haddad", "neutral", "« Est-ce que c'est celui dont on ne guérit pas ? »", [
            R("« C'est un cancer qu'on guérit rarement, oui. Ce qui ne veut pas dire qu'on ne fait rien : il y a des traitements qui ralentissent, et surtout des traitements qui soulagent. »", 11, "rd3 co2 cc3"),
            R("« Il ne faut jamais dire jamais, il y a toujours des exceptions. »", 11, "cc-2"),
            R("« Oui. La survie médiane est inférieure à un an. »", 11, "em-3 co-3 cc1"),
            R("« Rarement. Mais on peut vous soulager, et vous aider à vivre ce temps comme vous le voulez. »", 11, "cc2 co2 rd1"),
            R("« Oui. On ne peut plus rien faire. »", 11, "cc-2 co-3 pb-1"),
        ]),
        I(11, "haddad", "resigned", "« Ce n'est pas mourir qui m'inquiète. » Elle regarde par la fenêtre. « Combien de temps avant que je ne puisse plus m'occuper de moi-même ? »", [
            R("« Je ne sais pas encore, et c'est une question importante. Je la poserai à l'oncologue avec vous. Qu'est-ce qui compte le plus pour vous dans les mois qui viennent ? »", 12, "rd3 em3 co3 cc3"),
            R("« Ne vous projetez pas, on n'en est pas là. »", 12, "rd-2 em-2 cc-1"),
            R("« Probablement quelques mois. »", 12, "em-1"),
            R("« Je ne sais pas encore. Qu'est-ce qui vous fait le plus peur, dans ce « ne plus pouvoir » ? »", 12, "em3 cc1"),
            R("« Vous aurez de l'aide à domicile, ne vous inquiétez pas. »", 12, "cc-1 em-1"),
        ]),
        I(12, "haddad", "neutral", "« Rester chez moi. » Sans hésitation. « Et ne pas finir branchée dans un service de réanimation. »", [
            R("« C'est une chose très importante que vous venez de me dire, et je vais l'écrire dans votre dossier. On peut aussi en faire des directives anticipées, si vous voulez que ce soit respecté même si un jour vous ne pouvez plus le dire. »", 13, "rd3 em2 co3 cc3 pb3 ic2"),
            R("« On n'en est pas là, mais je le note. »", 13, "rd1 cc1"),
            R("« On fera tout ce qu'il faut, ne vous en faites pas. »", 13, "rd-1 cc-2 pb-2"),
            R("« Qu'est-ce que « rester chez moi » veut dire, pour vous ? »", 13, "em2 rd2"),
            R("« Ça, c'est aux médecins de le décider le moment venu. »", 13, "rd-3 pb-2"),
        ]),
        I(13, "haddad", "neutral", "« J'ai un papier chez moi. » Elle sourit. « Je l'ai écrit après la mort de mon mari. Personne ne me l'a jamais demandé. »", [
            R("« Alors je vais le demander, moi. Est-ce que quelqu'un peut l'apporter, pour qu'on le mette au dossier et que toute l'équipe le connaisse ? »", 14, "rd3 co2 cc3 pb3 ic3"),
            R("« C'est très bien, gardez-le précieusement. »", 14, "cc-1 pb-1 ic-1"),
            R("« Il compte énormément. Qui peut nous l'apporter ? »", 14, "rd2 ic1 cc1"),
            R("« Il faudra peut-être le refaire, s'il est ancien. »", 14, "rd-1 cc-1"),
        ]),
        I(14, "haddad", "neutral", "« Et j'aimerais voir l'aumônier. » Elle vous regarde, un peu sur la défensive. « Ça ne veut pas dire que j'ai renoncé. »", [
            R("« Ça ne veut rien dire d'autre que ce que vous en dites. Je transmets la demande aujourd'hui. »", 15, "rd3 em3 co2 cc2 ic3"),
            R("« Bien sûr, c'est important d'avoir un soutien spirituel dans ces moments. »", 15, "rd1 em1 co1 ic1"),
            R("« Vous n'avez pas à vous justifier auprès de moi. »", 15, "rd2 em2 cc1"),
            R("« D'accord. Vous voulez que je le note pour l'équipe ? »", 15, "ic2 rd1"),
            R("« Ce n'est peut-être pas nécessaire tout de suite. »", 15, "rd-2 em-2"),
        ]),
        I(15, "haddad", "neutral", "« Une dernière chose. » Elle vous regarde bien en face. « Sofia. Je ne veux pas qu'elle sache tout de suite. Laissez-moi le lui dire moi-même, à mon rythme. »", [
            R("« C'est votre droit le plus strict, et je vais le noter au dossier pour que toute l'équipe le respecte. Dites-moi quand vous voulez qu'on vous aide. »", 16, "rd3 em2 cc3 pb3 ic3"),
            R("« Elle va me poser la question directement, ça va être difficile de ne rien dire. »", 17, "cc1 pb-1"),
            R("« Ce serait mieux qu'elle sache, elle pourra vous soutenir. »", 17, "rd-2 em-1 pb-2"),
            R("« D'accord. Et si elle me pose la question, je lui dirai que c'est à vous qu'elle doit la poser. »", 16, "rd2 pb2 cc1"),
            R("« Elle a le droit de savoir. Je préfère le lui dire moi-même. »", 17, "rd-3 pb-3 em-1"),
        ]),
        I(16, "haddad", "melancholic", "« Elle va vouloir tout gérer. » Elle soupire. « Et surtout, elle va vouloir que je me batte. Je n'ai pas encore décidé si j'en avais envie. »", [
            R("« Vous n'êtes obligée de décider ni aujourd'hui ni seule. Et personne ici ne vous demandera de vous battre pour rassurer les autres. »", 18, "rd3 em3 co3 pb3"),
            R("« Il faut garder espoir, vous savez. »", 17, "rd-2 em-2"),
            R("« C'est normal d'être découragée au début. »", 18, "em1 co1"),
            R("« Et vous, de quoi avez-vous envie ? »", 18, "rd3 em1"),
            R("« Il faudra vous battre, pour elle. »", 17, "rd-3 em-2"),
        ]),
        I(17, "haddad", "cold-anger", "Elle se ferme un peu. « Vous aussi, alors. » Elle reprend le mot fléché. « Vous voulez que je sois courageuse pour vous rassurer. »", [
            R("« Vous avez raison, et c'est une remarque juste. Je vais m'occuper de ce que vous me demandez, pas de ce qui m'arrangerait. »", 18, "rd3 em3 er3 pb2"),
            R("« Pas du tout, je pensais à vous. »", 18, "rd-1 er-1"),
            R("« Pardon. Je vais vous écouter, vous. »", 18, "rd2 er1"),
            R("« Je dis ça pour votre bien. »", 18, "rd-2 er-1"),
        ]),
        I(18, "haddad", "neutral", "« Si Sofia vous demande quelque chose, vous lui dites quoi ? »", [
            R("« Que les résultats sont arrivés, que vous en avez parlé avec moi, et que c'est à vous qu'elle doit poser la question. Je ne mentirai pas, mais je ne dirai pas à votre place. »", 19, "rd3 cc3 pb3"),
            R("« Que je n'ai pas le droit de lui répondre. »", 19, "rd1 em-1 cc1 pb2"),
            R("« Qu'on attend encore des examens. »", 19, "rd-1 cc-3 pb-3"),
            R("« Que je ne peux rien lui dire sans votre accord, et qu'elle en parle avec vous. »", 19, "pb2 cc2 rd1"),
        ]),
        I(19, "haddad", "neutral", "Elle se tait. Vous n'avez pas encore vérifié ce qu'elle a réellement retenu de l'annonce.", [
            R("« Madame Haddad, pour être sûr·e de ne pas vous avoir embrouillée : si vous deviez résumer à voix haute ce que je viens de vous dire, ça donnerait quoi ? »", 20, "rd3 em2 cc3 pb2"),
            R("« Vous avez des questions sur ce que je vous ai expliqué ? »", 20, "rd1"),
            R("Conclure l'entretien.", 21, "rd-1 cc-2 pb-1"),
            R("« Est-ce qu'il y a quelque chose que j'ai dit qui n'était pas clair ? »", 20, "cc2"),
            R("« Bon, je crois qu'on a fait le tour. »", 21, "cc-2 em-1"),
        ]),
        I(20, "haddad", "neutral", "« Que j'ai un cancer du pancréas, qu'on ne le guérit pas, qu'on peut le ralentir un peu et surtout me soulager. Que je vois la spécialiste. Et que c'est moi qui parle à ma fille. »", [
            R("« C'est exactement ça. Vous avez tout retenu, et vous l'avez dit mieux que moi. »", 21, "rd3 em2 co2 cc3"),
            R("« Presque. On dit plutôt adénocarcinome du pancréas. »", 21, "rd-2 em-2 cc-2"),
            R("« Oui. Vous avez tout retenu. » Puis se taire.", 21, "rd2 cc1"),
            R("« Pas tout à fait : on ne parle pas encore de ne pas guérir. »", 21, "cc-3 pb-2"),
        ]),
        I(21, "ines", "neutral", "Inès Rey, restée en retrait, s'avance. « Madame Haddad, je suis là cet après-midi. Et je m'occupe de l'aumônier. »", [
            R("« Et je repasse demain matin avant la consultation d'oncologie, pour qu'on prépare vos questions ensemble. »", 22, "em2 co3 cc2 ic3"),
            R("« Voilà, vous êtes entre de bonnes mains. »", 22, "ic1"),
            R("« Je vous laisse mon nom, si vous voulez me faire appeler. »", 22, "co1 cc2"),
            R("Partir sans rien dire.", 22, "co-2 ic-1"),
        ]),
        I(22, "haddad", "grateful", "Alors que vous atteignez la porte : « Jeune personne. » Elle ne lève pas les yeux de son mot fléché. « Merci de ne pas m'avoir menti. »", [
            R("Rester dans l'embrasure un instant, puis : « Merci de me l'avoir demandé si clairement. À demain, Madame Haddad. »", -1, "rd3 em3 co3 er2"),
            R("« C'est normal, c'est mon travail. »", -1, "rd1"),
            R("« De rien. Bonne journée. »", -1, "em-1 co-1"),
            R("Lui faire un petit signe de tête, et refermer doucement la porte.", -1, "rd2 co1"),
        ]),
    ],
)

# Reprise de la v1 : scène 2.3 Le colloque
S2_3 = S(3, "2.3 Le colloque",
    "Salle de colloque, 8 h 15. Dr Moreau, Dre Keller, Inès Rey. Alex doit présenter la situation et défendre une position devant des gens qui ne sont pas d'accord.",
    focus=("ic", "pb", "cc"),
    nodes=[
        I(1, "moreau", "neutral", "« Alex, Mme Haddad. Vous avez mené l'entretien hier. Résumez-nous où on en est, et ce que vous proposez. »", [
            R("« Patiente informée du diagnostic à sa demande, par paliers. Elle a des directives anticipées à domicile, souhaite rester chez elle et refuse la réanimation. Elle demande que sa fille ne soit pas informée pour l'instant. Je propose qu'on trace tout ça et qu'on s'y tienne collectivement. »", 3, "rd3 cc3 pb3 ic3"),
            R("« Je lui ai tout dit. Elle a bien réagi. »", 2, "cc-1"),
            R("« C'est compliqué, il y a un conflit avec la famille. »", 2, "cc-2 ic-1"),
            R("« Elle a refusé la réanimation, et sa fille ne sait rien. On peut en parler ? »", 3, "cc2 ic1"),
            R("« Diagnostic annoncé. Le reste, je préfère que le Dr Moreau le présente. »", 2, "pb-1 ic-1"),
        ]),
        I(2, "moreau", "cold-anger", "« Ce n'est pas un résumé, c'est une impression. Un colloque sert à transmettre des décisions opposables. Reprenez. »", [
            R("« Vous avez raison. Trois décisions : diagnostic annoncé et compris, directives anticipées à récupérer, non-information de la fille à la demande de la patiente. »", 3, "er2 cc3 pb3 ic3"),
            R("« Je n'ai pas tout noté, je referai le point plus tard. »", 3, "cc-2 pb-2 ic-2"),
            R("« Pardon. Je reprends les décisions une par une. »", 3, "cc2 er1"),
            R("« Je ne vois pas la différence. »", 3, "er-2 ic-2"),
        ]),
        I(3, "keller", "neutral", "« Et si la fille me coince dans le couloir tout à l'heure, je réponds quoi ? Elle est personne de confiance sur le formulaire d'admission. »", [
            R("« La représentante thérapeutique intervient quand la patiente ne peut plus s'exprimer. Mme Haddad a toute sa capacité de discernement — c'est elle qui décide. »", 5, "rd3 cc3 pb3 ic2"),
            R("« Vous lui dites ce que vous jugez utile, vous avez plus d'expérience que moi. »", 4, "cc-2 pb-2 ic-1"),
            R("« On lui dit tout, elle finira par le savoir de toute façon. »", 4, "rd-3 cc-1 pb-3"),
            R("« La même chose que nous : c'est sa mère qui décide de ce qu'elle partage. »", 5, "pb2 cc2 ic1"),
        ]),
        I(4, "moreau", "neutral", "« Reprenons les principes, puisqu'ils ne sont manifestement pas acquis. Qui est titulaire de l'information médicale, et qu'est-ce que ça implique quand la famille demande le silence — ou l'inverse ? »", [
            R("« La patiente. Le secret médical la protège, y compris vis-à-vis de ses proches. La famille peut être associée, mais seulement si elle le veut. »", 5, "rd3 cc3 pb3"),
            R("« La famille, quand la patiente est âgée. »", 5, "rd-3 cc-3 pb-3"),
            R("« La patiente, tant qu'elle a sa capacité de discernement. »", 5, "pb2 cc1"),
            R("« Ça dépend de la famille. »", 5, "pb-2 cc-2"),
        ]),
        I(5, "ines", "neutral", "« D'accord sur le principe. Mais concrètement : la fille est là de 14 h à 20 h tous les jours. Mes collègues de nuit ne seront pas au courant, et ce sont elles qu'on va cuisiner. »", [
            R("« Vous avez raison, un principe non transmis ne vaut rien. Je rédige une note explicite dans le dossier et je la lis aux transmissions de ce soir. »", 6, "rd2 cc3 pb2 ic3"),
            R("« C'est écrit dans l'observation médicale, il suffit de la lire. »", 6, "cc-1 ic-2"),
            R("« On avisera au cas par cas. »", 6, "cc-2 pb-1 ic-2"),
            R("« Qu'est-ce qui les aiderait, vos collègues de nuit ? »", 6, "ic3 em1"),
        ]),
        I(6, "ines", "neutral", "« Et vous écrivez quoi, exactement ? Parce que « ne rien dire à la famille », ça va être compris de dix façons. »", [
            R("« Phrase par phrase : la patiente est informée du diagnostic ; elle souhaite informer sa fille elle-même ; en cas de question de la fille, répondre qu'il faut s'adresser à sa mère ; ne jamais dire qu'on attend des résultats. »", 7, "rd2 cc3 pb3 ic3"),
            R("« Que la fille ne doit pas être informée pour le moment. »", 7, ""),
            R("« Je vous propose la formulation, et vous la corrigez : c'est vous qui la lirez à 22 h. »", 7, "ic3 cc2"),
            R("« Écrivez ce que vous voulez. »", 7, "ic-3 cc-2"),
        ]),
        I(7, "keller", "cold-anger", "« Je ne suis pas d'accord sur un point. Retarder l'information de la famille retarde l'organisation du retour à domicile. On perd des jours, et on a douze patients en attente de lit. »", [
            R("« Je l'entends, et c'est un vrai argument. Est-ce qu'on peut proposer à Mme Haddad de fixer elle-même une échéance ? Si elle sait que l'organisation en dépend, elle décidera peut-être plus vite — mais ce sera sa décision. »", 9, "rd3 er3 cc3 pb3 ic3"),
            R("« Le droit est le droit, on ne va pas en discuter. »", 8, "rd1 er-2 pb2 ic-2"),
            R("« Vous avez sans doute raison, on informe la fille. »", 8, "rd-3 er-1 pb-3 ic-1"),
            R("« Je note la contrainte des lits, et je la lui expose sans pression. »", 9, "ic2 pb1 cc1"),
        ]),
        I(8, "keller", "cold-anger", "« Donc soit vous me récitez la loi, soit vous cédez dès qu'on vous pousse. Aucune des deux ne fait avancer la patiente. »", [
            R("« C'est juste. Ce que je peux faire, c'est retourner voir la patiente et lui exposer la contrainte d'organisation — sans en faire un chantage. C'est elle qui tranche, mais elle décide en connaissance de cause. »", 9, "rd3 er3 cc3 pb3 ic3"),
            R("« Alors proposez quelque chose, vous. »", 9, "er-2 cc-1 ic-1"),
            R("« Vous avez raison, je n'ai pas de solution. Je vous demande votre aide. »", 9, "ic3 er2"),
            R("« Je ne suis qu'étudiant·e. »", 9, "er-1 pb-1"),
        ]),
        I(9, "keller", "neutral", "Elle réfléchit. « D'accord. Je peux travailler avec ça. » Puis : « Autre chose : elle a refusé la réanimation. Ça, il faut que ce soit lisible en trois secondes, pas enterré dans une note. »", [
            R("« Je le mets dans le champ dédié du dossier, pas dans le texte libre, et je le signale à l'admission. Et je récupère ses directives anticipées écrites. »", 10, "rd3 cc3 pb3 ic3"),
            R("« C'est noté dans mon observation d'hier. »", 10, "cc-2 pb-2 ic-1"),
            R("« Je remplis le champ maintenant, pendant le colloque. »", 10, "ic2 pb2"),
            R("« Tout le monde lit mes notes, ça suffira. »", 10, "ic-2 cc-1"),
        ]),
        I(10, "keller", "neutral", "« Sur le fond maintenant. Elle a 74 ans, un état général conservé. Je peux lui proposer une chimiothérapie, mais la tolérance sera difficile. Vous lui présentez ça comment ? »", [
            R("« En lui présentant les deux options à égalité — traitement actif ou soins de confort — avec ce que chacune coûte et apporte. Si on présente le traitement comme la norme, refuser devient un abandon. »", 11, "rd3 em2 co2 cc3 pb3"),
            R("« En lui expliquant qu'il faut essayer, on verra bien comment elle supporte. »", 11, "rd-2 cc-2 pb-2"),
            R("« C'est à vous de lui présenter, je ne suis qu'en M1. »", 11, "em-1 cc-1 pb1 ic-1"),
            R("« En lui demandant d'abord ce qui compte pour elle, et en partant de là. »", 11, "rd3 cc1"),
        ]),
        I(11, "moreau", "neutral", "« Attention quand même. Présenter deux options à égalité quand elles ne le sont pas médicalement, ce n'est pas de la neutralité, c'est une démission. Où est la limite ? »", [
            R("« La limite, c'est de donner mon avis médical quand il est fondé, en le nommant comme tel : voilà ce que je recommande et pourquoi, et voilà ce qui reste votre choix. »", 12, "rd3 cc3 pb3"),
            R("« On ne doit jamais influencer le patient. »", 12, "cc-2 pb-2"),
            R("« On recommande toujours le traitement le plus actif. »", 12, "rd-3 cc-2 pb-3"),
            R("« Je lui dis ce que je recommanderais, et je lui laisse le temps de décider. »", 12, "cc2 rd2"),
        ]),
        I(12, "ines", "neutral", "« Elle a demandé l'aumônier. Je l'ai appelé. » Un silence gêné autour de la table. Dre Keller lève un sourcil.", [
            R("« Très bien, merci. C'est une demande explicite de la patiente, elle vaut autant que les autres. »", 13, "rd3 em2 co2 ic3"),
            R("« On note ça où ? »", 13, "cc1 ic1"),
            R("« Ce n'est pas vraiment un sujet de colloque médical. »", 13, "rd-2 em-2 co-2 ic-3"),
            R("« Elle vous l'a demandé à vous. Merci de l'avoir entendu. »", 13, "ic3 rd1"),
        ]),
        I(13, "ines", "anxious", "« Dernier point, et c'est le plus probable : cette nuit, la fille appelle le téléphone du service à 22 h et demande les résultats. La collègue fait quoi ? »", [
            R("« Elle dit qu'elle ne donne pas d'information médicale par téléphone, ce qui est vrai dans tous les cas, et l'invite à venir en parler avec sa mère. Je l'écris textuellement. »", 14, "rd3 cc3 pb3 ic3"),
            R("« Elle renvoie vers le médecin de garde. »", 14, "cc1 pb1 ic1"),
            R("« Elle improvise, on ne peut pas tout prévoir. »", 14, "cc-2 pb-2 ic-2"),
            R("« Qu'elle dise vrai : pas d'information médicale au téléphone, et qu'elle invite la fille à parler avec sa mère. »", 14, "cc2 pb2 ic1"),
            R("« Qu'elle raccroche. »", 14, "ic-2 em-2"),
        ]),
        I(14, "moreau", "neutral", "« Avant de clore : qu'est-ce que vous avez mal fait dans cette histoire, depuis le début ? »", [
            R("« J'ai failli m'engager auprès de la fille avant d'avoir parlé à la patiente. C'est l'ordre qui était faux : la famille d'abord, la patiente après. »", 15, "er3 cc3 pb3"),
            R("« Rien de grave, je crois que ça s'est bien passé. »", 15, "er-1 cc-1"),
            R("« J'ai manqué de fermeté avec la fille. »", 15, "em-1"),
            R("« J'ai parlé trop vite à la fille, dans le couloir, avant de parler à la patiente. »", 15, "pb2 er1"),
            R("« C'est la fille qui a compliqué les choses. »", 15, "pb-2 rd-2"),
        ]),
        I(15, "moreau", "neutral", "« Et si la patiente change d'avis demain et vous demande de tout cacher à sa fille définitivement, y compris au moment du décès ? »", [
            R("« Je respecte, je trace, et je reviens vers elle régulièrement — sans la harceler. Son avis d'aujourd'hui n'est pas son avis définitif, et c'est justement pour ça qu'il faut rouvrir la question, pas la forcer. »", 16, "rd3 em3 co2 cc3 pb3"),
            R("« Là je refuserais, ce serait trop dur pour la famille. »", 16, "rd-2 em1 pb-2"),
            R("« Je ferais remonter à l'éthique clinique. »", 16, "rd1 cc1 pb2 ic2"),
            R("« Je le lui demande franchement, et je lui explique ce que ça implique pour sa fille. »", 16, "rd2 cc2"),
        ]),
        I(16, "moreau", "neutral", "« Justement. Vous savez qu'il existe une structure de soutien éthique dans cet hôpital ? Quand est-ce qu'on la sollicite ? »", [
            R("« Quand l'équipe est durablement divisée sur ce qui est juste, pas quand elle est seulement mal à l'aise. Ici, on a réussi à décider ensemble. »", 17, "er2 cc3 pb3 ic3"),
            R("« Dès qu'il y a un conflit avec une famille. »", 17, "cc-1 pb-1"),
            R("« Quand on ne sait plus ce qui est juste, pas seulement quand c'est difficile. »", 17, "pb2 cc1"),
            R("« Jamais. C'est au chef de trancher. »", 17, "ic-2 pb-1"),
        ]),
        I(17, "moreau", "neutral", "« On tranche. Alex, vous faites quoi aujourd'hui, concrètement, dans l'ordre ? »", [
            R("« Note au dossier avec les quatre phrases exactes ; champ réanimation renseigné ; appel à la famille pour les directives anticipées écrites ; passage chez Mme Haddad pour lui exposer la contrainte d'organisation ; transmissions ce soir. »", -1, "rd3 co2 cc3 pb3 ic3"),
            R("« Note au dossier, et on en reparle la semaine prochaine. »", -1, ""),
            R("« Je laisse le Dr Moreau gérer la famille. »", -1, "em-1 cc-1 pb-2 ic-1"),
            R("« La note au dossier et le champ réanimation, maintenant. Le reste dans la journée. »", -1, "ic1 cc1 pb1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 2.4 Sofia — nouvelle scène
# ---------------------------------------------------------------------------
S2_4 = S(4, "2.4 Sofia",
    "Jeudi, 14 h 20. L'aumônier sort de la chambre 308. Sofia Haddad, qui arrivait avec "
    "un bouquet de pivoines, l'a croisé dans l'embrasure. Elle traverse le couloir vers "
    "le desk infirmier, où vous relisez un dossier avec Inès Rey.",
    focus=("er", "em", "pb"),
    entries=[
        Entry(1, when(all=["promesse_sofia"]),
              "Jeudi, 14 h 20. L'aumônier sort de la chambre 308. Sofia Haddad l'a croisé "
              "dans l'embrasure. Lundi, dans ce même couloir, vous lui avez promis qu'on ne "
              "dirait rien à sa mère."),
    ],
    nodes=[
        I(2, "sofia", "angry",
          "Elle pose le bouquet sur le desk si fort que l'eau déborde. « L'aumônier. Dans la "
          "chambre de ma mère. » Sa voix tremble. « Qui lui a dit ? »", [
            R("« Vous avez le droit d'être en colère. Venez, on va parler dans le petit salon, "
              "pas au milieu du couloir. »", 3, "er3 em2 rd2 pb1 co1"),
            R("« C'est elle qui a demandé l'aumônier. »", 4, "cc1 pb1 em-1"),
            R("« Je ne peux rien vous dire, c'est couvert par le secret médical. »", 5, "em-2 rd-1 er-1"),
            R("« Ce n'est pas moi, c'est le Dr Moreau qui a décidé. »", 6, "ic-3 pb-2 cc-2"),
            R("Poser la main sur le bouquet mouillé, doucement. « Vous êtes bouleversée. Je vous écoute. »", 3, "em3 er2 co1"),
        ]),
        I(1, "sofia", "angry",
          "Elle pose le bouquet sur le desk si fort que l'eau déborde. « Vous m'aviez "
          "promis. » Elle ne crie pas, c'est pire. « Vous m'avez regardée dans les yeux, "
          "lundi, et vous m'avez promis. »", [
            R("« Oui. Je vous ai promis quelque chose que je n'avais pas le droit de promettre. "
              "C'était une faute, et je vous dois une explication. Venez, on va s'asseoir. »",
              3, "pb2 er2 em2 cc2 rd1"),
            R("« C'est votre mère qui a posé la question. Je ne pouvais pas lui mentir. »",
              4, "cc1 pb1 em-1"),
            R("« Je n'ai jamais promis ça. »", 5, "rd-2 pb-3 cc-3"),
            R("« Je ne savais pas ce que je disais, votre histoire m'avait touché·e. »", 4, "pb-1 er1"),
            R("« Promettre, c'était ma façon de vous calmer. »", 5, "pb-3 rd-2 er-1 cc-1"),
        ]),
        I(3, "sofia", "sad",
          "Petit salon des familles. Elle ne s'assoit pas tout de suite. Quand elle le fait, "
          "ses mains tremblent. « Vous ne savez pas ce que c'est. Six semaines. Mon père a mis "
          "six semaines à mourir après l'annonce, et il n'a plus jamais parlé. »", [
            R("« Non, je ne sais pas. Racontez-moi ces six semaines, si vous voulez. »",
              7, "em3 co2 rd1"),
            R("« Votre mère n'est pas votre père. »", 8, "em-1 cc0"),
            R("« On a fait ça très différemment, je vous assure. »", 8, "er-1 em-1"),
            R("S'asseoir en face d'elle et attendre qu'elle continue.", 7, "em2 er2"),
            R("« Ça remonte à six ans, il faudrait peut-être tourner la page. »", 8, "em-3 co-2 rd-2"),
        ]),
        I(4, "sofia", "suspicious",
          "« Elle a demandé l'aumônier. » Elle répète, lentement. « Ma mère n'a pas mis les "
          "pieds dans une église depuis l'enterrement de mon père. Donc elle sait. Donc "
          "quelqu'un lui a dit. »", [
            R("« Ce que votre mère sait, c'est à elle de vous le dire. Ce que je peux vous "
              "dire, c'est que personne ne lui a menti, et qu'elle a choisi de vous en parler "
              "elle-même. »", 9, "pb3 cc2 rd2 em1"),
            R("« Oui, elle sait. Elle a un cancer du pancréas. »", 10, "rd-3 pb-3 ic-1"),
            R("« Je ne suis pas autorisé·e à en parler. »", 5, "cc-1 em-1"),
            R("« Qu'est-ce qui vous fait le plus peur, dans le fait qu'elle sache ? »", 9, "em3 pb1"),
        ]),
        I(5, "sofia", "angry",
          "Elle se lève. « Très bien. Je veux voir le chef de service. Je vais porter plainte. "
          "Vous êtes en train de tuer ma mère avec vos principes. » Des visiteurs se "
          "retournent. Inès Rey s'est approchée.", [
            R("Rester calme. « Vous pouvez voir le Dr Moreau, je l'appelle maintenant. Et je "
              "reste avec vous en attendant, si vous voulez. »", 11, "er3 ic2 em1 rd1"),
            R("« Madame, calmez-vous. »", 11, "er-1 em-2"),
            R("« Faites ce que vous voulez. »", 11, "er-3 em-2 rd-1 co-1"),
            R("« Vous avez le droit de voir le chef, et de vous plaindre. Est-ce que je peux d'abord vous dire ce qui s'est passé ? »", 11, "er2 pb2 cc1"),
        ]),
        I(6, "ines", "cold-anger",
          "Inès Rey pose son stylo. « Alex. » Un temps. « Le Dr Moreau n'a rien décidé seul. "
          "On en a parlé au colloque, tous ensemble, et vous y étiez. » Sofia vous regarde. "
          "« Donc personne n'est responsable ? »", [
            R("« Pardon, j'ai dit n'importe quoi. C'est une décision d'équipe, j'en fais "
              "partie — et c'est surtout le choix de votre mère. »", 3, "pb2 ic2 er1 cc1"),
            R("« Voilà, c'est une décision collective. »", 5, "pb-1 ic-1 em-1"),
            R("« Si. Moi, je suis responsable de ce que je vous ai dit lundi. »", 3, "pb3 er1"),
            R("« Ce n'est pas le moment de chercher un responsable. »", 5, "er-1 pb-1 em-1"),
        ]),
        I(7, "sofia", "sad",
          "« Il est rentré à la maison et il a fermé la porte de sa chambre. Il a regardé le "
          "mur pendant six semaines. Je lui apportais sa soupe et il me disait merci. C'est "
          "tout. Merci. » Elle s'essuie les yeux. « Ma mère, c'est tout ce qui me reste. »", [
            R("« Ce que vous décrivez, c'est de la solitude, pas de la vérité. Votre mère, en ce "
              "moment, fait le contraire : elle se prépare, et elle veut vous en parler. »",
              9, "em2 co2 cc2 rd1"),
            R("« Je suis désolé·e. »", 9, "em1 co1"),
            R("« Vous devriez peut-être consulter pour ce traumatisme. »", 8, "pb-1 em-2 co-1"),
            R("Se taire, et lui tendre un mouchoir.", 9, "co2 em1"),
        ]),
        I(8, "sofia", "cold-anger",
          "Elle vous fixe. « Vous me faites la leçon ? Vous avez quel âge ? »", [
            R("« Non. Pardon. Je vous écoute. »", 7, "er2 em2 rd1"),
            R("« Je dis simplement les faits. »", 5, "em-2 er-1"),
            R("« Vingt-trois ans. Vous avez raison, je n'ai pas votre expérience de ça. »", 7, "er2 rd1"),
            R("« L'âge ne change rien à la loi. »", 5, "er-2 em-2"),
        ]),
        I(9, "sofia", "anxious",
          "« Elle va arrêter, c'est ça ? » Elle serre ses genoux. « Elle va refuser la chimio "
          "et se laisser mourir, comme lui. »", [
            R("« Je ne peux pas parler à sa place. Ce que je peux faire, c'est lui dire que "
              "vous êtes là et que vous voulez comprendre — et lui proposer qu'on se voie tous "
              "les trois. »", 12, "pb2 ic2 em2 cc1"),
            R("« Si elle refuse, c'est son droit. »", 12, "pb1 em-2 co-1"),
            R("« Non, ne vous inquiétez pas. On va la convaincre de se battre. »",
              13, "pb-3 rd-3 cc-1"),
            R("« Je ne sais pas ce qu'elle décidera. Mais je sais qu'elle ne veut pas le faire sans vous. »", 12, "em2 cc2"),
        ]),
        I(10, "sofia", "sad",
          "Le mot tombe. Sofia se plie en deux sur la chaise, sans un son. Inès Rey, qui a "
          "entendu depuis la porte, vous regarde. Mme Haddad avait demandé une seule chose : "
          "le dire elle-même à sa fille.", [
            R("S'asseoir près de Sofia, attendre, puis : « Je n'aurais pas dû vous le dire "
              "comme ça. Votre mère voulait le faire elle-même. Je vais le lui avouer. »",
              14, "pb1 er1 co2 cc1"),
            R("« Elle allait l'apprendre de toute façon. »", 14, "pb-3 rd-3 co-1"),
            R("Appeler Inès du regard, et rester près de Sofia.", 14, "ic2 co1"),
            R("« Voilà. Maintenant, vous savez. »", 14, "rd-3 co-3 pb-1"),
        ]),
        I(11, "ines", "neutral",
          "Inès s'assoit à côté de Sofia. « Le Dr Moreau peut passer à 16 h. » Sofia hoche "
          "la tête, vidée. Puis, sans regarder personne : « Pourquoi elle ne m'a rien dit, à "
          "moi ? »", [
            R("« Peut-être pour la même raison que vous lundi : pour vous protéger, elle "
              "aussi. »", 12, "em3 co2 cc1"),
            R("« Il faudra le lui demander. »", 12, "cc1 em-1"),
            R("« Je ne peux pas répondre à ça. »", 12, "em-1 cc-1"),
            R("« Qu'est-ce que vous auriez voulu entendre, vous ? »", 12, "em3"),
        ]),
        I(12, "sofia", "neutral",
          "Un long silence. Les pivoines gouttent sur le desk. « Vous croyez qu'elle voudra "
          "me parler ? »", [
            R("« Je crois qu'elle attend ce moment depuis trois jours. Je peux lui demander si "
              "elle veut que ce soit aujourd'hui ou demain, avec moi ou sans moi. »",
              15, "em2 cc2 ic1 rd2"),
            R("« Je ne sais pas. »", 15, "cc0 em0"),
            R("« Laissez-lui le temps, elle viendra vers vous. »", 15, "cc-1 ic-1"),
            R("« Je vais lui demander maintenant, et je reviens vous dire sa réponse. »", 15, "ic2 cc2 rd1"),
            R("« Oui. Elle me l'a presque dit, ce matin. »", 15, "em1 pb-2"),
        ]),
        I(13, "moreau", "cold-anger",
          "Dr Moreau est entré·e sans que vous l'entendiez. « Convaincre ? » Le ton est égal. "
          "« Madame Haddad, je suis Dr Moreau. Je crois que l'étudiant·e a voulu vous "
          "rassurer. Alex, reformulez. »", [
            R("« Je retire ce mot. Je ne peux promettre ni qu'elle se battra ni qu'elle "
              "arrêtera. C'est elle qui décidera, et vous serez là. »", 12, "pb2 er2 cc2"),
            R("« Je voulais dire qu'on l'encouragerait. »", 12, "pb-1 cc-1"),
            R("« Pardon. Je ne peux pas promettre à votre place ce que votre mère choisira. »", 12, "pb2 cc1"),
            R("« Mais on peut quand même l'encourager un peu. »", 12, "pb-2 rd-2"),
        ]),
        I(14, "haddad", "cold-anger",
          "Chambre 308, dix minutes plus tard. Mme Haddad pose son mot fléché. « Vous lui "
          "avez dit. » Ce n'est pas une question. « Je vous avais demandé une seule chose. »", [
            R("« Oui. Je lui ai dit le mot que vous vouliez dire vous-même. Je vous demande "
              "pardon. Elle est dans le petit salon — si vous voulez, je vais la chercher, et "
              "vous lui dites le reste avec vos mots. »", 15, "rd2 pb2 co1 cc2"),
            R("« Elle était tellement en colère, je n'ai pas su faire autrement. »", 15, "pb-1 er-1"),
            R("« De toute façon, elle l'aurait deviné. »", 15, "rd-2 pb-2"),
            R("« Je vous demande pardon. Qu'est-ce que je peux faire, maintenant ? »", 15, "rd2 pb1"),
        ]),
        I(15, "ines", "neutral",
          "Fin d'après-midi. Inès ouvre le dossier de Mme Haddad. « Qu'est-ce que je note pour "
          "l'équipe ? La fille va revenir ce soir, et c'est ma collègue qui sera là. »", [
            R("« Ce que Sofia sait et comment elle l'a appris, qu'une rencontre à trois est "
              "proposée demain à la demande de la patiente, et qu'on renvoie toute question "
              "de Sofia vers sa mère ou le Dr Moreau. Je rédige, vous relisez ? »",
              END, "ic3 cc3 pb1 rd1"),
            R("« Que la fille est au courant, maintenant. »", END, "cc0 ic0"),
            R("« Rien. Il vaut mieux ne pas trop écrire. »", END, "cc-3 ic-2 pb-2"),
            R("« La même phrase que pour la nuit : pas de réponse au téléphone, on renvoie vers sa mère. »", -1, "cc2 ic2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 2.5 La chaise du jardin — nouvelle scène
# ---------------------------------------------------------------------------
S2_5 = S(5, "2.5 La chaise du jardin",
    "Vendredi, 10 h. Mme Haddad a demandé à parler à sa fille, et que vous soyez dans la "
    "pièce. Sofia attend dans le couloir. Mme Haddad a mis un gilet et s'est coiffée.",
    focus=("rd", "co", "cc", "em"),
    nodes=[
        I(1, "haddad", "neutral",
          "« Vous restez. » Elle lisse son gilet. « Mais vous ne parlez que si je vous "
          "regarde. C'est ma nouvelle, pas la vôtre. »", [
            R("« D'accord. Je serai là, un peu en retrait, et je me tais. »", 2, "rd3 pb2 er1"),
            R("« Vous êtes sûre de ne pas préférer que le Dr Moreau s'en charge ? »", 3, "rd-1 ic0 er-1"),
            R("« Je vais d'abord résumer la situation médicale à votre fille, ce sera plus "
              "simple pour vous. »", 4, "rd-3 pb-2"),
            R("« Voulez-vous qu'Inès soit là aussi, ou seulement moi ? »", 2, "rd2 ic1"),
            R("« Je préfère dire les choses médicales moi-même, pour éviter les erreurs. »", 4, "rd-3 pb-3 cc-1"),
        ]),
        I(2, "haddad", "neutral",
          "Sofia entre, s'assoit au bord du lit. Mme Haddad lui prend la main. « Ma chérie. "
          "J'ai un cancer du pancréas. » Sofia ne dit rien. Puis elle se tourne vers vous. "
          "« C'est vrai ? Il n'y a rien à faire ? » Mme Haddad vous regarde : c'est à vous.", [
            R("« C'est vrai. Il y a des traitements qui peuvent ralentir la maladie, et "
              "d'autres qui soulagent. Votre mère a commencé à réfléchir à ce qu'elle veut. »",
              5, "cc3 rd2 em1"),
            R("« Il y a toujours quelque chose à faire. »", 6, "cc-1 pb-1"),
            R("« Les chiffres sont mauvais, oui. La survie dépasse rarement un an. »", 7, "co-2 em-2 cc0"),
            R("Regarder Mme Haddad : « Voulez-vous que je réponde, ou que je complète ce que vous direz ? »", 5, "rd3 cc1"),
            R("« Ce n'est pas à moi de vous le dire. »", 6, "cc-2 em-1"),
        ]),
        I(3, "haddad", "cold-anger",
          "« Si je voulais qu'on le fasse à ma place, je vous l'aurais demandé. » Elle vous "
          "regarde par-dessus ses lunettes, comme six cents élèves avant vous.", [
            R("« Pardon. Je reste, et je me tais. »", 2, "rd2 er1"),
            R("« Je voulais seulement vous épargner ça. »", 2, "rd-2 er-1"),
            R("Hocher la tête, et reculer d'un pas.", 2, "rd2"),
            R("« C'était une proposition, ne vous vexez pas. »", 2, "rd-2 er-2"),
        ]),
        I(4, "haddad", "cold-anger",
          "« Jeune personne. » Le ton ferait rentrer une classe entière. « C'est ma fille et "
          "c'est ma maladie. Asseyez-vous. »", [
            R("« Pardon. Je vous laisse la parole. »", 2, "rd2 er1 pb1"),
            R("« Je voulais bien faire. »", 2, "rd-1 er-1"),
            R("S'asseoir, et se taire.", 2, "rd2 er1"),
            R("« Il faut bien que quelqu'un donne les chiffres. »", 2, "rd-3 co-2"),
        ]),
        I(5, "sofia", "anxious",
          "« Maman, tu vas faire la chimio ? » Mme Haddad secoue la tête. « Non. » Sofia se "
          "tourne vers vous, blanche. « Vous allez la laisser faire ça ? »", [
            R("« C'est sa décision, et elle la prend en sachant de quoi il s'agit. Ce qu'on "
              "peut faire ensemble, c'est s'assurer qu'elle ne souffre pas et qu'elle vive ce "
              "temps comme elle le souhaite. »", 8, "rd3 pb2 co2 cc1 em1"),
            R("Regarder Mme Haddad, et lui laisser la réponse.", 8, "rd2 er1"),
            R("« Vous devriez peut-être essayer de la convaincre. »", 9, "rd-3 pb-3 co-1"),
            R("« Vous avez peur qu'elle abandonne. Ce n'est pas ce qu'elle est en train de faire. »", 8, "em3 cc1 rd1"),
        ]),
        I(6, "sofia", "suspicious",
          "« Quelque chose. » Sofia a un rire sec. « Toujours quelque chose. C'est exactement "
          "ce qu'ils disaient pour papa. » Mme Haddad soupire.", [
            R("« Vous avez raison, c'était flou. Je reprends : on ne guérira pas ce cancer. On "
              "peut le ralentir un peu, et surtout soulager. »", 5, "cc3 er1 rd1"),
            R("« Je voulais dire qu'on ne baisse pas les bras. »", 5, "cc-1"),
            R("« Pardon. Le vrai mot, c'est : on ne guérira pas. On peut accompagner. »", 5, "cc3 co1"),
            R("« Chaque cas est différent. »", 5, "cc-2"),
        ]),
        I(7, "sofia", "angry",
          "Sofia lâche la main de sa mère. « Des chiffres. Voilà. Exactement comme lui. » Mme "
          "Haddad ferme les yeux. « Sofia. »", [
            R("« Pardon. Ce n'est pas un chiffre qui décidera de ce qui compte pour votre mère. "
              "C'est elle. »", 5, "em2 co1 er1 rd2"),
            R("« Vous m'avez demandé s'il y avait quelque chose à faire. »", 5, "er-2 em-2"),
            R("Se taire, et laisser Mme Haddad reprendre la main de sa fille.", 5, "er2 rd2"),
            R("« Je ne fais que mon travail. »", 5, "er-2 co-2"),
        ]),
        I(8, "haddad", "melancholic",
          "« Je veux rentrer. » Elle regarde la fenêtre. « J'ai une chaise sous le cerisier, au "
          "fond du jardin. Je veux être là quand ça se passera. Pas ici. » Sofia se met à "
          "pleurer sans bruit.", [
            R("À Sofia : « Est-ce que ça vous semble possible, de votre côté ? Il existe des "
              "soins à domicile, une équipe mobile de soins palliatifs, des gens joignables la "
              "nuit. On peut en parler avec l'équipe dès aujourd'hui. »", 10, "ic3 co2 cc2 em1"),
            R("« Ça va être difficile à organiser. »", 10, "co-1 ic-1"),
            R("« À l'hôpital, vous seriez quand même plus en sécurité. »", 11, "rd-2 pb-1 co-1"),
            R("« C'est une belle chose à vouloir. Qu'est-ce qu'il vous faudrait, pour que ce soit possible ? »", 10, "rd3 co2"),
        ]),
        I(9, "haddad", "cold-anger",
          "Mme Haddad retire ses lunettes. « Vous aussi, alors. » Elle ne s'adresse plus qu'à "
          "vous. « Vous voulez que je me batte pour que ma fille dorme mieux. »", [
            R("« Non. Pardon. Je retire ce que j'ai dit. Ce que vous voulez compte d'abord. »",
              8, "rd2 pb2 er1"),
            R("« Je pensais à Sofia. »", 8, "rd-1 em1"),
            R("« Vous avez raison. Je me suis mis·e à la place de Sofia, pas à la vôtre. »", 8, "rd2 er2"),
            R("« Il faut aussi penser aux autres. »", 8, "rd-2 em-1"),
        ]),
        I(10, "sofia", "sad",
          "« Et si ça se passe mal ? » Sofia s'essuie les yeux avec la manche. « Si elle "
          "étouffe, si elle a mal, la nuit, et que je suis seule avec elle ? »", [
            R("« C'est une vraie peur, et elle a des réponses : des médicaments préparés "
              "d'avance, une équipe joignable la nuit, et le droit de revenir. Rentrer n'est "
              "pas un aller simple. »", 12, "em3 cc3 co2 ic1"),
            R("« Vous pourrez toujours appeler les urgences. »", 12, "cc-1 co-1"),
            R("« Elle a choisi, il faudra l'assumer. »", 12, "co-3 em-2 rd-1 er-1"),
            R("« Vous ne serez pas seule. Je peux demander à l'équipe mobile de passer vous expliquer, avant le départ. »", 12, "ic3 co2"),
        ]),
        I(11, "sofia", "angry",
          "« Vous voyez ? » Sofia se tourne vers sa mère. « Même lui dit que c'est "
          "dangereux. » Mme Haddad vous regarde avec une déception d'institutrice.", [
            R("« Je me suis mal exprimé·e. Ce qui compte, c'est ce que votre mère veut. Notre "
              "travail, c'est de rendre ce choix sûr. »", 10, "rd2 cc2 er1"),
            R("« Je dis simplement que l'hôpital a plus de moyens. »", 10, "rd-2 pb-1"),
            R("« Non. Ce que je voulais dire, c'est qu'il faut préparer le retour, pas l'empêcher. »", 10, "cc2 rd1"),
            R("« Je ne changerai pas d'avis. »", 10, "rd-2 er-1"),
        ]),
        I(12, "haddad", "neutral",
          "Mme Haddad sort une enveloppe de son sac. « Sofia, tu es ma personne de confiance. "
          "Je veux que tu saches ce qui est écrit là-dedans. » Sofia recule. « Je ne veux pas "
          "lire ça. »", [
            R("« Vous n'êtes pas obligée aujourd'hui. Mais ce papier, c'est votre mère qui vous "
              "parle pour le jour où elle ne pourra plus. C'est aussi une façon de vous "
              "protéger, vous. »", 13, "em2 co2 cc2 rd1"),
            R("« C'est important, il faudrait le lire. »", 13, "cc1 em-1"),
            R("« Si vous ne le lisez pas, on appliquera ce qui est écrit sans vous. »", 13, "em-3 co-2"),
            R("« Voulez-vous qu'on le lise ensemble, tout à l'heure, quand vous serez prête ? »", 13, "em2 co2"),
        ]),
        I(13, "sofia", "sad",
          "Sofia déplie la feuille. Elle lit à voix haute, d'une voix cassée : « Pas de "
          "réanimation. Pas de sonde. La chaise du jardin. » Elle rit à travers ses larmes. "
          "« Elle a même écrit la chaise. » Puis, vers vous : « Pardon pour hier. »", [
            R("« Vous n'avez pas à vous excuser. Vous aimez votre mère. »", 14, "co3 em2"),
            R("« C'est oublié. »", 14, "co1"),
            R("« J'ai l'habitude. »", 14, "em-1 co-1 er-1"),
            R("Sourire, et ne rien dire.", 14, "co2"),
        ]),
        I(14, "ines", "neutral",
          "Dans le couloir, Inès Rey a déjà le téléphone à la main. « J'appelle les soins à "
          "domicile et l'équipe mobile de soins palliatifs. Alex, vous faites la lettre pour "
          "le médecin traitant ? »", [
            R("« Oui : diagnostic, ce que la patiente sait et veut, ses directives, le refus de "
              "réanimation, les réserves médicamenteuses et le numéro de l'équipe de nuit. Je "
              "vous la montre avant de l'envoyer. »", END, "ic3 cc3 pb1"),
            R("« Oui, je m'en occupe. »", END, "ic1"),
            R("« C'est plutôt au Dr Neuhaus de la faire, non ? »", END, "ic-2 pb-1"),
            R("« Oui. Et j'appelle moi-même le médecin traitant pour lui raconter. »", -1, "ic3 cc1"),
        ]),
    ],
)

CH2 = C(2, "Et si on ne disait rien ?",
    situation=(
        "Deuxième semaine. La fille de Mme Haddad demande à Alex de cacher le diagnostic "
        "à sa mère. Tout le service s'en mêle : l'infirmière de nuit, l'oncologue, le "
        "colloque — et la patiente elle-même, qui n'a rien d'une personne à protéger."
    ),
    objectives=(
        "identifier le pacte de silence familial, accueillir la peur des proches sans "
        "s'engager à mentir, poser que l'information appartient au patient capable de "
        "discernement — y compris son droit de ne pas savoir et de choisir qui est "
        "informé —, distinguer représentant thérapeutique et personne présente, recueillir "
        "des directives anticipées, porter la décision en équipe, la rédiger de façon "
        "opposable et la transmettre ; puis tenir face à la colère d'un proche et "
        "accompagner une patiente qui annonce elle-même sa maladie à sa fille."
    ),
    anchoring=(
        "UNIL M1.7 droit médical, éthique de la prise de décision · UNIGE Master, "
        "disciplines transversales Médecine légale et éthique, enseignement "
        "interprofessionnel, médecine palliative."
    ),
    focus=("rd", "cc", "pb", "em"),
    scenes=[S2_1, S2_2, S2_3, S2_4, S2_5],
)
