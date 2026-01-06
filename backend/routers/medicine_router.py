from fastapi import APIRouter
from schemas.medicine_schema import MedicineCreate
from models.medicine_model import get_all_medicines, create_medicine

router = APIRouter(
    prefix="/medicines",
    tags=["Medicines"]
)

@router.get("/")
def list_medicines():
    return get_all_medicines()

@router.post("/")
def add_medicine(medicine: MedicineCreate):
    create_medicine(medicine)
    return {"message": "Medicine added successfully"}
