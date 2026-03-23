from pydantic import BaseModel
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
