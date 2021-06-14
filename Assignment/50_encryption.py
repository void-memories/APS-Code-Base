import math

def main():
    string = input()
    charCount = len(string)
    # print(charCount)

    rows = math.floor(math.sqrt(charCount))
    cols = math.ceil(math.sqrt(charCount))


    if (rows*cols)<charCount:
        rows=cols=max(rows, cols)

    # print(rows, cols)
    string += (" "*(charCount%cols))

    op=""

    for j in range(cols):
        letterCount = 0
        for _ in range(rows):
            try:
                op += string[letterCount+j]
            except:
                op += " "
            letterCount+=cols
        op += " "
    print(op.replace("  "," "))


if __name__ == "__main__":
    main()
