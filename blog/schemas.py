from pydantic import BaseModel, Field
from typing import Optional


class BlogResponse(BaseModel):
    title: str
    description: str
    published: Optional[bool] = False


class ShowBlog(BaseModel):
    title: str
    description: str

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str = Field(..., min_length=6, max_length=72)


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True
