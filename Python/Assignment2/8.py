'''Implement QuickSort'''


print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def quick_sort(ar, s, e):
    if s<e:
        p = partition(ar, s, e)
        quick_sort(ar, s, p-1)
        quick_sort(ar, p+1, e)
    
def partition(ar, s, e):
    # Making first element as pivot
    pivot = ar[s]

    # changed from here
    i = s
    for j in range(s+1, e+1):
        if ar[j] < pivot:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]
    ar[i], ar[s] = ar[s], ar[i]
    return i


    # i = s-1
    # for j in range(s, e):
    #     if ar[j] < pivot:
    #         i += 1
    #         ar[i], ar[j] = ar[j], ar[i]
    # ar[i+1], ar[e] = ar[e], ar[i+1]
    # return i+1
    
ar = [37, 2, 6, 4, 89, 8, 10, 12, 68, 45]
print("Before sorting:", ar)
s = 0
e = len(ar)-1
quick_sort(ar, s, e)
print("After sorting: ", ar)
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Before sorting: [37, 2, 6, 4, 89, 8, 10, 12, 68, 45]
# After sorting:  [2, 4, 6, 8, 10, 12, 37, 45, 68, 89]