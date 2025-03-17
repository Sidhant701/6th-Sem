# Do not give output. Explain only.

n = 3

"""a"""
def example1(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
example1(n)
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
'time complexity: O(n^2)'
# The time complexity of the nested loops is quadratic. This is because the inner loop runs n times for each iteration of the outer loop, leading to n^2 iterations in total.

print()

"""b"""
for i in range(n):
    print(i)
# 0
# 1
# 2
'time complexity: O(n)'
# The time complexity of the loop is linear. This is because the loop runs n times, where n is the input to the function.

print()

"""c"""
def recursive_function(n):
    if n <= 1:
        return 1
    return recursive_function(n - 1) + recursive_function(n - 1)
print(recursive_function(n))
# 4
'time complexity: O(2^n)'
# The time complexity of the recursive function is exponential. This is because the function calls itself twice for each call, leading to a tree-like structure with 2^n nodes.