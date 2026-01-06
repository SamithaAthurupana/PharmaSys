from fastapi import APIRouter
from schemas.inventory_schema import InventoryCreate
from models.inventory_model import (
    get_inventory_with_medicines,
    create_inventory_item,
    update_inventory_quantity
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.get("/")
def list_inventory():
    return get_inventory_with_medicines()

@router.post("/")
def add_inventory_item(inventory: InventoryCreate):
    create_inventory_item(inventory)
    return {"message": "Inventory item added successfully"}

@router.put("/{inventory_id}")
def update_inventory(inventory_id: int, quantity: int):
    update_inventory_quantity(inventory_id, quantity)
    return {"message": "Inventory quantity updated"}
