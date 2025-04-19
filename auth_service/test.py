import requests

BASE_URL = "http://localhost:5007/auth"

def login(username, password):
    print(f"\n🔐 Logging in as {username}")
    response = requests.post(f"{BASE_URL}/login", json={
        "username": username,
        "password": password
    })
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json().get("token", None)

def get_me(token):
    print("\n👤 Testing /me")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/me", headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def admin_only(token):
    print("\n🛡️  Testing /admin-only")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def invalid_login():
    print("\n🚫 Testing invalid login")
    response = requests.post(f"{BASE_URL}/login", json={
        "username": "admin",
        "password": "wrongpass"
    })
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    token = login("admin", "admin123")
    if token:
        get_me(token)
        admin_only(token)
    invalid_login()

