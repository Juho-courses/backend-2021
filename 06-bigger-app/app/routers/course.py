from fastapi import APIRouter, status, Depends, Form, Response

from ..schemas.course import CourseIn, CourseOut2

from ..database import crud

from ..utils.common import common_params

router = APIRouter(
    prefix='/courses',
    tags=['courses']
)


@router.post('/', response_model=CourseOut2, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseIn):
    return {'course': crud.save_course(course)}


@router.post('/form', response_model=CourseOut2, status_code=status.HTTP_201_CREATED)
def create_course_form(name: str = Form(...), credits: int = Form(...)):
    return {'course': crud.save_course(CourseIn(name=name, credits=credits))}


@router.get('/')
def get_courses(commons: dict = Depends(common_params)):
    cs = crud.courses

    if commons['credits']:
        cs = []
        for c in crud.courses:
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
@router.get('/{course_id}')
def get_course(course_id: int, response: Response, commons: dict = Depends(common_params)):
    try:
        course = crud.courses[course_id - 1]
        if commons['fields']:
            course = {f: course[f] for f in course if f in commons['fields']}
        return {'course': course}
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': 'course not found'}
