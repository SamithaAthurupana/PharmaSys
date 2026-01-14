import pyodbc

def get_db_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=pharmacy_db_final;"
        "Trusted_Connection=yes;"
    )
