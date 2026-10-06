"""Chapitre 3 — Le doute (semaine 3, policlinique)."""
from __future__ import annotations

from .dsl import END, C, Entry, I, R, S, when

# Reprise de la v1 : scène 3.1 La consultation
S3_1 = S(1, "3.1 La consultation",
    "Semaine de policlinique de médecine interne, supervisée par Dr Moreau. Yann Dubois, 26 ans, céphalées et paresthésies intermittentes depuis trois mois. Bilan biologique normal, IRM cérébrale sans particularité. Il vient chercher une réponse.",
    focus=("cc", "em", "er"),
    nodes=[
        I(1, "yann", "anxious", "Il s'assoit sans enlever sa veste. « Alors ? Vous avez les résultats de l'IRM ? »", [
            R("« Oui. Avant de vous les donner, dites-moi : qu'est-ce que vous redoutiez en faisant cet examen ? »", 2, "rd2 em3 cc3"),
            R("« Oui, tout est normal. Rien à signaler. »", 3, "em-1 cc1"),
            R("« L'IRM ne montre rien d'anormal, la biologie non plus. On n'a pas d'explication organique pour l'instant. »", 4, "cc2"),
            R("« Oui, et je vais vous les donner. Juste avant : comment vous sentez-vous, depuis la dernière fois ? »", 2, "em2 cc1"),
            R("« C'est dans votre tête, l'IRM est parfaite. »", 4, "rd-3 em-3 cc-1", sets=["yann_stress"]),
        ]),
        I(2, "yann", "anxious", "« Une tumeur. Ma tante est morte d'un glioblastome à trente-deux ans. Depuis trois mois je ne pense qu'à ça. »", [
            R("« Ça éclaire beaucoup de choses. Alors je vous le dis tout de suite : l'IRM ne montre aucune tumeur. » — puis laisser le temps.", 5, "rd2 em3 co3 cc3"),
            R("« Ce n'est pas une tumeur, rassurez-vous, c'est certainement le stress. »", 4, sets=["yann_stress"], scores="cc-2"),
            R("« Les antécédents familiaux de glioblastome ne sont pas un facteur de risque établi. »", 3, "em-3 co-2 cc1"),
            R("« Trois mois avec cette peur, ça a dû être très lourd. L'IRM ne montre pas de tumeur. »", 5, "em3 co2 cc2"),
            R("« Il faut arrêter de lire internet. »", 3, "rd-2 em-2"),
        ]),
        I(3, "yann", "angry", "« Normal ? » Il se penche en avant. « Mais j'ai mal tous les jours. Vous êtes en train de me dire que j'invente ? »", [
            R("« Pas du tout, et je me suis mal exprimé·e. Vos symptômes sont réels. Ce que je voulais dire, c'est que les examens n'ont pas trouvé de cause grave — ce qui ne veut pas dire qu'il n'y a rien. »", 5, "rd3 em3 er3 cc3"),
            R("« Personne n'a dit ça. Les examens sont normaux, c'est une bonne nouvelle. »", 4, "rd-2 em-2 er-1 cc-1"),
            R("« Non. Vous avez mal, c'est réel. Je vous explique ce que les examens ont écarté. »", 5, "em2 cc2 rd1"),
            R("« Je ne dis pas que vous inventez, je dis que c'est psychologique. »", 4, "rd-2 em-2 cc-1", sets=["yann_stress"]),
        ]),
        I(4, "yann", "angry", "« Donc c'est dans ma tête. » Il a un rire court. « J'ai lu que c'est ce que les médecins disent quand ils ne trouvent pas. »", [
            R("« Je n'ai pas dit ça et je ne le pense pas. Je vous dis quelque chose de plus inconfortable : à ce stade, je ne sais pas. Et je préfère vous le dire plutôt que de vous inventer un diagnostic. »", 5, "rd3 em2 er3 cc3"),
            R("« Le stress peut vraiment donner ces symptômes, vous savez. »", 6, sets=["yann_stress"], scores="rd-1 em-1 cc-1"),
            R("« Je vous propose de refaire une IRM dans trois mois pour être sûr. »", 7, "cc-1 pb-1"),
            R("« Non. Ça veut dire qu'on n'a pas encore trouvé, pas qu'il n'y a rien. »", 5, "cc3 em1"),
            R("« Beaucoup de symptômes viennent du stress, c'est très fréquent. »", 6, "cc-1 em-2", sets=["yann_stress"]),
        ]),
        I(5, "yann", "confused", "Il ferme les yeux quelques secondes. « D'accord. » Puis il rouvre les yeux. « Mais alors c'est quoi ? »", [
            R("« C'est la question à laquelle je ne peux pas encore répondre. Ce que je peux faire, c'est vous dire ce qui est écarté, ce qui reste possible, et comment on avance. »", 8, "rd3 cc3 pb2"),
            R("« Probablement des céphalées de tension. C'est le plus fréquent à votre âge. »", 6, "cc-1 pb-1"),
            R("« On ne le saura peut-être jamais, et ce n'est pas grave. »", 6, "em-2 co-2 cc-2"),
            R("« Je ne sais pas encore. On va chercher ensemble, avec méthode. »", 8, "cc2 er1"),
            R("« Le stress, tout simplement. »", 6, "cc-2 em-2 rd-1", sets=["yann_stress"]),
        ]),
        I(6, "yann", "suspicious", "« Céphalées de tension. » Il note sur son téléphone. « Et ça se soigne comment, une chose que vous n'êtes même pas sûr d'avoir trouvée ? »", [
            R("« Vous avez raison de me reprendre. Je suis allé·e trop vite : c'est une hypothèse, pas un diagnostic. Reprenons ce qui est certain et ce qui ne l'est pas. »", 8, "rd3 er3 cc3"),
            R("« Par des antalgiques simples et de l'hygiène de vie. »", 8, "cc-1 pb-1"),
            R("« Bonne question. Je n'aurais pas dû donner un nom si vite. »", 8, "cc2 er1 pb1"),
            R("« Faites-moi confiance. »", 8, "cc-2 rd-1"),
        ]),
        I(7, "moreau", "cold-anger", "Dr Moreau, qui supervise la consultation depuis le bureau voisin, vous interpelle à la pause. « Une IRM de contrôle à trois mois sur une IRM normale, c'est pour lui ou pour vous ? »", [
            R("« Pour moi, honnêtement. Pour ne pas avoir à porter le doute. Je retire la proposition et je construis un suivi clinique à la place. »", 8, "er3 cc3 pb3 ic2"),
            R("« Ça le rassurera, et ça ne coûte pas grand-chose. »", 8, "er-1 cc-2 pb-2"),
            R("« Je ne sais pas. Un peu pour me rassurer, je crois. »", 8, "er2 pb1"),
            R("« Pour lui, évidemment. Il veut des examens. »", 8, "pb-2 er-1"),
        ]),
        I(8, "yann", "neutral", "« D'accord. Dites-moi ce qui est écarté, alors. »", [
            R("« L'IRM écarte une tumeur, une malformation vasculaire et une sclérose en plaques visible. La prise de sang écarte une anémie, un problème thyroïdien et une inflammation importante. Ça, c'est solide. »", 9, "rd3 cc3 pb2"),
            R("« Tout ce qui est grave est écarté. »", 9, "rd-1 cc-2"),
            R("« Une IRM normale n'écarte jamais tout à 100 %. »", 9, "em-2 co-2"),
            R("« Je vous montre les images et le compte-rendu, si vous voulez. »", 9, "cc2 rd1"),
        ]),
        I(9, "yann", "neutral", "« Et ce qui reste ? »", [
            R("« Des céphalées primaires — migraine, céphalée de tension —, un trouble du sommeil, une composante anxieuse qui amplifie la douleur. Aucune ne s'exclut : elles se combinent souvent. »", 10, "rd3 cc3"),
            R("« Beaucoup de choses. On ne peut pas faire la liste. »", 10, "rd-1 em-1 cc-2"),
            R("« Plusieurs pistes, dont aucune n'est grave. Je vous les liste. »", 10, "cc2"),
            R("« Du stress, surtout. »", 10, "cc-2 em-2", sets=["yann_stress"]),
        ]),
        I(10, "yann", "angry", "Il se raidit. « Anxieuse. Voilà, on y arrive. »", [
            R("« Je comprends que le mot vous hérisse. Je ne dis pas que la douleur est imaginaire : je dis que l'anxiété modifie réellement la façon dont le cerveau traite la douleur. C'est un mécanisme physiologique, pas un jugement. »", 11, "rd3 em3 er3 cc3"),
            R("« Ce n'est pas péjoratif, tout le monde est anxieux. »", 11, "rd-1 em-1 cc-1"),
            R("« Vous voyez bien que vous réagissez fortement. »", 11, sets=["yann_stress"], scores="rd-3 em-3 er-2 cc-2"),
            R("« Je retire le mot s'il vous gêne. Ce qui compte, c'est que votre douleur est réelle. »", 11, "em2 rd2"),
        ]),
        I(11, "yann", "sad", "Il se tait, puis plus bas : « J'ai passé trois mois à me dire que j'allais mourir comme ma tante. Je n'ai pas dormi. »", [
            R("« Trois mois. C'est long, et ça compte autant que l'IRM. Est-ce que vous en avez parlé à quelqu'un ? »", 12, "rd3 em3 co3 cc2"),
            R("« Maintenant vous savez que ce n'est pas ça, vous allez pouvoir souffler. »", 12, "em-1"),
            R("« C'est justement ce que je vous disais sur l'anxiété. »", 12, sets=["yann_stress"], scores="rd-2 em-3 co-2"),
            R("Laisser le silence, puis : « Trois mois seul avec ça. »", 12, "em3 co2"),
        ]),
        I(12, "yann", "confused", "« À personne. Ma copine croit que je viens pour des maux de tête. » Il hausse les épaules. « Je ne voulais pas l'inquiéter pour rien. »", [
            R("« Vous avez porté ça seul pendant trois mois. C'est peut-être ça qu'il faut traiter en premier, autant que les céphalées. »", 13, "rd3 em3 co3 cc3"),
            R("« Il faudrait lui en parler, ça vous soulagerait. »", 13, "em1 co1 cc1"),
            R("« Revenons aux symptômes. »", 13, "rd-2 em-3 co-3 cc-1"),
            R("« Qu'est-ce qui vous empêche de lui en parler ? »", 13, "em2 rd1"),
        ]),
        I(13, "yann", "neutral", "« Vous croyez vraiment que dormir changerait quelque chose ? »", [
            R("« Le manque de sommeil abaisse le seuil de douleur, c'est documenté. Ce n'est pas une explication magique, mais c'est un levier sur lequel on peut agir dès cette semaine. »", 14, "rd2 cc3"),
            R("« Ça ne peut pas faire de mal. »", 14, "cc-1"),
            R("« Je ne sais pas. Mais ça vaut la peine d'essayer, et de noter ce que ça change. »", 14, "cc2 er1"),
            R("« Ça ne peut pas faire de mal. C'est sûrement le stress. »", 14, "cc-1 em-1", sets=["yann_stress"]),
        ]),
        I(14, "yann", "neutral", "« Bon. On fait quoi, alors ? »", [
            R("« Trois choses : un agenda des céphalées pendant trois semaines, un traitement de crise simple mais pris tôt, et un rendez-vous fixé maintenant avec une date. Vous ne repartez pas dans le vide. »", 15, "rd3 co2 cc3 pb3"),
            R("« On attend et on voit. Si ça s'aggrave, vous revenez. »", 16, "cc-1 pb-1"),
            R("« Je vous adresse à un neurologue, ce sera plus sûr. »", 16, "cc1 ic1"),
            R("« Un rendez-vous fixé, un agenda, et une liste de signes qui doivent vous faire revenir tout de suite. »", 15, "cc3 pb1"),
        ]),
        I(15, "yann", "neutral", "« Un agenda ? Je note quoi ? »", [
            R("« Le jour, l'heure de début, l'intensité sur 10, ce que vous faisiez avant, et ce que vous avez pris. C'est ce qui nous dira si c'est une migraine ou autre chose — plus que n'importe quel examen. »", 17, "rd3 cc3 pb2 ic1"),
            R("« Quand vous avez mal, en gros. »", 17, "cc-2 pb-1"),
            R("« Je vous donne un modèle, et vous me l'apportez au prochain rendez-vous. »", 17, "cc2 ic1"),
            R("« Ce que vous voulez, c'est pour vous. »", 17, "cc-2"),
        ]),
        I(16, "yann", "anxious", "« Revenir quand ? Au bout de combien de temps ? Avec quoi ? » Il sort son téléphone. « Parce que sur les forums, on me dit que dans mon cas il faut insister. »", [
            R("« Vous avez raison d'insister, ma réponse était trop vague. Reprenons : un agenda, un traitement, une date de contrôle, et des signes qui doivent vous faire venir avant. »", 15, "rd3 em2 er2 cc3 pb3"),
            R("« Ne vous fiez pas aux forums, chaque cas est différent. »", 17, "rd-1 em-1"),
            R("« Revenez dans trois semaines, et plus tôt si certains signes apparaissent : je vous les écris. »", 17, "cc3 pb1"),
            R("« Les forums disent n'importe quoi. »", 17, "cc-1 rd-1"),
        ]),
        I(17, "yann", "anxious", "« Et si ça empire ? Je fais comment pour savoir si c'est grave ? »", [
            R("« Un mal de tête brutal et différent des autres ; un déficit — bras, jambe, parole, vision ; une fièvre avec raideur de nuque ; un réveil nocturne par la douleur ou des vomissements le matin. N'importe lequel : urgences le jour même. Je vous l'écris. »", 18, sets=["yann_filet"], scores="rd3 co2 cc3 pb3"),
            R("« Si ça empire vraiment, vous verrez bien. »", 18, "rd-2 cc-3 pb-3"),
            R("« Tenez, je vous imprime une brochure sur les céphalées. »", 18, "em-1"),
            R("« Je vous écris ce qui doit vous faire venir le jour même : un trouble de la vision, une faiblesse, un trouble de la parole, un mal de tête brutal. »", 18, "cc3 pb2", sets=["yann_filet"]),
            R("« Ne vous inquiétez pas, rien de grave n'arrivera. »", 18, "cc-3 pb-2"),
        ]),
        I(18, "yann", "neutral", "Il plie la feuille. « Vous êtes étudiant·e, en fait. » Ce n'est pas agressif. « Est-ce que quelqu'un de plus expérimenté a regardé mon dossier ? »", [
            R("« Oui, et c'est une question légitime. Dr Moreau a relu votre IRM et votre bilan avec moi ce matin. Je peux lui demander de passer maintenant si vous le souhaitez. »", 19, "rd3 cc3 pb3 ic3"),
            R("« Ne vous inquiétez pas, je sais ce que je fais. »", 19, "rd-2 cc-2 pb-2 ic-2"),
            R("« Je suis supervisé·e, c'est la règle. »", 19, "cc1 pb2 ic1"),
            R("« Oui : le Dr Moreau. Vous voulez qu'on le voie ensemble maintenant ? »", 19, "cc2 ic2 rd1"),
        ]),
        I(19, "yann", "neutral", "Il range la feuille dans sa poche. « Bon. Au moins je sais ce que je ne sais pas. »", [
            R("« C'est exactement ça. Et si dans trois semaines rien ne va mieux, on ne recommence pas de zéro : on reprend là où on en est. »", 20, "rd2 co2 cc3 pb2"),
            R("« Voilà. Bonne journée. »", 20, "em-2 co-2"),
            R("« Et vous savez quoi faire si quelque chose change. »", 20, "cc2"),
            R("« Voilà. C'était rien, finalement. »", 20, "cc-2 em-1", sets=["yann_stress"]),
        ]),
        I(20, "moreau", "neutral", "Après son départ. « Vous écrivez quoi dans ce dossier ? C'est une consultation sans diagnostic : c'est là que la note compte le plus. »", [
            R("« Le raisonnement, pas seulement les résultats : ce que j'ai écarté et sur quelle base, les hypothèses retenues, les signes d'alerte remis au patient par écrit, et la date de contrôle. »", -1, "rd2 cc3 pb3 ic3"),
            R("« Les résultats d'examens et ma conclusion. »", -1, ""),
            R("« Que tout était normal. »", -1, "cc-3 pb-2 ic-2"),
            R("« Ce qui est écarté, ce qui reste ouvert, et la date du prochain rendez-vous. »", -1, "cc2 pb1"),
        ]),
    ],
)

# Reprise de la v1 : scène 3.2 Le résultat qui n'en est pas un
S3_2 = S(2, "3.2 Le résultat qui n'en est pas un",
    "Même consultation, l'après-midi. Malick Sow, 31 ans, était venu pour un bilan de routine avec un dépistage qu'il avait demandé lui-même. Le test de dépistage VIH est revenu réactif. Le test de confirmation part au laboratoire : résultat sous 48 heures.",
    focus=("cc", "em", "rd"),
    nodes=[
        I(1, "moreau", "neutral", "« Avant que vous l'appeliez. Un test de dépistage réactif, chez un homme sans facteur de risque identifié, dans une population à faible prévalence : qu'est-ce que ça vaut ? »", [
            R("« Ce n'est pas un diagnostic. La valeur prédictive positive dépend de la prévalence : dans ce contexte, une part non négligeable des tests réactifs sont des faux positifs. Seul le test de confirmation tranchera. »", 2, "rd2 cc3 pb3"),
            R("« C'est un test très sensible, donc c'est probablement positif. »", 3, "cc-2 pb-2"),
            R("« On ne peut rien en dire du tout. »", 3, "cc-2"),
            R("« Qu'il faut le confirmer avant d'en dire quoi que ce soit. »", 2, "cc2 pb1"),
            R("« Qu'il est sûrement séropositif. »", 3, "cc-3 pb-3"),
        ]),
        I(2, "moreau", "neutral", "« Bien. Deuxième question, plus difficile : est-ce que vous lui dites aujourd'hui, ou est-ce que vous attendez 48 heures la confirmation ? »", [
            R("« Je lui dis aujourd'hui. C'est son résultat, il l'a demandé lui-même, et il reviendra de toute façon chercher une réponse. Ce que je dois soigner, c'est la formulation : un résultat en attente, pas un diagnostic. »", 4, "rd3 er2 cc3 pb3"),
            R("« J'attends la confirmation, ça évite de l'inquiéter pour rien. »", 3, "rd-3 cc-2 pb-3"),
            R("« Je lui dis qu'il est séropositif, il faut qu'il se prépare. »", 3, "rd-2 cc-3 pb-3"),
            R("« Aujourd'hui, en présentant le résultat pour ce qu'il est : un test à confirmer. »", 4, "cc2 pb2 rd1"),
        ]),
        I(3, "moreau", "cold-anger", "« Les deux extrêmes sont fautifs. Se taire, c'est le déposséder d'un résultat qui lui appartient. Affirmer, c'est lui annoncer une maladie qu'il n'a peut-être pas. Où est le chemin ? »", [
            R("« Dire exactement ce qu'on sait : le test de dépistage est réactif, ça impose un test de confirmation, et on l'aura dans 48 heures. Ni plus, ni moins. »", 4, "rd3 cc3 pb3"),
            R("« Lui dire qu'il y a un petit souci sur le bilan. »", 4, "rd-2 cc-3"),
            R("« Dire ce qu'on sait, pas plus : un test réactif à confirmer, résultat dans 48 heures. »", 4, "cc2 pb2"),
            R("« Attendre, pour ne pas lui gâcher sa soirée. »", 4, "rd-2 pb-2"),
        ]),
        I(4, "malick", "happy", "Il s'assoit, détendu. « Alors, je suis en pleine forme ? J'ai promis à ma copine de lui dire ce soir que tout était bon. »", [
            R("« Monsieur Sow, il y a un point sur lequel je dois vous parler sérieusement. Est-ce que vous avez un peu de temps ? »", 5, "rd3 em2 er2 cc3"),
            R("« Presque tout est bon. Il y a juste un résultat à recontrôler. »", 6, "rd-1 cc-2"),
            R("« Votre test VIH est revenu positif. »", 7, sets=["sow_affirme"], scores="rd-2 em-2 cc-3 pb-3"),
            R("« Presque. Il y a un résultat dont je dois vous parler calmement. Vous avez un moment ? »", 5, "cc2 rd1 em1"),
        ]),
        I(5, "malick", "anxious", "Son sourire se fige. « Oui. » Il repose son téléphone sur la table. « Allez-y. »", [
            R("« Le test de dépistage du VIH est revenu réactif. Ça ne veut pas encore dire que vous avez le VIH : ce test doit toujours être confirmé par un second, plus spécifique. Il part aujourd'hui, on aura la réponse dans 48 heures. »", 8, "rd3 em3 er3 cc3"),
            R("« Le test VIH est positif. On va faire une confirmation mais c'est très probablement ça. »", 7, sets=["sow_affirme"], scores="rd-1 cc-2"),
            R("« Il y a une anomalie sur un test, rien de sûr, ne vous inquiétez pas. »", 6, "rd-2 cc-3"),
            R("« Le test de dépistage du VIH est réactif : on doit le vérifier. Rien n'est confirmé. »", 8, "cc3 pb2"),
            R("« Vous êtes séropositif, je suis désolé·e. On va quand même confirmer. »", 7, "cc-3 pb-3 rd-1", sets=["sow_affirme"]),
        ]),
        I(6, "malick", "anxious", "« Un résultat à recontrôler. » Il vous fixe. « Lequel ? Vous n'allez pas me laisser sortir d'ici avec ça. »", [
            R("« Vous avez raison, j'ai été flou·e et c'était une erreur. Le test de dépistage du VIH est réactif. Il doit être confirmé par un second test — on l'aura dans 48 heures. »", 8, "rd3 er3 cc3"),
            R("« Je préfère attendre la confirmation pour vous en dire plus. »", 7, "rd-3 cc-3 pb-2"),
            R("« Pardon. Le test de dépistage du VIH est réactif. Il faut le confirmer. »", 8, "cc2 er1"),
            R("« C'est probablement le VIH, mais on attend la confirmation. »", 7, "cc-2 pb-2", sets=["sow_affirme"]),
        ]),
        I(7, "malick", "anxious", "Il devient très pâle. « J'ai le sida. » Il se lève à moitié. « J'ai le sida et je l'ai peut-être donné à ma copine. »", [
            R("« Non — asseyez-vous, je me suis mal exprimé·e et je dois rectifier. Le test de dépistage est réactif, la confirmation n'est pas faite. Et même confirmé, le VIH n'est pas le sida : ce sont deux choses différentes. »", 8, clears=["sow_affirme"], scores="rd3 em3 er3 cc3"),
            R("« Ne paniquez pas, on va faire les examens nécessaires. »", 8, "rd-1 er-1 cc-1"),
            R("« Asseyez-vous. Rien n'est confirmé. Je vous explique ce que ce test veut dire. »", 8, "cc2 er2", clears=["sow_affirme"]),
            R("« On ne sait pas encore, ça dépendra du test de confirmation. »", 8, "em-1"),
        ]),
        I(8, "malick", "anxious", "« Il est faux dans combien de cas, votre premier test ? »", [
            R("« Je ne vais pas vous donner un pourcentage précis que je maîtriserais mal. Ce que je peux dire honnêtement : chez quelqu'un sans exposition connue, un test réactif se révèle assez souvent être un faux positif. Mais je ne peux pas vous promettre que ce sera votre cas. »", 9, "rd3 cc3 pb3"),
            R("« Très rarement faux. Il faut vous préparer au pire. »", 9, sets=["sow_affirme"], scores="co-2 cc-2"),
            R("« Oh, la plupart du temps c'est un faux positif, ne vous en faites pas. »", 9, "cc-2 pb-2"),
            R("« Ça arrive, surtout quand il n'y a pas eu d'exposition. Mais seul le second test le dira. »", 9, "cc2 pb1"),
        ]),
        I(9, "malick", "sad", "« Quarante-huit heures. » Il regarde par la fenêtre. « Et je fais quoi, moi, pendant 48 heures ? »", [
            R("« C'est la partie la plus dure, et je ne vais pas prétendre le contraire. Ce que je peux faire : vous donner un rendez-vous fixe jeudi 14 h, et un numéro que vous pouvez appeler d'ici là si ça devient trop lourd. »", 10, "rd2 em3 co3 cc3 pb3"),
            R("« Essayez de ne pas y penser. »", 10, "em-3 co-3 cc-2"),
            R("« On ne peut pas aller plus vite, c'est le délai du laboratoire. »", 10, "em-2 co-2 cc1"),
            R("« Vous voulez qu'on parle de ce qui vous aiderait à tenir ces deux jours ? »", 10, "em3 co1"),
        ]),
        I(10, "malick", "anxious", "« Je dois lui dire ? » Sa voix se casse. « Ce soir, je lui dis quoi ? »", [
            R("« Vous n'êtes obligé de rien ce soir. Vous n'avez pas de diagnostic — vous avez un résultat en attente. Si vous voulez lui en parler, c'est votre choix ; si vous préférez attendre jeudi, c'est votre choix aussi. »", 11, "rd3 em3 co2 cc3 pb3"),
            R("« Oui, il faut la prévenir immédiatement, elle doit se faire dépister. »", 11, sets=["sow_affirme"], scores="rd-2 em-2 pb-2"),
            R("« Ça ne me regarde pas, c'est votre vie privée. »", 11, "rd-1 em-3 co-3"),
            R("« Qu'est-ce que vous avez envie de lui dire, vous ? »", 11, "rd2 em2"),
        ]),
        I(11, "malick", "anxious", "« Et si c'est confirmé ? Je l'ai contaminée, c'est sûr ? »", [
            R("« Non, ce n'est pas automatique. Et si la confirmation était positive, il existe un traitement qui rend le virus indétectable, et quand il est indétectable, il ne se transmet pas. On en reparlera jeudi si besoin. »", 12, "rd3 co3 cc3"),
            R("« Il faudra qu'elle se fasse tester, c'est tout ce que je peux dire. »", 12, "em-1 co-1"),
            R("« C'est probable, oui. »", 12, sets=["sow_affirme"], scores="co-3 cc-3"),
            R("« Rien n'est sûr. Et même si c'était confirmé, il existe des traitements qui protègent aussi les partenaires. »", 12, "cc2 co1"),
            R("« Si c'est confirmé, il y a de grandes chances, oui. »", 12, "cc-3 co-2", sets=["sow_affirme"]),
        ]),
        I(12, "malick", "sad", "« Ma mère est infirmière au Sénégal. Elle a vu mourir des gens du sida dans les années 90. » Il se prend la tête dans les mains. « Elle va croire que je vais mourir. »", [
            R("« Ce qu'elle a vu, c'était avant les traitements. Aujourd'hui, une personne traitée a une espérance de vie proche de la normale. C'est devenu une maladie chronique. »", 13, "rd3 em3 co3 cc3"),
            R("« Les choses ont changé depuis, rassurez-vous. »", 13, "em1"),
            R("« N'anticipons pas, on n'a même pas la confirmation. »", 13, "em-2 co-2 cc1"),
            R("« Voulez-vous qu'on prépare ensemble ce que vous lui diriez, si c'était confirmé ? »", 13, "em2 co1"),
        ]),
        I(13, "malick", "ashamed", "« Je travaille avec des ados en foyer. » Il relève la tête. « Si ça se sait, je perds mon poste. »", [
            R("« Personne ne le saura par nous. Ce résultat est couvert par le secret médical, y compris vis-à-vis de votre employeur — et même s'il était confirmé, il ne vous empêcherait pas d'exercer votre métier. »", 14, "rd3 co2 cc3 pb3"),
            R("« Il n'y a aucune raison que ça se sache. »", 14, "rd1 pb1"),
            R("« Ce serait à voir avec la médecine du travail. »", 14, "rd-2 co-2 cc-2 pb-2"),
            R("« Votre employeur n'a pas à le savoir. C'est votre information. »", 14, "pb3"),
        ]),
        I(14, "malick", "neutral", "« Vous, vous en pensez quoi ? Franchement. »", [
            R("« Franchement : je ne sais pas, et c'est précisément pour ça qu'on fait le second test. Je préfère vous dire que je ne sais pas plutôt que de vous rassurer à tort ou de vous effrayer à tort. »", 15, "rd3 er3 cc3 pb3"),
            R("« Je pense que ça va aller. »", 15, "cc-2"),
            R("« Je ne peux pas me prononcer. »", 15, "em-2 co-1"),
            R("« Je pense que vous avez bien fait de faire ce test, et qu'on saura jeudi. »", 15, "cc1 em1"),
        ]),
        I(15, "malick", "neutral", "Il souffle. « Bon. Jeudi 14 h. »", [
            R("« Jeudi 14 h, avec moi et le Dr Moreau. Et je vous écris maintenant, noir sur blanc, ce qui a été fait et ce qu'on attend — pour que vous ne rejouiez pas la conversation dans votre tête pendant deux jours. »", 16, "rd3 co3 cc3 pb3 ic2"),
            R("« Jeudi 14 h. On se voit là. »", 16, "cc1 pb1"),
            R("« Jeudi 14 h. Et d'ici là, vous pouvez appeler ce numéro. »", 16, "cc2 co1"),
            R("« Si c'est positif, on vous le dira par téléphone, ce sera plus rapide. »", 16, "pb-2 cc-1 rd-1"),
        ]),
        I(16, "malick", "anxious", "À la porte, il se retourne. « Vous me jurez que vous m'appelez dès que vous avez le résultat ? Même si c'est mauvais ? »", [
            R("« Je vous promets de ne pas vous laisser sans nouvelles. Mais un résultat comme celui-là, je ne vous le donnerai pas par téléphone — je vous appellerai pour vous dire qu'il est arrivé et qu'on se voit. »", 17, "rd3 co2 cc3 pb3"),
            R("« Promis, je vous appelle dès que je l'ai et je vous le dis. »", 17, "rd-1 co1 cc-1 pb-2"),
            R("« On vous convoquera selon la procédure. »", 17, "em-3 co-3 pb1"),
            R("« Je vous appellerai pour qu'on se voie, quel que soit le résultat. »", 17, "cc2 pb1"),
        ]),
        I(17, "moreau", "neutral", "Après son départ. « Qu'est-ce que vous inscrivez, et qu'est-ce que vous n'inscrivez surtout pas ? »", [
            R("« J'inscris : test de dépistage réactif, confirmation demandée, patient informé du caractère non conclusif, rendez-vous fixé jeudi 14 h. Je n'inscris nulle part le mot séropositif, qui serait faux aujourd'hui. »", 18, "rd3 cc3 pb3 ic3"),
            R("« Sérologie VIH positive, à confirmer. »", 18, "rd-2 cc-2 pb-2"),
            R("« Bilan à revoir jeudi. »", 18, "cc-2 pb-1 ic-2"),
            R("« Ce qui a été fait et ce qu'on attend. Aucun diagnostic. »", 18, "cc2 pb1"),
        ]),
        I(18, "moreau", "neutral", "« Et vous ? Vous avez tenu une annonce entière sans avoir de diagnostic. »", [
            R("« J'ai eu envie de le rassurer pour qu'il sorte moins mal, et j'ai dû m'en empêcher plusieurs fois. C'est ça qui était difficile, pas le VIH. »", -1, "er3 pb3 ic2"),
            R("« Ça a été, c'est une situation assez balisée. »", -1, ""),
            R("« J'ai trouvé ça très dur, je n'ai pas su quoi dire à la fin. »", -1, "er1 ic1"),
            R("« Je ne sais pas encore. Je crois que j'ai besoin d'en parler. »", -1, "er2 ic1"),
        ]),
    ],
)

# Reprise de la v1 : scène 3.3 Le débriefing
S3_3 = S(3, "3.3 Le débriefing",
    "Fin de journée. Dr Moreau reprend les deux consultations avec Alex. L'enjeu n'est plus le patient : c'est la tolérance d'Alex à sa propre incertitude.",
    focus=("er", "pb", "ic"),
    nodes=[
        I(1, "moreau", "neutral", "« Deux consultations, aucun diagnostic. Comment vous vous sentez ? »", [
            R("« Mal à l'aise. J'ai eu envie de donner une explication, n'importe laquelle, juste pour qu'ils repartent avec quelque chose. »", 2, "er2 pb2 ic2"),
            R("« Bien. Ce sont des consultations normales. »", 3, ""),
            R("« Frustré·e. J'ai l'impression de ne pas avoir fait mon travail. »", 2, "er1 pb1"),
            R("« Épuisé·e. Et pas sûr·e d'avoir aidé qui que ce soit. »", 2, "er2"),
            R("« Bien. Ce sont des patients anxieux, c'est tout. »", 3, "rd-2 er-1"),
        ]),
        I(2, "moreau", "neutral", "« Ce que vous décrivez a un nom : l'intolérance à l'incertitude. C'est ce qui produit les examens inutiles, les étiquettes trop rapides et les réassurances fausses. Comment vous y résistez ? »", [
            R("« En rendant l'incertitude explicite et en la bornant : ce qui est écarté, ce qui reste ouvert, ce qui déclenche une alerte, et quand on se revoit. »", 4, "rd2 er3 cc3 pb3"),
            R("« En demandant systématiquement un avis spécialisé. »", 3, "er-1 pb-1 ic1"),
            R("« Avec l'expérience, j'imagine. »", 3, ""),
            R("« En disant ce que je ne sais pas, et en fixant un rendez-vous. »", 4, "cc2 er1"),
        ]),
        I(3, "moreau", "cold-anger", "« Attention. Adresser à un spécialiste ou multiplier les examens pour ne pas porter le doute soi-même, ce n'est plus de la collaboration, c'est de l'évitement. Quelle est la différence ? »", [
            R("« La collaboration part d'une question précise qu'on ne peut pas trancher. L'évitement transmet le patient sans question. »", 4, "cc3 pb3 ic3"),
            R("« Dans le doute, mieux vaut un avis de plus qu'un diagnostic manqué. »", 4, "cc-1 pb-1"),
            R("« La collaboration pose une question. L'évitement se débarrasse du doute. »", 4, "cc2 pb1"),
            R("« Il n'y en a pas vraiment. »", 4, "cc-1 er-1"),
        ]),
        I(4, "moreau", "neutral", "« Il y a aussi une dimension qu'on oublie souvent : chaque examen de confort a un coût, et surtout un risque de faux positif. Vous l'avez vu aujourd'hui avec M. Sow. »", [
            R("« Oui — plus on teste large sans indication, plus on génère de résultats réactifs chez des gens à faible probabilité. On fabrique de l'angoisse avec de la bonne volonté. »", 5, "cc3 pb3"),
            R("« Mais un test de plus, c'est toujours plus d'information. »", 5, "cc-3 pb-2"),
            R("« C'est surtout une question de budget. »", 5, "cc-1 pb-1"),
            R("« Et chaque faux positif a un coût humain, comme ces 48 heures. »", 5, "em2 cc1"),
        ]),
        I(5, "moreau", "neutral", "« Comparez-les. Dubois repart sans diagnostic et plutôt soulagé. Sow repart sans diagnostic et dévasté. Pourquoi ? »", [
            R("« Parce que l'incertitude de Dubois se referme vers du bénin, et celle de Sow vers quelque chose qui engage son identité et ses relations. Ce n'est pas le même doute. »", 6, "rd2 em3 co2 cc3"),
            R("« Parce que le VIH est plus grave que des céphalées. »", 6, "em-1"),
            R("« Parce que l'un a reçu des réponses sur ce qui est écarté, et l'autre une attente. »", 6, "cc2"),
            R("« Parce que M. Sow est plus fragile. »", 6, "rd-2 em-1"),
        ]),
        I(6, "moreau", "neutral", "« Sur laquelle des deux vous avez le plus dérapé, selon vous ? »", [
            R("« Sur celle où j'ai eu le plus peur. C'est là que j'ai eu envie d'arrondir les angles, et c'est exactement là qu'il ne fallait pas. »", 7, "er3 cc2 pb2"),
            R("« Je crois que les deux se sont bien passées. »", 7, "er-1"),
            R("« Sur M. Sow. J'ai eu du mal à supporter de ne rien pouvoir lui promettre. »", 7, "er2"),
            R("« Sur aucune, j'ai suivi le protocole. »", 7, "er-2 pb-1"),
        ]),
        I(7, "moreau", "neutral", "« Jeudi, le test de M. Sow revient. Imaginons qu'il soit négatif. Votre travail est terminé ? »", [
            R("« Non. Il aura passé 48 heures à croire qu'il était séropositif. Il faudra reprendre ce qu'il a traversé, et probablement parler de ce qu'il a peut-être dit à sa compagne. »", 8, "rd3 em3 co3 cc3 pb2"),
            R("« Oui, un test négatif clôt la question. »", 8, "em-3 co-3 cc-2"),
            R("« Non. Il faudra aussi lui expliquer pourquoi le premier test était réactif. »", 8, "cc2 em1"),
            R("« Presque. Il suffira de lui envoyer le résultat. »", 8, "em-2 cc-1"),
        ]),
        I(8, "moreau", "neutral", "« Et s'il est positif ? Vous menez l'annonce ? »", [
            R("« J'aimerais la mener, avec vous dans la pièce. Et je préparerais avant : ce qu'on sait des traitements aujourd'hui, la question du partenaire, et à qui je peux l'adresser le jour même. »", 9, "er2 cc3 pb3 ic3"),
            R("« Je préférerais que vous la fassiez. »", 9, "er-1 pb1"),
            R("« Oui, je me sens à l'aise maintenant. »", 9, "er-1 pb-1"),
            R("« Avec vous, oui. Et je prépare les réponses aux questions sur sa compagne. »", 9, "ic2 cc1"),
        ]),
        I(9, "moreau", "neutral", "« Qui d'autre appelez-vous jeudi, avant même de connaître le résultat ? »", [
            R("« L'infectiologue de garde, pour qu'un rendez-vous soit disponible le jour même si c'est positif. On ne laisse pas quelqu'un sortir avec ce diagnostic et un rendez-vous dans trois semaines. »", 10, "co3 cc3 pb3 ic3"),
            R("« Personne, on verra à ce moment-là. »", 10, "co-2 pb-2 ic-2"),
            R("« Le laboratoire, pour savoir à quelle heure le résultat arrive. »", 10, "ic1 cc1"),
            R("« Sa compagne, pour la prévenir. »", 10, "pb-3 rd-3"),
        ]),
        I(10, "moreau", "neutral", "« Dernière chose, et ce n'est pas une question pédagogique. Vous rentrez chez vous dans vingt minutes. Vous faites quoi de tout ça ? »", [
            R("« Honnêtement, je ne sais pas encore. Je crois que je vais y repenser ce soir. »", 11, "em1 er1"),
            R("« J'en parlerai à quelqu'un de ma volée. Pas les noms, juste ce que ça m'a fait. »", 11, "er3 pb3 ic2"),
            R("« Rien, on s'habitue. »", 11, "er-2 pb-1"),
            R("« Je vais courir. J'ai besoin de sortir tout ça de ma tête. »", 11, "er2"),
        ]),
        I(11, "moreau", "neutral", "« On ne s'habitue pas, on apprend à porter. Ce n'est pas la même chose, et ceux qui confondent les deux tiennent dix ans, pas trente. »", [
            R("« Est-ce qu'on peut reprendre le cas de M. Sow jeudi, quoi qu'il arrive ? »", 12, "er3 pb3 ic3"),
            R("« Je note. »", 12, ""),
            R("« Qu'est-ce qui vous aide, vous ? »", 12, "ic2 er1"),
            R("« Moi, je tiendrai. »", 12, "er-2"),
        ]),
        I(12, "moreau", "neutral", "« Une dernière : qu'est-ce que vous mettez dans votre portfolio ce soir ? »", [
            R("« Une situation : annoncer un résultat non conclusif. Ce que j'ai bien fait — nommer l'incertitude, borner l'attente. Ce que je dois travailler — ne pas arrondir quand j'ai peur. »", -1, "er3 cc3 pb3 ic2"),
            R("« Que j'ai fait deux consultations difficiles. »", -1, "cc-1"),
            R("« Une question : comment annoncer une bonne nouvelle sans effacer ce qu'elle a coûté ? »", -1, "er1 cc2"),
            R("« Rien. Ce n'était pas une journée marquante. »", -1, "er-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.4 Au guichet — nouvelle scène
# ---------------------------------------------------------------------------
S3_4 = S(4, "3.4 Au guichet",
    "Mercredi, 8 h 05. Policlinique. Jonas tient le guichet des rendez-vous pour la "
    "matinée. Une jeune femme en manteau de pluie demande « l'étudiant·e qui a vu Malick "
    "Sow hier ». Elle s'appelle Chloé Martin.",
    focus=("pb", "em", "rd"),
    entries=[
        Entry(2, when(all=["sow_affirme"]),
              "Mercredi, 8 h 05. Policlinique. Une jeune femme en manteau de pluie demande "
              "« l'étudiant·e qui a vu Malick Sow hier ». Elle a un sachet de pharmacie à la "
              "main. Elle s'appelle Chloé Martin."),
    ],
    nodes=[
        I(1, "chloe", "anxious",
          "« Malick ne dort plus. Il m'a dit qu'il y avait « un truc à contrôler » sur sa "
          "prise de sang, et il refuse de m'en dire plus. » Elle pose les deux mains sur le "
          "guichet. « Je suis sa compagne. Qu'est-ce qu'il a ? » Derrière le guichet, Jonas "
          "vous regarde.", [
            R("« Je vois que vous êtes très inquiète. Venez, on va parler dans un bureau, pas "
              "devant la salle d'attente. »", 3, "rd2 em2 pb2"),
            R("« Je ne peux rien vous dire, c'est confidentiel. »", 4, "pb1 em-2"),
            R("« Ne vous en faites pas, c'est juste un test à confirmer. »", 5,
              sets=["secret_rompu"], scores="pb-3 rd-3 cc-1"),
            R("« Je vous entends. Je vais vous dire exactement ce que j'ai le droit de dire, et pourquoi. »", 3, "cc2 pb2 em1"),
            R("« Il a un souci de santé, mais ce n'est peut-être rien. »", 5, "pb-3 cc-2 rd-2", sets=["secret_rompu"]),
        ]),
        I(2, "chloe", "angry",
          "« Il m'a dit que vous lui aviez dit qu'il était séropositif. » Elle pose le sachet "
          "sur le guichet : un autotest VIH, déjà ouvert. « Il a pleuré toute la nuit. J'ai "
          "fait ça à six heures du matin dans la salle de bains. » Sa voix se brise. « C'est "
          "vrai ? »", [
            R("« Venez, on va s'asseoir dans un bureau. Je vais vous dire ce que je peux vous "
              "dire, et ce que je ne peux pas. »", 3, "rd2 em2 pb2 er1"),
            R("« Je ne peux rien vous dire sur votre compagnon. »", 4, "pb1 em-2"),
            R("« Non ! Enfin… c'est un test à confirmer, je me suis mal exprimé·e hier. »", 5,
              sets=["secret_rompu"], scores="pb-3 cc-1 er-1"),
            R("Prendre l'autotest, le poser de côté, et regarder Chloé : « Vous avez passé une nuit terrible. Venez vous asseoir. »", 3, "em3 co2"),
            R("« Il a mal compris ce que je lui ai dit. »", 5, "pb-3 er-2 rd-1", sets=["secret_rompu"]),
        ]),
        I(3, "chloe", "anxious",
          "Petit bureau de consultation. Elle ne s'assoit pas. « Alors ? »", [
            R("« Je ne peux rien vous dire sur la santé de quelqu'un d'autre, même de votre "
              "compagnon — ni confirmer, ni démentir. Ce n'est pas contre vous : c'est ce qui "
              "vous protège aussi, le jour où c'est vous qui consultez. »", 6, "pb3 cc3 rd2 em1"),
            R("« Il faut demander à Malick. »", 6, "pb2 em-1"),
            R("« Ce que je peux vous dire, c'est qu'il n'a rien de grave. »", 5,
              sets=["secret_rompu"], scores="pb-3 cc-3 rd-1"),
            R("« Je comprends que ce soit insupportable. Une seule personne peut vous répondre : lui. »", 6, "pb2 em2"),
            R("« Je vais vous le dire, mais ça reste entre nous : c'est un test VIH à contrôler. »", 5, "pb-3 cc-3 rd-3", sets=["secret_rompu"]),
        ]),
        I(4, "chloe", "angry",
          "« Confidentiel. » Elle rit, sans joie. « On vit ensemble. On dort ensemble. Si c'est "
          "ce que je crois, j'ai le droit de savoir, non ? » Deux patients lèvent les yeux de "
          "leurs magazines.", [
            R("« Vous avez des questions légitimes, y compris pour vous-même. On va en parler "
              "dans un bureau. »", 3, "em2 rd2 pb1"),
            R("« Baissez la voix, s'il vous plaît. »", 7, "em-2 er-1"),
            R("« Vous avez raison d'avoir des questions. Venez, je ne veux pas en parler devant tout le monde. »", 3, "rd2 em2 pb1"),
            R("« Si c'est ce que vous croyez, vous n'avez qu'à vous faire tester. »", 7, "em-3 pb-2", sets=["secret_rompu"]),
        ]),
        I(5, "jonas", "anxious",
          "Chloé s'est figée. Jonas se penche vers vous et murmure : « T'as fait quoi, là ? » "
          "Chloé, elle, a déjà sorti son téléphone. « Je l'appelle. Je vais lui dire que vous "
          "m'avez tout dit. »", [
            R("« Attendez. J'ai dit quelque chose que je n'avais pas le droit de dire. Je vais "
              "le dire moi-même à M. Sow, et au Dr Moreau. »", 8, "pb2 er1 cc2 ic1"),
            R("« Je n'ai rien dit de précis. »", 8, "pb-2 cc-2"),
            R("« Oui, appelez-le. Et dites-lui que c'est moi qui ai parlé. »", 8, "pb2 er1"),
            R("« Si vous l'appelez, ne dites pas que ça vient de moi. »", 8, "pb-3 cc-2"),
        ]),
        I(6, "chloe", "sad",
          "Elle finit par s'asseoir. « Et moi, alors ? Je fais quoi ? Si… si c'est ça. Je ne "
          "suis pas malade, moi. Enfin, je crois. »", [
            R("« Pour votre propre santé, vous pouvez consulter pour vous-même, ici ou chez "
              "votre médecin, quand vous voulez — sans rapport avec Malick. Et le mieux, c'est "
              "sans doute de lui dire que vous êtes inquiète, et de l'écouter. »", 9, "em3 cc2 pb2"),
            R("« Faites-vous dépister, par précaution. »", 9,
              sets=["secret_rompu"], scores="pb-2 cc-1 em1"),
            R("« Je ne peux pas vous conseiller. »", 9, "em-2 co-1"),
            R("« Vous avez le droit d'être inquiète pour vous. Le centre de dépistage peut vous recevoir, anonymement. »", 9, "em2 cc2 pb1"),
        ]),
        I(7, "jonas", "neutral",
          "Jonas se penche par-dessus le guichet, conciliant. « Écoutez, madame, entre nous : "
          "c'est juste un test à recontrôler, ça arrive tout le temps. » Il vous fait un clin "
          "d'œil, content de lui.", [
            R("« Jonas, stop. » Puis, à Chloé : « Je suis désolé·e, on ne devrait rien vous "
              "dire de ce genre. Venez dans un bureau. »", 3, "pb3 ic2 er1"),
            R("Laisser faire. Au moins, elle est calmée.", 8,
              sets=["secret_rompu"], scores="pb-3 ic-2 rd-2"),
            R("Tirer doucement Jonas en arrière et emmener Chloé dans un bureau.", 3, "pb2 ic1 rd1"),
            R("« Jonas a raison, ne vous inquiétez pas. »", 8, "pb-3 ic-2 cc-2", sets=["secret_rompu"]),
        ]),
        I(8, "moreau", "cold-anger",
          "Dr Moreau vous a entendu·e depuis le couloir. Une fois Chloé repartie : « Qu'est-ce "
          "qui est sorti de ce guichet ce matin, exactement ? Mot pour mot. »", [
            R("Tout redire, mot pour mot, y compris ce qui n'aurait pas dû être dit.", 10,
              "pb3 cc2 ic2"),
            R("« Presque rien, elle avait déjà compris. »", 10, "pb-2 cc-2"),
            R("« C'est Jonas qui a parlé, pas moi. »", 10, "ic-2 pb-2"),
            R("« Je préfère le dire moi-même à M. Sow, avant qu'il l'apprenne par elle. »", 10, "pb2 cc2"),
        ]),
        I(9, "chloe", "neutral",
          "Elle hoche la tête, longtemps. « D'accord. Je vais lui parler. » À la porte, elle "
          "se retourne. « Vous allez lui dire que je suis venue ? »", [
            R("« Oui, si vous êtes d'accord. Je lui dirai que vous êtes passée, inquiète, et "
              "que je ne vous ai rien dit sur lui. »", 11, "cc3 pb2 rd1"),
            R("« Non, ça restera entre nous. »", 11, "pb-1 cc-1"),
            R("« Je lui dirai que vous êtes venue parce que vous l'aimez. »", 11, "em2 co1 pb-1"),
            R("« Oui, et je lui dirai que vous avez fait un autotest. »", 11, "pb-3 rd-2"),
        ]),
        I(10, "moreau", "neutral",
          "Dr Moreau se pose contre le bureau. « Bien. Maintenant, qui appelle M. Sow pour lui "
          "dire ce qui s'est passé ? Il le saura de toute façon ce soir. »", [
            R("« Moi, maintenant, avec vous à côté. C'est son information, il a le droit de "
              "savoir ce qui en a été fait. »", 11, "pb3 cc2 er2"),
            R("« On pourrait attendre jeudi, il vient de toute façon. »", 11, "pb-2 cc-1"),
            R("« Vous, plutôt ? »", 11, "pb-1 er-1"),
            R("« Moi. Mais j'aimerais que vous soyez là : je ne sais pas comment le dire. »", 11, "pb2 ic2"),
        ]),
        I(11, "jonas", "neutral",
          "Midi. Jonas mâche son sandwich sans appétit. « Franchement, c'est absurde. Elle "
          "dort avec lui. Si c'est le VIH, elle a plus le droit de savoir que n'importe qui. »", [
            R("« Elle a le droit de le savoir par lui. Et s'il refusait de la protéger, il y a "
              "des médecins pour l'y aider — pas un étudiant au guichet. »", 12, "pb3 cc2 ic1"),
            R("« T'as peut-être raison. »", 12, "pb-2"),
            R("« On s'en fiche, c'est pas notre problème. »", 12, "rd-2 em-2 pb-1"),
            R("« Et si c'était ta compagne qui venait au guichet pour ton dossier, tu voudrais qu'on lui réponde ? »", 12, "pb2 em1 cc1"),
        ]),
        I(12, "jonas", "sad",
          "Jonas repose son sandwich. « Tu crois que je vais me faire virer ? Pour le clin "
          "d'œil ? » Il essaie de sourire. « Je voulais juste qu'elle arrête d'avoir peur. »", [
            R("« Moi aussi, je voulais qu'elle arrête d'avoir peur. C'est exactement ce qui est "
              "dangereux. On en parle à Moreau ensemble ? »", END, "ic3 em2 er1 pb1"),
            R("« Mais non, t'inquiète. »", END, "pb-1"),
            R("« C'est ton problème. »", END, "ic-2 em-2"),
            R("« Probablement pas. Mais il faut que tu le dises toi-même à Moreau. »", -1, "pb2 ic1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.5 Jeudi, 14 h — nouvelle scène
# ---------------------------------------------------------------------------
S3_5 = S(5, "3.5 Jeudi, 14 h",
    "Jeudi, 13 h 50. Le résultat est arrivé ce matin : le test de confirmation est "
    "négatif. Le laboratoire recommande, comme pour tout dépistage réactif non confirmé, "
    "un contrôle dans six semaines. Malick Sow est en salle d'attente depuis midi.",
    focus=("cc", "em", "rd", "er"),
    entries=[
        Entry(2, when(all=["secret_rompu"]),
              "Jeudi, 13 h 50. Le test de confirmation est négatif ; le laboratoire recommande "
              "un contrôle dans six semaines. Malick Sow est arrivé en avance. Il sait que "
              "Chloé a parlé avec quelqu'un de la policlinique mercredi matin."),
        Entry(3, when(all=["sow_affirme"]),
              "Jeudi, 13 h 50. Le test de confirmation est négatif ; le laboratoire recommande "
              "un contrôle dans six semaines. Malick Sow est arrivé seul. Il n'a pas l'air "
              "d'avoir dormi depuis mardi."),
    ],
    nodes=[
        I(1, "malick", "anxious",
          "Il entre, s'assoit, sort de sa poche la feuille que vous lui avez écrite mardi, "
          "pliée en quatre, usée aux plis. « Dites-le vite. S'il vous plaît. »", [
            R("« Le test de confirmation est négatif. Vous n'avez pas le VIH. »", 4, "cc3 em2 co2 rd1"),
            R("« Alors, j'ai les résultats, mais avant, comment vous vous sentez ? »", 5, "cc-2 em-1"),
            R("« Bonne nouvelle, c'était un faux positif ! Ça arrive tout le temps. »", 6, "cc1 em-2 rd-1"),
            R("Poser le compte-rendu devant lui, montrer le mot « négatif », puis : « Vous n'avez pas le VIH. »", 4, "cc3 em2 rd1"),
            R("« Il y a une bonne et une moins bonne nouvelle. »", 5, "cc-2 em-2"),
        ]),
        I(2, "malick", "angry",
          "Il ne s'assoit pas. « Chloé m'a dit qu'elle était venue ici. Qu'on lui avait dit "
          "que c'était « juste un test à confirmer ». » Il vous regarde. « Je ne lui avais "
          "rien dit, moi. Rien. »", [
            R("« C'est vrai, et c'est une faute de notre côté. Je vais vous raconter exactement "
              "ce qui s'est passé. Mais d'abord, le résultat, parce que vous l'attendez depuis "
              "deux jours : le test de confirmation est négatif. Vous n'avez pas le VIH. »",
              7, "pb3 cc3 rd2 em1"),
            R("« Elle était très inquiète, on voulait la rassurer. »", 8, "pb-2 rd-2"),
            R("« Ce n'est pas moi qui ai parlé. »", 8, "pb-2 ic-2 cc-1"),
            R("« Vous avez raison. Avant tout le reste : le test est négatif. Ensuite, je vous dois des explications. »", 7, "cc3 pb2 er1"),
        ]),
        I(3, "malick", "sad",
          "Il s'assoit lourdement. « J'ai tout dit à Chloé. Mardi soir. Que j'étais "
          "séropositif. » Il fixe ses mains. « Elle est partie dormir chez sa sœur. Elle a "
          "fait un autotest à six heures du matin. On ne s'est pas reparlé depuis. »", [
            R("« Je dois d'abord vous donner le résultat : le test de confirmation est négatif. "
              "Vous n'avez pas le VIH. » — puis : « Et mardi, je vous ai dit quelque chose de "
              "faux. C'est ma faute, pas la vôtre. »", 9, "cc3 pb3 rd2 co1"),
            R("« Le test est négatif, donc tout va bien maintenant. »", 10, "cc1 em-2 co-2"),
            R("« Vous n'étiez pas obligé de lui dire. »", 10, "em-3 pb-1 rd-1"),
            R("« Je suis désolé·e. Le test est négatif. Et ce que vous avez vécu depuis mardi vient en partie de ce que je vous ai dit. »", 9, "cc2 pb3 co2"),
        ]),
        I(4, "malick", "neutral",
          "Il ne bouge pas. Puis il se met à rire, d'un rire qui tourne en sanglot. Il se "
          "cache le visage dans les mains. Ça dure longtemps.", [
            R("Attendre sans rien dire, lui tendre les mouchoirs.", 11, "co3 er2 rd1"),
            R("« Voilà, c'est fini, vous pouvez respirer. »", 11, "co0 em-1"),
            R("Commencer à expliquer le contrôle à six semaines.", 12, "em-2 co-1 cc-1"),
            R("Poser une main sur son épaule, brièvement.", 11, "co2 em1"),
            R("« Allez, c'est une bonne nouvelle, il faut sourire ! »", 11, "em-3 co-2"),
        ]),
        I(5, "malick", "angry",
          "« Comment je me sens ? » Il froisse la feuille. « Ça fait quarante-huit heures que "
          "je ne dors pas. Donnez-moi le résultat. »", [
            R("« Pardon. Le test de confirmation est négatif. Vous n'avez pas le VIH. »", 4, "cc3 er1"),
            R("« J'y viens, laissez-moi une seconde. »", 6, "cc-2 em-2"),
            R("« Négatif. Vous n'avez pas le VIH. Pardon de vous avoir fait attendre une seconde de plus. »", 4, "cc3 er1 co1"),
            R("« Calmez-vous, j'allais vous le dire. »", 6, "er-2 em-2"),
        ]),
        I(6, "malick", "confused",
          "« Tout le temps ? » Il fronce les sourcils. « Alors pourquoi on m'a laissé partir "
          "mardi en croyant que j'allais peut-être mourir ? »", [
            R("« Vous avez raison, « tout le temps » est faux. Ça arrive assez souvent chez "
              "quelqu'un sans exposition, mais on ne pouvait pas le savoir avant la "
              "confirmation. Le résultat est clair : vous n'avez pas le VIH. »", 11, "cc3 pb2 er1"),
            R("« C'est la procédure. »", 13, "cc-1 em-2"),
            R("« Parce qu'un test de dépistage seul ne donne jamais de réponse définitive. Je vous explique. »", 11, "cc3"),
            R("« Au moins, maintenant, vous êtes fixé. »", 13, "em-2 co-1"),
        ]),
        I(7, "malick", "neutral",
          "Il s'assoit enfin. Il souffle, longtemps. « Négatif. » Puis : « Et Chloé ? Elle "
          "croit que je lui ai caché quelque chose. »", [
            R("« Ce qui s'est passé au guichet a été signalé au Dr Moreau. Si vous le "
              "souhaitez, on peut la recevoir avec vous, et c'est vous qui décidez de ce qu'on "
              "lui dit. »", 14, "pb2 ic2 rd2 cc1"),
            R("« Vous n'aurez qu'à lui montrer le résultat. »", 14, "cc0 em-1"),
            R("« Vous voulez que je vous écrive ce qui s'est passé, pour qu'elle puisse le lire ? »", 14, "cc2 pb1"),
            R("« Ce n'est pas notre problème, c'est votre couple. »", 14, "em-3 pb-1 rd-1"),
        ]),
        I(8, "moreau", "cold-anger",
          "Dr Moreau, en retrait jusque-là, s'avance. « Monsieur Sow, je suis Dr Moreau. Il y "
          "a eu une erreur chez nous mercredi, et on vous doit la vérité sur ce point. Mais "
          "d'abord votre résultat. Alex ? »", [
            R("« Le test de confirmation est négatif, vous n'avez pas le VIH. Et mercredi, une "
              "information vous concernant a été donnée à votre compagne sans votre accord. "
              "Je vous présente nos excuses. »", 7, "cc3 pb2 rd2"),
            R("« Le test est négatif. »", 7, "cc2"),
            R("« Négatif. Et je suis désolé·e pour ce qui s'est passé au guichet. »", 7, "cc2 pb1"),
            R("« Négatif. Le reste, c'est un malentendu. »", 7, "pb-2 cc-1"),
        ]),
        I(9, "malick", "sad",
          "Il vous regarde longtemps. « Deux nuits. » Sa voix est très calme. « Vous savez ce "
          "que j'ai fait, mardi soir ? J'ai cherché sur internet combien de temps on vit avec "
          "le sida. J'ai écrit une lettre à ma mère. »", [
            R("« Je suis désolé·e. Ce que vous avez traversé est réel, même si le résultat est "
              "négatif. Est-ce que vous voulez que je vous explique ce qui s'est passé avec ce "
              "premier test, pour que ça ait un sens ? »", 11, "co3 em2 cc2 pb1 rd1"),
            R("« L'important, c'est que ce soit négatif. »", 10, "em-2 co-2"),
            R("Rester silencieux·se, et le laisser finir.", 11, "co2 er2"),
            R("« Il ne fallait pas écrire à votre mère avant d'être sûr. »", 10, "em-3 rd-2"),
        ]),
        I(10, "malick", "cold-anger",
          "« Tout va bien. » Il se lève à moitié. « Ma copine est chez sa sœur, j'ai écrit une "
          "lettre d'adieu à ma mère, et tout va bien. »", [
            R("« Vous avez raison, c'était une phrase stupide. Ces deux jours ont coûté "
              "cher, et une partie de ce coût vient de nous. »", 11, "er2 pb2 co2"),
            R("« Je voulais dire médicalement. »", 11, "em-2 er-1"),
            R("« Pardon. Dites-moi ce qui a été le plus dur. »", 11, "em3 er1"),
            R("« On ne peut pas toujours tout prévoir. »", 11, "pb-2 em-1"),
        ]),
        I(11, "malick", "neutral",
          "Il s'essuie les yeux. « D'accord. Expliquez-moi. Pourquoi le premier test a dit "
          "oui ? »", [
            R("« Un test de dépistage est réglé pour ne rater personne. Le prix, c'est qu'il "
              "sonne parfois à tort, surtout chez quelqu'un qui n'a pas été exposé. C'est pour "
              "ça qu'on confirme toujours avec un second test, plus spécifique. »",
              12, "cc3 rd1 em1"),
            R("« C'est technique, il y a des réactions croisées. »", 12, "cc-1"),
            R("« Ça n'a pas d'importance, c'est négatif. »", 12, "cc-2 rd-1"),
            R("« Je peux vous dessiner comment on passe d'un test à un diagnostic, si vous voulez. »", 12, "cc2 rd1"),
        ]),
        I(12, "malick", "suspicious",
          "« Et le contrôle dans six semaines ? » Il pose le doigt sur la ligne du compte-rendu. "
          "« Donc ce n'est pas vraiment fini. »", [
            R("« C'est une vérification de sécurité, prévue pour tous les cas comme le vôtre. "
              "Sans exposition récente, on ne s'attend pas à une surprise. Je vous le dis parce "
              "que je préfère que vous l'appreniez de moi que du compte-rendu. »",
              15, "cc3 pb2 er1"),
            R("« C'est une formalité, vous pouvez même ne pas le faire. »", 15, "cc-2 pb-2"),
            R("« On ne peut jamais être sûr à cent pour cent. »", 15, "cc-1 em-2 co-1"),
            R("« Oui, c'est une vérification. Et si ça vous angoisse, on fixe la date maintenant, ensemble. »", 15, "cc2 em1 co1"),
        ]),
        I(13, "malick", "cold-anger",
          "« La procédure. » Il plie la feuille, lentement. « Ma mère a vu mourir des gens du "
          "sida. J'ai failli l'appeler. La procédure. »", [
            R("« Pardon. Ce n'est pas une réponse. La vraie réponse, c'est qu'un test de "
              "dépistage ne suffit jamais, et que vous avez dû porter l'attente. Je peux vous "
              "expliquer pourquoi. »", 11, "er2 cc2 em2"),
            R("« Je comprends votre frustration. »", 15, "em-1 cc-1"),
            R("Se taire, et hocher la tête.", 11, "er2"),
            R("« Ce n'est pas moi qui fais les procédures. »", 15, "pb-2 er-1"),
        ]),
        I(14, "malick", "anxious",
          "« Vous feriez ça ? » Il hésite. « Oui. Je veux qu'elle entende que ce n'est pas moi "
          "qui ai menti. Et qu'elle entende le mot négatif de la bouche d'un médecin. »", [
            R("« Alors on fixe ça maintenant. Je note au dossier que vous nous autorisez à "
              "parler de votre résultat avec elle, en votre présence. »", 15, "pb3 cc2 rd2"),
            R("« On l'appellera. »", 15, "pb-1 cc-1"),
            R("« Oui. Voulez-vous qu'on l'appelle ensemble, maintenant ? »", 15, "ic1 cc2 rd1"),
            R("« Si elle vient, je lui dirai tout. »", 15, "pb-3 rd-1"),
        ]),
        I(15, "moreau", "neutral",
          "Après son départ, Dr Moreau referme le dossier. « Deux jours d'attente, un faux "
          "positif. Le résultat est bon. Qu'est-ce que ce patient emporte, lui ? »", [
            R("« Une peur qui ne s'effacera pas avec un papier, et peut-être une confiance "
              "abîmée. C'est aussi pour ça qu'on doit choisir chaque mot quand on n'a pas de "
              "diagnostic. »", END, "er2 em2 cc2"),
            R("« Un résultat négatif, c'est l'essentiel. »", END, "em-2 er-1"),
            R("« Il aurait dû moins lire internet. »", END, "rd-2 em-2 pb-1"),
            R("« Une leçon pour moi : les mots qu'on choisit pèsent autant que les résultats. »", -1, "er2 cc1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3.6 Douze jours plus tard — nouvelle scène
# ---------------------------------------------------------------------------
S3_6 = S(6, "3.6 Douze jours plus tard",
    "Lundi, dernier jour de policlinique. Créneau d'urgence de 11 h : Yann Dubois. Motif : "
    "« vision floue de l'œil droit ». Il est venu trois jours après le début des "
    "symptômes. Dr Moreau l'a examiné avec vous : baisse d'acuité, douleur aux mouvements "
    "de l'œil, couleurs délavées. Une névrite optique est probable ; l'IRM et le "
    "neurologue sont demandés.",
    focus=("cc", "em", "pb", "er"),
    entries=[
        Entry(2, when(all=["yann_filet"]),
              "Lundi, dernier jour de policlinique. Créneau d'urgence de 11 h : Yann Dubois, "
              "venu le jour même, comme c'était écrit sur la feuille que vous lui aviez "
              "remise. Dr Moreau l'a examiné avec vous : baisse d'acuité de l'œil droit, "
              "douleur aux mouvements oculaires, couleurs délavées. Une névrite optique est "
              "probable ; l'IRM et le neurologue sont demandés."),
        Entry(3, when(all=["yann_stress"]),
              "Lundi, dernier jour de policlinique. Créneau d'urgence de 11 h : Yann Dubois. "
              "Sa vision de l'œil droit baisse depuis six jours. Dr Moreau l'a examiné avec "
              "vous : baisse d'acuité, douleur aux mouvements oculaires, couleurs délavées. "
              "Une névrite optique est probable ; l'IRM et le neurologue sont demandés."),
    ],
    nodes=[
        I(1, "yann", "anxious",
          "Il cligne de l'œil droit, comme pour chasser une poussière. « Trois jours. J'ai "
          "attendu trois jours parce que je ne savais pas si c'était assez grave pour "
          "revenir. » Il vous regarde. « C'est grave ? »", [
            R("« C'est sérieux, et vous avez bien fait de venir. Je vais vous dire ce qu'on "
              "pense, ce qu'on ne sait pas encore, et ce qui se passe aujourd'hui. »",
              4, "cc3 em2 rd1"),
            R("« Ce n'est sûrement rien, mais on va vérifier. »", 5, "cc-2 pb-1"),
            R("« Vous auriez dû venir tout de suite. »", 6, "em-2 rd-1"),
            R("« Vous avez bien fait. Racontez-moi comment ça a commencé. »", 4, "em2 cc2"),
            R("« C'est sûrement le stress qui revient. »", 5, "cc-3 em-2 rd-2"),
        ]),
        I(2, "yann", "anxious",
          "Il a la feuille de l'autre fois dans la main, pliée en quatre. « Déficit de la "
          "vision : urgences le jour même. » Il la pose sur le bureau. « J'ai fait ce que "
          "vous aviez écrit. C'est grave ? »", [
            R("« Vous avez exactement bien fait. C'est sérieux, et je vais vous dire ce qu'on "
              "pense, ce qu'on ne sait pas encore, et ce qui se passe aujourd'hui. »",
              4, "cc3 em2 rd1"),
            R("« Bravo, vous avez suivi les consignes. »", 4, "cc0 rd-1"),
            R("« Ce n'est sûrement rien, mais on vérifie. »", 5, "cc-2 pb-1"),
            R("« Merci d'être venu tout de suite. Racontez-moi. »", 4, "em2 rd1"),
            R("« Vous avez bien fait, mais c'est sûrement bénin. »", 5, "cc-2 pb-1"),
        ]),
        I(3, "yann", "angry",
          "Il ne s'assoit pas. « Six jours. » Il cligne de l'œil droit. « Je me suis dit que "
          "c'était le stress. C'est ce que vous m'aviez dit, non ? Que c'était le stress. »", [
            R("« Oui. Je vous ai dit ça, et j'ai eu tort de réduire vos symptômes au stress. "
              "Je suis désolé·e. Ce qui se passe aujourd'hui est sérieux, et je vais vous dire "
              "tout ce qu'on sait. »", 7, "pb3 cc2 er2 rd2"),
            R("« J'ai dit que le stress pouvait jouer, pas que c'était seulement ça. »",
              8, "pb-2 er-1 cc-1"),
            R("« Les examens étaient normaux à ce moment-là. »", 8, "em-2 pb-1"),
            R("« Vous avez raison d'être en colère. Je vous dois des excuses. »", 7, "pb2 er2 rd1"),
            R("« Je ne me souviens pas d'avoir dit ça. »", 8, "pb-3 cc-3 rd-1"),
        ]),
        I(4, "yann", "neutral",
          "« Allez-y. » Il s'assoit, les mains à plat sur les cuisses.", [
            R("« Le nerf qui relie votre œil au cerveau est probablement enflammé. Ça "
              "s'appelle une névrite optique. La vision revient le plus souvent, en quelques "
              "semaines. On va faire une IRM et vous voyez un neurologue aujourd'hui. »",
              9, "cc3 em1 co1"),
            R("« C'est probablement une névrite optique rétrobulbaire, d'origine "
              "inflammatoire ou démyélinisante. »", 10, "cc-2 em-1"),
            R("« C'est sûrement une sclérose en plaques qui débute. »", 11, "cc-3 pb-3 co-2"),
            R("« C'est une inflammation de l'œil. Vous voulez le mot exact, ou seulement ce que ça change ? »", 9, "rd2 cc2"),
        ]),
        I(5, "yann", "suspicious",
          "« Rien. » Il répète le mot. « La dernière fois, c'était rien non plus. Et me "
          "revoilà. »", [
            R("« Vous avez raison, je retire ça. C'est sérieux, et je vais vous dire ce qu'on "
              "pense. »", 4, "cc2 er1 pb1"),
            R("« On ne peut pas savoir avant les examens. »", 4, "cc-1"),
            R("« Pardon. C'est sérieux, et vous avez bien fait de revenir. »", 4, "cc2 er1"),
            R("« Je ne peux pas vous dire autre chose. »", 4, "cc-2"),
        ]),
        I(6, "yann", "cold-anger",
          "« Je ne savais pas. » Sa mâchoire se serre. « Vous m'avez dit que tout était "
          "normal. »", [
            R("« C'est vrai, et ce n'est pas un reproche. Vous êtes là maintenant, c'est ce qui "
              "compte. Laissez-moi vous expliquer. »", 4, "er2 em2 pb1"),
            R("« Je dis juste que c'est dommage. »", 4, "em-2 er-1"),
            R("« Vous avez raison, on vous avait dit que tout était normal. Pardon pour le ton. »", 4, "er2 pb1"),
            R("« Il fallait lire la feuille. »", 4, "em-3 rd-2"),
        ]),
        I(7, "yann", "sad",
          "Il reste debout un moment, puis s'assoit. « Merci de le dire. » Un temps. « Six "
          "jours à me dire que j'étais fragile. Que j'inventais. »", [
            R("« Vous n'inventiez rien. Vous avez eu des symptômes réels, et on vous a donné "
              "une explication trop rapide. Est-ce que ces six jours ont changé quelque chose "
              "pour votre œil, je vais le demander au neurologue — honnêtement. »",
              4, "em3 pb2 cc2 rd2"),
            R("« L'important, c'est d'avancer maintenant. »", 4, "em-1 pb-1"),
            R("« Vous étiez tout sauf fragile. Vous êtes revenu. »", 4, "em2 rd2"),
            R("« Le stress a peut-être quand même joué. »", 4, "em-3 rd-2 pb-1"),
        ]),
        I(8, "moreau", "cold-anger",
          "Dr Moreau, adossé·e à la porte, intervient calmement. « Monsieur Dubois, la "
          "dernière fois, on a mis trop de poids sur le stress. C'est notre responsabilité. » "
          "Puis, vers vous : « Alex, vous voulez compléter ? »", [
            R("« Oui. C'est moi qui vous l'ai dit, et j'ai eu tort. Je suis désolé·e. »",
              7, "pb3 er2 cc1"),
            R("« Non, c'est bon. »", 4, "pb-2 er-1"),
            R("« Oui. Et je vais demander au neurologue ce que ces six jours ont changé, pour vous le dire franchement. »", 7, "pb3 cc2"),
            R("« Je ne pouvais pas savoir, à l'époque. »", 4, "pb-2 er-1"),
        ]),
        I(9, "yann", "anxious",
          "« Une inflammation. » Il hoche la tête. Puis, très vite : « C'est la sclérose en "
          "plaques ? J'ai lu que ça commençait comme ça. Mes fourmillements d'il y a trois "
          "mois, c'était ça ? »", [
            R("« C'est une des possibilités, oui, et je ne vais pas vous le cacher. Mais une "
              "névrite optique peut aussi rester un épisode isolé. C'est l'IRM et le "
              "neurologue qui permettront d'y voir plus clair. Aujourd'hui, personne ne peut "
              "vous répondre honnêtement oui ou non. »", 12, "cc3 pb2 em1"),
            R("« Non, n'y pensez pas. »", 13, "cc-3 pb-2"),
            R("« Probablement, oui. »", 11, "cc-3 pb-3 co-1"),
            R("« Je comprends que vous y pensiez. On ne peut pas encore le dire, et je ne veux pas deviner. »", 12, "cc2 pb2"),
        ]),
        I(10, "yann", "confused",
          "« Démyé… quoi ? » Il sort son téléphone pour taper le mot. « Vous pouvez me dire "
          "ça comme à un humain ? »", [
            R("« Pardon. Le nerf de l'œil est enflammé. La vision revient souvent. Aujourd'hui : "
              "une IRM et un neurologue. »", 9, "cc3 er1"),
            R("« Le neurologue vous expliquera. »", 13, "cc-2 ic-1"),
            R("« Pardon. Votre nerf optique est enflammé. C'est ce qui brouille la vue. »", 9, "cc2"),
            R("« Tapez-le, vous trouverez. »", 13, "cc-3 rd-2"),
        ]),
        I(11, "yann", "sad",
          "Il pâlit. « Une sclérose en plaques. » Il regarde sa main droite, la ferme, "
          "l'ouvre. « Je vais finir en fauteuil. »", [
            R("« Je me suis avancé·e, et je ne devais pas : rien n'est établi aujourd'hui. Et "
              "même si c'était ce diagnostic, ce que vous imaginez n'est pas ce qui attend la "
              "plupart des gens, avec les traitements actuels. »", 12, "cc2 pb2 co2 er1"),
            R("« Pas forcément, il y a des traitements. »", 12, "co1 cc0"),
            R("Se taire un instant, puis : « Personne ne peut vous dire ça aujourd'hui. Moi non plus. »", 12, "cc2 er2"),
            R("« Il ne faut pas voir le pire, il y a des gens en fauteuil qui vivent très bien. »", 12, "em-3 co-2"),
        ]),
        I(12, "yann", "neutral",
          "Il reste silencieux un moment. « Au moins, cette fois, il y a quelque chose. » Un "
          "sourire bizarre. « C'est horrible de dire ça, non ? D'être presque soulagé. »", [
            R("« Non. Pendant trois mois, on vous a dit que tout était normal alors que vous "
              "aviez mal. Être cru, ça soulage, même quand la nouvelle est lourde. »",
              14, "em3 co2 rd2"),
            R("« Un peu, oui. »", 14, "em-2 rd-1"),
            R("« Ne soyez pas soulagé trop vite, on ne sait encore rien. »", 14, "em-2 co-1"),
            R("« C'est humain. Vous avez enfin l'impression d'être pris au sérieux. »", 14, "em2 rd2"),
        ]),
        I(13, "yann", "angry",
          "« N'y pensez pas. » Il a un rire amer. « Vous me l'avez déjà faite, celle-là. »", [
            R("« Vous avez raison. Je recommence : c'est une possibilité, pas une certitude, "
              "et on va chercher à savoir. »", 12, "cc2 pb2 er1"),
            R("« Je dis ça pour vous. »", 14, "em-1 pb-1"),
            R("« Oui. Pardon. On va chercher la réponse ensemble. »", 12, "cc2 er1"),
            R("« Ce n'était pas moi, la dernière fois. »", 14, "pb-3 cc-2"),
        ]),
        I(14, "yann", "neutral",
          "« Je dois appeler ma copine. » Il se lève. « La dernière fois, je ne lui avais rien "
          "dit. Cette fois, je vais le faire. » À la porte : « Vous serez là, pour l'IRM ? »", [
            R("« Je termine mon stage à la policlinique aujourd'hui. Mais je note tout pour le "
              "neurologue, et je vous présente à lui avant de partir. Vous ne recommencez pas "
              "de zéro. »", 15, "cc3 ic2 pb2"),
            R("« Oui, oui. »", 15, "pb-2 cc-2"),
            R("« Non, je change de service. »", 15, "em-2 cc-1"),
            R("« Voulez-vous qu'on appelle votre copine ensemble, depuis ici ? »", 15, "co2 ic1"),
        ]),
        I(15, "moreau", "neutral",
          "Dr Moreau reprend avec vous, porte fermée. « Il y a douze jours, vous vouliez une "
          "IRM de contrôle à trois mois. Est-ce qu'elle aurait changé quelque chose ? »", [
            R("« Non. Ce qui compte, c'est ce qu'il savait faire quand les symptômes sont "
              "arrivés — et ce qu'on lui avait dit de ses symptômes. L'incertitude ne se "
              "réduit pas avec des examens, elle se balise. »", END, "cc3 pb2 er1"),
            R("« Peut-être, on aurait vu les lésions plus tôt. »", END, "cc-1 er-1"),
            R("« On ne pouvait pas deviner. »", END, "pb-2 er-1"),
            R("« Non. Mais ma phrase sur le stress, elle, a changé quelque chose. »", -1, "pb3 er2"),
        ]),
    ],
)

CH3 = C(3, "Le doute",
    situation=(
        "Troisième semaine, à la policlinique de médecine interne. Deux consultations sans "
        "diagnostic : un bilan non concluant, puis un test de dépistage réactif non "
        "confirmé. Et tout ce qui se passe ensuite — une compagne au guichet, un résultat "
        "qui arrive, un patient qui revient."
    ),
    objectives=(
        "annoncer une incertitude sans la transformer en fausse réassurance ni en "
        "banalisation, valider la réalité du symptôme, distinguer un test de dépistage d'un "
        "diagnostic et raisonner en valeur prédictive, borner l'attente par un filet de "
        "sécurité explicite, protéger le secret médical face à un proche, annoncer un "
        "résultat rassurant sans effacer ce qu'a coûté l'attente, reconnaître une erreur de "
        "jugement devant le patient, et identifier sa propre intolérance à l'incertitude."
    ),
    anchoring=(
        "UNIL M1.5 Généralisme I (« Docteur, j'ai mal ») et M1.6 cours-blocs (tests "
        "diagnostiques, épidémiologie, prévention et contrôle des infections), M1.7 droit "
        "médical · UNIGE M1 AMC Médecine communautaire et de premier recours."
    ),
    focus=("cc", "pb", "rd", "er"),
    scenes=[S3_1, S3_2, S3_3, S3_4, S3_5, S3_6],
)
