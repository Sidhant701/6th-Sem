'''10. Implement the CommissionEmployee class with __init__ , earnings, and __repr__ methods. Include
properties for personal details and sales data. Create a test script to instantiate the object, display
earnings, modify sales data, and handle data validation errors for negative values.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class CommissionEmployee:
    def __init__(self, fName, lName, sales, cRate):
        self.fName = fName
        self.lName = lName
        self.sales = sales
        self.cRate = cRate

    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self, sales):
        if sales < 0:
            raise ValueError("Sales can't be negative.")
        self._sales = sales

    @property
    def cRate(self):
        return self._cRate
    @cRate.setter
    def cRate(self, cRate):
        if cRate < 0:
            raise ValueError("Commission rate can't be negative.")
        self._cRate = cRate

    @property
    def earnings(self):
        return self.sales * self.cRate
    
    def __repr__(self):
        return f'{self.fName} {self.lName}'
    
def test():
    emp = CommissionEmployee('Sidhanta', 'Barik', 10000, 0.6)
    print(emp)
    print(f'Earnings: Rs.{emp.earnings:.2f}')
    try:
        emp.sales = -1000
    except ValueError as e:
        print(e)
    try:
        emp.cRate = -0.05
    except ValueError as e:
        print(e)
    emp.sales = 15000
    emp.cRate = 0.8
    print(f'Earnings after modification: Rs.{emp.earnings:.2f}')

test()
        
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Sidhanta Barik
# Earnings: Rs.6000.00
# Sales can't be negative.
# Commission rate can't be negative.
# Earnings after modification: Rs.12000.00