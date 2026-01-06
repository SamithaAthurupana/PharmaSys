from fastapi import APIRouter
from schemas.supplier_schema import SupplierCreate
from models.supplier_model import get_all_suppliers, create_supplier

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

@router.get("/")
def list_suppliers():
    return get_all_suppliers()

@router.post("/")
def add_supplier(supplier: SupplierCreate):
    create_supplier(supplier)
    return {"message": "Supplier added successfully"}
