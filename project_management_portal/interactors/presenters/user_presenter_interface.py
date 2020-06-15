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
