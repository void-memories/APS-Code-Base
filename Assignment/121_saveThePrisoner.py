def main():
  t = int(input())
  while(t):
    t-=1
    n, m, s = map(int, input().split())
    s-=1
    print((m+s)%n if (m+s)%n != 0 else n)

if __name__ == "__main__":
  main()

