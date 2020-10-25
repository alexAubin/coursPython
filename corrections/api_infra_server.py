#!/usr/bin/env python
# encoding: utf-8

import datetime
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

datafile = "/tmp/apiformation.json"

def read_data():

    with open(datafile) as f:
        data = f.read()

    return json.loads(data)


def write_data(data):

    with open(datafile, "w") as f:
        f.write(json.dumps(data, indent=2))


if not os.path.exists(datafile):
    write_data([])


@app.route('/', methods=['GET'])
def root():
    return "Ici c'est la racine de l'API ! Tu cherches probablement la route /machines"


@app.route('/machines', methods=['GET'])
@app.route('/machines/<name>', methods=['GET'])
def get(name=None):

    records = read_data()

    if name:
        for record in records:
            if record['name'] == name:
                return jsonify(record)

        return "Cette machine n'existe pas ?", 404
    else:
        return jsonify(records)


@app.route('/machines', methods=['POST'])
def post():

    try:
        record = json.loads(request.data)
    except:
        record = {}

    try:
        assert all(field in record for field in ["name", "os", "ram", "owner"]), \
            "Il faut fournir les infos suivantes: name, os, ram and owner"
        assert isinstance(record["name"], str), "name doit etre une chaine"
        assert len(record["name"]) > 3, "Il faut choisir un nom plus long"
        assert len(record["name"]) < 30, "Il faut choisir un nom plus court"
        assert record["name"].isalnum(), "Le nom doit etre alphanumerique"

        assert isinstance(record["os"], str), "os doit etre une chaine"
        assert len(record["os"]) > 3, "Il faut choisir un nom d'os plus long"
        assert len(record["os"]) < 30, "Il faut choisir un nom d'os plus court"
        assert record["os"].isalnum(), "Le nom d'os doit etre alphanumerique"

        assert isinstance(record["owner"], str), "owner doit etre une chaine"
        assert len(record["owner"]) > 3, "Il faut choisir un nom d'owner plus long"
        assert len(record["owner"]) < 30, "Il faut choisir un nom d'owner plus court"
        assert record["owner"].isalnum(), "Le nom d'owner doit etre alphanumerique"

        assert isinstance(record['ram'], float) or isinstance(record['ram'], int), "La ram doit etre un entier ou float"
        assert record['ram'] > 0, "La ram doit etre positive, petit malin !"
        assert record['ram'] < 10000, "Ca fait beaucoup de Go pour une seule machine, j'espère que c'est pas toi qui paye !"

    except Exception as e:
        return str(e), 400

    records = read_data()

    if any(record["name"] == r["name"] for r in records):
        return "Cette machine existe deja", 400

    new_record = {
        "name": record["name"],
        "os": record["os"],
        "owner": record["owner"],
        "ram": float(record["ram"]),
        "state": "down",
        "since": datetime.datetime.now().__str__()
    }

    records.append(new_record)

    write_data(records)

    return jsonify(new_record)


@app.route('/machines/<name>/<action>', methods=['POST'])
def actions(name=None, action=None):
    if not action in ["start", "restart", "stop"]:
        return "Action invalide", 400

    records = read_data()

    if not any(name == r["name"] for r in records):
        return "Cette machine n'existe pas ?", 404

    record = [r for r in records if r["name"] == name][0]

    state = record["state"]
    if action == "start":
        if state != "down":
            return "Already started", 304
        else:
            record["state"] = "up"
            record["since"] = datetime.datetime.now().__str__()
    if action == "restart":
        record["state"] = "up"
        record["since"] = datetime.datetime.now().__str__()
    if action == "stop":
        if state != "up":
            return "Already stopped", 304
        else:
            record["state"] = "down"
            record["since"] = datetime.datetime.now().__str__()

    write_data(records)

    return jsonify(record)


@app.route('/machines/<name>', methods=['DELETE'])
def delete(name=None):

    records = read_data()

    if not any(name == r["name"] for r in records):
        return "Cette machine n'existe pas ?", 404

    records = [r for r in records if r["name"] != name]

    write_data(records)

    return "", 200

