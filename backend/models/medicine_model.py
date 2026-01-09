from database import get_db_connection
def get_all_medicines():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT medicine_id, medicine_name, category, batch_id,
               expiry_date, stock, price
        FROM medicines
        ORDER BY medicine_id DESC
    """)

    data = cursor.fetchall()

    # Convert date → string (important)
    for m in data:
        if m["expiry_date"]:
            m["expiry_date"] = m["expiry_date"].strftime("%Y-%m-%d")

    cursor.close()
    conn.close()
    return data




def create_medicine(med):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO medicines
        (medicine_name, category, batch_id, expiry_date, stock, price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        med.medicine_name,
        med.category,
        med.batch_id,
        med.expiry_date,
        med.stock,      # 🔥 CHANGED
        med.price
    ))

    conn.commit()
    cursor.close()
    conn.close()
    return True



def update_medicine(medicine_id, med):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE medicines
        SET medicine_name=%s,
            category=%s,
            expiry_date=%s,
            stock=%s,
            price=%s
        WHERE medicine_id=%s
    """, (
        med.medicine_name,
        med.category,
        med.expiry_date,
        med.stock,     # 🔥 CHANGED
        med.price,
        medicine_id
    ))

    conn.commit()
    cursor.close()
    conn.close()
    return True
