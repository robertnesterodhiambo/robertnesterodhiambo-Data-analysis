import mysql.connector

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host="falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password="1QAZ2wsx",
    database="cis3368DB"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Check if the table already exists
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
table_exists = False
for table in tables:
    if 'drinks' in table:
        table_exists = True
        break

# If the table doesn't exist, create it
if not table_exists:
    create_table_query = """
    CREATE TABLE drinks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        drinkname VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        color VARCHAR(50) NOT NULL,
        description TEXT
    )
    """
    cursor.execute(create_table_query)
    print("Table 'drinks' created successfully!")
else:
    print("Table 'drinks' already exists.")

# Commit changes and close connection
connection.commit()
connection.close()




# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host= "falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password= "1QAZ2wsx",
    database="cis3368DB"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# List of drinks entries to be inserted into the table
drinks_entries = [
    ("Latte", 3.99, "Brown", "A creamy coffee drink"),
    ("Espresso", 2.49, "Black", "A strong coffee shot"),
    ("Cappuccino", 4.29, "Brown", "Coffee with foamed milk"),
    ("Mocha", 4.49, "Brown", "Coffee with chocolate"),
    ("Iced Tea", 2.99, "Amber", "Cold tea"),
    ("Lemonade", 3.49, "Yellow", "Refreshing lemon drink"),
    ("Smoothie", 5.99, "Green", "Blended fruit drink"),
    ("Soda", 1.99, "Clear", "Carbonated beverage"),
    ("Water", 0.99, "Clear", "Plain drinking water"),
    ("Juice", 3.49, "Various", "Assorted fruit juice")
]

# SQL query to insert entries into the drinks table
insert_query = """
INSERT INTO drinks (drinkname, price, color, description)
VALUES (%s, %s, %s, %s)
"""

# Execute the insert queries for each entry
for drink_entry in drinks_entries:
    cursor.execute(insert_query, drink_entry)

# Commit changes and close connection
connection.commit()
connection.close()

print("Entries added to the 'drinks' table successfully!")



# Function to fetch all contents of the drinks table
def fetch_drinks(cursor):
    cursor.execute("SELECT * FROM drinks")
    drinks = cursor.fetchall()
    return drinks

# Function to calculate total price based on selected drinks
def calculate_total(drinks, selected_drink_ids):
    total_price = 0
    for drink in drinks:
        if drink[0] in selected_drink_ids:
            total_price += drink[2]  # Add price of the selected drink
    return total_price

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
     host= "falode3368-1.ch6kyu62mcnp.us-east-1.rds.amazonaws.com",
    user="Falode",
    password= "1QAZ2wsx",
    database="cis3368DB"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Fetch all contents of the drinks table
drinks = fetch_drinks(cursor)

# Print all contents of the drinks table
print("Contents of the 'drinks' table:")
for drink in drinks:
    print(drink)

# Prompt the user to enter the ID of the drink they want
selected_drink_ids = []
while True:
    drink_id = input("Enter the ID of the drink you want (or 'done' to finish): ")
    if drink_id.lower() == 'done':
        break
    selected_drink_ids.append(int(drink_id))

# Calculate total price based on selected drinks
total_price = calculate_total(drinks, selected_drink_ids)
print("Total price for selected drinks:", total_price)

# Close connection
connection.close()
