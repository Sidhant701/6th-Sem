'''Write a recursive function that takes a number n as an input parameter and prints n-digit strictly icreasing numbers.'''
def print_increasing(n):
    if n == 0:
        return 0
    print(print_increasing(n))
    return print_increasing(n-1) + 9*(10**(n-1))
    
print_increasing(2)