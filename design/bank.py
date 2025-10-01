'''
Design a Bank class to manage customer accounts.

Support the following operations:

create_account(accountId: int, initialBalance: int) → creates a new account with a starting balance. If account exists, do nothing.

deposit(accountId: int, amount: int) → add money to an account. If the account doesn’t exist, ignore.

withdraw(accountId: int, amount: int) → subtract money from an account. If insufficient funds, reject (no overdraft).

transfer(fromId: int, toId: int, amount: int) → move funds between accounts. Fail if sender has insufficient funds or accounts don’t exist.

get_balance(accountId: int) -> int → return current balance, or -1 if the account doesn’t exist.
'''


class Account:

    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance 
    
    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            return False
        self.balance = new_balance

class Bank:
    def __init__(self):
        self.accounts = {} #dict id: Account
        self.ids = set()
    
    def create_account(self, accountId: int, initialBalance: int):
        if accountId in self.ids:
            return 

        self.accounts[accountId] = Account(initialBalance)
        self.ids.add(accountId)

    def deposit(self, accountId: int, amount: int):
        if accountId not in self.ids:
            return 
        self.accounts[accountId].add_balance(amount)
    
    def withdraw(self, accountId: int, amount: int):
        if accountId not in self.ids:
            return
        self.accounts[accountId].subtract_balance(amount)
    
    def get_balance(self, accountId):
        return self.accounts[accountId].get_balance()
    
    def transfer(self, account1, account2, amount):
        if account1 not in self.ids or account2 not in self.ids:
            return
        
        withdrawal = self.accounts[account1].subtract_balance(amount)
        if not withdrawal:
            return 
        self.accounts[account2].add_balance(amount)
    
    
    

bank = Bank()
bank.create_account(101, 500)
bank.deposit(101, 200)           # balance = 700
print(bank.get_balance(101))
bank.withdraw(101, 100)          # balance = 600
print(bank.get_balance(101))
bank.create_account(102, 300)

