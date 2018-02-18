
# Feuille d'exercices


## 0. Hello world

Démarrer Thonny (ou votre éditeur/IDE préféré)

Écrire et lancer le programme suivant :

```
print("Hello World!")
```

## 1. Variables

1.1. : Écrire, lancer et analyser l'execution du programme suivant :

```
message = "Je connais la réponse à l'univers, la vie et le reste"
reponse = 6 * 7

print(message)
print(reponse)
```

1.2: À l'aide de python, calculer le résultat des opérations suivantes : 

- 567×72
- 33⁴
- 98.2/6
- ((7×9)⁴)/6


## 2. Interactivité

2.1.1 : Demander l'âge de l'utilisateur, puis calculer et afficher l'âge qu'il
aura dans deux ans.

2.1.2 : Même chose, mais en demandant l'année de naissance (approximativement,
sans tenir compte du jour et mois de naissance...)


## 3. Chaînes de caractères

3.1.1 : Demander un mot à l'utilisateur. Afficher la longueur du mot avec
une message tel que "Ce mot fait X caractères !"

3.1.2 : Remplacer les lettres A et E dans le mot, et afficher le mot ainsi
modifié.

3.1.3 : Encadrer le mot modifié avec des `####`.


## 4. Fonctions

4.1.1 : Faire une fonction qui permet de centrer une chaîne de caractère sur 80
caractères

4.1.2 : Ajouter un argument optionnel pour gérer la largeur au lieu du "80"
fixé.

4.1.3 : Encadrer le tout avec des `####`

4.1.4 : Au lieu d'utiliser des `#` pour encadrer le texte, passer le caractère
en argument optionnel.


## 5. Conditions

5.1.1 : Reprendre l'exercice 4.1 et gérer le cas où la largueur demandée est -1
(ne pas centrer, juste encadrer)

5.1.2 : Gérer le cas où le caractère d'encadrement est vide. Dans ce cas, ne pas
encadrer.

5.1.3 : Gérer également le cas où le texte dépasse la largueur demandée. Dans ce
cas, tronquer le texte.

5.1.4 : Gérer également le cas où la longueur demandée est 0 ou négative et
différente de -1. Dans ce cas : sortir directement de la fonction, en affichant
un message d'erreur. Détecter aussi le cas où la chaine de caractère est vide.


## 6. Boucles

6.1.1 : Écrire une fonction qui, pour un nombre donné, affiche la table de
multiplication.

6.1.2 : Cette fois, passer le nombre en argument.

6.1.3 : En utilisant cette fonction, afficher les tables de multiplication pour
tous les nombres entre 1 et 10.

6.1.4 : Protéger l'accès à toute cette connaissance précieuse en demandant en
boucle un "mot de passe" jusqu'à ce que le bon mot de passe soit donné.

6.2 : Écrire une fonction qui permet de déterminer si un nombre est premier

6.3 : Écrire une fonction qui permet de générer les n premiers nombres de la
suite de Fibonnaci

6.4 : Jeu des allumettes

Le jeu des allumettes est un jeu pour deux joueurs, où n allumettes sont
disposées, et chaque joueur peut prendre à tour de rôle 1, 2 ou 3 allumettes. Le
perdant est celui qui se retrouve obligé de prendre la dernière allumette.

- Écrire une fonction capable d'afficher un nombre donné d'allumette, par
  exemple avec le caractère `|`
- Demander à l'utilisateur combien d'allumette il veut prendre, puis afficher le
  nouveau nombre d'allumette, etc...
- Gérer deux joueurs 1 et 2, et gérer la condition de victoire où il reste
  moins d'une allumette.
- Écrire une "intelligence" artificielle capable de joueur au jeu des
  allumettes (en tant que 2eme joueur). 
- Produire un fichier unique contenant l'"intelligence" artificielle : le
  fichier devra au moins contenir une fonction `play(allumettes_restantes)` qui
  renvoie le nombre d'allumettes que l'IA décide de prendre. Partager le
  fichier pour faire combattre les différentes IA dans l'arène !


## 7.Structure de donnée

7.1 : Écrire une fonction qui retourne le plus grand élément d'une liste (ou
d'un set) de nombres, et une autre fonction qui permet retourn le plus petit.

7.2 : Écrire une fonction qui calcule la somme d'une liste de nombres

7.3 : Comme 7.2, mais cette fois en utilisant aucune variable intermédiaire
(utiliser la récursivité)

7.4 : Écrire une fonction qui retourne seulement les entiers pairs d'une liste

7.5 : Écrire une fonction qui permet de trier une liste (ou un set) d'entiers

7.6 : Écrire une fonction qui prends en argument un chemin de fichier comme
"/usr/bin/toto.py" et extrait le nom du fichier, c'est à dire "toto". On pourra
utiliser la méthode `str.split(caractere)` des chaînes de caractère.

7.7 : Écrire un "générateur de formule de compliment / encouragement". Voir : 
http://www.nioutaik.fr/Felicitron/


## 8. Fichiers

8.1 : Écrire une fonction qui remplace un mot par un autre dans un fichier

8.2 : Écrire une fonction qui permet d'afficher un fichier sans les commentaires
et les lignes vides. Spécifier le caractère qui symbolise le début d'un
commentaire en argument de la fonction. (Ou pourra utiliser la méthode `strip()`
des chaînes de caractère pour identifier plus facilement les lignes vides)

8.3 : Écrire une fonction qui trouve et retourne tous les utilisateurs dont le
login est `/bin/bash` dans `/etc/passwd`


## 9. Exceptions, assertions

9.1 Écrire une fonction qui prends un nom de fichier en argument et retourne
le contenu si elle a été capable de le récupérer. Sinon, elle doit déclencher
une exception qui explique en français pourquoi elle n'a pas pu.

9.2 Écrire une fonction qui demande un entier premier à un utilisateur. Si
l'utilisateur ne donne pas une réponse satisfaisante (par exemple, il répond un
mot ou un float), lui redemander jusqu'à ce qu'elle le soit.


## 10. Librairies

Les énoncés des exercices suivants sont un peu plus compliqués et techniques que
les précédents, et ont aussi pour objectifs de vous inciter à explorer la
documentation des librairies pour trouver les outils dont vous avez besoin. Il
existe de nombreuse façon de résoudre chaque exercice.

10.1.1 : Télécharger le fichier `https://app.yunohost.org/community.json` (avec
votre navigateur ou `wget` par exemple). Écrire une fonction qui lit ce fichier,
le charge en tant que données json. Écrire une autre fonction capable de filter
le dictionnaire pour ne garder que les apps d'un level `n` donné en argument.
Écrire une fonction similaire pour le status (`working`, `inprogress`,
`broken`).

10.1.2 : Améliorez le programme précédent pour récupérer la liste directement
depuis le programme avec `requests`. Gérer les différentes exceptions qui
pourraient se produire (afficher un message en français) : syntaxe json
incorrecte, erreur 404, time-out du serveur, erreur SSL

10.1.3 : Écrire le résultat d'un tri (par exemple toutes les applications
cassées) dans un fichier json.

10.2 : Écrire une fonction qui vérifie si un utilisateur système donné a le
droit d'accéder à un fichier. On précisera en argument si il s'agit de droit de
lecture, d'écriture ou d'execution.

10.3.1 : Écrire une fonction qui permet de trouver récursivement dans un dossier
tous les fichiers modifiés il y a moins de 5 minutes.

10.3.2 : À l'aide d'une deuxième fonction permettant d'afficher les `n`
dernières lignes d'un fichier, afficher les 10 dernières lignes des fichiers
récemment modifiés dans `/var/log`

10.4 : Écrire des fonctions qui permettent de tester automatiqmenet les
fonctions écrites en 10.3. Pour cela, la première fonction de test pourra par
exemple créer un dossier temporaire contenant un fichier récemment modifié et un
vieux fichier, puis utiliser `assert` pour vérifier ce que renvoie la fonction.

10.5 : Écrire une fonction qui renvoie les 3 processus les plus gourmands
actuellement en CPU, et les 3 processus les plus gourmands en RAM (avec
leur consommation actuelle, chacun en CPU et en RAM)


