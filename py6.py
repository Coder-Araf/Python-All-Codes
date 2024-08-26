num = list(range(10))
num1 = list(range(2,19))
num2 = list(range(2,50,2))

print(num2)

#for loop

for x in num:
    print(x)

li = [10,50,60,196,100,98]

sum = 0
for y in li:
    sum = sum + y

print(sum)

#series

n = int(input("Enter Your Digit: "))
sum = 1

for z in range(1,n+1,1):
    sum = sum * z

print(sum)