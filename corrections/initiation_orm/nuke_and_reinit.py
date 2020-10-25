import json
from mydb import db
from models import App

db.drop_all()
db.create_all()

with open("apps.json") as f:
    apps_from_json = json.loads(f.read())

for app, infos in apps_from_json.items():
    a = App(name=app, level=infos["level"], url=infos["git"]["url"])
    db.session.add(a)

db.session.commit()

apps_level_3 = App.query().filter(App.level == 3)
for app in apps_level_3:
    print(app.name)
