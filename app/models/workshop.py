from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class Workshop(Base):
    __tablename__ = 'workshops'

    workshop_id = Column(Integer, primary_key=True)
    name = Column(String)
    workshop_data = Column(String(255))
    # Other workshop attributes

    cases = relationship('Case', back_populates='workshop')
