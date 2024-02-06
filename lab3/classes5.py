class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, cash):
        self.balance += cash
        return self.balance
    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash
            return self.balance
        else:
            return "Error"

bank_account = Account("Eldana", 200)
print(bank_account.deposit(300))
print(bank_account.withdraw(600))
print(bank_account.withdraw(400))