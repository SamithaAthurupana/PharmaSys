from passlib.context import CryptContext
from database import get_db_connection

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

conn = get_db_connection()
cursor = conn.cursor()

hashed = pwd.hash("admin123")

cursor.execute("""
    UPDATE users
    SET password_hash = ?
    WHERE username = 'admin'
""", (hashed,))

conn.commit()
cursor.close()
conn.close()

print("Admin password reset to: admin123")
