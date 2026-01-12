from database import get_db_connection

def get_all_medicines():
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            m.medicine_id,
            m.medicine_name,
            m.category,
            m.batch_id,
            m.expiry_date,
            m.price,
            m.reorder_level,
            i.quantity
        FROM dbo.medicines m
        INNER JOIN dbo.inventory i 
            ON m.medicine_id = i.medicine_id
        ORDER BY m.medicine_id DESC
    """)

    rows = cursor.fetchall()

    medicines = []
    for r in rows:
        medicines.append({
            "medicine_id": r[0],
            "medicine_name": r[1],
            "category": r[2],
            "batch_id": r[3],
            "expiry_date": str(r[4]) if r[4] else None,
            "price": float(r[5]),
            "reorder_level": r[6],
            "quantity": r[7]
        })

    cursor.close()
    conn.close()
    return medicines

def create_medicine(med):
    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()

    try:
        # Insert medicine and get ID safely
        cursor.execute("""
            INSERT INTO dbo.medicines
            (medicine_name, category, batch_id, expiry_date, price, reorder_level)
            OUTPUT INSERTED.medicine_id
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            med.medicine_name,
            med.category,
            med.batch_id,
            med.expiry_date,
            med.price,
            med.reorder_level
        ))

        medicine_id = cursor.fetchone()[0]  # ✅ NEVER None

        # Auto-create inventory
        cursor.execute("""
            INSERT INTO dbo.inventory (medicine_id, quantity)
            VALUES (?, ?)
        """, (medicine_id, 0))

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print("❌ create_medicine error:", e)
        return False

    finally:
        cursor.close()
        conn.close()


def update_medicine(medicine_id, med):
    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE dbo.medicines
            SET 
                medicine_name = COALESCE(?, medicine_name),
                category = COALESCE(?, category),
                batch_id = COALESCE(?, batch_id),
                expiry_date = COALESCE(?, expiry_date),
                price = COALESCE(?, price),
                reorder_level = COALESCE(?, reorder_level)
            WHERE medicine_id = ?
        """, (
            med.medicine_name,
            med.category,
            med.batch_id,
            med.expiry_date,
            med.price,
            med.reorder_level,
            medicine_id
        ))

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print("❌ update_medicine error:", e)
        return False

    finally:
        cursor.close()
        conn.close()

def delete_medicine(medicine_id):
    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM dbo.medicines WHERE medicine_id = ?",
            (medicine_id,)
        )

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print("❌ delete_medicine error:", e)
        return False

    finally:
        cursor.close()
        conn.close()
