from unittest.mock import create_autospec
import pytest

from project_management_portal.interactors.user_logout_interactor\
    import UserLogoutInteractor
from project_management_portal.interactors.storages.user_storage_interface\
    import UserStorageInterface
from project_management_portal.interactors\
    .presenters.user_presenter_interface\
    import UserPresenterInterface
from project_management_portal.exceptions import InvalidToken

class TestLogout:

    def test_logout_with_valid_token(self):

        #arrange
        access_token = "kjfewrfjbwg"
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        interactor = UserLogoutInteractor(storage=storage)
        storage.validate_access_token.return_value = True
        presenter.logout_response.return_value = None
        expected_response = None

        #act
        response = interactor.logout_wrapper(access_token=access_token,
                                             presenter=presenter
                                            )

        #assert
        storage.validate_access_token.assert_called_once_with(
            access_token=access_token
            )
        assert response == expected_response

    def test_logout_with_invalid_token(self):

        #arrange
        access_token = "some_random"
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        interactor = UserLogoutInteractor(storage=storage)
        storage.validate_access_token.return_value = False
        presenter.raise_invalid_access_token_exception\
            .side_effect = InvalidToken

        #act
        with pytest.raises(InvalidToken):
            interactor.logout_wrapper(access_token=access_token,
                                      presenter=presenter
                                     )

        #assert
        storage.validate_access_token.assert_called_once_with(
            access_token=access_token
            )
        presenter.raise_invalid_access_token_exception.assert_called_once()
