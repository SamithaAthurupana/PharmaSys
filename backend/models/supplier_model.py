from database import get_db_connection

def get_all_suppliers():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()

    cursor.close()
    connection.close()

    return suppliers


def create_supplier(supplier):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO suppliers
        (supplier_name, contact_person, phone, email, category, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        supplier.supplier_name,
        supplier.contact_person,
        supplier.phone,
        supplier.email,
        supplier.category,
        supplier.status
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return True
