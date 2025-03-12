# 8/3/25

"""Named Tuple"""
'''1. Without Named Tuple'''
# def get_student():
#     return ("Danish", 1, "Python")
# stu = get_student()
# print(stu[2]) # Python

'''2. Using Named Tuple'''
# from collections import namedtuple
# Student = namedtuple('Student', 'name roll_no course')
# stu = Student("Danish", 1, "Python")
# print(stu.name) # Danish
# print(stu.roll_no) # 1
# print(stu.course) # Python

'''
Named Tuple has certain advantages such as:-
    1) Improved codereadability.
    2) Better Maintanability.
    3) Memory Efficiency -> Named tuples use less memory than regular classes.

There are some cases where named tuple should not be used, such as:-
    i) We need the methods from a class.
    ii) If the data needs to be mutable.
'''

'''1. Program without data classes'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __repr__(self):
#         return f"Person(name = '{self.name}', age = {self.age})"
#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.name == other.name and self.age == other.age
#         return False
# p1 = Person('Sid', 20)
# p2 = Person('Sid', 20)
# print(p1)
# print(p2)
# print(p1 == p2) # False

# p2 = Person('Sid', 21)
# print(p1)
# print(p2)
# print(p1 == p2) # False (without __eq__ if age is same, because objects have diff) / True (with __eq__)


'''
Data classes are decorator used in Python which automatically imlements __init__, __repr__ & __eq__ methods without defining them.
'''
'''2. Program with dataclass'''
# from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str
#     age: int
# p1 = Person('Sid', 20)
# p2 = Person('Sid', 21)
# print(p1)
# print(p2)
# print(p1 == p2) # False
# p2 = Person('Sid', 20)
# print(p1 == p2) # True
        
'Card Code'
from dataclasses import dataclass
from typing import ClassVar, List
@dataclass
class Card:
    FACES: ClassVar[List[str]] = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS: ClassVar[List[str]] = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    face: str
    suit: str
    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'
    def __str__(self):
        return f"{self.face} of {self.suit}"
    def __format__(self, format_spec):
        return f"{str(self): {format_spec}}"
    


from decimal import Decimal # capital Decimal is more accurate than float
class Accoount:
    def __init__(self, name, balance):
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00')
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError("Amount must be positive")
        self.balance += amount
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)

        