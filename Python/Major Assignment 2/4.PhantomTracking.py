'''1'''
transactions = [120, 45, 300, 220, 90, 600, 130, 75, 800, 500, 350, 40]
threshold = 250
def phantom_tracking(transactions, threshold):
    if len(transactions) == 0:
        return []
    if transactions[0] > threshold:
        return [transactions[0]] + phantom_tracking(transactions[1:], threshold)
    return phantom_tracking(transactions[1:], threshold)
print(phantom_tracking(transactions, threshold))

'''2'''
def phantom_