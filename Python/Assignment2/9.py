# You are given the following list of famous personalities with their net worth:
# • Elon Musk: $433.9 Billion
# • Jeff Bezos: $239.4 Billion
# • Mark Zuckerberg: $211.8 Billion
# • Larry Ellison: $204.6 Billion
# • Bernard Arnault & Family: $181.3 Billion
# • Larry Page: $161.4 Billion
# Develop a program to sort the aforementioned details on the basis of net worth using
# a. Selection sort
# b. Bubble sort
# c. Insertion sort.
# The final sorted data should be the same for all cases. After you obtain the sorted data, present the
# result in the form of the following dictionary:
# {’name1’:networth1, ’name2’:networth2,...}


print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class Billionaires:
    def __init__(self, name, net_worth):
        self.name = name
        self.net_worth = net_worth 

    def __str__(self):
        return f'{self.name}: {self.net_worth} Billion'

    # def __repr__(self):
    #     return f'{self.name}: {self.net_worth} Billion'

    def __lt__(self, other):
        return self.net_worth < other.net_worth

    def __gt__(self, other):
        return self.net_worth > other.net_worth

def insertionSort(l):
    n = len(l)
    if n<1:
        return
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j>=0 and key < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

def selectionSort(l):
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
    return l

def bubbleSort(l):
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

bData = {
    'Elon Musk': 433.9,
    'Jeff Bezos': 239.4,
    'Mark Zuckerberg': 211.8,
    'Larry Ellison': 204.6,
    'Bernard Arnault & Family': 181.3,
    'Larry Page': 161.4
}
l = [Billionaires(k, v) for k, v in bData.items()]

isl = insertionSort(l[:]) # copy of l is required to avoid modification of og list
ssl = selectionSort(l[:])
bsl = bubbleSort(l[:])

'Converting it to dictionary and displaying the sorted list'
# d1 = d2 = d3 = {} # WRONG(d1,d2,d3 refer to the same dictionary)
isd = {x.name: x.net_worth for x in isl}
ssd = {x.name: x.net_worth for x in ssl}
bsd = {x.name: x.net_worth for x in bsl}

print(f"Insertion Sort:-\n{isd}\n")
print(f"Selection Sort:-\n{ssd}\n")
print(f"Bubble Sort:-\n{bsd}")
# Insertion Sort:-
# {'Larry Page': 161.4, 'Bernard Arnault & Family': 181.3, 'Larry Ellison': 204.6, 'Mark Zuckerberg': 211.8, 'Jeff Bezos': 239.4, 'Elon Musk': 433.9}

# Selection Sort:-
# {'Larry Page': 161.4, 'Bernard Arnault & Family': 181.3, 'Larry Ellison': 204.6, 'Mark Zuckerberg': 211.8, 'Jeff Bezos': 239.4, 'Elon Musk': 433.9}

# Bubble Sort:-
# {'Larry Page': 161.4, 'Bernard Arnault & Family': 181.3, 'Larry Ellison': 204.6, 'Mark Zuckerberg': 211.8, 'Jeff Bezos': 239.4, 'Elon Musk': 433.9}
