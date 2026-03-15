import pytest
from src.clients.posts_client import PostsClient
from src.utils.data_generator import random_post_data
from tests.config_data.request_bodies import create_post_data

class TestCreatePost:

    @pytest.fixture
    def posts_client(self):
        return PostsClient()
    
    def test_create_valid_post(self, posts_client):
        test_data = random_post_data(user_id=1)
        created_post = posts_client.create_post(
            user_id=test_data["userId"],
            title=test_data["title"],
            body=test_data["body"]
        )

        assert created_post.id == 101
        assert created_post.title == test_data["title"]
        assert created_post.body == test_data["body"]

    def test_create_post_from_hardcoded_data(self, posts_client):
        data = create_post_data.VALID_POST_DATA
        created_post = posts_client.create_post(
            user_id=data["userId"],
            title=data["title"],
            body=data["body"]
        )

        assert created_post.title == data["title"]
        assert created_post.userId == data["userId"]