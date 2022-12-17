# class Mammal:
#     def walk(self):
#         print("Let's do some code.")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("Stop yelling without knowing anything.")
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1 = Dog()
# dog1.bark()
class Mammal:
    def walk(self):
        print("Dog is running")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

result = Dog()
result.walk()

class Jabed:
    def ambition(self):
        print("What's your ambition?")

class student1(Jabed):
    def stu1(self):
        print("I want to be a Software Engineer")

class student2(Jabed):
    def stu2(self):
        print("I wanna be the master of Programming Language")

finalresult = student1()
finalresult.ambition()
finalresult.stu1()

finalresult2 = student2()
finalresult2.ambition()
finalresult2.stu2()