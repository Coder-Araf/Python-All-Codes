#class
class student:
    roll = ""
    gpa = ""
    #methods
    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")



rahim = student()
rahim.set_value(103,3.95)
# rahim.roll = 101
# rahim.gpa = 3.70
rahim.display()


# rahim = student()
# print(isinstance(rahim , student))
# rahim.roll = 101
# rahim.gpa = 3.70
# print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

# karim = student()
# print(isinstance(karim , student))
# karim.roll = 102
# karim.gpa = 4.50
# print(f"Roll : {karim.roll}, GPA : {karim.gpa}")