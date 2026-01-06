from pydantic import BaseModel
from datetime import datetime

class InventoryBase(BaseModel):
    medicine_id: int
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    inventory_id: int
    last_updated: datetime

    class Config:
        from_attributes = True
