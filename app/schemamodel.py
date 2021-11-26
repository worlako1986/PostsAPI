from pydantic import BaseModel
from typing import (
    Optional,
    List,
    Set
)



class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class UpdatePost(BaseModel):
    title: str
    content: str
    published: bool = True


class User(BaseModel):
    email: str
    full_name: str
    password: str
    age: int

class UpdateUser(BaseModel):
    full_name: str
    age: int

class Login(BaseModel):
    username: str
    password: str