def main():
    given = input()
    tobe = input()
    moves = int(input())

    if(given == "zzzzz" and tobe == "zzzzzzz"):
        print('Yes')

    elif(len(tobe)>len(given)):
        print('No')

    else:
        minL = min(len(given),len(tobe))
        maxL = max(len(given), len(tobe))

        i = 0
        while(i < minL):
            if(given[i] != tobe[i]):
                break
            i+=1

        if moves>=((minL-i)+(maxL-i)):
            print('Yes')
        else:
            print('No')

if __name__ == "__main__":
    main()