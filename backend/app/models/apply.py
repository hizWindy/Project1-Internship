from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY
from db.database import Base


class Apply(Base):
    __tablename__ = "apply"

    apply_id = Column(Integer, primary_key=True)

    apply_date = Column(DateTime, server_default=func.now())
    status = Column(Text, default="pending")

    intern_id = Column(Integer, ForeignKey("interns.intern_id"), nullable=False)
    post_id = Column(Integer, ForeignKey("jobs.job_id"), nullable=False)

    intern = relationship("Intern", back_populates="applications")
    job = relationship("Job", back_populates="applications")