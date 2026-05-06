# Graphes — MedStudents Y2

Structure des scénarios — Généré à partir de MedStudents_Y2_v1.json

---

## Chapitre 1 : Premier jour de stage

### Scénario : 1.1 Accueil dans le service

```mermaid
flowchart TD
    I1["(Dr Moreau) « Bienvenue, Alex ! Je vais vous confier vot…"]
    I2["(Alex) Vous êtes devant la chambre 204. Que faites-…"]
    I3["(Dr Moreau) « C'est honnête de votre part de le dire. Po…"]
    I4["(Monsieur Bernard) « Entrez, entrez… »"]
    I5["(Monsieur Bernard) « Vous auriez pu attendre que je dise 'oui'……"]
    I6["(Monsieur Bernard) « Bon, asseyez-vous. Qu'est-ce que vous voul…"]

    I1 -->|"« Merci Dr Moreau. …"| I2
    I1 -->|"« D'accord, j'y vai…"| I2
    I1 -->|"« Je préférerais qu…"| I3
    I2 -->|"Je frappe deux fois…"| I4
    I2 -->|"J'entre directement…"| I5
    I2 -->|"Je frappe, j'ouvre …"| I4
    I3 -->|"« Merci, je serai p…"| I2
    I4 -->|"« Bonjour Monsieur …"| I6
    I4 -->|"« Bonjour, je suis …"| I6
    I4 -->|"« Salut Monsieur, j…"| I5
    I5 -->|"« Vous avez raison,…"| I6
    I5 -->|"« Je suis pressé·e,…"| I6
    I5 -->|"« Ce n'est pas grav…"| I6
```

*6 nœuds, 13 arêtes*

---

### Scénario : 1.2 Première anamnèse

```mermaid
flowchart TD
    I1["(Alex) Vous êtes assis·e face à Monsieur Bernard. C…"]
    I2["(Monsieur Bernard) « Hier soir, j'ai eu une vraie frousse. Une …"]
    I3["(Monsieur Bernard) Il soupire, croise les bras : « On dirait un…"]
    I4["(Dr Moreau) « Bien. On va sortir et parler deux minutes.…"]

    I1 -->|"« Prenez votre temp…"| I2
    I1 -->|"« Quel est votre mo…"| I3
    I2 -->|"« C'est effrayant c…"| I4
    I2 -->|"« Oui, c'est classi…"| I4
    I2 -->|"« Rassurez-vous, à …"| I4
    I3 -->|"« Pardon, je me sui…"| I2
    I3 -->|"« C'est la procédur…"| I4
```

*4 nœuds, 7 arêtes*

---

## Chapitre 2 : L'examen qui fait peur

### Scénario : 2.1 Avant la ponction lombaire

```mermaid
flowchart TD
    I1["(Madame Costa) « Alex, c'est ça ? On m'a dit que vous allie…"]
    I2["(Madame Costa) « J'ai déjà fait un malaise lors d'une prise…"]
    I3["(Madame Costa) Sa voix tremble : « Attendez, je ne suis pas…"]
    I4["(Alex) Comment présentez-vous concrètement le dérou…"]
    I5["(Dr Moreau) « Madame Costa, Alex m'a alerté·e. On peut t…"]
    I6["(Madame Costa) Elle respire, sourit faiblement : « D'accord…"]

    I1 -->|"« Oui, c'est moi. J…"| I2
    I1 -->|"« Ne vous inquiétez…"| I3
    I1 -->|"« Alors, on va vous…"| I3
    I2 -->|"« Merci de me le di…"| I4
    I2 -->|"« Ça n'arrivera sûr…"| I4
    I2 -->|"« Il faudra essayer…"| I4
    I3 -->|"« Vous avez tout à …"| I2
    I3 -->|"« Il le faut, le mé…"| I4
    I3 -->|"« Je vais chercher …"| I5
    I4 -->|"« Je vous explique …"| I6
    I4 -->|"« L'aiguille fait e…"| I3
    I5 -->|"Vous observez et co…"| I6
    I5 -->|"Vous quittez la piè…"| I6
```

*6 nœuds, 13 arêtes*

---

## Chapitre 3 : Secret médical et famille

### Scénario : 3.1 Une demande dans le couloir

```mermaid
flowchart TD
    I1["(Léa Costa) « Bonjour, je suis la fille de Madame Costa.…"]
    I2["(Dr Moreau) Ton ferme : « Alex, venez avec moi. Il faut …"]
    I3["(Léa Costa) « D'accord… c'est vrai, je connais la règle,…"]
    I4["(Léa Costa) Les larmes aux yeux : « J'ai juste peur pour…"]
    I5["(Dr Moreau) « Le secret médical n'est pas une formalité …"]
    I6["(Madame Costa) « Oui, bien sûr, je veux que Léa soit inform…"]

    I1 -->|"« Bonjour. Je compr…"| I3
    I1 -->|"« Bien sûr, entre n…"| I2
    I1 -->|"« Adressez-vous au …"| I4
    I2 -->|"« Vous avez raison,…"| I5
    I2 -->|"« Elle est infirmiè…"| I5
    I3 -->|"« Oui, avec plaisir…"| I6
    I3 -->|"« Allons-y directem…"| I6
    I4 -->|"« Je suis désolé·e,…"| I3
    I4 -->|"« Ce n'est pas mon …"| I5
```

*6 nœuds, 9 arêtes*

---
