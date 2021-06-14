from collections import Counter

def main():
  _ = int(input())
  arr = list(map(int, input().split()))
  
  counts = Counter(arr)

  uniqNums = list(counts.keys())
  uniqNums.sort()
  maxLen = 0
  for i in range(len(uniqNums)):
    maxLen=max(maxLen, counts[uniqNums[i]])
    if(i!=len(uniqNums)-1):
      if uniqNums[i+1]-uniqNums[i]==1:
        maxLen = max(maxLen, counts[uniqNums[i]]+counts[uniqNums[i+1]])
  
  print(maxLen)
  
if __name__ == "__main__":
  main()