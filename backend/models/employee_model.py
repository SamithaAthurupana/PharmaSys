from database import get_db_connection

def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            e.employee_id,
            e.full_name,
            e.phone,
            e.shift_time,
            e.status,
            u.username,
            u.role
        FROM employees e
        JOIN users u ON e.user_id = u.user_id
    """)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "employee_id": r[0],
            "full_name": r[1],
            "phone": r[2],
            "shift_time": r[3],
            "status": r[4],
            "username": r[5],
            "role": r[6]
        }
        for r in rows
    ]


def create_employee(employee):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO employees (user_id, full_name, phone, shift_time, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        employee.user_id,
        employee.full_name,
        employee.phone,
        employee.shift_time,
        employee.status
    ))

    conn.commit()
    cursor.close()
    conn.close()
