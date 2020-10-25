import requests
import json
import datetime

url = "https://api.github.com/orgs/yunohost-apps/repos"
token = "bb49a935a770e6b510d75bafe735596b1ebaa199"
headers = {"Authorization": "token %s" % token }

def get_all_repos():
    for page in range(0, 500):
        
        print("Fetching page %s" % page)
        
        r = requests.get(url + "?page=%s" % page, headers=headers)
        
        if r.status_code != 200:
            raise Exception(r.text)
        
        # Si il n'y a plus rien dans la page, on sort de la boucle
        # (On aurait pu aussi écrire r.json() == [] )
        if not r.json():
            break

        for repo in r.json():
            yield repo

def is_inactive(repo):
    pushed_at = datetime.datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
    date_diff = datetime.datetime.now() - pushed_at
    two_years = 365 * 2
    return date_diff.days > two_years


def get_all_inactive_repos():
      
    for repo in get_all_repos():
        if is_inactive(repo):
            yield repo


inactive_repos = list(get_all_inactive_repos())

print("Trouvé %s dépots inactifs" % len(inactive_repos))
print("---------------")
for repo in inactive_repos:
    print(repo["name"])