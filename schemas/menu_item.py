from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    category: str

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemOut(MenuItemBase):
    id: int

    class Config:
        orm_mode = True
