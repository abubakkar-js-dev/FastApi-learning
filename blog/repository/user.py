from fastapi import status,HTTPException,Response
from sqlalchemy.orm import Session
from .. import models
from ..utils.password import Hash


def create(request, db: Session):

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



def get_all(db: Session):
    users = db.query(models.User).all()

    return users



def show(id, password, response: Response, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': f'User with {id} is not available'}

    compaired_pass = Hash.verify_password(password, user.password)

    if not compaired_pass:
       raise HTTPException(401,{'message': 'Invalid credential'})

    return user