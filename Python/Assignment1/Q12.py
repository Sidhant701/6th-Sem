'''12. WAP to overload the + operator to perform addition of two complex numbers using a custom Complex
class?'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __str__(self):
        return f'{self.real} + {self.imag}i'
    
c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
print(f"({c1}) + ({c2}) = {c3}")

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# (2 + 3i) + (4 + 5i) = 6 + 8i