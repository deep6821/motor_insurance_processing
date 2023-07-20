from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from motor_insurance.base import Base


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"))
    assessment_report = Column(String)

    claim = relationship("Claim", back_populates="assessments")
    payments = relationship("Payment", back_populates="assessment")
