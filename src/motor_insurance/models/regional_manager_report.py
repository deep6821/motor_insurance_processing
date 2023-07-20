from sqlalchemy import Column, Integer, String
from motor_insurance.base import Base


class RegionalManagerReport(Base):
    __tablename__ = "regional_manager_reports"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other regional manager report attributes
