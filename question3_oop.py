class Student:
    #1. we have created a class student 

     #2 whenever any object for eg student1 created this __in__it constructor willbe intitiated 
     #3 we have passed three arguments name roll_number marks
     
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

    def check_pass(self):
        if self.marks >= 40:
            print("Status: Passed")
        else:
            print("Status: Failed")


# Creating  an  object
student1 = Student("Rahul", 12, 65)

# Calling  methods
student1.display_details()
student1.check_pass()