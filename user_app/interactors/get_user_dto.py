from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.interactors.presenters.user_presenter_interface\
    import UserPresenterInterface
from user_app.exceptions import InvalidUserId

class GetUserDtoInteractor:
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def get_user_dto_wrapper(self, user_id: int,
                             presenter: UserPresenterInterface
                            ):
        try:
            user_dto = self.get_user_dto(user_id)
        except InvalidUserId:
            presenter.raise_invalid_user_id_exception()

        return presenter.get_user_dtos_response(user_dto)

    def get_user_dto(self, user_id: int):

        user_dto = self.storage.get_user_dto(user_id)
        is_user_invalid = not user_dto

        if is_user_invalid:
            raise InvalidUserId()
        return user_dto
