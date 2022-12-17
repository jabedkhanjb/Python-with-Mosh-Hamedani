print("Enter the 3 students names where one will stand first in this semester: ")
names = [str(input("> ")), str(input("> ")), str(input("> "))]
import random
result = random.randint(0, 2)
print(f"Congratulation, {names[result]} will stand first in this semester.")
