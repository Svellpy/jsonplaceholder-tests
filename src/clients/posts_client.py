from typing import List
from src.constants.urls import ApiUrls, PostsEndpoints
from src.clients.base_client import BaseClient
from src.entities.post import Post

class PostsClient(BaseClient):

    def __init__(self):
        super().__init__(ApiUrls.BASE_URL)

    def get_all_posts(self) -> List[Post]:
        response = self.get(PostsEndpoints.GET_ALL)
        response.raise_for_status()
        return [Post.from_dict(item) for item in response.json()]
    
    def get_post(self, post_id: int) -> Post:
        endpoint = PostsEndpoints.GET_ONE.format(post_id=post_id)
        response = self.get(endpoint)
        response.raise_for_status()
        return Post.from_dict(response.json())
    
    def create_post(self, user_id: int, title: str, body: str) -> Post:
        data = {
            "userId": user_id,
            "title": title,
            "body": body
        }
        response = self.post(PostsEndpoints.CREATE, data=data)
        response.raise_for_status()
        return Post.from_dict(response.json())
    
    def update_post(self, post_id: int, user_id: int, title: str, body: str) -> Post:
        data = {
            "id": post_id,
            "userId": user_id,
            "title": title,
            "body": body
        }
        endpoint = PostsEndpoints.UPDATE.format(post_id=post_id)
        response = self.put(endpoint, data=data)
        response.raise_for_status()
        return Post.from_dict(response.json())
    
    def delete_post(self, post_id: int) -> int:
        endpoint = PostsEndpoints.DELETE.format(post_id=post_id)
        response = self.delete(endpoint)
        return response.status_code
    
