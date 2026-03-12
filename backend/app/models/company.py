from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Company(Base):
    __tablename__ = "companies"

    companies_id = Column(Integer, primary_key=True)

    name = Column(Text)
    description = Column(Text, nullable=False)
    industry = Column(Text, nullable=False)

    company_size = Column(Integer, nullable=False)
    founded_year = Column(Integer, nullable=False)

    employers = relationship("Employer", back_populates="company")
