from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)
    correspondence_address = Column(String)
    billing_cycle = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)

    claims = relationship('Claim', back_populates='customer')
