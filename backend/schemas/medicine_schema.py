from pydantic import BaseModel
from datetime import date

class MedicineBase(BaseModel):
    medicine_name: str
    category: str
    batch_id: str
    expiry_date: date
    price: float
    reorder_level: int

class MedicineCreate(MedicineBase):
    pass

class MedicineResponse(MedicineBase):
    medicine_id: int

    class Config:
        from_attributes = True
