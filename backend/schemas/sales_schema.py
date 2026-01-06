from pydantic import BaseModel
from typing import List
from datetime import datetime

class SaleItem(BaseModel):
    medicine_id: int
    quantity: int
    price: float

class SaleCreate(BaseModel):
    user_id: int
    discount: float = 0
    items: List[SaleItem]

class SaleResponse(BaseModel):
    sale_id: int
    total_amount: float
    discount: float
    sale_date: datetime
