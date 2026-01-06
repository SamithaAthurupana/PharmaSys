from database import get_db_connection

def authenticate_user(username: str, password: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT user_id, username, password_hash, role
        FROM users
        WHERE username = %s AND is_active = TRUE
    """

    cursor.execute(query, (username,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        return None

    # Simple password check (academic purpose)
    if user["password_hash"] == password:
        return {
            "user_id": user["user_id"],
            "username": user["username"],
            "role": user["role"]
        }

    return None
