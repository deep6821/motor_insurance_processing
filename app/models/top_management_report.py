from sqlalchemy import Column, Integer, String
from base import Base


class TopManagementReport(Base):
    __tablename__ = 'top_management_reports'

    top_management_report_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other top management report attributes
