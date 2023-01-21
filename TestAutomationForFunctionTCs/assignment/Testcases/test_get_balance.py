import pytest

from APIs.get_balance import GetBalance


class TestGetBalance(GetBalance):

    # Test case to get the current balance of the user
    def test_get_balance(self):
        # To verify the status code on getting balance from user
        assert self.get_user_balance().status_code == 200

    # testing to get the balance of a non-existing user

    def test_get_balance_of_non_existing_user(self):
        # To verify the status code on getting balance from non-existing user
        assert self.get_user_balance_of_non_existing_user().status_code == 404
