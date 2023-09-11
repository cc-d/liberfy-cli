import requests
from requests import Response, HTTPError
from typing import Optional, Union, List, Dict, Any, Tuple, Set
from config import BASE_URL
from .token import load_token, save_token


def _check_response_errors(response: Response) -> None:
    """Check if the response has an HTTP error and raise appropriate exception."""
    try:
        response.raise_for_status()
    except HTTPError:
        if response.status_code == 400:
            raise HTTPError(
                f"400 Bad Request: {response.text}", response=response
            )
        elif response.status_code == 404:
            raise HTTPError(
                f"404 Not Found: {response.text}", response=response
            )
        elif response.status_code == 500:
            raise HTTPError(
                f"500 Internal Server Error: {response.text}", response=response
            )
        raise


def _inject_auth(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    token = load_token()
    if token:
        headers = kwargs.get('headers', {})
        headers.update({'Authorization': f"Bearer {token}"})
        kwargs['headers'] = headers
    return kwargs


def get(url: str, *args, **kwargs) -> Response:
    kwargs = _inject_auth(kwargs)
    response = requests.get(f"{BASE_URL}/{url}", *args, **kwargs)
    _check_response_errors(response)
    return response


def post(url: str, *args, **kwargs) -> Response:
    kwargs = _inject_auth(kwargs)
    response = requests.post(f"{BASE_URL}/{url}", *args, **kwargs)
    _check_response_errors(response)
    return response


def put(url: str, *args, **kwargs) -> Response:
    kwargs = _inject_auth(kwargs)
    response = requests.put(f"{BASE_URL}/{url}", *args, **kwargs)
    _check_response_errors(response)
    return response


def delete(url: str, *args, **kwargs) -> Response:
    kwargs = _inject_auth(kwargs)
    response = requests.delete(f"{BASE_URL}/{url}", *args, **kwargs)
    _check_response_errors(response)
    return response


def patch(url: str, *args, **kwargs) -> Response:
    kwargs = _inject_auth(kwargs)
    response = requests.patch(f"{BASE_URL}/{url}", *args, **kwargs)
    _check_response_errors(response)
    return response
