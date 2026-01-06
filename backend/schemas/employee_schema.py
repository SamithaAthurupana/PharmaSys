from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    user_id: int
    full_name: str
    phone: Optional[str] = None
    shift_time: Optional[str] = None
    status: str = "ON_DUTY"

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    employee_id: int

    class Config:
        from_attributes = True
