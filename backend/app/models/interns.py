from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY

class Intern(Base):
    __tablename__ = "interns"

    intern_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    first_name = Column(Text, nullable=False)
    middle_name = Column(Text)
    last_name = Column(Text, nullable=False)

    course = Column(Text, nullable=False)
    college = Column(Text, nullable=False)
    about_me = Column(Text, nullable=False)

    target_roles = Column(ARRAY(Text))
    tech_stack = Column(ARRAY(Text))
    job_type = Column(ARRAY(Text))

    certifications = Column(Text)
    resume = Column(Text)

    user = relationship("User", back_populates="intern")
    addresses = relationship("Address", back_populates="intern")
    availability = relationship("Availability", back_populates="intern")
    projects = relationship("Project", back_populates="intern")
    applications = relationship("Apply", back_populates="intern")