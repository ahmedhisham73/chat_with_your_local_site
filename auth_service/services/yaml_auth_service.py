import yaml
import os
from interfaces.authenticator import Authenticator
from interfaces.role_provider import RoleProvider
from typing import List

class YAMLAuthService(Authenticator, RoleProvider):
    def __init__(self, yaml_path=None):
        if yaml_path is None:
            yaml_path = os.path.join(os.path.dirname(__file__), "..", "users.yaml")

        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
            self.users = {user["username"]: user for user in data["users"]}

    def authenticate(self, username: str, password: str) -> bool:
        user = self.users.get(username)
        if user and user["password"] == password:
            return True
        raise Exception("Invalid username or password")

    def get_roles(self, username: str) -> List[str]:
        user = self.users.get(username)
        return user["roles"] if user else []


