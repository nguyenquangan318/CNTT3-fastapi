from fastapi import Depends, status, HTTPException, Request, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from services.classrooms import delete_class_service, get_all_classes_service, create_class_service, update_class_service
from schemas.classrooms import CreateClassroom, UpdateClassroom

router = APIRouter(prefix='/classrooms',tags=['classrooms'])
        
@router.get('/')
def get_all_classes(db: Session = Depends(get_db)):
    list_classes = get_all_classes_service(db)
    return{
        "message": "Success!",
        "data": list_classes
    }
    
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_class(new_class: CreateClassroom , db: Session = Depends(get_db)):
    classroom = create_class_service(db, new_class)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@router.put('/{id}')
def update_class(id: int, update_class: UpdateClassroom, db: Session = Depends(get_db)):
    classroom = update_class_service(db, id, update_class)
    return {
        "message": "Success!",
        "data": classroom   
    }
    
@router.delete('/{id}')
def delete_class(request: Request, id:int, db: Session = Depends(get_db)):
    classroom = delete_class_service(db, id)
    if classroom is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Lớp muốn xóa không tồn tại"
        )
    return {
        "message": "Success!",
        "data": classroom
    }