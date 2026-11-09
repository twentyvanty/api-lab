import requests

BASE_URL = "http://127.0.0.1:5000"


def test_duplicate_username():
    username = "user_duplicate"
    password = "password123"

    # Create the first user
    requests.post(
        f"{BASE_URL}/register",
        json={"username": username, "password": password}
    )

    # Try to create the same user again
    response = requests.post(
        f"{BASE_URL}/register",
        json={"username": username, "password": password}
    )

    assert response.status_code == 400
    assert response.json() == {"error": "username already taken"}


def test_wrong_password():
    username = "user_wrong_password"
    password = "password123"

    # Create a new user
    requests.post(
        f"{BASE_URL}/register",
        json={"username": username, "password": password}
    )

    # Login with the wrong password
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": username, "password": "wrongpassword"}
    )

    assert response.status_code == 401
    assert response.json() == {"error": "authentication failed"}


def test_empty_username():
    response = requests.post(
        f"{BASE_URL}/register",
        json={"username": "", "password": "password123"}
    )

    assert response.status_code == 400
    assert response.json() == {"error": "username field is empty"}