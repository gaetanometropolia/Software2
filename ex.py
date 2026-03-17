#Create a student class with at least 3 attributes + method that corresponds to student

# class Student:
#
#     def __init__(self, name, birth_year, grade):
#         self.name=name
#         self.birth_year=birth_year
#         self.grade=int(grade)
#
#     def study(self, subject):
#         print(f"{self.name} is now studying {subject} for their grade {self.grade} exam.")
#         return
#
#
# user_name = input("Enter a name")
# user_birth_year = int(input("Enter a year" ))
# user_grade = int(input("enter a grade"))
#
# student = Student(user_name, user_birth_year, user_grade)
#
# student.study("Math")

class Student:

    def __init__(self, name, birth_year, grade):
        self.name=name
        self.birth_year=birth_year
        self.grade=int(grade)

    def intro(self):
        print (f"Hello my name is {self.name} and I am born {self.birth_year}")

students = []
number = int(input("enter number of student objects you want to create"))

for i in range (number):
    print(f"Enter details for student {i+1}")
    name= input("Enter a name")
    birth_year = int(input("enter a year"))
    grade = int(input("enter grade"))

    s=Student(name, birth_year, grade)
    students.append(s)

print("\nStudent Details are given below.:")

for s in students:
    s.intro()