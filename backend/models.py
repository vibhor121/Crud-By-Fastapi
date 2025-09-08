from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    
    class Config:
        from_attributes = True

