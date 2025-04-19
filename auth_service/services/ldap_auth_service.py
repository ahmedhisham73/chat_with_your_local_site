# services/ldap_auth_service.py

from interfaces.authenticator import Authenticator
from interfaces.role_provider import RoleProvider
from typing import List

class LDAPAuthService(Authenticator, RoleProvider):
    def __init__(self):
        pass  # No LDAP config needed for mock

    def authenticate(self, username: str, password: str) -> bool:
        # ✅ Temporary mocked login
        if username == "admin" and password == "admin":
            return True
        raise Exception("LDAP Authentication failed")

    def get_roles(self, username: str) -> List[str]:
        # ✅ Simulated security groups (RBAC)
        if username == "admin":
            return ["admin", "user"]
        return ["user"]

