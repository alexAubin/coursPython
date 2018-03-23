
### Prenom : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Nom : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Initiation à Python : questionnaire

### 1

Un programme contient cette instruction :

```python
age = input("Quel est ton âge ?")
```

Pendant une execution du programme, un utilisateur répond 28 à la question.
Que contient la variable `age` ?

- A. `28`
- B. `"28"`
- C. `None`



### 2

Pour concaténer un entier `n` à une chaîne de caractère, j'écris :

- A. `"une chaîne" + str(n)`
- B. `"une chaîne" + int(n)`
- C. `"une chaîne" + "n"`



### 3

Pour vérifier qu'une variable `n` est entier, j'utilise :

- A. `isinstance(n, int)` 
- B. `type(n) == "int"` 
- C. `int(n) == True` 


### 4

À la fin de l'execution de ce programme, que contiendra la variable `x` ?

```python
def dire_bonjour():
    print("Bonjour !")

x = dire_bonjour()
```

- A. `"Bonjour !"`
- B. `""`
- C. `None`



### 5

Dans le programme de la question précédente, pour que la fonction
`dire_bonjour()` renvoie `"Bonjour !"`,  j'aurais dû remplacer la deuxième ligne
par :

- A. `return "Bonjour !"`
- B. `return print("Bonjour !")`
- C. Rien du tout, c'était déjà bon !


### 6

Pour savoir si une variable `n` contient l'entier 20, j'écris :

- A. `n = 20`
- B. `n = "20"`
- C. `n == 20`
- D. `n == "20"`


### 7

Qu'affiche le programme suivant ?

```python
for i in range(0,10):
    if i % 2 == 0:
        continue
    print("La variable i vaut " + str(i))
```

- A. Un message pour chaque entier impair entre 0 et 9 compris
- B. Rien du tout
- C. Il y a une erreur de syntaxe


### 8

Qu'affiche le programme suivant ?

```python
for i in range(0,10):
    if i % 2 == 0:
    continue
    print("La variable i vaut " + str(i))
```

- A. Un message pour chaque entier impair entre 0 et 9 compris
- B. Rien du tout
- C. Il y a une erreur de syntaxe


### 9

Une liste a été créée de cette manière :

```python
ma_liste = [ "Le", "Python", "c'est", "cool", "!" ]
```

Laquelle de ces instructions renvoie `"Python"` ?

- A. `ma_liste[1]`
- B. `ma_liste[2]`
- C. `ma_liste[3]`

### 10

Pour découper une chaine de caractère `s` par rapport aux `;` qu'elle contient
et obtenir ainsi une liste, j'utilise : 

- A. `s.strip(';')`
- B. `s.join(';')`
- C. `s.split(';')`


### 11

Pour importer la librairie permettant de manipuler du json, j'écris au début de
mon programme :

- A. `include json`
- B. `import json`
- C. `require json`

### 12

Ecrire une fonction `pairs` qui prends en argument une liste d'entier et renvoie
la liste entiers pairs qu'elle contient. Par exemple, `pairs([3, 6, 9, 5, 2])`
renverra `[6, 2]`.

```python
|
|
|
|
|
|
|
```

### 13

Ecrire un petit programme qui ouvre le fichier `/etc/resolv.conf` et stocke son
contenu dans une variable `content`. (Sans oublier de fermer le programme,
explicitement ou implicitement)

```python
|
|
|
|
```

### 14

Compléter ce programme pour afficher dans la console le type de Pikachu à partir
du contenu de `d` :

```python
d = { "pikachu":   { "type": "Foudre", "level": 15 }, 
      "salameche": { "type": "Feu",    "level": 23 }
    }

|
|
|
```

### 15

Écrire la première ligne (`for ...`) qui permet d'itérer à la fois sur les clefs
et les valeurs d'un dictionnaire `d`.

```python
|
|
|
```

### 16

Ecrire un programme qui, étant donné une chaîne de caractère `stuff`, essaye de
la convertir en `float`, et stocke le résultat dans une variable `f`. Si la
conversion n'est pas possible / pas réussie, stocker `-1.0` dans `f` à la place.

```python
|
|
|
|
|
|
```


### 17

Ajouter, avant les deux lignes déjà écrites, quelques lignes permettant de
définir une classe `Voiture`, et que `v.color` renvoie `"bleu"`

```python
|
|
|
|
|
|
|

v = Voiture()
print(v.color)
```

### 18

En python, ce que l'on note généralement `self` représente :

- A. Le constructeur de la classe
- B. La classe en train d'être modifiée / étudiée
- C. L'objet en train d'être modifié / étudié

### 19

Pour expliciter et tester une hypothèse faite par un programme (par exemple,
avoir une liste d'au moins 3 elements), j'utilise :

- A. `if`
- B. `except`
- C. `assert`

### 20

Pour faciliter la compréhension de mon programme par mes collègues et mon futur
moi, j'appelle mes fonctions et mes variables :

- A. Par des noms qui décrivent précisémment ce qu'elles font / contiennent
- B. Avec une seule lettre comme `a`, `b`, `f`, `x` ...
- C. Obiwan Kénobi
- D. La réponse D.
