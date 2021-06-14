from math import sqrt, floor
def juggler(n):
    print(n)
    a = n
    while(a!=1):
        b = None
        if(a&1==0):
            b = floor(sqrt(a))
        else:
            b = floor(sqrt(a)*sqrt(a)*sqrt(a))
        a = b
        print(b)

juggler(9)