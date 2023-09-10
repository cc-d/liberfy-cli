# utils.py

import os

TOKEN_PATH = os.path.join(os.path.expanduser("~"), ".token")


def save_token(token: str) -> None:
    with open(TOKEN_PATH, 'w+') as file:
        file.write(token)


def load_token() -> str:
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as file:
            return file.read().strip()
    return ""
