class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} accepted. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal denied.")

'''
account = BankAccount("Dimash")

account.deposit(1000) => Deposit of $1000 accepted. Current balance: $1000
account.deposit(500)  => Deposit of $500 accepted. Current balance: $1500

account.withdraw(200)  => Withdrawal of $200 accepted. Current balance: $1300
account.withdraw(1500) => Insufficient funds. Withdrawal denied.
'''
