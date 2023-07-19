from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from base import Base


class Accident(Base):
    __tablename__ = 'accidents'

    accident_id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'))
    description = Column(String)
    # Other accident attributes

    claim = relationship('Claim', backref='accidents')
