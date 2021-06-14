def getLCS(s1, s2):
    lcs = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    s1 = ' '+s1
    s2 = ' '+ s2
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if(s1[i] == s2[j]):
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    print(lcs)
    return lcs[-1][-1] 

def main():
    s1 = input()
    s2 = input()
    print(getLCS(s1,s2))

if __name__ == "__main__":
    main()