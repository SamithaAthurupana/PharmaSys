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
            r.role_name
        FROM employees e
        JOIN users u ON e.user_id = u.user_id
        JOIN roles r ON u.role_id = r.role_id
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

    # CHECK user exists
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (employee.user_id,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        raise Exception("Invalid user ID")

    # CHECK employee already exists
    cursor.execute("SELECT employee_id FROM employees WHERE user_id = ?", (employee.user_id,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        raise Exception("Employee already exists for this user")

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


def update_employee_status(employee_id: int, status: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE employees
        SET status = ?
        WHERE employee_id = ?
    """, (status, employee_id))

    conn.commit()
    cursor.close()
    conn.close()


def delete_employee(employee_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 🔒 CHECK ROLE FIRST
    cursor.execute("""
        SELECT r.role_name
        FROM employees e
        JOIN users u ON e.user_id = u.user_id
        JOIN roles r ON u.role_id = r.role_id
        WHERE e.employee_id = ?
    """, (employee_id,))

    row = cursor.fetchone()

    if not row:
        conn.close()
        return False

    role_name = row[0]

    # 🔒 BLOCK ADMIN DELETION
    if role_name == "ADMIN":
        conn.close()
        raise Exception("ADMIN user cannot be deleted")

    # ✅ DELETE NON-ADMIN
    cursor.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
    conn.commit()
    conn.close()

    return True

def get_available_users_by_role(role_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.user_id, u.username
        FROM users u
        JOIN roles r ON u.role_id = r.role_id
        WHERE r.role_name = ?
        AND u.user_id NOT IN (SELECT user_id FROM employees)
    """, (role_name,))

    rows = cursor.fetchall()
    conn.close()

    return [{"user_id": r[0], "username": r[1]} for r in rows]