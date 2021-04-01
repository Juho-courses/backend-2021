from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from .routers import teacher, student, course

from .database import models
from .database.database import engine

# luodaan tietokanta
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(course.router)
app.include_router(teacher.router)
app.include_router(student.router)
