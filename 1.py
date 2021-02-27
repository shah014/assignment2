s1 ='google.com'
import operator
def fun(s1):
        a = {}
        for i in s1:
            keys = a.keys()
            if i in keys:
                a[i]+=1
            else:
                a[i] = 1
        a = dict(sorted(a.items(),key=operator.itemgetter(1),reverse=True))
        return a






