from sqlalchemy import Column, Integer, String
from motor_insurance.base import Base


class CaseManagerReport(Base):
    __tablename__ = "case_manager_reports"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other case manager report attributes
