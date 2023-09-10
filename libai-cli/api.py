# api.py

import requests

from config import BASE_URL


def login_user(email: str, password: str) -> requests.Response:
    return requests.post(
        f"{BASE_URL}/user/tokenlogin",
        json={"username": email, "password": password},
    )


def register_user(email: str, password: str) -> requests.Response:
    return requests.post(
        f"{BASE_URL}/user/create", json={"email": email, "password": password}
    )
