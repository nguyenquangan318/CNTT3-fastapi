from fastapi import FastAPI

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

app = FastAPI()

@app.get("/students")
def get_root():
    return {
        "data": students
    }

@app.get("/student/{student_id}")
def get_student(student_id):
    for student in students:
        if int(student_id) == student["id"]:
            return {
                "data": student
            }
    return {
        "message": "Không tìm thấy sinh viên",
        "data": None
    }
    
@app.get("/student")
def get_student(age, name):
    return {
        "data":{
            "age": age,
            "name": name
        }
    }