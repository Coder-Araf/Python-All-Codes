# #inheritance and Overriding
# class shape:
#     #constructor
#     def __init__(self,demi1,demi2):
#         self.demi1 = demi1
#         self.demi2 = demi2
#     #inheritance
#     def area(self):
#         print("I am shape for class methods")

# #overriding
# class tringle(shape):
#     def area(self):
#         area = 0.5 * self.demi1 * self.demi2
#         print("Area of Tringle : ",area)

# class rectangle(shape):
#     def area(self):
#         area = self.demi1 * self.demi2
#         print("Area of Rectangle : ",area)

# s1 = tringle(20,30)
# s2 = rectangle(20,30)
# s1.area()
# s2.area()

from abc import ABC,abstractmethod
#inheritance and Overriding
class shape(ABC):
    #constructor
    def __init__(self,demi1,demi2):
        self.demi1 = demi1
        self.demi2 = demi2
    #inheritance
    @abstractmethod
    def area(self):
       pass

#overriding
class tringle(shape):
    def area(self):
        area = 0.5 * self.demi1 * self.demi2
        print("Area of Tringle : ",area)

class rectangle(shape):
    def area(self):
        area = self.demi1 * self.demi2
        print("Area of Rectangle : ",area)

s1 = tringle(20,30)
s2 = rectangle(20,30)
s1.area()
s2.area()