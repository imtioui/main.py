import sqlite3

# Create a connection to the database
conn = sqlite3.connect('expenses.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Define the expenses table
create_table_query = ("""
CREATE TABLE IF NOT EXISTS expenses 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE,
    Description TEXT,
    Category TEXT,
    Amount REAL
)
""")

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()