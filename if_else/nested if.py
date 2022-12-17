a = input("Enter the marks of roll four: ")
#x = input("Enter your marks: ")
x = 86
print("Dear Student, You Obtained 86 number")
#print("X = ", x)

if x > int(a):
    print("Congratulations!!!!!!!!!\nyour position number is 4")
    b = input("Enter the marks of roll three: ")
    if x > int(b):
        print("Once more Congratulations...\nYour position number is 3")
        c = input("Enter the marks of roll two: ")
        if x > int(c):
            print("Bravo Bravo........!!\nHappy to let your know your 2nd position on this Semester.")
            d = input("Enter the marks of roll one: ")
            if x < int(d):
                print("SORRY.....!\nYou didn't stood first.")
                import time
                time.sleep(5)
                print("Dear Student,\nWe appreciate your hard working.\nYour dedication could have "
                      "reached you in number one position. \nUnfortunately you didn't stood first. \njust because "
                      "there are more talented student here for being your competitor."
                      "\nGood Luck"
                      "\nExamination Team")

else:
    print("Work hard & pay attention on your education")