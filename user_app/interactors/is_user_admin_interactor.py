from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.interactors.presenters.user_presenter_interface\
    import UserPresenterInterface
from user_app.exceptions import InvalidUserId

class IsUserAdminInteractor:
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def is_user_admin_wrapper(self, user_id: int,
                              presenter: UserPresenterInterface
                             ):
        try:
            is_admin = self.is_user_admin(user_id)
        except InvalidUserId:
            presenter.raise_invalid_user_id_exception()

        return presenter.is_admin_response(is_admin)

    def is_user_admin(self, user_id: int):
        user_dto = self.storage.get_user_dto(user_id)
        is_user_id_invalid = not user_dto

        if is_user_id_invalid:
            raise InvalidUserId()

        is_user_admin = user_dto.is_admin
        return is_user_admin
