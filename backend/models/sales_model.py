from database import get_db_connection

def create_sale(user_id, discount, items):
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor()

    try:
        total = sum(item["price"] * item["quantity"] for item in items)
        total_after_discount = total - discount

        # Insert sale
        cursor.execute("""
            INSERT INTO dbo.sales (user_id, total_amount, discount)
            OUTPUT INSERTED.sale_id
            VALUES (?, ?, ?)
        """, (user_id, total_after_discount, discount))

        sale_id = cursor.fetchone()[0]

        # Insert sale items + reduce stock
        for item in items:
            cursor.execute("""
                INSERT INTO dbo.sale_items (sale_id, medicine_id, quantity, price)
                VALUES (?, ?, ?, ?)
            """, (
                sale_id,
                item["medicine_id"],
                item["quantity"],
                item["price"]
            ))

            cursor.execute("""
                UPDATE dbo.inventory
                SET quantity = quantity - ?
                WHERE medicine_id = ? AND quantity >= ?
            """, (
                item["quantity"],
                item["medicine_id"],
                item["quantity"]
            ))

            if cursor.rowcount == 0:
                raise Exception("Insufficient stock")

        conn.commit()
        return sale_id

    except Exception as e:
        conn.rollback()
        print("❌ create_sale error:", e)
        return None

    finally:
        cursor.close()
        conn.close()
