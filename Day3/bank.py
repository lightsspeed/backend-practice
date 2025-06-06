class BankAccount:
    def __init__(self, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    def deposit(self, amount: float) -> bool:
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Error: Deposit amount must be positive")
            return False
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")
        return True

    def withdraw(self, amount: float) -> bool:
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False
        if amount > self._balance:
            print("Error: Insufficient funds")
            return False
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")
        return True

    def check_balance(self) -> float:
        return self._balance

# Test cases
if __name__ == "__main__":
    account = BankAccount(100.0)
    print(f"Initial balance: {account.check_balance()}")  # Output: Initial balance: 100.0
    account.deposit(50.5)  # Output: Deposited 50.5. New balance: 150.5
    account.withdraw(30.0)  # Output: Withdrew 30.0. New balance: 120.5
    account.withdraw(200.0)  # Output: Error: Insufficient funds
    account.deposit(-10)  # Output: Error: Deposit amount must be positive
    print(f"Final balance: {account.check_balance()}")  # Output: Final balance: 120.5