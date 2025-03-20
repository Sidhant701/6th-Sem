print('''Name: Sidhanta Barik, RegNo: 2241002049
-------------------------------------------------------''')

'''a'''
def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n-1, k) + k) % n

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
n,k = 5, 2
print(f"Last Person Remaining using Recursion: {josephus(n, k)}") # 2
print(f"Last Person Remaining using Loop: {josephus_iterative(n, k)}") # 2

n,k = 7, 3
print(f"Last Person Remaining using Recursion: {josephus(n, k)}") # 3
print(f"Last Person Remaining using Loop: {josephus_iterative(n, k)}") #3