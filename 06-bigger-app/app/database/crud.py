from ..schemas.course import CourseIn, CourseOut


courses = [
    {'id': 1, 'name': 'Programming Basics', 'credits': 6},
    {'id': 2, 'name': 'Object Oriented Programming', 'credits': 6},
    {'id': 3, 'name': 'Version control systems', 'credits': 3},
]


def save_course(course: CourseIn):
    next_id = len(courses) + 1
    ret = CourseOut(id=next_id, **course.dict())
    courses.append(ret.dict())
    return ret
