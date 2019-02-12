## 11. Outils et bonnes pratiques

11.1 - Utiliser `pip3` pour trouver quelle est le numéro de version du package `requests` installé

11.2 - Rechercher avec `pip3` si les paquets `flake8` et `autopep8` existent. Installez-les.

11.3 - Utilisez `flake8` sur un code que vous avez écrit récemment (disons d'au moins 30 ou 40 lignes !). Étudiez les erreurs et warnings rapportées par flake, et essayer les corriger manuellement. Si certains warnings vous semblent trop aggressif, utiliser `--ignore` pour spécifier des codes d'erreurs à ignorer.

11.4.1 - Sur un autre code relativement mal formatté, utiliser `autopep8` pour tenter d'ajuster automatiquement le formattage du code. Sauvegarder la sortie fournie par `autopep8` dans un autre fichier "version 2" et comparer le fichier initial avec le fichier de sortie à l'aide de `diff` ou de `git diff --no-index file1 file2`.

11.4.2 - Le nouveau fichier est-il exempt de problèmes d'après flake8 ?

11.5 - Récupérer le fichier `to_debug.py` auprès du formateur. Tenter d'executez ce script et de le faire fonctionner en résolvant les problèmes. En particuliez, ajoutez des breakpoints `pdb` (ou `ipdb`) pour étudiez ce qu'il se passe.
