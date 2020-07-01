from typing import List
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation

from user_app.interactors.is_user_admin_interactor\
    import IsUserAdminInteractor
from user_app.interactors.get_user_dto import GetUserDtoInteractor
from user_app.interactors .get_user_dtos import GetUserDtosInteractor

class UserServiceInterface:

    @staticmethod
    def is_admin(user_id: int):
        storage = UserStorageImplementation()
        interactor = IsUserAdminInteractor(storage=storage)
        is_admin = interactor.is_user_admin(user_id=user_id)
        return is_admin

    @staticmethod
    def get_user_dto(user_id: int):
        storage = UserStorageImplementation()
        interactor = GetUserDtoInteractor(storage=storage)
        user_dto = interactor.get_user_dto(user_id)
        return user_dto

    @staticmethod
    def get_user_dtos(user_ids: List[int]):

        storage = UserStorageImplementation()
        interactor = GetUserDtosInteractor(storage=storage)
        user_dtos = interactor.get_user_dtos(user_ids)
        return user_dtos
