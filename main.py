import sqlite3

# Function to create a new expense entry
def add_expense(date, description, category, amount):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Insert a new expense record
    insert_query = "INSERT INTO expenses (date, description, category, amount) VALUES (?, ?, ?, ?)"
    cursor.execute(insert_query, (date, description, category, amount))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to retrieve all expenses from the database
def get_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    select_query = "SELECT id, date, description, category, amount FROM expenses ORDER BY id"
    cursor.execute(select_query)
    expenses = cursor.fetchall()

    conn.close()

    return expenses


# Function to display all expenses
def show_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Retrieve all expenses
    select_query = "SELECT * FROM expenses"
    cursor.execute(select_query)
    expenses = cursor.fetchall()

    # Display the expenses
    for expense in expenses:
        print(expense)

    # Close the connection
    conn.close()

# Function to calculate the total expenses
def calculate_total_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Calculate the total expenses
    select_query = "SELECT SUM(amount) FROM expenses"
    cursor.execute(select_query)
    total_expenses = cursor.fetchone()[0]

    # Display the total expenses
    print("Total Expenses: $", total_expenses)

    # Close the connection
    conn.close()

# Function to delete an expense
def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Get the current expense details before deleting
    select_query = "SELECT * FROM expenses WHERE id = ?"
    cursor.execute(select_query, (expense_id,))
    expense = cursor.fetchone()

    # Delete the expense record
    delete_query = "DELETE FROM expenses WHERE id = ?"
    cursor.execute(delete_query, (expense_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Deleted Expense Details:")
    print("ID:", expense[0])
    print("Date:", expense[1])
    print("Description:", expense[2])
    print("Category:", expense[3])
    print("Amount: $", expense[4])

    # Reassign expense IDs starting from 1
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    reassign_query = "UPDATE expenses SET id = ? WHERE id = ?"
    expenses = get_expenses()
    for new_id, old_id in enumerate(expenses, start=1):
        cursor.execute(reassign_query, (new_id, old_id[0]))

    conn.commit()
    conn.close()

# Main program loop
while True:
    print("Expenses Tracker")
    print()
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Calculate Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter a description: ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: $"))

        add_expense(date, description, category, amount)
        print("Expense added successfully!")

    elif choice == "2":
        print("Expense List:")
        show_expenses()

    elif choice == "3":
        print("Calculating total expenses...")
        calculate_total_expenses()

    elif choice == "4":
        expense_id = input("Enter the expense ID to delete: ")
        delete_expense(expense_id)
        print("Expense", expense_id, "deleted successfully!")

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

    print("\n")

