from pydantic import BaseModel
from typing import Optional
from datetime import date

class MedicineBase(BaseModel):
    medicine_name: str
    category: str
    batch_id: str
    expiry_date: date
    price: float
    reorder_level: int

class MedicineCreate(BaseModel):
    medicine_name: str
    category: str
    batch_id: str
    expiry_date: date
    stock: int       # 🔥 NOT quantity
    price: float

class MedicineUpdate(BaseModel):
    medicine_name: Optional[str]
    category: Optional[str]
    expiry_date: Optional[date]
    stock: Optional[int]
    price: Optional[float]


class MedicineResponse(MedicineBase):
    medicine_id: int

    class Config:
        from_attributes = True
