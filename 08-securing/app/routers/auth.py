from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..utils.auth import get_db, get_user
from ..utils.common import fake_hash_password

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user(db, form_data.username)

    if not user:
        raise HTTPException(
            status_code=400, detail='Incorrect username or password')

    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=403, detail='Incorrect username or password')

    return {'access_token': user.username, 'token_type': 'bearer'}
