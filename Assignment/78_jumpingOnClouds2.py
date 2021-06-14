n, s = map(int, input().split())

arr = list(map(int, input().split()))

pos = s % n
e = 99
if arr[pos] == 1:
    e -= 2

while(pos != 0 and e != 0):
    e -= 1
    pos = (pos + s) % n
    if arr[pos] == 1:
        e -= 2

print(e)