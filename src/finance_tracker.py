import datetime
from data_storage import load_transactions, save_transactions
from utils import validate_date, validate_amount

class FinanceTracker:
    def __init__(self):
        self.transactions = load_transactions()

    def add_transaction(self, amount, date, category, description):
        if not validate_date(date):
            print("Invalid date format. Use YYYY-MM-DD.")
            return
        if category not in {"income", "expense"}:
            print("Invalid category. Use 'income' or 'expense'.")
            return
        
        self.transactions.append({
            "amount": amount,
            "date": date,
            "category": category,
            "description": description
        })
        print("Transaction added successfully.")

    def print_all_transactions(self):
        if not self.transactions:
            print("No transactions found.")
        for i, transaction in enumerate(self.transactions):
            print(f"{i}. {transaction}")

    def total_expense(self):
        return sum(t["amount"] for t in self.transactions if t["category"] == "expense")

    def total_income(self):
        return sum(t["amount"] for t in self.transactions if t["category"] == "income")

    def balance(self):
        return self.total_income() - self.total_expense()

    def monthly_spending_summary(self):
        summary = {}
        for transaction in self.transactions:
            if transaction["category"] == 'expense':
                month = datetime.datetime.strptime(transaction["date"], "%Y-%m-%d").strftime("%Y-%m")
                summary[month] = summary.get(month, 0) + transaction["amount"]
        
        print("Monthly Spending Summary:")
        for month in sorted(summary.keys()):
            print(f"{month}: {summary[month]:.2f}")

    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            confirm = input(f"Are you sure you want to delete this transaction? {self.transactions[index]} (yes/no): ")
            if confirm.lower() == "yes":
                del self.transactions[index]
                print("Transaction deleted successfully.")
            else:
                print("Transaction deletion cancelled.")
        else:
            print("Invalid index.")

    def save(self):
        save_transactions(self.transactions)

def main():
    from user_interface import handle_user_input
    tracker = FinanceTracker()
    handle_user_input(tracker)
    tracker.save()

if __name__ == "__main__":
    main()
