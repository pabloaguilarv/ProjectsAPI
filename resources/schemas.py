from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    name:str
    company:str

    class Config():
        orm_mode = True


class ShowTeam(BaseModel):
    name:str
    email:str
    role:str

    class Config:
        orm_mode = True

class ShowProject(BaseModel):
    name:str
    company:str
    members:List[ShowTeam] = []

    class Config:
        orm_mode = True


class ShowProjectSimple(BaseModel):
    name:str
    company:str

    class Config:
        orm_mode = True


class ShowTeamMember(BaseModel):
    name:str
    role:str
    project_name: ShowProjectSimple

    class Config():
        orm_mode=True


class TeamMember(BaseModel):
    name:str
    email:str
    password:str
    role:str
    project_name:str


class UpdateMember(BaseModel):
    name:str
    email:str
    role:str
    project_name:str

    class Config():
        orm_mode = True


class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    email:Optional[str] = None