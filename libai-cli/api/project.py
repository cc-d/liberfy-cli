from api import authrequests
import requests
from requests import Response
from typing import Optional, Dict


def create_project(name: str) -> Response:
    return authrequests.post("/p/new", json={"name": name})


def get_all_projects() -> Response:
    return authrequests.get("/p/all")


def get_project(project_id: str) -> Response:
    return authrequests.get(f"/p/{project_id}")
