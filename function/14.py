dict1 = {}
n = int(input("Enter the number of elements in dict1: "))
for i in range(n):
    key = int(input("Enter the key: "))
    value = int(input("Enter the value: "))
    dict1.update({key:value})
print(dict1)
def sortByValue():
    sortedValue = sorted(dict1.items(), key=lambda x: x[1])
    return sortedValue
print(dict(sortByValue()))



