import pytest
from oauth2_provider.models import AccessToken
from user_app.tests.storages.outputs import\
    test
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation

@pytest.mark.django_db
class TestUserStorage:

    def test_get_user_dto(self, users):

        #arrange
        from .expected_responses import user_dto
        user_id = 1
        storage = UserStorageImplementation()

        #act
        response = storage.get_user_dto(user_id)

        #assert
        assert response == user_dto

    def test_validate_username_valid(self, users):

        #arrange
        user = users[0]
        username = user.username
        storage = UserStorageImplementation()
        expected_response = user.user_id

        #act
        response = storage.validate_username(username=username)

        #assert
        assert response == expected_response

    def test_validate_username_invalid(self, users):

        #arrange
        username = "some random"
        storage = UserStorageImplementation()
        expected_response = False

        #act
        response= storage.validate_username(username=username)

        #assert
        assert response == expected_response

    def test_validate_login_credentials_valid(self, users):

        #arrange
        user = users[0]
        username = user.username
        password = "admin@123"
        storage = UserStorageImplementation()
        expected_response = True

        #act
        response = storage.validate_login_credentials(
            username=username,
            password=password
            )

        #assert
        assert response == expected_response

    def test_validate_login_credentials_password_invalid(self, users):

        #arrange
        user = users[0]
        username = user.username
        password = "some random"
        storage = UserStorageImplementation()
        expected_response = False

        #act

        response = storage.validate_login_credentials(
            username=username,
            password=password
            )

        #assert
        assert response == expected_response

    def test_validate_access_token(self, access_tokens):

        #arrange
        token = access_tokens[0]
        storage = UserStorageImplementation()
        access_token = "test_access_token"
        expected_response = token

        #act
        response = storage.validate_access_token(access_token)

        #assert
        assert response == expected_response

    def test_validate_access_token_with_invalid_token(self, access_tokens):

        #arrange
        storage = UserStorageImplementation()
        access_token = "test_dummy_token"
        expected_response = None

        #act
        response = storage.validate_access_token(access_token)

        #assert
        assert response == expected_response

    def test_is_admin(self, users):

        #arrange
        storage = UserStorageImplementation()
        user_id = 1
        expected_response = True

        #act
        response = storage.is_admin(user_id)

        #assert
        assert response == expected_response

    def test_is_admin_with_normal_user(self, users):

        #arrange
        storage = UserStorageImplementation()
        user_id = 2
        expected_response = False

        #act
        response = storage.is_admin(user_id)

        #assert
        assert response == expected_response

    def test_delete_access_token(self, access_tokens):

        #arrange
        from oauth2_provider.models import AccessToken
        storage = UserStorageImplementation()
        access_token = "test_access_token"

        #act
        storage.delete_access_token(access_token)

        #assert
        expected_is_token_exists = False
        is_token_exists = AccessToken.objects.filter(
            token=access_token).exists()
        assert is_token_exists == expected_is_token_exists
