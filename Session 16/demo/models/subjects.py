from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.student_subject import student_subject

class SubjectModel(Base):
    __tablename__ = "subjects"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    
    # student_subjects = relationship(
    #     "StudentSubjectModel",
    #     back_populates="subject"
    # )
    
    students = relationship(
        "StudentModel",
        back_populates=True,
        secondary = student_subject
    )
    