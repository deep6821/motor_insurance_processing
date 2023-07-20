from sqlalchemy import Column, Integer, String
from motor_insurance.base import Base


class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True)
    policy_number = Column(String, unique=True)
    # Other policy attributes
