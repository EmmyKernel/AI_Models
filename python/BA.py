class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = float(initial_balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        fee = 20.0 if amount > 2000 else 0.0
        total_deduction = amount + fee

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif total_deduction > self._balance:
            print(f"Insufficient funds. Available: ${self._balance:.2f}, Required: ${total_deduction:.2f}")
        else:
            self._balance -= total_deduction
            fee_message = f" (including a ${fee:.2f} fee)" if fee > 0 else ""
            print(f"Withdrew: ${amount:.2f}{fee_message}. New Balance: ${self._balance:.2f}")


account = BankAccount(3000)
account.withdraw(2500) 
account.withdraw(100) 
