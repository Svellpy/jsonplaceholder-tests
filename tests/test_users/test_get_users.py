import pytest
from src.clients.user_client import UsersClient

class TestGetUsers:

    @pytest.fixture
    def users_client(self):
        return UsersClient()
    
    def test_get_all_users(self, users_client):
        users = users_client.get_all_users()

        assert len(users) == 10
        assert all(user.id > 0 for user in users)
        assert all(user.name for user in users)
        assert all(user.email for user in users)

    def test_get_user_by_id(self, users_client):
        user = users_client.get_user(1)

        assert user.id == 1
        assert user.name == "Leanne Graham"
        assert user.username == "Bret"
        assert user.email == "Sincere@april.biz"
        assert user.address is not None
        assert user.address.city == "Gwenborough"
        assert user.company is not None
        assert user.company.name == "Romaguera-Crona"

    def test_get_user_with_complete_address(self, users_client):
        user = users_client.get_user(1)

        assert hasattr(user.address, 'street')
        assert hasattr(user.address, 'suite')
        assert hasattr(user.address, 'city')
        assert hasattr(user.address, 'zipcode')
        assert hasattr(user.address, 'geo')
        
        
        assert hasattr(user.address.geo, 'lat')
        assert hasattr(user.address.geo, 'lng')

    def test_user_with_complete_conpany(self, users_client):
        user = users_client.get_user(1)

        assert hasattr(user.company, 'name')
        assert hasattr(user.company, 'catchPhrase')
        assert hasattr(user.company, 'bs')

    def test_get_nonexistent_user(self, users_client):
        with pytest.raises(Exception):
            users_client.get_user(999)

    @pytest.mark.parametrize("user_id,expected_name", [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch"),
        (4, "Patricia Lebsack"),
        (5, "Chelsey Dietrich"),
    ])

    def test_multiple_users_have_correct_names(self, users_client, user_id, expected_name):
        user = users_client.get_user(user_id)
        
        assert user.name == expected_name