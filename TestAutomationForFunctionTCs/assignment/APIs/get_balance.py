import requests

from TestData import APIbase
from Jsons import jsons


class GetBalance:
    # Fetching the urls and API endpoints
    url = APIbase.url
    get_balance = APIbase.get_balance

    # This function will get the balance of valid user and return the response from the API
    def get_user_balance(self):
        response = requests.get((self.url + self.get_balance), json=jsons.valid_user)
        return response

    # This function will get the balance of non-existing user

    def get_user_balance_of_non_existing_user(self):
        response = requests.get((self.url + self.get_balance), json=jsons.invalid_user)
        return response
