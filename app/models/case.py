from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from base import Base


class Case(Base):
    __tablename__ = 'cases'

    case_id = Column(Integer, primary_key=True)
    case_data = Column(String(255))
    claim_id = Column(Integer, ForeignKey('claims.id'))
    surveyor_id = Column(Integer, ForeignKey('surveyors.id'))
    workshop_id = Column(Integer, ForeignKey('workshops.id'))
    # Other case attributes

    claim = relationship('Claim', backref='cases')
    surveyor = relationship('Surveyor', back_populates='cases')
    workshop = relationship('Workshop', back_populates='cases')
