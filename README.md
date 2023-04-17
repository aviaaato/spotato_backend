# spotato_backend doc

## Endpoints

- [x] `POST /api/client` : client inscription
```json
{
    "first_name"  : "first_name",
    "last_name"   : "last_name",
    "phone"       : "phone",
    "email"       : "email",
    "username"    : "username",
    "password"    : "password"
}
```
---
- [x] `GET /api/client` : obtenir détails d'un utilisateur
    - Need _User_ token
---
- [x] `POST /api/client/login` : client connexion , return user token
```json
{
        "username": "username",
        "password": "password"
}
```
---
- [x] `POST /api/spotter` : spotter inscription
```json
{
    "first_name"  : "first_name",
    "last_name"   : "last_name",
    "phone"       : "phone",
    "email"       : "email",
    "username"    : "username",
    "password"    : "password"
}
```
---

- [x] `GET /api/spotter` : obtenir détails d'un utilisateur
    - Need _Spotter_ token
---

- [x] `POST /api/spotter/login` : spotter connexion
```json
{
        "username": "username",
        "password": "password"
}
```
---

- [x] `GET /api/request/client` : obtenir toutes les requetes demandées par un utilisateur
    - Need _User_ token
---

- [x] `POST /api/request` : faire une nouvelle requete
    - <b>Need _User_ token</b>
```json
{
    "label" : "label",
    "description" : "description",
    "categorie" : 1,
    "latitude" : "latitude",
    "longitude" : "longitude",
    "duration" : "duration",
    "requested_start_time" : "requested_start_time",
    "montant" : "montant"
}
```
---

- [x] `GET /api/request`: obtenir toutes les requetes
    - Need _Spotter_ token or _Client_ token
---

- [x] `GET /api/request/{request_id}` : obtenir détails d'une requete
    - Need _AnyUser_ token
---

- [x] `GET /api/categorie` : get all categorie
