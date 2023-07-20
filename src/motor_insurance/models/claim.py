from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from motor_insurance.base import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    claim_data = Column(String(255))
    claim_status = Column(String(255))
    claim_coverage = Column(String(255))
    claim_amount = Column(String(255))
    claim_date = Column(DateTime)

    customer = relationship("Customer", back_populates="claims")
    assessments = relationship("Assessment", back_populates="claim")

