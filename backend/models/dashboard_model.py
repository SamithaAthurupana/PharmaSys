from database import get_db_connection
from datetime import date, timedelta

def get_dashboard_stats():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    today = date.today()
    next_30_days = today + timedelta(days=30)

    # 1️⃣ Today's Sales Total
    cursor.execute("""
        SELECT IFNULL(SUM(total_amount), 0) AS today_sales
        FROM sales
        WHERE DATE(sale_date) = CURDATE()
    """)
    today_sales = cursor.fetchone()["today_sales"]

    # 2️⃣ Total Medicines Count
    cursor.execute("SELECT COUNT(*) AS total_medicines FROM medicines")
    total_medicines = cursor.fetchone()["total_medicines"]

    # 3️⃣ Expiring Within 30 Days
    cursor.execute("""
        SELECT COUNT(*) AS expiring_soon
        FROM medicines
        WHERE expiry_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
    """)
    expiring_soon = cursor.fetchone()["expiring_soon"]

    # 4️⃣ Low Stock Alerts
    cursor.execute("""
        SELECT COUNT(*) AS low_stock
        FROM inventory i
        JOIN medicines m ON i.medicine_id = m.medicine_id
        WHERE i.quantity <= m.reorder_level
    """)
    low_stock = cursor.fetchone()["low_stock"]

    cursor.close()
    connection.close()

    return {
        "today_sales": today_sales,
        "total_medicines": total_medicines,
        "expiring_soon": expiring_soon,
        "low_stock": low_stock
    }
