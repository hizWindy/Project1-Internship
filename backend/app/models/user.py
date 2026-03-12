from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, Date, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
''

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    intern = relationship("Intern", back_populates="user")
    employer = relationship("Employer", back_populates="user")
