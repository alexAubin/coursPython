## 9. Fichiers

9.1 : Créer un fonction `liste_users` qui lit le fichier `/etc/passwd` et retourne la liste des utilisateurs ayant comme shell de login `/bin/bash`.

9.2 : Dans le code Python, écrire un modèle d'email comme:

```python
modele = """
Bonjour {prenom} !

Voici en pièce jointe les billets pour votre voyage en train vers {destination}.
"""
```

Ecrire une fonction `generer_email` qui remplace dans `modele` les chaines `{prenom}` et `{destination}` par des arguments fourni à la fonction, et enregistre le résultat dans un fichier `email_{prenom}.txt`. Par exemple, `generer_email("Alex", "Strasbourg")` générera le texte et sauvegardera le résultat dans `email_Alex.txt`.

9.3 : Écrire une fonction qui permet d'afficher un fichier sans les commentaires
et les lignes vides. Spécifier le caractère qui symbolise le début d'un
commentaire en argument de la fonction. (Ou pourra utiliser la méthode `strip()`
des chaînes de caractère pour identifier plus facilement les lignes vides)



## 10. Librairies

Les énoncés des exercices suivants peuvent être un peu plus ouverts que les
précédents, et ont aussi pour objectifs de vous inciter à explorer la
documentation des librairies (ou Internet en général...) pour trouver les
outils dont vous avez besoin. Il existe de nombreuse façon de résoudre chaque
exercice.

10.1.1 : Télécharger le fichier `https://app.yunohost.org/apps.json` (avec
votre navigateur ou `wget` par exemple). Écrire une fonction qui lit ce fichier,
le charge en tant que données json. Écrire une autre fonction capable de filter
le dictionnaire pour ne garder que les apps d'un level `n` donné en argument.
Écrire une fonction similaire pour le status (`working`, `inprogress`,
`notworking`).

10.1.2 : Améliorez le programme précédent pour récupérer la liste directement
depuis le programme avec `requests`. Gérer les différentes exceptions qui
pourraient se produire (afficher un message en français) : syntaxe json
incorrecte, erreur 404, time-out du serveur, erreur SSL

10.1.3 : Écrire le résultat d'un tri (par exemple toutes les applications
cassées) dans un fichier json.

10.2.1 : Récupérer le fichier de données CSV, le lire, et afficher le nom des
personnes ayant moins de 24 ans. Pour ce faire, on utilisera la librarie `csv`.

10.2.2 : Trier les personnes du fichier CSV par année de naissance et
enregistrer une nouvelle version de ce fichier avec seulement le nom et l'année
de naissance. Pour trier, on pourra utiliser `sorted` et son argument `key`.

10.3 : Écrire un fonction `create_tmp_dir` qui choisi un nombre au hasard entre
0 et 100000 puis créer le dossier `/tmp/tmp-{lenombre}` et retourne le nom du
dossier ainsi créé. On pourra utiliser la librairie `random` pour choisir un
nom aléatoire, et `os.system` ou `subprocess.check_call` pour créer le dossier.

10.4 : Écrire une fonction qui vérifie si un utilisateur système donné a le
droit d'accéder à un fichier. On précisera en argument si il s'agit de droit de
lecture, d'écriture ou d'execution.

10.5.1 : Écrire une fonction qui permet de trouver récursivement dans un dossier
tous les fichiers modifiés il y a moins de 5 minutes.

10.5.2 : À l'aide d'une deuxième fonction permettant d'afficher les `n`
dernières lignes d'un fichier, afficher les 10 dernières lignes des fichiers
récemment modifiés dans `/var/log`

10.6 : Écrire des fonctions qui permettent de tester automatiquement les
fonctions écrites en 10.5. Pour cela, la première fonction de test pourra par
exemple créer un dossier temporaire contenant un fichier récemment modifié et un
vieux fichier, puis utiliser `assert` pour vérifier ce que renvoie la fonction.

10.7 : Écrire une fonction qui récupère l'utilisation actuelle de la mémoire RAM
via la commande `free`. La fonction retournera une utilisation en pourcent.

10.8 : Écrire une fonction qui renvoie les 3 processus les plus gourmands
actuellement en CPU, et les 3 processus les plus gourmands en RAM (avec
leur consommation actuelle, chacun en CPU et en RAM)



## 11. Outils pour développer

11.1 - Utiliser `pip3` pour trouver quelle est le numéro de version du package `requests` installé

11.2 - Rechercher avec `pip3` si les paquets `flake8` et `autopep8` existent. Installez-les.

11.3 - Utilisez `flake8` sur un code que vous avez écrit récemment (disons d'au moins 30 ou 40 lignes !). Étudiez les erreurs et warnings rapportées par flake, et essayer les corriger manuellement. Si certains warnings vous semblent trop aggressif, utiliser `--ignore` pour spécifier des codes d'erreurs à ignorer.

11.4.1 - Sur un autre code relativement mal formatté, utiliser `autopep8` pour tenter d'ajuster automatiquement le formattage du code. Sauvegarder la sortie fournie par `autopep8` dans un autre fichier "version 2" et comparer le fichier initial avec le fichier de sortie à l'aide de `diff` ou de `git diff --no-index file1 file2`.

11.4.2 - Le nouveau fichier est-il exempt de problèmes d'après flake8 ?

11.5 - Récupérer le fichier `to_debug.py` auprès du formateur. Tenter d'executez ce script et de le faire fonctionner en résolvant les problèmes. En particuliez, ajoutez des breakpoints `pdb` (ou `ipdb`) pour étudiez ce qu'il se passe.
