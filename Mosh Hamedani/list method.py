numbers = [10, 15, 25, 12, 9]
numbers.append(22)
print(numbers)
numbers.insert(1, 99)
print(numbers)
numbers.remove(22)
print(numbers)
numbers.clear()
print(numbers)
print(f"Let's clear this list {numbers.clear()}")
numbers = [10, 15, 25, 12, 9]
numbers.pop()
print(numbers)
print(50 in numbers)            #numbers.index(14)
print(15 in numbers)
print(numbers)
numbers.insert(2, 32)
numbers.append(47)
print(47 in numbers)
print(numbers.count(47))
print(numbers)
numbers.insert(5, 10)
print(numbers)
print(numbers.count(10))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.index(12))
numbers2 = numbers.copy()
numbers.append(27)
print(numbers2)
print(numbers)
#write a program to duplicates in a list
random = [10, 12, 14, 10, 9, 8, 14, 8, 16, 15, 21, 19, 16]
print(f"Random duplicates numbers: \n{random}")
unique = []
for number in random:
    if number not in unique:
        unique.append(number)
print(f"All unique number has given below:\n{unique}")