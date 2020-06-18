from abc import ABC, abstractmethod

class PostPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_post_ids_exception(self, invalid_post_ids):
        pass
    
    @abstractmethod
    def get_posts_details(self, posts_details_dtos):
        pass
