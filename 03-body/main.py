from fastapi import FastAPI, Query, Depends
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

courses = [
    {'id': 1, 'name': 'Programming Basics', 'credits': 6},
    {'id': 2, 'name': 'Object Oriented Programming', 'credits': 6},
    {'id': 3, 'name': 'Version control systems', 'credits': 3},
]


def common_params(fields: Optional[List[str]] = Query(None, description='Include only these fields.'), credits: Optional[int] = None):
    return {'fields': fields, 'credits': credits}


class Course(BaseModel):
    id: Optional[int] = None
    name: str
    credits: int


@app.post('/courses')
def create_course(course: Course):
    return {'course': course}


@app.get('/courses')
def get_courses(commons: dict = Depends(common_params)):
    cs = courses

    if commons['credits']:
        cs = []
        for c in courses:
            if c['credits'] == commons['credits']:
                cs.append(c)

    if commons['fields']:
        cs2 = []
        for course in cs:
            c = {f: course[f] for f in course if f in commons['fields']}
            cs2.append(c)
        cs = cs2

    return {'courses': cs}


# /courses/1?fields=name&fields=credits
@app.get('/courses/{course_id}')
def get_course(course_id: int, commons: dict = Depends(common_params)):
    try:
        course = courses[course_id - 1]
        if commons['fields']:
            course = {f: course[f] for f in course if f in commons['fields']}
        return {'course': course}
    except:
        return {'error': 'course not found'}
