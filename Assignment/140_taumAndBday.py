t = int(input())

while(t):
    t-=1
    #blackRequired, whiteRequired
    b, w = map(int, input().split())
    # costOfBlack, costOfWhite, diff
    bc, wc, z = map(int, input().split())
    
    a = [None, None, None]
    a[0] = b * bc + w * wc
    a[1] = b * bc + w * (bc + z) 
    a[2] = b * (wc + z)  + w * wc 
    print(min(a))
