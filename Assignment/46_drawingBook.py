def main():
    n = int(input())
    p = int(input())

    p=p//2
    n=n//2

    print(min(p, n-p))

if __name__ == "__main__":
    main()
