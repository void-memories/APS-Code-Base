from collections import Counter

def main():
  _ = int(input())
  arr = list(map(int, input().split()))

  counts = Counter(arr)
  # print(counts)
  
  keyVal = []
  for key,value in zip(counts.keys(), counts.values()) :
    keyVal.append((key, value))
  
  keyVal = sorted(keyVal, key = lambda x: x[0])
  keyVal = sorted(keyVal, key = lambda x: x[1], reverse=True)
  print(keyVal[0][0])

if __name__ == "__main__":
  main()