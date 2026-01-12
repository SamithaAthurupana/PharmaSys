from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicineCreate(BaseModel):
    medicine_name: str
    category: Optional[str] = None
    batch_id: Optional[str] = None
    expiry_date: Optional[date] = None
    price: float
    reorder_level: int = 10

class MedicineUpdate(BaseModel):
    medicine_name: Optional[str]
    category: Optional[str]
    batch_id: Optional[str]
    expiry_date: Optional[date]
    price: Optional[float]
    reorder_level: Optional[int]
