import pytest
import json
from pathlib import Path
from src.clients.posts_client import PostsClient
from http import HTTPStatus
from http import HTTPMethod



class TestGetPosts:
    
    @pytest.fixture
    def posts_client(self):
        return PostsClient()
    
    def test_get_all_posts(self, posts_client):
        posts = posts_client.get_all_posts()

        assert len(posts) == 100
        assert all (post.id > 0 for post in posts)

    def test_get_post_by_id(self, posts_client):
        post = posts_client.get_post(1)

        json_path = Path(__file__).parent.parent / "config_data" / "expected_responses" / "post_1.json"
        with open(json_path, 'r', encoding='utf-8') as f:
            expected_data = json.load(f)


        assert post.id == expected_data["id"]
        assert post.userId == expected_data["userId"]
        assert post.title == expected_data["title"]
        assert post.body == expected_data["body"]

    def test_get_nonexistent_post(self, posts_client):
        with pytest.raises(Exception):
            posts_client.get_post(999)