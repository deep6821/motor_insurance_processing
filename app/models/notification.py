from sqlalchemy import Column, Integer, ForeignKey, String
from base import Base


class Notification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'))
    recipient_id = Column(Integer)
    message = Column(String)
    # Other notification attributes
