from sqlalchemy.orm import Session
from models.classrooms import ClassroomModel
from schemas.classrooms import CreateClassroom

def get_all_classes_service(db: Session):
    list_classes = db.query(ClassroomModel).all()
    return list_classes

def get_class_by_id_service(db:Session, id:int):
    classroom = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    return classroom

def create_class_service(db:Session, new_class: CreateClassroom):
    new_class = ClassroomModel(**new_class.model_dump())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def update_class_service(db:Session, id:int, update_class: CreateClassroom):
    db_class = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    if db_class is None:
        return db_class
    for key, value in update_class.model_dump().items():
        setattr(db_class, key, value)
    db.commit()
    db.refresh(db_class)
    return db_class

def delete_class_service(db: Session, id: int):
    db_class = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    delete_class = db_class
    if db_class is None:
        return db_class
    db.delete(db_class)
    db.commit()
    return delete_class