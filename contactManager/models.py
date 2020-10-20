from common import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Ici, on souhaite que chaque Contact dispose des champs:
    #  name :  un nom unique et obligatoire (type String)
    name = db.Column(db.String(25), unique=True, nullable=False)
    #  email : une adresse mail optionnelle (type String)
    email = db.Column(db.String(50), nullable=True)
    #  phone : un numero de telephone optionnel (type String)
    phone = db.Column(db.String(10), nullable=True)

    #  birthday : une date de naissance optionnelle (type Date)
