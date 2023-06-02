## Parallelisation

0. Récupérer le code d'exemple `parallelisation.py` auprès du formateur. Étudier et lancer le code.

1. Transformer le code pour que la tâche parallélisé soit de vérifier quels sont les entiers premiers entre 2 et 50000. On se contera d'afficher un message si l'entier est premier (et pas de message si il ne l'est pas).

2. Utiliser le module `time` pour mesurer le temps d'execution en fonction du nombre de workers utilisé (1, 2, 4, 8, ...)

3. Modifier le programme pour récupérer les résultats depuis le processus maître.

4. Simplifier le programme à l'aide de `Pool`

## Utilisation de fonctions C

0. Récupérer l'archive `libalex.zip`, inspecter les différents fichiers et tester l'ensemble.

1. Dans le fichier `.cpp`, définir une nouvelle fonction `is_prime` qui permet de vérifier si un entier est premier. Valider cette fonction `C` (par exemple en definissant un `main` et en testant la fonction sur des valeurs connues)

2. Ajouter l'interface à cette fonction dans le fichier `.py` puis tester cette interface depuis `main.py` sur des valeurs connues.

3. Générer la liste des nombres premiers entre 2 et 50000 et comparer le temps pris en utilisant le binding en C comparé à la même fonction écrite entièrement en Python.
