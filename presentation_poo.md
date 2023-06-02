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

## Autre exemple

### **Les cercles** (classe)

ont un centre, un rayon, une couleur, une épaisseur de trait : ce sont des attributs.

On peut : déplacer le cercle, l'agrandir, calculer son aire, le dessiner sur l'écran  : ce sont des méthodes.

### **Un petit cercle rouge** (objet, ou instance)

centre = (3, 5), rayon = 2, couleur = "red", épaisseur = 0.1

### **Un grand cercle bleu** (autre objet, instance)

centre = (-4, 2), rayon = 6, couleur = "blue", épaisseur = 1

---

# Orienté objet

## Exemple en Python

```python
class Cercle:

   def __init__(self, centre, rayon, couleur="black", epaisseur=0.1):
       self.centre = centre
       self.rayon = rayon
       self.couleur = couleur
       self.epaisseur = epaisseur

   def deplacer(self, dx=0, dy=0):
       self.centre = (self.centre[0]+dx, self.centre[1]+dy)

########################################################

cercle1 = Cercle((3, 5), 2, "red")
cercle2 = Cercle((-4, 2), 6, "blue", epaisseur=1)

cercle1.deplacer(dy=2)
print(cercle1.centre)
```

---

# Orienté objet

## Exemple en Python : précisions

- `__init__` est le constructeur
- `__init__` et `deplacer` sont des méthodes
- `self` correspond à l'objet en train d'être manipulé
- Toutes les méthodes ont au moins `self` comme premier argument
- On utilise les methodes en faisant `un_objet.la_methode(...)`
- `self.centre`, `self.rayon`, `self.couleur`, `self.epaisseur` sont des attributs
- On instancie un objet en faissant `mon_objet = Classe(...)`

---

# Orienté objet : héritage

Une classe peut hériter d'une autre pour étendre ses fonctionnalités. Inversement, cela permet de *factoriser* plusieurs classes ayant des fonctionnalités communes.

Par exemple, les **cercles**, les **carrés** et les **étoiles** sont trois types de **figures géométriques**.

En tant que figure géométriques, elles ont toutes un centre, une couleur et une épaisseur utilisés pour le dessin. On peut les déplacer, et on peut calculer leur aire.

---

```python
class FigureGeometrique:

    def __init__(self, centre, couleur="black", epaisseur=0.1):
        self.centre = centre
        self.couleur = couleur
        self.epaisseur = epaisseur

    def deplacer(self, dx=0, dy=0):
        self.centre = (self.centre[0]+dx, self.centre[1]+dy)

class Cercle(FigureGeometrique):

    def __init__(self, centre, rayon, couleur="black", epaisseur=0.1):
        self.rayon = rayon
        super().__init__(centre, couleur, epaisseur)

class Carre(FigureGeometrique):

    def __init__(self, centre, cote, couleur="black", epaisseur=0.1):
        self.cote = cote
        super().__init__(centre, couleur, epaisseur)
```

---

```python
class FigureGeometrique:

    def __init__(self, centre, couleur="black", epaisseur=0.1):
        self.centre = centre
        self.couleur = couleur
        self.epaisseur = epaisseur

    def deplacer(self, dx=0, dy=0):
        self.centre = (self.centre[0]+dx, self.centre[1]+dy)

class Cercle(FigureGeometrique):

    def __init__(self, centre, rayon, couleur="black", epaisseur=0.1):
        self.rayon = rayon
        super().__init__(centre, couleur, epaisseur)

class Carre(FigureGeometrique):

    def __init__(self, centre, cote, couleur="black", epaisseur=0.1):
        self.cote = cote
        super().__init__(centre, couleur, epaisseur)
```


---

```python
class FigureGeometrique:

    # def __init__ ...

    def deplacer(self, dx=0, dy=0):
        self.centre = (self.centre[0]+dx, self.centre[1]+dy)

    def aire(self):
        raise NotImplementedError("La classe fille doit implémenter cette fonction!")

class Cercle(FigureGeometrique):

    # def __init__ ...

    def aire(self):
        return 3.1415 * self.rayon * self.rayon

class Carre(FigureGeometrique):

    # def __init__ ...

    def aire(self):
        return self.cote ** 2
```


---

# Orienté objet : héritage

### (suite de l'exemple)

```python
cercle_rouge = Cercle((3, 5), 2, "red")
carre_vert  = Carre((5, -1), 3, "green", epaisseur=0.2)

cercle_rouge.deplacer(dy=2)
carre_vert.deplacer(dx=-3)

print(carre_vert.centre) # -> affiche (2, -1)
print(carre_vert.aire()) # -> affiche 9
```

---

# Orienté objet : héritage

### (llustration du polymorphisme)

```python
formes = [Cercle((3, 5), 2, "red"),
          Carre((5, -1), 3, "green"),
          Cercle((-2, 4), 5, "yellow"),
          Carre((4, -2), 2, "purple")]

for forme in formes:
    print(forme.aire())
```

(c.f. aussi [autre exemple sur stack overflow](https://stackoverflow.com/a/3724160))

---

# Orienté objet : héritage

## À retenir

- `class Cercle(FigureGeometrique)` fais hériter `Cercle` de `FigureGeometrique`
- `super().__init__(...)` permet d'appeler *le constructeur de la classe mère*
- Les classes filles disposent des méthodes de la classe mère mais peuvent les **surcharger** (c.f. exemple avec `aire`)
- `super().une_methode(...)` permet d'appeler `une_methode` telle que définie dans la classe mère.
- `isinstance` verifie l'heritage ! `isinstance(cercle_rouge, FigureGeometrique)` vaut `True` !


---

# Orienté objet : aller + loin

## Méthodes spéciales / "magiques"

- `__repr__` et `__str__` : génère une représentation de l'objet sous forme de chaîne de caractère

```python
   def __repr__(self):
      return "Cercle de couleur " + self.color + " et de rayon " + self.rayon
```

- `__add__` : définir l'addition de deux objets

- `__eq__` : définir l'égalité entre deux objets

- `__iter__` : définir comment itérer sur un objet

- ... [et plein d'autres](https://docs.python.org/3/reference/datamodel.html) ...

---

# Orienté objet : aller + loin

## Attributs 'statiques' (partagés par tous les objets d'une classe)

```python
class FormeGeometrique():

    nb_instances = 0

    def __init__(self):
        FormeGeometrique.nb_instances += 1

forme1 = FormeGeometrique()
forme2 = FormeGeometrique()
forme3 = FormeGeometrique()

print(FormeGeometrique.nb_instances)
# -> affiche 3
```

---

# Orienté objet : aller + loin

## Quelques astuces

- `dir(un_objet)` : listes tous les attributs / methodes d'un objet (ou module)
- Il existe aussi `un_objet.__dict__` 
- `MaClasse.__subclasses__()` : lister toutes les classes filles d'une classe

---

# Orienté objet : aller + loin

##  Des attributs "dynamiques" avec `@property`

```python
class Carre(FigureGeometrique):

    # [ ... ]

    @property
    def aire(self):
        return self.cote * self.cote


carre_vert  = Carre((5, -1), 3, "green", epaisseur=0.2)
print(carre_vert.aire) # N.B. : plus besoin de mettre de parenthèse ! Se comporte comme un attribut
```

---

# Orienté objet : aller + loin

## Autre exemple avec `@property`

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

# Orienté objet : aller + loin

## Attributs et méthodes privées

- Il est possible de définir des attributs et méthode privées si elles commencent par `__`
   - par exemple: `self.__toto`
- Un attribut / méthode privée de peut être appelé que depuis "l'intérieur de la classe"
   - attention : il ne s'agit pas de vraie "privacy" mais plutot de disuasion...

---

# Orienté objet : aller + loin

## Attributs et méthodes privées

- On peut étre tenté de définir des getters et setters `get_toto()`, `set_toto()` pour interagir avec les attributs privés ... mais la façon pythonique est:

```python
        @property
        def toto(self):
            return self.__toto

        @toto.setter
        def toto(self, value):
            self.__toto = value   # ... ou tout autre traitement
```


---

# Orienté objet : aller + loin

## Attributs et méthodes privées


On peut ensuite accéder et modifier l'attribut `toto` de manière transparente : 

```python
monobjet = Objet()

print(monobjet.toto)

monobjet.toto = 3
```


---

# Orienté objet : aller + loin

## Enregistrer des objets avec `pickle`

`pickle` permet de "sérialiser" et "déserialiser" des objets (ou de manière générale des structure de données) en un flux binaire (!= texte).

### Sauvegarde

```python
import pickle

ma_facture = Facture(45)

f = open("save.bin", "wb")   # the 'b' in 'wb' is important !
pickle.dump(ma_facture, f)
```

---

# Orienté objet : aller + loin

## Enregistrer des objets avec `pickle`

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
CREATE TABLE members (username text, email text, memberSince date, balance real)

# Add a record
INSERT INTO members VALUES ('alice', 'alice@gmail.com', '2017-11-05', 35.14)

# Find records
SELECT * FROM members WHERE balance>0;
```

---

# Orienté objet : ORM

## SQL "brut" en Python

```python
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE members
             (username text, email text, memberSince date, balance real)''')

# Add a record
c.execute("INSERT INTO members VALUES ('alice', 'alice@gmail.com', '2017-11-05', 35.14)")

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

db = ActiveAlchemy('sqlite:///members.db')

class Member(db.Model):
	username    = db.Column(db.String(25), nullable=False, unique=True)
	email       = db.Column(db.String(50), nullable=True)
	memberSince = db.Column(db.Date,       nullable=False)
    balance     = db.Column(db.Float,      nullable=False, default=0.0)
    active      = db.Column(db.Boolean,    nullable=False, default=True)
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
alice   = Member(name="Alice",   memberSince=datetime.date(day=5, month=11, year=2017))
bob     = Member(name="Bob",     memberSince=datetime.date.today(), balance=15)
camille = Member(name="Camille", memberSince=datetime.date(day=7, month=10, year=2018), balance=10)

# Dire qu'on veut les enregistrer
db.session.add(alice)
db.session.add(bob)
db.session.add(camille)

# Commiter les changements
db.session.commit()
```

---

# Orienté objet : ORM

## Exemple de requete (`query`)

```python
all_members = Member.query().all()

active_members = Member.query()
                .filter(Member.active == True)
                .order_by(Member.memberSince)

for member in active_members:
    print(user.name)
```
