
## Librairies Python

31 : Reprendre l'exercice sur les jeu de cartes et restructure le code de sorte à avoir:
  - un dossier `jeu_de_cartes/` qui contient `__init__.py` (vide) pour permettre l'import python dans ce dossier
  - `jeu_de_cartes/carte.py` : le fichier qui défini la classe Carte
  - `jeu_de_cartes/paquet.py` : le fchier qui défini la classe Paquet (qui aurait sans doute besoin d'importer la classe `Carte`)
  - `main.py` : le fichier "principal" qui teste l'éxécution du programme sur quelques exemples
  - (Optionnel) Comme présenté dans le cours, créer un fichier `setup.py` avec les métadonnées de votre petite librairie, puis faire `python3 setup.py install` pour tenter de contruire et d'installer votre paquet en "global" sur votre système. Testez ensuite que vous pouvez faire `from jeu_de_cartes.paquet importe Paquet` depuis n'importe où sur le système.

32 : Toujours en continuant avec le code qui permet de manipuler des jeux de carte, introduire dans chaque classe quelques messages de logging (en instanciant des loggers différents dans chaque fichier). Par exemple:
  - Un message de debug lorsqu'une carte est créée
  - Un message d'info lorsqu'un paquet de carte est créé
  - Un message d'info lorsqu'un paquet de carte est mélangé
  - Un message de warning lorsqu'on pioche une carte dans un paquet mais qu'il reste moins de 10 cartes
  - Un message d'erreur lorsqu'on pioche une carte dans un paquet qui ne contient plus de cartes (dans ce cas, on décide que la méthode renverra maintenant `None` plutôt que de crasher)

33 : Écrire une fonction qui permet de trouver récursivement dans un dossier (par exemple `/var/log`) tous les fichiers modifiés il y a moins de 5 minutes. On pourra par exemple utiliser `os.walk(dossier)` et `os.stat(fichier)`, ainsi que `time.time()` pour comparer la date de modification à l'heure qu'il est maintenant.

## Bonnes pratiques (PEP8, Black, annotation de types)

34.1 : Rechercher avec `pip3` si les paquets `flake8` et `autopep8` existent. Installez-les.

34.2 : Utilisez `flake8` sur un code que vous avez écrit récemment (disons d'au moins 30 ou 40 lignes !). Étudiez les erreurs et warnings rapportées par flake, et essayer les corriger manuellement. Si certains warnings vous semblent trop aggressif, utiliser `--ignore` pour spécifier des codes d'erreurs à ignorer.

34.3 : Sur un autre code relativement mal formatté, utiliser `black` pour tenter d'ajuster automatiquement le formattage du code. Sauvegarder la sortie fournie par `black` dans un autre fichier "version 2" et comparer le fichier initial avec le fichier de sortie à l'aide de `diff` ou de `git diff --no-index file1 file2`.

34.4 : Le nouveau fichier est-il exempt de problèmes d'après flake8 ?

35 : Sur votre code, ajouter quelques annotations de types sur vos variables et vos fonctions. Lancez `mypy` sur votre fichier de code pour confirmer que tout est cohérent.

## Debugging avec `pdb`

36 : Récupérer le fichier `to_debug.py` auprès du formateur. Tenter d'executez ce script et de le faire fonctionner en résolvant les problèmes. En particuliez, ajoutez des breakpoints `pdb` (ou `ipdb`) pour étudiez ce qu'il se passe.

## Parallelisation 

37.1 : Récupérer le code d'exemple `parallelisation.py` auprès du formateur. Étudier et lancer le code.

37.2 : Transformer le code pour que la tâche parallélisé soit de vérifier quels sont les entiers premiers entre 2 et 50000. On se contera d'afficher un message si l'entier est premier (et pas de message si il ne l'est pas).

37.3 : Utiliser le module `time` pour mesurer le temps d'execution en fonction du nombre de workers utilisé (1, 2, 4, 8, ...)

37.4 : Modifier le programme pour récupérer les résultats depuis le processus maître.

37.5 : Simplifier le programme à l'aide de `Pool`

