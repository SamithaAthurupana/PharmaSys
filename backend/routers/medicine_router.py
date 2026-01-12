from fastapi import APIRouter
from schemas.medicine_schema import MedicineCreate, MedicineUpdate
from fastapi import HTTPException
from models.medicine_model import (
    get_all_medicines,
    create_medicine,
    update_medicine
)

router = APIRouter(
    prefix="/medicines",
    tags=["Medicines"]
)

@router.get("/")
def list_medicines():
    return get_all_medicines()

@router.post("/")
def add_medicine(med: MedicineCreate):
    success = create_medicine(med)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Failed to add medicine. Check input values."
        )
    return {"message": "Medicine added successfully"}

@router.put("/{medicine_id}")
def edit_medicine(medicine_id: int, med: MedicineUpdate):
    update_medicine(medicine_id, med)
    return {"message": "Medicine updated successfully"}
