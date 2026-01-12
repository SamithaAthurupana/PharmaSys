from database import get_db_connection


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
