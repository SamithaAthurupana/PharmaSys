from database import get_db_connection

def get_all_employees():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
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
    """

    cursor.execute(query)
    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees


def create_employee(employee):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO employees (user_id, full_name, phone, shift_time, status)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        employee.user_id,
        employee.full_name,
        employee.phone,
        employee.shift_time,
        employee.status
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return True


def update_employee_status(employee_id, status):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE employees
        SET status = %s
        WHERE employee_id = %s
    """

    cursor.execute(query, (status, employee_id))
    connection.commit()

    cursor.close()
    connection.close()

    return True
