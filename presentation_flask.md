title: Python : introduction à Flask
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
# Introduction à Flask

---

# Flask

## En quelques mots (détaillés ensuite)

- un "micro-framework" pour faire du web
- typiquement dans un **virtualenv**
- Werkzeug : une URL = une fonction (controlleur?) 
- Jinja : système de **template** (vues?)
- SQLAlchemy : une classe = table dans une BDD (models, ORM)

---

# Virtualenv

- Environnement virtuel
- Isoler des paquets / dépendances pour utiliser des versions spécifiques

```bash
# La premiere fois :
sudo apt install python-virtualenv python3-virtualenv

# Creation d'un virtualenv 'venv'
virtualenv -p python3 venv
source venv/bin/activate

# Installation de dependance, manipulation ...
pip3 install <une dependance...>
<une commande...>

# Si on a fini et/ou que l'on veut "sortir" du virtualenv
deactivate
```

---

# Virtualenv "de base" pour Flask

```python
virtualenv -p python3 venv
source venv/bin/activate

pip install Flask
pip install Flask-Script
pip install Flask-SQLAlchemy
```

---

# Flask's Hello World

### URL = Fonction

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

ensuite : 
```
http://monsite.com/   # -> Affichera 'Hello world'
```

( `@app.route('/')` s'apelle un décorateur )

---

# Flask's Hello World

Lancer le serveur web de test/dev :

```bash
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

---

# Templating / Jinja

Un template ressemble à

```jinja
  Bonjour {% prenom %} !

  {% for app in apps %}
    {{ app.name }} est niveau {{ app.level }} !
  {% endfor %}
```

avec par exemple : 

```python
prenom = "Alex"
apps = [ { "name": "mailman", "level": 2 },
         { "name": "wordpress", "level": 7 } ]
```

---

# Templating / Jinja

Rendu : 

```
  Bonjour Alex !

  mailman est niveau 2 !
  wordpress est niveau 7 !
```

---

# Templates dans Flask

En supposant que le template précédent soit situé dans `templates/hello.html`

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Alex"):
    apps = [ { "name": "mailman", "level": 2 },
             { "name": "wordpress", "level": 7 } ]
    return render_template('hello.html', 
                           name=name,
                           apps=apps)
```

---

# SQL Alchemy, Models / ORM in Flask

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'
db = SQLAlchemy()
db.init_app(app)


class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    date_last_test = db.Column(db.Datetime, nullable=True)
```

---

# SQL Alchemy, Models / ORM in Flask

### Ecrire

```python
# Creer et ajouter une app dans la database...
mailman = App(name="mailman", level=3)
db.session.add(mailman)
db.session.commit()
```

### Lire

```python
# Trouver toutes les apps..
App.query.all()

# Trouver toutes les apps level 7 ...
App.query.filter_by(level=7).all()

# Trouver l'app qui s'apelle mailman
App.query.filter_by(name="mailman").first()
```


