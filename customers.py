customers = {

    "C101": {
        "name": "Aarav Sharma",
        "bank_name": "HDFC Bank",
        "branch": "Mumbai Main",
        "account_number": "1234567890",
        "upi_id": "aarav@hdfcbank",
        "balance": 25000,
        "income": 40000,
        "password": "demo123",
        "pin": "0428"
    },
    "C102": {
        "name": "Ananya Mehta",
        "bank_name": "ICICI Bank",
        "branch": "Pune Central",
        "account_number": "2345678901",
        "upi_id": "ananya@icici",
        "balance": 50000,
        "income": 65000,
        "password": "test123",
        "pin": "1234"
    },
    "C103": {
        "name": "Rohan Patel",
        "bank_name": "SBI",
        "branch": "Ahmedabad",
        "account_number": "3456789012",
        "upi_id": "rohan@sbi",
        "balance": 12000,
        "income": 30000,
        "password": "rohan123",
        "pin": "5678"
    },
    "C104": {
        "name": "Priya Nair",
        "bank_name": "Axis Bank",
        "branch": "Bangalore",
        "account_number": "4567890123",
        "upi_id": "priya@axis",
        "balance": 80000,
        "income": 90000,
        "password": "priya123",
        "pin": "9012"
    },
    "C105": {
        "name": "Kabir Verma",
        "bank_name": "HDFC Bank",
        "branch": "Delhi",
        "account_number": "5678901234",
        "upi_id": "kabir@hdfcbank",
        "balance": 5000,
        "income": 20000,
        "password": "kabir123",
        "pin": "3456"
    },
    "C106": {
        "name": "Isha Gupta",
        "bank_name": "Kotak Bank",
        "branch": "Jaipur",
        "account_number": "6789012345",
        "upi_id": "isha@kotak",
        "balance": 35000,
        "income": 45000,
        "password": "isha123",
        "pin": "7890"
    },
    "C107": {
        "name": "Aditya Rao",
        "bank_name": "SBI",
        "branch": "Hyderabad",
        "account_number": "7890123456",
        "upi_id": "aditya@sbi",
        "balance": 15000,
        "income": 35000,
        "password": "aditya123",
        "pin": "2468"
    },
    "C108": {
        "name": "Meera Shah",
        "bank_name": "ICICI Bank",
        "branch": "Surat",
        "account_number": "8901234567",
        "upi_id": "meera@icici",
        "balance": 100000,
        "income": 120000,
        "password": "meera123",
        "pin": "1357"
    },
    "C109": {
        "name": "Arjun Reddy",
        "bank_name": "Axis Bank",
        "branch": "Chennai",
        "account_number": "9012345678",
        "upi_id": "arjun@axis",
        "balance": 20000,
        "income": 28000,
        "password": "arjun123",
        "pin": "8642"
    },
    "C110": {
        "name": "Sana Khan",
        "bank_name": "HDFC Bank",
        "branch": "Nagpur",
        "account_number": "0123456789",
        "upi_id": "sana@hdfcbank",
        "balance": 60000,
        "income": 75000,
        "password": "sana123",
        "pin": "0987"
    }
}

def customer_exists(customer_id):
    return customer_id in customers

def get_customer(customer_id):
    return customers.get(customer_id)

def display_customer(customer_id):

    customer = get_customer(customer_id)

    if customer is None:
        print("Customer not found.")
        return

    account = customer["account_number"]
    masked_account = "*" * (len(account) - 4) + account[-4:]

    print("\n----- CUSTOMER DETAILS -----")
    print("Customer Name:", customer["name"])
    print("Bank:", customer["bank_name"])
    print("Branch:", customer["branch"])
    print("Account Number:", masked_account)
    print("UPI ID:", customer["upi_id"])
    print("Balance: Rs.", customer["balance"])
    print("Monthly Income: Rs.", customer["income"])
    print("----------------------------")

def validate_amount(raw_amount):
    raw_amount = raw_amount.strip()
    if raw_amount.isdigit():

        amount = int(raw_amount)

        if amount > 0:
            return amount
        else:
            return None

    else:
        return None

def validate_recipient(recipient, method):

    recipient = recipient.strip()
    method = method.lower()

    if method == "phone":

        if len(recipient) == 10 and recipient.isdigit():
            return True
        else:
            return False
    elif method == "qr":

        if recipient == "":
            return False

        parts = recipient.split("@")

        if len(parts) == 2:
            if parts[0] != "" and parts[1] != "":
                if " " not in recipient:
                    return True

        return False

    else:
        return False


