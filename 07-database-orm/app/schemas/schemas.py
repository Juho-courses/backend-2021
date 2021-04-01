from pydantic import BaseModel
from typing import List, Optional


class CourseBase(BaseModel):
    credits: int
    name: str
    teacher_id: int

    class Config:
        orm_mode = True


class CourseCreate(CourseBase):
    pass


class TeacherBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class TeacherNoCourses(TeacherBase):
    id: int


class Course(CourseBase):
    id: int
    teacher: TeacherNoCourses


class CourseNoTeacher(BaseModel):
    id: int
    credits: int
    name: str

    class Config:
        orm_mode = True


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    id: int
    courses: Optional[List[CourseNoTeacher]] = []


class StudentBase(BaseModel):
    name: str


class StudenCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    courses: Optional[List[Course]] = []

    class Config:
        orm_mode = True


class Grade(BaseModel):
    grade: int
