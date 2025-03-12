'''
The Josephus Problem is a famous theoretical problem related to recursion and combinatorics. It is defined as follows:
• There are n people standing in a circle, numbered from 0 to n − 1.
• Every k-th person is eliminated in a circular manner until only one person remains.
• Your task is to implement a recursive function to find the position of the last remaining person (zero-based index).
'''
def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n-1, k) + k) % n

print(josephus(6, 2))

INCOMPLETE