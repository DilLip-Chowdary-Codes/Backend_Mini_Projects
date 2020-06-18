from abc import ABC, abstractmethod

class DomainPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_domain_id_exception(self):
        pass

    @abstractmethod
    def raise_user_not_domain_member_exception(self):
        pass

    @abstractmethod
    def get_domain_details(self, domain_details_dto):
        pass

    @abstractmethod
    def get_domain_with_posts(self, domain_post_details_dto):
        pass
