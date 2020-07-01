from unittest.mock import create_autospec, patch

import pytest

from common.oauth2_storage import OAuth2SQLStorage
from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from user_app.interactors.user_login_interactor\
    import UserLoginInteractor
from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.interactors\
    .presenters.user_presenter_interface\
    import UserPresenterInterface
from user_app.exceptions\
    import InvalidUsername,\
           InvalidPassword
from user_app.tests.interactors.expected_responses\
    import valid_login_response

@pytest.mark.django_db
class TestUserLogin:

    def test_user_login_with_invalid_username(self):

        #arrange
        username = "test_username"
        password = "testing123"
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
            )
        storage.validate_username.return_value = False
        presenter.raise_invalid_username_exception\
            .side_effect = InvalidUsername

        #act
        with pytest.raises(InvalidUsername):
            interactor.login_wrapper(username=username, password=password,
                                     presenter=presenter
                                    )

        #assert
        storage.validate_username.assert_called_once_with(username=username)
        presenter.raise_invalid_username_exception.assert_called_once()

    def test_user_login_with_invalid_password(self):

        #arrange
        username = "username"
        password = "password_invalid"
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
            )
        storage.validate_username.return_value = True
        storage.validate_login_credentials.return_value = False
        presenter.raise_invalid_password_exception\
            .side_effect = InvalidPassword

        #act
        with pytest.raises(InvalidPassword):
            interactor.login_wrapper(username=username, password=password,
                             presenter=presenter
                            )

        #assert
        storage.validate_username.assert_called_once_with(username=username)
        storage.validate_login_credentials.assert_called_once_with(
            username=username,
            password=password
            )
        presenter.raise_invalid_password_exception.assert_called_once()

    def test_user_login_with_valid_values(self):

        #arrange
        from .raw_inputs import user_dto
        from .expected_responses import access_token_dto
        username = "username"
        password = "password"
        user_id = 1
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage
            )
        access_token_dto = UserAuthTokensDTO(user_id=1,
                                             access_token="testing_access_token",
                                             refresh_token="testing_refresh_token",
                                             expires_in=10000000)
        storage.validate_username.return_value = user_id
        storage.validate_login_credentials.return_value = True
        storage.get_user_dtos.return_value = user_dto
        presenter.get_login_response.return_value = valid_login_response
        #act
        with patch.object(OAuthUserAuthTokensService,
                          "create_user_auth_tokens",
                          return_value=access_token_dto):

            response = interactor.login_wrapper(
                    username=username,
                    password=password,
                    presenter=presenter
                    )

        #assert
        storage.validate_username.assert_called_once_with(username=username)
        storage.validate_login_credentials.assert_called_once_with(
            username=username,
            password=password
            )
        storage.get_user_dtos.assert_called_once_with(user_id)
        presenter.get_login_response.assert_called_once_with(
            user_dto,
            access_token_dto
            )
        assert response == valid_login_response
