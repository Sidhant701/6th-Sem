'''8. Write a Python program that defines a base class Vehicle with attributes make and model, and a
method display_info(). Create a subclass Car that inherits from Vehicle and adds an additional at-
tribute num_doors. Instantiate both Vehicle and Car objects, call their display_info() methods, and
explain how the subclass inherits and extends the functionality of the base class.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Make: {self.make}, Model: {self.model}')

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f'Number of doors: {self.num_doors}')

v1 = Vehicle('Lexus', 'LFA')
v1.display_info()
print()
c1 = Car('Lexus', 'LX', 5)
c1.display_info()

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Make: Lexus, Model: LFA

# Make: Lexus, Model: LX
# Number of doors: 5


# Explanation:
# Car class inherits Vehicle class and extends it by adding an additional attribute "num_doors".
# Car class overrides display_info() method of Vehicle class to display additional attribute num_doors.
# When display_info() method of Car class is called, it first calls the display_info() method of the Vehicle class using super() method to display make and model attributes, and then it displays the num_doors attribute of the Car class.

