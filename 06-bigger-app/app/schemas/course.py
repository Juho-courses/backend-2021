from pydantic import BaseModel


class CourseIn(BaseModel):
    name: str
    credits: int


class CourseOut(BaseModel):
    id: int
    name: str
    credits: int


class CourseOut2(BaseModel):
    course: CourseOut
