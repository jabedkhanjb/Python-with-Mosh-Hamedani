from pathlib import Path as jabedkhanjb
# Absolute path
    # a path from our hard disk c:/Local disk/user/python project
# Relative path
   # current folder directory file

newpath = jabedkhanjb("ecommerce")
print(newpath.exists())

anotherpath = jabedkhanjb("Emails")
print(anotherpath.mkdir())
print(anotherpath.rmdir())

onemorepath = jabedkhanjb()
for file in onemorepath.glob("*.py"):
    print(file)

print("\n\nHere are another execution: ")

for file in onemorepath.glob("*"):
    print(file)