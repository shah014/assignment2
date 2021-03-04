# to print the even no from the given list
# let's use filter for this

list1 = input("Enter a list: ")
l_s = list1.split()
for i in range(len(l_s)):
   l_s[i] = int(l_s[i])
print(l_s)

#now let's make use of lambda and filter(since we have a condn to meet)

even = lambda x:x % 2 == 0
res = list(filter(even,l_s))
print(f"Even no from the list are : {res} ")