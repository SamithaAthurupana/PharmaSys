from fastapi import APIRouter, HTTPException
from database import get_db_connection
from schemas.employee_schema import EmployeeCreate
from models.employee_model import (
    get_all_employees,
    create_employee,
    update_employee_status,
    delete_employee
)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/")
def list_employees():
    return get_all_employees()


@router.post("/")
def add_employee(employee: EmployeeCreate):
    try:
        create_employee(employee)
        return {"message": "Employee added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{employee_id}")
def remove_employee(employee_id: int):
    deleted = delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}


@router.get("/users/by-role/{role}")
def users_by_role(role: str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT u.user_id, u.username
        FROM users u
        JOIN roles r ON u.role_id = r.role_id
        WHERE r.role_name = ?
        AND u.user_id NOT IN (SELECT user_id FROM employees)
    """, (role.upper(),))

    rows = cur.fetchall()
    conn.close()

    return [{"user_id": r[0], "username": r[1]} for r in rows]
