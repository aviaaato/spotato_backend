# spotato_backend doc

## Endpoints

- [x] `POST /api/users` : inscription
- [x] `POST /api/login` : connexion

- [ ] `GET /api/users/{user_id}` : obtenir détails d'un utilisateur
 
- [ ] `GET /api/users/{user_id}/requests` : obtenir toutes les requetes demandées par un utilisateur


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
