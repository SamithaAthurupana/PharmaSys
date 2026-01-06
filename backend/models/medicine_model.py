from database import get_db_connection

def get_all_medicines():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()

    cursor.close()
    connection.close()

    return medicines


def create_medicine(medicine):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO medicines
        (medicine_name, category, batch_id, expiry_date, price, reorder_level)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        medicine.medicine_name,
        medicine.category,
        medicine.batch_id,
        medicine.expiry_date,
        medicine.price,
        medicine.reorder_level
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return True
