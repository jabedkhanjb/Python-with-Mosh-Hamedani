#problem, write a program to find out the largest number in a list

numbers = [10, 5, 9, 15, 32, 16, 18, 20, 25, 35]
higher = numbers[0]
for value in numbers:
    if value > higher:
        higher = value
print(higher)

numbers = [10, 12, 15, 18, 13, 17]
larger = numbers[0]
print(f"let's see first value {larger}")
for value in numbers:
    if value > larger:
        larger = value
print(larger)
