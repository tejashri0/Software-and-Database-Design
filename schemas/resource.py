from pydantic import BaseModel

class ResourceBase(BaseModel):
    ingredient: str
    quantity: float
    unit: str

class ResourceCreate(ResourceBase):
    pass

class ResourceOut(ResourceBase):
    id: int

    class Config:
        orm_mode = True
