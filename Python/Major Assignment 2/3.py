'''
You need to implement an efficient recursive function to compute ab (where a is the base and b is the exponent) using Exponentiation by Squaring, which reduces the number of recursive calls significantly.
Tasks:
    (a) Implement a recursive function fast power(a, b) that computes ab using divide and conquer.
    (b) Identify the base case and the recursive formula:
        • If b is even, use the identity: a^b = (a^(b/2))^2
        • If b is odd, use the identity: a^b = a * a^(b−1)
    (c) Compare the time complexity of the standard recursive method (O(b)) and the optimized exponentiation by squaring method (O(log b)).
    (d) Implement an iterative version of exponentiation by squaring and compare it with the recursive implementation.
    (e) Test your function with large values of b (e.g., a = 2, b = 1000000) and observe the performance.
'''


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
b = 10000
res = fast_power(a, b)
res_itr = fast_power_iterative(a, b)
print(res)
print()
print(res_itr)
