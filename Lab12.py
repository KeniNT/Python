import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

CSV_FILE = "Expenses.csv"
BACKUP_FILE = "expenses_backup.csv"

# Initialize CSV file with headers if it does not exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Date', 'Description', 'Amount', 'Category'])

# 1. Expense Logging
def log_expense():
    name = input("Enter your name: ")
    date = input("Enter the date (DD-MM-YYYY): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., groceries, utilities, entertainment): ")

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, description, amount, category])
    print("Expense logged successfully.")

# 2. Expense Analysis
def expense_analysis():
    data = pd.read_csv(CSV_FILE)
    total_by_member = data.groupby("Name")["Amount"].sum()
    average_daily = data["Amount"].sum() / data["Date"].nunique()
    
    print("\nTotal Expenses by Member:")
    print(total_by_member)
    print(f"\nAverage Daily Expense for Household: {average_daily:.2f}")

# 3. Expense Trends
def expense_trends():
    data = pd.read_csv(CSV_FILE)
    data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")
    daily_expenses = data.groupby("Date")["Amount"].sum().cumsum()
    
    plt.figure(figsize=(10, 5))
    plt.plot(daily_expenses.index, daily_expenses.values, marker='o')
    plt.title("Cumulative Expense Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Expense")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 4. Expense Categorization (handled in log_expense function)

# 5. Expense Reporting
def expense_report():
    data = pd.read_csv(CSV_FILE)
    total_by_member = data.groupby("Name")["Amount"].sum()
    total_by_category = data.groupby("Category")["Amount"].sum()
    
    print("\nMonthly Expense Report")
    print("Total Expenses by Member:")
    print(total_by_member)
    
    print("\nExpense Breakdown by Category:")
    print(total_by_category)
    
    # Monthly comparison bar chart
    data["Date   "] = pd.to_datetime(data["Date"]).dt.to_period("M")
    monthly_expenses = data.groupby("Month")["Amount"].sum()
    
    monthly_expenses.plot(kind='bar', color='skyblue')
    plt.title("Monthly Expenses Comparison")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.show()

# 6. Expense Budgeting
def set_budget():
    budget_data = {}
    while True:
        category = input("Enter category to set budget for (or 'done' to finish): ")
        if category.lower() == 'done':
            break
        budget = float(input(f"Enter budget for {category}: "))
        budget_data[category] = budget
    
    print("Budget set successfully.")
    return budget_data

def check_budget(budget_data):
    data = pd.read_csv(CSV_FILE)
    category_expenses = data.groupby("Category")["Amount"].sum()
    print("\nBudget Analysis:")
    
    for category, budget in budget_data.items():
        spent = category_expenses.get(category, 0)
        remaining = budget - spent
        print(f"{category}: Budget = {budget}, Spent = {spent}, Remaining = {remaining}")
        if remaining < 0:
            print(f"Warning: Budget exceeded for {category} by {-remaining}")

# 7. Data Backup and Restore
def backup_data():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r') as src, open(BACKUP_FILE, 'w') as dest:
            dest.write(src.read())
        print("Backup created successfully.")
    else:
        print("No data to backup.")

def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, 'r') as src, open(CSV_FILE, 'w') as dest:
            dest.write(src.read())
        print("Data restored successfully.")
    else:
        print("No backup found.")

# Menu-Driven Interface
def menu():
    initialize_csv()
    budget_data = {}

    while True:
        print("\n--- Household Expense Management ---")
        print("1. Log Expense")
        print("2. Analyze Expenses")
        print("3. Show Expense Trends")
        print("4. Generate Expense Report")
        print("5. Set Budget")
        print("6. Check Budget")
        print("7. Backup Data")
        print("8. Restore Data")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            log_expense()
        elif choice == '2':
            expense_analysis()
        elif choice == '3':
            expense_trends()
        elif choice == '4':
            expense_report()
        elif choice == '5':
            budget_data = set_budget()
        elif choice == '6':
            check_budget(budget_data)
        elif choice == '7':
            backup_data()
        elif choice == '8':
            restore_data()
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu-driven program
menu()
