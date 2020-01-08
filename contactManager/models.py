from common import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Ici, on souhaite que chaque Contact dispose des champs:
    #  name :  un nom unique et obligatoire (type String)
    #  email : une adresse mail optionnelle (type String)
    #  phone : un numero de telephone optionnel (type String)
    #  birthday : une date de naissance optionnelle (type Date)
