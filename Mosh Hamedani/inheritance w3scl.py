class Person:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname

    def printname(self):
        print(self.fname, self.lname)

yourname = Person("Jabed", "Khan")
yourname.printname()

# Parent class and child class
class Parent:
    def __init__(self, fparent, lparent):
        self.parent_one = fparent
        self.parent_two = lparent

    def represent(self):
        print(self.parent_one, self.parent_two)

class Child(Parent):
    def __init__(self, fparent, lparent):
        Parent.__init__(self, fparent, lparent)

xyz = Child("Mahfuz", "Islam")
xyz.represent()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) #in this line, we are using super(). it do automatically inherits all the
      #methods and properties from its Parent class

x = Student("Mike", "Olsen")
x.printname()

# add properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

# here is an example
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Jabedkhan", "JB", 2019)
print(x.firstname, x.lastname, x.graduationyear)

# add methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear, "in CSE Department of TMU")

x = Student("Jabed", "Khan", 2020)
x.welcome()

# alternatives of add methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


