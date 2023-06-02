from active_alchemy import ActiveAlchemy

db = ActiveAlchemy("sqlite:///foo.db") # DB file

class User(db.Model):
	name = db.Column(db.String(25), unique=True)
	location = db.Column(db.String(50), default="USA")
	last_access = db.Column(db.DateTime)

def main():

    db.drop_all()
    db.create_all()

    for user in User.query():
        print(user.name)

    user = User.create(name="Mardix", location="Moon")
    user2 = User.create(name="Mardix", location="Moon")
    db.session.add(user2)
    db.session.commit()

main()
