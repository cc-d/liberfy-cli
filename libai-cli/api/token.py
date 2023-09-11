# utils.py

import os

from logfunc import logf
from typing import Optional
from config import TOKEN_PATH, BASE_URL


@logf()
def save_token(token: str) -> None:
    with open(TOKEN_PATH, 'w+') as file:
        file.write(token)


@logf()
def load_token() -> Optional[str]:
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as file:
            return file.read().strip()