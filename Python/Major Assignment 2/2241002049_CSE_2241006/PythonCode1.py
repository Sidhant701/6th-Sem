print('''Name: Sidhanta Barik, RegNo: 2241002049
-------------------------------------------------------''')

"(a)"
def recursive_sum(n):
    if n == 1:
        return 1 # Base Case
    return n + recursive_sum(n-1) # Recursive Step
n = 10
sum = recursive_sum(n)
print(f"Sum of first {n} natural nos. using Recursion = {sum}") # 55

"(b)"
# Base Case: When n is 1, return 0
# Recursive Step: Return n + recursive_sum(n-1)

"(c)"
def iterative_sum(n):
    sum = 0 
    for i in range(1, n+1):
        sum += i
    return sum
n = 10
sum = iterative_sum(n)
print(f"Sum of first {n} natural nos. using Loop = {sum}") # 55

"(d)"
# Time complexity of recursive_sum(n) is O(n) because it performs n recursive calls.
# Time complexity of iterative_sum(n) is O(n) because it performs n iterations in the loop.

"(e)"
# Recursion is less efficient in this case compared to iteration because each recursive call creates a new stack frame, which consumes memory and CPU time.
# In contrast, iteration uses a loop, which is more memory-efficient and faster.