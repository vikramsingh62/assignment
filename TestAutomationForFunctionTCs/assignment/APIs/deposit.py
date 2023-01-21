import requests

from Jsons import jsons
from TestData import APIbase


class DepositAmount:
    # Fetching the urls and API endpoints
    url = APIbase.url
    deposit = APIbase.deposit

    # This function will deposit money into account and return the response from the API
    def deposit_amount(self):
        response = requests.post(self.url + self.deposit, json=jsons.correct_deposit)
        return response

    # This function will deposit money to an invalid account and return the response from the API
    def deposit_money_to_invalid_account(self):

        response = requests.post(self.url + self.deposit, data=jsons.deposit_payload_1)
        return response

    # This function will deposit money exceeding the deposit limit and return the response from the APIt
    def deposit_money_to_exceeding_max_limit(self):
        response = requests.post(self.url + self.deposit, data=jsons.deposit_payload_2)
        return response
