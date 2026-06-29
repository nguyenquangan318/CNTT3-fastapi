# import
from fastapi import FastAPI

# Tạo thực thể
app = FastAPI()

# Viết API
@app.get('/')
def get_root():
    return { "message": "Hello world"}