# Graphes End of Life

Structure des scénarios — Généré à partir de Chapters_v2-1.json

---

## Chapitre 1 : La rencontre

### Scénario : Présentation

```mermaid
flowchart TD
    I1["(Claude) Je suis devant la porte,..."]
    I2["(Agathe) On ne vous a jamais appris à frapper !"]
    I3["(Agathe) Agathe ne répond pas."]
    I4["(Agathe) ..."]
    I5["(Agathe) Agathe ne répond pas. Elle est dans son lit.…"]
    I6["(Agathe) Agathe ne répond pas."]
    I7["(Agathe) Agathe ne dit rien."]
    I8["(Agathe) Vous n’imaginez rien du tout. Vous n’avez pa…"]
    I9["(Agathe) Je veux rentrer chez moi !"]
    I10["(Agathe) Agathe se met en colère, son visage est roug…"]
    I11["(Agathe) Je suis perdue ici."]
    I12["(Agathe) J’avais mes habitudes, mes voisins, mon jard…"]
    I13["(Agathe) Agathe pleure."]
    I14["(Agathe) Mais qu’est-ce qui vous prends ? Je vous int…"]
    I15["(Agathe) Agathe soupire. Comment des enfants peuvent …"]
    I16["(Agathe) Agathe ne répond pas."]
    I17["(Agathe) Ma fille, elle a sa vie…"]
    I18["(Agathe) Agathe acquiesse."]
    I19["(Agathe) Agathe reste dans son silence."]
    I20["(Agathe) Agathe acquiesse."]
    I21["(Agathe) ..."]
    I22["(Agathe) ..."]

    I1 -->|"Je frappe"| I3
    I1 -->|"J'entre sans frappe…"| I2
    I2 -->|"Pardon"| I4
    I2 -->|"Je ne voulais pas d…"| I4
    I3 -->|"Entrer"| I4
    I4 -->|"Bonjour Madame Sala…"| I5
    I4 -->|"Bonjour, tout va bi…"| I5
    I4 -->|"Bonjour Madame Sala…"| I5
    I5 -->|"Je vois que vous n’…"| I6
    I5 -->|"Comment s’est passé…"| I6
    I5 -->|"Vous en faites une …"| I6
    I6 -->|"Je ne peux pas vous…"| I7
    I6 -->|"Je peux imaginer qu…"| I7
    I6 -->|"Si vous ne répondez…"| I7
    I7 -->|"Je ferais pareil."| I8
    I7 -->|"Quitter sa maison c…"| I8
    I7 -->|"J’imagine que c’est…"| I8
    I8 -->|"C'est vrai."| I9
    I8 -->|"C'est vrai mais j'a…"| I9
    I8 -->|"Peut-être préférez-…"| I21
    I8 -->|"Sur quel ton me par…"| I9
    I9 -->|"Ma grand-mère aussi…"| I10
    I9 -->|"Moi aussi, je serai…"| I11
    I9 -->|"Vous voulez rentrer…"| I11
    I9 -->|"Je comprend mais ce…"| I11
    I9 -->|"Votre état de santé…"| I10
    I10 -->|"Ne vous mettez pas …"| I21
    I10 -->|"Veuillez m’excuser."| I11
    I10 -->|"Je vais appeler mon…"| I21
    I11 -->|"Comment cela perdue…"| I12
    I11 -->|"Perdue."| I12
    I11 -->|"Vous trouverez de n…"| I12
    I11 -->|"Il y a des gens bie…"| I20
    I12 -->|"Et si on parlait un…"| I13
    I12 -->|"Vous vous réconcili…"| I13
    I12 -->|"Qu’est-ce qui vous …"| I13
    I12 -->|"Comme je suis trist…"| I13
    I12 -->|"Vous tombez bien, i…"| I13
    I13 -->|"Nous ferons tout po…"| I15
    I13 -->|"Votre tristesse me …"| I15
    I13 -->|"Ça va aller !"| I15
    I13 -->|"Se rapprocher pour …"| I13
    I14 -->|"Réconforter."| I15
    I14 -->|"Proposer de revenir…"| I20
    I15 -->|"Vous soupirez ?"| I16
    I15 -->|"Ils voulaient sûrem…"| I16
    I15 -->|"Vous vous sentez tr…"| I16
    I15 -->|"Probablement n’avai…"| I16
    I15 -->|"Vous exagérez un pe…"| I16
    I16 -->|"Puis-je vous faire …"| I20
    I16 -->|"Que dirait votre fi…"| I17
    I16 -->|"Vous ne dîtes rien !"| I19
    I16 -->|"Bon et bien je prop…"| I22
    I17 -->|"Vous aussi vous ave…"| I18
    I17 -->|"Oui elle a sa vie !"| I19
    I17 -->|"Laisser un silence"| I19
    I18 -->|"Puis-je vous faire …"| I20
    I18 -->|"Je dois faire votre…"| I20
    I19 -->|"Puis-je vous faire …"| I20
    I19 -->|"Je dois faire votre…"| I20
```

*22 nœuds, 60 arêtes*

---

### Scénario : Vite fait bien fait

```mermaid
flowchart TD
    I1["(Pascal) J’ai besoin que tu travailles plus rapidemen…"]
    I2["(Pascal) Bon, tâche à l’avenir de le faire plus rapid…"]
    I3["(Pascal) Je n’ai pas que ça à faire. Agis plus et par…"]
    I4["(Pascal) Merci Claude ! À l’avenir, il te faudra trav…"]
    I5["(Pascal) Si tu continues à contester mon autorité. Je…"]
    I6["(Pascal) Ça peut arriver ! À l’avenir, Il te faudra t…"]

    I1 -->|"Toutefois, je suis …"| I2
    I1 -->|"Les besoins de Mada…"| I2
    I1 -->|"Je n’ai pas vu le t…"| I6
    I1 -->|"Je fais du mieux qu…"| I2
    I2 -->|"Ça prend du temps d…"| I3
    I2 -->|"Je peux comprendre …"| I3
    I2 -->|"Je serais plus rapi…"| I4
    I2 -->|"Non, je préfère bie…"| I5
```

*6 nœuds, 8 arêtes*

---

### Scénario : Les soins

```mermaid
flowchart TD
    I1["(Claude) Vous êtes devant la porte."]
    I2["(Agathe) On ne vous a jamais appris à frapper !"]
    I3["(Agathe) Agathe ne me dit pas d’entrer."]
    I4["(Agathe) Agathe est dans son lit et me regarde sans d…"]
    I5["(Agathe) Agathe m’interromps d’une voix vive, en me r…"]
    I6["(Agathe) Mais je vous parle comme je veux. Ce n’est p…"]
    I7["(Agathe) Oui ça me convient ! Laissez les « Madame » …"]
    I8["(Agathe) Le ton vif, le regard pétillant, en remontan…"]
    I9["(Agathe) Agathe sourit. Vous avez quel âge, Claude ?"]
    I10["(Agathe) Je pourrais être votre grand-mère !"]
    I11["(Agathe) J’en suis navrée. Pouvez-vous changer mon pa…"]
    I12["(Agathe) J’avais bien compris. Pouvez-vous changer mo…"]
    I13["(Agathe) Agathe ne répond pas. Elle baisse les yeux c…"]
    I14["(Agathe) Allez-y doucement ! Mon pied me fait mal. Ça…"]
    I15["(Agathe) J’ai un petit-fils ! Mon petit-fils chéri, X…"]
    I16["(Agathe) Les larmes d’Agathe ne cessent de couler."]
    I17["(Agathe) Oui. Ça fait maintenant plus d’un mois qu’il…"]
    I18["(Agathe) Ça fait maintenant plus d’un mois qu’il est …"]
    I19["(Agathe) Il ne sait sûrement pas que je suis au home.…"]
    I20["(Agathe) Non, je n'ai pas envie de le déranger. Un pe…"]
    I21["(Agathe) Mais ma parole ! Vous êtes devine ? Ça vous …"]
    I22["(Agathe) Changez-moi ce pansement maintenant et allez…"]
    I23["(Agathe) Sa maman ! Mais je ne lui parle plus !"]
    I24["(Agathe) Elle a décidé de m’abandonner dans ce trou !"]
    I25["(Agathe) Ils n’avaient pas le droit de m’abandonner."]
    I26["(Agathe) Je me sens abandonnée !"]
    I27["(Agathe) Agathe ne répond pas. Elle semble plus calme…"]
    I28["(Agathe) Je sens mon cœur battre dedans."]
    I29["(Agathe) ..."]
    I30["(Agathe) ..."]
    I31["(Agathe) ..."]
    I32["(Agathe) ..."]
    I33["(Agathe) Laissez les « Madame » à la porte ! Je m’app…"]
    I34["(Agathe) Agathe ne répond rien. Je lui refais son pan…"]
    I35["(Agathe) Je ne parle plus à sa maman !"]

    I1 -->|"Je frappe à la port…"| I3
    I1 -->|"J’entre sans frappe…"| I2
    I2 -->|"Pardon, Madame Sala…"| I4
    I2 -->|"Je ne voulais pas v…"| I4
    I3 -->|"J'entre doucement"| I4
    I3 -->|"Je frappe plus fort"| I3
    I3 -->|"Je reviendrai plus …"| I32
    I4 -->|"Je viens pour la ré…"| I5
    I4 -->|"Il est temps de cha…"| I5
    I4 -->|"Montrez-moi votre p…"| I5
    I5 -->|"Pardon ?"| I33
    I5 -->|"Qu’est-ce que vous …"| I33
    I5 -->|"Moi non plus je ne …"| I33
    I5 -->|"Changez de ton avec…"| I6
    I6 -->|"Sans expérience, j’…"| I7
    I6 -->|"Je vous respecte et…"| I7
    I6 -->|"J’ai eu l’impressio…"| I33
    I6 -->|"Des règles permette…"| I33
    I7 -->|"Je viens pour la ré…"| I8
    I7 -->|"Il est l’heure de c…"| I8
    I7 -->|"Montrez-moi votre p…"| I8
    I7 -->|"J’ai encore beaucou…"| I8
    I8 -->|"J’ai 25 ans."| I10
    I8 -->|"Vous pouvez m’appel…"| I9
    I8 -->|"Laissez les « madam…"| I9
    I8 -->|"Cela m'étonnerais q…"| I13
    I9 -->|"J’ai 25 ans."| I10
    I9 -->|"J’ai 25 ans et je v…"| I10
    I10 -->|"Vous êtes grand-mèr…"| I13
    I10 -->|"Vous avez des petit…"| I13
    I10 -->|"Vous pourriez être …"| I13
    I10 -->|"Ma grand-mère est m…"| I11
    I10 -->|"Je suis votre infir…"| I12
    I11 -->|"Ça tape ?"| I28
    I11 -->|"Ce doit être infect…"| I28
    I11 -->|"Cela m’inquiète."| I28
    I12 -->|"Ça tape ?"| I28
    I12 -->|"Ce doit être infect…"| I28
    I12 -->|"Cela m’inquiète."| I28
    I13 -->|"Laisser le silence …"| I12
    I13 -->|"Répèter : Vous êtes…"| I15
    I13 -->|"Répèter : Vous avez…"| I15
    I13 -->|"Répèter : Vous pour…"| I28
    I13 -->|"Puis-je changer vot…"| I14
    I14 -->|"Ça tape ?"| I28
    I14 -->|"Ce doit être infect…"| I28
    I14 -->|"Cela m’inquiète."| I28
    I15 -->|"Prendre une chaisse…"| I16
    I15 -->|"Demander si changer…"| I14
    I15 -->|"Prendre congé et do…"| I32
    I16 -->|"Il compte beaucoup …"| I17
    I16 -->|"Qu’est-ce qui vous …"| I18
    I16 -->|"Laissez sortir tout…"| I18
    I17 -->|"Vous êtes sans nouv…"| I35
    I17 -->|"Qui pourrait avoir …"| I23
    I17 -->|"Il va vous contacte…"| I19
    I18 -->|"Vous êtes sans nouv…"| I35
    I18 -->|"Qui pourrait avoir …"| I23
    I18 -->|"Il va vous contacte…"| I19
    I19 -->|"Est-ce que vous vou…"| I20
    I19 -->|"Il le fera."| I21
    I20 -->|"Est-ce que c’est le…"| I14
    I20 -->|"Je dois maintenant …"| I14
    I20 -->|"Montrez-moi ce talo…"| I14
    I21 -->|"Je pensais vous con…"| I22
    I21 -->|"Je suis juste persu…"| I22
    I22 -->|"Ça tape ?"| I28
    I22 -->|"Ce doit être infect…"| I28
    I22 -->|"Cela m’inquiète."| I28
    I23 -->|"Vous ne parlez plus…"| I24
    I23 -->|"Pourquoi ne parlez-…"| I24
    I23 -->|"Voulez-vous que je …"| I24
    I24 -->|"Vous en voulez énor…"| I25
    I24 -->|"Que voulez-vous dir…"| I26
    I24 -->|"Vous ne croyez pas …"| I25
    I25 -->|"Que diraient vos en…"| I27
    I25 -->|"Qu’est-ce que vous …"| I27
    I26 -->|"Que diraient vos en…"| I27
    I26 -->|"Qu’est-ce que vous …"| I27
    I27 -->|"Est-ce que c’est le…"| I14
    I27 -->|"Je dois maintenant …"| I14
    I27 -->|"Montrez-moi ce talo…"| I14
    I28 -->|"Je vais d’abord enl…"| I29
    I28 -->|"Cela arrive parfois…"| I29
    I28 -->|"On va voir tout ça."| I29
    I29 -->|"Je retire le pansem…"| I30
    I30 -->|"C’est bien ce que j…"| I31
    I31 -->|"Je nettoie la plaie…"| I32
    I33 -->|"Je viens pour la ré…"| I8
    I33 -->|"Il est l’heure de c…"| I8
    I33 -->|"Montrez-moi votre p…"| I8
    I33 -->|"J’ai encore beaucou…"| I8
    I35 -->|"Vous ne parlez plus…"| I24
    I35 -->|"Pourquoi ne parlez-…"| I24
    I35 -->|"Voulez-vous que je …"| I24
```

*35 nœuds, 95 arêtes*

---

### Scénario : Le dîner

```mermaid
flowchart TD
    I1["(Agathe) Vous allez venir vingt fois par jour ! Vous …"]
    I2["(Agathe) Avec les Zinzins ! Non mais vous m’avez vu !…"]
    I3["(Agathe) Oui ! Laissez-moi !"]
    I4["(Agathe) Quoi ?"]
    I5["(Agathe) Agathe sourit."]
    I6["(Agathe) ..."]

    I1 -->|"Je venais vous prop…"| I2
    I1 -->|"Je vous propose d’a…"| I2
    I1 -->|"Pardon Agathe. Je v…"| I6
    I1 -->|"Arrêtez de me parle…"| I2
    I2 -->|"Vous préférez mange…"| I3
    I2 -->|"Je comprends. Alors…"| I6
    I2 -->|"J’ai compris son me…"| I6
    I3 -->|"Agathe."| I4
    I3 -->|"Oui, je vous laisse…"| I6
    I3 -->|"Sortir"| I6
    I4 -->|"Je suis heureuse de…"| I5
    I5 -->|"Je suis heureuse de…"| I6
    I5 -->|"Je vous fais amener…"| I6
```

*6 nœuds, 13 arêtes*

---

## Chapitre 2 : Vivre en EMS

### Scénario : Lieu de vie, lieu de mort

```mermaid
flowchart TD
    I1["(Claude) Claude frappe à la porte d’Agathe puis entre"]
    I2["(Agathe) Bonjour Claude. Je peine à trouver le sommei…"]
    I3["(Agathe) ..."]
    I4["(Agathe) Je n’ai pas bien dormi, mais c'est bien norm…"]
    I5["(Agathe) Agathe d'un ton vif et rapide. Mais, mais, m…"]
    I6["(Agathe) Agathe tourne la tête ostensiblement et rega…"]
    I7["(Agathe) Mon mari me manque. J’aimerais le rejoindre!…"]
    I8["(Agathe) Vous comprenez mes enfants ont leur vie. Ils…"]
    I9["(Agathe) ..."]
    I10["(Agathe) Qui choisit vraiment d'aller en home ? Seule…"]
    I11["(Agathe) Que je suis bien ici. Qu’il y a des gens qui…"]
    I12["(Agathe) Tous ceux qui sont venus aux Lilas sont mort…"]
    I13["(Agathe) Je sais pas ce que je fais ici ! Les vieux v…"]
    I14["(Agathe) Agathe la regarde attentivement, surprise pa…"]
    I15["(Agathe) Ils ont pas eu le choix ! Mais ils pouvaient…"]
    I16["(Agathe) Il est mort trois jours après !"]
    I17["(Agathe) Oui et ça me fait peur !"]
    I18["(Agathe) Séraphine du boulanger ?"]
    I19["(Agathe) Agathe soupire. Vous percevez Agathe plus dé…"]
    I20["(Agathe) Agathe reste silencieuse."]
    I21["(Agathe) Agathe regarde Claude en secouant la tête et…"]
    I22["(Agathe) ..."]
    I23["(Agathe) Je pense qu’ils doivent être soulagés. Silen…"]
    I24["(Agathe) Ça va mieux ! Merci Claude."]
    I25["(Agathe) Oui c’est ça !"]
    I26["(Agathe) Revoir mon petit-fils ! Pouvoir choisir ce q…"]
    I27["(Agathe) Oh oui, je tiens absolument à le revoir avan…"]
    I28["(Agathe) Après quelques minutes de silence Agathe rép…"]
    I29["(Agathe) Agathe la regarde toujours, son sourire à di…"]
    I30["(Agathe) Agathe acquiesce d'un signe de tête, tout en…"]
    I31["(Agathe) Je m’occupais de mon ménage, de mon jardin, …"]
    I32["(Agathe) ..."]
    I33["(Agathe) J’aimerais bien continuer à discuter avec vo…"]
    I34["(Agathe) Mais quand ?"]
    I35["(Agathe) Mais ça veut dire que je ne vous verrai pas …"]
    I36["(Agathe) Merci Claude. Au revoir."]
    I37["(Agathe) ..."]
    I38["(Agathe) ..."]

    I1 -->|"Saluer Agathe"| I2
    I1 -->|"Bonjour ! Alors Aga…"| I2
    I1 -->|"Bonjour Agathe, pas…"| I2
    I2 -->|"S’accroupir devant …"| I3
    I2 -->|"S'approcher du bord…"| I3
    I2 -->|"S'approcher d'Agath…"| I3
    I3 -->|"Vous me semblez tri…"| I7
    I3 -->|"Il me semble que vo…"| I4
    I3 -->|"La veilleuse a obse…"| I5
    I4 -->|"Seule !"| I8
    I4 -->|"Vous éprouvez un se…"| I9
    I4 -->|"Que pensez-vous que…"| I11
    I4 -->|"Je me demande ce qu…"| I10
    I4 -->|"Avez-vous déjà pens…"| I5
    I5 -->|"Je vous ai mal comp…"| I7
    I5 -->|"Je ne vous comprend…"| I6
    I6 -->|"..."| I12
    I7 -->|"Seule !"| I8
    I7 -->|"Vous éprouvez un se…"| I9
    I7 -->|"Que pensez-vous que…"| I11
    I7 -->|"Je me demande ce qu…"| I10
    I7 -->|"Avez-vous déjà pens…"| I5
    I8 -->|"Qu’est-ce qui renfo…"| I13
    I8 -->|"Avec ce sentiment i…"| I12
    I8 -->|"Cela vous attriste ?"| I13
    I9 -->|"Que pensez-vous que…"| I8
    I9 -->|"Je me demande ce qu…"| I10
    I10 -->|"Vous m’avez dit que…"| I22
    I10 -->|"Bon et ce sentiment…"| I22
    I10 -->|"Du coup en plus de …"| I22
    I11 -->|"Que pensez-vous que…"| I23
    I11 -->|"Pensez-vous que vos…"| I23
    I11 -->|"Et vous pensez à ce…"| I23
    I12 -->|"Que diraient les vi…"| I15
    I12 -->|"Que diraient ceux c…"| I15
    I12 -->|"Pleins d'autre ont …"| I15
    I13 -->|"Pour vous, c’est se…"| I12
    I13 -->|"Le home, n'est-il p…"| I12
    I13 -->|"C'est vrai..."| I14
    I13 -->|"Les larmes aux yeux…"| I37
    I14 -->|"Que diraient les vi…"| I15
    I14 -->|"Que diraient ceux c…"| I15
    I14 -->|"Pleins d'autre ont …"| I15
    I15 -->|"Comment ça s’est pa…"| I16
    I15 -->|"S'est-il plû aux Li…"| I16
    I15 -->|"Je suis sûre que so…"| I16
    I16 -->|"Est-ce que vous ima…"| I17
    I16 -->|"Vous êtes en pleine…"| I17
    I16 -->|"Arrêtez voir de vou…"| I17
    I17 -->|"Je comprends bien v…"| I18
    I17 -->|"Vous dîtes n'import…"| I18
    I17 -->|"Je suis sûre que vo…"| I18
    I18 -->|"Oui ! Et bien, Séra…"| I19
    I18 -->|"Elle-même ! Vous vo…"| I19
    I18 -->|"Oui et elle ne pass…"| I19
    I19 -->|"Vous pourriez m’en …"| I10
    I19 -->|"Personne ne choisir…"| I20
    I19 -->|"Pourquoi pas le hom…"| I21
    I20 -->|"Vous m’avez dit que…"| I22
    I20 -->|"Bon et ce sentiment…"| I22
    I20 -->|"Du coup en plus de …"| I22
    I21 -->|"Reprenons notre dis…"| I25
    I21 -->|"Alors vous êtes d'a…"| I25
    I21 -->|"Ici c'est donc votr…"| I25
    I22 -->|"Que diraient vos en…"| I11
    I22 -->|"Et vos enfants, que…"| I11
    I22 -->|"Vous et votre aband…"| I11
    I23 -->|"Et vous, comment vo…"| I24
    I23 -->|"Du coup ça va comme…"| I24
    I23 -->|"Bon, ça vous a aidé…"| I24
    I24 -->|"Reprenons notre dis…"| I25
    I24 -->|"Alors vous êtes d'a…"| I25
    I24 -->|"Ici c'est donc votr…"| I25
    I25 -->|"Mais avant d’y mour…"| I26
    I25 -->|"Vous allez évidemen…"| I26
    I25 -->|"Arrêtez donc de pen…"| I26
    I26 -->|"Vous aimeriez revoi…"| I27
    I26 -->|"Comment cela vivre …"| I28
    I26 -->|"Vous ne pouvez pas …"| I29
    I26 -->|"Rêver ?"| I30
    I27 -->|"Je suis venu pour l…"| I33
    I27 -->|"Bon le temps passe,…"| I33
    I27 -->|"Allez on reprend je…"| I33
    I28 -->|"Cela sera plus faci…"| I34
    I28 -->|"On reprendra le tem…"| I34
    I28 -->|"Bon arrêtez de vous…"| I34
    I30 -->|"Comment vous viviez…"| I31
    I30 -->|"Chez vous, c'était …"| I31
    I31 -->|"Je retrouve ce que …"| I32
    I31 -->|"Exactement comme mo…"| I32
    I32 -->|"Je suis venu pour l…"| I33
    I32 -->|"Bon le temps passe,…"| I33
    I32 -->|"Allez on reprend je…"| I33
    I33 -->|"Je comprends bien m…"| I38
    I33 -->|"Un peu agacée, vous…"| I38
    I33 -->|"Vous acquiescez d’u…"| I38
    I34 -->|"Jeudi après les soi…"| I35
    I34 -->|"Jeudi dans la journ…"| I35
    I34 -->|"Après-demain Agathe."| I35
    I35 -->|"Non, le mercredi c’…"| I36
    I35 -->|"Non, demain je me r…"| I36
    I35 -->|"Non, j'ai un jour d…"| I36
    I38 -->|"Cela sera plus faci…"| I34
    I38 -->|"On reprendra le tem…"| I34
    I38 -->|"Bon arrêtez de vous…"| I34
```

*38 nœuds, 105 arêtes*

---

### Scénario : Projet de vie

```mermaid
flowchart TD
    I1["(Claude) ..."]
    I2["(Agathe) Mais attendez donc que je vous réponde ! Que…"]
    I3["(Agathe) Je vais finir par me fâcher et m'adressez à …"]
    I4["(Agathe) Agathe est dans son fauteuil : Gentiment."]
    I5["(Agathe) Oui, ça va, je m’ennuie un peu."]
    I6["(Agathe) Tout à fait."]
    I7["(Agathe) Agathe se lève et s’installe dans son lit. C…"]
    I8["(Agathe) Agathe soupire."]
    I9["(Agathe) Oui, avec mon diabète, vous savez j’avais pe…"]
    I10["(Agathe) Oui, qu’on m’ampute !!! Agathe attrape son d…"]
    I11["(Agathe) Oui que je sois amputée, avec le diabète on …"]
    I12["(Agathe) Pas vraiment. Je me rappelle… que vous aviez…"]
    I13["(Agathe) Agathe sourit, ses yeux brillent, pétillent…"]
    I14["(Agathe) Agathe, des étoiles dans les yeux. Rêver !"]
    I15["(Agathe) Rimbaud, Baudelaire… J’aime les mots. Voler …"]
    I16["(Agathe) Non, non, je ne souhaite déranger personne ……"]
    I17["(Agathe) J’ai beaucoup lu dans ma vie. Des poèmes ! Ç…"]
    I18["(Agathe) Oh oui ! Je serais ravie."]
    I19["(Agathe) Vous feriez ça pour moi ! Merci Claude ! Du …"]
    I20["(Agathe) Xavier ! Il est parti travailler aux Etats-U…"]
    I21["(Agathe) Oui, les lettres sont grandes, c’est plus fa…"]
    I22["(Agathe) Oui nous avions pris l’habitude de jouer ens…"]
    I23["(Agathe) Oui, si je suis libre d’y aller quand je veu…"]
    I24["(Agathe) Je suis obligée de prendre mes médicaments q…"]
    I25["(Agathe) Agathe sourit."]
    I26["(Agathe) C'est tout ou rien, je l'ai fait jusqu'à pré…"]
    I27["(Agathe) C'est tout ou rien, je l'ai fait jusqu'à pré…"]
    I28["(Agathe) C'est tout ou rien, je l'ai fait jusqu'à pré…"]
    I29["(Agathe) Oui merci Claude. Je salue Agathe et je sors…"]
    I30["(Agathe) Je comprends. Merci pour votre temps. Je sal…"]
    I31["(Agathe) Je suis en paix avec eux ! Ils me manquent !"]
    I32["(Agathe) J’appellerai Margot aujourd’hui. La dernière…"]
    I33["(Agathe) Ma foi je ne sais pas si je me souviens de t…"]
    I34["(Agathe) Je ne pensais pas pouvoir encore vivre de bo…"]
    I35["(Agathe) ..."]
    I36["(Agathe) J’ai le sentiment de ne plus avoir de famill…"]
    I37["(Agathe) Oui, je ne sais pas trop quoi faire ici."]
    I38["(Agathe) C’est, vrai, ma maison, mon jardin me manque…"]
    I39["(Agathe) Justement, avant de venir ici, je n'ai jamai…"]
    I40["(Agathe) Il ne s’agit pas de ça… Agathe secoue la têt…"]

    I1 -->|"Prendre du temps po…"| I4
    I1 -->|"Prendre un temps po…"| I2
    I1 -->|"Prendre un temps po…"| I2
    I2 -->|"Excusez-moi, je sui…"| I3
    I2 -->|"Excusez-moi, je sui…"| I3
    I2 -->|"Excusez-moi, j'oubl…"| I3
    I3 -->|"J'entends bien, je …"| I6
    I3 -->|"Dites m'en plus Aga…"| I37
    I3 -->|"Je vous entends Aga…"| I38
    I3 -->|"Qu’aimiez-vous donc…"| I39
    I4 -->|"Gentiment."| I5
    I4 -->|"Êtes-vous en colère…"| I5
    I5 -->|"J'entends bien, je …"| I6
    I5 -->|"Dites m'en plus Aga…"| I37
    I5 -->|"Je vous entends Aga…"| I38
    I5 -->|"Qu’aimiez-vous donc…"| I39
    I5 -->|"L'animatrice ne vou…"| I40
    I6 -->|"Bien. Je vais faire…"| I7
    I6 -->|"Couchez-vous s'il v…"| I7
    I6 -->|"Allez, laissez moi …"| I7
    I7 -->|"Votre pied va mieux…"| I8
    I7 -->|"Votre pied va mieux…"| I8
    I8 -->|"Vous êtes soulagée."| I9
    I8 -->|"Quel soupire !"| I9
    I9 -->|"Vous aviez très peu…"| I10
    I9 -->|"Aviez-vous si peur ?"| I11
    I10 -->|"Vous souvenez-vous …"| I12
    I10 -->|"Vous rappelez-vous …"| I12
    I10 -->|"Bon on reprend la d…"| I12
    I11 -->|"Vous souvenez-vous …"| I12
    I11 -->|"Vous rappelez-vous …"| I12
    I11 -->|"Bon on reprend la d…"| I12
    I12 -->|"Oui et nous avons r…"| I13
    I12 -->|"Oui mais sourtout c…"| I13
    I13 -->|"Quel sourire ! Vous…"| I14
    I13 -->|"Je vous vois revivr…"| I14
    I14 -->|"Qu’est-ce qui vous …"| I15
    I14 -->|"Et de quoi rêvez-vo…"| I15
    I14 -->|"Dites m'en plus."| I15
    I15 -->|"Est-ce que vous lis…"| I17
    I15 -->|"Nous avons une bibl…"| I16
    I16 -->|"Vous auriez plaisir…"| I18
    I16 -->|"Aimeriez-vous que l…"| I18
    I16 -->|"Et si on vous lisai…"| I18
    I17 -->|"Vous auriez plaisir…"| I18
    I17 -->|"Aimeriez-vous que l…"| I18
    I17 -->|"Et si on vous lisai…"| I18
    I18 -->|"Je vais en parler à…"| I19
    I18 -->|"Vous pourrez en par…"| I19
    I19 -->|"Je vous en prie, Ag…"| I20
    I19 -->|"Pas de soucis ! Un …"| I20
    I20 -->|"Vous jouez au scrab…"| I21
    I20 -->|"Xavier et vous joui…"| I22
    I21 -->|"Vous voudriez peut-…"| I23
    I21 -->|"Jouez au scarbble a…"| I23
    I22 -->|"Cela me rappelle le…"| I23
    I22 -->|"C'est toujours symp…"| I23
    I23 -->|"C’est important que…"| I24
    I23 -->|"N'oubliez pas que p…"| I24
    I23 -->|"Bien entendu que vo…"| I24
    I24 -->|"Je vais en parler à…"| I25
    I24 -->|"Nous pourrions voir…"| I26
    I24 -->|"Nous sommes garante…"| I27
    I24 -->|"Vous pourriez peut …"| I28
    I24 -->|"Il est mieux que no…"| I30
    I25 -->|"Comment vous sentez…"| I31
    I25 -->|"Vous pensez toujour…"| I31
    I26 -->|"Comment vous sentez…"| I31
    I26 -->|"Vous pensez toujour…"| I31
    I27 -->|"Pensez-vous que nou…"| I29
    I27 -->|"On a fait le tour ?"| I29
    I31 -->|"Avez-vous songé à l…"| I32
    I31 -->|"Ils vous manquent ?"| I36
    I32 -->|"Faire un résumé de …"| I34
    I32 -->|"Faire un résumé de …"| I29
    I32 -->|"Agathe, pourriez-vo…"| I33
    I33 -->|"Faire un résumé de …"| I34
    I33 -->|"Faire un résumé de …"| I29
    I34 -->|"Je vous en prie Aga…"| I35
    I36 -->|"Vous souhaitez revo…"| I32
    I36 -->|"Maintenant vous vou…"| I32
    I37 -->|"J'entends bien, je …"| I6
    I37 -->|"Je vous entends Aga…"| I38
    I37 -->|"Qu’aimiez-vous donc…"| I39
    I37 -->|"L'animatrice ne vou…"| I40
    I38 -->|"Nous devons nous vo…"| I6
    I38 -->|"Allez on s'y met. V…"| I6
    I38 -->|"C'est à votre tour …"| I6
    I39 -->|"Bien. Je vais faire…"| I7
    I39 -->|"Couchez-vous s'il v…"| I7
    I39 -->|"Allez, laissez moi …"| I7
```

*40 nœuds, 91 arêtes*

---

### Scénario : Culpabilité des proches

```mermaid
flowchart TD
    I1["(Claude) Elle se dirige vers elle et engage la conver…"]
    I2["(Margot) Bonjour, je suis sa fille, Margot. Maman s’e…"]
    I3["(Margot) Bonjour, maman s’est endormie. Elle a l’air …"]
    I4["(Margot) Non, mais je la trouve changée, elle respire…"]
    I5["(Margot) Margot s’agite, secoue la tête. Elle est au …"]
    I6["(Margot) Non, mais je la trouve changée, elle respire…"]
    I7["(Margot) Non ce n'est pas ce que je voulais dire… Non…"]
    I8["(Margot) ..."]
    I9["(Margot) Excusez-moi de vous avoir dérangée ! Margot …"]
    I10["(Margot) J’en suis responsable ! Je m’en veux ! Je n’…"]
    I11["(Margot) Oui et je ne me sens pas bien avec cela"]
    I12["(Margot) Ne me dites surtout pas que je suis trop sen…"]
    I13["(Margot) Oui, je veux bien !"]
    I14["(Margot) Merci ! dit Margot en s'asseyant"]
    I15["(Margot) Margot en l'apercevant ainsi se lève et dit …"]
    I16["(Margot) Ma maman vous a dit que je l’avais abandonné…"]
    I17["(Margot) J'avais tellement pensée la voire mourir à l…"]
    I18["(Margot) Mieux que ce que je pensais. J’étais très ét…"]
    I19["(Margot) J’ai organisé son entrée en EMS. C’est à cau…"]
    I20["(Margot) C’est exactement ça ! J’aurais dû la prendre…"]
    I21["(Margot) Est-ce que ce n’est pas le rôle des enfants …"]
    I22["(Margot) Oui mais ce n'est pas ce que désire ma maman…"]
    I23["(Margot) Ecoutez, je vais l'accueillir à la maison, d…"]
    I24["(Margot) Elle est en sécurité. Elle est en contact av…"]
    I25["(Margot) Elle perd en autonomie. Margot baisse la têt…"]
    I26["(Margot) Je me rends compte qu’on a choisi la moins m…"]
    I27["(Margot) Non, oui, je ne sais pas vraiment… elle semb…"]
    I28["(Margot) Elle est quelque peu agressive ! Ce n'est pa…"]
    I29["(Margot) Comment ?"]
    I30["(Margot) Ecoutez, je vais l'accueillir à la maison, d…"]
    I31["(Margot) Margot me remercie pour mon temps et s'en va…"]
    I32["(Margot) Margot ne se sent à l'évidence pas écoutée e…"]
    I33["(Margot) Margot se lève et me répond : Vous avez prob…"]
    I34["(Margot) ..."]
    I35["(Margot) Je serais plus proche d’elle. Je la verrais …"]
    I36["(Margot) Je serais obligée de transformer la chambre …"]
    I37["(Margot) J'ai pris ma décision ! Vous commencez à dis…"]

    I1 -->|"Saluer Margot"| I3
    I1 -->|"Demander l'identité…"| I2
    I2 -->|"Agathe vit un grand…"| I4
    I2 -->|"Que dirait-elle si …"| I16
    I2 -->|"Vous a-t-elle expri…"| I4
    I2 -->|"Qu'est-ce qui vous …"| I6
    I2 -->|"Tout est nouveau ic…"| I7
    I3 -->|"Agathe vit un grand…"| I4
    I3 -->|"Que dirait-elle si …"| I16
    I3 -->|"Vous a-t-elle expri…"| I4
    I3 -->|"Qu'est-ce qui vous …"| I6
    I3 -->|"Tout est nouveau ic…"| I7
    I4 -->|"Je me dis que la fi…"| I34
    I4 -->|"Vous la voyez chang…"| I10
    I4 -->|"Je me demande pourq…"| I5
    I5 -->|"Je vois que cette s…"| I6
    I5 -->|"Je vois que cette s…"| I11
    I5 -->|"Cette situation ne …"| I12
    I6 -->|"Je vois que cette s…"| I13
    I6 -->|"Je vois que cette s…"| I11
    I6 -->|"Cette situation ne …"| I12
    I7 -->|"Je vous ai donc mal…"| I8
    I7 -->|"Je n'ai pas suivi."| I8
    I7 -->|"Je crois que nous a…"| I8
    I8 -->|"Je pense qu'il est …"| I34
    I8 -->|"J'attends une expli…"| I9
    I10 -->|"Je vois que cette s…"| I6
    I10 -->|"Je vois que cette s…"| I11
    I10 -->|"Cette situation ne …"| I12
    I11 -->|"Cela vous dirait de…"| I13
    I11 -->|"J'ai un peu de temp…"| I13
    I11 -->|"Si on se dépêche no…"| I13
    I12 -->|"..."| I9
    I13 -->|"Allons dans mon bur…"| I14
    I13 -->|"Dans mon bureau cel…"| I14
    I14 -->|"S'asseoir juste à c…"| I16
    I14 -->|"Rester debout devan…"| I15
    I14 -->|"S'installer derrièr…"| I15
    I15 -->|"Dites-moi ce qui vo…"| I16
    I15 -->|"N’avez-vous plus en…"| I32
    I16 -->|"Ce que votre maman …"| I18
    I16 -->|"Vous avez le sentim…"| I19
    I16 -->|"Cela doit être très…"| I17
    I16 -->|"Ce que vous me dite…"| I21
    I16 -->|"Votre maman était p…"| I33
    I17 -->|"L'idée que votre ma…"| I20
    I17 -->|"Pensez-vous vraimen…"| I20
    I17 -->|"Mourir à la maison"| I20
    I18 -->|"Qu’est-ce que vous …"| I19
    I18 -->|"C'est à dire ?"| I19
    I18 -->|"Que sous-entendez-v…"| I19
    I19 -->|"Votre maman ne pouv…"| I20
    I19 -->|"Votre maman ne pouv…"| I20
    I20 -->|"Héberger votre mère…"| I21
    I20 -->|"Soyez réaliste, viv…"| I21
    I21 -->|"Quels seraient les …"| I35
    I21 -->|"S'il s'agissait de …"| I22
    I21 -->|"Je ne sais pas vrai…"| I23
    I21 -->|"Les places en home …"| I37
    I22 -->|"Quelles difficultés…"| I36
    I22 -->|"Ne serait-elle pas …"| I36
    I23 -->|"Quels sont les avan…"| I24
    I23 -->|"Ne voyez-vous donc …"| I24
    I23 -->|"Il y a quand même d…"| I24
    I24 -->|"Y voyiez-vous alors…"| I25
    I25 -->|"Et si on regarde le…"| I26
    I25 -->|"Vous avez l'impress…"| I27
    I25 -->|"Ne vous semble-t-il…"| I28
    I25 -->|"Nous veillerons à c…"| I29
    I26 -->|"..."| I31
    I27 -->|"..."| I31
    I28 -->|"..."| I31
    I29 -->|"Je ne sais pas vrai…"| I30
    I29 -->|"Je ne sais pas moi …"| I30
    I34 -->|"Je vois que cette s…"| I6
    I34 -->|"Je vois que cette s…"| I11
    I34 -->|"Cette situation ne …"| I12
    I35 -->|"Quelles difficultés…"| I36
    I35 -->|"Ne serait-elle pas …"| I36
    I36 -->|"Quels seraient les …"| I24
    I36 -->|"Ne pensez-vous donc…"| I24
```

*37 nœuds, 81 arêtes*

---

## Chapitre 3 : La fin de vie

### Scénario : Les dernières volontés

```mermaid
flowchart TD
    I1["(Claude) Claude est maintenant devant la porte de la …"]
    I2["(Agathe) Claude, je suis contente de vous voir."]
    I3["(Agathe) C’est difficile. J’ai de la peine à respirer…"]
    I4["(Agathe) Oui, partir."]
    I5["(Agathe) Oui."]
    I6["(Agathe) J’ai le souffle court. Le médecin m’a mis so…"]
    I7["(Agathe) Non, mais je veux pas être réanimée ! Je veu…"]
    I8["(Agathe) Oui."]
    I9["(Agathe) Je ne veux pas devenir un légume ! Je veux c…"]
    I10["(Agathe) Agathe regarde le plafond. Son regard est ré…"]
    I11["(Agathe) J’aimerais que vous me fassiez la piqure."]
    I12["(Agathe) Oui, maintenant."]
    I13["(Agathe) Vous m’avez donné des nouveaux médicaments !…"]
    I14["(Agathe) ..."]
    I15["(Agathe) Oui, c’est pour ça que je veux mourir mainte…"]
    I16["(Agathe) Oui et ça me fait peur."]
    I17["(Agathe) Mais pourquoi faire ?"]
    I18["(Agathe) Mais je suis pas en état d’écrire quoi que c…"]
    I19["(Agathe) Je sais pas ce que c’est."]
    I20["(Agathe) Je sais pas si j’en suis capable."]
    I21["(Agathe) Je ne veux pas mourir étouffée."]
    I22["(Agathe) Mais je vous ai dit que je ne voulais pas de…"]
    I23["(Agathe) Aidez-moi à respirer et faîtes-moi voir ces …"]
    I24["(Agathe) Agathe soupire. Son visage manifeste de l’in…"]

    I1 -->|"Frappe et entre"| I2
    I2 -->|"Moi aussi, Agathe,"| I3
    I3 -->|"Vous en aller ?"| I4
    I4 -->|"Vous avez l’impress…"| I5
    I5 -->|"Qu’est-ce qui vous …"| I6
    I6 -->|"Le médecin vous a b…"| I7
    I7 -->|"Claude prend une ch…"| I8
    I8 -->|"Est-ce que vous ave…"| I9
    I9 -->|"Vous voulez choisir…"| I10
    I10 -->|"Qu’est-ce que vous …"| I11
    I11 -->|"Vous aimeriez que j…"| I12
    I12 -->|"Est-ce qu’il y a en…"| I13
    I13 -->|"Agathe, ce que vous…"| I14
    I14 -->|"Mourir étouffée, ce…"| I15
    I15 -->|"Si je résume un peu"| I16
    I16 -->|"Agathe, est-ce que …"| I17
    I17 -->|"Pour que l’on puiss…"| I18
    I18 -->|"Je peux vous aider …"| I19
    I19 -->|"C’est mettre par éc…"| I20
    I20 -->|"Je peux vous aider."| I21
    I21 -->|"Nous pouvons vous p…"| I22
    I22 -->|"L’un n’empêche pas …"| I23
    I23 -->|"Très bien Agathe"| I24
```

*24 nœuds, 23 arêtes*

---

### Scénario : Les professionnels face à la mort

```mermaid
flowchart TD
    I1["(Pascal) Salut Claude. Je sors d’une séance avec la d…"]
    I2["(Pascal) Oui, dix mais pas quinze. Pascal ferme la po…"]
    I3["(Pascal) Oui, elle n’a pas changé. Tu as bien fait."]
    I4["(Pascal) De tes valeurs ?"]
    I5["(Pascal) Oui, mais là elle ne veut plus être soignée."]
    I6["(Pascal) Tu lui as proposé de la soulager ?"]
    I7["(Pascal) Agathe est une personne capable de discernem…"]
    I8["(Pascal) Encore une fois tu n’es pas responsable de s…"]
    I9["(Pascal) Nos clients meurent ici que tu le veuilles o…"]
    I10["(Pascal) Bien sûr, mais cela touche une minorité de c…"]
    I11["(Pascal) Non, surtout pas."]
    I12["(Pascal) Oui, tu peux par contre soutenir Agathe dans…"]
    I13["(Pascal) Il ne s’agit pas de toi mais d’Agathe."]
    I14["(Pascal) Là, je trouve que tu exagères. Et en plus le…"]
    I15["(Pascal) Je t’en prie. Il sort, pressé comme à son ha…"]

    I1 -->|"C’est une bonne nou…"| I2
    I2 -->|"Je ne me sens pas t…"| I3
    I3 -->|"Je suis soulagée"| I4
    I4 -->|"Je suis très embarr…"| I5
    I5 -->|"Pascal, j’ai l’impr…"| I6
    I6 -->|"Oui, bien sûr !"| I7
    I7 -->|"Je sais tout ça."| I8
    I8 -->|"Mais enfin Pascal,"| I9
    I9 -->|"Je sais bien."| I10
    I10 -->|"Est-ce qu’il n’y au…"| I11
    I11 -->|"Ce choix lui appart…"| I12
    I12 -->|"Mais enfin Pascal."| I13
    I13 -->|"Ce temps de vie d’A…"| I14
    I14 -->|"Je dois commencer à…"| I15
```

*15 nœuds, 14 arêtes*

---

### Scénario : Acceptation inconditionnelle

```mermaid
flowchart TD
    I1["(Claude) Claude frappe et entre"]
    I2["(Agathe) Agathe est alitée. Elle parle lentement à vo…"]
    I3["(Agathe) Charlotte, ce matin. Elle a insisté ! Je ne …"]
    I4["(Agathe) Je m’étrangle ! J’ai plus envie de boire."]
    I5["(Agathe) J’en peux plus."]
    I6["(Agathe) Arrêtez ça !"]
    I7["(Agathe) Oui, arrêtez ça."]
    I8["(Agathe) Oui."]
    I9["(Agathe) Oui, on l’a écrit sur un papier."]
    I10["(Agathe) Merci !"]
    I11["(Agathe) C’est ma décision ! Merci de me respecter."]
    I12["(Agathe) N’en parlez pas à mes enfants."]
    I13["(Agathe) Ma fille me forcera à boire."]
    I14["(Agathe) Ça changerait tout."]
    I15["(Agathe) Oui."]
    I16["(Agathe) Des larmes coulent sur les joues d’Agathe. C…"]
    I17["(Agathe) Je veux mourir seule."]
    I18["(Agathe) Non. Laissez-moi reposer en paix."]

    I1 -->|"Vous avez sonné Aga…"| I2
    I2 -->|"On vous a forcé à b…"| I3
    I3 -->|"Vous n’arrivez plus…"| I4
    I4 -->|"Ça devient trop dif…"| I5
    I5 -->|"C’est important de …"| I6
    I6 -->|"Ce n’est plus suppo…"| I7
    I7 -->|"Vous souhaitez qu’o…"| I8
    I8 -->|"Si j’ai bien compri…"| I9
    I9 -->|"Je vais transmettre…"| I10
    I10 -->|"Votre décision me t…"| I11
    I11 -->|"Long silence."| I12
    I12 -->|"Quand ma grand-maman"| I13
    I13 -->|"Et si votre fille a…"| I14
    I14 -->|"Ce qui est important"| I15
    I15 -->|"J’ai l’impression"| I16
    I16 -->|"Ça vous rend triste."| I17
    I17 -->|"Long silence."| I18
```

*18 nœuds, 17 arêtes*

---
