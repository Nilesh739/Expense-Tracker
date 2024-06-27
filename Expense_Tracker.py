import json
from datetime import datetime

# Constants for the categories
CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Miscellaneous"]

# Function to load expenses from a file
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save expenses to a file
def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense(expenses):
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    date = input("Enter the date (YYYY-MM-DD) or press enter for today: ")
    date = date if date else datetime.now().strftime("%Y-%m-%d")
    
    print("Select a category:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    category_index = int(input("Enter the category number: ")) - 1
    category = CATEGORIES[category_index]
    
    expense = {
        "amount": amount,
        "description": description,
        "date": date,
        "category": category
    }
    expenses.append(expense)
    print("Expense added successfully!")

# Function to display expenses
def display_expenses(expenses):
    print("\nExpenses:")
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']} - {expense['description']}: ${expense['amount']:.2f}")

# Function to display monthly summary
def display_monthly_summary(expenses):
    summary = {}
    for expense in expenses:
        month = expense["date"][:7]  # Get the YYYY-MM part of the date
        if month not in summary:
            summary[month] = 0
        summary[month] += expense["amount"]
    
    print("\nMonthly Summary:")
    for month, total in summary.items():
        print(f"{month}: ${total:.2f}")

# Function to display category-wise summary
def display_category_summary(expenses):
    summary = {category: 0 for category in CATEGORIES}
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]
    
    print("\nCategory-wise Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

# Main function to run the Expense Tracker
def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View monthly summary")
        print("4. View category-wise summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            display_monthly_summary(expenses)
        elif choice == "4":
            display_category_summary(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
