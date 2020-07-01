from abc import ABC, abstractmethod
from typing import  Union #Optional, List

class UserStorageInterface(ABC):
    
    @abstractmethod
    def get_user_dto(self, user_id):
        pass
    
    @abstractmethod
    def get_user_dtos(self, user_ids):
        pass
    
    @abstractmethod
    def get_valid_user_ids(self, user_ids):
        pass

    @abstractmethod
    def validate_username(self, username: str) -> Union[bool, int]:
        pass

    @abstractmethod
    def validate_login_credentials(self,
                                   username: str,
                                   password: str
                                  ) -> bool:
        pass

    @abstractmethod
    def validate_access_token(self, access_token: str) -> Union[bool, object]:
        pass

    # @abstractmethod
    # def is_admin(self, user_id: int) -> bool:
    #     pass

    @abstractmethod
    def delete_access_token(self, access_token: str):
        pass
