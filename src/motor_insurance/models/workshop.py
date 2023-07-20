from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from motor_insurance.base import Base


class Workshop(Base):
    __tablename__ = "workshops"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    workshop_data = Column(String(255))
    # Other workshop attributes

    cases = relationship("Case", back_populates="workshop")
