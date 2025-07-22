from pydantic import BaseModel
from datetime import date

class PromotionBase(BaseModel):
    code: str
    discount: float
    expiry: date

class PromotionCreate(PromotionBase):
    pass

class PromotionOut(PromotionBase):
    id: int

    class Config:
        orm_mode = True
