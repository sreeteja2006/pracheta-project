import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False
