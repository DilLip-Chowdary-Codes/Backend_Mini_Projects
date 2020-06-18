import pytest
from freezegun import freeze_time
from datetime import datetime

from gyaan.interactors.storages.dtos\
    import DomainDTO,\
           DomainStatsDTO,\
           UserDetailsDTO,\
           PostDTO,\
           CommentDTO,\
           Tag,\
           PostTag,\
           PostTagDetails,\
           PostReactionsCount,\
           CommentReactionsCount,\
           PostCommentsCount,\
           CommentRepliesCount,\
           CompletePostDetails

from gyaan.interactors.dtos import DomainDetailsDTO

@pytest.fixture
def domain_dto():
    domain_dto = DomainDTO(domain_id=1,
                           name="Domain_1",
                           description="Some_Text"
                          )
    return domain_dto

@pytest.fixture
def domain_stats():
    domain_stats = DomainStatsDTO(domain_id=1,
                                  followers_count=100,
                                  posts_count=1000,
                                  bookmarked_count=123
                                 )
    return domain_stats

@pytest.fixture
def user_dtos():
    user_dtos = [
        UserDetailsDTO(user_id=user_id,
                       name=f"name_{user_id}",
                       profile_pic_url="https://www.google.com/")
        for user_id in range(2)
        ]
    return user_dtos

@pytest.fixture
def domain_details_dto(domain_dto, domain_stats, user_dtos):
    domain_experts = user_dtos
    domain_details_dto = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=domain_experts,
            is_user_domain_expert=False
            )

    return domain_details_dto

@pytest.fixture
def domain_details_response(domain_details_dto):
    domain_dto = domain_details_dto.domain
    domain_stats = domain_details_dto.domain_stats
    domain_experts = domain_details_dto.domain_experts
    is_user_domain_expert = domain_details_dto.is_user_domain_expert

    domain_stats_details = {
        "followers_count":domain_stats.followers_count,
        "posts_count":domain_stats.posts_count,
        "bookmarked_count":domain_stats.bookmarked_count
    }

    domain_experts_details = [
        {
            "user_id":domain_expert.user_id,
            "name":domain_expert.name,
            "profile_pic_url":domain_expert.profile_pic_url
        }
        for domain_expert in domain_experts
        ]

    domain_details_response = {
        "domain_id":domain_dto.domain_id,
        "name":domain_dto.name,
        "description":domain_dto.description,
        "domain_stats":domain_stats_details,
        "domain_experts":domain_experts_details,
        "is_user_domain_expert":is_user_domain_expert
    }

    return domain_details_response

@pytest.fixture
def post_dtos():

    with freeze_time("2020-06-18 09:38:20.000000"):
        post_dtos = [
            PostDTO(
                post_id=post_id,
                posted_at=datetime.now(),
                posted_by_id=user_id,
                title="Post",
                content="Dummy"
                )
            for post_id, user_id in zip(range(1,3), range(1,3))
            ]
    return post_dtos

@pytest.fixture
def comment_dtos():
    with freeze_time("2020-06-18 09:38:20.000000"):
        comment_dtos = [
            CommentDTO(
                comment_id=comment_id,
                post_id=post_id,
                commented_at=datetime.now(),
                commented_by_id=1,
                content="Dummy"
                )
            for comment_id, post_id in zip(range(1,3), range(1,3))
            ]
    return comment_dtos

@pytest.fixture
def tag_dtos():
    tag_dtos = [
        Tag(
            tag_id=1,
            name=f"Tag_{tag_id}"
            )
        for tag_id in range(2)
        ]
    return tag_dtos
 
@pytest.fixture
def post_tag_id_dtos():
    post_tag_id_dtos = [
        PostTag(
            post_id=post_id,
            tag_id=tag_id
            )
        for post_id,tag_id in zip(range(2), range(2))
        ]
    return post_tag_id_dtos

@pytest.fixture
def posts_tag_details(tag_dtos, post_tag_id_dtos):
    posts_tag_details = PostTagDetails(
        tags=tag_dtos,
        post_tag_ids=post_tag_id_dtos)
    return posts_tag_details

@pytest.fixture
def post_reaction_counts():
    post_reaction_counts = [
        PostReactionsCount(
            post_id=post_id,
            reactions_count=post_id + 2 # random
            )
        for post_id in range(2)
        ]
    return post_reaction_counts


@pytest.fixture
def comment_reaction_counts():
    comment_reaction_counts = [
        CommentReactionsCount(
            comment_id=comment_id,
            reactions_count=comment_id + 2 # random
            )
        for comment_id in range(2)
        ]
    return comment_reaction_counts

@pytest.fixture
def posts_comment_counts():
    post_comments_count = [
        PostCommentsCount(
            post_id=post_id,
            comments_count=post_id + 2 # random
            )
        for post_id in range(2)
        ]
    return post_comments_count

@pytest.fixture
def comment_replies_counts():
    comment_replies_counts = [
        CommentRepliesCount(
            comment_id=comment_id,
            replies_count=5 # random
            )
        for comment_id in range(2)
        ]
    return comment_replies_counts

@pytest.fixture
def all_post_details_dto(post_dtos,
                     post_reaction_counts,
                     posts_comment_counts,
                     comment_reaction_counts,
                     comment_replies_counts,
                     comment_dtos,
                     posts_tag_details,
                     user_dtos):

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

@pytest.fixture
def posts_details_response(user_dtos, comment_dtos):

    user_details = [
        {
            "user_id":user_dto.user_id,
             "name":user_dto.name,
             "profile_pic_url":user_dto.profile_pic_url
        }
        for user_dto in user_dtos
        ]
        
    comments_details = [
        {
            "comment_id":comment_dto.comment_id,
            "commented_by":user_details[0],
            "content":comment_dto.content,
            "replies_count":5,
            "reactions_count":5
        }
        for comment_dto in comment_dtos
        ]

    posts_details_response = {
     "total_posts":2,
     "posts":[
         {
             "post_id":post_id,
             "posted_by":user_details[0],
             "comments": comments_details,
             "reactions_count":5
         }
         for post_id, user_id in (range(1,3), range(1,3))
         ]
    }
    return posts_details_response
