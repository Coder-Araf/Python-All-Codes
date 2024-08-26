num1 = int(input("Enter Your 1st Number: "))
num2 = int(input("Enter Your 2nd Number: "))
num3 = int(input("Enter Your 3rd Number: "))


if num1<num2:
    if num1<num3:
        print(f"Your Lower number is: {num1}")
elif num2<num3:
    if num2<num1:
        print(f"Your Lower number is: {num2}")
else:
    print(f"Your Lower number is: {num3}")