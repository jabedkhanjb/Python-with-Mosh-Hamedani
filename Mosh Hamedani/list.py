names = ['Jabed', 'Rafi', 'Mohin', 'Emon', 'Raju', 'Rakib', 'Shoyeb', 'Nuhas', 'Mahi']
names = ['Jabed', 'Fahim', 'Taiyub mama', 'Shohid mama', 'Sharif mama']
import random
number = random.randint(0, 9)
USA = random.randint(0, 4)
print("Let's see who is going to the USA this year: ")
print(names[USA])

print("\n\nwrite a program that can find out the largest number from the list\n")
numbers = [10, 5, 9, 15, 32, 16, 18, 20, 25, 35]
print(max(numbers))

value = [10, 25, 35, 75, 65]
max = value[0]
for new in value:
    if new > max:
        max = new
print(max)