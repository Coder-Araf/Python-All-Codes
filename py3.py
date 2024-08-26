num1 = 50
num2 = 60

print(num1 if num1<num2 else num2)#Ternary Operator


#Logical operator
num3 = 80
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)


ch = input("Enter Your Letter: ")

if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Vowel")
else:
    print(
        "Consonent"
    )

# i = 1
# while i <= 100:
#     print(i)
#     i+=2

