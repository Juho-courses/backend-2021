from fastapi import APIRouter, Depends, status
from typing import List

from ..schemas import schemas

from ..database import crud_student

from ..utils.common import get_db

from sqlalchemy.orm import Session

from ..utils.auth import allow_teacher, allow_both, get_current_user, is_own_data

router = APIRouter(
    prefix='/student',
    tags=['student']
)


@router.post('/', response_model=schemas.Student, status_code=status.HTTP_201_CREATED, dependencies=[Depends(allow_teacher)])
def create_student(s: schemas.StudenCreate, db: Session = Depends(get_db)):
    return crud_student.create_student(db, s)


@router.post('/{student_id}/grade/{course_id}', dependencies=[Depends(allow_teacher)])
def add_grade(student_id: int, course_id: int, grade: schemas.Grade, db: Session = Depends(get_db)):
    crud_student.add_grade(db, student_id, course_id, grade.grade)
    return {'message': 'grade added'}


@router.get('/{student_id}/grade', dependencies=[Depends(allow_both)])
def get_grades(student_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # opiskelija saa hakea vain omat tietonsa
    is_own_data(user, student_id)
    return crud_student.get_grades(db, student_id)


@router.get('/', response_model=List[schemas.Student], dependencies=[Depends(allow_teacher)])
def read_students(db: Session = Depends(get_db)):
    return crud_student.get_students(db)


@router.get('/{student_id}', response_model=schemas.Student, dependencies=[Depends(allow_teacher)])
def read_student(student_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # opiskelija saa hakea vain omat tietonsa
    is_own_data(user, student_id)
    return crud_student.get_student(db, student_id)
