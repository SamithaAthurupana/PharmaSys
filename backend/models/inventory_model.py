from database import get_db_connection

def get_inventory_with_medicines():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT 
            i.inventory_id,
            m.medicine_name,
            m.batch_id,
            m.expiry_date,
            m.reorder_level,
            i.quantity,
            i.last_updated
        FROM inventory i
        JOIN medicines m ON i.medicine_id = m.medicine_id
    """

    cursor.execute(query)
    inventory = cursor.fetchall()

    cursor.close()
    connection.close()

    return inventory


def create_inventory_item(inventory):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO inventory (medicine_id, quantity)
        VALUES (%s, %s)
    """

    values = (
        inventory.medicine_id,
        inventory.quantity
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return True


def update_inventory_quantity(inventory_id, quantity):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE inventory
        SET quantity = %s
        WHERE inventory_id = %s
    """

    cursor.execute(query, (quantity, inventory_id))
    connection.commit()

    cursor.close()
    connection.close()

    return True
