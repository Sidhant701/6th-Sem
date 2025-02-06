'''2. Create a custom Python class for managing a bank account with basic functionalities like deposit and withdrawal?'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class BankAccount:
    def __init__(self, AC_no, bal = 0.00):
        self.AC_no = AC_no
        self.bal = bal
    
    def deposit(self, amt):
        self.bal += amt
        print(f"Deposited Rs.{amt} successfully!!")

    def withdraw(self, amt):
        if amt > self.bal:
            print("Insufficient funds!!")
            print(f"Unable to withdraw Rs.{amt}!!")
        else:
            self.bal -= amt
            print(f"Withdrawn Rs.{amt} successfully!!")

    def display(self):
        print(f"Account Number: {self.AC_no}")
        print(f"Balance = Rs.{self.bal:.2f}\n")

a1 = BankAccount(2049, 10)
a1.deposit(1500)
a1.display()
a1.withdraw(500)
a1.display()
a1.withdraw(2000)
a1.display()

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Deposited Rs.1500 successfully!!
# Account Number: 2049
# Balance = Rs.1510.00

# Withdrawn Rs.500 successfully!!
# Account Number: 2049
# Balance = Rs.1010.00

# Insufficient funds!!
# Unable to withdraw Rs.2000!!
# Account Number: 2049
# Balance = Rs.1010.00