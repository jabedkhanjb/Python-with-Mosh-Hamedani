for x in range(3):
    for y in range(3):
        print(f"{x},{y}")

numbers = [8, 2, 8, 2, 2]
for asterisk in numbers:
    output = ''
    for count in range(asterisk):
        output = output + "#"
    print(output)