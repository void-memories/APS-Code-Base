CHANGE_YEAR = 1919


def isLeapYear(year):
    if year < CHANGE_YEAR:
        if(year % 4 == 0):
            return True
        else:
            return False
    else:
        if(year % 400 == 0):
            return True
        elif(year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False


def main():
    year = int(input())

    if(year==1918):
        print("26.09.1918")
        return

    if isLeapYear(year):
        print(f"12.09.{year}")
    else:
        print(f"13.09.{year}")

if __name__ == "__main__":
    main()
