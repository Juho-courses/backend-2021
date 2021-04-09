from app.utils.common import fake_hash_password
from sqlalchemy.orm import Session

from . import models
from ..schemas import schemas


def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()


def get_teacher_by_username(db: Session, username: str):
    return db.query(models.Teacher).filter(models.Teacher.username == username).first()


def get_teachers(db: Session):
    return db.query(models.Teacher).all()


def get_courses(db: Session, teacher_id: int):
    t = db.query(models.Teacher).filter(
        models.Teacher.id == teacher_id).first()
    return [c.name for c in t.courses]


def create_teacher(db: Session, teacherIn: schemas.TeacherCreate):
    db_t = models.Teacher(name=teacherIn.name, username=teacherIn.username,
                          hashed_password=fake_hash_password(teacherIn.password))
    db.add(db_t)
    db.commit()
    db.refresh(db_t)
    print('asdasda ' + str(db_t.id))
    return db_t
