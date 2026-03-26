from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,models,database
from ..utils.password import Hash

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):

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


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()

    return users


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id, password, response: Response, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': f'User with {id} is not available'}

    compaired_pass = Hash.verify_password(password, user.password)

    if not compaired_pass:
       raise HTTPException(401,{'message': 'Invalid credential'})

    return user
 