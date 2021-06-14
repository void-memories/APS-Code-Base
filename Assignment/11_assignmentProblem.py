from math import inf
from collections import Counter

def checkNthBitSet(num, n):
  num = bin(num)[2:]
  try:
    return num[-n]==1
  except:
    return False

def getNumSetBits(num):
  num = bin(num)[2:]
  counts = Counter(num)
  return counts['1']

def assignmentTask(costMatrix, n):
  dp = [inf for _ in range(1<<n)]
  dp[0] = 0

  for mask in range((1<<n)-1):
    numSetBits = getNumSetBits(mask)
    for j in range(n):
      if not checkNthBitSet(mask, j):
        tempTaskAssignment = mask | 1<<j
        dp[tempTaskAssignment] = min(dp[tempTaskAssignment], dp[mask]+costMatrix[numSetBits][j])
  
  return dp[(1<<n)-1]


def main():
  costMatrix = [[3,2,7],[5,1,3],[2,7,2]]
  print(assignmentTask(costMatrix,3))

if __name__ == "__main__":
  main()
