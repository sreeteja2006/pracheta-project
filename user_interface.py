import datetime

def display_menu():
    print("\nPersonal Finance Tracker Menu:")
    print("-------------------------------")
    print("1. Add Transaction")
    print("2. Print Transactions")
    print("3. Total Expense")
    print("4. Total Income")
    print("5. Balance")
    print("6. Save Transactions")
    print("7. Delete Transaction")
    print("8. Monthly Spending Summary")
    print("9. Exit")
    print("-------------------------------")

def handle_user_input(tracker):
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_transaction(tracker)
        elif choice == "2":
            print_transactions(tracker)
        elif choice == "3":
            print("Total Expense:", tracker.total_expense())
        elif choice == "4":
            print("Total Income:", tracker.total_income())
        elif choice == "5":
            print("Balance:", tracker.balance())
        elif choice == "6":
            tracker.save()
        elif choice == "7":
            delete_transaction(tracker)
        elif choice == "8":
            tracker.monthly_spending_summary()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def get_transaction_details():
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (income/expense): ").strip().lower()
    description = input("Enter the description: ")
    
    return {
        "amount": amount,
        "date": date,
        "category": category,
        "description": description
    }

def add_transaction(tracker):
    from utils import validate_date, validate_amount
    details = get_transaction_details()
    if not validate_date(details["date"]):
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    if details["category"] not in {"income", "expense"}:
        print("Invalid category. Use 'income' or 'expense'.")
        return
    
    tracker.add_transaction(details["amount"], details["date"], details["category"], details["description"])

def print_transactions(tracker):
    print("1. All Transactions")
    print("2. Transactions until specific date")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        tracker.print_all_transactions()
    elif choice == "2":
        date_str = input("Enter the date (YYYY-MM-DD): ")
        # Implement print_transactions_until_date method in FinanceTracker
        print("Not implemented yet.")
    else:
        print("Invalid choice.")

def delete_transaction(tracker):
    tracker.print_all_transactions()
    try:
        index = int(input("Enter the index of the transaction to delete: "))
        tracker.delete_transaction(index)
    except ValueError:
        print("Invalid index. Please enter a number.")
