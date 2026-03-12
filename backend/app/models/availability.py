from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY
from db.database import Base


class Availability(Base):
    __tablename__ = "availability"

    availability_id = Column(Integer, primary_key=True)

    weekly_hours = Column(Integer, nullable=False)
    internship_duration_weeks = Column(Integer, nullable=False)

    preferred_start_date = Column(Date)

    location_preference = Column(String, nullable=False)

    expected_salary = Column(Integer)

    intern_id = Column(Integer, ForeignKey("interns.intern_id"), nullable=False)

    intern = relationship("Intern", back_populates="availability")