'''
Write a recursive function to compute the sum of the first n natural numbers. Then, analyze its time complexity using Big O notation.
Tasks:
    (a) Implement a recursive function recursive sum(n) that computes the sum of the first n natural numbers using recursion.
    (b) Determine the base case and recursive step.
    (c) Write a function iterative sum(n) that computes the sum using a loop.
    (d) Compare the time complexity of both functions using Big O notation.
    (e) Explain why recursion is less efficient in this case compared to iteration.
'''
"(a)"
def recursive_sum(n):
    "(b)"
    if n == 1:
        return 1 # Base Case
    return n + recursive_sum(n-1) # Recursive Step
sum = recursive_sum(10)
print(sum) # 55

"(c)"
def iterative_sum(n):
    sum = 0 
    for i in range(1, n+1):
        sum += i
    return sum
sum = iterative_sum(10)
print(sum) # 55

"(d)"
# Time complexity of recursive_sum(n) is O(n) because it performs n recursive calls.
# Time complexity of iterative_sum(n) is O(n) because it performs n iterations in the loop.

"(e)"
# Recursion is less efficient in this case compared to iteration because each recursive call creates a new stack frame, which consumes memory and CPU time.
# In contrast, iteration uses a loop, which is more memory-efficient and faster.