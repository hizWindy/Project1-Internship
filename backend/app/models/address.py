from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True)

    address_type = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    region = Column(Text, nullable=False)

    intern_id = Column(Integer, ForeignKey("interns.intern_id"), nullable=False)

    intern = relationship("Intern", back_populates="addresses")
