from typing import List, Union, Optional
from dataclasses import dataclass


@dataclass
class Token:
    access_token: str
    token_type: str = 'bearer'


class TokenLogin:
    username: str
    password: str
    grant_type: str = 'password'
    scope: str = ''
    client_id: str = ''
    client_secret: str = ''


class UserBase:
    email: str


class UserNew(UserBase):
    password: str


@dataclass
class UserOut(UserBase):
    id: str


class UserDB(UserOut):
    hpassword: str
    projects: List['ProjectDB']


class UserOutToken(UserOut):
    token: Token


class ProjectBase:
    pass


class ProjectNew(ProjectBase):
    name: str


class ProjectOut(ProjectNew):
    id: str
    user_id: str


class ProjectDB(ProjectOut):
    user: 'UserDB'
    syncdirs: List['SyncDirDB']


class SyncDirBase:
    path: str


class SyncDirCreate(SyncDirBase):
    project_id: str


class DirFileBase:
    relpath: str
    content: Optional[str]


class DirFileCreate(DirFileBase):
    syncdir_id: str
    checksum: str
    checksum_type: str = 'md5'


class DirFileOut(DirFileCreate):
    id: str


class SyncDirOut(SyncDirCreate):
    id: str
    dirfiles: List[DirFileOut]
    user_id: str


class SyncDirDB(SyncDirOut):
    project: 'ProjectDB'


class DirFileDB(DirFileOut):
    syncdir: 'SyncDirDB'
