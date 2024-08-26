roll = [101,102,103,104,105,106,107,108]
name = ["Shabbir","Araf","Jubayer","Roman","Amin","Arafat","Abrar","Arfan"]

print(list(zip(roll,name,"Abababab")))

#factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    

print(fact(5))