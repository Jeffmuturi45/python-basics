class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You withdrew {amount}. New balance is {self.balance}")
        else:
            print(f"Insufficient funds! Your account balance is: {self.balance}")

    def get_balance(self):
        return self.balance

# object
account = BankAccount("John", 10000)
account.deposit(100)
account.withdraw(2000)

print(f"Your current account balance is: {account.get_balance()}")
