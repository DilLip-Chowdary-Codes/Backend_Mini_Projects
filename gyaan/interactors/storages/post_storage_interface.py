from abc import ABC, abstractmethod

class PostStorageInterface(ABC):

    @abstractmethod
    def get_valid_post_ids(self, post_ids):
        pass

    @abstractmethod
    def get_posts(self, post_ids):
        pass

    @abstractmethod
    def get_comment_ids(self, post_ids, limit):
        pass

    @abstractmethod
    def get_comments(self, comment_ids):
        pass

    @abstractmethod
    def get_post_tags(self, post_ids):
        pass

    @abstractmethod
    def get_comments_count(self, post_ids):
        pass

    @abstractmethod
    def get_replies_count(self, comment_ids):
        pass

    @abstractmethod
    def get_posts_reactions_count(self, post_ids):
        pass

    @abstractmethod
    def get_comments_reactions_count(self, comment_ids):
        pass

    @abstractmethod
    def get_users(self, user_ids):
        pass
