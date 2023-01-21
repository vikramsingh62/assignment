import jsonpath
import pytest

from APIs.send import Send


class TestGetBalance(Send):

    # Testing by sending money to valid user
    def test_send_money(self):
        # To verify the status code on sending money
        assert self.send_money().status_code == 200

        # to get the new and old balance to compare if correct amount is added to the account
        old_balance = jsonpath.jsonpath((self.get_user_balance().json(), 'balance'))
        new_balance = jsonpath.jsonpath(self.send_money().json(), 'new_balance')

        # asserting if the new updated balance is correct or not
        assert old_balance + self.money == new_balance

    # Testing when user is trying to send money to an account which doesn't exist
    def test_send_money_to_invalid_account(self):
        # verify the status code when user not found
        assert self.send_money_to_invalid_account().status_code == 404

    # Testing when user id trying to send money with insufficient balance
    def test_send_money_when_having_insufficient_balance(self):
        # verify the status code for insufficient balance
        assert self.send_money_exceeding_current_balance().status_code == 422
