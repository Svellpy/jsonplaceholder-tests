import pytest
from src.clients.user_client import UsersClient
from src.entities.user import User, Address, Geo, Company

class TestUserStructure:

    @pytest.fixture
    def users_client(self):
        return UsersClient()
    
    def test_user_is_dataclass(self, users_client):
        user = users_client.get_user(1)

        assert isinstance(user, User)

    def test_user_has_all_fields(self, users_client):
        user = users_client.get_user(1)
        
        expected_fields = ['id', 'name', 'username', 'email', 
                        'address', 'phone', 'website', 'company']
        
        for field in expected_fields:
            assert hasattr(user, field), f"User missing field: {field}"

    def test_address_is_dataclass(self, users_client):
        user = users_client.get_user(1)

        assert isinstance(user.address, Address)

    def test_geo_is_dataclass(self, users_client):
        user = users_client.get_user(1)

        assert isinstance(user.address.geo, Geo)

    def test_company_is_dataclass(self, users_client):
        user = users_client.get_user(1)

        assert isinstance(user.company, Company)

    def test_email_format(self, users_client):
        user = users_client.get_user(1)
        
        assert "@" in user.email
        assert "." in user.email.split("@")[1]