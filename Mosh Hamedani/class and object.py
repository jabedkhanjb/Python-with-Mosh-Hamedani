class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


jb = Person("Jabed Khan", 19)
print(jb.name)
print(jb.age)

# Insert a function that prints a greeting, and execute it on the "  " object:

class People:
    def __init__(self, pronoun, old):
        self.person_name = pronoun
        self.person_age = old

    def greetings(self):
        print("Hello, Good Morning\nThis is " + self.person_name)

jbjb = People("Jabed Khan JB", 19)
jbjb.greetings()

class CSE:
    def __init__(computer, cse, ict):
        computer.dept_of_cse = cse
        computer.deft_of_ict = ict

    def science_dept(alldept):
        print("\n\nHello, Welcome to our department of " + alldept.dept_of_cse + alldept.deft_of_ict)

jabedkhanjb = CSE("Computer Science and Engineering", "\nDept of CSE")
jabedkhanjb.science_dept()