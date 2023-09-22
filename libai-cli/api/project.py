from typing import List

from httpx import Response
from logfunc import logf
from schemas import ProjectOut

from .utils import authhttpx


@logf()
async def create(name: str) -> Response:
    return await authhttpx.post("/p/new", json={"name": name})


@logf()
async def all() -> List[ProjectOut]:
    return await authhttpx.get("/p/all")


@logf()
async def get(project_id: str) -> Response:
    return await authhttpx.get(f"/p/{project_id}")
