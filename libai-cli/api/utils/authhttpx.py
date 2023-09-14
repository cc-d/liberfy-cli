import httpx

from logfunc import logf
from httpx import Response, HTTPError
from typing import Optional, Dict, Any

import utils.jwttoken as tokenutils
from config import BASE_URL


@logf()
async def _raise_excepts(resp: Response) -> None:
    """Check if the response has an HTTP error and raise appropriate exception."""
    try:
        resp.raise_for_status()
    except HTTPError:
        if resp.status_code == 400:
            raise HTTPError(f"400 Bad Request: {resp.text}")
        elif resp.status_code == 401:
            if resp.url.path == '/u/me':
                await tokenutils.remove()
            raise HTTPError(f"401 Unauthorized: {resp.text}")
        elif resp.status_code == 404:
            raise HTTPError(f"404 Not Found: {resp.text}")
        elif resp.status_code == 500:
            raise HTTPError(f"500 Internal Server Error: {resp.text}")
        raise


@logf()
async def _inject_auth(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    token = await tokenutils.read()
    if token:
        headers = kwargs.get('headers', {})
        headers.update({'Authorization': f"Bearer {token}"})
        kwargs['headers'] = headers
    return kwargs


@logf()
async def _method(method: str, url: str, **kwargs) -> Dict[str, Any]:
    url = '%s%s' % (BASE_URL, url) if not url.startswith('http') else url
    method = str(method).lower()
    if method != 'options':
        kwargs = await _inject_auth(kwargs)
    reqdata = kwargs.get('data', None)
    reqdata = reqdata if reqdata is not None else kwargs.get('json', None)
    kwargs = {k: v for k, v in kwargs.items() if k not in ['data', 'json']}

    async with httpx.AsyncClient() as client:
        usemethod = getattr(client, method)

        if method != 'options' and reqdata is not None:
            resp = await usemethod(
                url, data=reqdata, headers=kwargs.get('headers', {})
            )
        elif method == 'options':
            resp = await usemethod(url)
        else:
            resp = await usemethod(url, headers=kwargs.get('headers', {}))

    await _raise_excepts(resp)
    return resp.json()


@logf()
async def get(url: str, *args, **kwargs) -> Response:
    return await _method('get', url, *args, **kwargs)


@logf()
async def post(url: str, *args, **kwargs) -> Response:
    return await _method('post', url, *args, **kwargs)


@logf()
async def put(url: str, *args, **kwargs) -> Response:
    return await _method('put', url, *args, **kwargs)


@logf()
async def delete(url: str, *args, **kwargs) -> Response:
    return await _method('delete', url, *args, **kwargs)


@logf()
async def options(url: str, *args, **kwargs) -> Response:
    return await _method('options', url, *args, **kwargs)


@logf()
async def patch(url: str, *args, **kwargs) -> Response:
    return await _method('patch', url, *args, **kwargs)


@logf()
async def head(url: str, *args, **kwargs) -> Response:
    return await _method('head', url, *args, **kwargs)
