def fun(s1):
    a = s1[0]
    s1 = s1.replace(a ,'$')
    s1 = a + s1[1:]
    return s1

print(fun('restart'))