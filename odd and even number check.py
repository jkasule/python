n = int(input("enter new number for check: "))

if n % 2 != 0:
    print("Weird")
elif 2<=n<=5:
    print("not weird")
elif 6<=n<=20:
    print("weird")
elif n>20:
    print("not weird")
else:
    print("wierd")