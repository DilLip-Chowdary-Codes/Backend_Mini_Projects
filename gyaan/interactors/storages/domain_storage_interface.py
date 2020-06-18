from abc import ABC, abstractmethod

class DomainStorageInterface(ABC):

    @abstractmethod
    def get_domain(self, domain_id):
        pass

    @abstractmethod
    def is_user_following_domain(self, user_id, domain_id):
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id):
        pass

    @abstractmethod
    def get_users_details(self, user_ids):
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id):
        pass
    
    @abstractmethod
    def is_user_domain_expert(self, user_id, domain_id):
        pass
    
    @abstractmethod
    def validate_domain_id(self, domain_id):
        pass

    @abstractmethod
    def get_domain_post_ids(self, domain_id):
        pass
