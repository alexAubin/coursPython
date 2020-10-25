import json
import requests

def charger_json():
    
    r = requests.get("https://app.yunohost.org/apps.json", timeout=15)
    
    assert r.status_code == 200
    
    return json.loads(r.text)

def filtrer_level(apps, N):
    
    liste_filtree = []
    
    # pour chaque app
    for app, infos in apps.items():

        # regarder si level > N
        if isinstance(infos.get("level"), int) \
           and infos["level"] > N:
            
            # si oui, ajouter le nom de l'app dans liste_filtree
            liste_filtree.append(app)
    
    return liste_filtree

apps = charger_json()
apps_level_7 = filtrer_level(apps, 7)

with open('apps_level_7.json', 'w') as f:
    json.dump(apps_level_7, f, indent=4)