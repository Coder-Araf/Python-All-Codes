#File Type
file = open("student.txt","r+")
# print(file.readable())
text = file.read()
print(text)
print(len(text))
file.close

try:
    list = [20,0,30]
    result = list[0] / list[2]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by Zero Is not Possible")
# except IndexError:
#     print("Index Error")
finally:
    print("Successfully")


file = open("student.txt", "w")
file.write("\n mujse sadi karogeeee oooooo")
file.close()

try:
    num1 = int(input("Enter Your 1st number: "))
    num2 = int(input("Enter Your 2nd number: "))
    result2 = num1 / num2
    print(result2)

except (ValueError,ZeroDivisionError):
    print("You have entered Incorrect")

finally:
    print("Thanks")