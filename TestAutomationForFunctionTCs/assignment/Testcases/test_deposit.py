import pytest

from APIs.deposit import DepositAmount


class TestDepositAmount(DepositAmount):

    # Test case to deposit money to valid user account
    def test_deposit(self):
        # To verify the status code on depositing money to valid user
        assert self.deposit_amount().status_code == 200

    # Testing when user is trying to deposit money to an account which doesn't exist
    def test_deposit_money_to_invalid_account(self):
        # verify the status code when user not found
        assert self.deposit_money_to_invalid_account().status_code == 404

    # Testing when user id trying to send money above maximum limit

    def test_deposit_money_exceeding_limit(self):
        # verify the status code for insufficient balance
        assert self.deposit_money_to_exceeding_max_limit().status_code == 422
