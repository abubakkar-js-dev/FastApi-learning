from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,models,database


router = APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(
        title=request.title,
        description=request.description,
        published=request.published,
        user_id = 1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



# Get single blog
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': f'Blog with {id} is not available'}

    return blog




@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(f'Blog with {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return {'success': True}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
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