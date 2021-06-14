n = int(input())
x = n
scores = []
while n:
    n -= 1
    l = [input()]
    l.append(float(input()))
    scores.append(l)
scores.sort()
scores.sort(key = lambda x : x[1])

# print(scores)
lowest = scores[0][1]
# print(lowest)
c = 1
while c<x and scores[c][1] == lowest :
    # print(c)
    c+=1
lowest = scores[c][1]
while c<x and scores[c][1] == lowest:
    print(scores[c][0])
    c+=1 
    