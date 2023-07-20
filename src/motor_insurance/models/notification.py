from sqlalchemy import Column, Integer, ForeignKey, String
from motor_insurance.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"))
    recipient_id = Column(Integer)
    message = Column(String)
    # Other notification attributes
