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
        from_attributes = True
        # orm_mode = True 

class ShowBlog(BaseModel):
    title: str
    description: str 
    creator: Optional[ShowUser]

    class Config:
        # orm_mode = True
     from_attributes = True



class Login(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None



ShowBlog.model_rebuild()
ShowUser.model_rebuild()