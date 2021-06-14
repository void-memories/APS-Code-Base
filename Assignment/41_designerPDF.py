def main():
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  heights = list(map(int, input().split()))

  string = input()
  string = string.strip()
  # print(string)

  mappings = {}
  for i in range(26):
    mappings[letters[i]] = heights[i]

  # print(mappings)

  mH = 0
  for l in string:
    # print(mappings[l])
    if(mappings[l]>mH):
      mH = mappings[l]
  
  print(mH*len(string))

if __name__ == "__main__":
  main()