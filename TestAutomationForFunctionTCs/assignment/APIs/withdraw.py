import requests

from APIs.get_balance import GetBalance
from Jsons import jsons
from TestData import APIbase


class WithdrawAmount(GetBalance):
    # Fetching the urls and API endpoints
    url = APIbase.url
    withdraw = APIbase.withdraw

    # This function will withdraw given amount and return the response from the API
    def withdraw_amount(self):
        response = requests.get(self.url + self.withdraw, json=jsons.withdraw_valid_user)
        return response

    # This function will withdraw given amount from a non-existing user and return the response from the API
    def withdraw_amount_from_non_existing_user(self):
        response = requests.get(self.url + self.withdraw, json=jsons.withdraw_invalid_user)
        return response

    # This function will try to withdraw more amount than the balance and return the response
    def withdraw_amount_exceeding_current_balance(self):
        response = requests.get(self.url + self.withdraw, json=jsons.withdraw_exceeding_current_balance)
        return response
