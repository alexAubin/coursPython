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

# Orienté objet

## Heritage

Une classe peut hériter d'une autre pour étendre ses fonctionnalités. Inversement, cela permet de *factoriser* plusieurs classes ayant des fonctionnalités communes.

Par exemple, les **voitures**, les **camions** et les **vélos** sont trois types de **véhicules**.

En tant que véhicules, ils ont tous une couleur, une marque. Mais le nombre de place n'est pas très pertinent pour un vélo

---

# Orienté objet

```python
class Vehicule:
    
    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque

class Voiture(Vehicule):
    
    def __init__(self, couleur, marque, km=0, places=5):
        self.km = 0
        self.places = places
        super().__init__(self, couleur, marque)
        
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
        super().__init__(self, couleur, marque)
        
    def rouler(self, km):
        self.km += km

class Velo(Vehicule):
    
    def rouler(self, km):
        pass
```


---

# Orienté objet

## Héritage : suite de l'exemple

```python
ma_voiture = Voiture("rouge", "citroen")
mon_velo = Velo("argent", "decatlhon")

ma_voiture.rouler(34)
mon_velo.rouler(21)

print(ma_voiture.km)
```

---

# Orienté objet

## Héritage : à retenir

- `class Voiture(Vehicule)` fais hériter `Voiture` de `Vehicule`
- `super().__init__(...)` permet d'appeler le constructeur de la classe mère
- Les classes filles disposent des méthodes de la classe mère mais peuvent les **surcharger** (c.f. exemple avec `rouler`)
- `super().une_methode(...)` permet d'appeler `une_methode` telle que définie dans la classe mère.
- `isinstance` verifie l'heritage ! `isinstance(ma_voiture, Vehicule)` vaut `True` !

---

# Orienté objet

## `@property` :  des attributs "dynamiques"

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

# Orienté objet

## `@property` : autre exemple

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

# Orienté objet

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

# Orienté objet

## Enregistrer des objets avec `pickle`

`pickle` permet de "sérialiser" et "déserialiser" des objets (ou de manière générale des structure de données) en un flux binaire (!= texte).

### Puis recuperation

```python
import pickle

f = open("save.bin", "rb")
ma_facture = pickle.load(f)
```

