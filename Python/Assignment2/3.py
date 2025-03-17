'''Write a recursive function that takes a number n as an input parameter and prints n-digit strictly increasing numbers.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def print_increasing(n, curr="", lastDig = 0):
    if n==0:
        if curr!="":
            print(curr, end = " ")
        else:
            print("Invalid Input!!")
        return
    for i in range(lastDig+1, 10):
        print_increasing(n-1, curr + str(i),i)

n = int(input("Enter no. of digits: "))
print(f"\n{n}-digit strictly increasing numbers:-")
print_increasing(n)
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Enter no. of digits: 2

# 2-digit strictly increasing numbers:-
# 12 13 14 15 16 17 18 19 23 24 25 26 27 28 29 34 35 36 37 38 39 45 46 47 48 49 56 57 58 59 67 68 69 78 79 89