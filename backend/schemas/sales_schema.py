from pydantic import BaseModel
from typing import List


class SaleItem(BaseModel):
    medicine_id: int
    quantity: int
    price: float


class SaleCreate(BaseModel):
    user_id: int
    discount: float = 0
    total_amount: float
    items: List[SaleItem]
