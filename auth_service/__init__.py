import os
from services.auth_service import AuthService
from services.yaml_auth_service import YAMLAuthService  # ← التعديل هنا
from utils.jwt_provider import JWTProvider

def get_auth_service():
    yaml_auth = YAMLAuthService()  # ← هنا كمان
    jwt_provider = JWTProvider(secret=os.getenv("JWT_SECRET", "super_secret_key"))
    return AuthService(yaml_auth, yaml_auth, jwt_provider)

