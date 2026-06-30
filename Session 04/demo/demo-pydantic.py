from fastapi import FastAPI
from pydantic import BaseModel, Field

students = [
    {
        "id" : 1,
        "name" : "Nguyễn Văn A",
        "age": 18,
        "email": "a@gmail.com"
    },
    {
        "id" : 2,
        "name" : "Nguyễn Thị B",
        "age": 19,
        "email": "b@gmail.com"
    },
    {
        "id" : 3,
        "name" : "Trần Tùng D",
        "age": 20,
        "email": "d@gmail.com"
    }
]

class CreateStudent(BaseModel):
    id:int
    name:str = Field(min_length=1)
    age:int = Field(gt=18, lt=30)

app = FastAPI()

@app.get("/students")
def get_root():
    return {
        "data": students
    }
    
@app.post("/student")
def create_student(student: CreateStudent):
    return {
        "data": student
    }
    
