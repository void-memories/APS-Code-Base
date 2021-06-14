from collections import Counter

arr = []
n = 0

def union(u, v):
  global arr
  global n
  val = arr[u]
  for i in range(n):
    if(arr[i]==val):
      arr[i] = arr[v]


def main():
  global arr, n
  n,p = map(int, input().split())
  arr = [i for i in range(n)]
  while(p):
    p-=1
    u, v =map(int, input().split())
    union(u,v)

  sum = 0
  ans = 0
  dic = Counter(arr)
  for i in dic.values():
    ans += sum * i
    sum += i
  
  # print(arr)
  # print(Counter(arr).values())
  print(ans)


if __name__ == "__main__":
  main()
