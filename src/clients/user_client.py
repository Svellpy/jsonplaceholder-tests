from typing import List
from src.constants.urls import ApiUrls, UsersEndpoints
from src.clients.base_client import BaseClient
from src.entities.user import User

class UsersClient(BaseClient):

    def __init__(self):
        super().__init__(ApiUrls.BASE_URL)

    def get_all_users(self) -> List[User]:
        response = self.get(UsersEndpoints.GET_ALL)
        response.raise_for_status()
        return [User.from_dict(item) for item in response.json()]
    
    def get_user(self, user_id: int) -> User:
        endpoint = UsersEndpoints.GET_ONE.format(user_id=user_id)
        response = self.get_endpoint
        response.raise_for_status()
        return User.from_dict(response.json())