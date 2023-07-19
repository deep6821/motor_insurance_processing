from sqlalchemy import Column, Integer, String
from base import Base


class RegionalManagerReport(Base):
    __tablename__ = 'regional_manager_reports'

    regional_manager_report_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other regional manager report attributes
