import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="250906", 
        database="quanly_benhnhan"
    )
    return conn
