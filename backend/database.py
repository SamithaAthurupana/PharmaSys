import mysql.connector
from mysql.connector import Error

import pyodbc

def get_db_connection():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\SQLEXPRESS;"
            "DATABASE=pharmacy_db;"
            "Trusted_Connection=yes;"
        )
        return connection
    except Exception as e:
        print("Database connection error:", e)
        return None
