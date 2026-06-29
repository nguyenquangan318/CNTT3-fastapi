# import
from fastapi import FastAPI

# Tạo thực thể
app = FastAPI()

# Viết API
@app.get('/')
def get_root():
    return { "message": "Hello world"}

@app.get('/student/id')
def get_root():
    return { 
        "id": 1,
        "name": "Nguyễn Văn A"
    }