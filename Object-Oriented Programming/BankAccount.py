class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount: float) -> bool:
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                print("Insufficient balance.")
                return False
        else:
            print("Withdrawal amount must be grater than 0.")
            return False

    def get_balance(self) -> float:
        return self.balance


account = BankAccount("123456789", "Elon Musk", 100000000000000.0)
print(f"Initial balance: {account.get_balance()}")

account.deposit(50000000.0)
print(f"Balance after deposit: {account.get_balance()}")  

success = account.withdraw(3000000.0)
print(f"Balance after withdrawal: {account.get_balance()}")  

success = account.withdraw(200000000000000000000.0)
print(f"Balance after failed withdrawal: {account.get_balance()}")  # Output: Balance after failed withdrawal: 120.0