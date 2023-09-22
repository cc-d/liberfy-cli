from typing import Dict, Optional

import utils.jwttoken as tokenutils
from httpx import Response
from logfunc import logf
from schemas import Token, UserOut, UserOutToken

from .utils import authhttpx


@logf(level='info', logargs=False)
async def tokenlogin(email: str, password: str) -> Token:
    tok = Token(
        **await authhttpx.post(
            "/u/tokenlogin", json={"username": email, "password": password}
        )
    )
    await tokenutils.write(tok.access_token)
    return tok


@logf(level='info')
async def create(email: str, password: str) -> UserOutToken:
    resp = await authhttpx.post(
        "/u/new", json={"username": email, "password": password}
    )
    utoken = UserOutToken(**resp)
    await tokenutils.write(utoken.token.access_token)
    return utoken


@logf()
async def me() -> UserOut:
    return UserOut(**await authhttpx.get("/u/me"))
