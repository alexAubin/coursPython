title: Python : orienté-objet
class: animation-fade
layout: true

<!-- This slide will serve as the base layout for all your slides -->
<!--
.bottom-bar[
  {{title}}
]
-->

---

class: impact

# Interagir avec le XML

---

# Rappel (?) : généralités

- eXtensible Markup Language
- Format très général pour structurer des informations dans un fichier texte
- Défini et géré par le W3C
- (X)HTML est en cas particulier de XML
- ~historique ... à tendance à être remplacé par JSON, YAML, bases SQL / noSQL, ...

```html
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <script src="lib.js"></script>
    </head>
    <body>
        <p class="text-bold">Un morceau de texte</p>
        <p class="text-emph">Un autre paragraphe</p>
    </body>
</html>
```

---

# Rappel (?) : vocabulaire

```html
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
        <script src="lib.js"></script>
    </head>
    <body>
        <p class="text-bold">Un morceau de texte</p>
        <p class="text-emph">Un autre paragraphe</p>
    </body>
</html>
```

- **Balises** : ouvrantes et fermantes, e.g. `<p class="red">` et `</p>`
- **Attributs** : par exemple `class="red"`
- **Noeuds éléments** : caractérisés et délimités par des balises : `head`, `body`, `script`, `p`, ...
   - peut contenir d'autres noeuds (éléments, texte, ...) et donc créer un *arbre*
- **Noeuds texte** : e.g. `"Un morceau de texte"`

---

# XML : Approche DOM v.s. SAX

### DOM : Document Object Model

- Lecture et chargement initial de tout le document (peut être lourd pour les gros documents !)
- Puis accès à tous les noeuds de l'arbre
- Approche classique et répandue (c.f. Javascript)

### SAX : Simple API for XML

- Lecture et analyse "au fur et à mesure"
- Pas besoin de tout charger en mémoire
- Adaptée aux gros documents

---

- rajouter un exemple, e.g. liste d'apps ?

- Lib en python

- Exemple de lecture, accès au noeuds

- Exemple d'ecriture

- Exercice

