'''
The Josephus Problem is a famous theoretical problem related to recursion and combinatorics. It is defined as follows:
• There are n people standing in a circle, numbered from 0 to n − 1.
• Every k-th person is eliminated in a circular manner until only one person remains.
• Your task is to implement a recursive function to find the position of the last remaining person (zero-based index).

Tasks:
    (a) Implement a recursive function josephus(n, k) that returns the position of the last person remaining.
    (b) Identify the base case and the recursive formula.
    (c) Analyze the time complexity of your recursive implementation using Big O notation.
    (d) Implement an iterative version and compare its efficiency with the recursive version.
    (e) Test the function with different values of n and k.
'''


print('''Name: Sidhanta Barik, RegNo: 2241002049
-------------------------------------------------------''')

'''a'''
def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n-1, k) + k) % n
# print(josephus(5, 2))

'''b'''
# Base Case: When n is 1, return 0
# Recursive Formula: (josephus(n-1, k) + k) % n

'''c'''
# Time complexity of josephus(n, k) is O(n) because it performs n recursive calls.

'''d'''
def josephus_iterative(n, k):
    position = 0
    for i in range(2, n+1):
        position = (position + k) % i
    return position
# Time Complexity of josephus_iterative(n, k) is O(n) because it performs n iterations in the loop, but, it is more efficient than the recursive version because it does not create new stack frames for each iteration.

'''e'''
print(josephus(5, 2)) # 2
print(josephus_iterative(5, 2)) # 2



# Name: Sidhanta Barik, RegNo: 2241002049
# -------------------------------------------------------
# 2
# 2
