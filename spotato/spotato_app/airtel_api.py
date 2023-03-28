import uuid

import requests

MY_PHONE_NUMBER = "339337013"
TECH_ZARA = "333005864"


def get_authorisation() -> dict:
    """Get access Authorisation
    :return: json
    """
    client_id = "2601f408-027d-4dc5-a538-f995bf4ee17d"
    client_secret = "a353ed73-c3cf-4c97-8135-13f4a1976cc1"
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    json_data = {"client_id": client_id, "client_secret": client_secret,
                 "grant_type": "client_credentials", }
    response = requests.post("https://openapiuat.airtel.africa/auth/oauth2/token", headers=headers, json=json_data)
    return response.json()


class AirtelApi:
    def __init__(self):
        self.__access_token = get_authorisation()["access_token"]

    def get_access_token(self):
        """Return the access token of api"""
        token = self.__access_token
        return token

    def get_user_information(self, phone_number: str) -> dict:
        """Get information of user by phone number
        :param phone_number:
        :return:
        """

        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "X-Country": "MG",
            "X-Currency": "MGA",
            "Authorization": f'Bearer {self.__access_token}',
        }

        request = f'https://openapiuat.airtel.africa/standard/v1/users/{phone_number}'

        response = requests.get(request, headers=headers)

        return response.json()

    def payments(self, phone_number: str, valuer: int) -> dict:
        """Ask payment validation from some client by phone number"""
        transaction_id = str(uuid.uuid4())

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'X-Country': 'MG',
            'X-Currency': 'MGA',
            'Authorization': f'Bearer  {self.__access_token}'
        }

        json_data = {
            "reference": "Testing transaction",
            "subscriber": {
                'X-Country': 'MG',
                'X-Currency': 'MGA',
                "msisdn": phone_number
            },
            "transaction": {
                "amount": valuer,
                "country": "MG",
                "currency": "MGA",
                "id": transaction_id
            }
        }

        response = requests.post('https://openapiuat.airtel.africa/merchant/v1/payments/', headers=headers,
                                 json=json_data)

        return response.json()

    def transaction_enquiry(self, id_transaction) -> dict:
        headers = {
            'Accept': '*/*',
            'X-Country': 'MG',
            'X-Currency': 'MGA',
            'Authorization': f'Bearer  {self.__access_token}'
        }

        response = requests.get(f'https://openapiuat.airtel.africa/standard/v1/payments/{id_transaction}',
                                headers=headers)

        return response.json()

    def get_balance_enquery(self) -> dict:
        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'X-Country': 'MG',
            'X-Currency': 'MGA',
            'Authorization': f'Bearer  {self.__access_token}'
        }

        response = requests.get('https://openapiuat.airtel.africa/standard/v1/users/balance', headers=headers)

        return response.json()

    def callback(self, domaine_name: str):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(domaine_name, headers=headers)

        return response.json()


if __name__ == "__main__":
    client = AirtelApi()

    r_payement = client.payments(TECH_ZARA, 1000)
    transaction_id = r_payement["data"]["transaction"]["id"]

    print(r_payement)

    print(client.transaction_enquiry(transaction_id))
