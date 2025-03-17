'Given an array of N elements, not necessarily in ascending order, devised an algorithm to find the kth largest one. It should run in O(N )time on random inputs.'

"""Using BUCKETSORT"""
# def bucketSort(ar):
#     n = len(ar)
#     maxV = max(ar)
#     minV = min(ar)
#     bucket = [[] for _ in range(n)]
#     for i in range(n):
#         bucket[(ar[i]-minV)*(n-1)//(maxV-minV)].append(ar[i])
#     for i in range(n):
#         bucket[i].sort()
#     k = 0
#     for i in range(n):
#         for j in range(len(bucket[i])):
#             ar[k] = bucket[i][j]
#             k += 1
#     return ar

# def kth_largest(arr, k):
#     arr = bucketSort(arr)
#     return arr[-k]
# # time complexity: O(n^2) in worst case
# print(kth_largest([3, 2, 1, 5, 4], 2))


"""Using QUICKSELECT"""
print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
import random
def quickSelect(ar, k):
    if ar:
        # random pivot(to avoid worst case, still, rarely, worst case may occur)
        pivot = ar[random.randint(0, len(ar)-1)]
        left = [x for x in ar if x < pivot]
        right = [x for x in ar if x > pivot]
        if k == len(right) + 1:
            return pivot
        elif k <= len(right):
            return quickSelect(right, k)
        else:
            return quickSelect(left, k - len(right) - 1)
    return None
# time complexity: O(n) in avg case, 
#                  O(n^2) in worst case
print(quickSelect([3, 2, 1, 5, 4], 2)) 
# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# 4