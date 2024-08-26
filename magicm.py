class Bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __eq__(self, others) -> bool:
        return self.name == others.name and self.color == others.color

    def __str__(self):###Megic Call 
        return (f"Name: {self.name}, Color: {self.color}")

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}")


bike1 = Bike("Yamaha","Red")
bike2 = Bike("Yamaha","Red")
print(bike1)
print(bike1==bike2)
        