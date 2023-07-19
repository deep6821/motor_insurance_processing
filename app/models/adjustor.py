from sqlalchemy import Column, Integer, String
from base import Base


class Adjustor(Base):
    __tablename__ = 'adjustors'

    adjustor_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other adjustor attributes
