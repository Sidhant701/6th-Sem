print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

print(gcd(125,625)) 
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# 125