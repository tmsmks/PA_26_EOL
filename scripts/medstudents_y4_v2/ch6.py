"""Chapitre 6 — Ce qui reste (semaines 7-8, puis trois mois).

Deux voies selon la nuit du 14 (chapitre 5) : « erreur » (famille, avocate, revue
d'incident, audition) ou « évitée » (déclaration, Kevin, revue, Jonas). La scène 6.5
est commune. Les scènes sont entrelacées dans la liste pour que chaque voie les
joue dans l'ordre des emplacements (slots).
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, StartChoice, when

ERREUR = when(all=["erreur"])
EVITE = when(all=["evite"])

# ===========================================================================
# Voie ERREUR
# ===========================================================================

# ---------------------------------------------------------------------------
# 6.1 La rencontre
# ---------------------------------------------------------------------------
_INTRO_61_DECES = (
    "Lundi, quatre jours après la nuit du 14. Salle de réunion du 5ᵉ étage. Entretien "
    "d'information après incident : Dr Moreau, Nathalie Perrin (sécurité des patients) et "
    "vous. En face : Monique Jaquier, en noir, et son fils Olivier, un classeur devant lui."
)
_INTRO_61_SURVIE = (
    "Lundi, quatre jours après la nuit du 14. M. Jaquier a été extubé hier ; il ne sent "
    "presque plus ses jambes — une faiblesse acquise en réanimation, disent les "
    "intensivistes. Salle de réunion du 5ᵉ étage : Dr Moreau, Nathalie Perrin (sécurité "
    "des patients) et vous. En face : Monique Jaquier et son fils Olivier."
)
S6_1E = S(1, "6.1 La rencontre",
    _INTRO_61_DECES,
    focus=("rd", "co", "cc", "er"),
    slot="6.1",
    cond=ERREUR,
    entries=[
        Entry(2, when(all=["deces", "esquive"]), _INTRO_61_DECES),
        Entry(1, when(all=["deces"]), _INTRO_61_DECES),
        Entry(4, when(all=["survie", "esquive"]), _INTRO_61_SURVIE),
        Entry(3, when(all=["survie"]), _INTRO_61_SURVIE),
    ],
    nodes=[
        I(1, "monique", "neutral",
          "Nathalie Perrin explique son rôle en deux phrases. Dr Moreau présente les excuses "
          "de l'hôpital et annonce qu'une analyse est en cours. Mme Jaquier écoute sans "
          "bouger, puis elle se tourne vers vous. « Je veux que ce soit vous qui me disiez. "
          "Ce qui s'est passé à 19 h. »", [
            R("« D'accord. Je vais vous dire ce que j'ai fait, et ce que je n'ai pas fait. »",
              5, "pb2 rd2 er1"),
            R("Regarder Dr Moreau.", 5, "pb-1 er-1"),
            R("« Je ne peux pas parler avant la fin de l'analyse. »", 7, "rd-2 pb-1 em-1"),
            R("« Oui. Je vous dois ça. »", 5, "rd2 pb2"),
            R("« Tout est dans le rapport, vous pourrez le lire. »", 7, "rd-3 pb-2 em-1"),
        ]),
        I(2, "monique", "cold-anger",
          "Mme Jaquier n'attend pas que Dr Moreau ait fini. Elle vous regarde, vous. « La "
          "nuit où il est mort, vous m'avez parlé du dossier des urgences. De l'infirmier. » "
          "Sa voix ne tremble pas. « Je veux savoir si c'était vrai. Et ce qui s'est passé à "
          "19 h. »", [
            R("« Ce que je vous ai dit cette nuit-là était une manière de ne pas dire ma part. "
              "Je vous en demande pardon. Voici ce qui s'est passé. »", 5, "pb3 rd2 er2"),
            R("« C'était vrai, le dossier disait bien « aucune allergie ». »", 6, "pb-3 rd-2 cc-2"),
            R("« Je ne peux pas parler avant la fin de l'analyse. »", 7, "rd-2 pb-1"),
            R("« Non, ce n'était pas toute la vérité. Je vais vous la dire maintenant. »", 5, "pb3 rd2"),
            R("« J'étais sous le choc, ça ne compte pas. »", 6, "pb-2 er-1 rd-1"),
        ]),
        I(3, "monique", "anxious",
          "Dr Moreau présente les excuses de l'hôpital. Mme Jaquier a des cernes jusqu'aux "
          "joues : quatre nuits sur une chaise en réanimation. « Il ne sent plus ses jambes. "
          "On me dit que ça reviendra, peut-être. » Elle se tourne vers vous. « Je veux que "
          "ce soit vous qui me disiez. Ce qui s'est passé à 19 h. »", [
            R("« D'accord. Je vais vous dire ce que j'ai fait, et ce que je n'ai pas fait. »",
              5, "pb2 rd2 er1"),
            R("Regarder Dr Moreau.", 5, "pb-1 er-1"),
            R("« Je ne peux pas parler avant la fin de l'analyse. »", 7, "rd-2 pb-1 em-1"),
            R("« Je suis désolé·e pour ses jambes. Oui, je vais vous dire ce qui s'est passé à 19 h. »", 5, "co2 rd2 pb1"),
            R("« Tout est dans le rapport, vous pourrez le lire. »", 7, "rd-3 pb-2 em-1"),
        ]),
        I(4, "monique", "cold-anger",
          "Mme Jaquier a des cernes jusqu'aux joues. Elle n'attend pas la fin des excuses de "
          "Dr Moreau. « La nuit du 14, vous m'avez parlé du dossier des urgences. De "
          "l'infirmier. » Elle vous fixe. « Mon mari ne sent plus ses jambes. Je veux savoir "
          "si c'était vrai. Et ce qui s'est passé à 19 h. »", [
            R("« Ce que je vous ai dit cette nuit-là était une manière de ne pas dire ma part. "
              "Je vous en demande pardon. Voici ce qui s'est passé. »", 5, "pb3 rd2 er2"),
            R("« C'était vrai, le dossier disait bien « aucune allergie ». »", 6, "pb-3 rd-2 cc-2"),
            R("« Je ne peux pas parler avant la fin de l'analyse. »", 7, "rd-2 pb-1"),
            R("« Non, ce n'était pas toute la vérité. Je vais vous la dire maintenant. »", 5, "pb3 rd2"),
            R("« J'étais sous le choc, ça ne compte pas. »", 6, "pb-2 er-1 rd-1"),
        ]),
        I(5, "narr", "",
          "Tout le monde attend. Olivier a posé son stylo. Vous savez ce que vous allez dire, "
          "et ce qu'il vous en coûtera.", [
            R("« Je n'ai pas posé la question des allergies jusqu'au bout. Ce que vous saviez "
              "n'est arrivé ni dans le dossier, ni jusqu'au médecin qui a prescrit. J'en fais "
              "partie. Je suis désolé·e. »", 8, "pb3 rd3 cc2 er1"),
            R("« La lettre des urgences disait « aucune allergie connue ». Je l'ai "
              "reprise. »", 6, "pb-2 cc-1"),
            R("« Beaucoup de choses ont mal fonctionné cette nuit-là. »", 7, "cc-2 pb-1"),
            R("« Vous l'aviez dit, votre mari l'avait minimisé, et je n'ai rien écrit. C'est ma part, et je vous en demande pardon. »", 8, "pb3 rd2 co1"),
            R("« L'hôpital va vous expliquer, ce n'est pas à moi de le faire. »", 7, "pb-2 rd-2 er-1"),
        ]),
        I(6, "olivier", "angry",
          "Olivier se lève à moitié. « Le dossier. Encore le dossier. » Il frappe le classeur "
          "du plat de la main. « Ma mère vous l'a dit. Vous l'avez entendue. Arrêtez de vous "
          "cacher derrière un papier. »", [
            R("« Vous avez raison. Je me cache. Je recommence : je ne suis pas allé·e au bout, "
              "et ce que votre mère savait n'est pas arrivé au prescripteur. J'en fais partie. "
              "Je suis désolé·e. »", 8, "pb3 er2 rd1"),
            R("« Je dis simplement les faits. »", 7, "pb-2 er-1"),
            R("Se taire un instant, puis : « Vous avez raison. Pardon. »", 8, "pb2 er2"),
            R("« Je ne me cache pas, je suis les procédures. »", 7, "pb-3 er-2"),
        ]),
        I(7, "perrin", "neutral",
          "Nathalie Perrin intervient doucement. « L'analyse cherche comment c'est arrivé. Elle "
          "n'empêche personne de dire ce qu'il sait. Au contraire. » Elle vous regarde. "
          "« Alex, ce que vous savez, vous pouvez le dire. »", [
            R("« Je n'ai pas posé la question des allergies jusqu'au bout. Ce que Mme Jaquier "
              "savait n'est arrivé ni dans le dossier, ni au prescripteur. J'en fais partie. Je "
              "suis désolé·e. »", 8, "pb3 rd2 cc2"),
            R("« Je préfère attendre les conclusions. »", 9, "pb-1 rd-2"),
            R("« D'accord. Voilà ce que j'ai fait, et ce que je n'ai pas fait. » Puis le dire.", 8, "pb2 cc2 rd1"),
            R("« On m'a conseillé de ne rien dire. »", 9, "pb-2 cc-2"),
        ]),
        I(8, "olivier", "cold-anger",
          "Un silence. Olivier vous regarde longtemps. « Vous êtes désolé·e. » Il a un rire "
          "bref. « Mon père… » Il ne finit pas. « Et vous êtes désolé·e. »", [
            R("« Oui. Ça ne répare rien, et je ne vous demande rien. Je voulais que vous "
              "l'entendiez de moi. »", 10, "rd2 er2 co2 pb1 em1"),
            R("« Je fais ce que je peux. »", 10, "er-1 co-1"),
            R("« Je ne suis pas seul·e responsable. »", 11, "pb-1 ic-1 er-1"),
            R("Soutenir son regard. « Oui. Désolé·e, et responsable de ma part. »", 10, "pb2 er2 rd1"),
            R("« Qu'est-ce que vous voulez que je dise d'autre ? »", 11, "er-3 rd-2"),
        ]),
        I(9, "olivier", "angry",
          "« Les conclusions. » Olivier referme son classeur. « Vous savez quoi ? On les "
          "attendra avec une avocate. »", [
            R("« C'est votre droit. Et je ne veux pas vous faire attendre pour ce que je sais "
              "déjà : je n'ai pas posé la question jusqu'au bout. J'en fais partie. »",
              10, "pb3 er2"),
            R("« Comme vous voulez. »", 12, "er-1 rd-1"),
            R("« Je comprends. Et je dirai la même chose devant elle. »", 10, "pb2 er1"),
            R("« Votre avocate ne changera rien aux faits. »", 12, "er-2 rd-2"),
        ]),
        I(10, "olivier", "cold-anger",
          "« Qui a posé la perfusion ? » Olivier a repris son stylo. « Je veux un nom. »", [
            R("« Le médicament a été prescrit et administré avec ce que le dossier disait. "
              "L'analyse porte sur tout le chemin, pas sur une personne. Je ne vous donnerai "
              "pas un nom pour vous donner un coupable. »", 13, "pb3 ic3 cc1 er1"),
            R("« L'infirmier de nuit, Kevin Da Silva. »", 14, "ic-3 pb-3 rd-1"),
            R("« Je ne sais pas. »", 13, "pb-2 cc-2"),
            R("« Le nom que je peux vous donner, c'est le mien : c'est moi qui ai fait son entrée. »", 13, "pb3 er2"),
        ]),
        I(11, "perrin", "cold-anger",
          "Nathalie Perrin pose la main sur la table. « C'est vrai que l'analyse identifie "
          "plusieurs maillons. Mais la famille n'a pas à entendre qui se défausse. » Elle "
          "vous regarde. Olivier aussi.", [
            R("« Pardon. Je retire. Ma part existe, et c'est d'elle que je dois parler. »",
              10, "pb2 er2"),
            R("Se taire.", 10, "er0 pb-1"),
            R("« Vous avez raison. Je ne suis pas seul·e, mais ma part est réelle. »", 10, "pb2 er1"),
            R("« C'est pourtant vrai. Le Dr Neuhaus n'a pas relu. »", 14, "ic-3 pb-2"),
        ]),
        I(12, "moreau", "cold-anger",
          "Dr Moreau vous regarde sans rien dire. Puis, à la famille : « Alex a fait l'entrée "
          "de M. Jaquier. L'allergie signalée n'a été ni documentée ni transmise. C'est une "
          "erreur, et l'hôpital la reconnaît. » Olivier note chaque mot.", [
            R("« C'est exact. Je suis désolé·e. »", 10, "pb2 rd1"),
            R("Baisser les yeux.", 10, "pb-1 er-1"),
            R("« C'est exact. Et c'est à moi de le porter, pas au Dr Moreau. »", 10, "pb3 er1"),
            R("« Ce n'est pas tout à fait exact. »", 10, "pb-3 cc-2"),
        ]),
        I(13, "monique", "sad",
          "Mme Jaquier parle pour la première fois depuis longtemps. « Est-ce que ça va "
          "arriver à quelqu'un d'autre ? »", [
            R("« C'est exactement ce que l'analyse doit empêcher. Mme Perrin peut vous dire ce "
              "qui a déjà changé, et vous tenir informée de la suite. »", 15, "cc2 ic2 rd1"),
            R("« Non. Jamais. »", 15, "cc-2 pb-2"),
            R("« On ne peut pas l'exclure. »", 15, "cc1 co-2"),
            R("« Je ne peux pas vous le promettre. Mais je peux vous dire ce qui a déjà changé depuis cette nuit-là. »", 15, "cc2 pb2 rd1"),
        ]),
        I(14, "moreau", "cold-anger",
          "Dr Moreau coupe, très calme. « Nous ne désignons personne à la place de "
          "l'analyse. » Olivier : « Donc vous vous protégez entre vous. » Tout le monde vous "
          "regarde.", [
            R("« Non. J'ai eu tort de donner un nom. Kevin a fait ce qu'on lui a dit. Ma part "
              "est arrivée avant. »", 13, "pb2 er1 ic2"),
            R("Se taire.", 13, "ic-1 er-1"),
            R("« Non. Et je retire ce que j'ai dit sur Kevin. »", 13, "pb2 ic2"),
            R("« Je dis juste qui a branché. »", 13, "ic-3 pb-2"),
        ]),
        I(15, "olivier", "neutral",
          "Olivier fait glisser une carte de visite sur la table. « Me Claire Dufaux. Notre "
          "avocate. » Il se lève. « Elle vous contactera. »", [
            R("« C'est votre droit. Nous répondrons à ses questions, et je dirai la même chose "
              "qu'aujourd'hui. »", 16, "pb3 er2 cc1 rd1"),
            R("« Vous n'aviez pas besoin d'aller jusque-là. »", 16, "pb-2 rd-2"),
            R("« Alors je ne peux plus vous parler. »", 16, "pb-1 em-2 co-1"),
            R("« D'accord. J'aimerais quand même pouvoir répondre à votre mère, si elle le veut. »", 16, "co2 pb1 rd1"),
        ]),
        I(16, "monique", "sad",
          "Olivier est déjà dans le couloir. Mme Jaquier s'arrête à votre hauteur. « Quarante "
          "ans aux CFF. « Un aiguilleur qui se trompe d'une minute, ça fait un accident », "
          "c'était sa phrase. » Elle vous regarde. « Vous, vous allez continuer ? »", [
            R("« Oui. Et je n'oublierai pas votre mari. Ni ce que vous aviez dit ce soir-là. »",
              END, "co3 rd2 er1 em1"),
            R("« Je ne sais pas. »", END, "er1"),
            R("« C'est le métier. »", END, "co-2 rd-1"),
            R("« Je ne sais pas encore. Mais je ne ferai plus jamais une entrée de la même façon. »", -1, "pb2 er1 co1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.2 La lettre
# ---------------------------------------------------------------------------
_INTRO_62 = (
    "Dix jours plus tard. Une lettre recommandée de Me Claire Dufaux est arrivée à la "
    "direction : elle demande le dossier complet, historique compris, et annonce une "
    "action en responsabilité ainsi qu'une plainte pénale. Bureau du juriste de "
    "l'hôpital, M. Rochat. Dr Moreau est là."
)
S6_2E = S(3, "6.2 La lettre",
    _INTRO_62,
    focus=("pb", "cc", "er"),
    slot="6.2",
    cond=ERREUR,
    entries=[
        Entry(2, when(all=["dossier_modifie"]), _INTRO_62),
        Entry(3, when(all=["allergie_carnet"]), _INTRO_62),
    ],
    debriefs=[
        Debrief(when(all=["dossier_modifie"]), tone="hard", lead=(
            "Une ligne réécrite à 6 h 47 a transformé une erreur de transmission en question "
            "d'intégrité. Ce n'est plus seulement ce que vous n'avez pas fait qui sera "
            "examiné : c'est ce que vous avez fait après.")),
    ],
    nodes=[
        I(1, "rochat", "neutral",
          "M. Rochat parle lentement. « Je suis là pour l'hôpital, et en partie pour vous. Au "
          "civil, c'est l'hôpital qui répond envers la famille, pas vous personnellement. Au "
          "pénal, c'est autre chose. » Il croise les mains. « Première question : y a-t-il "
          "quoi que ce soit, dans ce dossier ou ailleurs, que je devrais savoir avant "
          "l'avocate ? »", [
            R("« Tout est dans ma note de 7 h, le matin même. Je n'ai rien d'autre, et je "
              "répondrai à toutes vos questions. »", 5, "pb2 cc2"),
            R("« Qu'est-ce que je risque, moi ? »", 4, "er-1"),
            R("« Je préfère ne rien dire sans avocat. »", 4, "pb0 ic-1 er-1"),
            R("« Il y a peut-être des choses que je n'ai pas dites. Je préfère tout vous dire maintenant. »", 5, "pb3 cc1"),
            R("« Qu'est-ce que je dois dire pour ne pas avoir de problème ? »", 4, "pb-3 er-1"),
        ]),
        I(2, "rochat", "cold-anger",
          "M. Rochat pose une feuille imprimée sur le bureau. « Historique du dossier "
          "Jaquier. Ligne « allergies » : modifiée le 15 à 06:47, par votre identifiant. "
          "Version initiale : « aucune allergie connue ». » Il vous regarde par-dessus ses "
          "lunettes. « Me Dufaux a demandé l'historique. Elle l'aura. Expliquez-moi. »", [
            R("« Je l'ai modifiée. J'ai eu peur. Je ne vais pas mentir là-dessus. »",
              6, "pb2 er2 cc2"),
            R("« C'était pour compléter, pas pour cacher. »", 7, "pb-2 cc-2"),
            R("« Le système a dû faire une erreur. »", 7, "pb-3 cc-3 er-1"),
            R("« C'est moi. Et je veux que ce soit corrigé officiellement, avec la raison. »", 6, "pb3 cc2"),
            R("« Quelqu'un a pu utiliser ma session. »", 7, "pb-3 cc-3 ic-1"),
        ]),
        I(3, "rochat", "neutral",
          "« Dr Moreau me dit que vous prenez des notes dans un carnet. » M. Rochat désigne "
          "votre poche. « Est-ce qu'il y a quelque chose sur M. Jaquier, là-dedans ? » Vous "
          "savez ce qu'il y a, à la page du 14, 19 h 40 : « Pénicilline ? — réaction il y a "
          "30 ans ».", [
            R("« Oui. Je l'ai noté et je ne l'ai pas reporté. Voici le carnet. »",
              5, "pb3 cc2 er1"),
            R("« Rien d'important. »", 8, "pb-3 cc-3 ic-1"),
            R("« Est-ce que je suis obligé·e de le donner ? »", 9, "pb-1 er-1"),
            R("Poser le carnet sur la table, ouvert à la bonne page.", 5, "pb3 cc1"),
        ]),
        I(4, "rochat", "neutral",
          "« Vous avez le droit d'être assisté·e, et si une procédure pénale vous visait, je "
          "vous conseillerais un avocat indépendant de l'hôpital. » Il marque un temps. "
          "« Aujourd'hui, vous n'êtes accusé·e de rien. Ce que je vous demande, c'est la "
          "vérité, pour que l'hôpital réponde honnêtement. »", [
            R("« D'accord. Voici ce qui s'est passé. »", 5, "pb2 cc1"),
            R("« Je vous dirai ce qui est dans ma note. Pas plus. »", 5, "pb-1 cc-1"),
            R("« D'accord. Et j'aimerais savoir ce que je peux dire à la famille si elle me contacte. »", 5, "pb2 cc1"),
            R("« Je préfère consulter un avocat avant de vous parler. »", 5, "ic-1"),
        ]),
        I(5, "moreau", "neutral",
          "Votre téléphone vibre sur la table. Un message privé sur Instagram : « Je sais qui "
          "vous êtes. Je veux vous voir seul·e. Vous me devez ça. — Olivier Jaquier ». Dr "
          "Moreau a vu l'écran.", [
            R("Montrer le message. « Je ne répondrai pas seul·e. Je veux que la famille puisse "
              "me poser ses questions, mais dans un cadre où on peut y répondre "
              "correctement. »", 10, "pb3 ic2 cc1"),
            R("Lui répondre en privé : « D'accord. Où et quand ? »", 11, "pb-3 ic-2"),
            R("Bloquer le compte.", 10, "pb0 em-2 co-1"),
            R("Répondre à Olivier : « Je suis prêt·e à répondre à vos questions, dans un cadre organisé par l'hôpital. »", 10, "pb2 cc2 rd1"),
        ]),
        I(6, "rochat", "neutral",
          "M. Rochat hoche la tête, lentement. « Merci de ne pas mentir. C'est la seule chose "
          "qui compte maintenant. » Il reprend la feuille. « Réécrire une pièce du dossier "
          "après coup peut être qualifié de faux dans les titres. Ce n'est pas moi qui en "
          "déciderai. Mais cette correction, on la rend visible nous-mêmes, avant que "
          "l'avocate la trouve. »", [
            R("« D'accord. Je veux l'écrire moi-même, avec la raison. »", 5, "pb3 er1"),
            R("« Est-ce que je vais être exclu·e de la faculté ? »", 12, "er-1"),
            R("« Merci. Et je voudrais le dire moi-même à Mme Jaquier. »", 5, "pb2 rd1"),
            R("« Si c'est déjà grave, autant ne rien dire de plus. »", 12, "pb-3 er-1"),
        ]),
        I(7, "rochat", "cold-anger",
          "« L'historique ne se trompe pas. » M. Rochat ne hausse pas la voix. « Me Dufaux ne "
          "se trompera pas non plus. Vous avez une seule occasion de dire vrai avant qu'elle "
          "vous pose la question. C'est maintenant. »", [
            R("« Je l'ai modifiée. J'ai eu peur. »", 6, "pb2 er1"),
            R("« Je maintiens ce que j'ai dit. »", 13, "pb-3 cc-2"),
            R("« Oui. Je l'ai modifiée à 6 h 47, parce que j'avais peur. »", 6, "pb3 er1"),
            R("« Je ne vois pas de quoi vous parlez. »", 13, "pb-3 cc-3"),
        ]),
        I(8, "moreau", "cold-anger",
          "Dr Moreau se tourne vers vous. « Mme Jaquier a dit à Mme Perrin que vous aviez noté "
          "quelque chose dans un petit carnet noir, le 14 au soir. » Un temps. « Alex. »", [
            R("« C'est vrai. Voici le carnet. »", 5, "pb2 er1"),
            R("« Je ne l'ai plus. »", 13, "pb-3 cc-3 ic-1"),
            R("« Oui. Il est chez moi, je l'apporte demain. »", 5, "pb2 cc1"),
            R("« C'est mon carnet personnel, ça ne vous regarde pas. »", 13, "pb-3 ic-2"),
        ]),
        I(9, "rochat", "neutral",
          "« Obligé·e, non, pas aujourd'hui. » M. Rochat retire ses lunettes. « Mais s'il "
          "existe et qu'on apprend plus tard que vous l'avez gardé pour vous, ce sera pire que "
          "tout ce qui est écrit dedans. »", [
            R("Donner le carnet.", 5, "pb2 cc1"),
            R("Le garder dans sa poche.", 13, "pb-2"),
            R("« Je vous le donne. Et j'aimerais savoir comment il sera utilisé. »", 5, "pb2 cc1"),
            R("« Je vais d'abord arracher les pages personnelles. »", 13, "pb-3 cc-2"),
        ]),
        I(10, "rochat", "neutral",
          "« Me Dufaux demande à vous entendre, en présence de l'hôpital. » M. Rochat range ses "
          "feuilles. « Vous n'êtes pas obligé·e. Si vous acceptez, je serai là. »", [
            R("« J'accepte. Je dirai la même chose qu'ici. »", END, "pb3 er2"),
            R("« Je préfère ne pas y aller. »", END, "pb0 er-1"),
            R("« Qu'est-ce que je dois dire ? »", 14, "pb-1"),
            R("« J'irai. Mais je dirai que je ne me souviens plus de rien. »", 14, "pb-3 cc-3 rd-1"),
            R("« J'accepte, et je voudrais que le Dr Moreau soit là aussi. »", -1, "pb2 ic1"),
        ]),
        I(11, "moreau", "cold-anger",
          "« Vous allez voir le fils d'un patient, seul·e, sans cadre, pendant qu'une "
          "procédure se prépare ? » Dr Moreau ne vous quitte pas des yeux. « Pour lui dire "
          "quoi ? »", [
            R("« Vous avez raison. Je lui réponds que je suis prêt·e à répondre à ses questions "
              "dans un cadre organisé. »", 10, "pb2 er1 cc1"),
            R("« Il a le droit de savoir. »", 10, "pb-2"),
            R("« Vous avez raison. Je vous montre le message, et je ne réponds pas seul·e. »", 10, "pb2 ic1"),
            R("« Je lui dois bien ça. »", 10, "pb-3"),
        ]),
        I(12, "moreau", "neutral",
          "« Je ne sais pas. » Dr Moreau ne vous ment pas non plus. « Ce que je sais, c'est "
          "que ceux qui s'en sortent le moins mal sont ceux qui arrêtent de mentir le plus "
          "tôt. »", [
            R("« Alors je rédige la correction maintenant. »", 5, "pb2 er1"),
            R("« D'accord. Je le signale moi-même. »", 5, "pb2 er1"),
            R("« Donc je suis fichu·e. »", 5, "er-2"),
            R("« Et si je ne dis rien de plus ? »", 5, "pb-3"),
        ]),
        I(13, "rochat", "cold-anger",
          "M. Rochat referme son dossier. « Je ne peux pas vous aider si vous ne me dites pas "
          "la vérité. » Il se lève. Dr Moreau regarde par la fenêtre.", [
            R("« Attendez. Je vous dis tout. »", 5, "pb2 er1"),
            R("Le laisser partir.", 10, "pb-2 er-1"),
            R("« Laissez-moi une journée pour réfléchir. »", 10, "pb-1"),
            R("Rester assis·e, sans rien dire.", 10, "pb-2 er-1"),
        ]),
        I(14, "rochat", "neutral",
          "« La vérité. Ce que vous avez vu, fait, entendu. Pas ce que vous auriez dû faire, "
          "pas ce que les autres ont fait. Et « je ne sais pas » quand vous ne savez pas. »", [
            R("« D'accord. »", END, "pb2 cc1"),
            R("« Et si on me demande ce que j'aurais dû faire ? »", -1, "pb1 cc1"),
            R("« Je dirai ce qui m'arrange, alors. »", -1, "pb-3"),
            R("« D'accord. Et je dirai « je ne sais pas » quand je ne sais pas. »", -1, "pb2 cc2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.3 La revue
# ---------------------------------------------------------------------------
S6_3E = S(5, "6.3 La revue",
    "Troisième semaine après la nuit du 14. Revue d'incident, salle de colloque. Nathalie "
    "Perrin mène la séance. Autour de la table : Dr Moreau, Dr Neuhaus, Inès Rey, Fatou "
    "Diallo, et Kevin Da Silva, en congé depuis dix jours, venu exprès.",
    focus=("ic", "pb", "cc", "er"),
    slot="6.3",
    cond=ERREUR,
    nodes=[
        I(1, "perrin", "neutral",
          "« On ne cherche pas un coupable, on cherche comment c'est arrivé. Et ce qui peut "
          "empêcher que ça recommence. » Nathalie Perrin trace une ligne du temps au tableau. "
          "« Commençons par 19 h. Alex ? »", [
            R("Raconter précisément l'anamnèse, y compris ce qui n'a pas été demandé, noté ou "
              "transmis.", 3, "cc3 pb3 ic1"),
            R("« J'ai fait l'anamnèse. Le patient a dit qu'il n'avait pas d'allergie. »",
              2, "cc-1 pb-2"),
            R("« Je préfère que le Dr Neuhaus commence. Il était responsable de l'entrée. »",
              4, "ic-2 pb-2"),
            R("« Je commence. Et j'aimerais que Fatou puisse parler après moi. »", 3, "cc2 ic2 pb1"),
            R("« Je n'étais qu'étudiant·e, je ne vois pas ce que je peux apporter. »", 4, "pb-2 ic-2"),
        ]),
        I(2, "fatou", "sad",
          "Fatou, qui n'avait pas prévu de parler, parle. « La dame m'a dit, à moi, en "
          "partant. Pour la pénicilline. » Silence autour de la table. Nathalie Perrin : "
          "« Alex, est-ce que c'est venu dans votre anamnèse ? »", [
            R("« Je ne suis pas allé·e au bout de la question. C'est ma part. »", 3, "pb3 er1 cc1"),
            R("« Non. Le patient a dit non. »", 3, "pb-2 cc-1"),
            R("« Merci, Fatou. » Puis : « Non, je ne suis pas allé·e au bout. »", 3, "pb3 ic2"),
            R("« Fatou aurait pu le dire à quelqu'un d'autre. »", 3, "ic-3 rd-2"),
        ]),
        I(3, "kevin", "sad",
          "Neuhaus reconnaît avoir signé l'entrée sans la relire : vingt-quatre patients et "
          "un infarctus. Puis c'est au tour de Kevin. « J'ai demandé s'il avait des "
          "allergies. On m'a dit non. J'ai branché. » Quelqu'un, au bout de la table, "
          "demande pourquoi il n'a pas vérifié lui-même auprès du patient. Tous les regards "
          "vont vers Kevin.", [
            R("« Kevin a posé la bonne question et a reçu une mauvaise réponse — celle du "
              "dossier, donc la mienne. Le problème est arrivé avant la poche. »",
              5, "ic3 pb2 em1 er1 rd1"),
            R("Se taire.", 6, "ic-1"),
            R("« Il aurait pu vérifier le bracelet. »", 6, "ic-3 pb-2 rd-1 cc-1"),
            R("Regarder Kevin : « Moi, j'avais eu les informations avant toi. »", 5, "pb2 ic2"),
        ]),
        I(4, "moreau", "cold-anger",
          "Dr Moreau lève les yeux. « Chacun parle de sa part. Commencez par la vôtre. »", [
            R("Raconter précisément l'anamnèse, y compris ce qui n'a pas été demandé, noté ou "
              "transmis.", 3, "cc2 pb2"),
            R("« J'ai fait l'anamnèse. Le patient a dit non. »", 2, "cc-1 pb-2"),
            R("« D'accord. Ma part, c'est l'anamnèse. »", 3, "pb2 cc1"),
            R("« Je préfère écouter d'abord. »", 2, "pb-2 ic-1"),
        ]),
        I(5, "perrin", "neutral",
          "Nathalie Perrin écrit au tableau : « Allergie recopiée d'une lettre de 2019 » — "
          "« Question posée fermée à un patient fébrile » — « Information de la famille à "
          "une ASSC sans chemin vers le dossier » — « Entrée signée sans relecture » — "
          "« Un assistant pour vingt-quatre patients ». « Qu'est-ce qui aurait pu arrêter la "
          "chaîne, selon vous ? »", [
            R("« Un champ allergie vérifié avec le patient et un proche à l'entrée, une "
              "question aux ASSC à chaque relève, la relecture de l'entrée avant toute "
              "première prescription, et pas d'étudiant·e en deuxième nuit d'affilée. »",
              7, "cc3 ic3 pb1"),
            R("« Plus de vigilance de la part de chacun. »", 7, "cc-1"),
            R("« Que les étudiants ne fassent plus d'entrées. »", 7, "ic-1 cc0"),
            R("« Que les infirmiers vérifient eux-mêmes les allergies avant de brancher. »",
              7, "ic-3 pb-1"),
            R("« Qu'on demande à chaque famille, à l'entrée : « Y a-t-il quelque chose qu'on doit absolument savoir ? » »", 7, "cc2 rd2 ic1"),
        ]),
        I(6, "ines", "cold-anger",
          "Inès Rey pose son stylo. « Kevin a demandé. On lui a répondu. Il n'y avait pas de "
          "bracelet parce qu'il n'y avait rien dans le dossier. » Elle se tourne vers vous. "
          "« Vous ne dites rien ? »", [
            R("« Si. Kevin n'est pas le problème. Le problème est arrivé avant lui. »",
              5, "ic2 pb2"),
            R("« Ce n'est pas à moi de juger. »", 5, "ic-2 pb-1"),
            R("« Vous avez raison. Kevin a fait son travail. »", 5, "ic2 pb1"),
            R("« Chacun est responsable de ce qu'il fait. »", 5, "ic-2 em-2"),
        ]),
        I(7, "perrin", "neutral",
          "« Dernier facteur. » Nathalie Perrin se tourne vers la salle. « La fatigue. Qui "
          "avait dormi combien, avant cette nuit-là ? » Neuhaus rit jaune. Kevin répond : "
          "« Douzième nuit du mois. » Puis on vous regarde.", [
            R("Donner ses heures de sommeil exactes, même si ça expose.", 8, "pb2 er2 cc1"),
            R("« Ça n'a rien à voir. »", 8, "pb-1 er-1"),
            R("« Deuxième nuit d'affilée. Je le dis pour que ça change, pas pour m'excuser. »", 8, "pb2 er2"),
            R("« Je ne vois pas le rapport. »", 8, "pb-2 er-1"),
        ]),
        I(8, "narr", "",
          "Deux heures. Au tableau, onze facteurs. Aucun nom. Kevin est sorti le premier, "
          "sans dire au revoir.", [
            R("Le rattraper dans l'escalier.", 9, "ic2 em2"),
            R("Rester pour parler à Nathalie Perrin.", 10, "ic1"),
            R("Partir sans parler à personne.", 10, "ic-2 er-1"),
            R("Aller voir Fatou, restée seule à la table.", 10, "ic2 rd1"),
        ]),
        I(9, "kevin", "sad",
          "Il est assis sur une marche, entre deux étages. « On m'a mis en congé. « Pour me "
          "protéger. » » Il regarde ses mains. « J'ai deux gamins, et je ne dors plus. Je "
          "vois la poche. » Il lève les yeux. « Tu le savais, toi ? Pour l'allergie ? »", [
            R("« Je n'ai pas fait ce qu'il fallait pour le savoir. Je suis désolé·e que ce "
              "soit retombé sur toi. »", 11, "pb2 em2 co2 er1 ic1"),
            R("« Non. »", 11, "cc-1 em-1"),
            R("« On est tous dans le même bateau. »", 11, "em-1"),
            R("S'asseoir sur la marche à côté de lui.", 11, "em2 co2"),
        ]),
        I(10, "perrin", "neutral",
          "Nathalie Perrin range ses feutres. « Vous vouliez me dire quelque chose ? »", [
            R("« Kevin est seul avec ça depuis dix jours. Est-ce que quelqu'un s'occupe de "
              "lui ? »", 12, "ic3 em2"),
            R("« Est-ce que je vais avoir des problèmes ? »", 12, "er-1"),
            R("« Merci pour la séance. Ça m'a fait du bien qu'il n'y ait aucun nom au tableau. »", 12, "ic2 er1"),
            R("« Vous allez me retirer de mon stage ? »", 12, "er-2"),
        ]),
        I(11, "kevin", "sad",
          "« Tu sais ce qui me tue ? » Kevin se relève. « Personne ne m'a appelé. Dix ans "
          "ici. Personne. »", [
            R("« Moi, je t'appelle. Et je demande à Moreau et Perrin qu'on te propose le soutien "
              "pour les soignants impliqués. Tu n'as pas à porter ça seul. »",
              END, "ic3 co2 em1"),
            R("« Ça va aller. »", END, "em-1 co-1"),
            R("« Tu devrais voir un psy. »", END, "em-1"),
            R("« Moi aussi, j'aurais dû t'appeler. Je t'appelle ce soir. »", -1, "ic2 co2 pb1"),
        ]),
        I(12, "perrin", "neutral",
          "« Il existe un programme de soutien pour les soignants impliqués dans un "
          "incident. Kevin ne l'a pas activé. » Elle vous regarde. « Vous pouvez lui en "
          "parler ? Et vous, vous l'avez activé ? »", [
            R("« Je lui en parle aujourd'hui. Et oui, je vais l'activer pour moi aussi. »",
              END, "ic2 er2"),
            R("« Moi, ça va. »", END, "er-2"),
            R("« Oui. Et je l'accompagne au premier rendez-vous s'il veut. »", -1, "ic2 co2"),
            R("« Ce n'est pas mon rôle de m'occuper de lui. »", -1, "ic-2 em-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.4 Me Dufaux
# ---------------------------------------------------------------------------
_INTRO_64 = (
    "Cinq semaines après la nuit du 14. Salle de réunion de la direction. Me Claire "
    "Dufaux, avocate de la famille, a demandé à vous entendre. M. Rochat est à votre "
    "gauche. Olivier Jaquier est assis au fond, les bras croisés. Il y a un "
    "enregistreur sur la table."
)
S6_4E = S(7, "6.4 Me Dufaux",
    _INTRO_64,
    focus=("pb", "cc", "er", "rd"),
    slot="6.4",
    cond=ERREUR,
    entries=[
        Entry(2, when(all=["dossier_modifie"]), _INTRO_64),
        Entry(3, when(all=["nuits_enchainees"]), _INTRO_64),
    ],
    debriefs=[
        Debrief(when(all=["dossier_modifie"]), tone="hard", lead=(
            "L'avocate a commencé par la ligne de 6 h 47. Tout ce que vous avez dit ensuite a "
            "été entendu à travers elle. Une erreur de soin se comprend ; une pièce réécrite "
            "après coup, beaucoup moins.")),
    ],
    nodes=[
        I(1, "dufaux", "neutral",
          "« Merci d'être venu·e. Je ne suis pas là pour vous piéger. Je veux comprendre, "
          "heure par heure. » Me Dufaux ouvre un carnet. « 19 h 10. Qui vous a demandé de "
          "faire l'entrée de M. Jaquier, et qui devait la relire ? »", [
            R("« Le Dr Neuhaus m'a demandé de faire l'anamnèse, le status et l'entrée. Il "
              "devait la relire et la signer. »", 4, "cc3 pb2"),
            R("« Le Dr Neuhaus m'a laissé·e seul·e avec ça. »", 5, "ic-2 pb-1"),
            R("« Je ne me souviens plus très bien. »", 6, "pb-2 cc-2"),
            R("« Le Dr Neuhaus. Et c'est moi qui ai posé les questions au patient. »", 4, "cc2 pb2"),
            R("« Je ne répondrai qu'en présence de mon propre avocat. »", 8, "er-1 cc-1"),
        ]),
        I(2, "dufaux", "neutral",
          "« J'ai reçu l'historique complet du dossier. » Me Dufaux pose la feuille entre "
          "vous. « La ligne « allergies » a été modifiée à 6 h 47, par votre identifiant. "
          "Après les faits. » Elle attend. « Pourquoi ? »", [
            R("« Parce que j'ai eu peur. C'était une faute, et je ne cherche pas à "
              "l'excuser. »", 4, "pb3 er2 cc2 rd1"),
            R("« Pour compléter l'information. »", 7, "pb-3 cc-3 rd-1"),
            R("« Je refuse de répondre à cette question. »", 8, "pb-1 er-1"),
            R("« Je l'ai modifiée, et l'hôpital l'a signalé. Je peux vous dire pourquoi. »", 4, "pb3 cc2"),
            R("« C'était une simple mise à jour. »", 7, "pb-3 cc-3"),
        ]),
        I(3, "dufaux", "neutral",
          "« Le planning indique que vous étiez de garde la nuit du 13 aussi. » Me Dufaux "
          "ne lève pas les yeux de son carnet. « Combien d'heures aviez-vous dormi, le 14, "
          "avant de reprendre votre garde ? »", [
            R("« Quatre heures. J'avais accepté d'échanger une garde avec un collègue. Je "
              "n'aurais pas dû, et personne ne me l'a interdit. »", 4, "pb3 cc2 er1"),
            R("« Assez. »", 6, "pb-2 cc-2"),
            R("« Ça ne regarde que moi. »", 6, "pb-2 er-2"),
            R("« Peu. Moins de cinq heures, je crois. »", 4, "pb2 cc1"),
        ]),
        I(4, "dufaux", "neutral",
          "« Mme Jaquier affirme qu'elle a parlé de la pénicilline le soir même. » Me Dufaux "
          "vous regarde enfin. « Est-ce vrai ? »", [
            R("« Elle en a parlé ce soir-là, oui. Je ne suis pas allé·e au bout de la "
              "question, et l'information n'est pas arrivée au prescripteur. »",
              9, "pb3 cc3"),
            R("« Je ne m'en souviens pas. »", 6, "pb-2 cc-2"),
            R("« Le patient, lui, avait répondu non. »", 10, "pb-1 rd-1"),
            R("« Oui. Elle avait raison, et je ne l'ai pas assez écoutée. »", 9, "pb3 rd2"),
            R("« C'est ce qu'elle dit. »", 6, "pb-2 rd-2"),
        ]),
        I(5, "rochat", "neutral",
          "M. Rochat pose la main sur la table. « Tenez-vous à ce que vous avez vu et fait. » "
          "Me Dufaux sourit à peine. « Je note que l'étudiant·e met en cause son "
          "superviseur. »", [
            R("« Pardon. Le Dr Neuhaus devait relire l'entrée ; il avait vingt-quatre "
              "patients. Moi, je devais la faire complètement. »", 4, "pb2 cc2 ic1"),
            R("« Je dis ce qui s'est passé. »", 4, "pb-1 ic-1"),
            R("« Je ne mets personne en cause. Je dis ce que chacun devait faire, moi compris. »", 4, "pb2 ic2"),
            R("« Oui, il aurait dû relire. »", 4, "ic-3 pb-1"),
        ]),
        I(6, "dufaux", "cold-anger",
          "« « Je ne me souviens plus. » » Me Dufaux feuillette. « Vous avez rédigé une note "
          "à 7 h le matin même. Très précise. Voulez-vous qu'on la relise ensemble ? »", [
            R("« Oui. Pardon. Je réponds. »", 4, "pb2 er1"),
            R("« Je n'ai rien à ajouter. »", 11, "pb-2 cc-1"),
            R("« Oui, relisons-la. »", 4, "pb2 cc1"),
            R("« Ma note dit tout, je n'ai rien à rajouter. »", 11, "pb-2 cc-1"),
        ]),
        I(7, "dufaux", "cold-anger",
          "« Compléter. » Me Dufaux répète le mot. « À 6 h 47. Sans mention de la date de la "
          "correction. Ce qui laisse croire que c'était écrit à 19 h 40. » Un temps. « Vous "
          "comprenez ce que vous êtes en train de me dire ? »", [
            R("« Oui. Je retire. Je l'ai modifiée par peur. »", 4, "pb2 er1"),
            R("« Je maintiens. »", 11, "pb-3 cc-3 er-1"),
            R("« Oui. Je l'ai réécrite par peur, et c'était une faute. »", 4, "pb3 er1"),
            R("« Tout le monde modifie ses notes. »", 11, "pb-3 cc-3"),
        ]),
        I(8, "rochat", "neutral",
          "« Vous en avez le droit », dit M. Rochat. Me Dufaux acquiesce. « C'est votre droit. "
          "Je le note. Le Ministère public posera la même question. »", [
            R("« Je vais répondre. J'ai eu peur, j'ai modifié la ligne. »", 4, "pb2 er1"),
            R("Se taire.", 11, "pb-1"),
            R("« Je préfère répondre maintenant. »", 4, "pb2 er1"),
            R("« Je répondrai au Ministère public, pas à vous. »", 11, "pb-1 er-1"),
        ]),
        I(9, "dufaux", "neutral",
          "Me Dufaux referme son carnet. Sa voix change. « Dernière question, et elle n'est "
          "pas juridique. Mme Jaquier m'a demandé de vous la poser. » Un temps. « Est-ce que "
          "vous pensez à lui ? »", [
            R("« Tous les jours. À chaque anamnèse, quand j'arrive à la ligne "
              "« allergies ». »", 12, "co3 er2 rd1 em1"),
            R("« Je ne sais pas quoi répondre à ça. »", 12, "er0"),
            R("« Je préfère ne pas répondre. »", 12, "co-1 er-1"),
            R("« Je voudrais lui écrire, si elle le veut bien. »", 12, "co2 rd1"),
        ]),
        I(10, "dufaux", "neutral",
          "« Selon votre propre note, M. Jaquier avait 39,2 de fièvre et il était confus. » "
          "Me Dufaux vous regarde. « Vous avez pris sa réponse pour argent comptant ? »", [
            R("« Oui. Je n'aurais pas dû. »", 9, "pb2 cc1 er1"),
            R("« Il était capable de répondre. »", 11, "pb-2"),
            R("« Non. J'aurais dû appeler sa femme. »", 9, "pb3 cc1"),
            R("« C'était son dossier, pas le mien. »", 11, "pb-3 ic-2"),
        ]),
        I(11, "narr", "",
          "Me Dufaux vous remercie et range son carnet. Dans le couloir, M. Rochat ne dit "
          "rien. Deux semaines plus tard, le Ministère public ouvre une instruction. Le "
          "procès-verbal de cette rencontre y est joint.", []),
        I(12, "olivier", "neutral",
          "Olivier se lève. Il s'arrête devant vous. « Je voulais que vous soyez un monstre. "
          "Ça aurait été plus simple. » Il cherche ses mots. « Vous n'en êtes pas un. C'est "
          "pire. »", [
            R("« Je comprends. Je suis désolé·e. »", END, "co2 er1"),
            R("Soutenir son regard, sans rien dire.", END, "er2 rd1"),
            R("« Je faisais mon travail, c'est tout. »", END, "co-2 er-1"),
            R("« Vous avez le droit de m'en vouloir. »", -1, "er2 rd1"),
        ]),
    ],
)

# ===========================================================================
# Scène commune
# ===========================================================================

# ---------------------------------------------------------------------------
# 6.5 Un appel
# ---------------------------------------------------------------------------
_INTRO_65 = (
    "Huitième semaine, dernier jeudi de stage. 18 h 20, vestiaire. Votre téléphone sonne : "
    "un numéro fixe que vous ne connaissez pas."
)
S6_5 = S(9, "6.5 Un appel",
    _INTRO_65,
    focus=("co", "em", "er", "pb"),
    slot="6.5",
    entries=[
        Entry(1, ERREUR,
              "Huitième semaine. Le jour même de la revue d'incident. 18 h 20, vestiaire. "
              "Votre téléphone sonne : un numéro fixe que vous ne connaissez pas."),
    ],
    nodes=[
        I(1, "sofia", "sad",
          "« Alex ? C'est Sofia Haddad. » Un silence. « Je ne sais pas si vous vous souvenez "
          "de moi. » Sa voix est calme, fatiguée. « Maman est morte dimanche. Dans la chaise "
          "du jardin. Sous le cerisier. Comme elle l'avait écrit. »", [
            R("« Je me souviens très bien. Je suis désolé·e, Sofia. Et je suis heureux·se "
              "qu'elle ait pu être là où elle le voulait. »", 2, "co3 em2 rd2"),
            R("« Oh… Mes condoléances. »", 2, "co1"),
            R("« Comment avez-vous eu ce numéro ? »", 3, "pb1 co-2 em-1"),
            R("Un silence. Puis : « Merci de m'avoir appelé·e pour me le dire. »", 2, "co2 em1"),
            R("« Ah. On s'y attendait. »", 2, "co-3 em-2"),
        ]),
        I(2, "sofia", "grateful",
          "« Les derniers jours, elle a beaucoup parlé. De papa. De moi. Elle m'a dit que je "
          "n'avais rien fait de mal, il y a six ans. Que c'était le médecin, pas moi. » Elle "
          "respire. « Elle voulait que je vous dise une chose. Ses mots : « Merci de ne pas "
          "m'avoir menti. » »", [
            R("« Merci de me le transmettre. Et vous, comment allez-vous ? »", 4, "em3 co2 er1"),
            R("« C'était une femme exceptionnelle. »", 4, "co1"),
            R("« C'est toute l'équipe qu'il faut remercier. »", 4, "ic2 co0 em-1"),
            R("« Vous savez, je faisais juste mon travail. »", 4, "co-2 em-1"),
            R("Se taire un moment, ému·e. « Merci, Sofia. »", 4, "co2 er1"),
        ]),
        I(3, "sofia", "neutral",
          "« Par le secrétariat du service. » Elle hésite. « Je… je voulais juste vous le "
          "dire. Pardon de vous déranger. »", [
            R("« Vous ne me dérangez pas. Pardon, je vous écoute. »", 2, "co2 er1"),
            R("« Ce n'est pas grave. Dites-moi. »", 2, "co1"),
            R("« Je suis content·e que vous l'ayez fait. »", 2, "co2 rd1"),
            R("« Normalement, ce numéro ne devrait pas être donné. »", 2, "pb1 co-2 em-1"),
        ]),
        I(4, "sofia", "neutral",
          "« Moi ? » Un petit rire mouillé. « Je suis restée avec elle. Toute la nuit. Pas "
          "comme avec papa. » Un temps. « Et vous ? Vous avez une voix fatiguée. »", [
            R("« C'est une période difficile au travail. Mais votre appel compte beaucoup, "
              "justement cette semaine. »", 5, "er2 pb2 co1"),
            R("Lui raconter tout ce qui se passe à l'hôpital en ce moment.", 6, "pb-3 er-2 rd-2"),
            R("« Ça va très bien. »", 5, "er-1"),
            R("« Un peu. Mais parlez-moi de vous : c'est pour ça que vous appelez. »", 5, "pb2 em2"),
            R("« Vous n'avez pas à vous inquiéter pour moi. »", 5, "pb1 em-1"),
        ]),
        I(5, "sofia", "neutral",
          "« On fait une petite cérémonie samedi, dans le jardin. Rien de religieux, "
          "maman n'aurait pas voulu. Juste la chaise, et ses élèves qui viennent. » Elle "
          "hésite. « Vous viendriez ? »", [
            R("« Merci de m'inviter. Je ne pense pas que ce soit ma place, mais je penserai à "
              "elle samedi — sous un cerisier ou ailleurs. »", 7, "pb3 co2"),
            R("« Oui, bien sûr, je viendrai. »", 7, "pb-1 co2"),
            R("« C'est interdit, je ne peux pas. »", 7, "pb1 co-2 cc-1"),
            R("« Je ne pourrai pas venir. Est-ce que je peux vous envoyer quelques mots, que vous lirez si vous voulez ? »", 7, "pb2 co2"),
            R("« Je viendrai, et je dirai un petit mot sur ce qu'elle m'a appris. »", 7, "pb-2 co1"),
        ]),
        I(6, "sofia", "confused",
          "Un long silence au bout du fil. « Je… je ne savais pas. » Elle ne sait plus quoi "
          "dire. « Je suis désolée pour vous. »", [
            R("« Pardon. Je n'aurais pas dû vous raconter ça. Parlez-moi plutôt de votre "
              "mère. »", 5, "pb2 er1"),
            R("« Merci. Ça fait du bien d'en parler. »", 5, "pb-2 er-1"),
            R("« Merci. Parlons plutôt d'elle. Comment était-elle, ces derniers jours ? »", 5, "pb2 em2"),
            R("« Et en plus, personne ne me soutient, là-bas. »", 5, "pb-3 er-2"),
        ]),
        I(7, "narr", "",
          "Elle raccroche. Vous restez un moment assis·e sur le banc du vestiaire, le "
          "téléphone dans la main. Dans le couloir, quelqu'un rit. Vous pensez à une chaise "
          "sous un cerisier, et à une institutrice qui détestait qu'on la prenne pour une "
          "idiote.", []),
    ],
)

# ---------------------------------------------------------------------------
# 6.6 Trois mois plus tard (voie erreur)
# ---------------------------------------------------------------------------
S6_6E = S(10, "6.6 Trois mois plus tard",
    "Septembre. Votre stage est fini depuis trois mois. Mme Jaquier a demandé, par "
    "l'intermédiaire de Nathalie Perrin, à vous rencontrer. Sans avocat. Cafétéria de "
    "l'hôpital, 10 h. Elle a posé une petite boîte en carton sur la table.",
    focus=("co", "er", "rd"),
    slot="6.6",
    cond=ERREUR,
    entries=[
        Entry(1, when(all=["deces"])),
        Entry(10, when(all=["survie"]),
              "Septembre. Votre stage est fini depuis trois mois. M. Jaquier a demandé à vous "
              "voir. Il est en réadaptation, dans une clinique au-dessus du lac. Salle de "
              "physiothérapie, 14 h. Il est en fauteuil roulant."),
    ],
    nodes=[
        # --- Décès : Monique -----------------------------------------------------
        I(1, "monique", "neutral",
          "« Merci d'être venu·e. » Elle tourne sa tasse sans boire. « La procédure continue. "
          "Olivier y tient. Moi, je ne sais plus. »", [
            R("« Je suis venu·e parce que vous l'avez demandé. Je vous écoute. »", 2, "rd2 em2"),
            R("« Je ne suis pas sûr·e d'avoir le droit de vous parler, avec la "
              "procédure. »", 3, "pb1 em-1"),
            R("« Est-ce que vous allez retirer la plainte ? »", 4, "pb-3 rd-3 co-1"),
            R("S'asseoir en face d'elle, sans rien dire, et attendre.", 2, "rd2 em1 er1"),
            R("« J'espère que vous n'êtes pas venue pour m'accuser. »", 4, "er-2 rd-2"),
        ]),
        I(2, "monique", "neutral",
          "« Je voulais vous voir sans les avocats. Pour vous dire une chose, et vous en "
          "demander une. » Elle vous regarde. « La chose : je ne vous pardonne pas. Pas "
          "encore. Peut-être jamais. » Un temps. « La question : qu'est-ce que vous avez "
          "changé ? »", [
            R("« Je ne vous demande pas de pardonner. Ce que j'ai changé : je ne passe plus la "
              "ligne « allergies » sans la poser à voix haute, au patient et à un proche. Et à "
              "chaque relève, je demande aux soignants ce qu'ils ont entendu que je n'ai pas "
              "entendu. »", 5, "co2 cc3 pb2 rd2"),
            R("« Tout. Je ne suis plus la même personne. »", 5, "er0 cc-1"),
            R("« L'hôpital a changé ses procédures. »", 5, "ic1 pb-1 cc-1"),
            R("« Vous devriez peut-être essayer de pardonner. Pour vous. »", 5, "rd-3 co-2 pb-2"),
            R("« Je n'ai pas le droit de vous demander de pardonner. Ce que j'ai changé, c'est ma façon d'écouter les familles. »", 5, "co1 cc2 pb1 rd1"),
        ]),
        I(3, "monique", "neutral",
          "« M. Rochat m'a dit que vous pouviez me parler, tant qu'on ne parle pas de la "
          "procédure. » Elle pousse la boîte vers le milieu de la table. « Je ne veux pas "
          "parler de la procédure. »", [
            R("« Alors je vous écoute. »", 2, "rd2 em1"),
            R("S'asseoir. « Je vous écoute. »", 2, "rd2 em1"),
            R("« Je dois quand même faire attention à ce que je dis. »", 2, "em-1"),
            R("« Merci d'avoir demandé à me voir. »", 2, "rd1 co1"),
        ]),
        I(4, "monique", "cold-anger",
          "Elle retire la main de la boîte. « C'est pour ça que vous êtes venu·e. » Elle se "
          "lève à moitié.", [
            R("« Non. Pardon. C'était une question lâche. Je suis venu·e parce que vous l'avez "
              "demandé. »", 2, "pb2 er1 rd1"),
            R("La laisser partir.", 20, "co-2 rd-1"),
            R("« Restez, s'il vous plaît. Je voulais surtout vous écouter. »", 2, "em2 rd2"),
            R("« Si vous le prenez comme ça. »", 20, "er-3 co-2"),
        ]),
        I(5, "monique", "sad",
          "Elle ouvre la boîte. Une montre à gousset, un cadran blanc, « CFF » en lettres "
          "rouges. « Il la remontait tous les matins. Depuis qu'il est mort, c'est moi qui la "
          "remonte. Je ne sais pas pourquoi. » Elle la tient dans sa paume. « Je voulais que "
          "vous la voyiez. »", [
            R("La regarder longtemps. « Merci de me l'avoir montrée. »", 20, "co3 rd2"),
            R("« Elle est belle. »", 20, "co1"),
            R("« Je ne sais pas quoi dire. »", 20, "er0"),
            R("« Il faudrait peut-être la ranger, pour avancer. »", 20, "co-2 rd-2"),
            R("« Il la remontait pour ne jamais être en retard. Vous la remontez pour ne pas le laisser partir. »", 20, "em3 co2"),
        ]),

        # --- Survie : Roland -----------------------------------------------------
        I(10, "roland", "neutral",
          "« Alors c'est vous. » Il vous détaille. « Monique m'a raconté. Moi, je ne me "
          "souviens de rien après la piqûre. Neuf jours de trou. »", [
            R("« Oui, c'est moi qui ai fait votre entrée. Je voulais vous le dire en face : je "
              "suis désolé·e. »", 11, "pb3 rd2 co1"),
            R("« Comment allez-vous ? »", 11, "em1"),
            R("« Vous avez l'air d'aller beaucoup mieux ! »", 12, "em-1 co-1"),
            R("S'asseoir à sa hauteur. « Oui. Je suis venu·e vous demander pardon. »", 11, "pb2 rd2 co1"),
            R("« Je voulais voir si vous alliez mieux, pour me rassurer. »", 12, "pb-2 em-2"),
        ]),
        I(11, "roland", "cold-anger",
          "« Désolé·e. Tout le monde est désolé. » Il frappe les accoudoirs du plat des mains. "
          "« Je marchais dix kilomètres par jour. Maintenant je fais le tour de la salle avec "
          "un déambulateur, et on m'applaudit. » Puis, plus bas : « Vous voulez savoir le "
          "pire ? C'est moi qui ai dit que c'était rien. Trente ans que je dis que c'était "
          "rien. »", [
            R("« Vous avez dit ce que vous pensiez. C'était à moi de poser la question jusqu'au "
              "bout, et d'écouter votre femme. Ce n'est pas vous qui deviez le savoir. »",
              13, "pb3 co2 em2 rd2"),
            R("Se taire, et rester.", 13, "er1 co1"),
            R("« C'est vrai que vous auriez dû le dire. »", 14, "rd-2 em-2 pb-1"),
            R("« Vous marchiez dix kilomètres. Qu'est-ce qui vous manque le plus ? »", 13, "em3 co1"),
        ]),
        I(12, "roland", "cold-anger",
          "« Mieux ? » Il regarde ses jambes sous la couverture. « Mieux que mort, oui. »", [
            R("« Pardon. Ce n'était pas à moi de le dire. Je suis venu·e vous dire que je suis "
              "désolé·e. »", 11, "er2 pb1"),
            R("« Je voulais dire que vous progressez. »", 11, "em-2 er-1"),
            R("Se taire, et baisser les yeux.", 11, "er1"),
            R("« Vous pourriez être content d'être vivant. »", 11, "em-3 co-2"),
        ]),
        I(13, "roland", "neutral",
          "« Les kinés disent que je remarcherai. Peut-être sans canne. Au printemps. » Il se "
          "tait un moment. « L'avocate d'Olivier voulait que je dise que vous étiez "
          "incompétent·e. Je lui ai dit que vous étiez fatigué·e et mal entouré·e. Elle "
          "n'était pas contente. »", [
            R("« Merci. Mais je ne veux pas qu'on me protège : dites ce que vous pensez "
              "vraiment. C'est votre droit. »", 20, "pb3 er1"),
            R("« Merci, vraiment. »", 20, "co1"),
            R("« Elle a raison d'être en colère, Olivier aussi. »", 20, "em2 rd1"),
            R("« Votre fils a le droit d'être en colère. Moi, je veux que vous sachiez que je n'oublie pas. »", 20, "em2 co2 pb1"),
        ]),
        I(14, "monique", "cold-anger",
          "Mme Jaquier, qui arrivait avec deux cafés, s'arrête net. « Roland a passé trente "
          "ans à minimiser. Vous, vous deviez le savoir. » Elle pose les gobelets sans vous en "
          "tendre un.", [
            R("« Vous avez raison. Pardon, M. Jaquier. C'était à moi de poser la question. »",
              13, "pb2 er1 rd1"),
            R("« Je disais juste que… »", 13, "pb-1 er-1"),
            R("« Vous avez raison, madame. C'était à moi de savoir. »", 13, "pb2 rd2"),
            R("« Il faut aussi que les patients disent les choses. »", 13, "rd-3 pb-2"),
        ]),

        # --- L'évaluation de fin de stage (commune aux deux variantes) --------------
        I(20, "moreau", "neutral",
          "Plus tard, bureau de Dr Moreau. Votre évaluation de stage, repoussée de trois mois "
          "« pour qu'on la fasse à froid ». « Huit semaines. Une annonce, un pacte de silence, "
          "deux consultations sans diagnostic, un décès, une nuit. Et une procédure en cours. » "
          "Moreau pose son stylo. « Vous voulez encore faire ce métier ? »", [
            R("« Oui. Pas malgré ce qui s'est passé — avec. Je veux être le médecin qui pose la "
              "question jusqu'au bout. »", 21, "er3 pb2"),
            R("« Je ne sais plus. »", 22, "er1"),
            R("« Oui. Et je veux oublier cette histoire. »", 23, "er-2 pb-1"),
            R("« Je ne sais pas. Mais je sais quel médecin je ne veux pas être. »", 21, "er2 pb1"),
            R("« Si l'hôpital me laisse continuer. »", 22, "er-1 pb-1"),
        ]),
        I(21, "moreau", "neutral",
          "« Alors je vais écrire ce que j'ai vu. L'annonce à M. Ferreira. Mme Haddad. Et la "
          "nuit du 14. » Un temps. « Qu'est-ce que vous voulez que j'écrive sur la nuit du "
          "14 ? »", [
            R("« La vérité. Ce que j'ai fait, ce que je n'ai pas fait, et ce que j'ai dit "
              "après. »", 24, "pb3 cc2"),
            R("« Rien, si c'est possible. »", 24, "pb-2"),
            R("« Que j'ai dit la vérité après. Et ce qu'il m'en a coûté de ne pas l'avoir cherchée avant. »", 24, "pb3 er2"),
            R("« Que c'était une erreur collective. »", 24, "pb-2 cc-1"),
        ]),
        I(22, "moreau", "neutral",
          "« C'est une réponse honnête. Beaucoup de gens bien se posent la question à ce "
          "moment-là. » Dr Moreau vous regarde. « La psychologue du personnel, vous l'avez "
          "appelée ? »", [
            R("« Oui. Je la vois tous les quinze jours. »", 21, "er2 ic1"),
            R("« Pas encore. »", 21, "er0"),
            R("« Pas encore. Je l'appelle cette semaine. »", 21, "er2"),
            R("« Je n'en ai pas besoin. »", 21, "er-2"),
        ]),
        I(23, "moreau", "cold-anger",
          "« Vous n'oublierez pas. » Ce n'est pas une menace. « Et c'est tant mieux, si vous "
          "en faites quelque chose. »", [
            R("« Vous avez raison. »", 21, "er1"),
            R("« J'en ferai quelque chose. »", 21, "er2 pb1"),
            R("« On verra. »", 21, "er-2"),
            R("« J'espère bien. »", 21, "er1"),
        ]),
        I(24, "narr", "",
          "En sortant, vous passez devant la chambre 304. Un nouveau patient, une nouvelle "
          "famille, un sac de pharmacie posé sur une chaise. Sur l'écran du couloir, le champ "
          "« allergies » est devenu obligatoire : il clignote en rouge tant qu'il n'a pas été "
          "vérifié avec le patient et un proche. Sous le formulaire, une nouvelle case : "
          "« Ce que la famille a dit aux soignant·e·s ».", []),
    ],
)

# ===========================================================================
# Voie ÉVITÉE
# ===========================================================================

# ---------------------------------------------------------------------------
# 6.1 La déclaration
# ---------------------------------------------------------------------------
_INTRO_61N = (
    "Septième semaine, lundi. Bureau de Nathalie Perrin, responsable de la sécurité des "
    "patients, au rez-de-chaussée. Elle a imprimé la déclaration de quasi-incident de la "
    "nuit du 14."
)
S6_1N = S(2, "6.1 La déclaration",
    _INTRO_61N,
    focus=("ic", "pb", "er"),
    slot="6.1",
    cond=EVITE,
    entries=[
        Entry(1, when(all=["cirs_declare"]), _INTRO_61N),
        Entry(2, when(none=["cirs_declare"]),
              "Septième semaine, lundi. Bureau de Nathalie Perrin, responsable de la sécurité "
              "des patients. Kevin Da Silva a déclaré seul le quasi-incident de la nuit du 14. "
              "Votre nom y figure comme témoin."),
    ],
    nodes=[
        I(1, "perrin", "neutral",
          "« Merci pour la déclaration. » Nathalie Perrin sourit. « Vous êtes le premier "
          "étudiant, la première étudiante, à en cosigner une cette année. » Elle croise les "
          "mains. « Racontez-moi, sans vous juger. »", [
            R("Raconter la soirée dans l'ordre : l'anamnèse, la relève, 2 h 10, la poche.",
              3, "cc3 pb2"),
            R("« C'est surtout Kevin qui l'a faite. »", 3, "ic1 cc0"),
            R("« Je veux que ça ne retombe sur personne. »", 3, "pb1 cc-1"),
            R("« Je préfère ne pas revenir là-dessus. C'est fini. »", 4, "pb-2 cc-1"),
            R("« Je l'ai faite avec Kevin. Et c'est Fatou qui avait tout entendu. »", 3, "ic3 cc1"),
        ]),
        I(2, "perrin", "neutral",
          "« Kevin a déclaré le quasi-incident de la nuit du 14. Votre nom y figure comme "
          "témoin. » Elle vous regarde sans reproche. « Vous ne l'avez pas déclaré vous-même. "
          "Pourquoi ? »", [
            R("« Le Dr Neuhaus m'a demandé de ne pas le faire, et j'ai eu peur de le mettre en "
              "difficulté. Je n'aurais pas dû. »", 3, "pb2 er1 cc2"),
            R("« Il ne s'était rien passé. »", 4, "pb-2"),
            R("« Je ne savais pas comment faire. »", 3, "cc0 pb-1"),
            R("« Parce que je n'ai pas eu le courage. C'est aussi pour ça que je suis là aujourd'hui. »", 3, "pb3 er2"),
            R("« C'est Kevin qui aurait dû me le rappeler. »", 4, "ic-3 pb-1"),
        ]),
        I(3, "perrin", "neutral",
          "« Alors reprenons la chaîne. » Elle dessine des maillons sur une feuille. « Qu'est-"
          "ce qui a fait que ça a failli arriver ? »", [
            R("« Une allergie recopiée d'une vieille lettre, une question posée trop vite à un "
              "patient fébrile, une ASSC à qui personne ne demandait rien, une entrée signée "
              "sans relecture, un assistant pour vingt-quatre patients. Et moi au milieu. »",
              5, "cc3 ic2 pb2"),
            R("« Moi. J'ai mal fait l'anamnèse. »", 6, "cc1 er-1"),
            R("« Le Dr Neuhaus a prescrit trop vite. »", 7, "ic-2 pb-1"),
            R("« Tout le monde a fait un peu défaut, moi le premier : c'est justement ce qui est inquiétant. »", 5, "cc2 ic2 pb1"),
        ]),
        I(4, "perrin", "cold-anger",
          "« Il ne s'est rien passé pour M. Jaquier. » Elle ne hausse pas le ton. « Pour le "
          "prochain patient, on ne sait pas. C'est à lui que sert une déclaration. »", [
            R("« Vous avez raison. Je ne l'avais pas vu comme ça. »", 3, "pb2 er1"),
            R("« Je comprends. »", 3, "pb-1 cc-1"),
            R("« Alors écrivons-la ensemble, maintenant. »", 3, "pb2 ic2"),
            R("« Il y a des choses plus importantes. »", 3, "pb-3 cc-1"),
        ]),
        I(5, "neuhaus", "cold-anger",
          "La porte s'ouvre. Neuhaus, convoqué juste après vous, s'arrête en vous voyant. "
          "« Ah. C'est toi. » Il ne s'assoit pas. « Tu m'as balancé. »", [
            R("« Non. Ton nom n'est nulle part. J'ai écrit que tu avais vingt-quatre patients "
              "et un infarctus. C'est ça, le problème. »", 8, "pb2 ic3 er1"),
            R("« Tu as prescrit sans vérifier, c'est un fait. »", 9, "ic-2 er-1"),
            R("« Désolé·e, je ne voulais pas. »", 9, "er0 pb-1"),
            R("« Je ne t'ai pas balancé. Si tu veux, on la relit ensemble. »", 8, "pb2 ic2 er1"),
            R("« Tu aurais préféré qu'il meure ? »", 9, "er-3 ic-3"),
        ]),
        I(6, "perrin", "neutral",
          "« Votre part existe. Elle n'est pas la seule. » Nathalie Perrin repose son stylo. "
          "« Si on s'arrête à « l'étudiant·e a mal fait », on ne change rien, et le prochain "
          "étudiant fera la même chose. »", [
            R("« Alors : l'allergie recopiée, la question fermée, l'ASSC qu'on n'écoute pas, "
              "l'entrée non relue, la charge de nuit. »", 5, "cc2 ic2"),
            R("« Alors je vais écrire toute la chaîne, pas seulement mon maillon. »", 5, "cc2 ic2"),
            R("« Ça me soulage d'entendre ça. »", 5, "er1"),
            R("« Alors ce n'est pas vraiment ma faute. »", 5, "pb-2 er-1"),
        ]),
        I(7, "perrin", "neutral",
          "« Il a prescrit à 2 h avec l'information qu'il avait. » Nathalie Perrin vous "
          "regarde. « Pourquoi est-ce qu'il ne l'avait pas ? »", [
            R("« Parce que je ne la lui avais pas transmise. »", 5, "pb2 er1"),
            R("« Parce qu'il n'a pas relu l'entrée. »", 5, "ic-2 pb-1"),
            R("« Parce que personne ne la lui avait transmise, à commencer par moi. »", 5, "pb3 ic1"),
            R("« Ce n'est pas mon problème. »", 5, "pb-3 ic-2"),
        ]),
        I(8, "neuhaus", "resigned",
          "Neuhaus reste debout un moment. « Vingt-quatre patients. Ouais. » Il s'assoit enfin. "
          "« Tu sais que j'ai failli arrêter, l'hiver passé ? »", [
            R("« Non. Tu veux en parler ? »", 10, "em3 ic1"),
            R("« On est tous crevés. »", 10, "em-1"),
            R("S'asseoir à côté de lui, et attendre qu'il continue.", 10, "em2 co1"),
            R("« Tout le monde y pense. »", 10, "em-2"),
        ]),
        I(9, "neuhaus", "cold-anger",
          "« Super. Merci. » Neuhaus ressort. Nathalie Perrin soupire. « Il reviendra. Il est "
          "épuisé, pas méchant. »", [
            R("« Je vais aller lui parler. »", 10, "ic2 em1"),
            R("« Tant pis pour lui. »", 10, "ic-2 em-2"),
            R("« Il a raison d'être fâché. Je lui dirai pourquoi je l'ai fait. »", 10, "ic2 em1 er1"),
            R("« Il n'avait qu'à relire. »", 10, "ic-3 em-1"),
        ]),
        I(10, "perrin", "neutral",
          "« La direction veut rendre le champ allergie obligatoire, vérifié avec le patient "
          "et un proche. Et créer une place dans le dossier pour ce que les ASSC entendent. » "
          "Elle vous tend une feuille. « Vous voulez faire partie du groupe de travail ? »", [
            R("« Oui. Et je propose qu'on y invite Fatou Diallo. »", END, "ic3 rd2"),
            R("« Oui. »", END, "ic1"),
            R("« Je n'ai pas le temps. »", END, "ic-2"),
            R("« Oui. Et je propose qu'on demande aussi l'avis des infirmiers de nuit. »", -1, "ic3 cc1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.2 Kevin
# ---------------------------------------------------------------------------
S6_2N = S(4, "6.2 Kevin",
    "Septième semaine, mercredi, 7 h 30. Parc de l'hôpital, derrière le bâtiment des "
    "urgences. Kevin sort de sa nuit. Il fume, lui qui avait arrêté depuis trois ans.",
    focus=("em", "ic", "er"),
    slot="6.2",
    cond=EVITE,
    nodes=[
        I(1, "kevin", "sad",
          "« J'ai recommencé. Depuis la nuit du 14. » Il regarde la cigarette comme si elle "
          "appartenait à quelqu'un d'autre. « Je la vois, la poche. Sur la tubulure. Dix ans "
          "de nuits, et c'est la première fois que j'ai peur de venir travailler. »", [
            R("« Moi aussi, je repense aux dix minutes. Tu en as parlé à quelqu'un ? »",
              2, "em3 ic1 er1 co2"),
            R("« Il ne s'est rien passé, Kevin. »", 3, "em-2"),
            R("« Tu devrais arrêter la cigarette. »", 3, "em-2 rd-1"),
            R("S'asseoir sur le banc à côté de lui, sans rien dire.", 2, "em2 co2"),
            R("« Tu vas en parler toute ta vie, d'une poche ? »", 3, "em-3 rd-2"),
        ]),
        I(2, "kevin", "neutral",
          "« Ma femme. Elle dit de changer de service. Ou d'arrêter. » Il écrase la cigarette. "
          "« Douze nuits ce mois-ci. Une collègue en arrêt, pas remplacée. »", [
            R("« Douze nuits, c'est un fait qu'on peut dire à la revue. Ce n'est pas toi qui "
              "es fragile, c'est le planning. »", 4, "ic2 em2 cc1"),
            R("« Tu devrais peut-être changer, oui. »", 4, "em0 ic-1"),
            R("« Tout le monde fait des nuits. »", 3, "em-2"),
            R("« Qu'est-ce qui t'aiderait à revenir sans avoir peur ? »", 4, "em3 ic1"),
        ]),
        I(3, "kevin", "cold-anger",
          "« Rien ne s'est passé. Ouais. » Il a un rire sans joie. « C'est ce que dit Neuhaus "
          "aussi. »", [
            R("« Pardon. C'est faux : il s'est passé quelque chose, même s'il n'y a pas eu de "
              "dommage. Et ça pèse. »", 2, "em2 er1"),
            R("Partir.", 6, "em-2 ic-1"),
            R("« Neuhaus a tort. Ça compte, ce qui a failli arriver. »", 2, "em2 ic1"),
            R("« Il n'a pas tort. »", 6, "em-3 ic-1"),
        ]),
        I(4, "kevin", "anxious",
          "« Tu crois que je devrais le dire, à la revue ? Les douze nuits ? » Il secoue la "
          "tête. « On va dire que je me plains. »", [
            R("« Oui. Et je le dirai avec toi si tu veux. Ce n'est pas se plaindre, c'est "
              "expliquer comment une poche arrive sur une tubulure. »", 5, "ic3 pb2"),
            R("« C'est à toi de voir. »", 5, "ic-1"),
            R("« Ce n'est pas te plaindre. Tu protèges la prochaine équipe de nuit. »", 5, "ic2 em2"),
            R("« Tu risques de te faire mal voir, je te préviens. »", 5, "ic-2 pb-1"),
        ]),
        I(5, "kevin", "neutral",
          "« Tu sais ce qui m'aiderait ? » Il enfonce les mains dans ses poches. « Que les "
          "médecins arrêtent de dire « c'est l'infirmier qui a branché » quand ça se passe "
          "mal. »", [
            R("« Je ne le dirai jamais. Et si je l'entends, je répondrai. »", 7, "ic3 rd1"),
            R("« Je ne peux pas parler pour les autres. »", 7, "ic-1"),
            R("« Je te promets de ne jamais le dire. Et de rappeler que c'est toi qui as arrêté la poche. »", 7, "ic3 rd1"),
            R("« C'est quand même toi qui branches. »", 7, "ic-3 rd-2"),
        ]),
        I(6, "narr", "",
          "Vous rentrez dormir. La semaine suivante, Kevin n'est pas sur le planning : arrêt "
          "maladie. Personne ne sait pour combien de temps.", []),
        I(7, "kevin", "neutral",
          "« Perrin m'a parlé d'un programme de soutien pour les soignants impliqués. » Il "
          "hésite. « Tu crois que c'est pour les gens comme moi ? Même quand personne n'est "
          "mort ? »", [
            R("« Oui. Surtout. Je t'accompagne au premier rendez-vous si tu veux. »",
              END, "ic2 co2 em1"),
            R("« Je ne sais pas. »", END, "cc-1"),
            R("« Oui. Et j'y vais aussi, moi. »", -1, "ic2 er2"),
            R("« C'est surtout pour ceux qui ont tué quelqu'un. »", -1, "em-3 co-2"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.3 La revue
# ---------------------------------------------------------------------------
S6_3N = S(6, "6.3 La revue",
    "Huitième semaine. Revue de morbidité, salle de colloque. Un seul cas à l'ordre du "
    "jour : « Quasi-incident — pénicilline, chambre 304 ». Autour de la table : Nathalie "
    "Perrin, Dr Moreau, Dre Keller, Dr Neuhaus, Inès Rey, Kevin, Fatou.",
    focus=("ic", "cc", "pb"),
    slot="6.3",
    cond=EVITE,
    nodes=[
        I(1, "perrin", "neutral",
          "« Personne n'a été blessé, et c'est pour ça qu'on peut parler librement. » "
          "Nathalie Perrin se tourne vers vous. « Alex, vous commencez ? »", [
            R("Raconter la soirée entière, y compris ce qui n'a pas été fait à 19 h.",
              2, "cc3 pb3"),
            R("« Heureusement, j'ai vérifié à 2 h. »", 3, "ic-2 pb-1"),
            R("« Je préfère que Kevin commence. »", 2, "ic-1 er-1"),
            R("« Je commence par ce que je n'ai pas fait. »", 2, "pb3 cc1"),
            R("« Il n'y a pas grand-chose à dire, il ne s'est rien passé. »", 3, "pb-2 cc-2"),
        ]),
        I(2, "keller", "cold-anger",
          "Dre Keller lève la main. « Sincèrement ? On mobilise huit personnes pendant une "
          "heure pour une poche qui n'a pas été branchée ? »", [
            R("« Justement parce qu'elle n'a pas été branchée. Les mêmes causes, une autre "
              "nuit, donnent un décès. C'est moins cher d'apprendre maintenant. »",
              4, "pb2 cc3 ic2"),
            R("« Vous avez peut-être raison. »", 4, "pb-2"),
            R("« Vous diriez ça si c'était votre père ? »", 5, "er-2 ic-1"),
            R("« Parce que la prochaine fois, ce ne sera peut-être pas une poche arrêtée à temps. »", 4, "cc2 pb1"),
        ]),
        I(3, "kevin", "cold-anger",
          "Kevin ne lève pas les yeux. « Tu as vérifié à 2 h. Et à 19 h ? »", [
            R("« Tu as raison. À 19 h, je ne suis pas allé·e au bout. »", 2, "pb2 er2"),
            R("« Je n'étais pas le seul à pouvoir vérifier. »", 2, "ic-1 er-1"),
            R("« À 19 h, j'ai écrit un point d'interrogation. C'est ça qu'on doit comprendre. »", 2, "pb3 cc2"),
            R("« Tu cherches un coupable ? »", 2, "er-2 ic-2"),
        ]),
        I(4, "fatou", "neutral",
          "Inès se tourne vers Fatou : « Vous voulez dire quelque chose ? » Fatou hésite. "
          "« La dame m'avait parlé de la pénicilline. Mais je ne savais pas à qui le dire. » "
          "Elle regarde la table. « Personne ne me demande jamais. »", [
            R("« C'est le cœur du problème. Je propose qu'à chaque relève, on demande "
              "systématiquement aux ASSC ce qu'ils ont entendu des familles. »",
              6, "ic3 rd2 cc1"),
            R("« Merci, Fatou. »", 6, "ic1 rd1"),
            R("« Vous auriez pu le noter quelque part. »", 7, "ic-3 rd-2"),
            R("« Fatou, qu'est-ce qui vous aurait aidée à le dire ? »", 6, "ic3 rd2"),
        ]),
        I(5, "moreau", "cold-anger",
          "Dr Moreau pose son stylo. « Alex. On ne gagne pas un débat en culpabilisant un "
          "collègue. »", [
            R("« Pardon, Dre Keller. Ce que je voulais dire : la prochaine fois, les mêmes "
              "causes peuvent tuer. »", 4, "er2 ic1 cc1"),
            R("« C'était une vraie question. »", 4, "er-1 ic-1"),
            R("« Vous avez raison. Pardon, Dre Keller. »", 4, "er2 ic1"),
            R("« Je n'ai culpabilisé personne. »", 4, "er-2 ic-1"),
        ]),
        I(6, "perrin", "neutral",
          "« Des actions. Une proposition concrète chacun. » Nathalie Perrin écrit au tableau. "
          "« Alex ? »", [
            R("« Champ allergie vérifié avec le patient et un proche, et relecture de l'entrée "
              "par le médecin avant toute première prescription. »", 8, "cc3 ic2 pb1"),
            R("« Former les étudiants. »", 8, "cc0"),
            R("« Que les ASSC écrivent directement dans le dossier. »", 8, "ic1 cc1"),
            R("« Honnêtement ? Rien. Il ne s'est rien passé. »", 8, "pb-2 ic-2"),
            R("« Un bracelet allergie posé dès l'entrée, même en cas de doute. »", 8, "cc2 pb1"),
        ]),
        I(7, "ines", "cold-anger",
          "Inès Rey se redresse. « Noter où ? Elle n'a pas accès au dossier médical. »", [
            R("« Pardon, vous avez raison. Le problème, c'est qu'il n'existe pas de chemin. »",
              6, "ic2 er1"),
            R("« Alors il faut lui donner l'accès. »", 6, "ic0 cc1"),
            R("« Alors une question systématique, à la relève : « Qu'est-ce que les familles vous ont dit ? » »", 6, "ic3 cc1"),
            R("« Ce n'est pas à moi de gérer les accès. »", 6, "ic-2"),
        ]),
        I(8, "neuhaus", "resigned",
          "Neuhaus, qui n'avait rien dit : « Et la charge ? Un assistant pour vingt-quatre "
          "patients, la nuit ? » Dr Moreau : « Je porte ça à la direction. » Puis Nathalie "
          "Perrin vous regarde. « Vous voulez présenter ce cas à la journée sécurité des "
          "étudiants, en novembre ? »", [
            R("« Oui. Avec ce que j'ai mal fait, pas seulement ce que j'ai bien fait. »",
              END, "pb3 cc2"),
            R("« Je préfère que quelqu'un d'autre le fasse. »", END, "er0"),
            R("« Oui, pour montrer qu'un·e étudiant·e peut sauver un patient. »", END, "pb-1 ic-1"),
            R("« Oui, avec Kevin et Fatou, s'ils sont d'accord. »", -1, "ic3 pb1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.4 Jonas
# ---------------------------------------------------------------------------
S6_4N = S(8, "6.4 Jonas",
    "Huitième semaine, mardi, 18 h. Vestiaire. Jonas est assis sur le banc, en blouse, "
    "le téléphone à la main. Il ne s'est pas changé.",
    focus=("pb", "ic", "em"),
    slot="6.4",
    cond=EVITE,
    nodes=[
        I(1, "jonas", "anxious",
          "« J'ai fait une connerie. » Il parle vite. « Ce matin, les prélèvements. J'ai "
          "étiqueté les tubes du 310 et du 312 d'avance, au chariot. Le labo a appelé : "
          "groupe sanguin incompatible avec l'historique du 310. Ils refont. Personne n'a été "
          "transfusé. » Il vous regarde. « Personne ne sait que c'est moi. Tu ne dis rien, "
          "OK ? »", [
            R("« Ça arrive. Mais ça se déclare, Jonas. C'est exactement ce qui a sauvé M. "
              "Jaquier : quelqu'un a parlé. Tu veux qu'on le fasse ensemble ? »",
              2, "pb3 ic2 em2 er1"),
            R("« OK, je ne dis rien. »", 3, "pb-3 ic-2"),
            R("« Tu le déclares, sinon c'est moi qui le fais. »", 4, "pb2 em-2 ic-1"),
            R("« Tu as eu peur. Assieds-toi. Personne n'a été transfusé, c'est l'essentiel pour l'instant. »", 2, "em2 er1"),
            R("« Tu aurais dû faire attention, franchement. »", 3, "em-3 ic-1"),
        ]),
        I(2, "jonas", "ashamed",
          "« Tu sais ce qu'ils vont dire ? Que je suis nul. » Il se passe la main dans les "
          "cheveux. « Je voulais faire chirurgie. »", [
            R("« Ils vont dire que les tubes sont étiquetés d'avance au chariot, pas au lit "
              "devant le patient. C'est ça qu'on corrige. Pas toi. »", 5, "em2 cc2 ic2"),
            R("« Tu n'es pas nul. Tu as fait une erreur. »", 5, "em2"),
            R("« Il fallait faire attention. »", 5, "em-2"),
            R("« Les chirurgiens aussi déclarent leurs erreurs. Les bons, surtout. »", 5, "em2 pb2"),
        ]),
        I(3, "ines", "cold-anger",
          "Deux jours plus tard, Inès Rey vous arrête au desk. « Le labo a signalé deux tubes "
          "inversés au 310, mardi matin. Vous étiez de prélèvements avec Jonas. Vous savez "
          "quelque chose ? »", [
            R("« Oui. C'est Jonas, il me l'a dit. Il avait peur. J'aurais dû l'aider à le "
              "déclarer. »", 7, "pb2 er1 cc1"),
            R("« Non. »", 8, "pb-3 cc-3 ic-1"),
            R("« Je préfère que Jonas vous le dise lui-même. Je vais le chercher. »", 7, "ic2 pb2"),
            R("« Demandez au labo. »", 8, "pb-2 ic-2"),
        ]),
        I(4, "jonas", "angry",
          "« Sinon tu le fais ? » Jonas se lève. « Sympa. Depuis ta nuit du 14, tu donnes des "
          "leçons à tout le monde. »", [
            R("« Pardon, ce n'était pas une menace. Je ne te laisserai pas porter ça seul, mais "
              "je ne mentirai pas non plus. »", 2, "er2 em2 pb2"),
            R("« Fais comme tu veux. »", 3, "ic-2 pb-1"),
            R("« Tu as raison, ça ressemblait à une menace. Pardon. Qu'est-ce qui te fait le plus peur ? »", 2, "er2 em2"),
            R("« Si tu ne le fais pas, tu es un danger pour les patients. »", 3, "em-3 ic-2"),
        ]),
        I(5, "jonas", "neutral",
          "Il souffle. « OK. On le fait. » Il ouvre l'ordinateur du vestiaire. « Tu restes à "
          "côté pendant que je remplis ? »", [
            R("« Oui. »", 6, "ic2 co1"),
            R("« Je te dicte, ça ira plus vite. »", 6, "pb-2 ic-1"),
            R("« Oui. Et je témoigne que tu es venu me le dire. »", 6, "ic2 em1"),
            R("« Tu peux mettre que c'était un problème d'imprimante ? »", 6, "pb-3 cc-2"),
        ]),
        I(6, "ines", "neutral",
          "Le lendemain, Inès Rey vous arrête au desk. « Jonas a déclaré une inversion "
          "d'étiquettes. C'est rare, un étudiant qui déclare lui-même. » Elle vous regarde. "
          "« Vous y êtes pour quelque chose ? »", [
            R("« C'est lui qui l'a fait. Je suis juste resté·e à côté. »", END, "ic2 rd1"),
            R("« Oui, je l'ai convaincu. »", END, "ic-2 rd-1"),
            R("« Il a eu le courage. Moi, je l'ai juste écouté. »", -1, "ic2 em1"),
            R("« Il n'avait pas vraiment le choix. »", -1, "ic-2"),
        ]),
        I(7, "ines", "neutral",
          "Inès hoche la tête. « Merci. » Un temps. « La prochaine fois, aidez-le à le faire "
          "lui-même, avant que quelqu'un d'autre ne pose la question. C'est comme ça qu'on "
          "reste un collègue. »", [
            R("« Vous avez raison. Je vais le voir. »", END, "ic2 er1"),
            R("« Ce n'était pas à moi de le faire. »", END, "ic-1 pb-1"),
            R("« Merci de me le dire. Vous avez raison. »", -1, "ic2 er1"),
            R("« Je ne suis pas son babysitter. »", -1, "ic-3 em-2"),
        ]),
        I(8, "ines", "cold-anger",
          "« Le labo a les horaires de prélèvement et les identifiants de connexion. » Inès "
          "referme le classeur. « On saura. »", [
            R("« Attendez. C'est Jonas. Il avait peur. Moi aussi. »", 7, "pb1 er1"),
            R("« Je n'ai rien à dire. »", END, "pb-3 ic-2"),
            R("« Attendez. Je vais d'abord lui dire de venir vous voir lui-même. »", 7, "pb1 ic2"),
            R("« Vous n'avez qu'à chercher. »", -1, "pb-3 ic-3"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6.6 Fin de stage (voie évitée)
# ---------------------------------------------------------------------------
_INTRO_66N = (
    "Dernier jour de stage. Bureau de Dr Moreau, 17 h. L'évaluation de fin de stage. Sur le "
    "bureau, une enveloppe à votre nom, écrite à la main."
)
S6_6N = S(11, "6.6 Fin de stage",
    _INTRO_66N,
    focus=("er", "rd", "ic"),
    slot="6.6",
    cond=EVITE,
    entries=[
        Entry(2, when(all=["quasi_dit"]), _INTRO_66N),
    ],
    nodes=[
        I(1, "moreau", "neutral",
          "« Huit semaines. Une annonce, un pacte de silence, deux consultations sans "
          "diagnostic, un décès, et une nuit où il ne s'est rien passé. » Dr Moreau pose son "
          "stylo. « Qu'est-ce qui vous a le plus appris ? »", [
            R("« La nuit où il ne s'est rien passé. Parce que j'ai vu combien de fois ça "
              "aurait pu arriver. »", 3, "er2 pb2 cc1"),
            R("« M. Ferreira. Parce que c'était le premier. »", 3, "co2 er1"),
            R("« La policlinique. C'est là que j'ai fait le plus de diagnostics. »", 3, "er0 cc-1"),
            R("« Fatou. Elle m'a appris à demander. »", 3, "ic3 rd2"),
            R("« Rien de spécial. Tout s'est bien passé. »", 3, "er-2 pb-1"),
        ]),
        I(2, "moreau", "neutral",
          "Dr Moreau vous tend l'enveloppe. Une carte, l'écriture penchée de Mme Jaquier : "
          "« Merci de nous avoir dit la vérité sur la nuit du 14, même quand rien n'était "
          "arrivé. Roland a fait plastifier sa carte d'allergie. Il la montre à tout le "
          "monde. » Moreau attend que vous ayez fini. « Vous savez combien de familles "
          "apprennent qu'il y a eu un quasi-incident ? Presque aucune. »", [
            R("« Je ne savais pas si j'avais bien fait de le dire. »", 4, "er1 rd1"),
            R("« Merci de me l'avoir donnée. »", 1, "co1"),
            R("Lire la carte deux fois, et la ranger dans votre blouse.", 1, "co2 er1"),
            R("« C'est Kevin qui a tout fait. »", 1, "ic1 er-1"),
        ]),
        I(3, "moreau", "neutral",
          "« Et dans votre prochain stage, dès le premier jour, qu'est-ce que vous ferez "
          "différemment ? »", [
            R("« Je me présenterai aux infirmières et aux ASSC avant le tour, et je leur "
              "demanderai ce qu'elles ont entendu. Je poserai la question des allergies "
              "jusqu'au bout, au patient et à un proche. Et je dirai non à une deuxième "
              "nuit. »", 5, "cc3 ic3 pb2 er1"),
            R("« Je serai plus prudent·e. »", 5, "cc-1"),
            R("« Rien. Ça s'est bien passé. »", 5, "er-2 pb-1"),
            R("« Je demanderai à chaque relève : « Qu'est-ce que je n'ai pas entendu ? » »", 5, "ic3 cc2"),
        ]),
        I(4, "moreau", "neutral",
          "« Vous avez bien fait. » Dr Moreau range la carte dans l'enveloppe et vous la "
          "rend. « On ne dit pas la vérité aux patients seulement quand elle nous coûte "
          "peu. »", [
            R("« Je m'en souviendrai. »", 1, "er1"),
            R("« Merci. Je la garderai. »", 1, "co1 er1"),
            R("« Ça ne se reproduira plus, promis. »", 1, "pb-1"),
            R("« Je m'en souviendrai, surtout quand ça me coûtera. »", 1, "pb2 er1"),
        ]),
        I(5, "kevin", "neutral",
          "On frappe. Kevin, en civil. « Je passe de jour, au 2ᵉ étage, à partir de lundi. Je "
          "voulais te dire au revoir. » Il hausse les épaules. « Et merci pour la revue. »", [
            R("« Merci à toi, Kevin. Pour la poche, et pour le reste. »", 6, "ic2 co2"),
            R("« Bonne continuation. »", 6, "ic0"),
            R("« C'est surtout moi qui ai sauvé la situation, cette nuit-là. »", 6, "ic-2 pb-1"),
            R("« Tu vas me manquer, la nuit. Prends soin de toi. »", 6, "ic2 co2 em1"),
        ]),
        I(6, "narr", "",
          "En sortant, vous passez devant la chambre 304. Un nouveau patient, une nouvelle "
          "famille, un sac de pharmacie posé sur une chaise. Vous vous arrêtez une seconde "
          "devant la porte. Puis vous frappez.", []),
    ],
)

CH6 = C(6, "Ce qui reste",
    situation=(
        "Les semaines qui suivent la nuit du 14, et trois mois plus tard. Selon ce qui s'est "
        "passé cette nuit-là : une famille à rencontrer, une lettre d'avocate, une revue "
        "d'incident, un collègue suspendu — ou un quasi-accident qu'on choisit de déclarer, "
        "de dire, et d'analyser. Et, au milieu, un appel de Sofia Haddad."
    ),
    objectives=(
        "mener un entretien d'information après incident (reconnaître, présenter des "
        "excuses, ne pas spéculer, ne pas désigner de coupable), connaître ses droits et "
        "devoirs face à une procédure, ne jamais dissimuler ni réécrire, dire sa part dans "
        "une revue d'incident et défendre une culture juste, soutenir un collègue deuxième "
        "victime, déclarer et dire un quasi-incident, accompagner un pair qui a commis une "
        "erreur, garder une juste distance avec une famille endeuillée, et prendre soin de "
        "soi pour continuer."
    ),
    anchoring=(
        "UNIL M1.7 droit médical, assécurologie, éthique · UNIGE Master, disciplines "
        "transversales Médecine légale et éthique, enseignement interprofessionnel "
        "(sécurité des patients, culture juste)."
    ),
    focus=("pb", "er", "ic", "cc"),
    start_choice=StartChoice(
        unless_any=["erreur", "evite"],
        question=(
            "Ce chapitre raconte la suite de la nuit du 14 (chapitre 5), que vous n'avez pas "
            "jouée sur cet appareil. Quelle nuit voulez-vous que ce chapitre prolonge ?"
        ),
        options=[
            ("La nuit où M. Jaquier est mort d'un choc anaphylactique.",
             ["erreur", "deces", "aveu"]),
            ("La nuit où M. Jaquier a survécu à l'erreur, après neuf jours de réanimation.",
             ["erreur", "survie", "aveu"]),
            ("La nuit où l'erreur a été évitée de justesse.",
             ["evite", "cirs_declare"]),
        ],
    ),
    # Entrelacées : chaque voie joue ses scènes dans l'ordre des slots.
    scenes=[S6_1E, S6_1N, S6_2E, S6_2N, S6_3E, S6_3N, S6_4E, S6_4N, S6_5, S6_6E, S6_6N],
)
