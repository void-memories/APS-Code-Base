from collections import Counter

def main():
  _ = input()
  arr = list(map(int, input().split()))
  counts = Counter(arr)

  pairCount = 0
  for val in counts.values():
    pairCount += val//2
  
  print(pairCount)

if __name__ == "__main__":
    main()