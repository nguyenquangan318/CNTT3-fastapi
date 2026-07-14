from fastapi import FastAPI
from routers.classrooms import router as classrooms_router
from database import Base, engine
from models.teachers import TeacherModel
from models.students import StudentModel
from models.subjects import SubjectModel

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def start():
    return{
        "message": "Welcome"
    }

app.include_router(classrooms_router)