from fastapi import FastAPI, Depends, HTTPException, status, Response
from typing import List
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
import uvicorn

from .models import Blog
from .schemas import Blog, ShowBlog, ShowUser
from .utils.password import Hash
from .routers import blog,user,authentication


app = FastAPI()


models.Base.metadata.create_all(bind=engine)
 
 
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




# @app.get('/blogs/{id}', response_model=Blog)
# def get_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.get(Blog, id)
#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with id {id} not found"
#         )
#     return blog

# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=9000)


