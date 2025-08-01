import os
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv



# If .env is in the same folder as this script
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

dataBase = mysql.connector.connect(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("Database elderco created successfully!")