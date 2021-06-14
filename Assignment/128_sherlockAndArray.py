t = int(input())
while(t):
    t-=1
    n = int(input())
    arr = list(map(int, input().split()))
    if(n == 1):
        print("YES")
        break

    preArr  = [arr[0]]
    for i in range(1, n):
        preArr.append(preArr[i-1]+arr[i])
    
    flag = "NO"
    for i in range(1, n):
        if(preArr[i-1] == preArr[-1]-preArr[i]):
            # print(i)
            flag = "YES"
            break
    
    print(flag)

    # print(preArr)