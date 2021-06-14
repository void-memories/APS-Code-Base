def main():
  b, _, _ = map(int, input().split())
  kb = list(map(int, input().split()))
  ms = list(map(int, input().split()))
  kb.sort()
  ms.sort()

  max = 0

  for kp in kb:
    for mp in ms:
      if (kp + mp) <= b and (kp + mp) > max :
        max = (kp + mp)
  if(max!=0):
    print(max)
  else:
    print(-1)

if __name__ == "__main__":
  main()