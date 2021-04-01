from fastapi import APIRouter, Depends, status
from typing import List

from ..schemas import schemas

from ..database import crud_student

from ..utils.common import get_db

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/student',
    tags=['student']
)


@router.post('/', response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
def create_student(s: schemas.StudenCreate, db: Session = Depends(get_db)):
    return crud_student.create_student(db, s)


@router.post('/{student_id}/grade/{course_id}')
def add_grade(student_id: int, course_id: int, grade: schemas.Grade, db: Session = Depends(get_db)):
    crud_student.add_grade(db, student_id, course_id, grade.grade)
    return {'message': 'grade added'}


@router.get('/{student_id}/grade')
def get_grades(student_id: int, db: Session = Depends(get_db)):
    return crud_student.get_grades(db, student_id)


@router.get('/', response_model=List[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud_student.get_students(db)


@router.get('/{student_id}', response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud_student.get_student(db, student_id)
