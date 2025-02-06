'''13. WAP to create a custom exception class in Python that displays the balance and withdrawal amount
when an error occurs due to insufficient funds?'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class InsufficientFundsException(Exception):
    def __init__(self, bal, amt):
        self.bal = bal
        self.amt = amt
        super().__init__(f"Insufficient balance. Current balance: Rs.{self.bal}, Withdrawal amount: Rs.{self.amt}")
        
class BankAccount:
    def __init__(self, bal):
        self.bal = bal

    def withdraw(self, amt):
        if self.bal < amt:
            raise InsufficientFundsException(self.bal, amt)
        self.bal -= amt
        print(f"Withdrawal of Rs.{amt} successful. Current balance: Rs.{self.bal}")
    
    def deposit(self, amt):
        self.bal += amt
        print(f"Deposit of Rs.{amt} successful. Current balance: Rs.{self.bal}")

try:
    acc = BankAccount(1000)
    acc.withdraw(200)
    acc.withdraw(1200)
except InsufficientFundsException as e:
    print(e)

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Withdrawal of Rs.200 successful. Current balance: Rs.800
# Insufficient balance. Current balance: Rs.800, Withdrawal amount: Rs.1200
