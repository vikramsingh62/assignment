import requests

from APIs.get_balance import GetBalance
from Jsons import jsons
from TestData import APIbase


class Send(GetBalance):
    # Fetching the urls and API endpoints
    url = APIbase.url
    money = APIbase.send_money

    # This function will send money and return the response from the API
    def send_money(self):
        response = requests.post((self.url + self.money), data=jsons.send_valid_user)
        return response

    # This function will send money to an invalid account and return the response from the API
    def send_money_to_invalid_account(self):
        response = requests.post((self.url + self.send_money()), data=jsons.send_to_invalid_user)
        return response

    # This function will send the amount exceeding its balance and return the response from the API
    def send_money_exceeding_current_balance(self):
        response = requests.post((self.url + self.send_money()), data=jsons.send_exceeding_current_balance)
        return response
