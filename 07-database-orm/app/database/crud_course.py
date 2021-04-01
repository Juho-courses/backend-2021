from sqlalchemy.orm import Session

from . import models
from ..schemas import schemas


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(models.Course).all()


def get_students(db: Session, course_id: int):
    c = db.query(models.Course).filter(models.Course.id == course_id).first()

    return [s.name for s in c.students]


def create_course(db: Session, courseIn: schemas.CourseCreate):
    c = models.Course(credits=courseIn.credits,
                      name=courseIn.name, teacher_id=courseIn.teacher_id)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c


def add_student_to_course(db: Session, course_id: int, student_id: int):
    c = db.query(models.Course).filter(models.Course.id == course_id).first()
    s = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    c.students.append(s)

    db.add(c)
    db.commit()
    db.refresh(c)
    return c
