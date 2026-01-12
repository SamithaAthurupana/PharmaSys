from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_db_connection
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["Auth"])

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, username, password_hash
        FROM users
        WHERE username = ?
    """, (data.username,))

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    user_id, username, password_hash = row

    if not pwd_context.verify(data.password, password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "user": {
            "user_id": user_id,
            "username": username
        }
    }
