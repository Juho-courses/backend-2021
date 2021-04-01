from typing import List
from fastapi import APIRouter, Depends, status

from ..schemas import schemas
from ..utils.common import get_db

from ..database import crud_course

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/courses',
    tags=['courses']
)


@router.post('/', response_model=schemas.Course, status_code=status.HTTP_201_CREATED)
def create_course(c: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud_course.create_course(db, c)


@router.get('/{course_id}/students')
def get_students(course_id: int, db: Session = Depends(get_db)):
    return {'students': crud_course.get_students(db, course_id)}


@router.post('/{course_id}/enroll/{student_id}')
def enroll_to_course(course_id: int, student_id: int, db: Session = Depends(get_db)):
    c = crud_course.add_student_to_course(db, course_id, student_id)
    return {'message': 'enroll ok'}


@router.get('/', response_model=List[schemas.Course])
def get_courses(db: Session = Depends(get_db)):
    return crud_course.get_courses(db)


@router.get('/{course_id}', response_model=schemas.Course)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return crud_course.get_course(db, course_id)
