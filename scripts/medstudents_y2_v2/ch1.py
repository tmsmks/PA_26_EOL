"""Chapitre 1 — Madame 14 (septembre-octobre).

Cinq scènes jouées (six avec l'histoire annexe), sept écrites :
  1.1 La salle froide · 1.2 La story · 1.3 Montchéry · 1.4 La ferme des Combettes
  1.5 branche parallèle : « La lettre » (la photo a circulé) ou « Le livre des donneurs »
  1.6 histoire annexe « 2 h 14 » (si Alex a soutenu Noah en 1.1)
Voir docs/MedStudents_Y2_v2_bible.md, §5.
"""
from __future__ import annotations

from .dsl import END, C, Debrief, Entry, I, R, S, go, when

# ---------------------------------------------------------------------------
# 1.1 La salle froide
# ---------------------------------------------------------------------------
S1_1 = S(1, "1.1 La salle froide",
    "Lundi de la deuxième semaine de septembre, 8 h. Sous-sol de l'institut d'anatomie. "
    "L'odeur du formol colle aux vêtements dès la porte. Vingt tables sous des draps "
    "blancs. Votre groupe, la table 14 : Noah, Maëlle, Yasmine, Léo — et vous. Personne "
    "ne parle.",
    focus=("rd", "er", "ic"),
    nodes=[
        I(1, "vautier", "neutral",
          "Une femme en blouse, cheveux gris coupés court, attend que le silence soit "
          "complet. « Hélène Vautier. Pendant deux semestres, ces personnes seront vos "
          "premières patientes et vos premiers patients. Elles ont choisi de vous donner "
          "leur corps. Pas leur nom, pas leur visage, pas leur histoire : leur corps. » Elle "
          "lève une feuille. « Avant de commencer, l'un ou l'une d'entre vous lit le texte "
          "des donneurs. À voix haute. »", [
            R("Lever la main, même si votre voix risque de trembler. « Je veux bien le "
              "lire. »", 2, "rd3 er1 cc1 ic1"),
            R("Rester immobile, et attendre que quelqu'un d'autre se propose.", 2, "rd1"),
            R("Glisser à Noah, à voix basse, pour détendre l'atmosphère : « On a le droit de "
              "rire après, ou c'est interdit aussi, comme les photos ? »", 3, "rd-2 pb-2 er-1"),
            R("Vérifier discrètement l'heure sur votre téléphone.", 3, "rd-2 pb-1"),
            R("« Est-ce que leurs familles savent ce qu'on fait ici, concrètement ? »",
              4, "rd2 cc1 em1"),
        ]),
        I(2, "narr", "",
          "Le texte tient en dix lignes. Il remercie « celles et ceux qui ont accepté d'être "
          "nos premiers maîtres, sans jamais nous entendre les remercier ». À la dernière "
          "ligne, la salle s'est tue d'une autre manière. La Pre Vautier replie la feuille. "
          "« Les règles, maintenant. Pas de photo. Pas de surnom : si vous avez besoin de "
          "parler d'elle ou de lui, dites le numéro de la table. Pas de plaisanterie sur la "
          "personne. Les signes particuliers — cicatrices, tatouages — sont couverts d'une "
          "compresse : vous ne la soulevez pas. Une famille reconnaît un tatouage. »",
          [go(5)]),
        I(3, "vautier", "cold-anger",
          "La Pre Vautier s'est arrêtée à votre hauteur. Elle ne hausse pas la voix ; c'est "
          "pire. « Vous avez quelque chose à partager avec la salle ? » Vingt-quatre paires "
          "d'yeux se tournent vers la table 14.", [
            R("« Non. Pardon. C'était déplacé, et je m'en suis rendu compte trop tard. »", 2, "rd2 er2 pb2"),
            R("« C'était pour détendre l'atmosphère. On est tous stressés. »", 2, "er1 pb-1 rd-1 ic-1"),
            R("Désigner Noah du menton : « On parlait de l'horaire. »",
              2, "pb-3 ic-2 rd-1 cc-1"),
            R("Baisser les yeux sans répondre.", 2, "er-1"),
            R("« Ce n'est qu'un corps, non ? »", 2, "rd-3 pb-3 em-2 co-1"),
        ]),
        I(4, "vautier", "neutral",
          "« Bonne question. » Elle vous regarde, vraiment, pour la première fois. « Les "
          "familles savent que le corps servira à l'enseignement. Elles ne savent pas qui l'a "
          "eu, ni ce qu'on y a appris. En juin, on les invite à une cérémonie. C'est là "
          "qu'elles l'apprennent, d'une certaine manière : par ce que vous en dites. » Elle "
          "vous tend la feuille. « Vous lisez ? »", [
            R("Prendre la feuille. « Oui. »", 2, "rd2 er1 ic1"),
            R("« Je préfère que quelqu'un d'autre lise. »", 2, "ic-1"),
            R("« Et si une famille n'aime pas ce qu'on dit, en juin ? »", 2, "cc1 rd1"),
            R("« On ne pourrait pas les rencontrer avant, les familles ? Ce serait plus "
              "humain, pour elles comme pour nous, de mettre un visage sur le corps. »",
              2, "rd-2 pb-2 em1"),
        ]),
        I(5, "narr", "",
          "La Pre Vautier retire le drap jusqu'aux épaules. Une femme, autour de quatre-vingts "
          "ans. Des mains fines, posées à plat. Du vernis rouge, écaillé sur deux ongles. Au "
          "poignet gauche, une compresse fixée par un sparadrap. Maëlle se penche vers vous : "
          "« Elle avait du style, Madame 14. » Yasmine a déjà enfilé ses gants. Léo relit le "
          "protocole en remuant les lèvres. Noah est très pâle.", [
            R("« Quelqu'un lui a fait les ongles. »", 6, "rd3 em2 er1"),
            R("Rire doucement : « Madame 14, ça lui va bien. »", 6, "rd-1 er1"),
            R("« Maëlle. Pas ici. »", 6, "rd2 pb1 ic-1"),
            R("Regarder Noah. « Ça va ? »", 7, "em2 co2 ic1"),
            R("Ouvrir l'atlas à la page du thorax et se plonger dans le protocole, pour ne "
              "plus avoir à la regarder.", 6, "er1 cc1 rd-1"),
            R("« Elle était vieille, au moins. C'est moins triste. »", 6, "rd-2 em-2 er-1"),
        ]),
        I(6, "vautier", "neutral",
          "« Table 14. Première incision : la paroi thoracique, de la fourchette sternale à "
          "l'appendice xiphoïde. » Elle dépose le scalpel sur un champ vert, au centre de la "
          "table. « Qui commence ? » Yasmine tend déjà la main. Noah s'est accroché au bord "
          "de la table, les jointures blanches.", [
            R("« Yasmine, vas-y : tu as l'expérience. Je lis le protocole et je tiens "
              "l'écarteur. »", 9, "ic3 cc1 er1"),
            R("Prendre le scalpel avant tout le monde. « Moi. J'ai besoin de ce geste, sinon "
              "je ne le ferai jamais : autant que ce soit tout de suite. »",
              9, "ic-2 rd-1 pb-1 er-1"),
            R("« Noah, t'es le fils du chirurgien : à toi l'honneur. »",
              9, "em-2 rd-1 ic-1 co-1"),
            R("Se glisser à côté de Noah, à voix basse : « T'es tout blanc. On sort deux "
              "minutes ? »",
              7, "em3 co2 ic1"),
            R("« On tire au sort ? »", 9, "ic1"),
        ]),
        I(7, "noah", "anxious",
          "Vous sortez avec Noah. Dans le couloir, il s'appuie contre le mur carrelé et "
          "respire par la bouche. « C'est l'odeur. » Un temps. « Mon père a fait sa première "
          "dissection à dix-neuf ans. Il raconte qu'il mangeait un sandwich au jambon à côté "
          "du corps. Il trouve ça drôle. » Il rit, mal. « Moi, je vais tomber dans les pommes "
          "devant tout le monde. »", [
            R("« Tu n'es pas ton père. On y retourne quand tu veux, ensemble. »", 8, "em3 co3 er1 ic1", sets=["noah_soutenu"]),
            R("« Respire. Ça passe en dix minutes. J'ai lu que le formol fait ça à un "
              "étudiant sur trois : c'est physiologique, ça n'a rien à voir avec toi ni avec "
              "ton père. »", 8, "em1 co1 cc-1"),
            R("« Si tu tombes dans les pommes devant une morte, imagine devant un vivant. »",
              9, "em-3 co-2 er-1"),
            R("« Tu devrais peut-être te demander si la médecine, c'est pour toi. »",
              9, "em-3 rd-2 co-2 pb-1"),
            R("« Je préviens la Pre Vautier ? Elle a sûrement vu ça cent fois. »",
              8, "ic2 em1 pb1", sets=["noah_soutenu"]),
            R("Lui tendre une pastille de menthe, et attendre avec lui sans rien dire.",
              8, "em2 co2", sets=["noah_soutenu"]),
        ]),
        I(8, "narr", "",
          "L'heure passe. Yasmine incise d'un geste sûr ; Léo tient l'écarteur ; vous lisez "
          "le protocole à voix haute. La peau, puis la graisse, jaune et dense, puis le "
          "muscle. Maëlle, qui s'ennuie, soulève du bout de la pince la compresse du "
          "poignet. « Attendez, elle a un tatouage ? » Une hirondelle bleue, un peu floue, "
          "de celles qu'on se faisait faire dans les ports. « Trop beau. » Elle sort son "
          "téléphone de la poche de sa blouse.", [
            R("Poser la main sur son téléphone. « Range-le. Et remets la compresse, "
              "maintenant. »",
              14, "rd3 pb3 ic1", sets=["maelle_avertie"]),
            R("« Maëlle… » Puis détourner les yeux, sans finir la phrase.", 14, "pb-1 er-1"),
            R("« Envoie-la-moi aussi, pour réviser. »", 14, "rd-3 pb-3 ic-1"),
            R("Lever la main pour appeler la Pre Vautier.", 11, "pb2 rd1 ic-1",
              sets=["maelle_avertie"]),
            R("Faire semblant de ne rien voir.", 14, "pb-2 rd-1"),
            R("« Une hirondelle… C'est beau. Mais remets la compresse, s'il te plaît. »", 14, "rd2 pb2 cc1 em1", sets=["maelle_avertie"]),
        ]),
        I(9, "narr", "",
          "Dix minutes plus tard, Noah glisse le long de la table comme un drap qu'on retire. "
          "Yasmine le rattrape par les aisselles avant que sa tête ne touche le carrelage. "
          "« Malaise vagal. Jambes en l'air ! » Des chaises raclent. Quelqu'un rit "
          "nerveusement, deux tables plus loin. La Pre Vautier traverse la salle sans "
          "courir.", [
            R("Lever les jambes de Noah pendant que Yasmine surveille sa respiration. "
              "« Laissez-lui de l'air. »", 10, "ic3 er2 cc2 co1", sets=["noah_soutenu"]),
            R("Envoyer Léo chercher de l'eau, et s'accroupir près de Noah.", 10, "ic2 em1 co2", sets=["noah_soutenu"]),
            R("Rester figé·e, le protocole à la main.", 10, "er-2 ic-1"),
            R("« Il nous fait un deuxième cadavre, la table 14 ! »", 10,
              "rd-3 em-3 er-1 pb-1 co-1"),
            R("Fixer, d'un regard dur, la table d'où vient le rire.", 10, "rd1 er1"),
        ]),
        I(10, "noah", "ashamed",
          "Noah est assis par terre, dos au mur, un gobelet d'eau dans les mains. Il ne "
          "regarde personne. « Tout le monde a vu. » Plus bas : « Mon père va le savoir. Il "
          "connaît la moitié des assistants d'ici. »", [
            R("« Ils ont vu que tu es humain. C'est tout. »",
              16, "em3 co2 er1 rd1", sets=["noah_soutenu"]),
            R("« Mais non, personne n'a rien vu, je t'assure : tout le monde était penché sur "
              "sa table, même la Pre Vautier regardait ailleurs à ce moment-là. »",
              16, "cc-2 em1"),
            R("« Ton père n'a pas besoin de le savoir. »", 16, "em1 cc-1"),
            R("« C'était un peu ridicule, mais bon. »", 16, "em-2 rd-1 co-2"),
            R("S'asseoir par terre à côté de lui, sans rien dire.", 16, "em2 co3 er1",
              sets=["noah_soutenu"]),
        ]),
        I(16, "yasmine", "annoyed",
          "Yasmine se relave les mains en grommelant. « Il n'a pas mangé, je parie. » Elle "
          "regarde Noah, assis contre le mur. « En ambulance, on avait un mot pour ceux qui "
          "tombaient au premier corps : les stagiaires. » Maëlle pouffe. Noah baisse la "
          "tête.", [
            R("« On a tous été stagiaires, toi aussi. »",
              8, "ic2 em2 rd1 er1"),
            R("Rire avec Maëlle.", 8, "rd-2 em-2 co-1 ic-1"),
            R("« Yasmine a raison, Noah : il fallait manger. »", 8, "em-2 co-1 cc1"),
            R("Ne rien dire à Yasmine, mais aller chercher pour Noah un sucre et un verre "
              "d'eau à la fontaine du couloir, en lui promettant que plus personne n'en "
              "parlera.", 8, "co2 em1 pb-1"),
            R("« Et toi, ta première fois, c'était comment ? »", 8, "em1 ic1 er1"),
        ]),
        I(11, "vautier", "cold-anger",
          "La Pre Vautier arrive en trois pas. Elle voit la compresse soulevée, le téléphone "
          "que Maëlle glisse trop tard dans sa poche. Elle remet elle-même la compresse et "
          "lisse le sparadrap du pouce. « Mademoiselle Dupasquier, nous nous parlerons à la "
          "fin de la séance. » Puis, à vous seul·e, à voix basse : « Merci. Ce n'est pas "
          "agréable, ce que vous venez de faire. C'était juste. »", [
            R("« Avec Maëlle, pas contre elle. »",
              14, "ic2 pb1 em1 co1"),
            R("« Je voulais juste qu'elle arrête. »", 14, "cc1"),
            R("« Ce n'est pas moi qui lui ai demandé de la soulever, je tiens à le dire : "
              "je lisais le protocole, je n'ai rien vu avant qu'elle sorte son téléphone. »",
              14, "ic-1 pb-1 er-1"),
            R("Ne rien répondre, et éviter le regard de Maëlle jusqu'à la fin de la séance.",
              14, "ic-1 er-1"),
        ]),
        I(12, "vautier", "neutral",
          "Fin de séance. La Pre Vautier passe derrière la table 14, vérifie du bout des "
          "doigts la compresse du poignet, et s'arrête. « Qu'est-ce qu'elle vous a appris, "
          "aujourd'hui ? » C'est à vous qu'elle pose la question.", [
            R("« Que quelqu'un a pris soin d'elle jusqu'au bout. Le vernis, sur ses "
              "ongles. »",
              13, "rd3 em2 cc1"),
            R("« Les trois plans de la paroi thoracique. »", 15, "cc1"),
            R("« Qu'il faut manger avant de descendre ici. »", 15, "er1 rd-1"),
            R("« Rien que je n'avais déjà vu dans l'atlas, pour être franc·he : les planches "
              "sont plus lisibles, on y voit mieux les plans. »", 15, "rd-2 er-1"),
            R("« Que j'ai eu peur, et que ça ne m'a pas empêché·e de rester. »",
              13, "er3 rd1 cc1"),
        ]),
        I(14, "yasmine", "neutral",
          "Une heure plus tard, Yasmine vous tend le scalpel : « À toi, le plan suivant. » La "
          "lame bute contre une côte. Une sueur froide vous coule dans le dos ; le carrelage "
          "se met à tanguer, doucement. Personne ne l'a remarqué. Pas encore.", [
            R("« Quelqu'un peut prendre le relais ? Je ne me sens pas bien, je préfère le "
              "dire avant de tomber. »",
              17, "er3 ic2 cc1"),
            R("Poser le scalpel, dire « Je sors une minute », et revenir après dix "
              "respirations.", 17, "er3 pb1 ic1"),
            R("Serrer les dents et continuer, la main qui tremble au-dessus du thorax.",
              17, "er-2 pb-1 rd-1"),
            R("Faire une blague bien fort sur l'odeur du formol, pour que personne ne "
              "remarque rien.",
              17, "er-1 rd-2"),
            R("Fixer les mains de Madame 14, respirer lentement, et reprendre quand le sol "
              "s'arrête de bouger.", 17, "er2 rd1"),
        ]),
        I(17, "leo", "vulnerable",
          "Léo prend doucement le scalpel de vos doigts et le pose sur le champ. Il parle "
          "bas, pour vous seul·e. « Bei mir war es der Geruch… Chez moi, c'était l'odeur, "
          "l'an dernier, à Zurich. » Il cherche ses mots. « Tu veux que je continue, et toi "
          "tu me lis le protocole ? »", [
            R("« Oui, merci, Léo. Je te lis le protocole, et tu me dis si je vais trop "
              "vite. »", 12, "er2 ic2 em1"),
            R("« Ça va, ça va. » Et reprendre le scalpel aussitôt.", 12, "er-1 ic-1"),
            R("« Tu peux parler français, Léo ? On ne comprend rien. »", 12, "rd-2 ic-2 em-2"),
            R("Lui sourire, et lui demander comment on dit « vertige » en allemand.",
              12, "ic1 em1 er1"),
        ]),
        I(13, "vautier", "neutral",
          "La Pre Vautier hoche la tête. « Ce que vous venez de dire, gardez-le. Vous en "
          "aurez besoin en juin. » Elle remonte le drap jusqu'au visage de Madame 14, "
          "lentement, comme on borde quelqu'un. Au vestiaire, tout le monde sent le formol. "
          "Maëlle rit trop fort. Noah se lave les mains pour la troisième fois. Yasmine est "
          "déjà partie."),
        I(15, "vautier", "neutral",
          "La Pre Vautier ne commente pas. « Revenez lundi avec une autre réponse. Elle sera "
          "encore là. » Elle remonte le drap jusqu'au visage de Madame 14, lentement, comme on "
          "borde quelqu'un. Au vestiaire, tout le monde sent le formol. Maëlle rit trop fort. "
          "Noah se lave les mains pour la troisième fois. Yasmine est déjà partie."),
    ],
)

# ---------------------------------------------------------------------------
# 1.2 La story
# ---------------------------------------------------------------------------
_INTRO_12 = (
    "Lundi, 22 h 07. Votre chambre, en colocation. Vos cheveux sentent encore le formol "
    "malgré deux shampoings. Le groupe WhatsApp « Table 14 » vibre sur la table de nuit."
)
_INTRO_12_AVERTIE = (
    "Lundi, 22 h 07. Votre chambre, en colocation. Vos cheveux sentent encore le formol "
    "malgré deux shampoings. Cet après-midi, Maëlle vous a juré qu'elle avait effacé la "
    "photo. Le groupe WhatsApp « Table 14 » vibre sur la table de nuit."
)

S1_2 = S(2, "1.2 La story", _INTRO_12,
    focus=("pb", "rd", "ic"),
    entries=[
        Entry(2, when(all=["maelle_avertie"]), _INTRO_12_AVERTIE),
    ],
    debriefs=[
        Debrief(when(all=["photo_virale"]), tone="hard", lead=(
            "La story a été vue, reprise et commentée par des milliers de personnes. Un "
            "tatouage suffit à reconnaître quelqu'un : c'est pour cela que les signes "
            "particuliers des donneuses et des donneurs sont couverts. Le don du corps repose "
            "sur une promesse d'anonymat faite à des gens qui ne pourront jamais se plaindre. "
            "Quand un·e camarade franchit cette limite, le geste utile est le plus simple : "
            "lui demander directement, vite et en privé, de retirer l'image — puis prévenir "
            "si elle reste en ligne.")),
        Debrief(when(all=["maelle_vautier"]), tone="good", lead=(
            "La story a disparu en une demi-heure, parce que vous l'avez demandé directement "
            "à Maëlle, sans l'humilier devant le groupe. Et vous irez voir la Pre Vautier "
            "ensemble : dire ce qui s'est passé, avant que quelqu'un d'autre le découvre, "
            "protège la donneuse, le programme — et Maëlle.")),
        Debrief(when(all=["photo_supprimee"]), tone="mixed", lead=(
            "La story a disparu en une demi-heure. Personne ne sait combien de gens l'ont "
            "vue, ni si quelqu'un l'a enregistrée. Retirer une image ne l'efface pas "
            "toujours : la responsable du programme est la seule à pouvoir vérifier, et "
            "prévenir si besoin.")),
    ],
    nodes=[
        I(1, "narr", "",
          "Une notification Instagram : Maëlle a publié une story. Elle, en blouse dans le "
          "vestiaire, langue tirée, avec la légende « Day 1 avec notre nouvelle coloc 💀 ». "
          "Dans le coin de l'image, floue mais lisible : une main posée sur un drap blanc, "
          "du vernis rouge, une hirondelle bleue au poignet. Maëlle a mille huit cents "
          "abonnés. Dans le groupe, Noah a écrit « euh maëlle ? », Léo « ? ». Yasmine n'a "
          "pas encore répondu.", [
            R("En privé : « Retire ta story, on voit le tatouage. Je t'appelle ? »", 3, "rd3 pb3 cc2 em1"),
            R("Écrire dans le groupe : « Maëlle, retire ça tout de suite. »",
              4, "pb2 rd1 cc1 em-1"),
            R("Liker la story. Tout le monde poste des trucs de la fac.",
              7, "rd-3 pb-3 ic-1"),
            R("Signaler la story à Instagram, anonymement, avec le motif « contenu "
              "choquant » : la plateforme saura quoi en faire, et Maëlle ne saura pas que "
              "c'est vous.", 6, "pb1 rd1 cc-1 ic-1"),
            R("Écrire tout de suite un mail à la Pre Vautier.", 5, "pb2 rd1 ic-1 em-1"),
            R("Poser le téléphone. Ce n'est pas votre story, et vous êtes épuisé·e.",
              7, "pb-2 rd-1 er1"),
        ]),
        I(2, "narr", "",
          "Une notification Instagram : Maëlle a publié une story. Elle, en blouse dans le "
          "vestiaire, langue tirée, avec la légende « Day 1 avec notre nouvelle coloc 💀 ». "
          "Dans le coin de l'image, floue mais lisible : une main posée sur un drap blanc, "
          "du vernis rouge, une hirondelle bleue au poignet. La photo qu'elle vous avait "
          "juré avoir effacée. Mille huit cents abonnés. Dans le groupe, Noah a écrit "
          "« euh maëlle ? ».", [
            R("Lui écrire en privé : « Tu m'avais dit que tu l'avais effacée. Retire-la, on "
              "voit le tatouage. Je t'appelle ? »", 3, "rd3 pb3 cc2 em1"),
            R("Écrire dans le groupe : « Maëlle, tu nous avais juré que tu l'avais effacée. "
              "Tu nous mens à tous, et maintenant c'est toute la table qui va payer pour "
              "toi. Retire ça. »", 4, "pb2 rd1 cc1 em-2 ic-1"),
            R("Liker la story. Après tout, c'est elle qui l'a gardée, pas vous.",
              7, "rd-3 pb-3 ic-1"),
            R("Écrire tout de suite un mail à la Pre Vautier.", 5, "pb2 rd1 ic-1 em-1"),
            R("L'appeler.", 10, "em1 cc1 ic1 co2"),
            R("Poser le téléphone. Vous l'aviez prévenue ; maintenant, c'est son problème.",
              7, "pb-2 rd-1 ic-1"),
        ]),
        I(3, "maelle", "annoyed",
          "Trois petits points, longtemps. Puis : « quoi ?? on voit rien c'est flou » « et "
          "c'est MA story » « t'es pas vautier »", [
            R("« On voit l'hirondelle. Sa famille la reconnaîtrait. Elle a donné son corps, "
              "pas son image. »", 8, "cc3 rd3 pb2"),
            R("« Tu veux que Vautier tombe dessus demain matin ? »", 8, "pb1 cc1 em-1"),
            R("« T'es vraiment débile. »", 7, "rd-2 em-2 ic-2"),
            R("« Je te demande juste de la retirer. Je ne dirai rien à personne. »",
              8, "pb-1 rd1 em1"),
            R("« Tu peux pas juste recadrer la photo ? »", 7, "pb-2 rd-2"),
            R("L'appeler.", 10, "em1 cc1 ic1 co2"),
        ]),
        I(4, "yasmine", "angry",
          "Yasmine répond dans le groupe, en majuscules : « T'ES SÉRIEUSE ? RETIRE ÇA AVANT "
          "QUE JE LE SIGNALE. » Noah : « elle a peut-être pas fait exprès ». Maëlle : « ok "
          "la police ». Une minute plus tard : « c'est bon je l'ai mise en amis proches ». "
          "Ses amis proches : trois cents personnes.", [
            R("« Amis proches, c'est encore trois cents personnes. Retire-la complètement. Je "
              "t'appelle. »", 10, "pb2 rd2 cc2 em1"),
            R("« Ok, c'est déjà mieux. »", 7, "pb-2 rd-1"),
            R("« Yasmine a raison, t'as aucune limite. »", 9, "ic-2 em-2 rd-1"),
            R("« On arrête de lui tomber dessus en groupe. Maëlle, je t'écris en privé. »",
              3, "ic2 em2 rd1"),
            R("Couper les notifications du groupe.", 7, "ic-2 pb-1 co-1"),
        ]),
        I(5, "narr", "",
          "Vous écrivez trois lignes à la Pre Vautier. Réponse automatique, immédiate : « Je "
          "lirai votre message demain dès 7 h 30. » La story, elle, a encore vingt-trois "
          "heures à vivre.", [
            R("Écrire aussi à Maëlle : « J'ai prévenu Vautier, mais ça ne suffit pas. Retire-"
              "la, s'il te plaît. »", 8, "pb2 rd2 cc1 em-1"),
            R("Attendre la réponse de la Pre Vautier.", 7, "pb-1 ic-1"),
            R("Appeler Maëlle, là, tout de suite, sans attendre.", 10, "em1 cc1 ic1 co2"),
            R("Écrire dans le groupe : « J'ai prévenu Vautier. »", 9, "ic-2 em-2 pb1"),
            R("Aller se coucher : le mail est parti, vous avez fait votre part, et la Pre "
              "Vautier saura mieux que vous ce qu'il faut faire demain matin.",
              7, "pb-1 er1 ic-1"),
        ]),
        I(6, "narr", "",
          "Instagram vous remercie : « Nous examinerons ce contenu. » Vous rafraîchissez la "
          "page toutes les cinq minutes. Au bout d'une heure, la story est toujours là.",
          [go(7)]),
        I(7, "narr", "",
          "23 h 41. Noah vous envoie un lien. Un compte de mèmes d'étudiants en médecine — "
          "douze mille abonnés — a repris la story de Maëlle, avec la légende « La vraie vie "
          "en 2e année 😂 ». Deux cents cœurs. Et un commentaire : « attendez c'est quoi ce "
          "tatouage, ma grand-mère avait le même ».", [
            R("Appeler Maëlle tout de suite, pour qu'elle écrive au compte, et prévenir "
              "la Pre Vautier dès 7 h 30.",
              13, "pb2 rd2 ic2 cc1", sets=["photo_virale"]),
            R("Commenter sous le mème : « Supprimez ça, c'est une donneuse. »",
              13, "rd1 pb-1 cc-1", sets=["photo_virale"]),
            R("Liker, et envoyer « mdrrr » à Noah.", 13, "rd-3 pb-3 em-2",
              sets=["photo_virale"]),
            R("Écrire poliment au compte de mèmes : « C'est une donneuse. Retirez-la, "
              "s'il vous plaît. »", 13, "pb1 rd2 cc1", sets=["photo_virale"]),
            R("Éteindre le téléphone. Demain est un autre jour.", 13, "pb-2 rd-1 er-1",
              sets=["photo_virale"]),
        ]),
        I(13, "noah", "anxious",
          "Minuit moins le quart. Noah appelle. Il chuchote, il a peur. « C'est notre table. "
          "C'est… elle. Si Vautier voit ça, on est tous virés. » Un temps. « Il faut qu'on se "
          "mette d'accord : on n'a rien vu, on ne savait rien. D'accord ? »", [
            R("« Non, Noah. On dira ce qu'on a vu. Mais là, aide-moi à joindre Maëlle. »",
              14, "pb3 ic2 cc1 er1"),
            R("« D'accord, on n'a rien vu. »", 14, "pb-3 cc-2 rd-1"),
            R("« Respire. Personne ne sera viré pour une story. Et ce n'est ni toi ni moi qui "
              "l'avons postée : on n'a rien à se reprocher, alors on dort, et on verra demain "
              "ce que dit Vautier. »", 14, "er1 pb-2 cc-1 co-1"),
            R("« Tu as raison d'avoir peur. Moi aussi. On ne se protège pas en mentant, "
              "c'est tout. »", 14, "em2 pb2 er1"),
            R("Raccrocher : vous n'avez pas la force.", 14, "em-2 ic-1 er-1"),
        ]),
        I(14, "maelle", "sad",
          "0 h 32. Maëlle répond enfin. « supprimée. mais le compte l'a gardée, ils répondent "
          "pas ». Puis : « je suis morte de honte. dis-moi que c'est pas si grave ».", [
            R("« C'est grave. Et tu n'es pas seule. Demain, on va voir Vautier. »", 18, "pb3 em1 cc2 co2"),
            R("« C'est pas si grave, ça va passer : dans deux jours, plus personne n'en "
              "parlera, tu sais comment sont ces comptes, une publication chasse l'autre. »",
              18, "cc-2 pb-2 em1"),
            R("« Tu aurais dû y penser avant. »", 18, "em-3 co-2 ic-1"),
            R("« Va dormir. On en reparle demain. »", 18, "em1 cc-1"),
            R("« Je ne sais pas. Écris au compte une deuxième fois, et à Instagram. »",
              18, "cc1 ic1"),
        ]),
        I(18, "narr", "",
          "Mardi, 7 h 25. Couloir de l'institut. La porte du bureau 112 est encore fermée ; "
          "la lumière, allumée. Sur votre téléphone, le mème a deux mille cœurs.", [
            R("Frapper à la porte du bureau 112, et tout raconter.",
              11, "pb3 rd2 ic2 er1"),
            R("Attendre Maëlle dans le couloir : c'est à elle d'y aller.", 11, "ic-1 pb-1"),
            R("Repartir. Si quelqu'un doit parler, ce sera Yasmine.", 11, "ic-2 pb-2 er-1"),
            R("Envoyer à la Pre Vautier un long mail avec le lien du mème et le détail de qui "
              "a fait quoi, minute par minute, pour que personne ne puisse dire que la "
              "table 14 a caché quelque chose.", 11, "pb1 cc1 ic-2 em-1"),
            R("Écrire au groupe : « J'y vais. Qui vient ? »", 11, "ic2 pb2 cc1"),
        ]),
        I(8, "maelle", "sad",
          "Long silence. Puis : « ok. supprimée. » Une minute plus tard : « tu me trouves "
          "horrible ? »", [
            R("« Non. Tu as fait une erreur, et tu viens de la réparer. Demain, on va voir "
              "Vautier ensemble ? »", 19, "em1 co1 pb3 rd2 ic2",
              sets=["photo_supprimee", "maelle_vautier"]),
            R("« Un peu, oui. »", 15, "em-2 rd-1 ic-1 co-1", sets=["photo_supprimee"]),
            R("« Non. On n'en parle plus, promis. »", 15, "em2 pb-1",
              sets=["photo_supprimee"]),
            R("« Non. Mais vérifie que personne ne l'a capturée. »", 15, "pb1 cc1 rd1", sets=["photo_supprimee"]),
            R("« Ça arrive à tout le monde. »", 15, "cc-1 pb-1 em1",
              sets=["photo_supprimee"]),
        ]),
        I(9, "maelle", "angry",
          "Maëlle quitte le groupe. Puis, en privé : « merci de m'avoir balancée devant tout "
          "le monde ». La story est toujours en ligne.", [
            R("« Pardon pour le groupe. Mais retire-la. »", 8, "pb2 em2 rd1 ic1 er1"),
            R("« Tu l'as cherché, Maëlle. Assume, maintenant. »", 7, "em-3 ic-2 co-1"),
            R("« C'est Vautier qui décidera de ce qui est grave, pas moi, et sûrement pas "
              "toi : moi, j'ai juste dit ce que tout le monde pensait dans le groupe. »",
              7, "ic-1 em-1 er-1"),
            R("L'appeler, sans attendre la suite.", 10, "em1 ic1 co2"),
            R("Ne pas répondre, et attendre qu'elle se calme.", 7, "ic-1 em-1"),
        ]),
        I(10, "maelle", "anxious",
          "Elle décroche à la première sonnerie. Sa voix est plus petite qu'en vrai. « Tu "
          "crois que j'ai fait un truc grave ? » Un temps. « Je poste tout, tu sais. Si j'en "
          "fais une blague, ça devient pas réel. Aujourd'hui, j'ai eu peur toute la "
          "journée. »", [
            R("« Je comprends que ce soit ta façon de tenir. Mais pas avec elle. Supprime-la, "
              "et demain on va voir Vautier ensemble. »", 19, "em2 pb3 rd2 ic2 cc1 co1",
              sets=["photo_supprimee", "maelle_vautier"]),
            R("« Supprime-la, et on n'en parle plus. »", 15, "pb1 rd1",
              sets=["photo_supprimee"]),
            R("« C'est pas si grave. Mais supprime quand même. »", 15, "rd-1 cc-1 pb1",
              sets=["photo_supprimee"]),
            R("« Moi aussi, j'ai eu peur toute la journée. Je ne raccroche pas : "
              "supprime-la pendant que je suis là. »", 15, "em3 er1 pb2 rd1", sets=["photo_supprimee"]),
            R("« Débrouille-toi avec ta conscience. »", 7, "em-3 ic-2 co-2"),
        ]),
        I(15, "narr", "",
          "22 h 51. La story a disparu. Maëlle a mis un cœur sous votre dernier message. "
          "Assis·e sur votre lit, vous regardez le plafond. Trois cent quarante personnes "
          "l'ont vue, disait l'application. Combien l'ont enregistrée ?", [
            R("Proposer à Maëlle d'aller voir Vautier demain.", 12, "pb3 ic2 rd1", sets=["maelle_vautier"]),
            R("Se dire que c'est réglé, et éteindre la lumière.", 12, "pb-1 er1"),
            R("Fouiller les comptes de mèmes pendant une heure pour vérifier que personne ne "
              "l'a reprise, en faisant des captures de tout ce que vous trouvez, au cas où il "
              "faudrait des preuves plus tard.", 12, "er-1 pb-1 rd-1"),
            R("Écrire dans le groupe : « C'est réglé, on n'en parle plus jamais. »",
              12, "pb-2 ic-1 cc-1"),
            R("Écrire à Noah, qui n'a plus rien dit depuis : « Ça va, toi ? »",
              12, "em2 co1 ic1"),
        ]),
        I(19, "maelle", "vulnerable",
          "« tu viendras vraiment avec moi demain ? » Puis : « et si elle me vire ? »", [
            R("« Je viendrai. C'est ce qui te protège. »", 12, "pb2 em2 cc2 co1"),
            R("« Elle ne te virera pas, ne t'inquiète pas pour ça. »", 12, "cc-1 em1"),
            R("« Si elle te vire, ce sera mérité. Tu savais très bien ce que tu faisais. "
              "»", 12, "em-3 co-2"),
            R("« Je viendrai, oui. Et si elle te vire, je dirai que j'étais d'accord pour la "
              "photo : comme ça, on sera deux à partager la sanction, et ça te fera moins "
              "peur. »", 12, "pb-3 cc-2 em1"),
            R("« Je ne sais pas. On verra demain. Essaie de dormir un peu. »", 12, "em-1"),
        ]),
        I(11, "narr", "",
          "À midi, le mème a disparu : la faculté a écrit au compte. Il a été vu trente mille "
          "fois. Sous la dernière capture que quelqu'un a gardée, le commentaire est toujours "
          "là : « ma grand-mère avait le même ». Quelqu'un a répondu : « envoie-lui en MP »."),
        I(12, "narr", "",
          "Vous mettez longtemps à vous endormir. L'odeur du formol est toujours là, sur "
          "l'oreiller. Avant d'éteindre, vous ouvrez une dernière fois le profil de Maëlle : "
          "il n'y a plus rien, qu'un selfie de l'été, au bord d'un lac."),
    ],
)

# ---------------------------------------------------------------------------
# 1.3 Montchéry
# ---------------------------------------------------------------------------
S1_3 = S(3, "1.3 Montchéry",
    "Jeudi, 13 h 30. Montchéry, mille quatre cents habitants au pied du Jura. Le cabinet de "
    "la Dre Golay occupe le rez-de-chaussée d'une ancienne ferme, entre la boulangerie et "
    "le Café de la Gare. Votre premier après-midi d'immersion en médecine de famille. Dans "
    "la salle d'attente : sept personnes, un chien et une odeur de café.",
    focus=("cc", "rd", "ic"),
    nodes=[
        I(1, "sandra", "anxious",
          "Derrière le comptoir, une femme d'une quarantaine d'années tient le téléphone "
          "entre l'épaule et l'oreille, un tube de sang dans une main, l'agenda dans l'autre. "
          "« Cabinet de Montchéry, ne quittez pas. » Elle vous regarde. « Vous êtes "
          "l'étudiant·e ? Sandra. La Dre est en retard, une visite à domicile qui a mal "
          "tourné. » Elle soupire. « Vous savez prendre une tension ? Il me faudrait celles "
          "de la salle d'attente. »", [
            R("« Oui. Je me présente comme étudiant·e à chaque patient, et vous me "
              "montrez où noter ? »",
              2, "ic3 pb2 cc1 rd1"),
            R("« Je ne sais pas si j'ai le droit, sans la Dre. »", 3, "pb1 ic-1"),
            R("« Je suis là pour voir la médecin, pas pour aider au secrétariat. »",
              4, "ic-3 rd-3 pb-1"),
            R("« Bien sûr. » Et filer vers la salle d'attente avec le tensiomètre.",
              2, "ic1 pb-1"),
            R("« Montrez-moi d'abord comment vous faites ici, pour ne rien déranger ? »", 3, "ic2 cc1 rd1"),
        ]),
        I(2, "narr", "",
          "Salle d'attente. Un vieil homme en salopette vous tend son bras avant que vous "
          "ayez ouvert la bouche. « Ah, le petit docteur ! Vous allez me guérir ma goutte ? » "
          "M. Cuendet, huitante-huit ans, dit l'étiquette du dossier. Les autres rient. Une "
          "dame en foulard rouge, une canne entre les genoux, vous observe par-dessus ses "
          "lunettes.", [
            R("« Bonjour Monsieur Cuendet. Alex, étudiant·e en deuxième année : pas encore "
              "docteur. Je prends votre tension, d'accord ? »", 6, "rd2 cc3 pb2"),
            R("« Pas encore docteur, mais j'y travaille ! » Et brancher le brassard.",
              6, "cc1 er1"),
            R("« Oui, oui. » Et brancher le brassard sans le détromper.", 6, "pb-2 cc-1"),
            R("« La goutte, c'est l'acide urique. Vous buvez de la bière, Monsieur "
              "Cuendet ? »", 6, "pb-2 rd-2 cc-1"),
            R("Lui proposer de passer dans le couloir, pour prendre sa tension à l'écart des "
              "autres.", 6, "rd2 pb1 cc1"),
        ]),
        I(3, "sandra", "neutral",
          "« Prendre une tension, oui. Dire à quelqu'un que sa tension est mauvaise, non : "
          "ça, c'est la Dre. » Elle vous tend le tensiomètre et une feuille. « Le nom, "
          "l'heure, les deux bras pour les nouveaux. Et ici, tout le monde va vous appeler "
          "docteur. Faites-en ce que vous voulez. »", [
            R("« Compris : je mesure, je note, je ne commente pas. »", 2, "pb2 cc1 ic1"),
            R("« Et si c'est très haut, je vous préviens ? »",
              2, "pb2 cc1 ic2"),
            R("« Je pourrai quand même leur dire si c'est normal ou pas, non ? Ça les "
              "rassure, et de toute façon ils vont me le demander, ils demandent toujours. »",
              2, "pb-2 cc-1"),
            R("« Docteur, ça me va très bien. »", 2, "pb-3 rd-1"),
            R("Prendre le tensiomètre sans un mot.", 2, "ic-1"),
        ]),
        I(4, "sandra", "cold-anger",
          "Sandra raccroche, lentement. « Ici, le secrétariat, c'est la moitié de la "
          "médecine. C'est moi qui sais que Mme Bovay ne viendra jamais un mardi, et "
          "pourquoi. » Elle repose le tube. « La Dre arrive dans vingt minutes. Asseyez-vous "
          "dans la salle d'attente. Avec les patients. »", [
            R("« Vous avez raison. Pardon. Je prends les tensions ? »", 2, "ic3 rd2 er1 pb1"),
            R("S'asseoir dans la salle d'attente sans un mot, vexé·e, et sortir son "
              "téléphone.", 5, "ic-1 er-1"),
            R("« Je ne voulais pas vous vexer. »", 5, "ic1"),
            R("« Je verrai ça avec la Dre Golay quand elle arrivera : c'est elle qui "
              "m'accueille, c'est à elle de me dire ce que je dois faire pendant mon "
              "immersion. »", 5, "ic-2 rd-1 pb-1"),
        ]),
        I(5, "narr", "",
          "Vous vous asseyez entre un chien et un vieil homme en salopette, qui vous "
          "dévisage : « Alors c'est vous, le petit docteur ? Vous allez me guérir ma "
          "goutte ? » Les autres rient. Une dame en foulard rouge, une canne entre les "
          "genoux, vous observe par-dessus ses lunettes.", [go(6)]),
        I(6, "jeannine", "happy",
          "La dame au foulard rouge tapote la chaise à côté d'elle. « Laisse le petit "
          "tranquille, Albert, il a l'air plus perdu que toi. » Puis, à vous : « Jeannine "
          "Pittet. Vous êtes de la fac ? Vous faites de la dissection ? » Toute la salle "
          "d'attente écoute.", [
            R("« Oui, depuis lundi. Et vous, qu'est-ce qui vous amène ? »", 7, "rd1 cc1 em1"),
            R("Raconter la salle, l'odeur, la scie, pour faire rire la salle d'attente.",
              7, "rd-2 pb-2 er-1"),
            R("« Oui. Mais je n'en parle pas ici : on leur doit de la discrétion. »",
              7, "rd3 pb2 cc1"),
            R("Raconter l'hirondelle tatouée et le vernis rouge de « Madame 14 », parce que "
              "c'est ce qui vous a le plus touché·e, et que ça montre qu'on les respecte.",
              7, "rd-3 pb-3 em-1", sets=["anecdote_donneuse"]),
            R("« Oui. Vous connaissez quelqu'un qui a fait ce don ? »", 7, "em1 pb-1 cc1"),
        ]),
        I(7, "sandra", "neutral",
          "Sandra passe la tête par la porte. « Madame Pittet ! » Deux personnes se lèvent : "
          "la dame au foulard rouge, et un homme d'une soixantaine d'années en veste de "
          "chasse. « Jean-Paul, assieds-toi, c'est Jeannine. Toi, c'est après. » L'homme se "
          "rassied en grommelant ; Jeannine ne le regarde pas. En passant près de vous, elle "
          "glisse : « Le cousin. On ne se parle plus depuis l'héritage de 1987. » Puis, plus "
          "bas encore, avec un drôle de sourire : « Moi aussi, un jour, je viendrai vous "
          "apprendre des choses. »", [go(8)]),
        I(8, "golay", "neutral",
          "La Dre Golay arrive en coup de vent, sacoche à la main, cheveux en bataille. "
          "« Alex ! Pardon : une chute à domicile. Vous faites l'anamnèse de Mme Pittet avec "
          "moi ? » Elle se tourne vers Jeannine. « Jeannine, ça vous dérange qu'un·e "
          "étudiant·e la fasse ? — Plus on est de fous… » La Dre s'assied en retrait. "
          "« Allez-y. Je n'interviens que si besoin. »", [
            R("Se présenter, demander son accord, puis : « Qu'est-ce qui vous amène "
              "aujourd'hui ? »", 9, "rd3 cc2 pb1"),
            R("« Douleur dans la poitrine ? Essoufflement ? Toux ? Fièvre ? Palpitations ? "
              "Perte de poids ? Vous fumez ? Vous buvez ? Des allergies ? »",
              10, "cc-1 em-1 rd-1"),
            R("Lire le dossier à l'écran, en silence, avant de commencer.", 9, "cc-1 rd-1"),
            R("« Racontez-moi ce qui ne va pas, à votre façon. »", 9, "cc3 em2 rd2"),
            R("« Vous mangez trop salé, je parie. »", 11, "rd-2 cc-2 pb-1"),
        ]),
        I(9, "jeannine", "neutral",
          "« Les chevilles. Elles gonflent. Et la Dre veut me voir parce que j'ai pris deux "
          "kilos en une semaine. » Elle rit. « À mon âge, deux kilos, c'est plutôt une bonne "
          "nouvelle. » Puis, plus bas : « Je dors avec deux oreillers, maintenant. Sinon je "
          "me réveille comme si on m'appuyait sur la poitrine. Mais bon. Je ne vais pas me "
          "plaindre. »", [
            R("« Depuis quand dormez-vous avec deux oreillers ? Vous vous réveillez "
              "essoufflée, la nuit ? »", 13, "cc3 em1 rd1"),
            R("« Vous en riez. Mais ça vous inquiète ? »",
              13, "em3 cc1 rd1 co1"),
            R("Rire avec elle, et passer aux médicaments.", 13, "em-1 cc-1"),
            R("« Ça ressemble beaucoup à une orthopnée, dans le cadre d'une insuffisance "
              "cardiaque décompensée, avec la prise de poids et les œdèmes : c'est le tableau "
              "typique du cours. »", 12, "cc-3 pb-3 rd-1"),
            R("« Vous pouvez vous plaindre, ici. C'est fait pour ça. »", 13, "em2 rd2 co1"),
        ]),
        I(10, "jeannine", "suspicious",
          "Jeannine vous regarde par-dessus ses lunettes. « Non, non, non et non. » Un "
          "temps. « Vous m'avez posé dix questions et vous n'avez pas écouté une seule "
          "réponse, petit. J'ai fait des accouchements pendant quarante ans : on n'apprend "
          "rien d'une femme en lui lisant un formulaire. » Derrière vous, la Dre Golay cache "
          "un sourire.", [
            R("« Vous avez raison. Racontez-moi, à votre façon. »",
              9, "cc2 er2 rd2"),
            R("« C'est la méthode qu'on nous apprend en communication : des questions fermées "
              "pour ne rien oublier. On est notés là-dessus, vous savez. »",
              9, "er-1 cc-1 rd-1"),
            R("Se tourner vers la Dre Golay pour qu'elle reprenne la main.", 9, "er-1 ic1"),
            R("« Alors apprenez-moi. »", 9, "rd2 er1 em1"),
            R("Continuer la liste : « Et des palpitations ? »", 11, "rd-2 cc-2 er-1"),
        ]),
        I(11, "golay", "neutral",
          "La Dre Golay pose doucement la main sur le bureau. « Alex. On écoute d'abord. On "
          "explique après — et c'est moi qui explique. » Jeannine croise les bras. « Ce "
          "n'est pas un interrogatoire de police, ici. »", [
            R("« Pardon, Madame Pittet. Racontez-moi. »",
              9, "rd2 er2 cc1 pb1"),
            R("« C'était une question, pas un jugement. »", 9, "er-1 cc-1"),
            R("Se taire, et laisser la Dre Golay reprendre l'entretien.", 9, "er1 ic1"),
            R("« C'est quand même vrai que le sel fait gonfler les chevilles, c'est dans tous "
              "les manuels : je voulais juste vérifier son alimentation avant le reste. »",
              9, "pb-2 rd-2 er-1"),
        ]),
        I(12, "jeannine", "anxious",
          "Jeannine a perdu son sourire. « Ortho-quoi ? C'est grave ? » La Dre Golay se "
          "redresse. « Alex, les hypothèses, on les discute entre nous, après. » Puis, à "
          "Jeannine : « On va regarder ça ensemble. »", [
            R("« Pardon, je parle trop vite. C'est la Dre qui va vous expliquer. »", 13, "pb2 cc2 rd2 er1"),
            R("« Non, non, ce n'est pas grave du tout. »", 13, "cc-2 pb-2 co-1"),
            R("Lui expliquer en détail ce qu'est une insuffisance cardiaque : le cœur qui "
              "pompe moins bien, l'eau qui s'accumule dans les poumons et dans les jambes, "
              "les médicaments qui existent pour ça.", 13, "pb-3 cc-1 rd-1"),
            R("Rougir et se taire.", 13, "er-1"),
            R("« Un mot savant pour dire que vous respirez mieux assise. Le reste, c'est la "
              "Dre. »", 13, "cc3 pb1 rd1"),
        ]),
        I(13, "jeannine", "sad",
          "Jeannine tourne son alliance autour de son doigt. « Depuis les foins, à peu près. "
          "Je monte moins à la grange. Daniel, mon fils, croit que c'est la paresse. » Elle "
          "rit, mais pas longtemps. « Mon mari, lui, n'a jamais eu le temps de vieillir. »", [
            R("Laisser un silence, puis : « Votre mari… ? »", 14, "em3 rd1 cc1 co1"),
            R("« Et Daniel, il passe vous voir souvent ? »", 15, "cc1 em1"),
            R("« Vous avez l'air d'être quelqu'un qui ne se plaint jamais, qui porte tout "
              "toute seule depuis longtemps, et qui n'aime pas qu'on s'occupe d'elle. Je me "
              "trompe ? »", 15, "em2 rd1"),
            R("Revenir aux symptômes : « Et vous toussez, la nuit ? »", 15, "cc1 em-1"),
            R("« Les fils, ils ne comprennent jamais rien, de toute façon. »",
              15, "rd-1 pb-1 em-1"),
        ]),
        I(14, "jeannine", "melancholic",
          "« Un tracteur, en 98, dans le talus derrière la maison. C'est Daniel qui l'a "
          "trouvé. Il avait vingt-huit ans. » Elle lisse son foulard. « Voilà. Maintenant, "
          "vous savez pourquoi mon fils a peur de tout ce qui touche aux corps. » La Dre "
          "Golay vous regarde sans rien dire.", [
            R("« Merci de me l'avoir dit. » Puis laisser un silence.",
              15, "em2 rd2 er1 co1"),
            R("« Je suis désolé·e. Ça a dû être terrible, pour vous deux. »", 15, "em2 co2"),
            R("« Et vous, comment avez-vous tenu ? »", 15, "em2 co1"),
            R("« Ah. Et les chevilles, depuis quand exactement ? »", 15, "em-2 rd-1 co-1"),
            R("Taper « deuil, fils traumatisé par le décès du père, accident agricole 1998 » "
              "dans le dossier, à l'écran, pendant qu'elle parle, pour ne rien oublier.",
              15, "rd-2 em-1 pb-1"),
        ]),
        I(15, "golay", "neutral",
          "La Dre Golay fait allonger Jeannine sur la table d'examen. « Alex, venez sentir. "
          "Appuyez là, au-dessus de la cheville, une dizaine de secondes. » Jeannine relève sa "
          "jupe d'un geste vif. « Allez-y, je ne mords pas. J'ai fait ça à six cents femmes "
          "enceintes. »", [
            R("« Je peux ? Dites-moi si ça fait mal. »",
              16, "rd3 cc2 em1"),
            R("Appuyer directement, en comptant à voix haute.", 16, "rd-1 cc1"),
            R("« J'ai les mains froides, pardon. Je les réchauffe d'abord. »", 16, "rd2 em1 co1"),
            R("Commenter pour la Dre, sans regarder Jeannine : « Godet bilatéral, prenant, "
              "quatre millimètres, remontant jusqu'à mi-jambe, non douloureux. »",
              16, "rd-2 cc-1"),
            R("« Je préfère regarder, cette fois. »", 16, "er-1"),
        ]),
        I(16, "jeannine", "neutral",
          "Le doigt laisse un creux dans la cheville, qui se remplit lentement. La Dre Golay "
          "sort imprimer une ordonnance. Jeannine se rassied, rajuste son foulard, et vous "
          "regarde droit dans les yeux. « Votre faculté, ils ont un bureau pour les dons du "
          "corps, là-bas ? »", [
            R("« Oui, à l'institut d'anatomie. Pourquoi ? Vous y pensez ? »",
              17, "em2 cc1 rd1"),
            R("« Je ne sais pas. Il faudrait demander à la Dre Golay. »", 17, "pb1 em-1"),
            R("« Ah non, vous n'allez pas mourir, Madame Pittet ! »", 17, "em-1 cc-2 rd-1"),
            R("Lui raconter ce qui se passe vraiment en salle de dissection : la scie, les "
              "bacs, l'odeur, ce que les étudiants se disent entre eux.", 17, "rd-3 pb-3",
              sets=["anecdote_donneuse"]),
            R("« Je vous dis ce que je sais, la Dre fera le reste. »", 17, "cc2 pb2 em1 rd1"),
        ]),
        I(17, "jeannine", "happy",
          "Elle sort de son porte-monnaie une carte plastifiée, coincée entre sa carte "
          "Cumulus et une photo d'enfant. « Signé il y a deux ans. La Dre le sait : c'est "
          "elle qui a signé le certificat. » Elle range la carte. « J'ai mis au monde six "
          "cents enfants dans ce coin. Il faut bien que quelqu'un vous apprenne à les "
          "recevoir. Et à recevoir le reste. » Un temps. « Venez me voir mardi, aux "
          "Combettes, avec Thierry, l'infirmier. Il y a quelque chose que je veux vous "
          "demander. »", [
            R("« Si la Dre est d'accord. Et ça restera dans l'équipe. »", 19, "pb3 cc2 rd2"),
            R("« Je viendrai, promis. Et je ne dirai rien à personne, ni à la Dre, ni à "
              "Thierry, ni à votre famille : ce sera entre vous et moi. »",
              19, "pb-3 em1 cc-1"),
            R("« Pourquoi moi ? »", 18, "em1 cc1"),
            R("« Je n'ai pas le droit de faire des visites à domicile, je crois. »",
              19, "pb1 em-1"),
            R("« Vous êtes sûre de vous ? C'est une décision lourde, pour votre famille. »",
              19, "rd-2 pb-2"),
        ]),
        I(18, "jeannine", "happy",
          "« Parce que vous êtes au début. » Elle sourit. « Au début, on écoute encore. "
          "Après, on sait trop de choses pour écouter. » Elle referme son porte-monnaie. "
          "« Alors, mardi ? »", [
            R("« Je demande à la Dre Golay ; si elle est d'accord, je viens. »",
              19, "pb3 ic2 cc1"),
            R("« Mardi, promis. Et motus. »", 19, "pb-3 cc-1 em1"),
            R("« Si c'est pour parler de votre don, je ne suis pas la bonne personne : il y a "
              "un bureau à l'institut, avec des gens formés, ils vous expliqueront tout mieux "
              "que moi. »", 19, "em-2 pb1 rd-1 cc1"),
            R("« Avec plaisir. »", 19, "em1"),
        ]),
        I(19, "golay", "neutral",
          "La Dre Golay revient, l'ordonnance à la main. Elle regarde Jeannine, puis vous, "
          "comme si elle sentait qu'il s'est passé quelque chose pendant ses deux minutes "
          "d'absence.", [
            R("« Mme Pittet m'invite mardi, avec Thierry. Je peux y aller ? »", 20, "ic3 pb3 cc2 rd1"),
            R("Ne rien dire. Vous irez mardi par vos propres moyens.", 20, "pb-3 ic-2",
              sets=["golay_pas_informee"]),
            R("Demander d'abord à Jeannine, à voix basse : « Je peux en parler à la Dre ? »",
              20, "rd2 pb2 ic1"),
            R("En riant : « Mme Pittet veut me léguer son corps ! »", 20, "rd-3 pb-2 ic-1"),
            R("« On parlait de ses six cents accouchements. Elle a une mémoire incroyable : "
              "vous saviez qu'elle se souvient du prénom de chaque enfant ? »",
              20, "pb-2 cc-2 ic-2", sets=["golay_pas_informee"]),
        ]),
        I(20, "golay", "neutral",
          "18 h 40. Le dernier patient est parti. La Dre Golay ferme elle-même les volets. "
          "« Jeannine a choisi. Elle choisit toujours, depuis quarante ans. » Elle cherche "
          "ses clés dans sa sacoche. « Le difficile, ce ne sera pas elle. Ce sera son "
          "fils. » Puis : « Qu'est-ce qui vous a frappé·e, aujourd'hui ? »", [
            R("« Que tout le monde ici vous connaît, vous et Sandra. Que la médecine commence "
              "au comptoir. »", END, "ic3 rd1 cc1"),
            R("« L'œdème. Je n'avais jamais senti un godet. »", END, "cc1"),
            R("« Que Mme Pittet m'a raconté sa vie en dix minutes, et que je ne sais pas quoi "
              "en faire. »", END, "er2 em1 cc1"),
            R("« Pas grand-chose de médical, honnêtement : c'était surtout des tensions et de "
              "la conversation. Je pensais voir davantage de pathologies intéressantes en "
              "médecine de famille. »", END, "ic-2 rd-2"),
            R("« Qu'on m'appelle docteur, et que j'aime ça. Ça m'inquiète. »",
              END, "er3 pb2 cc1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 1.4 La ferme des Combettes
# ---------------------------------------------------------------------------
_INTRO_14 = (
    "Mardi, 17 h. La Dre Golay a dit oui, à condition que vous accompagniez Thierry Bovet, "
    "l'infirmier du CMS, dans sa tournée. Sa vieille Panda cahote sur le chemin de gravier "
    "des Combettes, à deux kilomètres du village. Un chien aboie. On entend des vaches "
    "qu'on ne voit pas."
)
_INTRO_14_SECRET = (
    "Mardi, 17 h. Vous n'avez rien dit à la Dre Golay : c'est Sandra qui vous a donné "
    "l'horaire de Thierry Bovet, l'infirmier du CMS. Sa vieille Panda cahote sur le chemin "
    "de gravier des Combettes, à deux kilomètres du village. Thierry n'a pas encore dit un "
    "mot."
)

S1_4 = S(4, "1.4 La ferme des Combettes", _INTRO_14,
    focus=("pb", "em", "rd"),
    entries=[
        Entry(3, when(all=["golay_pas_informee", "anecdote_donneuse"]), _INTRO_14_SECRET),
        Entry(2, when(all=["golay_pas_informee"]), _INTRO_14_SECRET),
        Entry(4, when(all=["anecdote_donneuse"]), _INTRO_14),
    ],
    debriefs=[
        Debrief(when(all=["revele_a_daniel"]), tone="hard", lead=(
            "Daniel a appris le don du corps de sa mère par vous, dans sa cuisine, devant "
            "elle. Le secret médical (art. 321 du Code pénal) vise aussi les étudiant·e·s "
            "pour ce qu'ils et elles apprennent pendant leurs études ; il protège la "
            "patiente, même face à son propre fils. Ce qu'une personne a décidé pour son "
            "corps, c'est à elle de le dire, quand elle le veut — ou de ne pas le dire.")),
        Debrief(when(all=["promesse_jeannine"]), tone="mixed", lead=(
            "Vous avez promis à Jeannine que personne ne saurait jamais. C'est une promesse "
            "qu'aucun soignant ne peut tenir seul : un dossier se lit, un village parle, une "
            "équipe se transmet des informations. Ce que vous pouviez promettre, c'était "
            "votre propre silence — et l'encourager à parler elle-même à son fils.")),
    ],
    nodes=[
        I(1, "thierry", "neutral",
          "Thierry conduit d'une main. « Jeannine, c'est trois passages par semaine : "
          "pilulier, pesée, bas de contention. La toilette, elle refuse : « je ne suis pas "
          "encore morte ». Daniel, son fils, passe matin et soir pour les bêtes. » Il vous "
          "jette un coup d'œil. « Qu'est-ce que tu viens faire, exactement ? »", [
            R("« Voir comment tu travailles. Et elle m'a demandé de passer. »", 5, "ic2 cc2 rd1"),
            R("« Voir un vrai patient chronique, avec des comorbidités, pour mon cours de "
              "médecine de famille. »", 5, "rd-2 ic-1"),
            R("« C'est quoi, exactement, ton travail ? »", 6, "ic3 cc1"),
            R("« Elle veut me demander quelque chose, je ne sais pas quoi. Et je ne sais pas "
              "si je dois en parler à la Dre : elle m'a fait comprendre que c'était "
              "personnel. »", 5, "cc1 pb-1"),
            R("Hausser les épaules : « La Dre m'a envoyé·e. »", 5, "ic-1 cc-1"),
        ]),
        I(2, "thierry", "cold-anger",
          "Au premier virage, Thierry parle sans vous regarder. « La Dre m'a appelé à midi. "
          "Elle ne savait pas que tu venais. » Un temps. « Les visites, c'est avec son "
          "accord. Pas en douce. Jeannine est sa patiente, pas ta copine. »", [
            R("« Elle a raison. Je l'appelle ce soir pour m'excuser, et je lui dirai "
              "tout. »", 5, "pb3 ic2 er1"),
            R("« Je ne pensais pas que c'était un problème. »", 5, "pb-1"),
            R("« C'est Jeannine qui m'a invité·e, pas la Dre. »", 5, "pb-2 ic-2"),
            R("« Tu peux lui dire que c'est réglé ? »", 5, "ic-1 pb-1"),
            R("« Je descends ici, si tu préfères. Je rentrerai à pied. »", 5, "pb1 er-1"),
        ]),
        I(3, "thierry", "cold-anger",
          "Au premier virage, Thierry parle sans vous regarder. « La Dre ne savait pas que "
          "tu venais. Et Jeannine m'a appelé hier. » Un temps. « Il paraît que tu as raconté "
          "un tatouage de cadavre à toute la salle d'attente. Elle hésite à te parler, "
          "maintenant. Dans un village, tout se sait. Surtout ça. »", [
            R("« J'ai fait deux erreurs : parler de la donneuse, et venir en douce. Je les "
              "répare ce soir. »", 5, "pb3 rd2 ic2 er1"),
            R("« Je ne pensais pas que c'était grave. »", 5, "pb-1 rd-1"),
            R("« Ce n'était qu'une anecdote, sans nom, sans lieu, sans date : personne ne "
              "peut reconnaître qui que ce soit avec une hirondelle, il y en a des "
              "milliers. »", 5, "rd-2 pb-2"),
            R("« Tu veux que je descende ? »", 5, "er-1 pb1"),
            R("« Qui lui a raconté ça ? »", 5, "pb-1 ic-1 er-1"),
        ]),
        I(4, "thierry", "neutral",
          "Au premier virage, Thierry vous jette un coup d'œil. « Jeannine m'a appelé hier. "
          "Il paraît que tu as raconté un tatouage de cadavre à toute la salle d'attente. » "
          "Il rétrograde. « Elle hésite à te parler, du coup. Dans un village, tout se sait. "
          "Et toi, tu viens de lui montrer que ça sortait. »", [
            R("« Elle a raison d'hésiter. C'était une faute envers la donneuse. Je le lui "
              "dirai. »", 5, "rd3 pb3 er1"),
            R("« Ce n'était qu'une anecdote, sans nom. »", 5, "rd-2 pb-2"),
            R("« Je ne pensais pas que c'était grave. »", 5, "pb-1 rd-1"),
            R("« Elle exagère un peu, non ? Au café, on raconte bien pire. »", 5, "rd-2 em-1 pb-1"),
            R("Se taire jusqu'à la ferme.", 5, "er-1"),
        ]),
        I(5, "jeannine", "neutral",
          "La cuisine sent le café réchauffé et le savon de Marseille. Jeannine est assise à "
          "la toile cirée, un chat sur les genoux. Thierry la pèse — un kilo et demi de plus "
          "en une semaine — et ouvre le pilulier : le casier du dimanche matin est plein. "
          "« Le dimanche, je vais à la messe, pas aux toilettes », dit-elle avant qu'il ait "
          "posé la question. Puis : « Thierry, tu peux aller voir mes bas dans la chambre ? "
          "J'aimerais dire deux mots à ton étudiant·e. »", [
            R("« D'accord. Thierry, je te redis ensuite les soins ? »",
              7, "ic3 rd2 pb2"),
            R("« Thierry peut rester, on travaille ensemble. »", 15, "ic2 pb1 rd-2"),
            R("Ne rien dire, et s'asseoir en face d'elle.", 7, "rd1"),
            R("« Vous savez que votre diurétique du dimanche, c'est important ? Si vous le "
              "sautez, l'eau s'accumule : c'est pour ça que vous avez repris un kilo et "
              "demi. »", 7, "pb-1 cc1 rd-1"),
            R("« Je préfère que Thierry reste : je ne veux pas de secrets. »",
              15, "rd-2 pb-1 em-1"),
        ]),
        I(6, "thierry", "happy",
          "« Infirmier du CMS ? » Il sourit. « Je suis l'œil de la Dre dans la maison. Je "
          "vois le frigo, le pilulier, l'escalier, le fils. Elle, elle voit une tension et "
          "une prise de sang. » Il se gare devant la ferme. « Les deux ensemble, ça fait "
          "une patiente. Séparément, ça fait deux dossiers. »", [
            R("« Alors aujourd'hui, je regarde avec tes yeux. Tu me dis quoi voir ? »",
              5, "ic3 rd1 cc1"),
            R("« Et toi, tu dis à la Dre tout ce que tu vois ? »", 5, "ic2 cc1"),
            R("« C'est du travail social, finalement, plus que de la médecine : la vraie "
              "médecine, c'est ce qui se passe au cabinet, avec les examens. »",
              5, "rd-1 ic-2"),
            R("« Joli. Je le note. »", 5, "ic1"),
            R("« Je croyais que c'était surtout des pansements et des prises de sang à "
              "domicile. »", 5, "ic-2 rd-1"),
        ]),
        I(7, "jeannine", "neutral",
          "Quand la porte de la chambre s'est refermée, Jeannine vous jauge un long moment. "
          "Puis elle pose sur la toile cirée sa carte de donneuse, et une enveloppe beige, "
          "fermée, avec écrit dessus, de sa grande écriture penchée : « À ouvrir après. » "
          "« Celle-là, c'est pour plus tard. » Elle pose la main dessus. « Daniel ne sait pas, "
          "pour le don. Il ne doit pas savoir. Il me ferait une scène, il dirait que sa mère "
          "ne finira pas en morceaux dans une cave en ville. » Elle vous regarde. "
          "« Promettez-moi de ne rien lui dire. »", [
            R("« Je ne dirai rien à Daniel : c'est votre décision. Mais je ne peux pas "
              "promettre qu'il ne l'apprendra jamais. »", 9, "pb3 cc3 rd2"),
            R("« Je vous le promets. Personne ne saura, jamais. »", 9, "pb-2 cc-2 em1", sets=["promesse_jeannine"]),
            R("« Il faut lui dire, Madame Pittet. C'est votre fils. »", 9, "rd-2 pb-1 cc1"),
            R("« De quoi avez-vous peur, avec Daniel ? »", 8, "em3 cc1 co1"),
            R("« Je vous le jure sur ma tête. »", 9, "pb-3 cc-2",
              sets=["promesse_jeannine"]),
            R("« Ça ne me regarde pas vraiment. »", 9, "em-2 rd-1 pb1 co-1"),
        ]),
        I(8, "jeannine", "sad",
          "« De quoi j'ai peur ? » Elle caresse le chat. « Quand il a trouvé son père, "
          "Daniel n'a laissé personne le toucher. Il a attendu l'ambulance une heure, assis "
          "dans le talus, à le tenir. » Un temps. « Depuis, il ne supporte pas qu'on touche "
          "aux corps. Même pas au mien : il ne m'a jamais vue à l'hôpital. » Elle repousse "
          "l'enveloppe vers le milieu de la table. « Alors ? Vous promettez ? »", [
            R("« Je ne lui dirai rien. Mais je ne peux pas promettre pour les autres. »", 9, "em3 pb3 cc2"),
            R("« Je vous le promets. Personne ne saura. »", 9, "pb-2 cc-2 em2",
              sets=["promesse_jeannine"]),
            R("« Vous pourriez renoncer au don, alors, pour lui ? Ce serait plus simple pour "
              "tout le monde, et il n'aurait pas à revivre ce qu'il a vécu avec son "
              "père. »", 9, "rd-2 pb-2 co-1"),
            R("« Ça a dû être terrible, pour vous deux. »", 9, "em2 co2"),
            R("« C'est une raison de plus pour lui en parler, avec la Dre Golay à côté, "
              "peut-être. »", 9, "cc2 ic2 em1"),
        ]),
        I(9, "daniel", "suspicious",
          "Des bottes sur le seuil. La porte s'ouvre sur un homme d'une cinquantaine "
          "d'années, casquette, mains rouges de froid. « Salut, maman. » Il voit l'enveloppe ; "
          "Jeannine la glisse sous le journal, d'un geste qu'elle croit discret. Thierry "
          "revient de la chambre : « Daniel, je te présente Alex, étudiant·e en médecine. » "
          "Daniel ne tend pas la main. « Vous êtes de la fac ? Alors dites-moi franchement : "
          "elle peut encore vivre seule ici, oui ou non ? »", [
            R("« Je ne peux pas en juger. Demandez-lui : elle est là. »", 10, "pb3 rd2 cc2"),
            R("« Franchement ? Non. Elle a l'air épuisée. »", 10, "pb-3 rd-3 cc-1"),
            R("« Oui, elle a l'air de très bien se débrouiller : la maison est propre, elle "
              "est coiffée, elle a de la conversation, et Thierry passe trois fois par "
              "semaine. »", 10, "pb-2 cc-1"),
            R("Se tourner vers Jeannine : « Madame Pittet, vous voulez répondre ? »",
              10, "rd3 pb1"),
            R("« Thierry la voit trois fois par semaine. Il est mieux placé que moi. »",
              10, "ic2 pb2"),
        ]),
        I(10, "daniel", "suspicious",
          "Daniel regarde le journal, et la bosse sous le journal. « C'est quoi, cette "
          "enveloppe ? Encore un papier du notaire ? » — « Des recettes », dit Jeannine. "
          "Daniel ne la regarde pas. C'est vous qu'il regarde. « Vous savez ce que c'est, "
          "vous ? »", [
            R("« C'est à elle de vous répondre. »",
              12, "pb3 rd2 cc1"),
            R("« Des recettes, oui. »", 12, "pb-1 cc-2 rd-1"),
            R("« C'est pour le don de son corps à la faculté. »", 11,
              "pb-3 rd-3 em-1 co-1", sets=["revele_a_daniel"]),
            R("Regarder Jeannine, puis Daniel : « Vous devriez en parler tous les deux, avec "
              "quelqu'un à côté de vous. C'est important, et ce n'est pas à moi de le faire à "
              "sa place. »", 12, "pb1 cc1 rd-1"),
            R("« Je ne peux pas parler de ce qui concerne votre mère. Je suis désolé·e. »",
              12, "pb2 cc1 rd1 em1"),
            R("Changer de sujet : « Vous avez combien de vaches ? »", 12, "cc-1 em1"),
        ]),
        I(11, "daniel", "cold-anger",
          "Daniel ne dit rien pendant longtemps. Il soulève le journal, prend l'enveloppe, la "
          "repose sans l'ouvrir. « En morceaux. Dans une cave. » Sa voix ne monte pas. « Tu "
          "ne m'as rien dit, maman. C'est un·e gamin·e de la fac qui me l'apprend, dans ta "
          "cuisine. » Il sort. La porte claque. Jeannine regarde ses mains. « Sortez, s'il "
          "vous plaît. Thierry, ramène-le. »", [
            R("« Madame Pittet, j'ai trahi votre confiance. Je n'en avais pas le droit. "
              "Pardon. »", END, "pb2 rd2 er1 co1"),
            R("« Il fallait bien qu'il le sache un jour. »", END, "pb-3 rd-3 em-2"),
            R("Sortir sans un mot.", END, "er-1 rd-1"),
            R("« Je vais lui parler, à Daniel. Il comprendra. »",
              END, "pb-3 er-1 rd-1"),
            R("« Je le dirai moi-même à la Dre Golay, ce soir. »", END, "pb2 ic2 er1"),
        ]),
        I(12, "jeannine", "neutral",
          "Daniel vous regarde encore une seconde, puis repart vers l'étable. Jeannine "
          "ressort l'enveloppe, la regarde, la remet sous le journal. Elle ne commente pas. "
          "Puis, en vous tendant un bloc-notes et un crayon : « Si j'ai besoin de vous, je "
          "vous appelle comment ? Vous me donnez votre numéro de Natel ? »", [
            R("« La nuit, le 144. Le jour, le cabinet. »", 17, "pb3 cc2 ic2 em1"),
            R("« Bien sûr. » Écrire votre numéro de portable sur le bloc.", 17,
              "em2 rd1 pb-3", sets=["numero_donne"]),
            R("« Je n'ai pas le droit de donner mon numéro. »", 17, "pb2 cc1 em-2"),
            R("« Pour les urgences seulement, alors : si vous avez mal la nuit, ou si vous "
              "tombez, vous m'appelez et je viens, même tard. » Et écrire votre numéro.",
              17, "pb-3 cc-2 em1", sets=["numero_donne"]),
            R("Écrire en gros, sur le calendrier près du téléphone, les numéros du cabinet, "
              "de Thierry et le 144.", 17, "cc3 pb2 ic1 rd1"),
        ]),
        I(17, "daniel", "sad",
          "Dans la cour, Daniel vous attend près de la Panda, pendant que Thierry range son "
          "matériel. Il parle sans vous regarder, les yeux sur l'étable. « Vous, vous êtes "
          "neuf. Vous me direz la vérité. » Un temps. « Elle est en train de mourir ? »", [
            R("« Demandez-le-lui, à elle. »", 13, "pb3 cc1"),
            R("« Non, elle va bien. »", 13, "cc-3 pb-2"),
            R("« Elle est fatiguée, ses chevilles gonflent, et la Dre s'inquiète pour son "
              "cœur. Je ne devrais pas vous le dire, mais vous êtes son fils : vous avez le "
              "droit de savoir ce qui se passe chez vous. »", 13, "pb-3 cc-1 rd-2 em1"),
            R("« Vous avez l'air inquiet. Vous en avez parlé avec elle ? »",
              13, "em3 co1 pb2"),
            R("Monter dans la Panda sans répondre.", 13, "em-2 co-1 pb1"),
        ]),
        I(13, "thierry", "neutral",
          "Dans la Panda, Thierry allume une cigarette qu'il ne fume pas. « Alors ? Elle t'a "
          "dit quoi ? Moi, je suis son infirmier : ce qui touche à ses soins, j'ai besoin de "
          "le savoir. »", [
            R("« Son diurétique du dimanche. Et sa peur de Daniel. »", 14, "ic3 pb2 cc2"),
            R("« Elle m'a fait promettre de ne rien dire. »", 14, "ic-2 pb-1"),
            R("Tout raconter : le don, l'enveloppe, l'accident du mari, Daniel dans le talus, "
              "et ce que vous pensez de la relation entre la mère et le fils, pour que "
              "Thierry ait toutes les cartes en main.", 14, "pb-2 rd-1 ic1"),
            R("« Rien d'important. »", 14, "ic-2 cc-1"),
            R("« Qu'est-ce que tu as besoin de savoir, toi, pour bien la soigner ? »",
              14, "ic3 pb1 cc1"),
        ]),
        I(14, "thierry", "happy",
          "Thierry démarre. « Tu sais ce qu'elle m'a dit, la première fois que je suis "
          "venu ? « Thierry, le jour où je meurs, tu ouvres la fenêtre. Pour que je puisse "
          "sortir. » » Il sourit. « Les sages-femmes, elles savent ouvrir les portes dans les "
          "deux sens. »"),
        I(15, "jeannine", "cold-anger",
          "Jeannine ne vous quitte pas des yeux. « Thierry est un amour. Mais ce que j'ai à "
          "dire, je le dis à vous, ou je ne le dis à personne. Je suis chez moi, ici. » "
          "Thierry lève les mains, mi-amusé, mi-sérieux, et part vers la chambre.",
          [go(7)]),
    ],
)

# ---------------------------------------------------------------------------
# 1.5 La lettre — branche « la photo a circulé »
# ---------------------------------------------------------------------------
S1_5A = S(5, "1.5 La lettre",
    "Vendredi, 8 h 15. Un mail de la Pre Vautier aux cinq étudiant·e·s de la table 14. "
    "Objet : « Convocation — 9 h, bureau 112 ». Pas un mot de plus. Dans le couloir de "
    "l'institut, Maëlle a les yeux gonflés. Noah fixe ses chaussures. Yasmine est appuyée "
    "au mur, bras croisés. Léo arrive en courant.",
    focus=("rd", "co", "pb"),
    slot="1.5",
    cond=when(all=["photo_virale"]),
    debriefs=[
        Debrief(when(all=["mensonge_groupe"]), tone="hard", lead=(
            "Vous avez soutenu un mensonge devant la responsable du programme pour protéger "
            "une camarade. Couvrir quelqu'un, ce n'est pas le protéger : c'est ajouter une "
            "faute à la sienne, et faire porter le soupçon sur toute la table. On peut "
            "rester solidaire de Maëlle — être à côté d'elle, dire sa propre part — sans "
            "mentir pour elle.")),
        Debrief(when(all=["rencontre_rapin"]), tone="mixed", lead=(
            "Rien ne répare entièrement une atteinte à la dignité d'une personne qui ne peut "
            "plus se défendre. Mais vous êtes allé·e au-devant de sa fille : reconnaître "
            "les faits, présenter des excuses sans se défausser, dire ce que la donneuse "
            "vous a appris. C'est ce qu'on attend d'un soignant après une faute — la vôtre "
            "ou celle de votre équipe.")),
    ],
    nodes=[
        I(1, "maelle", "sad",
          "Maëlle vous attrape par la manche. « Je l'ai retirée, je te jure. Mais le compte "
          "de mèmes l'avait déjà. » Elle parle vite. « Tu peux dire que tu étais d'accord ? "
          "Que c'était une blague de groupe ? Comme ça, c'est pas que moi. S'il te plaît. »", [
            R("« Je ne vais pas mentir. Mais je serai à côté de toi. »", 4, "pb3 rd1 em1 co2"),
            R("« D'accord. On dit que c'était une blague de groupe. »", 2, "pb-3 rd-2 cc-2",
              sets=["mensonge_groupe"]),
            R("« C'est ton problème, Maëlle. »", 4, "em-3 ic-2 co-2"),
            R("« On dit la vérité. Toute. Et on s'excuse, tous ensemble, devant Vautier et "
              "devant la famille s'il le faut : c'est ce qu'on aurait dû faire lundi. »",
              4, "pb2 rd2 cc1"),
            R("La prendre dans vos bras, sans répondre.", 4, "em2 co2"),
            R("« Yasmine, Léo, Noah : on y va ensemble, et chacun dit ce qu'il a vu ? »",
              4, "ic3 pb1 cc1"),
        ]),
        I(2, "vautier", "cold-anger",
          "Bureau 112. La Pre Vautier ne vous fait pas asseoir. Maëlle parle la première, très "
          "vite : « C'était une blague de groupe, on était tous d'accord. » Yasmine se tourne "
          "vers elle, la bouche ouverte. La Pre Vautier ne regarde que vous. « C'est "
          "vrai ? »", [
            R("« Non. Maëlle a pris la photo, et je ne l'ai pas empêchée. »",
              4, "pb3 cc2 er1 rd1", clears=["mensonge_groupe"]),
            R("« Oui. On était tous d'accord, c'était une blague entre nous. »", 3, "pb-3 cc-3 rd-2 ic-1"),
            R("Se taire.", 3, "pb-2 cc-1"),
            R("« Je… je ne sais plus. C'est allé tellement vite, lundi, on était tous sous le "
              "choc de la première dissection, je ne me souviens plus très bien qui a dit "
              "quoi. »", 3, "cc-2 pb-1 er-1"),
            R("« En partie. Certains étaient d'accord, d'autres non. »", 3, "cc-2 pb-2"),
        ]),
        I(3, "yasmine", "angry",
          "« C'est faux. » Yasmine décroise les bras. « Personne n'était d'accord. J'ai écrit "
          "dans le groupe de la retirer à 22 h 15, c'est dans mon téléphone. » La Pre Vautier "
          "ne vous quitte pas des yeux. « Je vous verrai chacun séparément cet après-midi. "
          "Mais je vous repose la question maintenant. »", [
            R("« Yasmine a raison. J'ai menti. »", 4, "pb3 cc2 er1",
              clears=["mensonge_groupe"]),
            R("« Je maintiens ce que j'ai dit tout à l'heure. »", 4, "pb-3 cc-3 ic-2",
              sets=["mensonge_groupe"]),
            R("« Yasmine n'était pas là quand on en a parlé, à la sortie du vestiaire : elle "
              "ne peut pas savoir ce qu'on s'est dit entre nous, Maëlle, Noah et moi. »",
              4, "pb-3 cc-2 ic-3", sets=["mensonge_groupe"]),
            R("Se taire.", 4, "pb-2 cc-1"),
            R("Se tourner vers Maëlle : « Il faut dire la vérité, Maëlle. »",
              4, "pb2 cc1 em1", clears=["mensonge_groupe"]),
        ]),
        I(4, "vautier", "neutral",
          "Dans le bureau 112, la Pre Vautier déplie une feuille manuscrite. « Je vous lis la "
          "lettre que j'ai reçue hier soir. Je n'en enlève rien. » Elle lit sans lever les "
          "yeux. « Madame, ce soir, ma fille m'a montré une image sur son téléphone. C'était "
          "la main de ma mère. Je l'ai reconnue à l'hirondelle : elle se l'était fait tatouer "
          "à dix-neuf ans, à Marseille, contre l'avis de tout le monde. Le vernis rouge, "
          "c'est moi qui le lui avais mis, la veille de sa mort. Elle voulait partir "
          "élégante. Ma mère a donné son corps pour que vos étudiants apprennent. Pas pour "
          "qu'ils rient. » » Elle replie la feuille. « Elle signe Françoise Rapin. »", [
            R("« C'est nous qui lui avons fait ça. »", 5, "rd3 co2 pb2"),
            R("« On ne pensait pas que quelqu'un la reconnaîtrait : c'était flou, et la story "
              "ne devait durer que vingt-quatre heures. Personne n'imaginait qu'un compte de "
              "mèmes la reprendrait. »", 5, "pb-2 rd-1 co-2"),
            R("Garder le silence, les yeux sur la lettre.", 5, "rd1 er1"),
            R("« Ce n'est pas moi qui ai posté. »", 5, "pb-2 co-2 ic-2"),
            R("« Le vernis… Lundi, je m'étais dit que quelqu'un avait pris soin d'elle. »",
              5, "co3 rd2 em1"),
        ]),
        I(5, "vautier", "neutral",
          "« Ce programme existe depuis plus d'un siècle. Il tient sur une seule chose : la "
          "confiance de gens qui ne pourront jamais vérifier ce qu'on fait d'eux. » Elle pose "
          "la lettre. « La faculté demande la suppression de l'image partout, et Mlle "
          "Dupasquier recevra un avertissement formel. Mme Rapin, elle, demande autre chose : "
          "rencontrer les étudiants de la table. Cet après-midi. Je ne vous y oblige pas. »", [
            R("« J'irai. Je ne sais pas ce que je lui dirai, mais je lui dois d'être là. »",
              6, "rd3 co2 pb2 er1", sets=["rencontre_rapin"]),
            R("« Maëlle, tu veux qu'on y aille ensemble ? »", 6, "ic2 em1 co2 rd1",
              sets=["rencontre_rapin"]),
            R("« Je préfère lui écrire. »",
              10, "rd1 co1 er-1"),
            R("« Est-ce qu'on risque une sanction, nous aussi ? »", 10, "pb-1 er-1 rd-1 co-1"),
            R("« Ce n'est pas à nous d'aller la voir, c'est à Maëlle. »", 10, "ic-2 co-2 em-1"),
        ]),
        I(6, "rapin", "sad",
          "14 h, une petite salle sans fenêtre. Une femme d'environ cinquante-cinq ans, "
          "manteau gris, une broche en forme d'hirondelle au revers. Elle regarde les visages "
          "un par un. Maëlle pleure déjà. « Je ne vous dirai pas son nom. » Sa voix ne tremble "
          "pas. « Elle l'a donné une fois, ça suffit. » Elle se tourne vers vous, parce que "
          "vous êtes au bout de la rangée. « Alors ? »", [
            R("« Pardon. Nous l'avons exposée. »", 7, "rd3 co3 pb1"),
            R("« On ne pensait pas que quelqu'un la reconnaîtrait. »", 8, "pb-2 rd-1 co-1"),
            R("« C'est Maëlle qui a posté, pas nous : on lui a dit de la retirer dès qu'on l'a "
              "vue, il y a des messages dans le groupe qui le prouvent, je peux vous les "
              "montrer. »", 8, "pb-2 ic-3 co-2 rd-1"),
            R("Baisser la tête, sans rien dire.", 8, "rd1"),
            R("« Qu'est-ce qu'elle aimait, votre mère ? »", 7, "em2 co2 rd-1"),
        ]),
        I(7, "rapin", "neutral",
          "Mme Rapin vous regarde. « Lundi. Qu'est-ce qu'elle vous a appris ? » Elle attend "
          "vraiment la réponse.", [
            R("« Que quelqu'un avait pris soin d'elle jusqu'au bout. J'ai vu le vernis "
              "avant tout le reste. »",
              9, "co3 rd2 em2"),
            R("« L'anatomie de la paroi thoracique : les trois plans musculaires, les espaces "
              "intercostaux, le trajet des vaisseaux et des nerfs sous chaque côte. »",
              9, "cc1 em-2 co-1"),
            R("« Qu'on n'a pas le droit de la traiter comme un objet. Et qu'on l'a fait quand "
              "même. »", 9, "rd3 pb2 co1"),
            R("« Je ne sais pas encore. »", 9, "er1 cc1"),
            R("« Que les tatouages, il faut les couvrir. »", 9, "rd-2 em-2 co-1"),
        ]),
        I(8, "rapin", "cold-anger",
          "Mme Rapin vous regarde longtemps. « Vous êtes jeunes. » Dans sa bouche, ce n'est "
          "pas une excuse. « Ma mère aussi l'a été. Elle a fait des bêtises. Elle les a "
          "assumées. » Elle se lève. « Je crois que j'ai entendu ce que j'avais à "
          "entendre. »", [
            R("« Attendez. Pardon. Nous sommes responsables. »",
              7, "pb3 rd2 er1 co1"),
            R("La laisser partir.", 11, "co-1"),
            R("« On a déjà dit pardon. »", 11, "co-3 rd-2 em-2"),
            R("Se lever aussi, et lui ouvrir la porte en silence, la tête basse.", 11, "rd1"),
            R("« Qu'est-ce qu'on pourrait faire, à votre avis, pour que ça n'arrive plus "
              "jamais à une autre famille ? Une charte, une formation, un engagement écrit de "
              "chaque étudiant ? »", 7, "co1 cc1 rd1 ic1"),
        ]),
        I(9, "rapin", "melancholic",
          "« C'est moi, le vernis. » Elle touche sa broche. « Continuez. Apprenez. Mais ne la "
          "montrez plus jamais. » Elle se lève. En passant, elle pose la main une seconde sur "
          "l'épaule de Maëlle.", [go(11)]),
        I(10, "maelle", "sad",
          "Le soir, Maëlle vous écrit : « elle est venue. elle a dit que le vernis c'était "
          "elle. elle a demandé si on l'avait remarqué. j'ai dit oui. j'ai menti, je l'avais "
          "pas remarqué ».", [
            R("« Moi, je l'avais remarqué. J'aurais dû être là pour le lui dire. »",
              11, "co2 rd2 er1"),
            R("« Tu as bien fait de lui dire oui. »", 11, "cc-2 pb-1"),
            R("« Ça s'est bien passé, alors ? »", 11, "em-1"),
            R("« Tu veux qu'on lui écrive une lettre, ensemble, pour lui dire la vérité ? "
              "»", 11, "co2 ic2 rd2"),
            R("« Tu n'aurais pas dû mentir, même pour lui faire plaisir : elle t'a posé une "
              "vraie question, et tu lui as donné la réponse qu'elle voulait entendre, comme "
              "sur Instagram. »", 11, "pb1 cc1 em-2 co-1"),
        ]),
        I(11, "maelle", "sad",
          "Lundi matin, dans le couloir de l'institut, Maëlle s'assied par terre, le dos "
          "contre le radiateur. « Je suis une horrible personne. »", [
            R("« Non. Tu as regardé ta faute en face. »", 12, "em3 co2 pb1 rd1"),
            R("« Un peu, oui. »", 12, "em-3 co-2 ic-2"),
            R("« Mais non, c'est rien. Tout le monde a déjà oublié. »", 12, "cc-2 pb-2 em1"),
            R("S'asseoir par terre à côté d'elle, contre le radiateur, sans rien dire.", 12, "em2 co2"),
            R("« Tu devrais parler à quelqu'un de pourquoi tu postes tout, même ce qui te "
              "fait peur : le service de consultation psychologique de l'université, par "
              "exemple. Ils reçoivent des étudiants pour ça. »", 12, "ic2 em1 pb1"),
        ]),
        I(12, "yasmine", "neutral",
          "Yasmine s'arrête devant vous deux. Elle regarde Maëlle, longtemps, puis s'assied à "
          "son tour. « La première fois que j'ai fait une connerie en ambulance, personne ne "
          "s'est assis à côté de moi. » Elle n'en dit pas plus. Le carrelage est froid. "
          "Personne ne se relève tout de suite."),
    ],
)

# ---------------------------------------------------------------------------
# 1.5 Le livre des donneurs — branche « la photo n'a pas circulé »
# ---------------------------------------------------------------------------
_INTRO_15B = (
    "Vendredi, 16 h. Dernière heure de dissection de la semaine. La Pre Vautier fait le tour "
    "des tables avec un grand cahier relié de toile bleue : le livre des donneurs. Chaque "
    "table y écrira une page à la fin du semestre ; on la lira à la cérémonie de juin, "
    "devant les familles."
)
_INTRO_15B_VAUTIER = (
    "Vendredi, 16 h. Mardi matin, vous êtes allé·e avec Maëlle au bureau de la Pre Vautier, "
    "pour la story. Elle avait écouté sans rien dire, puis vous avait remercié·e·s. Depuis, "
    "rien. Dernière heure de dissection de la semaine : elle fait le tour des tables avec "
    "un grand cahier relié de toile bleue, le livre des donneurs."
)

S1_5B = S(6, "1.5 Le livre des donneurs", _INTRO_15B,
    focus=("rd", "co", "er"),
    slot="1.5",
    cond=when(none=["photo_virale"]),
    entries=[
        Entry(2, when(all=["maelle_vautier"]), _INTRO_15B_VAUTIER),
    ],
    nodes=[
        I(1, "vautier", "neutral",
          "Elle pose le cahier sur la paillasse de la table 14. « Vous écrirez votre page en "
          "décembre. Mais je veux que vous commenciez à y penser maintenant, pendant qu'elle "
          "est encore là. » Elle regarde Madame 14, puis vous. « Si sa famille lisait cette "
          "page, que voudriez-vous qu'elle y trouve ? »", [
            R("« Qu'elle était quelqu'un. »",
              3, "rd3 co2 cc1"),
            R("« Ce qu'on a appris grâce à elle, organe par organe, avec les termes exacts : "
              "c'est ce qui montre le mieux que son don n'a pas servi à rien. »",
              3, "cc1 rd1 em-1"),
            R("« Je n'en sais rien. Je ne la connais pas. »", 3, "rd-1 em-1"),
            R("« Merci, et c'est tout. Les grandes phrases, ça sert les vivants. »",
              3, "rd1 cc1"),
            R("« Que personne ne s'est moqué d'elle. Ce qui n'est pas tout à fait vrai. »",
              3, "rd2 pb2 er1"),
            R("« Franchement, il est un peu hypocrite, ce livre. »", 3, "rd-2 co-2 pb-1"),
        ]),
        I(2, "vautier", "neutral",
          "Elle pose le cahier sur la paillasse de la table 14 et attend que Maëlle relève la "
          "tête. « Cette semaine, deux étudiant·e·s sont venu·e·s me parler d'une photo "
          "retirée à temps. Je ne citerai personne. En vingt ans, j'ai reçu ce genre de "
          "visite trois fois. » Elle ouvre le cahier sur une page blanche. « Si sa famille "
          "lisait cette page, que voudriez-vous qu'elle y trouve ? »", [
            R("« La vérité : qu'on a failli la trahir, et qu'on s'est rattrapés à temps. »",
              3, "rd2 pb2 cc2 er1"),
            R("« Qu'on a remarqué ses mains. Le vernis. »", 3, "rd3 co2"),
            R("« Rien sur la photo, j'espère. »",
              3, "pb-1 cc-1 em1"),
            R("« Que c'était Maëlle, pas toute la table. »", 3, "ic-3 em-2 rd-1"),
            R("« Merci, et c'est tout. »", 3, "rd1 cc1"),
        ]),
        I(3, "maelle", "sad",
          "Vous ouvrez l'abdomen, plan après plan. Sous l'ombilic, une cicatrice horizontale, "
          "ancienne, blanchie : une césarienne. Léo la montre du bout de la sonde. Maëlle, "
          "tout bas : « Elle a eu un enfant. » Personne ne parle pendant un moment. « Quelqu'un, "
          "quelque part, a été cet enfant. »", [
            R("« Et c'est peut-être lui qui lui a verni les ongles. »", 4, "rd3 co3 em2 er1"),
            R("« Césarienne segmentaire transversale. Ça tombe à l'examen. »",
              4, "rd-1 cc1 em-1"),
            R("« On pourrait la retrouver, sa famille, avec la cicatrice et le tatouage : un "
              "avis de décès de fin d'été, une femme de quatre-vingts ans, une hirondelle. Ce "
              "serait fou, non ? »", 4, "rd-3 pb-3 em-1"),
            R("Laisser le silence durer un peu, avant de reprendre.", 4, "rd2 er1 co1"),
            R("En riant : « Arrête, Maëlle, tu vas me faire pleurer. »", 4, "er-1 rd-1"),
        ]),
        I(4, "maelle", "vulnerable",
          "Pendant que la Pre Vautier passe à la table suivante, Maëlle se penche vers vous. "
          "« Merci. Pour lundi. » Elle tripote son téléphone, éteint. « Je poste tout, tu "
          "sais. Si j'en fais une blague, ça devient pas réel. Lundi, j'ai eu peur toute la "
          "journée, alors j'ai posté. »", [
            R("« Moi aussi, j'ai eu peur. Mais ta blague retombait sur quelqu'un qui ne pouvait "
              "pas répondre. »", 5, "em2 rd2 pb1 er1"),
            R("« Pas de quoi. On oublie. »", 5, "em1"),
            R("« Tu devrais en parler à quelqu'un, de pourquoi tu postes tout. »", 5, "em1 ic1 pb-1"),
            R("« Tu me dois une bière. »", 5, "er1"),
            R("« Franchement, j'ai failli te dénoncer. »", 5, "em-2 ic-1 co-1"),
        ]),
        I(5, "noah", "anxious",
          "Noah a ouvert son carnet sur une page vierge. Il n'a rien écrit depuis vingt "
          "minutes. « Qu'est-ce qu'on écrit à quelqu'un qu'on a ouvert ? » Il rit, pas "
          "vraiment. « Mon père dirait : on écrit le compte rendu opératoire. »", [
            R("« On n'est pas obligés de trouver aujourd'hui. On l'écrira ensemble, en "
              "décembre. »", 6, "em2 co2 ic2"),
            R("« Écris merci. Personne ne te demande de la poésie. »", 6, "cc1 em-1"),
            R("« Ton père n'a pas l'air d'être une référence pour ça. »",
              6, "em1 rd-1 pb-1"),
            R("« Écris ce que tu as ressenti lundi. Même le malaise. »", 6, "em2 er1 cc1"),
            R("« Laisse, je l'écrirai pour toute la table. »", 6, "ic-2 em-1"),
        ]),
        I(6, "leo", "vulnerable",
          "Yasmine, sans lever les yeux de l'artère qu'elle dégage : « Moi, j'écris merci, et "
          "c'est tout. » Léo, tout bas : « À Zurich, à la Gedenkfeier, chaque table lisait "
          "trois mots. Danke. Merci. Grazie. Et puis une minute de silence. » Il rougit. "
          "« C'était… bien. »", [
            R("« Trois langues. Et chacun sa ligne ? »",
              7, "ic3 rd2 em1"),
            R("« On n'est pas à Zurich, Léo. »", 7, "ic-2 rd-2 em-1"),
            R("« Yasmine a raison : faisons simple. »", 7, "ic1"),
            R("Noter l'idée de Léo dans le cahier, avec son nom à côté, pour qu'on se souvienne "
              "que c'est lui qui l'a proposée quand on écrira la page en décembre.",
              7, "ic2 rd1 cc1"),
            R("Sourire à Léo, sans rien dire.", 7, "em1"),
        ]),
        I(7, "yasmine", "melancholic",
          "Yasmine pose ses pinces. « La minute de silence, je l'ai faite trop souvent. Au "
          "bord d'une route, à trois heures du matin, à côté d'un brancard. » Elle reprend ses "
          "pinces. « Faites votre page en trois langues. Moi, j'écrirai merci. »", [
            R("« Si tu veux en parler un jour, je suis là. »", 9, "em2 rd2 pb1 co1"),
            R("« Raconte. C'était quoi, la pire nuit, en ambulance ? »", 9, "pb-2 em-2 rd-1"),
            R("Hocher la tête, sans poser de question, et lui tendre la pince qu'elle "
              "cherche.", 9, "rd2 em1"),
            R("« T'as vu tellement de morts que ça ne te fait plus rien, ici, non ? Moi, à ta "
              "place, je serais blindé·e, depuis le temps, je ne sentirais même plus "
              "l'odeur. »", 9, "em-3 rd-2 pb-1 co-1"),
            R("« D'accord, va pour merci. »", 9, "ic1"),
        ]),
        I(9, "vautier", "neutral",
          "La Pre Vautier revient avec un autre cahier, plus ancien, à la toile délavée. Elle "
          "l'ouvre à une page de 2019 et la tourne vers la table. Une écriture ronde, des "
          "dessins de poumons, et cette ligne : « Merci Madame 7, grâce à vous j'ai eu 5,5 à "
          "l'examen 😂. » Elle referme. « Celle-là, une famille l'a lue en juin. » Elle vous "
          "regarde. « Qu'en pensez-vous ? »", [
            R("« Qu'elle parle de l'étudiant, pas de la donneuse. »", 10, "rd3 cc2 er1"),
            R("« C'est drôle. Elle aurait peut-être ri, elle aussi. »", 10, "rd-2 pb-1 em-1"),
            R("« Que la famille a dû avoir mal. Et qu'on ne fera pas ça. »",
              10, "rd2 co2 pb1"),
            R("« Que c'est maladroit, mais sincère : au fond, il la remercie vraiment, et une "
              "note de 5,5, c'est le résultat concret de son don, ça vaut bien un "
              "smiley. »", 10, "rd-1 cc-1 em1"),
            R("« Je n'en pense rien. Chacun écrit ce qu'il veut. »", 10, "rd-1 pb-1"),
        ]),
        I(10, "noah", "vulnerable",
          "Avant de partir, Noah vous montre son carnet. Il a écrit une seule ligne, d'une "
          "petite écriture serrée : « Pardon d'être tombé. Merci de m'avoir attendu. » Il "
          "attend votre réaction comme une note.", [
            R("« Garde-la. C'est la plus belle. »",
              8, "em2 co2 rd2"),
            R("« Tu ne lui dois pas pardon. Tu étais malade. »", 8, "em1 cc1"),
            R("« Il faudrait une deuxième phrase sur ce que tu as appris, pour que ce soit "
              "complet, sinon on dirait que tu ne parles que de ton malaise. »",
              8, "em-1 cc1 co-1"),
            R("« C'est un peu court. »", 8, "em-2 co-1"),
            R("Lui serrer l'épaule, sans rien dire.", 8, "em1 co2"),
        ]),
        I(8, "vautier", "neutral",
          "La Pre Vautier lit les lignes du cahier sans rien dire, puis recouvre Madame 14, "
          "lentement, en commençant par les mains. « À lundi. Elle vous attend. » Au "
          "vestiaire, Léo vous demande si vous voulez réviser l'anatomie avec lui ce "
          "week-end. C'est la première fois qu'il propose quelque chose à quelqu'un.", [
            R("« Avec plaisir. Samedi ? »", END, "ic2 em2"),
            R("« Pas ce week-end, mais la semaine prochaine, oui. »", END, "ic1 em1"),
            R("« Je révise seul·e, désolé·e. »", END, "ic-1 em-1"),
            R("« Pourquoi pas. On pourrait demander aux autres, aussi : Noah aurait bien "
              "besoin de réviser avec quelqu'un, et Yasmine connaît l'anatomie mieux que les "
              "assistants. »", END, "ic2 em-1"),
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 1.6 2 h 14 — histoire annexe (si Alex a soutenu Noah en 1.1)
# ---------------------------------------------------------------------------
S1_6 = S(7, "1.6 2 h 14",
    "Nuit de dimanche à lundi, 2 h 14. Votre téléphone s'allume sur la table de nuit. "
    "Noah.",
    focus=("em", "er", "pb"),
    slot="1.6",
    cond=when(all=["noah_soutenu"]),
    annex=True,
    nodes=[
        I(1, "noah", "anxious",
          "« t'es réveillé·e ? » Puis : « désolé ». Puis : « laisse tomber ».", [
            R("« Oui. Qu'est-ce qui se passe ? »", 2, "em2 cc1"),
            R("L'appeler.", 3, "em3 co2"),
            R("« Il est 2 h, Noah. Dors. »", 11, "em-2 co-1"),
            R("Ne pas répondre. Vous verrez demain.", 11, "em-1 co-1"),
            R("Envoyer un message vocal, à voix basse, en vous excusant d'avoir la voix "
              "endormie : « Je suis là, je ne dormais pas vraiment. Raconte, prends ton "
              "temps. »", 2, "em2 co1"),
        ]),
        I(2, "noah", "sad",
          "« je dors plus depuis lundi » « je sens le formol partout, même sous la douche » "
          "« je la vois quand je ferme les yeux » « et demain c'est l'abdomen »", [
            R("« Moi aussi, je sens le formol. Et j'ai rêvé d'elle jeudi. Tu n'es pas seul. »",
              4, "em2 er2 co2"),
            R("« C'est normal la première semaine. Ça passe. »", 4, "em1 cc-1"),
            R("« Prends un somnifère de tes parents. »",
              4, "pb-3 em-1 cc-1"),
            R("« Tu veux qu'on s'appelle ? »", 3, "em2 co1"),
            R("« Faut que t'arrêtes de dramatiser. »", 4, "em-3 co-2 rd-1"),
        ]),
        I(3, "noah", "sad",
          "Il décroche avant la première sonnerie et parle bas, pour ne pas réveiller sa "
          "colocataire. « Désolé. Je savais pas qui appeler. Je dors plus. Je sens le formol "
          "partout. » Un silence. « Et mon père a appelé ce soir. Quelqu'un lui a raconté "
          "lundi. Il voulait savoir mon rang au test d'anatomie de première. Il a dit : « Les "
          "vrais médecins ne tombent pas dans les pommes. » »", [
            R("« Ton père n'était pas là. Moi, si. »", 5, "em3 co2 er1"),
            R("« Il a peut-être raison. Il faut s'endurcir. »", 5, "em-3 co-2 er-1 rd-1"),
            R("« Qu'est-ce que tu lui as répondu ? »", 5, "em2 cc1"),
            R("L'écouter sans l'interrompre, jusqu'à ce qu'il ait fini.", 5, "em2 co2"),
            R("« Tu devrais couper les ponts avec lui, franchement : un père qui te parle "
              "comme ça à 2 h du matin, alors que tu ne dors plus, ça ne t'aide pas, ça te "
              "détruit. »", 5, "pb-2 rd-1 em1"),
        ]),
        I(4, "noah", "sad",
          "« mon père a appelé » « quelqu'un lui a raconté lundi » « il voulait mon rang au "
          "test d'anatomie de première » « il a dit que les vrais médecins tombent pas dans "
          "les pommes »", [
            R("« Ton père n'était pas dans la salle. Moi, j'y étais. Tu es resté jusqu'au "
              "bout. »", 5, "em3 co2 er1"),
            R("« Il a peut-être raison. Il faut s'endurcir. »", 5, "em-3 co-2 er-1 rd-1"),
            R("« Qu'est-ce que tu lui as répondu ? »", 5, "em2 cc1"),
            R("L'appeler, maintenant.", 3, "em2 co2"),
            R("« Tu devrais couper les ponts avec lui. »", 5, "pb-2 rd-1 em1"),
        ]),
        I(5, "noah", "anxious",
          "« Si je viens pas demain, tu signes pour moi la feuille de présence ? Juste "
          "demain. La dissection, c'est obligatoire, ils comptent les absences. »", [
            R("« Non. Mais je passe te chercher à 7 h 30, et on y va ensemble. Si c'est "
              "trop, on ressort. »",
              6, "pb3 em2 co2 ic1"),
            R("« OK. Juste demain. »", 6, "pb-3 rd-1 ic-2", sets=["signature_noah"]),
            R("« Je ne peux pas faire ça. Débrouille-toi. »", 7, "pb2 em-2 co-1"),
            R("« Écris à la Pre Vautier que tu ne te sens pas bien. Elle comprendra. »",
              6, "pb2 ic2 em1"),
            R("« On verra demain matin. »",
              7, "cc-2 pb-2"),
        ]),
        I(6, "noah", "vulnerable",
          "Un long silence. Puis : « ok ». Et : « tu dis rien aux autres ? pour ce soir ? »", [
            R("« Je ne dirai rien. Mais si tu vas vraiment mal, je t'aiderai. »", 8, "pb3 em1 co1 cc2", sets=["noah_confie"]),
            R("« Promis. Jamais. Quoi qu'il arrive. »", 8, "pb-2 em1 cc-1",
              sets=["noah_confie", "promesse_noah"]),
            R("« Les autres ont tous vu, de toute façon. »", 8, "em-2 rd-1 co-1"),
            R("« Tu devrais leur en parler, toi. Yasmine aussi a eu des nuits comme ça, je "
              "crois, avec l'ambulance : elle comprendrait mieux que moi, et tu ne serais pas "
              "seul à porter ça. »", 8, "ic1 em1 pb-1"),
            R("« Ça reste entre nous. Et tu as le droit d'écrire à 2 h du matin. »",
              8, "em2 co2 pb-1", sets=["noah_confie"]),
        ]),
        I(7, "noah", "sad",
          "« ok » « laisse » « bonne nuit ». Il se déconnecte. Vous fixez l'écran longtemps.", [
            R("« Attends. Je passe te chercher à 7 h 30. »", 8, "em2 co2 pb2"),
            R("Poser le téléphone face contre la table, et essayer de dormir.", END, "em-1 co-1"),
            R("« Désolé·e, il faut vraiment que je dorme, j'ai cours à 8 h. »", END, "er1 em-1"),
            R("Écrire à sa colocataire, que vous connaissez un peu, pour qu'elle passe le voir "
              "et vous dise s'il dort, sans lui dire pourquoi vous le lui demandez.",
              END, "pb-2 ic1 em1"),
        ]),
        I(8, "narr", "",
          "2 h 51. « Merci. » Puis, une minute plus tard, un message : « c'est bizarre mais "
          "je crois que je vais réussir à dormir ». Vous, non."),
        I(11, "noah", "ashamed",
          "Lundi, 7 h 10. Un message de Noah, envoyé à 4 h 02 : « oublie pour cette nuit. "
          "j'étais fatigué. ça va ». Puis, à 6 h 55 : « tu peux signer pour moi à la dissec ? "
          "juste aujourd'hui ».", [
            R("« Non. Mais je passe te chercher, et on y va ensemble. »", 9, "pb3 em1 co2"),
            R("Signer pour lui en arrivant.", 9, "pb-3 rd-1", sets=["signature_noah"]),
            R("Ne pas répondre.", 9, "em-2 co-1"),
            R("« Désolé·e pour cette nuit, je dormais vraiment. Pour la feuille, je ne sais "
              "pas : si c'est la Pre Vautier qui surveille, c'est non, mais si c'est un "
              "assistant, on verra. »", 9, "pb-2 cc-1 em1"),
            R("« Tu vas bien ? Pour de vrai ? »", 9, "em2 co1 cc1"),
        ]),
        I(9, "noah", "ashamed",
          "Le lendemain matin, Noah n'est pas au cours de 8 h. Il arrive à 10 h, les yeux "
          "rouges, et s'assied au fond de l'auditoire. Il ne vous regarde pas.", [
            R("S'asseoir à côté de lui. « Je suis là. »",
              10, "em3 co2 er1", sets=["noah_confie"]),
            R("« T'étais où, ce matin ? »", END, "em-1"),
            R("Ne rien dire.", END, "em-1 co-1"),
            R("« Désolé·e, je dormais. » Et passer à autre chose.", END, "em-2 co-1"),
            R("Lui envoyer un message depuis l'autre bout de l'auditoire, avec un émoji, pour "
              "qu'il sache que vous pensez à lui sans que personne autour ne le remarque.",
              END, "em1"),
        ]),
        I(10, "narr", "",
          "À midi, sur un banc devant l'institut, Noah vous raconte. Le formol, les nuits, "
          "son père. Pas tout. Assez pour que vous sachiez qu'il ne dort plus."),
    ],
)

CH1 = C(1, "Madame 14",
    situation=(
        "Septembre et octobre, début de la 2ᵉ année. Le lundi, la salle de dissection : un "
        "corps anonyme que la table 14 appelle « Madame 14 », une hirondelle tatouée au "
        "poignet. Le jeudi, le cabinet de médecine de famille de Montchéry, et Jeannine "
        "Pittet, 81 ans, ancienne sage-femme du village, qui a un secret."
    ),
    objectives=(
        "respecter la dignité et l'anonymat des personnes qui ont donné leur corps (gestes, "
        "paroles, images) ; réagir, vite et sans humilier, quand un·e pair franchit une "
        "limite ; soutenir un camarade en difficulté sans se substituer à une aide "
        "professionnelle ; se présenter comme étudiant·e et rester dans son rôle ; conduire "
        "le début d'une anamnèse en écoutant d'abord ; garder un secret confié par une "
        "patiente sans faire de promesse intenable ; reconnaître le savoir de l'assistante "
        "médicale et de l'infirmier à domicile."
    ),
    anchoring=(
        "UNIL BMed2.10 (TP anatomie), BMed2.1 (cellules et signaux : vieillissement, "
        "pathologie générale), BMed2.8 (anamnèse et communication) et BMed2.7 (rôle du "
        "médecin de famille et de l'équipe interprofessionnelle) · UNIGE TP d'anatomie, "
        "Croissance et vieillissement cellulaire, compétences cliniques, stage IMFE, identité "
        "professionnelle · UZH Praktikum klinische Anatomie I et Klinischer "
        "Untersuchungskurs I."
    ),
    focus=("rd", "em", "pb", "cc"),
    scenes=[S1_1, S1_2, S1_3, S1_4, S1_5A, S1_5B, S1_6],
)
