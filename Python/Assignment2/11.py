print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def merge(l, r):
    i = j = 0
    ml = []
    while i<len(l) and j<len(r):
        if l[i] < r[j]:
            ml.append(l[i])
            i += 1
        else:
            ml.append(r[j])
            j += 1
    ml.extend(l[i:])
    ml.extend(r[j:])
    return ml

sortedList1 = [1,3,5,7]
sortedList2 = [2,4,6,8]
mergedList = merge(sortedList1, sortedList2)

print(f"Sorted List 1: {sortedList1}")
print(f"Sorted List 1: {sortedList2}")
print(f"Sorted Merged List: {mergedList}")

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Sorted List 1: [1, 3, 5, 7]
# Sorted List 1: [2, 4, 6, 8]
# Sorted Merged List: [1, 2, 3, 4, 5, 6, 7, 8]