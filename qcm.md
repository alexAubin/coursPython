
### Prenom : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Nom : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Initiation à Python : questionnaire

*Pour chaque question, entourer la bonne réponse.*

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

Un programme contient seulement les deux lignes suivantes :

``` python
def afficher_allumettes(n=20):
    print("|" * n)
```

Si j'execute ce **programme** :

- A. Il affichera `||||||||||||||||||||` dans la console
- B. Il y aura une erreur disant que `n` n'est pas défini
- C. Il ne fera rien



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

Dans le programme de la question précédente, pour que la fonction `dire_bonjour()` renvoie `"Bonjour !"`,  j'aurais dû remplacer la deuxième ligne par :

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

- A. Un message pour chaque entier pair entre 0 et 9 compris
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

- A. Un message pour chaque entier pair entre 0 et 9 compris
- B. Rien du tout
- C. Il y a une erreur de syntaxe


### 9

Une liste a été créée de cette manière :

```python
ma_liste = [ "Le", "Python", "c'est", "cool" ]
```

Laquelle de ces instructions renvoie `"Python"` ?

- A. `ma_liste[1]`
- B. `ma_liste[2]`
- C. `ma_liste[3]`


### 10

Pour faciliter la compréhension de mon programme par mes collègues et mon futur
moi, j'appelle mes fonctions et mes variables :

- A. Par des noms qui décrivent précisémment ce qu'elles font / contiennent
- B. Avec une seule lettre comme `a`, `b`, `f`, `x` ...
- C. Obiwan Kénobi
- D. La réponse D.
