from typing import List
from models.user import User

class AuthService:
    def __init__(self, authenticator, role_provider, jwt_provider):
        self.authenticator = authenticator
        self.role_provider = role_provider
        self.jwt_provider = jwt_provider

    def login(self, username: str, password: str) -> str:
        if self.authenticator.authenticate(username, password):
            roles: List[str] = self.role_provider.get_roles(username)
            user = User(username, roles)
            return self.jwt_provider.generate_token(user.username, user.roles)
        raise Exception("Authentication Failed")

