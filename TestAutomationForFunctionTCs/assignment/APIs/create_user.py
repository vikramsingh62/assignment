import requests

from Jsons import jsons
from TestData import APIbase


class CreateUser:
    # Fetching the urls and API endpoints
    url = APIbase.url
    create_user = APIbase.create_user
    payload = jsons.new_user

    # This function will create new users and return the response from the API
    def create_new_user(self):
        response = requests.post(self.url + self.create_user, json=self.payload)
        return response
