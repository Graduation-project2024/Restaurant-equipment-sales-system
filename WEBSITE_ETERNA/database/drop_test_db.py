import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3305,
    user='root',
    password='012053aA',
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci'
)

# Create a cursor
cursor = connection.cursor()

# Drop the test database if it exists
try:
    cursor.execute("DROP DATABASE IF EXISTS test_restaurant_equipment_sales_system")
    print("Test database dropped successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close the connection
cursor.close()
connection.close()