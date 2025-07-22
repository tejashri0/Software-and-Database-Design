from pydantic import BaseModel

class ReviewBase(BaseModel):
    customer_id: int
    text: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int

    class Config:
        orm_mode = True
