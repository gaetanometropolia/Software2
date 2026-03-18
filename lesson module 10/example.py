
class Student:
    def __init__ (self, name):
        self.name=name

    def respond_to_name(self):
        print (f"{self.name}: Present!")

class Teacher:
    def __init__(self, name, subject ):
        self.name = name
        self.subject = subject
        self.attendance_record = []

    def checkin(self,student):
        self.attendance_record.append(student)
        print(f"{student.name} is present at {teacher.name} {teacher.subject} lesson")
        return

#I make the students
student1=Student("Mario")
student2= Student("Gianni")

teacher = Teacher("Kirpal", "Python")

teacher.checkin(student1)
teacher.checkin(student2)



