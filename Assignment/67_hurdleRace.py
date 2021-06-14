def main():
  _, k = map(int, input().split())
  arr = list(map(int, input().split()))

  maxVal = max(arr)
  if maxVal > k:
    print(maxVal-k)
  else:
    print(0)

if __name__ == "__main__":
  main()