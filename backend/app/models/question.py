from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True)

    questionaire = Column(Text, nullable=False)
    answer = Column(Text, default="N/A")

    job_id = Column(Integer, ForeignKey("jobs.job_id"), nullable=False)

    job = relationship("Job", back_populates="questions")
