from typing import Dict, Optional

from httpx import Response
from logfunc import logf

from .utils import authhttpx


@logf(level='info')
async def create(project_id: str, path: str) -> Response:
    return await authhttpx.post(
        f"/p/{project_id}/s/new", json={"path": path, "project_id": project_id}
    )


@logf()
async def all(project_id: str) -> Response:
    return await authhttpx.get(f"/p/{project_id}/s/all")


@logf()
async def get(project_id: str, syncdir_id: str) -> Response:
    return await authhttpx.get(f"/p/{project_id}/s/{syncdir_id}")
