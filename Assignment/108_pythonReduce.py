from functools import reduce
from fractions import Fraction

n = int(input())
nums = []
while n:
    n-=1
    a,b = map(int, input().split())
    nums.append(Fraction(f'{a}/{b}'))
print(*str((reduce(lambda x, y: x*y, nums))).split('/'))