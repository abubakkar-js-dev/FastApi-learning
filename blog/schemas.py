from pydantic import BaseModel, Field
from typing import Optional, List



class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool] = False


class User(BaseModel): 
    name: str
    email: str
    password: str = Field(..., min_length=6, max_length=72)



class ShowUser(BaseModel): 
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True 

class ShowBlog(BaseModel):
    title: str
    description: str 
    creator: ShowUser

    class Config:
        orm_mode = True


ShowBlog.model_rebuild()
ShowUser.model_rebuild()