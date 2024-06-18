year = int(input("enter year: "))
# leap year has to be divisible by 4, NOT divisible by 100
def year_check():
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("leap year")
    else:
        print("lunar, NOT LEAP YEAR")

year_check()