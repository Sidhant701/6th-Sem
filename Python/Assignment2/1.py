print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def power(base, exponent):
    if exponent < 0:
        return power(1/base, -exponent)
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)   
print(power(4,3)) 
print(power(4,-2)) 
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# 64
# 0.0625