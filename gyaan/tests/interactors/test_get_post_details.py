import pytest
from unittest.mock import Mock, create_autospec

from django_swagger_utils.drf_server.exceptions import BadRequest

from gyaan.interactors.presenters.post_presenter_interface\
    import PostPresenterInterface
from gyaan.interactors.storages.post_storage_interface\
    import PostStorageInterface
from gyaan.interactors.get_posts_details import GetPostsDetailsInteractor

class TestGetPostDetails:
    def test_get_post_details_with_invalid_post_ids_raises_exception(self):
        #arrange
        post_ids = [1, 2, 3, 4, 5]
        valid_post_ids = [1, 2, 3]
        invalid_post_ids = [4, 5]
        storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PostPresenterInterface)
        interactor = GetPostsDetailsInteractor(storage)
        storage.get_valid_post_ids.return_value = valid_post_ids
        presenter.raise_invalid_post_ids_exception.side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.get_posts_details_wrapper(post_ids, presenter)

        #assert
        storage.get_valid_post_ids.assert_called_once_with(post_ids)
        presenter.raise_invalid_post_ids_exception.assert_called_once_with(
            invalid_post_ids)
    
    def test_get_post_details_with_valid_values(self,
                                                post_dtos,
                                                comment_dtos,
                                                posts_tag_details,
                                                post_reaction_counts,
                                                comment_reaction_counts,
                                                posts_comment_counts,
                                                comment_replies_counts,
                                                user_dtos,
                                                posts_details_response,
                                                all_post_details_dto):
        #arrange
        post_ids = [1, 2, 3]
        valid_post_ids = [1, 2, 3]
        comment_ids = [1, 2]
        user_ids = [1, 2]
        storage = create_autospec(PostStorageInterface)
        presenter = create_autospec(PostPresenterInterface)
        interactor = GetPostsDetailsInteractor(storage)
        storage.get_valid_post_ids.return_value = valid_post_ids
        storage.get_posts.return_value = post_dtos
        storage.get_posts_reactions_count.return_value = post_reaction_counts
        storage.get_post_tags.return_value = posts_tag_details
        storage.get_comment_ids.return_value = comment_ids
        storage.get_comments.return_value = comment_dtos
        storage.get_comments_reactions_count.return_value = comment_reaction_counts
        storage.get_comments_count.return_value = posts_comment_counts
        storage.get_replies_count.return_value = comment_replies_counts
        storage.get_users.return_value = user_dtos
        presenter.get_posts_details.return_value = posts_details_response
        expected_response = posts_details_response

        #act
        response = interactor.get_posts_details_wrapper(post_ids, presenter)

        #assert
        assert response == posts_details_response
        storage.get_valid_post_ids.assert_called_once_with(post_ids)
        storage.get_posts.assert_called_once_with(post_ids)
        storage.get_comment_ids.assert_called_once_with(post_ids, limit=2)
        storage.get_comments.assert_called_once_with(comment_ids)
        storage.get_post_tags.assert_called_once_with(post_ids)
        storage.get_comments_count.assert_called_once_with(post_ids)
        storage.get_replies_count.assert_called_once_with(comment_ids)
        storage.get_posts_reactions_count.assert_called_once_with(post_ids)
        storage.get_comments_reactions_count.assert_called_once_with(
            comment_ids)
        storage.get_users.assert_called_once_with(user_ids)
        presenter.get_posts_details.assert_called_once_with(
            all_post_details_dto)
        assert response == expected_response
