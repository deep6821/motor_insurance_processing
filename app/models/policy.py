from sqlalchemy import Column, Integer, String
from base import Base


class Policy(Base):
    __tablename__ = 'policies'

    policy_id = Column(Integer, primary_key=True)
    policy_number = Column(String, unique=True)
    # Other policy attributes
