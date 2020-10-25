from mydb import db

class App(db.Model):
    name = db.Column(db.String(20), unique=True, nullable=False)
    level = db.Column(db.Integer, nullable=True)
    url = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return "<App " + self.name + ">"