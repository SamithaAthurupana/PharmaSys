from fastapi import APIRouter, HTTPException
from schemas.medicine_schema import MedicineCreate, MedicineUpdate
from models.medicine_model import (
    get_all_medicines,
    create_medicine,
    update_medicine,
    delete_medicine
)

router = APIRouter(prefix="/medicines", tags=["Medicines"])


@router.get("/")
def list_medicines():
    return get_all_medicines()



@router.post("/")
def add_medicine(med: MedicineCreate):
    if not create_medicine(med):
        raise HTTPException(
            status_code=400,
            detail="Failed to add medicine"
        )
    return {"message": "Medicine added successfully"}


@router.put("/{medicine_id}")
def edit_medicine(medicine_id: int, med: MedicineUpdate):
    if not update_medicine(medicine_id, med):
        raise HTTPException(
            status_code=400,
            detail="Failed to update medicine"
        )
    return {"message": "Medicine updated successfully"}


@router.delete("/{medicine_id}")
def remove_medicine(medicine_id: int):
    if not delete_medicine(medicine_id):
        raise HTTPException(
            status_code=404,
            detail="Medicine not found"
        )
    return {"message": "Medicine deleted successfully"}
