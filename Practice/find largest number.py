print("Assign value in this variable: ")
numbers = [int(input("> ")), int(input("> ")), int(input("> ")), int(input("> ")), int(input("> ")), ]
large = numbers[0]
print("let's see the large = number[0] value: ", large)
for find in numbers:
    if find > large:
        large = find
        print("in if condition: ", large)
    print("along if condition: ", find, large)
print("Out of if condition: ", large)