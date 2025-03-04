# 4/3/25

"""Operator Overloading:-"""
class Complex:
    '''
    Complex class that represents a complex number with real and imaginary part.
    '''
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, right):
        return Complex(self.real + right.real, self.imag + right.imag)
    
    def __iadd__(self, right): #OPTIONAL
        self.real += right.real
        self.imag += right.imag
        
    def __sub__(self, right):
        return Complex(self.real - right.real, self.imag - right.imag)

    def __isub__(self, right):
        self.real -= right.real
        self.imag -= right.imag
        
    def __mul__(self, right):
        return Complex(self.real * right.real, self.imag * right.imag)

    def __truediv__(self, right):
        return Complex(self.real / right.real, self.imag / right.imag)

    def __floordiv__(self, right):
        return Complex(self.real // right.real, self.imag // right.imag)
    
    def __mod__(self, right):
        return Complex(self.real % right.real, self.imag % right.imag)
    
    def __repr__(self):
        """Return string representation for repr()."""
        return (f'({self.real} ' + 
                ('+' if self.imag >= 0 else '-') + 
                f' {abs(self.imag)}i)')

x = Complex(2,3)
y = Complex(4,5)
print(x+y)  # Output: (6 + 8i)
print(y-x) # Output: (2 + 2i)
print(x*y) # Output: (8 + 15i)
print(y/x) # Output: (2.0 + 1.6666666666666667i)
print(y//x) # Output: (2 + 1i)
print(x%y) # Output: (2 + 3i)

