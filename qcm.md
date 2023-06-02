
### Prenom : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Nom : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Initiation à Python : questionnaire

### 1 (1 point)

Un programme contient cette instruction :

```python
age = input("Quel est ton âge ?")
```

Pendant une execution du programme, un utilisateur répond 28 à la question.
Que contient la variable `age` ?

- A. `28`
- B. `"28"`
- C. `None`


### 2 (1 point)

Pour __afficher__ "Le python c'est cool !" dans la console, j'écris :

- A. `print("Le python, c'est cool !")`
- B. `return("Le python, c'est cool !")`
- C. `"Le python, c'est cool"`
- D. `Le python, c'est cool`

### 3 (1 point)

Pour concaténer un entier `n` à une chaîne de caractère, j'écris :

- A. `"une chaîne" + n`
- B. `"une chaîne" + str(n)`
- C. `"une chaîne" + int(n)`
- D. `"une chaîne" + "n"`

### 4 (2 points)

À la fin de l'execution de ce programme, que contiendra la variable `x` ?

```python
def dire_bonjour():
    print("Bonjour !")

x = dire_bonjour()
```

- A. `"Bonjour !"`
- B. `""`
- C. `None`


### 5 (2 points)

Dans le programme de la question précédente, pour que la fonction
`dire_bonjour()` renvoie `"Bonjour !"`,  j'aurais dû remplacer la deuxième ligne
par :

- A. `return "Bonjour !"`
- B. `return print("Bonjour !")`
- C. Rien du tout, c'était déjà bon !

### 6 (1 point)

Pour tester si une variable `n` contient l'entier 20, j'écris :

- A. `n = 20`
- B. `n = "20"`
- C. `n == 20`
- D. `n == "20"`

### 7 (1 point)

Pour vérifier qu'une variable `n` est entier, j'utilise :

- A. `isinstance(n, int)` 
- B. `type(n) == "int"` 
- C. `int(n) == True` 


### 8 (2 points)

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


### 9 (2 points)

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

### 10 (2 points)

Écrire le code d'une fonction `moyenne` qui prends comme arguments 3 nombres notés `a`, `b` et `c`, et renvoie leur moyenne.

```python
|
|
|
|
|
```

### 11 (1 point)

Une liste a été créée de cette manière :

```python
ma_liste = [ "Le", "Python", "c'est", "cool", "!" ]
```

Laquelle de ces instructions renvoie `"Python"` ?

- A. `ma_liste[1]`
- B. `ma_liste[2]`
- C. `ma_liste[3]`

### 12 (1 point)

Pour itérer sur les éléments d'une liste `L`, j'utilise préférientiellement une syntaxe du type :

- A. `for element in L:`
- B. `for i in range(0, len(L)):`
- C. `for L[i] in L:`

### 13 (1 point)

Après avoir écris le programme suivant : 

```python
def est_pair(n):
    return n%2==0
```

pour tester le bon fonctionnement de la fonction `est_pair` : 

- A. Je lance directement ce programme. Il m'affichera `True` ou `False` si ça marche ;
- B. J'ajoute un unique appel à la fonction à la fin du programme : `est_pair()` ;
- C. Je teste avec plusieurs valeurs, par exemple `est_pair(5)` et `est_pair(10)`, pour vérifier que la fonction réponds entièrement au cahier des charges ;
- D. Je demande à mon boss si c'était bien ce qu'il fallait écrire.

### 14 (1 point)

En testant un programme, une erreur se produit. Pour comprendre et corriger le problème de manière efficace : 

- A. J'efface des lignes qui semblent poser problème jusqu'à ce qu'il n'y ai plus d'erreurs ;
- B. J'apelle mon boss pour qu'il m'aide ;
- C. Je relis attentivement le message d'erreur et la ligne correspondante pour identifier la véritable cause du problème.


### 15 (1 point)

Pour faciliter la compréhension de mon programme par mes collègues et mon futur
moi, j'appelle mes fonctions et mes variables :

- A. Par des noms qui décrivent précisémment ce qu'elles font / contiennent ;
- B. Avec une seule lettre comme `a`, `b`, `f`, `x` ...
- C. Obiwan Kénobi
- D. La réponse D.
