from sqlalchemy import Column, Integer, String
from base import Base


class ServiceStation(Base):
    __tablename__ = 'service_stations'

    service_station_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Other service station attributes
