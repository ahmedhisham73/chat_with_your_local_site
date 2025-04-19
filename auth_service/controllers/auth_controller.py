from flask import Blueprint, request, jsonify
import os
import jwt

from __init__ import get_auth_service


from utils.rbac import require_roles                # ✅

auth_bp = Blueprint("auth", __name__)
auth_service = get_auth_service()                   # ✅

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        token = auth_service.login(data["username"], data["password"])
        return jsonify({"token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@auth_bp.route("/me", methods=["GET"])
def me():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Authorization header missing or invalid"}), 401

    token = auth_header.split(" ")[1]
    try:
        decoded = jwt.decode(token, os.getenv("JWT_SECRET", "super_secret_key"), algorithms=["HS256"])
        return jsonify({
            "username": decoded.get("sub"),
            "roles": decoded.get("roles")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@auth_bp.route("/admin-only", methods=["GET"])
@require_roles(["admin"])
def admin_only():
    return jsonify({"message": "Welcome, Admin!"})



