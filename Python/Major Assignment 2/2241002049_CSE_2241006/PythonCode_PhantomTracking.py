print('''Name: Sidhanta Barik, RegNo: 2241002049
-------------------------------------------------------''')

'''1'''
def findSusTransactions(trans, thresh):
    return [t for t in trans if t > thresh]

transactions = [120, 45, 300, 220, 90, 600, 130, 75, 800, 500, 350, 40]
threshold = 250
susTransactions = findSusTransactions(transactions, threshold)
print(f"High Value Transactions: {susTransactions}")


'''2'''
def SelectionSort(ar):
    for i in range(len(ar)):
        minIdx = i
        for j in range(i+1, len(ar)):
            if ar[j] < ar[minIdx]:
                minIdx = j
        ar[i], ar[minIdx] = ar[minIdx], ar[i]
    return ar
sorted_susTransactions = SelectionSort(susTransactions)
print(f"Sorted Transactions: {sorted_susTransactions}")


'''3'''
def BinarySearch(ar, x):
    l, r = 0, len(ar)-1
    while l <= r:
        mid = (l+r)//2
        if ar[mid] == x:
            return True
        elif ar[mid] < x:
            l = mid+1
        else:
            r = mid-1
    return False
search_amount = 500
found = BinarySearch(sorted_susTransactions, search_amount)
if found:
    print(f"{search_amount} is found")
else:
    print(f"{search_amount} is not found")


'''4'''
def mergeSort(ar):
    if len(ar) <= 1:
        return ar
    mid = len(ar) // 2
    l = ar[:mid]
    r = ar[mid:]

    l = mergeSort(l)
    r = mergeSort(r)

    return merge(l, r)

def merge(l, r):
    merged = []
    i = 0
    j = 0
    while(i < len(l) and j < len(r)):
        if l[i] <= r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    merged.extend(l[i:])
    merged.extend(r[j:])
    return merged

transactions = [120, 45, 300, 220, 90, 600, 130, 75, 800, 500, 350, 40]
sorted_transactions = mergeSort(transactions)
print(f"Sorted Transaction History: {sorted_transactions}")