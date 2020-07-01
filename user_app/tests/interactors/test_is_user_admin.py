from unittest.mock import create_autospec, patch

import pytest

from user_app.interactors.is_user_admin_interactor\
    import IsUserAdminInteractor
from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.interactors\
    .presenters.user_presenter_interface\
    import UserPresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound

class TestIsUserAdminInteractor:

    def test_is_user_admin_with_invalid_user_id(self):
        #arrange
        user_id = 1
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        interactor = IsUserAdminInteractor(storage=storage)
        storage.get_user_dtos.return_value = None
        presenter.raise_invalid_user_id_exception.side_effect = NotFound

        #act
        with pytest.raises(NotFound):
            interactor.is_user_admin_wrapper(
                user_id=user_id, presenter=presenter)

        #assert
        presenter.raise_invalid_user_id_exception.assert_called_once()

    def test_is_user_admin_with_valid_user_id_and_user_is_not_admin(
            self,
            user_dto):

        #arrange
        user_id = 1
        is_admin_response = {"is_admin": False}
        expected_is_admin = is_admin_response
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        interactor = IsUserAdminInteractor(storage=storage)
        storage.get_user_dtos.return_value = user_dto
        presenter.is_admin_response.return_value = is_admin_response

        #act
        response = interactor.is_user_admin_wrapper(user_id=user_id,
                                                    presenter=presenter
                                                   )

        #assert
        assert response == expected_is_admin
        storage.get_user_dtos.assert_called_once_with(user_id=user_id)
        presenter.is_admin_response.assert_called_once_with(
            is_admin=user_dto.is_admin)

    def test_is_user_admin_with_valid_user_id_and_user_is_admin(
        self,
        user_admin_dto):

        #arrange
        user_id = 1
        is_admin_response = {"is_admin": True}
        expected_is_admin = is_admin_response
        storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UserPresenterInterface)
        interactor = IsUserAdminInteractor(storage=storage)
        storage.get_user_dtos.return_value = user_admin_dto
        presenter.is_admin_response.return_value = is_admin_response

        #act
        response = interactor.is_user_admin_wrapper(user_id=user_id,
                                                    presenter=presenter
                                                   )

        #assert
        assert response == expected_is_admin
        storage.get_user_dtos.assert_called_once_with(user_id=user_id)
        presenter.is_admin_response.assert_called_once_with(
            is_admin=user_admin_dto.is_admin)
