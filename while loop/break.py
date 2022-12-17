number = input("Enter a number: ")
text = input("Enter something to print out in this loop:\n")
i = 1
while i < int(number):
    print(text)
    if i == 5:
        break
    i += 1