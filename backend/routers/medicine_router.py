from fastapi import APIRouter
from schemas.medicine_schema import MedicineCreate, MedicineUpdate
from models.medicine_model import (
    get_all_medicines,
    create_medicine,
    update_medicine
)

router = APIRouter(prefix="/medicines", tags=["Medicines"])

@router.get("/")
def list_medicines():
    return get_all_medicines()

@router.post("/")
def add_medicine(med: MedicineCreate):
    create_medicine(med)
    return {"message": "Medicine added"}

@router.put("/{medicine_id}")
def edit_medicine(medicine_id: int, med: MedicineUpdate):
    update_medicine(medicine_id, med)
    return {"message": "Medicine updated"}
