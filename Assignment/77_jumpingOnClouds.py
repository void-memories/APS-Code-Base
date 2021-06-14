n = int(input())

arr = input().split()
c = 0
pos = 0
while(pos+2 < n):
    # print(pos, arr[pos+2])
    if(arr[pos+2] == '0'):
        pos += 2
    else:
        pos += 1
    c+=1

# print(n,pos)
if(pos+1!=n):
    c+=1
print(c)