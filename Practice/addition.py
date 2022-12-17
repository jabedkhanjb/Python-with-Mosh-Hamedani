value = int(input("Insert a value > "))
value2 = int(input("Insert another value > "))
result = value + value2
print(f"Here is the total value is {result}")

print("Find out the largest number")

numbers = [10, 15, 13, 14]
higher = numbers[0]

for high in numbers:
    if high > higher:
        higher = high
print(f"{higher} is the largest number.")