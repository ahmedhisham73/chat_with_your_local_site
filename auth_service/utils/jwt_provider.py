import jwt
import datetime
from typing import List

class JWTProvider:
    def __init__(self, secret: str):
        self.secret = secret

    def generate_token(self, username: str, roles: List[str]) -> str:
        payload = {
            "sub": username,
            "roles": roles,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, self.secret, algorithm="HS256")
        return token if isinstance(token, str) else token.decode("utf-8")



