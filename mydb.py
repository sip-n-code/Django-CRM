import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="StupidMysql10",
    # database="elderco"
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("Database elderco created successfully!")