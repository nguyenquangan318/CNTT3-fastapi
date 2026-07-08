from fastapi import FastAPI, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from classroom_services import delete_class_service, get_all_classes_service, create_class_service, update_class_service
from schemas import CreateClassroom, UpdateClassroom
from fastapi.responses import JSONResponse
from typing import Optional, Any
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any]
    errors: Optional[Any]
    timestamp: str
    path: str

def create_response(req: Request, status_code: int, message: str, data = None, errors = None):
    return BaseResponse(
        status_code = status_code,
        message = message,
        data = data,
        errors = errors,
        timestamp = datetime.now().isoformat(),
        path = req.url.path
    )

@app.get('/test-connection')
def test_connect(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {
            "message": "Success!"
        }
    except Exception as err:
        return {
            "message": str(err)
        }
        
@app.get('/classrooms')
def get_all_classes(db: Session = Depends(get_db)):
    list_classes = get_all_classes_service(db)
    return{
        "message": "Success!",
        "data": list_classes
    }
    
@app.post('/classroom', status_code=status.HTTP_201_CREATED)
def create_class(new_class: CreateClassroom , db: Session = Depends(get_db)):
    classroom = create_class_service(db, new_class)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@app.put('/classroom/{id}')
def update_class(id: int, update_class: UpdateClassroom, db: Session = Depends(get_db)):
    classroom = update_class_service(db, id, update_class)
    return {
        "message": "Success!",
        "data": classroom   
    }
    
@app.delete('/classrom/{id}')
def delete_class(request: Request, id:int, db: Session = Depends(get_db)):
    classroom = delete_class_service(db, id)
    if classroom is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Lớp muốn xóa không tồn tại"
        )
    return create_response(
        request,
        status.HTTP_200_OK,
        "Success!",
        classroom
    )
    
@app.exception_handler(HTTPException)
def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    response = create_response(request, exc.status_code, "Failed!", errors=exc.detail)
    return JSONResponse(
        content = response.model_dump(),
        status_code = exc.status_code
    )
    