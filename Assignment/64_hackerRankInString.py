n = int(input())
str = 'hackerrank'
while n:
    n-=1
    s = input()
    count = 0
    for i in s:
        if str[count] == i:
            count += 1
            if count == 10:
                break
    
    if(count == 10):
        print("Yes")
    else:
        print("No")