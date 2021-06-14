def main():
    l = int(input())
    r = int(input())

    print(pow(2,len(bin(l^r))-2)-1)

if __name__ == "__main__":
    main()