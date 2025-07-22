from sqlalchemy import Column, Integer, String, Float, Date
from dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50))
    discount = Column(Float)
    expiry = Column(Date)
