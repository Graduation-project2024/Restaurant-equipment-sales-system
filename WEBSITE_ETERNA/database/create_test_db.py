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

# Drop and create the test database
try:
    cursor.execute("DROP DATABASE IF EXISTS test_restaurant_equipment_sales_system")
    cursor.execute("CREATE DATABASE test_restaurant_equipment_sales_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    print("Test database created successfully")
    
    # Switch to the test database
    cursor.execute("USE test_restaurant_equipment_sales_system")
    
    # Create roles table
    cursor.execute("""
        CREATE TABLE roles (
            rol_id INT AUTO_INCREMENT PRIMARY KEY,
            rol_name VARCHAR(255) NOT NULL
        )
    """)
    
    # Create users table
    cursor.execute("""
        CREATE TABLE users (
            usr_id INT AUTO_INCREMENT PRIMARY KEY,
            rol_id INT,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255),
            password VARCHAR(255) NOT NULL,
            FOREIGN KEY (rol_id) REFERENCES roles(rol_id)
        )
    """)
    
    # Create customers table (empty, just to satisfy migrations)
    cursor.execute("""
        CREATE TABLE customers (
            cust_id INT AUTO_INCREMENT PRIMARY KEY,
            cust_name VARCHAR(255) NOT NULL,
            cust_phone VARCHAR(20),
            cust_email VARCHAR(255),
            cust_username VARCHAR(255) NOT NULL UNIQUE,
            cust_password VARCHAR(255) NOT NULL
        )
    """)
    
    print("Tables created successfully")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close the connection
cursor.close()
connection.close()
