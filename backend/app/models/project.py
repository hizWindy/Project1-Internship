from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY




class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True)

    project_name = Column(Text, nullable=False)
    project_description = Column(Text, nullable=False)
    project_link = Column(Text, nullable=False)

    intern_id = Column(Integer, ForeignKey("interns.intern_id"), nullable=False)

    intern = relationship("Intern", back_populates="projects")
