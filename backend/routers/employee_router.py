from fastapi import APIRouter
from schemas.employee_schema import EmployeeCreate
from models.employee_model import (
    get_all_employees,
    create_employee,
    update_employee_status
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.get("/")
def list_employees():
    return get_all_employees()

@router.post("/")
def add_employee(employee: EmployeeCreate):
    create_employee(employee)
    return {"message": "Employee added successfully"}

@router.put("/{employee_id}")
def update_status(employee_id: int, status: str):
    update_employee_status(employee_id, status)
    return {"message": "Employee status updated"}
