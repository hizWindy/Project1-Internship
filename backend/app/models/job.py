from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True)

    employer_id = Column(Integer, ForeignKey("employer.employer_id"), nullable=False)

    job_status = Column(Text, default="open")

    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    location = Column(Text, nullable=False)
    internship_mode = Column(Text, nullable=False)

    salary_min = Column(Integer, nullable=False)
    salary_max = Column(Integer)

    requirements = Column(Text, nullable=False)
    responsibilities = Column(Text, nullable=False)

    duration_months = Column(Integer, nullable=False)

    posted_at = Column(DateTime, server_default=func.now())
    update_date = Column(DateTime, server_default=func.now())

    expire_date = Column(Date)
    application_deadline = Column(Date, nullable=False)

    employer = relationship("Employer", back_populates="jobs")
    questions = relationship("Question", back_populates="job")
    applications = relationship("Apply", back_populates="job")
