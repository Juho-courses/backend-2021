from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .common import get_db
from typing import List

from ..database import crud_student, crud_teacher


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


def get_user(db, username):
    # tarkistetaan ensin löytyykö opiskelijaa
    user = crud_student.get_student_by_username(db, username)
    if user is None:
        # ei löytynyt opiskelijaa, löytyiskö opettaja
        user = crud_teacher.get_teacher_by_username(db, username)
    return user


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_user(db, token)
    if not user:
        raise HTTPException(
            status_code=401,
            details='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return user


def is_own_data(user, student_id):
    # opiskelija saa hakea vain omat tietonsa
    if user.role == 'student' and user.id is not student_id:
        raise HTTPException(
            status_code=403, detail='Operation not permitted')


class RoleChecker:
    def __init__(self, allowed_roles: List):
        # print('rolechecker init')
        self.allowed_roles = allowed_roles

    def __call__(self, user=Depends(get_current_user)):
        # print(f"user.role {user.role}")
        # print(f"allowed roles {''.join(self.allowed_roles)}")
        if user.role not in self.allowed_roles:
            # print(f"user with role {user.role} not in {self.allowed_roles}")
            raise HTTPException(
                status_code=403, detail='Operation not permitted')


allow_student = RoleChecker(['student'])
allow_teacher = RoleChecker(['teacher'])
allow_both = RoleChecker(['student', 'teacher'])
