# utils.py

import os

from logfunc import logf
from typing import Optional
from config import Paths

TOKEN_PATH = Paths.TOKEN_PATH


@logf()
async def save_token(token: str) -> None:
    with open(TOKEN_PATH, 'w+') as file:
        file.write(token)


@logf()
async def load_token() -> Optional[str]:
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as file:
            return file.read().strip()


@logf()
async def delete_token() -> bool:
    if os.path.exists(TOKEN_PATH):
        os.remove(TOKEN_PATH)
        return True
    return False
