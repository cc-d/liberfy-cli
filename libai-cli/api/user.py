from api import authrequests
from api.authrequests import BASE_URL
import requests
from logfunc import logf
from .token import save_token, load_token
from requests import Response
from typing import Optional, Dict
from schemas import UserOutToken, UserOut, Token


@logf()
def tokenlogin(email: str, password: str) -> UserOut:
    resp = requests.post(
        "%s/u/tokenlogin" % BASE_URL,
        json={"username": email, "password": password},
    )
    print(resp, type(resp), resp.text)
    return Token(**resp.json())


@logf()
def create(email: str, password: str) -> UserOutToken:
    utoken = UserOutToken(
        **requests.post(
            "%s/u/create" % BASE_URL,
            json={"email": email, "password": password},
        ).json()
    )
    save_token(utoken.token.access_token)
    return utoken


@logf()
def me() -> UserOut:
    resp = authrequests.get("%s/u/me" % BASE_URL)
    print(resp, type(resp))
    return UserOut(**resp.json())
