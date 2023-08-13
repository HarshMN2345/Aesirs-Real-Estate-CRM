import mysql.connector
dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uncharted4"
)
cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE AesirsCRM")
print("Database Created Successfully")
