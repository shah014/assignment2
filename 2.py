# output: #Pyon  #PyPy #empty
s1='Python'
def fun(s1):
        if len(s1) < 2:
            return ''

        return s1[0:2] + s1[-2:]
print(fun(s1))
print(fun('Py'))
print(fun('w'))



