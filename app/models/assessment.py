from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from base import Base


class Assessment(Base):
    __tablename__ = 'assessments'

    assessment_id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'))
    assessment_report = Column(String)

    claim = relationship('Claim', back_populates='assessments')
    payments = relationship('Payment', back_populates='assessment')
