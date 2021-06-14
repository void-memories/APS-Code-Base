def getSumPair(arr, target):
    p1 = 0
    p2 = 1
    count = 0
    while(p2 < len(arr)):
        s = arr[p2] - arr[p1]
        # print(s)
        if(s == target):
            count += 1
            p2 += 1
        elif(s<target):
            p2+=1
        else:
            p1+=1
    return count

def main():
    _, t = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    print(getSumPair(arr, t))

if __name__ == "__main__":
    main()