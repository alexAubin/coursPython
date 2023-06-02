from common import app, db
from flask import render_template, request, redirect
from models import Contact


# Cette fonction gère l'affichage de la page d'acceuil ( '/' ) de l'app web
@app.route('/')
def homepage():

    # Ici, nous devons recuperer la liste de tous les Contact qui existent
    # et mettre ça dans la variable 'contacts' qui ensuite utilisée par le template

    contacts = Contact.query.all()

    return render_template('homepage.html', contacts=contacts)


# Cette fonction gère ce qu'il se passe lorsqu'on appuie sur le bouton 'Ajouter'
@app.route('/add', methods=['POST'])
def add_contact():

    # Ici, on veut créer et ajouter à la base de donnée un nouveau Contact
    #
    # Les données du formulaire fournie par l'utilisateur sont disponibles
    # dans request.form qui a cette structure :
    # { "name": "Sacha",
    #   "phone": "0612345678",
    #   "email": "sacha@example.com",
    #   "birthday": "16/03/1993"
    # }
    # 1. Créer l'objet Contact
        # note : convertir la valeur associée à "birthday" en objet datetime peut être compliqué.
        # Dans un premier temps on peut forcer la valeur à None pour valider que le reste marche...

    new_contact = Contact(name=request.form["name"],
                          email=request.form["email"],
                          phone=request.form["phone"])


    # 2. L'ajouter à la base (et commiter l'ajout)

    db.session.add(new_contact)
    db.session.commit()

    # Une fois le contact ajouté, nous redirigeons l'utilisateur vers la page
    # d'acceuil (cela déclenche un rafraichissement de la page)
    return redirect("/")
