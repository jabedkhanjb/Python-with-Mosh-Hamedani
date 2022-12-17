numbers = [10, 1, 5, 7, 2, 6, 10, 4, 9, 3, 8]
numbers.reverse()
print(f"Sorting list {numbers}")
numbers.sort()
print(f"Reverse list {numbers}")
print(f"Counting if 10 is in twice: \n> {numbers.count(10)}") #count is basically an inline code
numbers.append(15)
print(numbers)
numbers.remove(10)
print(numbers)
print("Number is in index", numbers.index(15)) #here by inputing a certain number we will get its index location
numbers.insert(10, 11)
print(numbers)
print(numbers.pop()) #when pop() as like null, it will print the last value
print(numbers)
print(numbers.pop(10)) #when you input a number of its sequence, it will print its 2nd value which will be considered its last value
print(numbers)
print(numbers.pop())
random = [10, 12, 14, 10, 9, 8, 14, 8, 16, 15, 21, 19, 16]
print(f"There are a bunch of duplicate numbers included in this list has given below.\n{random}")
unique = []
print(unique)
for number in random:
    print("Here are the first number is", number)
    if number not in unique:
        print(number, "is not in", unique)
        unique.append(number)
        print("We are saving the number:", unique)
    else:
        print(number, "has taken already. we don't allow duplicate numbers.")
print(f"So we got all unique numbers which are {unique}")
unique.sort()
print(f"Now we gonna sort it in a sequence as below: \n{unique}")