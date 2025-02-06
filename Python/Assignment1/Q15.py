'''15. How do Python data classes provide advantages over named tuples in terms of flexibility and func-
tionality? Give an example using python code.'''

'''
Ans:- 
Advantages of Python data classes over named tuples:
    1. Data classes support inheritance, default values, and type hints.
    2. Data classes provide built-in methods for comparison, hashing, and string representation.
    3. Data classes support mutable fields.
    4. Data classes can be used to create complex data structures, such as nested data classes.
    5. Data classes can be used to create data classes with custom initialization methods.
'''

# Example:-

'''Named tuple'''
# print('''Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------''')
# from collections import namedtuple
# Student = namedtuple("Student", ['name', 'age'])
# s1 = Student('Sid', 21)
# print(s1)
# try:
#     s1.age = 30
# except Exception as e:
#     print(e)

# # Student(name='Sid', age=21)
# # can't set attribute


'''Data class'''
print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')

from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    age: int = field(default=21)
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
s2 = Student('Sid', 21)
s2.display()
try:
    s2.age = 30
except Exception as e:
    print(e)
print("\nAfter changing age:-")
s2.display()

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Name: Sid, Age: 21

# After changing age:-
# Name: Sid, Age: 30