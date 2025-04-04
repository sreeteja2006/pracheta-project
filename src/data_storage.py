import json

def load_transactions():
    try:
        with open("transactions.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_transactions(transactions):
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)
    print("Transactions saved successfully.")
