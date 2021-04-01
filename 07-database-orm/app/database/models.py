from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from .database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    courses = relationship('Course', back_populates='teacher')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    credits = Column(Integer)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='courses')

    students = relationship(
        'Student', secondary='student_course_linker', back_populates='courses')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    courses = relationship(
        'Course', secondary='student_course_linker', back_populates='students')

    grades = relationship('StudentGrades')


class StudentCourseLink(Base):
    __tablename__ = 'student_course_linker'

    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)


class StudentGrades(Base):
    __tablename__ = 'students_grades'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    grade = Column(Integer, nullable=False)

    student = relationship('Student', back_populates='grades')
    course = relationship('Course')
