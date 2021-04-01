from sqlalchemy.orm import Session

from . import models
from ..schemas import schemas


def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()


def get_teachers(db: Session):
    return db.query(models.Teacher).all()


def get_courses(db: Session, teacher_id: int):
    t = db.query(models.Teacher).filter(
        models.Teacher.id == teacher_id).first()
    return [c.name for c in t.courses]


def create_teacher(db: Session, teacherIn: schemas.TeacherCreate):
    db_t = models.Teacher(name=teacherIn.name)
    db.add(db_t)
    db.commit()
    db.refresh(db_t)
    return db_t
