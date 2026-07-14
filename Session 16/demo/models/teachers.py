from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class TeacherModel(Base):
    __tablename__ = "teachers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classes.id"), unique=True)
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="teacher",
        uselist= False
    )
    