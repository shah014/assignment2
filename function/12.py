a = int(input("Enter arg: "))
n = int(input("Enter a unknown number: "))

def fun(n):
     return lambda a: a*n

ent_fun_n = fun(n)
print(ent_fun_n(a))


