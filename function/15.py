from functools import reduce
list1 = input("Enter a list: ")
sp_list1 = list1.split()
for i in range(0,len(sp_list1)):
    sp_list1[i] = int(sp_list1[i])
print(sp_list1)
int_sort = lambda x:x/2>0
result = filter(int_sort,sp_list1)
print(list(result))
