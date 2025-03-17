# 8/3/25

'''
Serching Algorithms:-
    1. Linear Search Algorithm: It runs in O(n) time complexity. 
    2. Binary Search Algorithm: Works on a sorted list. It has a time complexity of O(log2(n)).
'''

"""Linear Search Algorithm"""
# l = [2,3,5,1,7,6,8,9]
# key = 7
# def lins(l, key):   
#     f = 0 
#     for i in range(len(l)):
#         if key == l[i]:
#             f = 1
#     if f == 1:
#         return (f"{key} found at index {i}")
#     return (f"{key} not found.")
# print(lins(l, key))


"""Binary Search Algorithm"""
# def binSearch(l, low, high, x):
#     if high >= low:
#         mid = (low+high)//2
#         if x == l[mid]:
#             return mid
#         elif x < l[mid]:
#             return binSearch(l, low, mid-1, x)
#         elif x > l[mid]:
#             return binSearch(l, mid+1, high, x)
#     else:
#         return -1
# l = [1,2,3,4,5,6,7,8,9]
# l.sort()
# x = 6
# res = binSearch(l, 0, len(l)-1, x)
# if res != -1:
#     print(f"{x} is found at index {res}")
# else:
#     print(f"{x} is not found")
# # 6 is found at index 5


'''Searching Algos:-'''
"""1. Selection Sort: O(n^2)"""
def selectionSort(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1, len(l)):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
        # print(l)
l = [4,5,3,2,1]
selectionSort(l)
print(l) # [1, 2, 3, 4, 5]

"""2. Insertion Sort: O(n^2)"""
def insertionSort(l):
    n = len(l)
    if n<1:
        return
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j>=0 and key<l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
l = [12,11,13,5,6]
insertionSort(l)
print(l) # [5, 6, 11, 12, 13]


"""2 Sum"""
def twoSum(ar, target):
    ar.sort()
    l, r = 0, len(ar)-1
    while(l<r):
        sum = ar[l]+ar[r]
        if sum == target:
            print(f"Target exists: [{ar[l]},{ar[r]}]")
            return [ar[l], ar[r]]
        elif sum < target:
            l += 1
        else:
            r -= 1
    else:
        print("Target does not exist!")

l = [1,2,3,1,5,6]
x = 5
twoSum(l, x)
    
"""
3. Merge Sort: It is a complex but a good sorting algorithm with complexity: O(n log2(n)) [log2 = log.base2]. 
                  It Follows the Divide and Conquer rule.
"""
def mergeSort(ar):
    if len(ar) <= 1:
        return ar
    mid = len(ar) // 2
    left = ar[:mid]
    right = ar[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while(left_index<len(left) and right_index<len(right)):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

print(mergeSort([4,5,6,1,3,7,0,9]))

