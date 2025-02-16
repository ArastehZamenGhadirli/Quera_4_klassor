class BankAccount:
    def __init__(self,balance:int=0,amount:int):
        self.balance=balance
        self.amount=amount
        
    def deposit(self,balance,amount):
        self.balance+=self.amount
        
    def withdraw(self,balance,amount):
        if(self.balance)