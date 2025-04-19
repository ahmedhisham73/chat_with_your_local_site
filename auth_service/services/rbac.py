from functools import wraps
from flask import request, jsonify
import jwt
import os

def require_roles(allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"error": "Missing or invalid token"}), 401

            token = auth_header.split(" ")[1]
            try:
                decoded = jwt.decode(token, os.getenv("JWT_SECRET", "super_secret_key"), algorithms=["HS256"])
                user_roles = decoded.get("roles", [])
                if not any(role in allowed_roles for role in user_roles):
                    return jsonify({"error": "Access denied: insufficient permissions"}), 403
                return f(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401
        return wrapper
    return decorator

