from api import authhttpx
import httpx
from httpx import Response
from typing import Optional, Dict


async def create_syncdir(project_id: str, path: str) -> Response:
    return await authhttpx.post(
        f"/p/{project_id}/s/new", json={"path": path, "project_id": project_id}
    )


async def get_all_syncdirs(project_id: str) -> Response:
    return await authhttpx.get(f"/p/{project_id}/s/all")


async def get_syncdir(project_id: str, syncdir_id: str) -> Response:
    return await authhttpx.get(f"/p/{project_id}/s/{syncdir_id}")
