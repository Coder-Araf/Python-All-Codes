#constructor 
#class
class student:
    roll = ""
    gpa = ""
    #Constructor
    def __init__(self,degree,gpa):
        self.degree = degree
        self.gpa = gpa

    #inheritance
    def display(self):
        print(f"Degree : {self.degree}, GPA : {self.gpa}")



shabbir = student("HSC",4.50)
shabbir.display()

class A():
    def display1(self):
        print("I am display 1 class")

class B():
    def display2(self):
        print("I am display 2 class")

class C(A,B):#Multiple inheritance
    def display3(self):
        super().display1()
        super().display2()
        print("I am display 3 class")


obj = C()
obj.display3()