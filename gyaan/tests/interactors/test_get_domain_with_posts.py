import pytest
from unittest.mock import Mock, create_autospec
from gyaan.interactors.get_domain_with_posts import GetDomainWithPosts
from gyaan.interactors.storages.domain_storage_interface\
    import DomainStorageInterface
from gyaan.interactors.storages.post_storage_interface\
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface\
    import PostPresenterInterface
from gyaan.interactors.presenters.domain_presenter_interface\
    import DomainPresenterInterface
from gyaan.exceptions \
    import UserNotFollowingDomain, InvalidPostIdsException, InvalidDomainId
from django_swagger_utils.drf_server.exceptions import BadRequest

class TestGetDomainWithPosts:

    def test_get_domain_posts_with_invalid_domain_id_raises_exception(self):
        #arrange
        user_id = 1
        domain_id = 1
        limit = 10
        offset = 0
        post_storage = create_autospec(PostStorageInterface)
        domain_storage = create_autospec(DomainStorageInterface)
        post_presenter = create_autospec(PostPresenterInterface)
        domain_presenter = create_autospec(DomainPresenterInterface)
        interactor = GetDomainWithPosts(domain_storage, post_storage)
        domain_storage.get_domain.side_effect = InvalidDomainId
        domain_presenter.raise_invalid_domain_id_exception\
            .side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.get_domain_with_posts_wrapper(user_id, domain_id,
                                                limit, offset,
                                                domain_presenter,
                                                post_presenter)
        #assert
        domain_storage.get_domain.assert_called_once_with(domain_id)
        domain_presenter.raise_invalid_domain_id_exception\
            .assert_called_once()

    def test_get_domain_posts_with_user_who_is_not_follower_raises_exception(
        self, domain_dto):
        #arrange
        user_id = 1
        domain_id = 1
        limit = 10
        offset = 0
        domain_storage = create_autospec(DomainStorageInterface)
        post_storage = create_autospec(PostStorageInterface)
        domain_presenter = create_autospec(DomainPresenterInterface)
        post_presenter = create_autospec(PostPresenterInterface)
        interactor = GetDomainWithPosts(domain_storage, post_storage)
        domain_storage.get_domain.return_value = domain_dto
        domain_storage.is_user_following_domain.return_value = False
        domain_presenter.raise_user_not_domain_member_exception\
            .side_effect = BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.get_domain_with_posts_wrapper(user_id,
                                                domain_id,
                                                limit,
                                                offset,
                                                domain_presenter,
                                                post_presenter,)
        #assert
        domain_storage.get_domain.assert_called_once_with(domain_id)
        domain_storage.is_user_following_domain.assert_called_once_with(
            user_id, domain_id)
        domain_presenter.raise_user_not_domain_member_exception\
            .assert_called_once()

    def test_get_domain_posts_with_invalid_post_ids_raises_exception(self):
        #arrange
        user_id = 1
        domain_id = 1
        limit = 10
        offset = 0 
        post_ids = [1, 2, 3, 4, 5]
        valid_post_ids = [1, 2, 3]
        invalid_post_ids = [4, 5]
        post_storage = create_autospec(PostStorageInterface)
        domain_storage = create_autospec(DomainStorageInterface)
        domain_presenter = create_autospec(DomainPresenterInterface)
        post_presenter = create_autospec(PostPresenterInterface)
        interactor = GetDomainWithPosts(domain_storage, post_storage)
        post_storage.get_valid_post_ids.return_value = valid_post_ids
        post_presenter.raise_invalid_post_ids_exception.side_effect = \
            BadRequest

        #act
        with pytest.raises(BadRequest):
            interactor.get_domain_with_posts_wrapper(user_id, domain_id,
                                                limit, offset,
                                                domain_presenter,
                                                post_presenter)

        #assert
        post_storage.get_valid_post_ids.assert_called_once_with(post_ids)
        post_presenter.raise_invalid_post_ids_exception\
            .assert_called_once_with(invalid_post_ids)

    def test_get_domain_with_posts_with_valid_values(self,
                                                post_dtos,
                                                user_dtos,
                                                comment_dtos,
                                                posts_tag_details,
                                                post_reaction_counts,
                                                all_post_details_dto,
                                                posts_comment_counts,
                                                posts_details_response,
                                                comment_replies_counts,
                                                comment_reaction_counts
                                                ):
        #arrange
        user_id = 1
        domain_id = 1
        limit = 10
        offset = 0 
        post_ids = [1, 2, 3]
        valid_post_ids = [1, 2, 3]
        comment_ids = [1, 2]
        user_ids = [1, 2]
        post_storage = create_autospec(PostStorageInterface)
        domain_storage = create_autospec(DomainStorageInterface)
        domain_presenter = create_autospec(DomainPresenterInterface)
        post_presenter = create_autospec(PostPresenterInterface)
        interactor = GetDomainWithPosts(domain_storage, post_storage)
        post_storage.get_valid_post_ids.return_value = valid_post_ids
        post_storage.get_posts.return_value = post_dtos
        post_storage.get_posts_reactions_count.return_value = \
            post_reaction_counts
        post_storage.get_post_tags.return_value = posts_tag_details
        post_storage.get_comment_ids.return_value = comment_ids
        post_storage.get_comments.return_value = comment_dtos
        post_storage.get_comments_reactions_count.return_value = \
            comment_reaction_counts
        post_storage.get_comments_count.return_value = posts_comment_counts
        post_storage.get_replies_count.return_value = comment_replies_counts
        post_storage.get_users.return_value = user_dtos
        domain_storage.get_domain_post_ids.return_value = post_ids
        domain_presenter.get_domain_with_posts.return_value = \
            posts_details_response
        expected_response = posts_details_response

        #act
        response = interactor.get_domain_with_posts_wrapper(user_id,
                                                            domain_id,
                                                            limit, offset,
                                                            domain_presenter,
                                                            post_presenter)

        #assert
        print(response)
        print(posts_details_response)
        assert response == posts_details_response
        post_storage.get_valid_post_ids.assert_called_once_with(post_ids)
        post_storage.get_posts.assert_called_once_with(post_ids)
        post_storage.get_comment_ids.assert_called_once_with(post_ids,
                                                             limit=2)
        post_storage.get_comments.assert_called_once_with(comment_ids)
        post_storage.get_post_tags.assert_called_once_with(post_ids)
        post_storage.get_comments_count.assert_called_once_with(post_ids)
        post_storage.get_replies_count.assert_called_once_with(comment_ids)
        post_storage.get_posts_reactions_count.assert_called_once_with(
            post_ids)
        post_storage.get_comments_reactions_count.assert_called_once_with(
            comment_ids)
        post_storage.get_users.assert_called_once_with(user_ids)
        domain_presenter.get_domain_with_posts.assert_called_once_with(
            all_post_details_dto)
        assert response == expected_response
