#Function Peramiter
def add(a,b):
    print(a+b)


add(10,20)

#function returning peramiter

def rel(a,b):
    if a>b:
        return a
    else:
        return b
    

result = rel(50,60)
print(result)


#x argument

def student(*details):
    print(details)


student("shabbir", 22, 4.50)#one kind of tuples

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(50,60,90,70)

#xx argument

def stud(**info):
    print(info)

stud(name= "shabbir",id= 101)