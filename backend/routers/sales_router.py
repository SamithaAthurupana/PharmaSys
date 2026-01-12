from fastapi import APIRouter, HTTPException
from database import get_db_connection

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/")
def create_sale(data: dict):
    conn = get_db_connection()
    cursor = conn.cursor()

    items = data["items"]
    user_id = data["user_id"]

    try:
        # 1️⃣ CHECK STOCK
        for item in items:
            cursor.execute(
                "SELECT quantity FROM inventory WHERE medicine_id = ?",
                (item["medicine_id"],)
            )
            row = cursor.fetchone()

            if not row:
                raise HTTPException(status_code=400, detail="Medicine not found")

            if row[0] < item["quantity"]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Not enough stock for medicine_id {item['medicine_id']}"
                )

        # 2️⃣ CALCULATE TOTAL
        total = sum(item["price"] * item["quantity"] for item in items)

        # 3️⃣ CREATE SALE
        cursor.execute(
            "INSERT INTO sales (user_id, total_amount) VALUES (?, ?)",
            (user_id, total)
        )
        cursor.execute("SELECT SCOPE_IDENTITY()")
        sale_id = int(cursor.fetchone()[0])

        # 4️⃣ INSERT ITEMS + REDUCE INVENTORY
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
            """, (
                item["quantity"],
                item["medicine_id"]
            ))

        # 5️⃣ COMMIT
        conn.commit()

        return {
            "message": "Sale completed",
            "sale_id": sale_id,
            "total": total
        }

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()
