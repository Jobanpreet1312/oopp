class Student_Details:

    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.cname = input("Enter Your College Name: ")
        self.roll = int(input("Enter Your Roll Number: "))


class Temp(Student_Details):
    def display(self):
        print("============ Student Details are ==========")
        print("Name: ", self.name)
        print("College Name:", self.cname)
        print("Roll number:", self.roll)


obj1 = Temp()
obj1.display()