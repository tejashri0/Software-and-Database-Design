from pydantic import BaseModel

class OrderDetailBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailOut(OrderDetailBase):
    id: int

    class Config:
        orm_mode = True
