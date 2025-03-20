print('''Name: Sidhanta Barik, RegNo: 2241002049
-------------------------------------------------------''')

'''a'''
def fast_power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return fast_power(a, b/2) ** 2
    return a * fast_power(a, b-1)

'''b'''
# Base Case: if b is 0, return 1
# Recursive Step1: if b is even, return fast_power(a, b/2) ** 2
# Recursive Step2: if b is odd, return fast_power(a, b-1)

'''c'''
# Time complexity of the standard recursive method is O(b) because it performs b recursive calls.
# Time complexity of the optimized exponentiation by squaring method is O(log b) because it reduces the number of recursive calls significantly.

'''d'''
def fast_power_iterative(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result
# time complexity: O(log b) because it performs log b iterations in the loop.

'''e'''
a = 2
# b = 1000000 # This causes value to overflow
b = 1000000
res = fast_power(a, b)
res_itr = fast_power_iterative(a, b)
print(f"{a}^{b} (Using Recursion):-\n{res}")
print()
print(f"{a}^{b} (Using Loop):-\n{res}")
# Performance of the iterative method is better than the recursive method because it does not create new stack frames for each iteration.