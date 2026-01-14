from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    user_id: int
    full_name: str
    phone: str | None = None
    shift_time: str        # ❗ REQUIRED
    status: str = "ON_DUTY"