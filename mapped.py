class ATM:
    def __init__(self, location, branch_name):
        self.location = location
        self.branch_name = branch_name

    def show(self):
        print(f"ATM Location: {self.location}, Branch: {self.branch_name}")

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def update_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

    def verify_pin(self, input_pin):
        return self.pin == input_pin

class Transaction:
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.amount = 0
        self.status = "Pending"

    def initiate_withdrawal(self, account, amount):
        if account.update_balance(amount):
            self.amount = amount
            self.status = "Successful"
            print(f"Transaction Successful! Withdrawn Amount: ${amount}")
        else:
            self.status = "Failed"
            print("Transaction Failed: Insufficient Funds.")

# Example usage
atm = ATM("Downtown", "InfoSuper Branch")
account = Account("123456789", 500)  # Example account with $500 balance
user = User("user01", "1234")  # Example user with a PIN
transaction = Transaction("TXN001")

# Simulate ATM interaction
atm.show()
pin_input = input("Enter your PIN: ")
if user.verify_pin(pin_input):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Insufficient funds.Enter a valid amount.")
    else:
        transaction.initiate_withdrawal(account, amount)
else:
    print("Invalid PIN.")