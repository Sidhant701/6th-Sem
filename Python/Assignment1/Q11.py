'''11. What is duck typing in Python? Write a Python program demonstrating duck typing by creating a
function describe() that accepts any object with a speak() method. Implement two classes, Dog and
Robot, each with a speak() method. Pass instances of both classes to the describe() function and
explain how duck typing allows the function to work without checking the object’s type.'''

'''
Ans: Duck typing is a concept related to dynamic typing, where the type or class of an object is determined by the presence of certain methods and properties, rather than the actual type of the object itself. In other words, if an object behaves like a duck (i.e., it has a quack() method), then it is a duck.
'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')

def describe(obj):
    obj.speak()

class Dog:
    def speak(self):
        print('Bhow Bhow')

class Robot:
    def speak(self):
        print('Beep Bop')

d1 = Dog()
r1 = Robot()
describe(d1)
describe(r1)

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Bhow Bhow
# Beep Bop