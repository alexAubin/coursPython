from common import db
from models import Contact

# Ici on souhaite créer un petit script qui va supprimer les données existantes, recréer les bases nécessaires, et ajouter des valeurs "de test"

# 1. Supprimer toutes les tables existantes
# 2. Creer toutes les tables nécessaire
db.drop_all()
db.create_all()

# 3. Créer des objets Contact "de test" (par exemple Alice, Bob, Charlie) en utilisant des données fictives
alice = Contact(name="Alice", email="alice@gmail.com", phone="1234567")
bob = Contact(name="Bob", email="bob@hotmail.fr", phone="5837293")
charlie = Contact(name="Charlie", email="charlie@yahoo.fr", phone="0918375")

# 4. Ajouter (et commiter) ces nouveaux objets dans la base
db.session.add(alice)
db.session.add(bob)
db.session.add(charlie)
db.session.commit()
