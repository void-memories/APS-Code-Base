from functools import reduce

def main():
    _ = int(input())
    nums = input().split()

    print(reduce(lambda x,y: x^int(y),nums,0))

if __name__ == "__main__":
    main()