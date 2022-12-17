# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
# john = Person("Jabed Khan")
# john.talk()
#
# bob = Person("Mahfuz Islam")
# bob.talk()
# class LetsTalk:
#     def __init__(self, name):
#         self.person = name
#     def greetings(self):
#         print(f"Hi this is {self.person}")
#
#
# call = LetsTalk("Jabed")
# call.greetings()
class Chat:
    def __init__(self, x):
        self.fname = x
        #self.lname = y

    def talk(self):
        print(f"Hi, This is {self.fname}")

result = Chat("Jabed")
result.talk()

passed = Chat("Hammie")
passed.talk()