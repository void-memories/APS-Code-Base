def main():
  _, ind = map(int,input().split())
  arr = list(map(int, input().split()))
  charged = int(input())
  arr.pop(ind)
  actualCharge = sum(arr)//2
  # print(actualCharge)
  if(actualCharge == charged):
    print("Bon Appetit")
  else:
    print(charged-actualCharge)

if __name__ == "__main__":
    main()