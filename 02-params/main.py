from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

courses = [
    {'id': 1, 'name': 'Programming Basics', 'credits': 6},
    {'id': 2, 'name': 'Object Oriented Programming', 'credits': 6},
    {'id': 3, 'name': 'Version control systems', 'credits': 3},
]


@app.get('/courses')
def get_courses(credits: Optional[int] = None):
    cs = courses

    if credits:
        cs = []
        for c in courses:
            if c['credits'] == credits:
                cs.append(c)

    return {'courses': cs}


# /courses/1?fields=name&fields=credits
@app.get('/courses/{course_id}')
def get_course(course_id: int, fields: Optional[List[str]] = Query(None, description='Include only these fields.')):
    try:
        course = courses[course_id - 1]
        if fields:
            course = {f: course[f] for f in course if f in fields}
        return {'course': course}
    except:
        return {'error': 'course not found'}
