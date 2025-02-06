'''9. Write a Python program demonstrating polymorphism by creating a base class Shape with a method
area(), and two subclasses Circle and Rectangle that override the area() method. Instantiate objects
of both subclasses and call the area() method. Explain how polymorphism simplifies working with
different shapes in an inheritance hierarchy'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi*self.r**2

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b
        
c1 = Circle(6)
print(f'Area of circle: {c1.area()}')
r1 = Rectangle(4, 5)
print(f'Area of rectangle: {r1.area()}')

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Area of circle: 113.09733552923255
# Area of rectangle: 20

'''
Ans: Polymorphism is the ability of an object to take on many forms. It simplifies working with different shapes in an inheritance hierarchy by allowing objects of different classes to be treated as objects of a common superclass. In this case, the base class Shape has a method area() that is overridden by the subclasses Circle and Rectangle. When the area() method is called on objects of the Circle and Rectangle classes, the appropriate implementation of the area() method is executed based on the type of the object. This allows for a more flexible and extensible design, as new shapes can be added to the hierarchy without modifying the existing code. 
'''