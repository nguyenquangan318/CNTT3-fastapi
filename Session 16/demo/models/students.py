from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.student_subject import student_subject

class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classes.id"), unique=True)
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="students",
        uselist= False
    )
    
    # student_subjects = relationship(
    #     "StudentSubjectModel",
    #     back_populates="student"
    # )

    subjects = relationship(
        "SubjectModel",
        back_populates = True,
        secondary = student_subject
    )