def getMultipleSum(n, r):
  m = r//n
  s = m*(m+1)//2
  return n*s


def main():
  t = int(input())
  while t:
    t-=1
    r = int(input())
    r -= 1
    s1 = getMultipleSum(3,r)
    s2 = getMultipleSum(5,r)
    s3 = getMultipleSum(15,r)
    print(int(s1+s2-s3))

if __name__ == "__main__":
  main()