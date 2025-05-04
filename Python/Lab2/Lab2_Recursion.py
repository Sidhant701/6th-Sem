# 25/2/25

'''
Recursion: It is the process of defining something in terms of itself. There are 3 Steps:-
    i) Define a function f()
    ii) Create a base case.
    iii) use "f" to find "f".
'''

"Factorial"
# def fact(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n = int(input("Enter a number: "))
# print(f"Factorial of {n} = {fact(n)}")
# # Enter a number: 6
# # Factorial of 6 = 720



"Fibonacci Sequence"
# def fibo(n):
#     if n<0:
#         print("Enter a +ve number!!")
#         return
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# n = int(input("Enter choice: "))
# print(f"Fibonacci number at position {n} = {fibo(n)}")
# # Enter choice: 7
# # Fibonacci number at position 7 = 13


"Length of String"
# def lent(s):
#     if s=="":
#         return 0
#     else:
#         return 1+lent(s[1:])
# s = input(("Enter a string: "))
# print(f"Length of string = {lent(s)}")
# # Enter a string: Sid B
# # Length of string = 5


"String Reversal"
# def rev(s):
#     if s=="":
#         return s
#     else:
#         return rev(s[1:]) + s[0] #Both statements work
#         # return s[-1] + rev(s[:-1]) #Both statements work
# s = input("Enter a String: ")
# print(f"Reversed string = {rev(s)}")
# # Enter a String: Sid B
# # Reversed string = B diS


"GCD of 2 Nos."
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print(f"GCD of {a} and {b} = {gcd(a,b)}")
# # Enter 1st number: 18
# # Enter 2nd number: 12
# # GCD of 18 and 12 = 6


"Palindrome"
# def isPalindrome(s):
#     if len(s) < 2:
#         return True
#     elif s[0] == s[-1]:
#         return isPalindrome(s[1:-1])
#     else:
#         return False
# s = input("Enter a String: ")
# s = s.lower()
# if isPalindrome(s):
#     print(f'"{s}" is Palindrome')
# else:
#     print(f'"{s}" is not Palindrome')
# # Enter a String: racecar
# # "racecar" is Palindrome
# # Enter a String: racecars
# # "racecars" is not Palindrome


"Sum of nos. in a list"
# def listSum(l, n):
#     if n == 0:
#         return 0
#     else:
#         return l[n-1] + listSum(l, n-1)
# l = eval(input("Enter a list: "))
# n = len(l)
# print(f"Sum of list: {listSum(l, n)}")
# # Enter a list: [1,2,3,4,5]
# # Sum of list: 15