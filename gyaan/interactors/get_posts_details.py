from gyaan.interactors.storages.post_storage_interface\
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface\
    import PostPresenterInterface
from gyaan.exceptions import InvalidPostIdsException
from gyaan.interactors.storages.dtos import CompletePostDetails

class GetPostsDetailsInteractor:

    def __init__(self, storage):
        self.storage = storage

    def get_posts_details_wrapper(self, post_ids, presenter):
        try:
            posts_details_dtos = self.get_posts_details(post_ids)
        except InvalidPostIdsException as error:
            presenter.raise_invalid_post_ids_exception(error.invalid_post_ids)
        else:
            response = presenter.get_posts_details(posts_details_dtos)
        return response

    def get_posts_details(self, post_ids):

        valid_post_ids = self.storage.get_valid_post_ids(post_ids)
        invalid_post_ids = list(set(post_ids) - set(valid_post_ids))

        if invalid_post_ids:
            raise InvalidPostIdsException(invalid_post_ids)

        post_dtos = self.storage.get_posts(post_ids)
        latest_comment_ids = self.storage.get_comment_ids(post_ids, limit=2)
        comment_dtos = self.storage.get_comments(latest_comment_ids)
        posts_tag_details = self.storage.get_post_tags(post_ids=post_ids)
        posts_comment_counts = self.storage.get_comments_count(post_ids)
        comment_replies_counts = self.storage.get_replies_count(
            latest_comment_ids)
        post_reaction_counts = self.storage.get_posts_reactions_count(
            post_ids)
        comment_reaction_counts = self.storage.get_comments_reactions_count(
            latest_comment_ids)
        user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids += [
            comment_dto.commented_by_id\
            for comment_dto in comment_dtos
            ]
        user_ids = list(set(user_ids))
        user_dtos = self.storage.get_users(user_ids)

        all_post_details_dto = CompletePostDetails(
            post_dtos=post_dtos,
            post_reaction_counts=post_reaction_counts,
            comment_counts=posts_comment_counts,
            comment_reaction_counts=comment_reaction_counts,
            reply_counts=comment_replies_counts,
            comment_dtos=comment_dtos,
            post_tag_ids=posts_tag_details.post_tag_ids,
            tags=posts_tag_details.tags,
            users_dtos=user_dtos
        )

        return all_post_details_dto
