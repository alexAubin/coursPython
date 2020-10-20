# Feuille d'exercices : API REST

## 1. Requétes GET sur l'API Github

1.1 : Afficher la liste des titre des issues Github pour le dépot de code de Linux. L'url correspondante est : https://api.github.com/repos/torvalds/linux/issues . (Avant d'écrire du code, on commencera par regarder la structure de la réponse depuis Firefox)

1.2.1 : Lire la documentation de l'API Github pour trouver comment lister tous les dépots de code d'une "organisation" sur Github. (c.f. la page https://docs.github.com/en/free-pro-team@latest/rest/reference/repos ). Regarder dans Firefox ce que le resultat d'une telle requête donne pour l'organisation nommée "Yunohost-Apps"

1.2.2 : Écrire un code Python capable de récupérer la liste de tous les dépots de l'organisation Yunohost-Apps. N.B. : la liste sera longue, mais Github ne fourni pas tous les résultats d'un coup ... il vous faudra faire plusieurs requêtes pour avoir la liste complète ... c.f. l'argument `page`) 

1.2.3 : Pour chaque dépót listé précédemment, récupérer la valeur de `pushed_at` et parser cette date à l'aide du module `datetime`. Utiliser cette information pour générer la liste des dépóts inactifs (`pushed_at` il y a plus de deux ans)

## 2. Interaction avec une API grâce à une classe

Le formateur expose une API sur `https://dismorphia.info/apiformation/` permettant de gérer une infrastructure informatique tel qu'un parc de serveur. Chaque machine est caractérisée par :
- `name`: le nom de la machine
- `owner`: le nom du propriétaire
- `os`: le nom du système d'exploitation installé
- `ram`: un réel corresondant à la quantité de RAM en Go
- `state`: `up` ou `down` suivant si la machine est allumée ou éteinte
- `since`: une date depuis laquelle la machine a changé d'état

L'API dispose des routes suivantes : 
- `GET /machines`, qui liste toutes les machines existantes
- `GET /machines/<name>`, qui donne les infos sur une machine à partir de son nom
- `POST /machines`, qui permet d'ajouter une nouvelle machine. Pour créer une nouvelle machine, il faudra fournir les quatres données name, owner, os et ram dans la payload HTTP. (Les données state et since seront initalisée par le serveur)
- `DELETE /machines/<name>`, qui permet de supprimer une machine à partir de son nom
- `POST /machines/<name>/<action>`, où l'action peut étre start, restart ou stop et permet d'allumer/éteindre la machine.

On propose la création d'une classe Python nommée `Infra` pour interagir avec cette API gráce à des fonctions

2.1 : Créer une classe `Infra`. Lorsque l'on créé un objet de cette classe, la racine de l'API sera passée en argument : 

```python
infra = Infra("https://dismorphia.info/apiformation")
```

2.2 : En dehors du code, et pour se familiariser avec l'API, tester d'accéder aux différentes routes depuis Firefox, ou bien en utilisant Insomnia ou curl.

2.3 : Implémenter une méthode `.list()` qui permet de lister les machines (c.f. `GET /machines`), et une méthode `.get(nom)` qui permet de récupérer les informations d'une machine en particulier. (On prendra soin de valider que le code de retour est bien celui attendu)

```python
all_machines = infra.list()
google = infra.get("google")
print(all_machines)
print(google)
```

2.4 : Implémenter une méthode `.create(...)` qui créera une nouvelle machine à l'aide d'un nom de machine, de propriétaire, d'OS, et d'une quantité de RAM passée en argument à la fonction

```python
infra.create(name="phoenix", owner="alex", os="linuxmint", ram=3.5)
```

2.5 : De même, implémenter une méthodes `.delete(nom)` et `.start(nom)`, `.restart(nom)` et `.stop(nom)`.

```python
infra.start("google")
assert infra.get("google")["state"] == "up"

infra.stop("google")
assert infra.get("google")["state"] == "down"

infra.delete("google")
```

## 3. Construction d'une API avec Flask

On propose maintenant de construire soi-méme l'API cóté serveur suivant le méme schéma que celle mise à disposition par le formateur sur dismorphia.

3.1 : À l'aide des exemples donnés dans le cours, mettre en place un virtualenv pour travailler avec Flask. On commencera par définir une application minimaliste (hello world...) et lancer le serveur avec :

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

puis essayer d'accéder à `http://127.0.0.1:5000/`.

3.2 : La liste et l'état des machines sera stocké dans une pseudo-base de données sous forme de fichier json qui sera lu et/ou écrit en fonction des requétes parvenant à l'API. On introduit donc des fonctions `read_infra()` et `write_infra(data)` qui permettent de lire/écrire un fichier `infra.json` sur la machine. Pour commencer et valider, on remplira ce fichier avec quelques données de test.

3.3 : Implémenter les deux premières routes `GET /machines` et `GET /machines/<name>` qui permettent de récupérer la liste de toutes les machines, ou juste une machine en fonction de son nom. On prendra soin de valider que la machine recherchée existe bien, et si ce n'est pas le cas de renvoyer une erreur 404. Valider que ces routes fonctionnent en effectuant des requétes "à la main" avec Firefox, curl ou Insomnia, puis avec la classe `Infra` de la partie 2.

3.4 : Implémenter la route `POST /machines`. Les données fournie par la requéte POST seront accessible via `request.data` (`request` étant une entité que l'on peut importer du module `Flask`). On commencera par valider que les données fournie semblent valides (qu'elles contiennent les clefs `name`, `owner` etc... et que les valeurs associées sont raisonnables) puis ajoutera la machine décrite à la liste des machines existantes. Valider que cette méthode fonctionne en effectuant des requétes "à la main" avec Firefox, curl ou Insomnia, puis avec la classe `Infra` de la partie 2.

3.5 : (Si vous avez le courage) Implémentez les autres opérations `POST /machines/<name>/<action>` et `DELETE /machines/<name>`.



