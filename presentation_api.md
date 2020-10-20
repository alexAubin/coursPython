title: Les API REST avec Python
class: animation-fade
layout: true

<!-- This slide will serve as the base layout for all your slides -->
<!--
.bottom-bar[
  {{title}}
]
-->

---

class: impact

# Les API REST avec Python

---

# Contexte

- Construire des sites web, applications mobiles, systèmes embarqués, ...
- Automatiser des traitements (bots, analyse, ...)

---

# API

- Application Programming Interface
    - Interface de programmation applicative
- Normalisation des interactions entre un client et un serveur
- Séparation de la logique et des préoccupations entre le client et le serveur

---

# REST API

- Un style d'architecture d'API
- Défini par 5 principes généraux (+ 1 optionnel)
- Défini par un thesard dans les années 2000 (en parallèle de HTTP 1.1)
- À cette époque, le type "classique" d'API était SOAP

>At that point, most developers had to deal with SOAP (Simple Object Access Protocol) to integrate APIs. And the “simple” part of that acronym is not to be taken literally.

(c.f. https://blog.readme.com/the-history-of-rest-apis/ )

- Objectifs de REST : 
    - simplicité
    - performance
    - scalabilité / passage à l'échelle
    - portabilité

---

# Disclaimers

- REST n'est PAS une spécification !

- Dans plein de situation, des APIs dites "REST" ne le sont pas vraiment
   - ... certaines contraintes sont plus importantes que d'autres

- REST != HTTP
   - ... mais c'est implémenté en HTTP 99.99% du temps

- REST != JSON
   - ... mais c'est le format le plus utilisé

---

# Paradigme des API REST

- Notion de ressources (user, machine, depot de code, app, catalogue de produit, ...)
- Notion de représentation des ressources
    - REST: REpresentation State Transfer

- Exemple : représentation d'une ressource "contact" en JSON

```json
{
    "id": "98ef4a7b",
    "first_name": "Max",
    "last_name": "Dupont",
    "bith_date": "13/06/1987",
    "phone_number": "+33 6 35 65 65 65",
    "email": "max.dupont@sans-nuage.fr",
    "address": "3 rue du Moulin, 67853 Shoucroutheim"
}
```

---

# Exemple d'interactions REST

### Lister les contacts

`GET /contacts` -> Renvoie : une liste de représentation des contacts enregistrés

### Créer un nouveau contact (informations dans la payload HTML)

`POST /contacts` -> Renvoie : une représentation du contact créé

### Demander les infos sur le contact id=98ef4a7b

`GET /contacts/98ef4a7b` -> Renvoie : une représentation du contact

### Mettre à jour les infos sur le contact id=98ef4a7b

`PATCH /contacts/98ef4a7b` -> Renvoie : la nouvelle représentation du contact

### Supprimer le id=98ef4a7b

`DELETE /contacts/98ef4a7b` -> Renvoie : rien? (code 200..)


---


# Exemple d'interactions REST

Par contre on n'écrit pas : 

```
GET /create_user
```

(ça n'a pas de sens et pose des problèmes de sécurité ou de fonctionnement global de l'application ... le fonctionnement des requêtes GET et POST est vraiment différent !)

---

# Contraintes/propriété des REST API

- Client/Serveur
- Stateless (sans-état)
- Cacheability (possibilité de mise en cache)
- Layered system (système en couche)
- Interface uniforme 
- (Optionnel) Code à la demande

---

# 1. Client/serveur

- Séparation des préoccupations
- Le serveur n'a pas besoin de savoir comment le client fonctionne, et vice-versa
- Le serveur s'occupe des données (format, stockage, cohérence, ...), de l'authentification, ...
- Le client s'occupe d'aller chercher les données, de les présenter pour interagir avec l'utilisateur, ...
- Plusieurs types de clients peuvent exister
- Le serveur et le client peuvent être conçus indépendamment 

---

# 2. Stateless (sans état)

- Chaque requête contient l'entièreté des informations nécessaires à son traitement
- Les requêtes sont indépendantes les unes des autres
- Plusieurs requêtes consécutives peuvent être traités par des machines différentes (c.f. répartition de charge) de manière transparente
- Améliore la scalabilité du système, permet une certaine simplicité

---

# 3. Cacheability (possibilité de mise en cache)

- Le client (ou les intermédiaires techniques !) peuvent mettre en cache des résultats de requêtes
- À définir au cas par cas en fonction des ressources et des requêtes, explicitement ou implicitement
- Améliore les performances et la scalabilité
- Exemple : mise en cache d'une liste de 200 000 contacts

---

# 4. Système en couche

- Possibilité d'introduire des intermédiaires techniques dans la communication
- ... pour répartir la charge entre plusieurs machines
- ... et/ou pour mettre des données en cache
- ... et/ou pour séparer l'aspect business de l'aspect sécurité

---

# 5. Interface uniforme

- Définie par quatre sous-principes
   - Les ressources sont identifiées dans les requêtes (par ex. `/contact/98ef4a7b`)
   - Manipulation des ressources grâce à leur représentation
   - Messages auto-descriptifs
   - Hypermédia engine : possibilité de découvrir toutes les ressources et actions possibles depuis les réponses de l'API, sans conaissance a priori sur la structure

- Implicitement(?) : cohérence générale de l'écriture des requêtes

---


# 6. Code à la demande

- Propriété optionelle
- Possibilité pour le client de demander au serveur du code "à la volée" pour gérer certaines fonctionnalités 

---


# En pratique : les API REST en HTTP

- Notion de verbe et de nom
- Différents verbes : 
    - GET
    - POST (créer)
    - DELETE (supprimer)
    - PUT / PATCH (remplacer / mettre à jour)
- Moins utilisés : 
    - HEAD
    - OPTIONS

---

# En pratique : les API REST en HTTP

Une discussion plus exhaustive sur les verbes : 
- https://en.wikipedia.org/wiki/Representational\_state\_transfer#Relationship\_between\_URI\_and\_HTTP\_methods

---

# En pratique : les API REST en HTTP

- GET est une operation qui ne modifie pas l'etat
- GET, PUT et DELETE sont idempotent

---

# Lire une documentation d'API REST

- Par exemple, regardons la doc de l'API Github:

- https://docs.github.com/en/free-pro-team@latest/rest/overview/resources-in-the-rest-api
- https://docs.github.com/en/free-pro-team@latest/rest/reference/repos

---


# En pratique : outil pour tester / débuguer
    
- Firefox/Chromium, ou plus avancé : curl, Insomnia
    - https://insomnia.rest/download/
- Testons avec : 
   - https://api.github.com/repos/torvalds/linux/issues
   - https://api.github.com/repos/torvalds/linux/issues?page=2
   - https://api.github.com/repos/torvalds/linux/issues?page=100

---

# En pratique : interagir avec une API en Python

- "à la main" en utilisant `requests`
- ... ou bien des librairies qui proposent une interface deja toute faite
- Exemple de requete GET avec requests:

```python
url = "https://api.github.com/repos/torvalds/linux/issues"

r = requests.get(url)
if r.text != 200:
    raise Exception(r.text)
    
issues = json.loads(r.text)

for issue in issues:
    print(issue["title"])
```

---

# En pratique : interagir avec une API en Python

- Exemple de requete POST :

```python
pull_request = { 
    "title": "[feature] Add wireguard support to Linux kernel",
    "head": "wireguard-aaubin",
    "base": "master",
    "maintainer_can_modify": True
}

url = "https://api.github.com/repos/torvalds/linux/pulls"
r = requests.post(url, json.dumps(pull_request))

if r.text != 200:
    raise Exception(r.text)
```

(N.B. : j'ai triché un peu : pour vraiment créer une pull request, il faut être authentifié...)

---

# Authentification

- Sert typiquement à rendre une API (ou sous-partie d'API) privée ou introduire un rate-limit
- Gereneralement : se fait par token (+ eventuellement un login)
- Bonnes pratiques : 
    - un token différent par application
    - avec des permissions limitées à ce qui est nécessaire (c.f. OAuth)
    - le token n'est évidemment pas dans le code en dur et pas versionné !

Exemple:
```python
TOKEN = '0123456789abcdef'
r = requests.get('https://api.github.com/api/...', 
                 headers={'Authorization': 'token %s' % TOKEN})
```

---

# Authentification

- Dans des cas plus avancés : avec un certificat client

```bash
# Recuperer son certificat
$ curl https://badssl.com/certs/badssl.com-client.pem
```

puis:
```python
r = requests.get("https://client.badssl.com/")
# Renvoie une erreur 40x car pas de certif fourni

r = requests.get("https://client.badssl.com/", cert="badssl.com-client.pem")
# Un mot de passe est demandé en interactif pour déverouiller le certificat
# Il s'agit de : 'badssl.com'
```

---

# Versionnement des API

- Tout comme du code, le format d'une API est sujet à évolution ...
- Pour assurer la rétro compatibilité et de pouvoir faire évoluer cette API, il est crucial de mettre en place dès le début un versionnement de l'API (cóté serveur **et** côté client) AVANT de se rendre compte qu'on en aura besoin...

- Par exemple : 

```python
requests.get("https://example.com/api/v2/...")
```

- Peut aussi ẽtre géré via les headers HTTP : 

```python
requests.get("https://api.github.com/...", 
             headers={"Accept": "application/vnd.github.v3.full+json")
```

---

# Critique des API REST

- c.f. GraphQL, un type d'API plus moderne
- API statique 
- Multiples requetes
- N+1 problem: Overfetching / underfetching

---

# Références

- https://restfulapi.net/
- https://en.wikipedia.org/wiki/Representational_state_transfer
- https://www.django-rest-framework.org/

---

# Créer sa propre API avec Flask

## Flask En quelques mots

Un "micro-framework" pour faire du web, composé de plusieurs morceaux
- Vues gérées avec **Jinja**  (moteur de template avec une syntaxe "à la Python")
- Controleurs gérés avec **Werkzeug**  (une URL <-\> une fonction)
- Modèles gérées avec **SQLAlchemy**  (ORM : une classe <-\> une table SQL)

On peut y greffer pleins d'autres modules petits modules optionnels

Pour des applications plus grosses, on préferera tout même **Django** qui est un framework plus complet et puissant (mais plus complexe) mais qui suis la même logique

---

# Virtualenv

- Environnement virtuel
- Isoler des paquets / dépendances pour utiliser des versions spécifiques

```bash
# La premiere fois :
sudo apt install python-virtualenv python3-virtualenv virtualenv

# Creation d'un virtualenv 'venv'
virtualenv -p python3 venv
source venv/bin/activate

# Installation de dependances
pip3 install <une dependance...>
pip3 install <une autre dependance...>


# On développe, on teste, etc....


# Si on a fini et/ou que l'on veut "sortir" du virtualenv
deactivate
```

---

# Virtualenv "de base" pour Flask

```python
virtualenv -p python3 venv
source venv/bin/activate

pip install Flask
```

---

# Hello World en Flask

#### On associe l'url `/` à un controleur (= une fonction) qui renvoie `Hello World`

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

Mon controleur `hello_world()` doit renvoyer du texte ou une "HTTP response" (par exemple, erreur 404, ou redirection, ...)

---

# Hello World en Flask

Lancer le serveur web de test :

```bash
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

ensuite, je visite: 
```
http://127.0.0.1:5000/     # -> Affichera 'Hello world'
```

---

# Hello World en Flask

#### On peut créer d'autres controleur pour d'autres URLs...

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/python')
def python():
    return "Le python, c'est la vie!"
```

ensuite : 
```
http://127.0.0.1:5000/python    # -> Affichera 'Le python, c'est la vie!'
```

---

# Renvoyer du JSON avec Flask (`jsonify`)

```python
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/users')
def list_users():
    
    with open("/etc/passwd/") as f:
        etcpasswd = f.readlines()

    users = []
    for line in etcpasswd:
        user = line.split(":")[0]
        users.append(user)

    return jsonify(users)
```

---

# Routes avec des paramètres dans l'URL

```python
from flask import Flask
app = Flask(__name__)


@app.route('/users/<username>')
def get_user(username):
    
    with open("/etc/passwd/") as f:
        etcpasswd = f.readlines()

    for line in etcpasswd:
        if line.startswith(name + ":"):
             return "Cet utilisateur existe!"

    return "Cet utilisateur n'existe pas", 404
```

---

# Renvoyer du JSON avec Flask

```python
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/users/<username>')
def get_user(username):
    
    with open("/etc/passwd/") as f:
        etcpasswd = f.readlines()

    for line in etcpasswd:
        if line.startswith(name + ":"):
             infos = lines.split(":")
             return jsonify({
                  "username": username,
                  "uid": infos[1],
                  "home": infos[6],
                  "shell": infos[7],
             })

    return "Cet utilisateur n'existe pas", 404
```

---

# Gérer des requetes POST (`request`)

- Exemple à visée pedagogique uniquement ... pas faire des horreurs comme ça dans la vraie vie !

```python
@app.route('/users', methods=['POST'])
def create_user(username):
    
    with open("/etc/passwd/") as f:
        etcpasswd = f.readlines()

    for line in etcpasswd:
        if line.startswith(name + ":"):
             return "Cet utilisateur existe deja", 400

    try:
       data = json.loads(data)
       assert isinstance(data, dict)
       assert "username" in data
       assert data["username"].isalnum()
    except:
       return "Invalid data, not a valid json", 400

    os.system("useradd " + data["username"])
```

---

# Des vues pour les humains (HTML..)

```python
@app.route('/')
def homepage():
    users = User.query.all()
    return render_template('homepage.html', users=users)
```

`homepage.html` (template Jinja !)

```html
<html>
   <head>...</head>
<body>
    <ul>
    {% for user in users %}
        <li>{{user.username}}</li>
    {% endfor %}
    </ul>
<body>
```

---

# Aller plus loin : `Flask-restful`

- Fourni des classes comme `Ressource` permettant de gérer l'API avec de l'orienté objet
- Permet également de formaliser / parser plus facilement les paramètres des requetes POST
- Doc: https://flask-restful.readthedocs.io

```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
```

---

```python
from flask_restful import Resource, Api
api = Api(app)

class Contact(db.Model):
    
    name = db.Column(db.String(25), nullable=False, unique=True)

    def rest_repr(self):
        return {"name": self.name}

class ResourceContact(Resource):    

    # Correspondra à la route /contacts
    def get(self, name=None):
        return Contact.query.filter(Contact.name == name).first_or_404().rest_repr()

class ResourceContactList(Resource):

    def get(self):
        return [c.rest_repr() for c in Contact.query.all()]

api.add_resource(ResourceContactList, '/contacts')
api.add_resource(ResourceContact, '/contacts/<string:name>')
```

---

# Aller plus loin : `flasgger`

- Générer des documentation Swagger
- Basé sur les docstrings des routes
- Demo Swagger : https://petstore.swagger.io/
- Tutoriel Swagger : https://www.grafikart.fr/tutoriels/swagger-openapi-php-1160
- Doc Flasgger : https://pypi.org/project/flasgger/

---

# Exercices complémentaires

- Crash-course sur Git et Github
    - Demander dee identifiants au formateur
    - Créer un dépot pour votre code sur https://github.com/formationPythonSXB/
    - Pour les exos suivants, tenter de travailler dans une nouvelle branche (!= main) puis faire une pull request ?

- Ajouter une vue HTML pour visualiser la liste des machines et leur propriété
    - S'inspirer du template dans https://github.com/formationPythonSXB/contactManager

- Refactoriser le code de votre API pour utiliser `flask_sqlalchemy` plutôt qu'un json brut

- Tester d'ajouter un bout de documentation pour votre API avec `flasgger`
    - Valider qu'elle fonctionne en accédant à `http://127.0.0.1:5000/apidocs`

- Refactoriser le code de votre API pour utiliser `flask_restful` pour gérer les routes

- Regarder ce qu'il est possible de faire avec `Flask-admin`
