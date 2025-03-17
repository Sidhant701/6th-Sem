print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def mergeSort(ar):
    if len(ar) <= 1:
        return ar
    mid = len(ar) // 2
    left = ar[:mid]
    right = ar[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

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

ar = ['apple', 'orange', 'banana', 'grape']
print(f"Before sorting: {ar}")
l = 0
r = len(ar)-1
print(f"After sorting:  {mergeSort(ar)}")
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Before sorting: ['apple', 'orange', 'banana', 'grape']
# After sorting:  ['apple', 'banana', 'grape', 'orange']

"Better Approach: Changes the actual list"
# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#     L = [0] * (n1)
#     R = [0] * (n2)
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#     i = 0     # Initial index of first subarray
#     j = 0     # Initial index of second subarray
#     k = l     # Initial index of merged subarray
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# def mergeSort(arr, l, r):
#     if l < r:
#         m = l+(r-l)//2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         merge(arr, l, m, r)

# ar = ['apple', 'orange', 'banana', 'grape']
# print(f"Before sorting: {ar}")
# l = 0
# r = len(ar)-1
# mergeSort(ar, l, r)
# print(f"After sorting:  {ar}")
# Before sorting: ['apple', 'orange', 'banana', 'grape']
# After sorting:  ['apple', 'banana', 'grape', 'orange']