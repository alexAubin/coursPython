## 10. Librairies

Les énoncés des exercices suivants peuvent être un peu plus ouverts que les
précédents, et ont aussi pour objectifs de vous inciter à explorer la
documentation des librairies (ou Internet en général...) pour trouver les
outils dont vous avez besoin. Il existe de nombreuse façon de résoudre chaque
exercice.

#### JSON, requests et argparse

10.1.1 : Télécharger le fichier `https://app.yunohost.org/default/v2/apps.json` (avec
votre navigateur ou `wget` par exemple). Écrire une fonction qui lit ce fichier,
le charge en tant que données json. Écrire une autre fonction capable de filter
le dictionnaire pour ne garder que les apps d'un level supérieur à `n` donné 
en argument. Écrire une fonction similaire pour le status (`working`, 
`inprogress`, `notworking`).

10.1.2 : Améliorer le programme précédent pour récupérer la liste directement
depuis le programme avec `requests`. (Ajoutez une instruction pour s'assurer que
le code du retour est bien 200 avant de continuer).

10.1.3 : Exporter le résultat d'un filtre (par exemple toutes les applications
avec level >= 7) dans un fichier json.

10.1.4 : À l'aide de la librairie `argparse`, paramétrez le tri à l'aide d'un argument donné en ligne de commande. Par exemple: `python3 filtre_apps.py --level 7` exportera dans "result.json" seulement les apps level >= 7.

#### CSV

10.2.1 : Récupérer le fichier de données CSV auprès du formateur, le lire, et 
afficher le nom des personnes ayant moins de 24 ans. Pour ce faire, on 
utilisera la librarie `csv`.

10.2.2 : Trier les personnes du fichier CSV par année de naissance et
enregistrer une nouvelle version de ce fichier avec seulement le nom et l'année
de naissance. Pour trier, on pourra utiliser `sorted` et son argument `key`.

### Random

10.3 : Écrire une fonction `jets_de_des(N)` qui simule N lancés de dés 6 et retourne le nombre d'occurence de chaque face dans un dictionnaire. Par exemple : `{1: 13, 2:16, 3:12, ... }`. Calculer ensuite la frequence (`nb_occurences / nb_lancés_total`) pour chaque face. Testez avec un N grand et en déduire si votre dé virtuel est pipé ou non.

10.4 : Écrire un fonction `create_tmp_dir` qui choisi un nombre au hasard entre
0 et 100000 puis créer le dossier `/tmp/tmp-{lenombre}` et retourne le nom du
dossier ainsi créé. On pourra utiliser la librairie `random` pour choisir un
nom aléatoire, et `os.system` ou `subprocess.check_call` pour créer le dossier.

### Interaction avec le systeme de fichier

10.5.1 : Écrire une fonction qui permet de trouver récursivement dans un dossier
tous les fichiers modifiés il y a moins de 5 minutes.

10.5.2 : À l'aide d'une deuxième fonction permettant d'afficher les `n`
dernières lignes d'un fichier, afficher les 10 dernières lignes des fichiers
récemment modifiés dans `/var/log`

### Interaction avec l'OS

10.6 : Écrire une fonction qui récupère l'utilisation actuelle de la mémoire RAM
via la commande `free`. La fonction retournera une utilisation en pourcent.

10.7 : Écrire une fonction qui renvoie les 3 processus les plus gourmands
actuellement en CPU, et les 3 processus les plus gourmands en RAM (avec
leur consommation actuelle, chacun en CPU et en RAM)


## 11. Outils pour développer

11.1 - Utiliser `pip3` pour trouver quelle est le numéro de version du package `requests` installé

11.2 - Rechercher avec `pip3` si les paquets `flake8` et `autopep8` existent. Installez-les.

11.3 - Utilisez `flake8` sur un code que vous avez écrit récemment (disons d'au moins 30 ou 40 lignes !). Étudiez les erreurs et warnings rapportées par flake, et essayer les corriger manuellement. Si certains warnings vous semblent trop aggressif, utiliser `--ignore` pour spécifier des codes d'erreurs à ignorer.

11.4.1 - Sur un autre code relativement mal formatté, utiliser `autopep8` pour tenter d'ajuster automatiquement le formattage du code. Sauvegarder la sortie fournie par `autopep8` dans un autre fichier "version 2" et comparer le fichier initial avec le fichier de sortie à l'aide de `diff` ou de `git diff --no-index file1 file2`.

11.4.2 - Le nouveau fichier est-il exempt de problèmes d'après flake8 ?

11.5 - Récupérer le fichier `to_debug.py` auprès du formateur. Tenter d'executez ce script et de le faire fonctionner en résolvant les problèmes. En particuliez, ajoutez des breakpoints `pdb` (ou `ipdb`) pour étudiez ce qu'il se passe.
