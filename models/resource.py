from sqlalchemy import Column, Integer, String, Float
from dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    ingredient = Column(String(100))
    quantity = Column(Float)
    unit = Column(String(20))
