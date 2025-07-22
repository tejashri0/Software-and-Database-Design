from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    customer_id: int
    total: float
    status: str

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
