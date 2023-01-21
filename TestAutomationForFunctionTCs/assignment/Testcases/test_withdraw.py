import jsonpath
import pytest

from APIs.withdraw import WithdrawAmount


class TestDepositAmount(WithdrawAmount):

    # Testing by withdrawing valid amount
    def test_withdraw(self):
        # To verify the status code on withdrawing amount
        assert self.withdraw_amount().status_code == 200
        old_balance = jsonpath.jsonpath((self.get_user_balance().json(), 'balance'))
        new_balance = jsonpath.jsonpath(self.withdraw_amount().json(), 'new_balance')
        assert old_balance == new_balance + old_balance

    # Testing by withdrawing the amount from the non-existing user
    def test_withdraw_from_non_existing_user(self):
        # verifying the status code for the user not exist
        assert self.withdraw_amount_from_non_existing_user().status_code == 404

    # Testing by withdrawing the amount exceeding the balance
    def test_withdraw_amount_exceeding_the_balance(self):
        # verifying the status code for withdrawing amount exceeding the balance
        assert self.withdraw_amount_exceeding_current_balance().status_code == 422

