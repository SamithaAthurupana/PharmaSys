from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pyodbc
from database import get_db_connection

router = APIRouter(prefix="/auth", tags=["Auth"])

# Request model
class LoginRequest(BaseModel):
    username: str
    password: str

# LOGIN API
@router.post("/login")
def login(data: LoginRequest):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            u.user_id,
            u.username,
            r.role_name
        FROM users u
        JOIN roles r ON u.role_id = r.role_id
        WHERE u.username = ? 
          AND u.password_hash = ?
          AND u.is_active = 1
        """

        cursor.execute(query, (data.username, data.password))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if not row:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        user = {
            "user_id": row[0],
            "username": row[1],
            "role": row[2]
        }

        return {
            "message": "Login successful",
            "user": user
        }

    except HTTPException:
        raise

    except Exception as e:
        print("LOGIN ERROR:", e)
        raise HTTPException(status_code=500, detail="Server error")
