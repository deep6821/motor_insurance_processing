from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from base import Base


class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True)
    claim_id = Column(String(50), unique=True)
    assessment_id = Column(Integer, ForeignKey('assessments.id'))
    payment_amount = Column(Integer)
    payment_data = Column(String(255))
    status = Column(String(20))

    assessment = relationship('Assessment', back_populates='payments')
