from itertools import combinations

def strOr(st1, st2, l):
    res = 0
    for i in range(l):
        res += 1 if (st1[i]=="1" or st2[i]=="1") else 0
    return res

n, m = map(int, input().split())

skills = []
for i in range(n):
    skills.append(input())

combs = list(combinations(skills, 2))

ml = 0
cnt = 0

for c in combs:
    cz = strOr(c[0],c[1], m)
    if ml < cz:
        ml = cz
        cnt = 1
    elif cz == ml:
        cnt += 1

print(ml)
print(cnt)