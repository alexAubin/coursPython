# Exercices de manipulation de données XML

## 1. Utilisation de ElementTree

1.1 - En utilisant la module ElementTree de Python, charger le fichier `country.xml` fourni par le formateur. Boucler sur les différents éléments `country` et afficher pour chaque élément la valeur du `gdppc` et le nom des voisins.

1.2 - Ajouter un element `country` pour la France et l'Espagne en suivant la même structure.

1.3 - Sauvegarder la version modifier en `country_extended.xml`

## 2. Lecture itérative

2.1 - Installer `lxml` grâce à `pip3`, et récupérer le "gros" fichier XML, `copyright.xml`. Attention à ne pas tenter d'ouvrir "brutalement" ce fichier avec un éditeur ou avec la méthode utilisée en 1 : cela consommera beaucoup trop de RAM !

2.2 - En utilisant des commandes comme `head -n 50 copyright.xml`, analyser visuellement la structure du fichier d'après ses premières lignes.

2.3 - Initialiser un itérateur destiné à itérer sur ce fichier, et en particulier sur les tags `Title`. Créer une boucle à partir de cet itérateur et afficher tous les titres qui contiennent la chaîne `"Pyth"`. **On prendra soin de nettoyer les éléments trouver avant de passer à chaque nouvelle itération sous peine de remplir la RAM très vite !**

2.4 - Pour chaque titre trouvé, remonter au parent 'Record' pour trouver le 'Holder Name' correspondant à ce titre. S'aider de `ipython` et/ou `ipdb` pour tester et expérimenter en interactif.

# 3. Scrapping avec BeautifulSoup

3.1 - Récupérer (manuellement à l'aide de Firefox ou `wget`) le code HTML de la page wikipédia "List of Doctor Who episodes (2005-present)". Par exemple, on pourra appeler ce fichier `doctorwho_list.html`. Charger ce fichier à l'aide de BeautifulSoup

3.2 - Récupérer les éléments correspondant à chaque épisode (indice : ce sont les tags `tr` avec comme classe `vevent`)

3.3 - Pour chaque épisode, récupérer le titre, le story code, et l'auteur (written by). Mettre ces informations dans un dictionnaire par épisode, puis construire une liste avec tous ces épisodes.S'aider de `ipython` et/ou `ipdb` pour tester et expérimenter en interactif.
