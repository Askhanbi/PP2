# TASK 5    class

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print("ERROR404")

OWNER = str(input("OWNER: "))
BALANCE = int(input("You're balance: "))

account = BankAccount(OWNER, BALANCE)

account.deposit(int(input("Enter deposit count: ")))
account.withdraw(int(input("Enter withdraw count: ")))
