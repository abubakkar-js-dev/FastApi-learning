from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,models,database
from ..utils.password import Hash
from  ..repository import user as user_repo

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user_repo.create(request, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all(db: Session = Depends(database.get_db)):
    return user_repo.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id, password, response: Response, db: Session = Depends(database.get_db)):
    return user_repo.show(id,password,response,db)
 