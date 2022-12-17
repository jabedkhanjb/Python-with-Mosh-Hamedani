#if name is less than 3 characters long,
#    name must be at least 3 characters
#otherwise if it's more than 50 characters long,
#    name can be a maximum of 50 characters
#otherwise
#   name looks good

name = input("Enter your name:\n")

if len(name) <= 3:
    print("Warning!!\nName must be at least 4 characters.")
elif len(name) > 20:
    print("Alert!!\nName can be a maximum of 20 characters.")
else:
    print("Name Looks good")