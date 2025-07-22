from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    amount: float
    status: str
    method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int

    class Config:
        orm_mode = True
