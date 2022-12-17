s_name = str(input("Enter the student name: "))
course = ["Visual Programming", "Database Management System", "Operating System"]
print(type(course))
print("Please input your academic marks according to the course name.\n")
t_number = 0
for name in course:
    print(name, ": ", end="")
    marks = float(input())
    t_number += marks
compare_OS = course[2] = marks
lownumber = course[1] = marks
avg = t_number / 3
print("Your Total marks is %.2f "% avg)

# Highest number in OS
print(f"{s_name}'s marks in Operating System is", compare_OS)

s2_name = str(input("\nEnter the student name: "))
course2 = ["Visual Programming", "Database Management System", "Operating System"]
print("Please input your academic marks according to the course name.\n")
for name in course2:
    print(name, ": ", end="")
    marks2 = float(input())
    t_number += marks2
compare_OS2 = course2[2] = marks2
lownumber2 = course2[1] = marks2
avg = t_number / 3
print("Your Total marks is %.2f " % avg)

# Highest number in OS
print(f"{s2_name}'s marks in Operating System is", compare_OS2)

s3_name = str(input("\nEnter the student name: "))
course3 = ["Visual Programming", "Database Management System", "Operating System"]
print("Please input your academic marks according to the course name.\n")
for name in course3:
    print(name, ": ", end="")
    marks3 = float(input())
    t_number += marks3
compare_OS3 = course3[2] = marks3
lownumber3 = course2[1] = marks3
avg = t_number / 3
print("Your Total marks is %.2f " % avg)

# Highest number in OS
print(f"{s3_name}'s marks in Operating System is", compare_OS3)

# maxnumberComparing = max(compare_OS , compare_OS2 , compare_OS3)
# print(maxnumberComparing)

print("\n")

highest_mark = topper = max(compare_OS, compare_OS2, compare_OS3)
if topper == marks:
    print(f"{s_name}'s highest marks in operating system is ", highest_mark)
elif topper == marks2:
    print(f"{s2_name}'s highest marks in operating system is ", highest_mark)
elif topper == marks3:
    print(f"{s3_name}'s highest marks in operating system is ", highest_mark)

lowest_marks = lower = min(lownumber, lownumber2, lownumber3)
if lower == marks:
    print(f"{s_name}'s lowest marks in Database Management system is ", lowest_marks)
elif lower == marks2:
    print(f"{s2_name}'s lowest marks in Database Management system is ", lowest_marks)
elif lower == marks3:
    print(f"{s3_name}'s lowest marks in Database Management system is ", lowest_marks)

