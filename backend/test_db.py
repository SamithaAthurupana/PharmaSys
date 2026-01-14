from database import get_db_connection

conn = get_db_connection()

if conn:
    print("SQL Server connected successfully")
    conn.close()
else:
    print("❌ Connection failed")
