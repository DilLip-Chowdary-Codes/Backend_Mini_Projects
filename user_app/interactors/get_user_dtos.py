from typing import List
from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.interactors.presenters.user_presenter_interface\
    import UserPresenterInterface
from user_app.exceptions import InvalidUserIds

class GetUserDtosInteractor:
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def get_user_dtos_wrapper(self, user_ids: List[int],
                              presenter: UserPresenterInterface
                             ):
        try:
            user_dtos = self.get_user_dtos(user_ids)
        except InvalidUserIds:
            presenter.raise_invalid_user_ids_exception(user_ids)

        return presenter.get_user_dtos_response(user_dtos)

    def get_user_dtos(self, user_ids: int):

        valid_user_ids = self.storage.get_valid_user_ids(user_ids)
        invalid_user_ids = list( set(user_ids) - set(valid_user_ids) )

        is_invalid_user_ids_exists = not invalid_user_ids

        if is_invalid_user_ids_exists:
            raise InvalidUserIds(invalid_user_ids)

        user_dtos = self.storage.get_user_dtos(user_ids)

        return user_dtos
