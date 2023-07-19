from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class Surveyor(Base):
    __tablename__ = 'surveyors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surveyor_id = Column(String(50), unique=True)
    surveyor_data = Column(String(255))
    # Other surveyor attributes

    cases = relationship('Case', back_populates='surveyor')
