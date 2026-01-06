from pydantic import BaseModel

class SupplierBase(BaseModel):
    supplier_name: str
    contact_person: str | None = None
    phone: str | None = None
    email: str | None = None
    category: str | None = None
    status: str = "ACTIVE"

class SupplierCreate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    supplier_id: int

    class Config:
        from_attributes = True
