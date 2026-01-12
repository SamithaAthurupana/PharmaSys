from passlib.context import CryptContext
import pyodbc

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=pharmacy_db;"
    "Trusted_Connection=yes;"
)

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

print("✅ Admin password reset successfully")
