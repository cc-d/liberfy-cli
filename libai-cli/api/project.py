from api import authhttpx
from api.authhttpx import resp_exceptions
import httpx
from httpx import Response
from typing import Optional, Dict, List, Union, Any, Tuple
from logfunc import logf
from schemas import ProjectOut, ProjectNew


@logf()
async def create(name: str) -> Response:
    return await authhttpx.post("/p/new", json={"name": name})


@logf()
async def all() -> List[ProjectOut]:
    return await authhttpx.get("/p/all")


@logf()
async def get(project_id: str) -> Response:
    return await authhttpx.get(f"/p/{project_id}")
