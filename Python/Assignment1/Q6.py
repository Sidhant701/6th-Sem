'''6. Write a Python program that uses private attributes for creating a BankAccount class. Implement
methods to deposit, withdraw, and display the balance, ensuring direct access to the balance attribute is
restricted. Explain why using private attributes can help improve data security and prevent accidental
modifications.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class BankAccount:
    def __init__(self, AC_no, bal = 0.0):
        self.AC_no = AC_no
        self.__bal = bal
    
    def deposit(self, amt):
        self.__bal += amt
        print(f"Deposited Rs.{amt} successfully!!")

    def withdraw(self, amt):
        if amt > self.__bal:
            print("Insufficient funds!!")
            print(f"Unable to withdraw Rs.{amt}!!")
        else:
            self.__bal -= amt
            print(f"Withdrawn Rs.{amt} successfully!!")

    def display(self):
        print(f"Account Number: {self.AC_no}")
        print(f"Balance = Rs.{self.__bal:.2f}\n")

ac1 = BankAccount(2049, 5000.75)
ac1.deposit(500.5)
ac1.display()
ac1.withdraw(2000)
ac1.display()
ac1.__bal = 1000 # This will not modify the balance attribute as it is a private attribute
ac1.display()

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Account Number: 2049
# Balance = Rs.5000.75

# Deposited Rs.500.5 successfully!!
# Account Number: 2049
# Balance = Rs.5501.25

# Withdrawn Rs.2000 successfully!!
# Account Number: 2049
# Balance = Rs.3501.25

# Account Number: 2049
# Balance = Rs.3501.25


# Using private attributes can help improve data security and prevent accidental modifications by restricting direct access to the attributes from outside the class. This ensures that the attributes can only be accessed and modified through the class methods, which allows for better control over the data and prevents unauthorized changes. It also enforces data hiding and protect the internal state of the class from external interference, improving the overall security and integrity of the program.