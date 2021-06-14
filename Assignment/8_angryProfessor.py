def main():
    t = int(input())
    while(t):
        t -= 1
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        count = 0
        for num in arr:
            if(num <= 0):
                count += 1
        
        if(count>=k):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()
