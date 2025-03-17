'''Implement a recursive solution for computing the nth Fibonacci number. Then, analyze its time complexity. Propose a more efficient solution and compare the two approaches.'''

"""Recursive Solution"""
print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(5))
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# 5
# Time Complexity: O(2^n)
# The time complexity of the recursive solution is exponential. This is because the function calls itself twice for each call, leading to a tree-like structure with 2^n nodes.

"""More Efficient Solution"""
print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def fibo_efficient(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c
print(fibo_efficient(5))
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# 5
for i in range(10):
    print(fibo_efficient(i), end = " ")
    # 0 1 1 2 3 5 8 13 21 34
# Time Complexity: O(n)
# The time complexity of the efficient solution is linear. This is because the function iterates n times to calculate the nth Fibonacci number.