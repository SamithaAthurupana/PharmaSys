from fastapi import APIRouter, HTTPException
from database import get_db_connection

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/")
def create_sale(data: dict):
    conn = get_db_connection()
    cursor = conn.cursor()

    items = data["items"]
    user_id = data["user_id"]

    # 1. CHECK STOCK
    for item in items:
        cursor.execute(
            "SELECT quantity FROM inventory WHERE medicine_id = ?",
            (item["medicine_id"],)
        )
        row = cursor.fetchone()
        if not row or row[0] < item["quantity"]:
            raise HTTPException(status_code=400, detail="Not enough stock")

    # 2. CALCULATE TOTAL
    total = sum(item["price"] * item["quantity"] for item in items)

    # 3. CREATE SALE
    cursor.execute(
        "INSERT INTO sales (user_id, total_amount) VALUES (?, ?)",
        (user_id, total)
    )
    cursor.execute("SELECT @@IDENTITY")
    sale_id = cursor.fetchone()[0]

    # 4. INSERT SALE ITEMS + UPDATE INVENTORY
    for item in items:
        cursor.execute("""
            INSERT INTO sales_items (sale_id, medicine_id, quantity, price)
            VALUES (?, ?, ?, ?)
        """, (
            sale_id,
            item["medicine_id"],
            item["quantity"],
            item["price"]
        ))

        cursor.execute("""
            UPDATE inventory
            SET quantity = quantity - ?
            WHERE medicine_id = ?
        """, (item["quantity"], item["medicine_id"]))

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "sale_id": sale_id,
        "total_amount": total
    }
