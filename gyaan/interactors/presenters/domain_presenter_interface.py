from abc import ABC, abstractmethod

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_domain_id_exception(self):
        pass
    
    @abstractmethod
    def raise_user_not_domain_member_exception(self):
        pass

    @abstractmethod
    def get_domain_details(self, domain_details_dto):
        pass
