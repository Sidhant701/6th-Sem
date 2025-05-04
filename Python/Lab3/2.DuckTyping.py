# 4/3/25

'''
Duck Typing is Type System used in dynamic languages.
Eg: Python, PHP, JS, etc. where the type or the class of an object is less important than the method it defines. 
Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute. The name "duck typing" comes from the phrase "If it looks like a duck and it quacks like a duck, it must be duck".
'''

from decimal import Decimal

class WellPaidDuck:
    def __repr__(self):
        return 'I am a well-paid duck'
    def earnings(self):
        return Decimal('1_000_000.00')

wpd = WellPaidDuck()
print(wpd) # I am a well-paid duck
print(wpd.earnings()) # 1000000.00