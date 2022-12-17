semester = str(2)
year = str(22)
dept = "CSE"
number = "0001"

print(f"My id is: {semester+year+dept+number}\n")

print("Enter number:")
num1 = input("> ")
print("Our data type is ", type(num1))
print("Enter another number:")
num2 = input("> ")
print("Our data type is ", type(num2))

addition = int(num1) + int(num2)
subtract = int(num1) - int(num2)
multiply = int(num1) * int(num2)
division = int(num1) / int(num2)

print(f"Here our addition value is {addition}, "
      f"subtraction value is {subtract}, "
      f"multiplication value is {multiply}, "
      f"and division value is {division}")

