from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from .. import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()

    return blogs


def create(request, db: Session, user_id: int):
    new_blog = models.Blog(
        title=request.title,
        description=request.description,
        published=request.published,
        user_id=user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id,response,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': f'Blog with {id} is not available'}

    return blog



def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(f'Blog with {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return {'success': True}



def update(id, request, db: Session):
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