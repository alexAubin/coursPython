import requests
import json

class Infra:
    
    def __init__(self, api_root):
        self.api_root = api_root
    
    def _request(self, method, route, payload={}):
        if method == "GET":
            r = requests.get(self.api_root + route)
        elif method == "DELETE":
            r = requests.delete(self.api_root + route)
        elif method == "POST":
            r = requests.post(self.api_root + route, json.dumps(payload))
        else:
            raise Exception("invalid method")

        if r.status_code != 200:
            raise Exception(r.text)
        elif method in ["GET", "POST"]:
            return r.json()

    def list(self):   
        return self._request("GET", "/machines")
        
    def get(self, name):
        return self._request("GET", "/machines/" + name)
    
    def create(self, name, owner, os, ram):
        data = {"name": name, "owner": owner, "ram": ram, "os": os}
        return self._request("POST", "/machines", data)
    
    def delete(self, name):
        self._request("DELETE", "/machines/" + name)
    
    def start(self, name):
        self._request("POST", "/machines/" + name + "/start")
    
    def stop(self, name):
        self._request("POST", "/machines/" + name + "/stop")

    def restart(self, name):
        self._request("POST", "/machines/" + name + "/restart")


infra = Infra("https://dismorphia.info/apiformation")

all_machines = infra.list()
print(infra.get("google"))

for machine in all_machines:
    if machine["name"] == "ibformation":
        infra.delete("ibformation")


    
ib = infra.create(name="ibformation", owner="ibformation", os="windoze", ram=4)
print(ib)
assert ib["name"] == "ibformation"
assert ib["state"] == "down"

infra.start("ibformation")
ib = infra.get("ibformation")
assert ib["state"] == "up"