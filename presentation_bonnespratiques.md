title: Python : bonnes pratiques
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

# Conventions, linter, bonnes pratiques

---

# Conventions, linter, bonnes pratiques

## Faire du "bon code"

.center[
**La lisibilité est la priorité numéro 1**
]

Un programme est vivant et évolue. Mieux vaut un programme cassé mais lisible (donc débuggable) qu'un programme qui marche mais incompréhensible (donc fragile et/ou qu'on ne saura pas faire évoluer)

>“You primarily write your code to communicate with other coders, and, to a lesser extent, to impose your will on the computer.”
>   — Guido van Rossum

 <br/>

>"Maintainable code is more important than clever code"
>   — Guido van Rossum

https://blog.dropbox.com/topics/company/thank-you--guido 


---

# Conventions, linter, bonnes pratiques

## Lisibilité, "bon code"

- **Keep It Simple**
- **Sémantique** : utiliser des noms de variables et de fonctions concis et pertinents
- **Commentaires** : *lorsque c'est nécessaire*, pour démystifier ce qu'il se passe
- **Modularité** : découper son programme en fonctions qui chacune résolvent un sous-problème
- **Couplage faible** : garder ses fonctions autant que possibles indépendantes, limiter les effets de bords
- **Prendre le temps de refactoriser** quand nécessaire
    - si je répète plusieurs fois les mémes opérations, peut-être définir une nouvelle fonction
    - si le contenu d'une variable ou d'une fonction change, peut-être changer son nom
- **Ne pas abuser** des principes précédents
    - trop d'abstractions tue l'abstraction
    - tout ça viens avec le temps et l'expérience
    - à un moment c'est "good enough" et on passe à autre chose

---

# Conventions, linter, bonnes pratiques

## Lisibilité, "bon code"

[How to write good code](https://xkcd.lapin.org/strips/844Code%20correct.png)

---

# Conventions, linter, bonnes pratiques

## Conventions de nommages des variables, fonctions et classes

Variables et fonctions en snake case : `nom_de_ma_variable`

Constantes globales en macro case: `NOM_DE_MA_CONSTANTE`

Nom de classes en upper camel case : `NomDeMaClasse`

---

# Conventions, linter, bonnes pratiques

## Les docstrings

Un commentaire multiligne placé directement après le prototype(?) de la fonction, et qui peut être plus tard lu avec `help(ma_fonction)`

```python
def ma_fonction(arg1, arg2):
    """
    Ici je documente ce que fait ma fonction : 
    ses arguments, son retour, son comportement
    """

    # et ici le vrai code de la fonction
```

---

# Conventions, linter, bonnes pratiques

## Des commentaires utiles ... ou pas

- Un commentaire qui se contente de paraphrase le code est inutile
- La meilleure documentation commence par nommer de manière adéquate ses variables et fonctions

![](img/thisisastopsign.png)

---

# Conventions, linter, bonnes pratiques

## Syntaxe, PEP8, linters

- Le style d'écriture de python est standardisé via la norme PEP8
- Il existe des "linter" pour détecter le non-respect des conventions (et également certaines erreurs logiques)
    - Par exemple `flake8`, `pylint`
- Intégration possible dans `vim` et autres IDE...
- `autopep8` ou `black` permettent de corriger un bon nombre de problème automatiquement

---

# Conventions, linter, bonnes pratiques

## Black

![](img/black.png)

"The Uncompromising Code Formatter"

- Formattage automatique de votre code Python, PEP8-compatible
- L'idée est de laisser Black s'occuper du formattage du code pour **oublier la forme et vous concentrer sur le fond**
- Utilisation avec `pip3 install black` puis `black fichier_ou_dossier`
- À automatiser dans vos chaînes de développement (par ex. pre-commit hook, pull request automatique, ...)

---

# Conventions, linter, bonnes pratiques

## Type hints (Python typé ... sort of)

- Depuis Python 3.5 (puis amélioré dans les versions suivantes)
- ***Annotations** de types: **ignorées au runtime** !
- À voir comme des commentaires formalisés
- Utilisé par des outils d'analyse statique de code pour vérifier la cohérence
- Optionnel (on peut l'utiliser un peu sur quelques endroits du code, pas forcément partout)

```python
# Prends en argument un dictionnaire d'app,
# et renvoie une liste de nom d'app qui ont un level >= M
def at_least_level(apps: Dict[str, Dict], N: int) -> List[str]:

    L: List[str] = []
    for app, infos in apps.items():
        if infos["level"] >= N:
            L.append(L)
    return L
```

---

# Conventions, linter, bonnes pratiques

## Type hints : autres exemples

```python
age: int = 1

# Pas besoin d'initialiser une variable pour annoter son type
x: int  # Ok (no value at runtime until assigned)

# Structures spéciales pour créer des types
from typing import Union, Optional

ma_liste: List[Union[int, str]] = [3, 5, "test", "fun"]

x: Optional[str] = "something" if some_condition() else None
# Mypy understands a value can't be None in an if-statement
if x is not None:
    print(x.upper())
```

Plus d'infos: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

---

# Conventions, linter, bonnes pratiques

## Type hints : `mypy`

- Un outil qui fait une analyse statique du code
- `pip3 install mypy`

---

```python
from typing import List

def plus_grand(liste: List[int]) -> int:

    max_tmp = liste[0]
    for element in liste:
        if element > max_tmp:
            max_tmp = element

    return max_tmp

assert plus_grand([8, 32, 9, 10, -9, 5]) == 32
assert plus_grand([3.14, 1.414, 2.718]) == 16
assert plus_grand("toto") == "t"
```

```text
 > mypy script.py 
script.py:15: error: List item 0 has incompatible type "float"; expected "int"
script.py:15: error: List item 1 has incompatible type "float"; expected "int"
script.py:15: error: List item 2 has incompatible type "float"; expected "int"
script.py:16: error: Argument 1 to "plus_grand" has incompatible type "str"; expected "List[int]"
Found 4 errors in 1 file (checked 1 source file)
```

---



class: impact

# Debugging interactif : `pdb`, `ipdb`

---

# Debugging interactif : `pdb`, `ipdb`

- Python DeBugger
- Permet (entre autre) de définir des "break point" pour rentrer en interactif
   - `import ipdb; ipdb.set_trace()`
   - en 3.7 : `breakpoint()` <small>Mais fait appel à `pdb` et non `ipdb` ?</small>
- Une fois en interactif, on peut inspecter les variables, tester des choses, ...
- On dispose aussi de commandes spéciales pour executer le code pas-à-pas
- Significativement plus efficace que de rajouter des `print()` un peu partout !

---

# Debugging interactif : `pdb`, `ipdb`

### Commandes spéciales

- `l(ist)` : affiche les lignes de code autour de code (ou continue le listing precedent)
- `c(ontinue)` : continuer l'execution normalement (jusqu'au prochain breakpoint)
- `s(tep into)` : investiguer plus en détail la ligne en cours, possiblement en descendant dans les appels de fonction
- `n(ext)` : passer directement à la ligne suivante
- `w(here)` : print the stack trace, c.a.d. les différents sous-appels de fonction dans lesquels on se trouve
- `u(p)` : remonte d'un cran dans les appels de la stacktrace
- `d(own)` : redescend d'un cran dans les appels de la stacktrace

- `pp <variable>` : pretty-print d'une variable (par ex. une liste, un dict, ..)

---

# Debugging interactif : `pdb`, `ipdb`

### Astuces

Indépendamment de `pdb`, on peut utiliser plusieurs choses pour inspecter le contenu d'un objet:
- `un_objet.__dict__`
- `dir(un_objet)`
- `import inspect` (boîte à outil puissante pour étudier les objets)
   - `inspect.getmembers(un_objet)`
   - `inspect.getsourcefile(un_objet)`
   - ... voir https://docs.python.org/3/library/inspect.html
