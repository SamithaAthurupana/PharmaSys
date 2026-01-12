from fastapi import APIRouter, HTTPException
from models.inventory_model import (
    get_inventory_list,
    update_inventory_quantity
)

router = APIRouter(prefix="/inventory", tags=["Inventory"])


# ✅ GET inventory list
@router.get("/")
def get_inventory():
    return get_inventory_list()


# ✅ UPDATE inventory quantity (THIS WAS MISSING)
@router.put("/{medicine_id}")
def update_inventory(medicine_id: int, quantity: int):
    success = update_inventory_quantity(medicine_id, quantity)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to update inventory quantity"
        )

    return {"message": "Inventory updated successfully"}
