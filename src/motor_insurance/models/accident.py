from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from motor_insurance.base import Base


class Accident(Base):
    __tablename__ = "accidents"

    id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"))
    description = Column(String)
    # Other accident attributes

    claim = relationship("Claim", backref="accidents")
