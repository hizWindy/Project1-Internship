from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY
from db.database import Base


class Employer(Base):
    __tablename__ = "employer"

    employer_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    companies_id = Column(Integer, ForeignKey("companies.companies_id"), nullable=False)

    first_name = Column(Text, nullable=False)
    middle_name = Column(Text)
    last_name = Column(Text, nullable=False)

    position = Column(Text, nullable=False)

    user = relationship("User", back_populates="employer")
    company = relationship("Company", back_populates="employers")
    jobs = relationship("Job", back_populates="employer")
