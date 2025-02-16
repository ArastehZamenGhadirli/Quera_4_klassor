class BankAccount:
    """
    bank account class with deposit and withdrawal method
    """

    def __init__(self, balance: int = 0):
        """
        Initializes a BankAccount with a balance.

        Parameters:
        balance (int, optional): The initial balance of the account. Default is 0.
        """

        self.balance: int = balance

    def deposit(self, amount: int):
        """
        Adds the specified amount to the account balance.

        Parameters:
        amount (int): The amount to deposit.
        """
        self.balance += amount

    def withdraw(self, amount: int):
        """
        Withdraws the specified amount from the account balance if sufficient funds are available.

        Parameters:
        amount (int): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount


account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.balance)  # 50
