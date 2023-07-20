from sqlalchemy import Column, Integer, ForeignKey, String
from motor_insurance.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"))
    file_name = Column(String)
    # Other document attributes
