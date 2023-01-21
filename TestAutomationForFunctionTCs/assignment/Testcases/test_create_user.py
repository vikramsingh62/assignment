import pytest

from APIs.create_user import CreateUser


class TestCreateNewUser(CreateUser):

    # Test case to verify the creation of new user
    def test_create_user(self):
        # To verify the status code on creating a new user
        assert self.create_new_user().status_code == 201
