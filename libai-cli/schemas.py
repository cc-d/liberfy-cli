from typing import List, Union, Optional
from dataclasses import dataclass
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class TokenLogin(BaseModel):
    username: str
    password: str
    grant_type: str = 'password'
    scope: str = ''
    client_id: str = ''
    client_secret: str = ''


class UserBase(BaseModel):
    email: str


class UserNew(UserBase):
    password: str


class UserOut(UserBase):
    id: str


class UserDB(UserOut):
    hpassword: str
    projects: List['ProjectDB']


class UserOutToken(UserOut):
    token: Token


class ProjectBase(BaseModel):
    pass


class ProjectNew(ProjectBase):
    name: str


class ProjectOut(ProjectNew):
    id: str
    user_id: str


class ProjectDB(ProjectOut):
    user: UserDB
    syncdirs: List['SyncDirDB']


class SyncDirBase(BaseModel):
    path: str


class SyncDirCreate(SyncDirBase):
    project_id: str


class DirFileBase(BaseModel):
    relpath: str
    content: Optional[str]


class DirFileCreate(DirFileBase):
    syncdir_id: str
    checksum: str


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
    checksum_type: str = 'md5'
