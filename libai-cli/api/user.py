from api import authhttpx
from api.authhttpx import BASE_URL
import httpx
from logfunc import logf
from .token import save_token, load_token, delete_token
from httpx import Response
from typing import Optional, Dict
from schemas import UserOutToken, UserOut, Token
from api.authhttpx import resp_exceptions


@logf()
async def tokenlogin(email: str, password: str) -> Token:
    tok = Token(
        **await authhttpx.post(
            "/u/tokenlogin", json={"username": email, "password": password}
        )
    )
    await save_token(tok.access_token)
    return tok


@logf()
async def create(email: str, password: str) -> UserOutToken:
    resp = await authhttpx.post(
        "/u/new", json={"email": email, "password": password}
    )
    utoken = UserOutToken(**resp)
    await save_token(utoken.token.access_token)
    return utoken


@logf()
async def me() -> UserOut:
    return UserOut(**await authhttpx.get("/u/me"))
