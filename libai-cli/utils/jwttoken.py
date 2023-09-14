import config
import os

from logfunc import logf
from typing import Optional


@logf()
async def write(token: str) -> None:
    with open(config.JWT_TOKEN_PATH, 'w+') as file:
        file.write(token)


@logf()
async def read() -> Optional[str]:
    if os.path.exists(config.JWT_TOKEN_PATH):
        with open(config.JWT_TOKEN_PATH, 'r') as file:
            return file.read().strip()


@logf()
async def remove() -> bool:
    if os.path.exists(config.JWT_TOKEN_PATH):
        os.remove(config.JWT_TOKEN_PATH)
        return True
    return False
