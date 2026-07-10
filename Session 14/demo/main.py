from fastapi import FastAPI
from routers.classrooms import router as classrooms_router

app = FastAPI()

@app.get('/')
def start():
    return{
        "message": "Welcome"
    }

app.include_router(classrooms_router)