title: Python : orienté-objet
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

# Orienté objet en Python

---

# Orienté objet

## Rappels (?)

- L'orienté objet est un paradigme de programmation
- Regrouper les variables et fonctions en entités ("objets") cohérentes qui appartiennent à des classes
   - **attributs** (les variables décrivant l'état de l'objet)
   - **méthodes** (les fonctions appliqubles à l'objet)
- Critique pour garder un code structuré et compréhensible quand la complexité d'un projet augmente
- Possibilité d'interfaçage avec les bases de données (c.f. ORM)

---

# Orienté objet

## Exemple

### **Les voitures** (classe) 

ont une couleur, une marque, un nombre de place et un kilométrage : ce sont des attributs. 

Elles peuvent embarquer des passager, rouler, activer un clignotant : ce sont des méthodes.

### **Ma voiture** (objet, ou instance) 

est une citroên rouge, 3 places et a parcouru 15672 km.

### **Celle de mon voisin** (autre objet, instance) 

est une peugeot bleue, 5 places et a parcouru 3450 km.

---

# Orienté objet

## Exemple en Python

```python
class Voiture:

   def __init__(self, couleur, marque, places=5, km=0):
       self.couleur = couleur
       self.marque = marque
       self.places = places
       self.km = km

   def rouler(self, km):
       self.km += km

########################################################

ma_voiture = Voiture("rouge", "citroen", places=3, km=15672)
voiture_voisin = Voiture("bleu", "peugeot", km=3450)

ma_voiture.rouler(143)
```

---

# Orienté objet

## Exemple en Python : précision

- `__init__` est le constructeur
- `__init__` et `rouler` sont des méthodes
- `self` correspond à l'objet en train d'être manipulé
- Toutes les méthodes ont au moins `self` comme premier argument 
- On utilise les methodes en faisant `un_objet.la_methode(...)`
- `self.couleur`, `self.marque`, `self.places`, `self.km` sont des attributs
- On instancie un object en faissant `mon_objet = Classe(...)`

---

# Orienté objet : héritage

Une classe peut hériter d'une autre pour étendre ses fonctionnalités. Inversement, cela permet de *factoriser* plusieurs classes ayant des fonctionnalités communes.

Par exemple, les **voitures**, les **camions** et les **vélos** sont trois types de **véhicules**.

En tant que véhicules, ils ont tous une couleur, une marque. Mais le nombre de place n'est pas très pertinent pour un vélo

---

# Orienté objet : héritage

```python
class Vehicule:
    
    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque

class Voiture(Vehicule):
    
    def __init__(self, couleur, marque, km=0, places=5):
        self.km = 0
        self.places = places
        super().__init__(couleur, marque)
        
    def rouler(self):
        self.km += km

class Velo(Vehicule):
    
    pass
```

---

```python
class Vehicule:

    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque

    def rouler(self, km):
        raise Exception("La classe fille doit implémenter cette fonction!")

class Voiture(Vehicule):
    
    def __init__(self, couleur, marque, km=0, places=5):
        self.km = 0
        self.places = places
        super().__init__(couleur, marque)
        
    def rouler(self, km):
        self.km += km

class Velo(Vehicule):
    
    def rouler(self, km):
        pass
```


---

# Orienté objet : héritage

### (suite de l'exemple)

```python
ma_voiture = Voiture("rouge", "citroen")
mon_velo = Velo("argent", "decatlhon")

ma_voiture.rouler(34)
mon_velo.rouler(21)

print(ma_voiture.km)
```

---

# Orienté objet : héritage

## À retenir

- `class Voiture(Vehicule)` fais hériter `Voiture` de `Vehicule`
- `super().__init__(...)` permet d'appeler le constructeur de la classe mère
- Les classes filles disposent des méthodes de la classe mère mais peuvent les **surcharger** (c.f. exemple avec `rouler`)
- `super().une_methode(...)` permet d'appeler `une_methode` telle que définie dans la classe mère.
- `isinstance` verifie l'heritage ! `isinstance(ma_voiture, Vehicule)` vaut `True` !

---

# Orienté objet : `@property`

## Des attributs "dynamiques"

```python
class Voiture(Vehicule):

    [ ... ]

    @property
    def total_emission_co2(self):
        return self.km * 0.0031


ma_voiture = Voiture("rouge", "citroen")
ma_voiture.rouler(342)

print("Ma voiture a émis %s g de CO2" % ma_voiture.total_emission_co2)
# -> Ma voiture a émis 1.0602 g de CO2
```

---

# Orienté objet : `@property`

### Autre exemple

```python
class Facture():

    def __init__(self, total):
        self.montant_total = total
        self.montant_deja_paye = 0

    @property
    def montant_restant_a_payer(self):
        return montant_total - montant_deja_paye


ma_facture = Facture(45)
ma_facture.montant_deja_paye += 7

print("Il reste %s à payer" % ma_facture.montant_restant_a_payer)
# -> Il reste 38 à payer
```

---

# Orienté objet : `pickle`

## Enregistrer des objets

`pickle` permet de "sérialiser" et "déserialiser" des objets (ou de manière générale des structure de données) en un flux binaire (!= texte).

### Sauvegarde

```python
import pickle

ma_facture = Facture(45)

f = open("save.bin", "wb")   # the 'b' in 'wb' is important !
pickle.dump(ma_facture, f)
```

---

# Orienté objet : `pickle`

## Enregistrer des objets

`pickle` permet de "sérialiser" et "déserialiser" des objets (ou de manière générale des structure de données) en un flux binaire (!= texte).

### Puis recuperation

```python
import pickle

f = open("save.bin", "rb")
ma_facture = pickle.load(f)
```

---

# Orienté objet : ORM

## Rappels (?) sur SQL

- Base de données : stocker des informations en masse et de manière efficace
- On manipule des tables (des lignes, des colonnes) ...
- Les colonnes sont fortement typées et on peut poser des contraintes (unicité, ...)
- Relations entres les tables, écritures concurrentes, ...
- Exemple de requête : 

```sql
# Create a table
CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)

# Add a record
INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)

# Find records
SELECT * FROM stocks WHERE qty=100;
```

---

# Orienté objet : ORM

## SQL "brut" en Python

```python
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Add a record
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes and close the connection
conn.commit()
conn.close()
```

---

# Orienté objet : ORM

## Object Relational Mapping

- Sauvegarder et charger des objets dans une base de donnée de type SQL de manière "transparente"
- Simplifie énormément l'interface entre Python et SQL
   - Python <-> base SQL
   - classes (ou modèle) <-> tables
   - objets <-> lignes
   - attributs <-> colonnes
- Gère aussi la construction et execution des requêtes (query)
- Syntaxe spéciale pour définir les types et les contraintes (en fonction de la lib utilisée)
- Librairie populaire et efficace : `SQLAlchemy` (on utilisera la surcouche `ActiveAlchemy`)

---

# Orienté objet : ORM

## Exemple de classe / modèle

```python
from active_alchemy import ActiveAlchemy

db = ActiveAlchemy('sqlite://foo.db')

class User(db.Model):
    # (id existe implicitement avec ActiveAlchemy)
    # id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(25), unique=True, nullable=False)
	location = db.Column(db.String(50), default="USA")
	birthday = db.Column(db.Date, nullable=True)
```

---

# Orienté objet : ORM

## Créer des tables et des objets

```python
# Supprimer toutes les tables (attention ! dans la vraie vie on fait des migrations...)
db.drop_all()
# Initialiser toutes les tables dont il y a besoin
db.create_all()

# Créer des utilisateurs
alex    = User(name="Alex",    location="Strasbourg")
bob     = User(name="Bob",     location="Strasbourg")
charlie = User(name="Charlie", location="Paris")

# Dire qu'on veut les enregistrer
db.session.add(alex)
db.session.add(bob)
db.session.add(charlie)

# Commiter les changements
db.session.commit()
```

---

# Orienté objet : ORM

## Exemple de requete (`query`)

```python

users_in_strasbourg = User.query()
                          .filter(User.location == "Strasbourg")

for user in users_in_strasbourg:
    print(user.name)

# On peut aussi faire : 
User.query().all()   # ---> Execute la query "pour de vrai" et renvoie une liste
User.query().filter(User.location == "Strasbourg").all()
```

---

# Orienté objet : ORM

## `query` ... plus complexes mais plus puissant !

```python
users_in_strasbourg = User.query()
                          .filter(User.location == "Strasbourg")

# Meme chose mais en selection des colonnes
users_in_strasbourg = User.query(User.name, User.last_access)
                          .filter(User.location == "Strasbourg")

# .. et avec un tri
users_in_strasbourg = User.query(User.name, User.last_access)
                          .filter(User.location == "Strasbourg")
                          .order_by(User.birthday)
```

