from database import get_db_connection

def create_sale(sale):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 1️⃣ Create sale
        cursor.execute("""
            INSERT INTO sales (user_id, discount, total_amount)
            VALUES (?, ?, ?)
        """, (
            sale.user_id,
            sale.discount,
            sale.total_amount
        ))

        sale_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]

        # 2️⃣ Insert sale items + reduce inventory
        for item in sale.items:
            # Insert sale item
            cursor.execute("""
                INSERT INTO sale_items (sale_id, medicine_id, quantity, price)
                VALUES (?, ?, ?, ?)
            """, (
                sale_id,
                item.medicine_id,
                item.quantity,
                item.price
            ))

            # 🔥 IMPORTANT: Reduce inventory
            cursor.execute("""
                UPDATE inventory
                SET quantity = quantity - ?
                WHERE medicine_id = ?
            """, (
                item.quantity,
                item.medicine_id
            ))

        conn.commit()
        return sale_id

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()


def get_inventory_list():
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        m.medicine_id,
        m.medicine_name,
        m.batch_id,
        m.expiry_date,
        m.reorder_level,
        m.price,
        i.quantity
    FROM dbo.medicines m
    JOIN dbo.inventory i ON m.medicine_id = i.medicine_id
    ORDER BY m.medicine_name
""")


    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    inventory = []
    for r in rows:
        inventory.append({
    "medicine_id": r[0],
    "medicine_name": r[1],
    "batch_id": r[2],
    "expiry_date": str(r[3]) if r[3] else None,
    "reorder_level": r[4],
    "price": float(r[5]),   # ✅ ADD THIS
    "quantity": r[6]
})


    return inventory


def update_inventory_quantity(medicine_id, quantity):
    if quantity < 0:
        return False

    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE dbo.inventory
            SET quantity = ?
            WHERE medicine_id = ?
        """, (quantity, medicine_id))

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        conn.commit()
        return True


    except Exception as e:
        conn.rollback()
        print("❌ update_inventory_quantity error:", e)
        return False

    finally:
        cursor.close()
        conn.close()
