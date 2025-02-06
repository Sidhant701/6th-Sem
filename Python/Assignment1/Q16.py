'''16. Write a Python program that demonstrates unit testing directly within a function’s docstring using the
doctest module. Create a function add(a, b) that returns the sum of two numbers and includes multiple
test cases in its docstring. Implement a way to automatically run the tests when the script is executed.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def add(a, b):
    """
    Test Cases
    ==========
    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    >>> add(-1, -1)
    -2
    >>> add(1.4, 4.2)
    5.6
    """
    return a+b

if __name__ == "__main__":
    import doctest
    res = doctest.testmod()
    if res.failed > 0:
        print(f"Tests failed: {res.failed}")
    else:
        print("All tests passed")
    print(f"Total tests: {res.attempted}")


# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# All tests passed
# Total tests: 4