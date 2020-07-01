from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO

class UserPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def raise_invalid_access_token_exception(self):
        pass

    @abstractmethod
    def get_login_response(self,
                           userdto,
                           oauth_token_dto: UserAuthTokensDTO
                          ):
        pass

    @abstractmethod
    def logout_response(self):
        pass

    @abstractmethod
    def raise_invalid_user_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_user_ids_exception(self, invalid_user_ids):
        pass

    @abstractmethod
    def is_admin_response(self, is_admin: bool):
        pass

    @abstractmethod
    def get_user_dto_response(self, user_dto):
        pass

    @abstractmethod
    def get_user_dtos_response(self, user_dtos):
        pass
