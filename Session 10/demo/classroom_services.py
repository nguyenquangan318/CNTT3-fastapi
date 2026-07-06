from sqlalchemy.orm import Session
from models import ClassModel
from datetime import datetime

def create_class_service(db:Session, class_code: str, name: str, description:str, created_at: datetime):
    new_class = ClassModel(
        class_code = class_code,
        name = name,
        description = description,
        created_at = created_at
    )
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def get_all_class_service(db:Session):
    list_classes = db.query(ClassModel).all()
    return list_classes

def get_class_by_id_service(db:Session, id: int):
    classroom = db.query(ClassModel).filter(ClassModel.id == id).first()
    return classroom