from sqlalchemy import Column, Integer, String
from motor_insurance.base import Base


class Adjustor(Base):
    __tablename__ = "adjustors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other adjustor attributes
