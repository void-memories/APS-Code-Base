s = input()
n = int(input())

aCount = s.count('a')
sLen = len(s)

print((n//sLen)*aCount + s[:n%sLen].count('a'))