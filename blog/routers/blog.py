from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,models,database
from ..repository import blog


router = APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)



@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request,db)



# Get single blog
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(database.get_db)):
    return blog.show(id,response,db)




@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id, db: Session = Depends(database.get_db)):
    return blog.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id,request,db)