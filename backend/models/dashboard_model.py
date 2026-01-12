from database import get_db_connection

def get_dashboard_stats():
    conn = get_db_connection()
    if conn is None:
        return {
            "today_sales": 0,
            "total_medicines": 0,
            "low_stock": 0,
            "expiring_soon": 0
        }

    cursor = conn.cursor()

    # ✅ TOTAL SALES (NO DATE FILTER — SAFE)
    cursor.execute("""
        SELECT ISNULL(SUM(total_amount), 0)
        FROM sales
    """)
    today_sales = cursor.fetchone()[0]

    # ✅ TOTAL MEDICINES
    cursor.execute("SELECT COUNT(*) FROM medicines")
    total_medicines = cursor.fetchone()[0]

    # ✅ LOW STOCK
    cursor.execute("""
        SELECT COUNT(*)
        FROM inventory i
        JOIN medicines m ON i.medicine_id = m.medicine_id
        WHERE i.quantity <= m.reorder_level
    """)
    low_stock = cursor.fetchone()[0]

    # ✅ EXPIRING SOON (SAFE NULL CHECK)
    cursor.execute("""
        SELECT COUNT(*)
        FROM medicines
        WHERE expiry_date IS NOT NULL
        AND expiry_date <= DATEADD(DAY, 30, GETDATE())
    """)
    expiring_soon = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "today_sales": float(today_sales),
        "total_medicines": total_medicines,
        "low_stock": low_stock,
        "expiring_soon": expiring_soon
    }
