# spotato_backend doc

## Endpoints

- [x] `POST /api/client` : client inscription
```json
{
    "first_name"  : "first_name",
    "last_name"   : "last_name",
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

- [x] `GET /api/client/` : obtenir détails d'un utilisateur , **need token**
 
- [x] `GET /api/client/requests` : obtenir toutes les requetes demandées par un utilisateur **need token**


- [ ] `POST /api/requests` : faire une nouvelle requete
- [ ] `GET /api/requests`: obtenir toutes les requetes

- [ ] `GET /api/requests/{request_id}` : obtenir détails d'une requete

- [ ] `PATCH /api/requests/{request_id}/start` : modifier requete (annuler, commencer, finir)

- [ ] `PATCH /api/requests/{request_id}/cancel` : modifier requete (annuler, commencer, finir)

- [ ] `PATCH /api/requests/{request_id}/stop` : modifier requete (annuler, commencer, finir)


- [ ] `POST /api/transactions` : effectuer transaction

- [ ] `GET /api/users/{user_id}/transactions` : obtenir toutes les transactions d'un utilisateur

- [ ] `GET /api/users/{user_id}/account` : obtenir les détails du compte airtelmoney d'un utilisateur (en rapport avec l'application)

- [ ] `POST /api/transaction_callback` : callback de transaction
