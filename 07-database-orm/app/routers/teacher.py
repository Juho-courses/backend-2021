from typing import List
from fastapi import APIRouter, Depends, status

from ..schemas import schemas

from ..database import crud_teacher
from ..utils.common import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/teacher',
    tags=['teacher']
)


@router.post('/', response_model=schemas.Teacher, status_code=status.HTTP_201_CREATED)
def create_teacher(t: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud_teacher.create_teacher(db, t)


@router.get('/', response_model=List[schemas.Teacher])
def read_teachers(db: Session = Depends(get_db)):
    return crud_teacher.get_teachers(db)


@router.get('/{teacher_id}', response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return crud_teacher.get_teacher(db, teacher_id)


@router.get('/{teacher_id}/courses')
def get_courses(teacher_id: int, db: Session = Depends(get_db)):
    return crud_teacher.get_courses(db, teacher_id)
