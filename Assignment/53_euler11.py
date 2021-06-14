def main():
    arr = []
    for _ in range(20):
        arr.append(list(map(int, input().split())))
    
    # for _ in range(3):
    #     arr.append([float('-inf')]*23)
    
    # print(arr)

    maxProd = float('-inf')

    for i in range(20):
        for j in range(20):
            hProd = 1
            vProd = 1
            drProd = 1
            dlProd = 1
            # horizontal product
            try:
                for k in range(4):
                    hProd *= arr[i][j+k]
            except:
                hProd = 0
            # vertical product
            try:
                for k in range(4):
                    vProd *= arr[i+k][j]
            except:
                vProd = 0
            #diagonal right product
            try:
                for k in range(4):
                    drProd *= arr[i+k][j+k]
            except:
                drProd = 0
            try:
                for k in range(4):
                    dlProd *= arr[i-k][j+k]
            except:
                dlProd = 0
            
            maxProd = max(maxProd, hProd, vProd, drProd, dlProd)
    
    print(maxProd)
            
            


if __name__ == "__main__":
    main()