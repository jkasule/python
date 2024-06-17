operator = input("enter operator, ie + - * /:  ")
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    if num2 == 0:
        print("IMPOSSIBLE")
    else:
        result = num1 / num2
        print(round(result, 3))

else:
    print("operator " + str(operator) + " is not a valid operator")
