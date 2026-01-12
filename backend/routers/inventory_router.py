from fastapi import APIRouter
from database import get_db_connection

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/")
def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            m.medicine_id,
            m.medicine_name,
            m.batch_id,
            m.expiry_date,
            m.price,
            i.quantity
        FROM inventory i
        JOIN medicines m ON i.medicine_id = m.medicine_id
    """)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "medicine_id": r[0],
            "medicine_name": r[1],
            "batch_id": r[2],
            "expiry_date": str(r[3]),
            "price": float(r[4]),
            "quantity": r[5]
        }
        for r in rows
    ]
