from fastapi import FastAPI, Depends, HTTPException, status, Response
from typing import List
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
import uvicorn

from .models import Blog
from .schemas import BlogResponse, ShowBlog, ShowUser
from .utils.password import Hash


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogResponse, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=request.title,
        description=request.description,
        published=request.published
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs', status_code=200, response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


# Get single blog
@app.get('/blogs/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': f'Blog with {id} is not available'}

    return blog


@app.delete('/blogs/{id}', status_code=status.HTTP_200_OK)
def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(f'Blog with {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return {'success': True}


@app.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: ShowBlog, db: Session = Depends(get_db)):
    updated_blog = {
        'title': request.title,
        'description': request.description,
        'published': request.published,
    }
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(f'Blog with {id} not found')

    blog.update(updated_blog)
    db.commit()

    return {'message': f'Updated blog of id:{id} successfully'}

# @app.get('/blogs/{id}', response_model=BlogResponse)
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


@app.post('/users', response_model=ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):

    hashedPass = Hash.hash_password(request.password)

    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashedPass,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {'message': 'new user is created successfully', 'data': new_user}


@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[ShowUser])
def all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()

    return {'message': 'All users loaded', 'data': users}


@app.get('/users/{id}', status_code=status.HTTP_200_OK)
def show(id, response: Response,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': f'User with {id} is not available'}

    return user
