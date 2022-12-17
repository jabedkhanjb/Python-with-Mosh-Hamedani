class Student_information:
    def __init__(self, name, id, department, mobile):
        self.student_name = name
        self.student_id = id
        self.student_department = department
        self.student_mobile = mobile

    def details(self):
        print("\n")
        asterisk = ""
        P_asterisk = asterisk.center(57, "*")
        print(P_asterisk)
        print("*             The Millennium University                 *")
        print("*                   Student ID Card                     *")
        print(P_asterisk)
        print("*     Student name : " + self.student_name,)
        print("*     Id : " + self.student_id)
        print("*     Department : " + self.student_department)
        print("*     Cell : " + self.student_mobile)
        print(P_asterisk)
        print("\n")


student1 = Student_information(name=input("Enter your name : "), id=input("Enter your ID : "),
                               department=input("Enter your department name : "),
                               mobile=input("Enter your mobile number : +88"))
student1.details()
student2 = Student_information(name=input("Enter your name : "), id=input("Enter your ID : "),
                               department=input("Enter your department name : "),
                               mobile=input("Enter your mobile number : +88"))
student2.details()
student3 = Student_information(name=input("Enter your name : "), id=input("Enter your ID : "),
                               department=input("What's your department name?\n: "),
                               mobile=input("Enter your mobile number : +88"))
student3.details()
