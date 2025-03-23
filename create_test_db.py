import os
import MySQLdb
import dotenv

dotenv.load_dotenv()

db_name = os.getenv("TEST_DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT", 3306))

print(f"Connecting to MySQL with USER={db_user}, HOST={db_host}, PORT={db_port}")

# Connect to MySQL Server (without selecting a DB)
connection = MySQLdb.connect(
    user=db_user, 
    passwd=db_password,
    host=db_host,
    port=db_port
)

cursor = connection.cursor()

# Create database if it does not exist
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")

# Ensure the user exists and update the password separately
cursor.execute(f"CREATE USER IF NOT EXISTS '{db_user}'@'localhost' IDENTIFIED WITH mysql_native_password BY '{db_password}';")

# Grant privileges to the user
cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost';")
cursor.execute("FLUSH PRIVILEGES;")

cursor.close()
connection.close()

print(f"Database `{db_name}` ensured with proper user access!")
