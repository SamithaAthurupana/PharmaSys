from database import get_db_connection

def create_sale(sale):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # 1️⃣ Calculate total
        total_amount = sum(item.quantity * item.price for item in sale.items)
        total_amount -= sale.discount

        # 2️⃣ Insert into sales table
        sale_query = """
            INSERT INTO sales (user_id, total_amount, discount)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sale_query, (sale.user_id, total_amount, sale.discount))
        sale_id = cursor.lastrowid

        # 3️⃣ Insert sale items + update inventory
        for item in sale.items:
            cursor.execute(
                """
                INSERT INTO sale_items (sale_id, medicine_id, quantity, price)
                VALUES (%s, %s, %s, %s)
                """,
                (sale_id, item.medicine_id, item.quantity, item.price)
            )

            # Reduce stock
            cursor.execute(
                """
                UPDATE inventory
                SET quantity = quantity - %s
                WHERE medicine_id = %s
                """,
                (item.quantity, item.medicine_id)
            )

        connection.commit()
        return sale_id, total_amount

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()
