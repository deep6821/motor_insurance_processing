from sqlalchemy import Column, Integer, String
from motor_insurance.base import Base


class TopManagementReport(Base):
    __tablename__ = "top_management_reports"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other top management report attributes
