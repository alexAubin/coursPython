title: Introduction à Python
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

# {{title}}
*From padawan to jedi master in five days!*

---

class: impact

## Hello, world!

---

## À propos de moi

.col-4[
.center[
![](img/me.jpg)
]
]

.col-8[.center[
<br>
<br>
<br>
`https://github.com/alexAubin`
<br>
<br>
`alex.aubin@mailoo.org`
<br>
<br>
<br>
<br>
]]

.col-4[.center[
Ingénieur/Physicien
</br>
</br>
![](img/particles.jpg)
]]

.col-4[.center[
Dev / hacktiviste?

![](img/yunohost.jpg)
]]

.col-4[.center[
Formateur indépendant

![](img/python_arduino.jpg)
]]

---

## À propos de vous

---

# Enseigner et apprendre la programmation

#### (Mauvaises nouvelles)

- Abstrait
- Booooring exercices
- Disparité de vitesses d'apprentissage
- Rien ne remplace l'expérience..
- Eloigné du taf de "la vraie vie" :
    - Analyse, architecture, UX, debugging, refactoring, tests, VCS, ...

---

# Enseigner et apprendre la programmation

#### (Bonnes nouvelles)

- On a du temps
- Je suis payé pour répondre à vos questions ;)
- Vous montrer l'essentiel et l'utile
- Exercices ludiques ?
- Priorité aux moins rapides
- Devenir architecte du cyberespace

---

# Objectifs

Transmettre :

- Des bases solides et une vue globale
- De l'enthousiasme !
- Des bonnes pratiques ?
- Du "pragmatisme" et du fun ?

---

# Plan

## 1. Notions de "bases" (~ 1.5 jours ?)
## 2. Orienté objet appliqué à un jeu vidéo (~2 jours ?)
## 3. ??? Travailler sur "un vrai projet" 

## Et aussi :
- Une (petite?) évaluation


---

# Logistique ?

- 5 jours
    - 9h15 -> 12h15
    - 13h15 -> 17h15



---








class: impact

# La programmation

---

class: impact

## L'ordinateur comme outil universel

---

class: impact

# « Informatique »

---

# Cooking information

* Préparer **des outils** et **des ingrédients**
* Donner **des instructions**
* ... parfois en utilisant **des "fonctions"**
    * _« monter des oeufs en neige »_
    * _« cuire à thermostat 6 pendant 20 minutes »_

---

# Langage de programmation

## Comme un vrai language

0. **Concepts** (mots, verbes, phrases ...)
1. **Grammaire et syntaxe**
2. **Vocabulaire** 
3. **Organiser** sa rédaction et ses idées : **structurer** correctement son code et ses données

---

# Python

- Versatile
- "Moyen-niveau"
- Syntaxe légère, lisible, facile à prendre en main
- Interprété, "scripting"
- Prototypage rapide
- Grande communauté
- De plus en plus répandu (?)




---

class: impact


*Programming mindset*

---

class: impact

# Machines ain't smart.

# You are !

---

.center[![](img/brainMelting.jpg)]

---

.center[![](img/clouds.jpg)]

---

class: impact

## Programming *is* complicated

## <br>
## Don't be ashamed 
## of not understanding right away

---

.center[![](img/suckingAtSomething.jpg)]

---

# Cassez des trucs !

.center[![](img/yodaMistakes.jpg)]

---

# Explorez !

.center[![](img/changingThings.jpg)]

---








# Setup

- Linux ? Python ?
- Thonny
- Atom

---

# 0. Hello world !

Dans Thonny : 

```python
print("Hello, world!")
```

---

# 1. Les variables

## 1.1. Exemple

```python
message = "Je connais la réponse à l'univers, la vie et le reste"
reponse = 6 * 7

print(message)
print(reponse)
```

---

# 1. Les variables

.center[![](img/sorcery.jpg)]

---

# 1. Les variables

## 1.2. Principe

- Les variables sont des abstractions de la mémoire
- Un contenant pour une information : nom + contenu
- Différence avec le concept mathématique

---

# 1. Les variables

## 1.3. Déclaration, nommage, assignation

- En python : déclaration implicite

```python
x = 42     # déclare et assigne une valeur
x = 3.14   # ré-assigne la variable avec une autre valeur
```

- Restrictions sur le nommage : caractères alphanumérique et `_`.

---

# 1. Les variables

## 1.5. Opérations mathématiques

```python
2 + 3   # Addition      
2 - 3   # Soustraction  
2 * 3   # Multiplication
2 / 3   # Division      
2 % 3   # Moduloe       
2 ** 3  # Exponentiation
```

---

# 1. Les variables

## 1.4. Types

```python
reponse = 42      # Entier / integer    / int
pi = 3.1415       # Réel                / float
prenom = "Alex"   # Chaîne de caractère / string
oui = True        # Booléen             / bool
```

Connaître le type d'une variable : `type(variable)`

---

# 1. Les variables

## 1.5. Conversion de type

```python
int("3")      -> 3
str(3)        -> "3"
float(3)      -> 3.0
int(3.14)     -> 3
str(3.14)     -> "3.14"
float("3.14") -> 3.14
int(True)     -> 1
int("trois")  -> Erreur
```

---

# 2. Interactivité basique

En terminal, il est possible de demander une information à l'utilisateur
avec `input("message")`

```python
reponse = input("Combien font 6 fois 7 ?")
```

N.B. : ce que renvoie `input()` est une chaîne de caractère !

---

# 3. Chaînes de caractères

### Concatenation

```python
"Cette phrase" + " est en deux morceaux"
```

### Multiplication

```python
"a" * 6    -> "aaaaaa"
```

### Longueur

```python
len("Hello world") -> 11
```

---

# 3. Chaînes de caractères

### Extraction

.center[![](img/string.png)]

```python
m = "Hello world"
m[:5]  -> 'Hello'
m[6:8] -> 'wor'
m[-3:] -> 'rld'
```

### Substitution

```python
"Hello world".replace("Hello", "Goodbye")
```

---

# 4. Fonctions

## 4.1 Principe

Donner un nom à un ensemble d'instructions (modularité, sémantique)

.col-6[
```python
def ma_fonction(arg1, arg2):
    instruction1
    instruction2
    ...
    return resultat
```
]

.col-6[
.center[
    ![test](fonction.png)
]
]

On peut ensuite utiliser la fonction et récupérer le resultat : 

```python
mon_resultat = ma_fonction("truc", "bidule")
```

---

# 4. Fonctions

.col-6[
```python
def ma_fonction(arg1, arg2):
    instruction1
    instruction2
    ...
    return resultat
```
]

.col-6[
.center[
    ![test](fonction.png)
]
]

## 4.2 Elements de syntaxe

- `def`, `:`
- indentation !!
- Des arguments
- `return`


---

# 4. Fonctions

## 4.3 Exemple

```python
def distance(dx, dy):
    dx_carre = dx ** 2
    dy_carre = dy ** 2
    return math.sqrt(dx_carre + dy_carre)
```

Utilisation :

```python
D = distance(3, 5)       # -> D vaut 34
```

---

# 4. Fonctions

## 4.4 Variables locales

```python
def distance(dx, dy):
    dx_carre = dx ** 2
    dy_carre = dy ** 2
    return math.sqrt(dx_carre + dy_carre)
```

- Les variables créées dans la fonction sont **locales**
- Les noms dx, dy sont égalements "locaux" : ils font reference aux arguments de cette fonction, meme si d'autres variables nommées dx ou dy existent ailleurs dans le code !

---

# 4. Fonctions

## 4.5 'Return'

- `return` quitte immédiatement la fonction !
- Il peut néanmoins y avoir plusieurs `return` dans une fonction (mais seul un sera executé)
- Une fonction sans `return` renvoie implicitement `None`. 

---

# 4. Fonctions

## 4.6 Arguments optionnels

Les arguments peuvent être rendu optionnels si ils ont une valeur par défaut :

```python
def distance(dx, dy=0, dz=0):
    [...]
```

Dans ce cas, tous ces appels sont valides : 

```python
distance(1)
distance(1, 2)
distance(1, 2, 3)
distance(1, dy=2)
distance(1, dz=3)
distance(1, dy=2, dz=3)
distance(1, dz=3, dy=2)
```

---

# 4. Fonctions

## 4.7 Différence avec le concept mathématique

- Domaine généralement mal défini (e.g. type d'entrée et de sortie)
- Effets de bords (e.g. `print()`)


---

# 5. Conditions

Gérer des cas pour adapter le fonctionnement du programme

### 5.1 Syntaxe générale 

```python
if condition:
    instruction1
    instruction2
elif (autre condition):
    instruction3
elif (encore autre condition):
    instruction4
else:
    instruction5
    instruction6
```

Attention à l'indentation !

---

# 5. Conditions

Tout n'est pas nécessaire, par exemple on peut simplement mettre un `if` :

```python
if condition:
    instruction1
    instruction2
```

---

# 5. Conditions

## 5.2 Exemple

```python
def dire_bonjour(nom):
    if nom == "Jack Sparrow":
        return "Bonjour, *Capitaine* " + nom
    else:
        return "Bonjour, " + nom
```

.center[![](img/captain.jpg)]

---

# 5. Conditions

Les conditions comme `nom == "Jack Sparrow"` sont en fait transformées en booléen lorsque la ligne est interprétée.

On aurait pu écrire :

```python
is_jack_sparrow = (nom == "Jack Sparrow")

if is_jack_sparrow:
    [...]
else:
    [...]
```

---

# 5. Conditions

## 5.4 Ecrire des conditions

```python
angle == pi      # Égalité
angle != pi      # Différence
angle > pi       # Supérieur
angle >= pi      # Supérieur ou égal
angle < pi       # Inférieur
angle <= pi      # Inférieur ou égal
```

## Combiner des conditions

```python
not (nom == "Jack Sparrow")                # Négation
(nom == "Sparrow") and (prenom == "Jack")  # ET
(nom == "Sparrow") or (prenom == "Jack")   # OU inclusif
```

---

# 5. Conditions

## Condition "avancées" (chaînes de caractères)

```python
"Jack" in nom           # 'nom' contient 'Jack'
nom.startswith("Jack")  # 'nom' commence par 'Jack'
nom.endswith("row")     # 'nom' fini par 'row'
```

---

# 6. Boucles

Répéter plusieurs fois un même ensemble d'instruction

- pour plusieurs valeurs (`for`)
- tant qu'une condition est remplie (`while`)

---

# 6. Boucles

## 6.1 Les boucles `for`

```python
for i in range(0,10):
    print("En ce moment, i vaut " + str(i))
```

donne :
```python
En ce moment, i vaut 0
En ce moment, i vaut 1
En ce moment, i vaut 2
...
En ce moment, i vaut 9
```

---

# 6. Boucles

## 6.2 `continue` et `break`

`continue` permet de passer immédiatement à l'itération suivante

`break` permet de sortir immédiatement de la boucle

---

# 6. Boucles

## 6.2 `continue` et `break`

```python
for i in range(0,10):
    if i % 2 == 0:
        continue

    print("En ce moment, i vaut " + str(i))
```

-> Affiche le message seulement pour les nombres impairs

---

# 6. Boucles

## 6.2 `continue` et `break`

```python
for i in range(0,10):
    if i == 7:
        break

    print("En ce moment, i vaut " + str(i))
```

-> Affiche le message pour 0 à 6

---

# 6. Boucles

## 6.3 Boucle `while`

(un peu moins utilisé que `for`)

```python
x = 40
while x % 2 == 0:
    print(str(x) + " est pair !")
    x = x/2

print(str(x) + " est impair !")
```

---

# 7. Listes, dictionnaires

Les listes et dictionnaires permettent de stocker des séries
d'information...

## 7.1 Les listes

```python
favourite_pokemons = [ "Bulbizarre", "Roucoups", "Insecateur" ]
fibonnaci = [ 1, 1, 2, 3, 5, 8 ]
stuff = [ 3.14, 42, "bidule", ["a", "b", "c"] ]
```

### Accès à un élément particulier

```python
favourite_pokemons[1]    ->  "Roucoups"
```

### Longueur

```python
len(favourite_pokemons)    -> 3
```

---

# 7. Structure de données

```python
favourite_pokemons = [ "Bulbizarre", "Roucoups", "Insecateur" ]
```

### Iteration

```python
for pokemon in favourite_pokemons:
    print(pokemon + " est un de mes pokemons préférés !")
```

### Iteration avec index

```python
for i, pokemon in enumerate(favourite_pokemons):
    print(pokemon + " est mon "+ str(i) +"ème pokemon préféré !")
```

---

# 7. Structure de données

```python
favourite_pokemons = [ "Bulbizarre", "Roucoups", "Insecateur" ]
```

### Modification d'un élément

```python
favourite_pokemons[1] = "Roucarnage"
```

### Ajout à la suite

```python
favourite_pokemons.append("Mewtwo")
```

### Insertion

```python
favourite_pokemons.insert(1, "Papillusion")
```

---

# 7. Structure de données

### Transformation de string en liste

```python
"Hello World".split()    -> ["Hello", "World"]
```

### Transformation de liste en string

```python
' | '.join(["a", "b", "c"])      -> "a | b | c"
```

---

# 7. Structure de données

## 7.2 Les dictionnaires

```python
ages = { "Alice": 20, "Bob": 24, "Charlie": 19 }
```

N.B. : dans les dictionnaires, l'ordre des éléments est sans importance !

### Accès à une valeur

```python
ages["Charlie"]    ->   19
```

### Modification d'une entrée, ajout d'une nouvelle entrée

```python
ages["Charlie"] += 1
ages["Deborah"] = 21
```

---

```python
ages = { "Alice": 20, "Bob": 24, "Charlie": 19 }
```

### Iteration sur les clefs

```python
for prenom in ages:
    print("Je connais l'age de "+prenom)
```

### Iteration sur les valeurs

```python
for age in ages.values():
    print("Quelqu'un a "+str(age)+" ans")
```

### Iterations sur les clefs et valeurs

```python
for prenom, age in ages.items():
    print(prenom + " a " + str(age) + " ans !")
```

---

# 7. Structure de données

## 7.3 Les sets

Les `set`s stockent des éléments de manière unique et désordonnée.  

```python
chat = set("chat")     # -> {'h', 'c', 'a', 't'}
chien = set("chien")   # -> {'c', 'e', 'i', 'n', 'h'}
chat - chien           # -> {'a', 't'}
chien - chat           # -> {'i', 'n', 'e'}
chat & chien           # -> {'h', 'c'}
chat | chien           # -> {'c', 't', 'e', 'a', 'i', 'n', 'h'}
chat.add("z")          # ajoute `z` à `chat`
```

---

# 7. Structure de données

## 7.4 Les tuples

Les tuples permettent de stocker des données de manière similaire à une liste, mais de manière non-mutable. Typiquement : des coordonnées de point.

```python
P = (2,3)
P[0]        # -> 2
P[1]        # -> 3
P[0] = 5    # -> Erreur!
```

---

# 7. Structure de données

## 7.5 List/dict comprehensions

Les "list/dict comprehensions" sont des syntaxes particulière permettant de rapidement construire des listes (ou dictionnaires) à partir d'autres structures.

### Syntaxe (list comprehension)

```python
[ new_e for e in liste if condition(e) ]
```

### Exemple (list comprehension)

Carré des entiers impairs d'une liste

```python
[ e**2 for e liste if e % 2 == 1 ]
```

---

# 7. Structure de données

## 7.5 List/dict comprehensions

Les "list/dict comprehensions" sont des syntaxes particulière permettant de rapidement construire des listes (ou dictionnaires) à partir d'autres structures.

### Syntaxe (dict comprehension)

```python
{ new_k:new_v for k, v in d.items() if condition(k, v) }
```

### Exemple (dict comprehension)

Carré des entiers impairs d'une liste

```python
{ nom: age-20 for nom, age in ages.items() if age >= 20 }
```

---

# 8. Fichiers

## 8.1 Lire

```python
with open("/etc/passwd", "r") as f:
    toutes_les_lignes = f.readlines()

for ligne in toutes_les_lignes:
    print(ligne)
```

### Explications

- `open("fichier", "r")` ouvre un fichier en lecture
- `with ... as ...` ouvre un contexte, à la fin duquel le fichier sera fermé
- `f.readlines()` permet d'obtenir une liste de toutes les lignes du fichier

---

# 8. Fichiers

## 8.2 Ecrire

### En remplacant tout !

```python
with open("/home/alex/test", "w") as f:
    f.write("Plop")
```

### À la suite (« append »)

```python
with open("/home/alex/test", "a") as f:
    f.write("Plop")
```

---

# 9. Exceptions, assertions

Les exceptions correspondent à des erreurs ou des cas particuliers qui empêchent
(a priori) la suite du déroulement du programme ou d'une fonction.

### Exemple

```python
>>> int("test")
[...]
ValueError: invalid literal for int() with base 10: 'test'
```

---

# 9. Exceptions, assertions

## 9.1 `try`/`except`

En Python, il est courant d'« essayer » des opérations puis de gérer les
exceptions. 

On utilise pour cela des `try: ... except: ...`. On peut déclencher nos propres
exceptions avec `raise Exception("message")`

### Exemple

```python
try:
    str = input("Entrez un entier svp !")
    n = int(str)
except:
    raise Exception("Ce n'est pas un entier !")
```

---

# 9. Exceptions, assertions

### Utilisation différente

```python
try:
    str = input("Entrez un entier svp !")
    n = int(str)
except:
    n = -1
```

---

# 9. Exceptions, assertions

### Autre exemple

```python
try:
    with open("/some/file", "r") as f:
        lines = f.readlines()
except:
    raise Exception("Impossible d'ouvrir le fichier en lecture !")
```

---

# 9. Exceptions, assertions

### Autre exemple

```python
try:
    with open("/etc/shadow", "r") as f:
        lines = f.readlines()
except PermissionError:
    raise Exception("Pas le droit d'ouvrir le fichier !")
except FileNotFoundError:
    raise Exception("Ce fichier n'existe pas !")
```

---

# 9. Exceptions, assertions

<br>
<br>
<br>
<br>
<br>

.center[
## The "python way"
### « Better to ask forgiveness than permissions »
]

---


# 9. Exceptions, assertions

### 9.2 Assertions

Il est possible d'utiliser des `assert`ions pour expliciter certaines hypothèses
qui sont faites à certains endroit du code. Si l'hypothèse n'est pas validée,
une exception est déclenchée.

```python
def somme(liste):
    assert isinstance(liste, list), "Cette fonction ne marche que pour des list"
    assert len(liste) >= 1, "Cette liste est vide !"
    for e in liste:
        assert isinstance(liste, int), "Cette liste n'est pas une liste d'entier"
```

---

# 10. Librairies

L'une des puissances de python vient de l'écosystème de librairie disponibles.

Librairie / bibliothèque / module : un ensemble de fonctionnalité déjà pensés et
éprouvées, prêtes à l'emploi. Par exemple : `datetime`

### Syntaxes d'import

```python
import some_module            # -> Importer tout un module
some_module.some_function()   # -> Appeler la fonction some_function()
                              # du module

import some_module as m       # -> Import mais en renommant le module
m.some_function()


from some_module import some_function   # -> Import seulement d'une 
some_function()                         # fonction
```

---

# 10. Librairies

## 10.1 Exemple : `json`

```python
{
    "mailman": {
        "branch": "master",
        "level": 2,
        "state": "working",
        "url": "https://github.com/yunohost-apps/mailman_ynh",
        "flags": [ "mailing-list", "lightweight" ]
    },
    "mastodon": {
        "branch": "master",
        "level": 3,
        "state": "inprogress",
        "url": "https://github.com/YunoHost-Apps/mastodon_ynh",
        "flags": [ "social network", "good-UX" ]
    }
}
```
---

# 10. Librairies

## 10.1 Exemple : `json`

```python
import json
with open("some.json") as f:
    j = json.loads(f.readlines())

j["mailman"]["state"]     # -> "working"
```

---

# 10. Librairies

## 10.4 Exemple : `requests`

---

# 10. Librairies

## 10.2 Exemple : `os`

`os` permet d'interagir avec le système d'exploitation pour réaliser différent
type d'action... Certaines étant spécifiques à l'OS en question (Linux, Windows,
...)

Quelques exemples :

```python
import os
os.listdir("/etc/")  # Liste les fichiers dans /etc/
os.path.join("/etc", "passwd") # Génère un chemin à partir de plusieurs parties
os.system("ls /etc/") # (à éviter) Execute une commande "brute"
```

Voir aussi : copie ou suppression de fichiers, modification des permissions, ...

---

# 10. Librairies

## 10.3 Exemple : `subprocess`

`subprocess` peut typiquement être utiliser pour lancer des commandes et
récupérer leur résultat

```python
out = subprocess.check_output(["echo", "Hello World!"])
print(out)    # -> Affiche 'Hello World'
```

---

# 10. Librairies

## 10.3 Exemple : `subprocess`

`subprocess` peut typiquement être utiliser pour lancer des commandes et
récupérer leur résultat

```python
out = subprocess.check_output(["echo", "Hello World!"])
print(out)    # -> Affiche 'Hello World'
```


---

# 10. Librairies

.center[![](img/moar.jpg)]


---

# 10. Librairies

### Moar ?

- Debian packages : `python-*`

</br>

- Python package manager : `pip`
    - `pip search polib`
    - `pip install polib`

---

# 11. Les classes

---

# 12. Pygame

---








---

xkcd pixels

Methode de programmation

Chercher de la doc

Concept : edge-case

How to write good code

Code for human and for the future,
not juste code for machines right now.

Code semantique

Debugger du code (rubbger duck programming)
    -> gdb

Factorisation

Paradigme de programmation

Test-driven dev ?

virtualenv

Git / vcs




