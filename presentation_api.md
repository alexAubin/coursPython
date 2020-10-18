

# Contexte

- Construire des sites web ou application mobile
- Automatiser des traitements (bots, analyse, ...)


# API

- Application Programming Interface

# REST API

- Un style d'architecture d'API
- Défini par 5 principes généraux (+ 1 optionnel)
- Défini par un thesard dans les années 2000 (en parallèle de HTTP 1.1)

- Objectifs : 
    - simplicité des systèmes
    - performance
    - scalability / passage à l'échelle
    - portabilité

# Disclaimer

- REST n'est PAS une spécification !
- Dans plein de situation, des APIs dites "REST" ne le sont pas vraiment
- ... certaines contraintes sont plus importantes que d'autres

- REST != HTTP
- ... mais c'est implémenté en HTTP 99.99% du temps

- REST != JSON
- ... mais c'est le format le plus utilisé

# Paradigme des API REST

- Notion de ressource
- Notion de représentation de ressources
    - REST: REpresentation State Transfer

- Exemple : représentation d'une ressource "contact" en JSON

```json
{
    "id": "98ef4a7b"
    "first_name": "Max",
    "last_name": "Dupont",
    "bith_date": "13/06/1987",
    "phone_number": "+33 6 35 65 65 65",
    "email": "max.dupont@sans-nuage.fr",
    "address": "3 rue du Moulin, 67853 Shoucroutheim"
}
```

# Exemple d'interactions REST

```
GET /contacts             # Demander la liste des contacts
                          # -> Renvoie : une liste de représentation des contacts enregistrés

POST /contacts            # Créer un nouveau contact (informations dans la payload HTML)
                          # -> Renvoie : une représentation du contact créé

GET /contacts/98ef4a7b    # Demander les infos sur le contact avec id=98ef4a7b
                          # -> Renvoie : une représentation du contact

PATCH /contacts/98ef4a7b  # Mettre à jour les infos sur le contact id=98ef4a7b
                          # -> Renvoie : la nouvelle représentation du contact
```

# Exemple d'interactions REST

Par contre on n'écrit pas : 

```
GET /create_user
```

(ça n'a pas de sens et pose des problèmes de sécurité ou de fonctionnement global de l'application ... le fonctionnement des requêtes GET et POST est vraiment différent !)

# Contraintes/propriété des REST API

- 1. Client/Serveur
- 2. Stateless (sans-état)
- 3. Cacheability (possibilité de mise en cache)
- 4. Layered system (système en couche)
- 5. Interface uniforme 
- 6. (Optionnel) Code à la demande

# 1. Client/serveur

- Séparation des préoccupations
- Le serveur n'a pas besoin de savoir comment le client fonctionne, et vice-versa
- Le serveur s'occupe des données (format, stockage, cohérence, ...), de l'authentification, ...
- Le client s'occupe d'aller chercher les données, de les présenter pour interagir avec l'utilisateur, ...
- Plusieurs types de clients peuvent exister
- Le serveur et le client peuvent être conçus indépendamment 

# 2. Stateless (sans état)

- Chaque requête contient l'entièreté des informations nécessaires à son traitement
- Plusieurs requêtes consécutives peuvent être traités par des serveurs différents
- Améliore la scalabilité du système

# 3. Cacheability (possibilité de mise en cache)

- Le client (ou les intermédiaires techniques !) peuvent mettre en cache des résultats de requêtes
- À définir au cas par cas en fonction des ressources et des requêtes, explicitement ou implicitement
- Améliore les performances et la scalabilité
- Exemple : mise en cache d'une liste de 20 000 contacts

# 4. Système en couche

- Possibilité d'introduire des intermédiaires techniques dans la communication
- ... pour répartir la charge entre plusieurs machines
- ... et/ou pour mettre des données en cache
- ... et/ou pour séparer l'aspect business de l'aspect sécurité

# 5. Interface uniforme

- Définie par quatre sous-principes
   - Les ressources sont identifiées dans les requêtes (par ex. `/contact/98ef4a7b`)
   - Manipulation des ressources grâce à leur représentation
   - Messages auto-descriptifs
   - Hypermédia engine : possibilité de découvrir toutes les ressources et actions possibles depuis les réponses de l'API, sans conaissance a priori sur la structure

- Implicitement(?) : cohérence générale de l'écriture des requêtes

# 6. Code à la demande


# En pratique : les API REST en HTTP

- Notion de verbe et de nom
- Différents verbes : 
    - GET
    - POST
    - DELETE
    - PUT / PATCH
- Moins utilisés : 
    - HEAD
    - OPTIONS

# Lire une documentation d'API REST

# En pratique : interagir avec une API en Python

# En pratique : outil pour tester / débuguer

# En pratique : créer une API en Python

# Authentification

# De l'importance de versionner les API

# Références

https://restfulapi.net/
https://en.wikipedia.org/wiki/Representational_state_transfer
https://www.django-rest-framework.org/

