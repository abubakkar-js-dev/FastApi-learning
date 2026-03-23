from pydantic import BaseModel
from typing import Optional


class BlogResponse(BaseModel):
    title: str
    description: str
    published: Optional[bool] = False
