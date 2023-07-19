from sqlalchemy import Column, Integer, String
from base import Base


class CaseManagerReport(Base):
    __tablename__ = 'case_manager_reports'

    case_manager_report_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other case manager report attributes
