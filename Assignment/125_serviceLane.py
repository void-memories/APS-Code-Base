_, t = map(int, input().split())
arr = list(map(int, input().split()))

while(t):
    t-=1
    l,r = map(int, input().split())
    print(min(arr[l:r+1]))