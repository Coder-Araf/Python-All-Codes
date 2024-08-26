a = (lambda a,b: a*a + 2*a*b +b*b)(5,6)
print(a)

#map
def  square(x):
    return x*x

num = [7,9,12,46,71,16]###this is map
m = list(map(square,num))
print(m)

result = list(filter(lambda x: x%2==0,num))
print(result)


#List Comprehensions

y = [x*x for x in num]
res = [x for x in num if x%2==0]
print(y)
print(res)
