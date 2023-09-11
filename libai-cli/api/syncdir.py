from api import authrequests
import requests
from requests import Response
from typing import Optional, Dict


def create_syncdir(project_id: str, path: str) -> Response:
    return authrequests.post(
        f"/p/{project_id}/s/new", json={"path": path, "project_id": project_id}
    )


def get_all_syncdirs(project_id: str) -> Response:
    return authrequests.get(f"/p/{project_id}/s/all")


def get_syncdir(project_id: str, syncdir_id: str) -> Response:
    return authrequests.get(f"/p/{project_id}/s/{syncdir_id}")
