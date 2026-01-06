from fastapi import APIRouter, HTTPException
from schemas.user_schema import LoginRequest
from models.user_model import authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(login_data: LoginRequest):
    user = authenticate_user(login_data.username, login_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "user": user
    }
