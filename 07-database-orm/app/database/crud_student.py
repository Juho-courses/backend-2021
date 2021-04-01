from sqlalchemy.orm import Session

from . import models
from ..schemas import schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students(db: Session):
    return db.query(models.Student).all()


def create_student(db: Session, studentIn: schemas.StudenCreate):
    s = models.Student(name=studentIn.name)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s


def add_grade(db: Session, student_id: int, course_id: int, grade: int):
    s = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    c = db.query(models.Course).filter(models.Course.id == course_id).first()
    g = models.StudentGrades(student=s, course=c, grade=grade)

    db.add(g)
    db.commit()
    db.refresh(g)
    return g


def get_grades(db: Session, student_id: int):
    s = db.query(models.Student).filter(
        models.Student.id == student_id).first()

    return [{'course': g.course.name, 'grade': g.grade} for g in s.grades]
