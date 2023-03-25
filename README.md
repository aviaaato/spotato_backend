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
    "password"    : "password",
}
```
- [x] `POST /api/spotter` : spotter inscription
```json
{
    "first_name"  : "first_name",
    "last_name"   : "last_name",
    "phone"       : "phone",
    "email"       : "email",
    "username"    : "username",
    "password"    : "password",
}

```
- [x] `POST /api/client/login` : client connexion 
```json
{
        "username": "username",
        "password": "password",
}
```
- [x] `POST /api/spotter/login` : spotter connexion
```json
{
        "username": "username",
        "password": "password",
}
```

- [x] `GET /api/client/` : obtenir détails d'un utilisateur
    - Need _User_ token

- [x] `GET /api/client/requests` : obtenir toutes les requetes demandées par un utilisateur
    - Need _User_ token


- [x] `POST /api/requests` : faire une nouvelle requete 
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
- [x] `GET /api/requests`: obtenir toutes les requetes
    - Need _Spotter_ token


- [x] `GET /api/requests/{request_id}` : obtenir détails d'une requete
    - Need _Spotter_ token

- [x] `PATCH /api/requests/{request_id}` : modifier requete (annuler, commencer, finir)
    - Need _Spotter_ token
```json
{
    "status": "start"
}
```

- [x] `PATCH /api/requests/{request_id}` : modifier requete (annuler, commencer, finir)
    - Need _Spotter_ token
```json
{
    "status": "start-chrono",
    "start_time": ""
}
```

- [ ] `PATCH /api/requests/{request_id}/cancel` : modifier requete (annuler, commencer, finir)

- [ ] `PATCH /api/requests/{request_id}/stop` : modifier requete (annuler, commencer, finir)


- [ ] `POST /api/transactions` : effectuer transaction

- [ ] `GET /api/users/transactions` : obtenir toutes les transactions d'un utilisateur

- [ ] `GET /api/users/account` : obtenir les détails du compte airtelmoney d'un utilisateur (en rapport avec l'application)

- [ ] `POST /api/transaction_callback` : callback de transaction

- [x] `GET /api/categorie` : get all categorie

