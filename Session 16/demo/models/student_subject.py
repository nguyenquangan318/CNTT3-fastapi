from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

# class StudentSubjectModel(Base):
#     __tablename__ = "student_subject"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     Created_at = Column(DateTime)
#     student_id = Column(Integer, ForeignKey("students.id"))
#     subject_id = Column(Integer, ForeignKey("subjects.id"))
    
#     student = relationship(
#         "StudentModel",
#         back_populates="",
#         uselist= False
#     )
    
#     subject = relationship(
#         "subjectModel",
#         back_populates="",
#         uselist= False
#     )

student_subject = Table(
    "student_subject",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True)
)